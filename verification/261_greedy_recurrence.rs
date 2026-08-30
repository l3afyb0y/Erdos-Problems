//! Exact finite checker for the greedy recurrence in Erdős problem 261.
//!
//! For a target `n`, the desired finite identity is
//!
//!     n / 2^n = sum(a / 2^a),
//!
//! where the selected indices `a` are distinct. Positivity forces every
//! selected index past `n`. At index `a`, scale the unrepresented remainder by
//! `2^a` and call the resulting integer `r`. The greedy decision and update are
//! then exact:
//!
//!     omit a   when r < a:  r <- 2*r
//!     include a when r >= a: r <- 2*(r-a)
//!
//! Equivalently, `r <- 2*(r mod a)`. The initial state is `a = n+1` and
//! `r = 2*n`. For `n >= 2`, reaching zero produces a representation with at
//! least two terms. The greedy sweep starts at `n = 2`; target `n = 1` is handled
//! separately by the exact witness `(3, 6, 8)`, because its greedy trajectory is
//! only the inadmissible one-term identity `1/2 = 2/4`. Failing to reach zero
//! before the supplied step limit is reported as unresolved, never as a
//! counterexample.

use std::env;
use std::process::ExitCode;

#[derive(Clone, Copy, Debug)]
struct Outcome {
    steps: u64,
    stopping_index: u64,
    selected_terms: u64,
    last_selected_index: u64,
    terminated: bool,
}

fn trajectory(target: u64, step_limit: u64) -> Outcome {
    let mut index = target.checked_add(1).expect("target is too large");
    let mut remainder = target.checked_mul(2).expect("target is too large");
    let mut steps = 0;
    let mut selected_terms = 0;
    let mut last_selected_index = 0;

    while remainder != 0 && steps < step_limit {
        debug_assert!(remainder / 2 < index);
        if remainder >= index {
            selected_terms += 1;
            last_selected_index = index;
        }
        remainder = (remainder % index)
            .checked_mul(2)
            .expect("remainder overflowed");
        index = index.checked_add(1).expect("index overflowed");
        steps += 1;
    }

    Outcome {
        steps,
        stopping_index: index,
        selected_terms,
        last_selected_index,
        terminated: remainder == 0,
    }
}

fn parse_u64(label: &str, value: Option<String>) -> Result<u64, String> {
    let value = value.ok_or_else(|| format!("missing {label}"))?;
    value
        .parse::<u64>()
        .map_err(|error| format!("invalid {label} {value:?}: {error}"))
}

fn run() -> Result<(), String> {
    let mut args = env::args().skip(1);
    let bound = parse_u64("bound", args.next())?;
    let step_limit = parse_u64("step limit", args.next())?;
    if args.next().is_some() {
        return Err("usage: 261_greedy_recurrence BOUND STEP_LIMIT".to_owned());
    }
    if bound < 2 || step_limit == 0 {
        return Err("BOUND must be at least 2 and STEP_LIMIT must be positive".to_owned());
    }

    let mut longest = Outcome {
        steps: 0,
        stopping_index: 0,
        selected_terms: 0,
        last_selected_index: 0,
        terminated: true,
    };
    let mut longest_target = 0;
    let mut most_terms = longest;
    let mut most_terms_target = 0;
    let mut furthest_index = 0;
    let mut furthest_target = 0;

    for target in 2..=bound {
        let outcome = trajectory(target, step_limit);
        if !outcome.terminated {
            println!(
                "unresolved target={target} step_limit={step_limit} current_index={}",
                outcome.stopping_index
            );
            return Err("the finite sweep hit its explicit step limit".to_owned());
        }
        if outcome.steps > longest.steps {
            longest = outcome;
            longest_target = target;
        }
        if outcome.selected_terms > most_terms.selected_terms {
            most_terms = outcome;
            most_terms_target = target;
        }
        if outcome.stopping_index > furthest_index {
            furthest_index = outcome.stopping_index;
            furthest_target = target;
        }
    }

    println!("checked_targets=2..={bound}");
    println!("boundary_target_1_witness=3,6,8");
    println!("step_limit_per_target={step_limit}");
    println!(
        "longest_trajectory_target={longest_target} steps={} stopping_index={}",
        longest.steps, longest.stopping_index
    );
    println!(
        "most_terms_target={most_terms_target} selected_terms={} last_selected_index={}",
        most_terms.selected_terms, most_terms.last_selected_index
    );
    println!("furthest_stopping_index_target={furthest_target} stopping_index={furthest_index}");
    println!("result=all_checked_trajectories_terminated");
    Ok(())
}

fn main() -> ExitCode {
    match run() {
        Ok(()) => ExitCode::SUCCESS,
        Err(message) => {
            eprintln!("error: {message}");
            ExitCode::FAILURE
        }
    }
}

#[cfg(test)]
mod tests {
    use super::trajectory;

    #[test]
    fn consecutive_block_seed_terminates_at_six() {
        let outcome = trajectory(4, 100);
        assert!(outcome.terminated);
        assert_eq!(outcome.selected_terms, 2);
        assert_eq!(outcome.last_selected_index, 6);
    }

    #[test]
    fn target_one_uses_a_separate_non_greedy_witness() {
        let outcome = trajectory(1, 100);
        assert!(outcome.terminated);
        assert_eq!(outcome.selected_terms, 1);
        assert_eq!(outcome.last_selected_index, 2);

        let common_exponent = 8;
        let target = 1_u64 << (common_exponent - 1);
        let term_3 = 3_u64 << (common_exponent - 3);
        let term_6 = 6_u64 << (common_exponent - 6);
        let term_8 = 8_u64 << (common_exponent - 8);
        assert_eq!(term_3 + term_6 + term_8, target);
    }

    #[test]
    fn explicit_limit_is_not_reported_as_termination() {
        let outcome = trajectory(56, 100);
        assert!(!outcome.terminated);
        assert_eq!(outcome.steps, 100);
    }

    #[test]
    fn reproduces_published_peak_trajectories() {
        let expected = [
            (56, 6_092, 12_230),
            (3_113, 13_370, 29_752),
            (3_817, 76_072, 155_942),
            (5_588, 226_913, 460_536),
        ];
        for (target, selected_terms, last_selected_index) in expected {
            let outcome = trajectory(target, 1_000_000);
            assert!(outcome.terminated);
            assert_eq!(outcome.selected_terms, selected_terms);
            assert_eq!(outcome.last_selected_index, last_selected_index);
        }
    }
}

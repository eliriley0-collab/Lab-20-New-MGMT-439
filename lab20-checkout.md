# Lab 20 — Project 2 Readiness

## Partner cold run

- Repository link:
- README command followed: `python3 project2_results.py`
- First failure, or clean run: Clean run. The partner followed the README and reported no failures.
- Elapsed time: 1 minute.
- Location of result: `project2_results.json` at the repository root, as documented in the README.

## Locked Changed-Input Record

Complete the prediction with AI closed. Commit and push it before running the changed input.

- Input, old value and new value with units: SPY expected annual return, from 14.11% to 5.00% (full-history baseline).
- Expected direction of change in the decision numbers:
- Expected effect on the decision:

After the run, add the following.

- Prediction commit link:
- Before output link and decision numbers: [Saved project baseline](../project2_results.json) — 15% SPY / 85% BIL, 5.17% estimated annual return, 2.46% estimated annual volatility. Confirm these match the before run.
- After output link and decision numbers: [Local SPY-change verification](../spy-changed-input.md). Original allocation: 3.81% estimated annual return. Reoptimized allocation: 5.18% estimated annual return.
- Did the verdict change? The original allocation fails the 5.00% objective. The local search still finds a qualifying mix by replacing SPY with VOO.
- Why did the result match or differ from the prediction?

## Fix and partner rerun

- No fix or rerun needed. The first cold run was clean.

## Committee decision

Adopt the 15% SPY / 85% BIL starting allocation. Reject that allocation if BIL’s estimated annual return falls by 1 percentage point.

## Open items and checkout links

- Unresolved items: No pre-run prediction commit was available for the proposed SPY change. The student reported a missed objective in the app. If the app displayed no qualifying mix under Current inputs, the settings or output need confirmation.
- Markdown, Python and other GitHub file links:

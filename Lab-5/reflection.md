# Static analysis reflection

## Which issues were easiest and hardest to fix?

Spacing around an assignment or comma had one local fix. Review identifiers required a design decision: concatenation makes different title/review pairs indistinguishable before hashing. Encoding the pair as JSON preserves its boundary. The new IDs are intentionally longer.

## Did the tools report a false positive?

B104 flagged the wildcard address. The demo prints it and never opens a socket, so no network listener was exposed during the run. A loopback default makes a later local listener safer. B311 also had limited consequence here because the featured title carries no access privilege.

## How would these checks fit into development?

Run Flake8 before committing, then run Pylint and Bandit on the changed module in CI with the demo assertions. Review each security finding in context before deciding whether a code or configuration change is needed.

## What changed in measurable terms?

Pylint improved from 5.47 to 10.00. Bandit went from four findings to zero, and Flake8 from four to zero. The same three average ratings (4.5, 2.0 and 4.0) and top-two ranking were preserved. Independent boards now isolate their catalogues.

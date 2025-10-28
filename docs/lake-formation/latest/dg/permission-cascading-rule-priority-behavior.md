# Rule priority behavior

- When Lake Formation detects an _identical tag policy_, it only evaluates **Rule #1** (grantable permissions)
- When the tag policy is _different_, it evaluates **Rule #2** (DESCRIBE permissions)

# Validation and analysis overview

## Cedar validation (static analysis)

Cedar validation performs static analysis to ensure policies are syntactically
correct and comply with the schema:

- **Syntax correctness** — Verifies Cedar
  policy language syntax
- **Schema compliance** — Checks that policies
  reference valid actions (tools), use correct data types, and access only
  defined context fields
- **Type safety** — Ensures parameter types
  match the gateway's tool definitions

## Cedar analysis (automated reasoning)

Cedar analysis uses automated reasoning to detect potential security and logic
issues:

- **Overly permissive policies** — If
  created, the policy engine will allow all requests for the specified
  principal, action, and resource combination
- **Overly restrictive policies** — If
  created, the policy engine will deny all requests for the specified
  principal, action, and resource combination

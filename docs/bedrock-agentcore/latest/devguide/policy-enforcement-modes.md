# Policy enforcement modes

Enforcement mode defines how the gateway applies policy decisions. The policy engine
supports two modes:

- In `LOG_ONLY` mode, the policy engine evaluates and logs whether
  the action is would be allowed or denied without enforcing the the
  decision
- In `ENFORCE` mode, the policy engine evaluates the action and
  enforces decisions by allowing or denying agent operations.

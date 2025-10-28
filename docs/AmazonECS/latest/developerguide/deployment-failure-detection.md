# Amazon ECS deployment failure detection

Amazon ECS provides two methods for detecting deployment failures:

- Deployment Circuit Breaker
- CloudWatch Alarms
  Both methods can be configured to automatically roll back failed deployments to the last known good state.

Consider the following:

- Both methods only support rolling update deployment and blue/green deployment
  types.
- When both methods are used, either can trigger deployment failure.
- The rollback method requires a previous deployment in COMPLETED state.
- EventBridge events are generated for deployment state changes.

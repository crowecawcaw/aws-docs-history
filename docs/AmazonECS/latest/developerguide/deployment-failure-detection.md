

# Amazon ECS deployment failure detection
<a name="deployment-failure-detection"></a>

Amazon ECS provides two methods for detecting deployment failures:
+ Deployment Circuit Breaker
+ CloudWatch Alarms

You can configure both methods to automatically roll back failed deployments to the last known good state.

Consider the following:
+ Both methods only support rolling update deployment and blue/green deployment types.
+ When a service uses early success criteria, the deployment circuit breaker and CloudWatch alarm rollback apply until Amazon ECS completes the deployment. After the deployment completes, they no longer roll back the service. For more information, see [Complete Amazon ECS rolling deployments early with early success criteria](early-success-criteria.md).
+ When both methods are used, either can trigger deployment failure.
+ The rollback method requires a previous deployment in COMPLETED state.
+ EventBridge events are generated for deployment state changes.
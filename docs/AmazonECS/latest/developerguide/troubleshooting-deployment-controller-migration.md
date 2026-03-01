# Troubleshooting Amazon ECS deployment strategy updates

This section provides solutions for common issues you might encounter when migrating
deployment strategies.

## Multiple service revisions or tasks sets

The following issues relate to having multiple service revisions for a deployment.

Multiple task sets when updating ECS deployment controller

_Error message_: `Updating the deployment controller is
 not supported when there are multiple tasksets in the service. Please ensure your
 service has only one taskset and try again.`

_Solution_: This error occurs when attempting to change the
deployment controller type of a service with multiple active task sets. To resolve this
issue for the `CODE_DEPLOY` or `EXTERNAL` deployment
controller:

1. Check current task sets:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].taskSets"
```

2. Wait for any in-progress deployments to complete.
3. Force a new deployment to clean up task sets:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --force-new-deployment
```

4. If necessary, delete extra task sets manually:

```
aws ecs delete-task-set --cluster `your-cluster-name` --service `your-service-name` --task-set `task-set-id`
```

5. After only one task set remains, retry updating the deployment
   controller.

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

Missing primary task set when updating `ECS` deployment controller

_Error message_: `Updating the deployment controller
 requires a primary taskset in the service. Please ensure your service has a primary
 taskset and try again.`

_Solution_: This error occurs when attempting to change the
deployment controller type of a service that doesn't have a primary task set. To
resolve this issue:

1. Verify the service status and task sets. ). If a task set exists in the
   service, it should be marked as `ACTIVE`.

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].taskSets[*].[status,id]
```

If there are no task sets in the `ACTIVE` state, migrate the deployment. For more information, see [Migration approaches](migrate-codedeploy-to-ecs-bluegreen.md#migration-paths "migrate-codedeploy-to-ecs-bluegreen.md#migration-paths"). 2. If the service has no running tasks, deploy at least one task by updating the
service:

```
aws ecs update-service-primary-task-set --cluster `your-cluster-name` --service `your-service-name` --primary-task-set your-taskset-id
```

This will mark the (previously `ACTIVE`) task set in the service as
`PRIMARY` status. 3. Wait for the task to reach a stable running state. You can check the status
with:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].deployments"
```

4. After the service has a primary task set with running tasks, retry updating
   the deployment controller.

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

## Mismatch between the deployment failure detection type and deployment controller

The following issues relate to a mismatch between the deployment failure detection type
and deployment controller.

Deployment circuit breaker with non-ECS controller

_Error message_: `Deployment circuit breaker feature is only
 supported with ECS deployment controller. Update to ECS deployment controller and try
 again.`

_Solution_: This error occurs when attempting to enable the
deployment circuit breaker feature on a service that is not using the `ECS`
deployment controller. The deployment circuit breaker is only compatible with the
`ECS`deployment controller.

1. Check your service's current deployment controller:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].deploymentController"
```

2. Update your service to use the `ECS` deployment controller:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-controller type=ECS
```

3. After the service is using the `ECS` deployment controller, enable
   the deployment circuit breaker:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-configuration "deploymentCircuitBreaker={enable=true,rollback=true}"
```

For more information, see [How the Amazon ECS deployment circuit breaker detects failures](deployment-circuit-breaker.md "deployment-circuit-breaker.md").

Alarm-based rollback with non-ECS controller

_Error message_: `Alarm based rollback feature is only
 supported with ECS deployment controller. Update to ECS deployment controller and try
 again.`

_Solution_: This error occurs when attempting to configure
alarm-based rollback on a service that is not using the `ECS` deployment
controller. The alarm-based rollback feature is only compatible with the
`ECS` deployment controller.

1. Check your service's current deployment controller:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].deploymentController"
```

2. Update your service to use the `ECS` deployment controller:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-controller type=ECS
```

3. After the service is using the `ECS` deployment controller, configure
   alarm-based rollback:

```
aws ecs update-service --cluster `your-cluster-name` --services `your-service-name` --deployment-configuration "alarms={alarmNames=[your-alarm-name],enable=true,rollback=true}"
```

For more information, see [How CloudWatch alarms detect Amazon ECS deployment failures](deployment-alarm-failure.md "deployment-alarm-failure.md").

## Mismatch between Service Connect and the deployment controller

The following issues relate to a mismatch between Service Connect and the deployment
controller.

`EXTERNAL` controller with Service Connect

_Error message_: `The EXTERNAL deployment controller type is
 not supported for services using Service Connect.`

_Solution_: This error occurs when attempting to use the
`EXTERNAL` deployment controller with an service that has Service Connect
enabled. The `EXTERNAL` controller is not compatible with
Service Connect.

1. Check if your service has Service Connect enabled:

```
aws ecs describe-services --cluster `your-cluster-name` --services your-service-name --query "services[0].serviceConnectConfiguration"
```

2. If you need to use the `EXTERNAL` deployment controller, disable
   Service Connect by updating your service:

```
aws ecs update-service --cluster your-cluster-name --service your-service-name --service-connect-configuration "{}"
```

3. Alternatively, if you must use Service Connect, use the `ECS`
   deployment controller instead:

```
aws ecs update-service --cluster your-cluster-name --service your-service-name --deployment-controller type=ECS
```

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

Service Connect with non-ECS controller

_Error message_: `Service Connect feature is only supported
 with ECS (rolling update) deployment controller. Update to ECS deployment controller
 and try again.`

_Solution_: This error occurs when attempting to enable
Service Connect on a that is not using the `ECS` deployment controller. The
Service Connect feature is only compatible with the `ECS` deployment
controller.

1. Check your service's current deployment controller:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].deploymentController"
```

2. Update your service to use the ECS deployment controller:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-controller type=ECS
```

3. Once the service is using the ECS deployment controller, enable Service
   Connect:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --service-connect-configuration "enabled=true,namespace=your-namespace"
```

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

## Mismatch between controller type and scheduling strategy

The following issues relate to a mismatch between controller type and scheduling
strategy.

`CODE_DEPLOY` controller with `DAEMON` scheduling
strategy

_Error message_: `The CODE_DEPLOY deployment controller type
 is not supported for services using the DAEMON scheduling strategy.`

_Solution_: This error occurs when attempting to use the
CODE_DEPLOY deployment controller with a service that uses the `DAEMON`
scheduling strategy. The `CODE_DEPLOY` controller is only compatible with the
`REPLICA` scheduling strategy.

1. Check your service's current scheduling strategy:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].schedulingStrategy"
```

2. If you need blue/green deployments, change your service to use the
   `REPLICA` scheduling strategy:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --scheduling-strategy REPLICA
```

3. Alternatively, if you must use the `DAEMON` scheduling strategy, use
   the `ECS` deployment controller instead:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-controller type=ECS
```

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

EXTERNAL controller with DAEMON scheduling strategy

_Error message_: `The EXTERNAL deployment controller type is
 not supported for services using the DAEMON scheduling strategy.`

_Solution_: This error occurs when attempting to use the EXTERNAL
deployment controller with an ECS service that uses the DAEMON scheduling strategy. The
EXTERNAL controller is only compatible with the REPLICA scheduling strategy.

1. Check your service's current scheduling strategy:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].schedulingStrategy"
```

2. If you need to use the `EXTERNAL` deployment controller, change your
   service to use the `REPLICA` scheduling strategy:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --scheduling-strategy REPLICA
```

3. Alternatively, if you must use the `DAEMON` scheduling strategy, use
   the `ECS` deployment controller instead:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --deployment-controller type=ECS
```

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

Service registries with external launch type

_Error message_: `Service registries are not supported for external launch type.`

_Solution_: This error occurs when attempting to configure
service discovery (service registries) for a service that uses the `EXTERNAL`
launch type. Service discovery is not compatible with the `EXTERNAL` launch
type.

1. Check your service's current launch type:

```
aws ecs describe-services --cluster `your-cluster-name` --services `your-service-name` --query "services[0].launchType"
```

2. If you need service discovery, change your service to use either the
   `EC2` or `FARGATE` launch type:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --launch-type FARGATE
```

3. Alternatively, if you must use the `EXTERNAL` launch type, remove the
   service registry configuration:

```
aws ecs update-service --cluster `your-cluster-name` --service `your-service-name` --service-registries "[]"
```

For more information, see [Amazon ECS service deployment controllers and strategies](ecs_service-options.md "ecs_service-options.md").

## Revert a deployment controller update

If you decide that you want to return to the previous deployment controller, you can do one of the following:

- If you used CloudFormation, you can use the previous template to create a new stack. For more
  information, see [Create a stack
  from](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") in the _CloudFormation User Guide_.
- If you used the Amazon ECS console, or the AWS CLI, you can update the service. For more
  information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").

If you use the update-service command, use the `--deployment-controller`
option and set it to the previous deployment controller.

# How the Amazon ECS deployment circuit breaker

detects failures

The deployment circuit breaker is the rolling update mechanism that determines if the
tasks reach a steady state. The deployment circuit breaker has an option that will
automatically roll back a failed deployment to the deployment that is in the
`COMPLETED` state.

When a service deployment changes state, Amazon ECS sends a service deployment state change
event to EventBridge. This provides a programmatic way to monitor the status of your service
deployments. For more information, see [Amazon ECS service deployment state change
events](ecs_service_deployment_events.md "ecs_service_deployment_events.md"). We recommend that you create and
monitor an EventBridge rule with an `eventName` of
`SERVICE_DEPLOYMENT_FAILED` so that you can take manual action to start
your deployment. For more information, see [Getting started with
EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_.

When the deployment circuit breaker determines that a deployment failed, it looks for
the most recent deployment that is in a `COMPLETED` state. This is the
deployment that it uses as the roll-back deployment. When the rollback starts, the
deployment changes from a `COMPLETED` to `IN_PROGRESS`. This means
that the deployment is not eligible for another rollback until it reaches a
`COMPLETED` state. When the deployment circuit breaker does not find a
deployment that is in a `COMPLETED` state, the circuit breaker does not
launch new tasks and the deployment is stalled.

When you create a service, the scheduler keeps track of the tasks that failed to
launch in two stages.

- Stage 1 - The scheduler monitors the tasks to see if they transition into the
  RUNNING state.
  - Success - The deployment has a chance of transitioning to the
    COMPLETED state because there is more than one task that transitioned to
    the RUNNING state. The failure criteria is skipped and the circuit
    breaker moves to stage 2.
  - Failure - There are consecutive tasks that did not transition to the
    RUNNING state and the deployment might transition to the FAILED state.

- Stage 2 - The deployment enters this stage when there is at least one task in
  the RUNNING state. The circuit breaker checks the health checks for the tasks in
  the current deployment being evaluated. The validated health checks are
  Elastic Load Balancing, AWS Cloud Map service health checks, and container health checks.

      + Success - There is at least one task in the running state with health
       checks that have passed.
      + Failure - The tasks that are replaced because of health check failures
       have reached the failure threshold.

  Consider the following when you use the deployment circuit breaker method on a
  service. EventBridge generates the rule.

- The `DescribeServices` response provides insight into the state of
  a deployment, the `rolloutState` and `rolloutStateReason`.
  When a new deployment is started, the rollout state begins in an
  `IN_PROGRESS` state. When the service reaches a steady state, the
  rollout state transitions to `COMPLETED`. If the service fails to
  reach a steady state and circuit breaker is turned on, the deployment will
  transition to a `FAILED` state. A deployment in a `FAILED`
  state doesn't launch any new tasks.
- In addition to the service deployment state change events Amazon ECS sends for
  deployments that have started and have completed, Amazon ECS also sends an event when
  a deployment with circuit breaker turned on fails. These events provide details
  about why a deployment failed or if a deployment was started because of a
  rollback. For more information, see [Amazon ECS service deployment state change
  events](ecs_service_deployment_events.md "ecs_service_deployment_events.md").
- If a new deployment is started because a previous deployment failed and a
  rollback occurred, the `reason` field of the service deployment state
  change event indicates the deployment was started because of a rollback.
- The deployment circuit breaker is only supported for Amazon ECS services that use
  the rolling update (`ECS`) deployment controller.
- You must use the Amazon ECS console, or the AWS CLI when you use the deployment
  circuit breaker with the CloudWatch option. For more information, see [Create a service using defined
  parameters](create-service-console-v2.md#create-custom-service "create-service-console-v2.md#create-custom-service") and [create-service](../../../cli/latest/reference/ecs/create-service.md "../../../cli/latest/reference/ecs/create-service.md") in
  the _AWS Command Line Interface Reference_.
  The following `create-service` AWS CLI example shows how to create a Linux
  service when the deployment circuit breaker is used with the rollback option.

```
`aws ecs create-service \
 --service-name `MyService` \
 --deployment-controller type=`ECS` \
 --desired-count `3` \
 --deployment-configuration "deploymentCircuitBreaker={enable=`true`,rollback=`true`}" \
 --task-definition `sample-fargate:1` \
 --launch-type `FARGATE` \
 --platform-family `LINUX` \
 --platform-version `1.4.0` \
 --network-configuration "awsvpcConfiguration={subnets=[`subnet-12344321`],securityGroups=[`sg-12344321`],assignPublicIp=`ENABLED`}"`
```

Example:

Deployment 1 is in a `COMPLETED` state.

Deployment 2 cannot start, so the circuit breaker rolls back to Deployment 1.
Deployment 1 transitions to the `IN_PROGRESS` state.

Deployment 3 starts and there is no deployment in the `COMPLETED` state, so
Deployment 3 cannot roll back, or launch tasks.

## Failure threshold

The deployment circuit breaker calculates the threshold value, and then uses the
value to determine when to move the deployment to a `FAILED`
state.

The deployment circuit breaker has a minimum threshold of 3 and a maximum
threshold of 200. and uses the values in the following formula to determine the
deployment failure.

```
Minimum threshold <= 0.5 * `desired task count` => maximum threshold
```

When the result of the calculation is greater than the minimum of 3, but smaller
than the maximum of 200, the failure threshold is set to the calculated threshold
(rounded up).

###### Note

You cannot change either of the threshold values.

There are two stages for the deployment status check.

1.  The deployment circuit breaker monitors tasks that are part of the
    deployment and checks for tasks that are in the `RUNNING` state.
    The scheduler ignores the failure criteria when a task in the current
    deployment is in the `RUNNING` state and proceeds to the next
    stage. When tasks fail to reach in the `RUNNING` state, the
    deployment circuit breaker increases the failure count by one. When the
    failure count equals the threshold, the deployment is marked as
    `FAILED`.
2.  This stage is entered when there are one or more tasks in the
    `RUNNING` state. The deployment circuit breaker performs
    health checks on the following resources for the tasks in the current
    deployment:

        * Elastic Load Balancing load balancers
        * AWS Cloud Map service
        * Amazon ECS container health checks

    When a health check fails for the task, the deployment circuit breaker
    increases the failure count by one. When the failure count equals the
    threshold, the deployment is marked as `FAILED`.

The following table provides some examples.

| Desired task count | Calculation             | Threshold                                              |
| ------------------ | ----------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                  | `3 <= 0.5 * 1 => 200`   | 3 (the calculated value is less than the minimum)      |
| 25                 | `3 <= 0.5 * 25 => 200`  | 13 (the value is rounded up)                           |
| 400                | `3 <= 0.5 * 400 => 200` | 200                                                    |
| 800                | `3 <= 0.5 * 800 => 200` | 200 (the calculated value is greater than the maximum) | For example, when the threshold is 3, the circuit breaker starts with the failure count set at 0. When a task fails to reach the `RUNNING` state, the deployment circuit breaker increases the failure count by one. When the failure count equals 3, the deployment is marked as `FAILED`. For additional examples about how to use the rollback option, see [Announcing Amazon ECS deployment circuit breaker](https://aws.amazon.com/blogs/containers/announcing-amazon-ecs-deployment-circuit-breaker/ "https://aws.amazon.com/blogs/containers/announcing-amazon-ecs-deployment-circuit-breaker/"). |

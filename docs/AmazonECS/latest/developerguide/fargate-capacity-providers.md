# Amazon ECS clusters for Fargate

With Amazon ECS on AWS Fargate capacity providers, you can use both Fargate and Fargate Spot
capacity with your Amazon ECS tasks.

With Fargate Spot, you can run interruption tolerant Amazon ECS tasks at a rate
that's discounted compared to the Fargate price. Fargate Spot runs tasks on
spare compute capacity. When AWS needs the capacity back, your tasks are
interrupted with a two-minute warning.

When tasks that use the Fargate and Fargate Spot capacity providers are stopped,
the task state change event is sent to Amazon EventBridge. The stopped reason describes the
cause. For more information, see [Amazon ECS task state change events](ecs_task_events.md "ecs_task_events.md").

A cluster can contain a mix of Fargate and Auto Scaling group capacity
providers. However, a capacity provider strategy can only contain either
Fargate or Auto Scaling group capacity providers, but not both. For more
information, see [Auto Scaling Group Capacity Providers](cluster-auto-scaling.md#asg-capacity-providers "cluster-auto-scaling.md#asg-capacity-providers").

Consider the following when using capacity providers:

- You must associate a capacity provider with a cluster before you associate
  it with the capacity provider strategy.
- You can specify a maximum of 20 capacity providers for a capacity provider
  strategy.
- You can't update a service using an Auto Scaling group capacity provider to use a
  Fargate capacity provider. The opposite is also the case.
- In a capacity provider strategy, if no `weight` value is
  specified for a capacity provider in the console, then the default value of
  `1` is used. If using the API or AWS CLI, the default value of
  `0` is used.
- When multiple capacity providers are specified within a capacity provider
  strategy, at least one of the capacity providers must have a weight value
  that's greater than zero. Any capacity providers with a weight of zero
  aren't used to place tasks. If you specify multiple capacity providers in a
  strategy with all the same weight of zero, then any `RunTask` or
  `CreateService` actions using the capacity provider strategy
  fail.
- In a capacity provider strategy, only one capacity provider can have a
  defined _base_ value. If no base value is specified, the
  default value of zero is used.
- A cluster can contain a mix of both Auto Scaling group capacity providers and
  Fargate capacity providers. However, a capacity provider strategy can only
  contain Auto Scaling group, or Fargate capacity providers, but not both.
- A cluster can contain a mix of services and standalone tasks that use both
  capacity providers. A service can be updated to use a
  capacity provider strategy rather than a launch type. However, you must
  force a new deployment when doing so.

## Fargate Spot

termination notices

During periods of extremely high demand, Fargate Spot capacity might
be unavailable. This can cause Fargate Spot tasks to be delayed. When this
happens, Amazon ECS services retry launching tasks until the required capacity becomes
available. Fargate doesn't replace Spot capacity with on-demand capacity.

When tasks using Fargate Spot capacity are stopped due to a Spot
interruption, a two-minute warning is sent before a task is stopped. The
warning is sent as a task state change event to Amazon EventBridge and as a
SIGTERM signal to the running task. If you use Fargate Spot as part of
a service, then in this scenario the service scheduler receives the
interruption signal and attempts to launch additional tasks on
Fargate Spot if there's capacity available. A service with only one
task is interrupted until capacity is available. For more information
about a graceful shutdown, see [Graceful shutdowns with ECS](https://aws.amazon.com/blogs/containers/graceful-shutdowns-with-ecs/ "https://aws.amazon.com/blogs/containers/graceful-shutdowns-with-ecs/").

To ensure that your containers exit gracefully before the task stops, you can
configure the following:

- A `stopTimeout` value of `120` seconds or less
  can be specified in the container definition that the task is using. The
  default `stopTimeout` value is 30 seconds. You can specify a
  longer `stopTimeout` value to give yourself more time between
  the moment that the task state change event is received and the point in
  time when the container is forcefully stopped. For more information, see
  [Container timeouts](task_definition_parameters.md#container_definition_timeout "task_definition_parameters.md#container_definition_timeout").
- The SIGTERM signal must be received from within the container to
  perform any cleanup actions. Failure to process this signal results in
  the task receiving a SIGKILL signal after the configured
  `stopTimeout` and may result in data loss or
  corruption.

The following is a snippet of a task state change event. This snippet displays
the stopped reason and stop code for a Fargate Spot interruption.

```
{
  "version": "0",
  "id": "9bcdac79-b31f-4d3d-9410-fbd727c29fab",
  "detail-type": "ECS Task State Change",
  "source": "aws.ecs",
  "account": "111122223333",
  "resources": [
    "arn:aws:ecs:us-east-1:111122223333:task/b99d40b3-5176-4f71-9a52-9dbd6f1cebef"
  ],
  "detail": {
    "clusterArn": "arn:aws:ecs:us-east-1:111122223333:cluster/default",
    "createdAt": "2016-12-06T16:41:05.702Z",
    "desiredStatus": "STOPPED",
    "lastStatus": "RUNNING",
    **"stoppedReason": "Your Spot Task was interrupted.",
 "stopCode": "SpotInterruption",**
    "taskArn": "arn:aws:ecs:us-east-1:111122223333:task/b99d40b3-5176-4f71-9a52-9dbd6fEXAMPLE",
    ...
  }
}
```

The following is an event pattern that's used to create an EventBridge rule for Amazon ECS
task state change events. You can optionally specify a cluster in the
`detail` field. Doing so means that you will receive task state
change events for that cluster. For more information about creating an EventBridge rule, see [Getting started with
Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_.

```
{
    "source": [
        "aws.ecs"
    ],
    "detail-type": [
        "ECS Task State Change"
    ],
    "detail": {
        "clusterArn": [
            "`arn:aws:ecs:us-west-2:111122223333:cluster/default`"
        ]
    }
}
```

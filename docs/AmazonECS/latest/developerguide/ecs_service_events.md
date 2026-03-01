# Amazon ECS service action events

Amazon ECS sends service action events with the detail type **ECS Service
Action**. Unlike the container instance and task state change events,
the service action events do not include a version number in the
`details` response field. The following is an event pattern that is
used to create an EventBridge rule for Amazon ECS service action events. For more information,
see [Getting started with EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_.

```
{
    "source": [
        "aws.ecs"
    ],
    "detail-type": [
        "ECS Service Action"
    ]
}
```

Amazon ECS sends events with `INFO`, `WARN`, and
`ERROR` event types. The following are the service action
events.

## Service action events with `INFO` event type

`SERVICE_STEADY_STATE`

The service is healthy and at the desired number of tasks, thus
reaching a steady state. The service scheduler reports the status
periodically, so you might receive this message multiple
times.

`TASKSET_STEADY_STATE`

The task set is healthy and at the desired number of tasks, thus
reaching a steady state.

`CAPACITY_PROVIDER_STEADY_STATE`

A capacity provider associated with a service reaches a steady
state.

`SERVICE_DESIRED_COUNT_UPDATED`

When the service scheduler updates the computed desired count for
a service or task set. This event is not sent when the desired count
is manually updated by a user.

`TASKS_STOPPED`

The service has stopped the running task.

`SERVICE_DEPLOYMENT_IN_PROGRESS`

A service deployment is in progress. The service deployment can be either a rollback, or a new service revision.

`SERVICE_DEPLOYMENT_COMPLETED`

A service deployment is in the steady state and is complete. The
service deployment can be either a rollback, or to deploy an updated
service revision.

## Service action events with `WARN` event type

`SERVICE_TASK_START_IMPAIRED`

The service is unable to consistently start tasks
successfully.

`SERVICE_DISCOVERY_INSTANCE_UNHEALTHY`

A service using service discovery contains an unhealthy task. The
service scheduler detects that a task within a service registry is
unhealthy.

`VPC_LATTICE_TARGET_UNHEALTHY`

The service using VPC Lattice has detected one of the targets for the
VPC Lattice is unhealthy.

## Service action events with `ERROR` event type

`SERVICE_DAEMON_PLACEMENT_CONSTRAINT_VIOLATED`

A task in a service using the `DAEMON` service
scheduler strategy no longer meets the placement constraint strategy
for the service.

`ECS_OPERATION_THROTTLED`

The service scheduler has been throttled due to the Amazon ECS API
throttle limits.

`SERVICE_DISCOVERY_OPERATION_THROTTLED`

The service scheduler has been throttled due to the AWS Cloud Map API
throttle limits. This can occur on services configured to use
service discovery.

`SERVICE_TASK_PLACEMENT_FAILURE`

The service scheduler is unable to place a task. The cause will be
described in the `reason` field.

A common cause for this service event being generated is because
of a lack of resources in the cluster to place the task. For
example, not enough CPU or memory capacity on the available
container instances or no container instances being available.
Another common cause is when the Amazon ECS container agent is
disconnected on the container instance, causing the scheduler to be
unable to place the task.

`SERVICE_TASK_CONFIGURATION_FAILURE`

The service scheduler is unable to place a task due to a
configuration error. The cause will be described in the
`reason` field.

A common cause of this service event being generated is because
tags were being applied to the service but the user or role had not
opted in to the new Amazon Resource Name (ARN) format in the Region.
For more information, see [Amazon Resource Names (ARNs) and IDs](ecs-account-settings.md#ecs-resource-ids "ecs-account-settings.md#ecs-resource-ids"). Another common cause is that
Amazon ECS was unable to assume the task IAM role provided.

`SERVICE_HEALTH_UNKNOWN`

The service was unable to describe the health data for tasks.

`SERVICE_DEPLOYMENT_FAILED`

A service deployment did not reach the steady. This happens when a
CloudWatch is triggered or the circuit breaker detects a service
deployment failure.

###### Example Service steady state event

Service steady state events are delivered in the following format. For more
information about EventBridge parameters, see [Events in EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the
_Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "af3c496d-f4a8-65d1-70f4-a69d52e9b584",
    "detail-type": "ECS Service Action",
    "source": "aws.ecs",
    "account": "111122223333",
    "time": "2019-11-19T19:27:22Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
    ],
    "detail": {
        "eventType": "INFO",
        "eventName": "SERVICE_STEADY_STATE",
        "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
        "createdAt": "2019-11-19T19:27:22.695Z"
    }
}
```

###### Example Capacity provider steady state event

Capacity provider steady state events are delivered in the following
format.

```
{
    "version": "0",
    "id": "b9baa007-2f33-0eb1-5760-0d02a572d81f",
    "detail-type": "ECS Service Action",
    "source": "aws.ecs",
    "account": "111122223333",
    "time": "2019-11-19T19:37:00Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
    ],
    "detail": {
        "eventType": "INFO",
        "eventName": "CAPACITY_PROVIDER_STEADY_STATE",
        "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
        "capacityProviderArns": [
            "arn:aws:ecs:us-west-2:111122223333:capacity-provider/ASG-tutorial-capacity-provider"
        ],
        "createdAt": "2019-11-19T19:37:00.807Z"
    }
}
```

###### Example Service task start impaired event

Service task start impaired events are delivered in the following
format.

```
{
    "version": "0",
    "id": "57c9506e-9d21-294c-d2fe-e8738da7e67d",
    "detail-type": "ECS Service Action",
    "source": "aws.ecs",
    "account": "111122223333",
    "time": "2019-11-19T19:55:38Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
    ],
    "detail": {
        "eventType": "WARN",
        "eventName": "SERVICE_TASK_START_IMPAIRED",
        "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
        "createdAt": "2019-11-19T19:55:38.725Z"
    }
}
```

###### Example Service task placement failure event

Service task placement failure events are delivered in the following format.
For more information, see [Events in EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the
_Amazon EventBridge User Guide_.

In the following example, the task was attempting to use the
`FARGATE_SPOT` capacity provider but the service scheduler was
unable to acquire any Fargate Spot capacity.

```
{
    "version": "0",
    "id": "ddca6449-b258-46c0-8653-e0e3a6d0468b",
    "detail-type": "ECS Service Action",
    "source": "aws.ecs",
    "account": "111122223333",
    "time": "2019-11-19T19:55:38Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
    ],
    "detail": {
        "eventType": "ERROR",
        "eventName": "SERVICE_TASK_PLACEMENT_FAILURE",
        "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
        "capacityProviderArns": [
            "arn:aws:ecs:us-west-2:111122223333:capacity-provider/FARGATE_SPOT"
        ],
        "reason": "RESOURCE:FARGATE",
        "createdAt": "2019-11-06T19:09:33.087Z"
    }
}
```

In the following example for EC2, the task was attempted to
launch on the Container Instance `2dd1b186f39845a584488d2ef155c131`
but the service scheduler was unable to place the task because of insufficient
CPU.

```
{
  "version": "0",
  "id": "ddca6449-b258-46c0-8653-e0e3a6d0468b",
  "detail-type": "ECS Service Action",
  "source": "aws.ecs",
  "account": "111122223333",
  "time": "2019-11-19T19:55:38Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:ecs:us-west-2:111122223333:service/default/servicetest"
  ],
  "detail": {
    "eventType": "ERROR",
    "eventName": "SERVICE_TASK_PLACEMENT_FAILURE",
    "clusterArn": "arn:aws:ecs:us-west-2:111122223333:cluster/default",
    "containerInstanceArns": [
    "arn:aws:ecs:us-west-2:111122223333:container-instance/default/2dd1b186f39845a584488d2ef155c131"
    ],
    "reason": "RESOURCE:CPU",
    "createdAt": "2019-11-06T19:09:33.087Z"
  }
}
```

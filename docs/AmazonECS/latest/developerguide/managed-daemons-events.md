# Daemon events

Amazon ECS sends daemon events to to provide visibility into daemon task management and
deployment lifecycle changes. You can use these events to monitor daemon health, track
deployment progress, and trigger automated workflows.

Amazon ECS supports the following daemon event types:

- [Daemon service action events](#managed-daemons-service-action-events "#managed-daemons-service-action-events") - Events related to
  daemon task placement and startup issues.
- [Daemon deployment state change events](#managed-daemons-deployment-state-change-events "#managed-daemons-deployment-state-change-events") - Events
  related to daemon deployment lifecycle transitions.
  To learn how to create rules for these events, see [Creating rules for daemon events](#managed-daemons-eventbridge-rules "#managed-daemons-eventbridge-rules").

## Daemon service action events

Amazon ECS sends daemon service action events with the detail type `ECS Daemon
 Service Action`. These events notify you when Amazon ECS encounters issues
starting daemon tasks on your container instances. Amazon ECS emits an EventBridge event
when a daemon task fails to start, for both critical and non-critical daemons.

### DAEMON\_TASK\_START\_IMPAIRED

Amazon ECS sends the `DAEMON_TASK_START_IMPAIRED` event when it is unable
to successfully start a daemon task on a container instance. The event includes a
`failureType` field that indicates the cause of the failure:

- `TASK_FAILED_TO_RUN` - The daemon task was created but failed
  to reach `RUNNING` status. Common causes include container image
  pull failures, container health check failures, or essential container exits.
  The `taskArn` field is present in the event.
- `TASK_CREATION_FAILED` - The daemon task could not be created
  on the container instance. Common causes include insufficient CPU, memory, or
  other resources on the instance. The `taskArn` field is not
  present in the event because no task was created.

### Example: TASK\_FAILED\_TO\_RUN event

The following event shows a daemon task that was created but failed to reach
`RUNNING` status due to a container image pull failure.

```
{
    "version": "0",
    "id": "12345678-1234-1234-1234-123456789012",
    "detail-type": "ECS Daemon Service Action",
    "source": "aws.ecs",
    "account": "`123456789012`",
    "time": "2026-03-24T12:00:00Z",
    "region": "`us-west-2`",
    "resources": [
        "arn:aws:ecs:`us-west-2`:`123456789012`:task/`my-cluster`/`a1b2c3d4e5f6`"
    ],
    "detail": {
        "eventType": "WARNING",
        "eventName": "DAEMON_TASK_START_IMPAIRED",
        "clusterArn": "arn:aws:ecs:`us-west-2`:`123456789012`:cluster/`my-cluster`",
        "containerInstanceArn": "arn:aws:ecs:`us-west-2`:`123456789012`:container-instance/`my-cluster`/`a1b2c3d4e5f6`",
        "taskArn": "arn:aws:ecs:`us-west-2`:`123456789012`:task/`my-cluster`/`a1b2c3d4e5f6`",
        "daemonRevisionArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon-revision/`my-cluster`/`my-daemon`/`a1b2c3d4-e5f6-7890-abcd-ef1234567890`",
        "capacityProviderName": "`my-capacity-provider`",
        "daemonArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon/`my-cluster`/`my-daemon`",
        "daemonTaskDefinitionArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon-task-definition/`my-daemon-td`:1",
        "failureType": "TASK_FAILED_TO_RUN",
        "createdAt": "2026-03-24T12:00:00.000Z",
        "reason": "Task failed to reach RUNNING status: CannotPullContainerError: pull image manifest has been retried 5 time(s)"
    }
}
```

### Example: TASK\_CREATION\_FAILED event

The following event shows a daemon task that could not be created on the container
instance due to insufficient CPU resources. The `taskArn` field is not
present because no task was created.

```
{
    "version": "0",
    "id": "87654321-4321-4321-4321-210987654321",
    "detail-type": "ECS Daemon Service Action",
    "source": "aws.ecs",
    "account": "`123456789012`",
    "time": "2026-03-24T12:01:00Z",
    "region": "`us-west-2`",
    "resources": [],
    "detail": {
        "eventType": "WARNING",
        "eventName": "DAEMON_TASK_START_IMPAIRED",
        "clusterArn": "arn:aws:ecs:`us-west-2`:`123456789012`:cluster/`my-cluster`",
        "containerInstanceArn": "arn:aws:ecs:`us-west-2`:`123456789012`:container-instance/`my-cluster`/`b2c3d4e5f6a7`",
        "daemonRevisionArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon-revision/`my-cluster`/`my-daemon`/`a1b2c3d4-e5f6-7890-abcd-ef1234567890`",
        "capacityProviderName": "`my-capacity-provider`",
        "daemonArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon/`my-cluster`/`my-daemon`",
        "daemonTaskDefinitionArn": "arn:aws:ecs:`us-west-2`:`123456789012`:daemon-task-definition/`my-daemon-td`:1",
        "failureType": "TASK_CREATION_FAILED",
        "createdAt": "2026-03-24T12:01:00.000Z",
        "reason": "RESOURCE:CPU - Unable to place daemon task on container instance: insufficient CPU"
    }
}
```

## Daemon deployment state change events

Amazon ECS sends daemon deployment state change events with the detail type `ECS
 Daemon Deployment State Change`. Amazon ECS emits these events each time the state
of a daemon deployment changes.

### Deployment state change event types

Amazon ECS categorizes deployment state change events by the following event
types:

**INFO events**

- `DAEMON_DEPLOYMENT_PENDING` - Amazon ECS has initiated a daemon
  deployment.
- `DAEMON_DEPLOYMENT_IN_PROGRESS` - Amazon ECS has started the
  deployment and is actively replacing daemon tasks.
- `DAEMON_DEPLOYMENT_SUCCESSFUL` - Amazon ECS has successfully
  completed the deployment with all daemon tasks running and healthy.
- `DAEMON_DEPLOYMENT_STOPPED` - Amazon ECS has stopped the
  deployment. This occurs when a deployment has failed or has been replaced by
  a new deployment.
- `DAEMON_DEPLOYMENT_STOP_REQUESTED` - Amazon ECS has stopped the
  deployment from moving forward and will now start to roll back.
- `DAEMON_DEPLOYMENT_ROLLBACK_IN_PROGRESS` - Amazon ECS has
  initiated a rollback due to deployment failure or circuit breaker
  trigger.
- `DAEMON_DEPLOYMENT_ROLLBACK_SUCCESSFUL` - Amazon ECS has
  successfully completed the deployment rollback.

**ERROR events**

- `DAEMON_DEPLOYMENT_ROLLBACK_FAILED` - Amazon ECS was unable to
  complete the deployment rollback.

### Example: Deployment pending event

The following event shows a daemon deployment that Amazon ECS has initiated.

```
{
    "version": "0",
    "id": "3329f79b-3dca-07f8-b1c2-5fe99f0b5e87",
    "detail-type": "ECS Daemon Deployment State Change",
    "source": "aws.ecs",
    "account": "`111122223333`",
    "time": "2026-03-05T15:54:41Z",
    "region": "`us-west-2`",
    "resources": [
        "arn:aws:ecs:`us-west-2`:`111122223333`:daemon/`my-cluster`/`my-daemon`"
    ],
    "detail": {
        "eventType": "INFO",
        "eventName": "DAEMON_DEPLOYMENT_PENDING",
        "clusterArn": "arn:aws:ecs:`us-west-2`:`111122223333`:cluster/`my-cluster`",
        "daemonArn": "arn:aws:ecs:`us-west-2`:`111122223333`:daemon/`my-cluster`/`my-daemon`",
        "daemonDeploymentArn": "arn:aws:ecs:`us-west-2`:`111122223333`:daemon-deployment/`my-cluster`/`my-daemon`/`0EYSiB0qap8xf0N76FsbE`",
        "targetDaemonRevisionArn": "arn:aws:ecs:`us-west-2`:`111122223333`:daemon-revision/`my-cluster`/`my-daemon`/`85707969-3732-4b6a-a37d-5cefddd7d7dd`",
        "updatedAt": "2026-03-05T15:54:41.618059641Z"
    }
}
```

## Creating rules for daemon events

You can create rules to receive notifications when daemon events occur. For
more information about creating rules, see [Creating a rule](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User
Guide_.

The following example event patterns show how to filter daemon events.

### Example: Match all daemon service action events

```
{
    "source": ["aws.ecs"],
    "detail-type": ["ECS Daemon Service Action"]
}
```

### Example: Match a specific failure type

```
{
    "source": ["aws.ecs"],
    "detail-type": ["ECS Daemon Service Action"],
    "detail": {
        "eventName": ["DAEMON_TASK_START_IMPAIRED"],
        "failureType": ["TASK_CREATION_FAILED"]
    }
}
```

### Example: Match events for a specific cluster

```
{
    "source": ["aws.ecs"],
    "detail-type": ["ECS Daemon Service Action"],
    "detail": {
        "eventName": ["DAEMON_TASK_START_IMPAIRED"],
        "clusterArn": ["arn:aws:ecs:`us-west-2`:`123456789012`:cluster/`my-cluster`"]
    }
}
```

### Example: Match all deployment state change events

```
{
    "source": ["aws.ecs"],
    "detail-type": ["ECS Daemon Deployment State Change"]
}
```

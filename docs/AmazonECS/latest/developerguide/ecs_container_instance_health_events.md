# Amazon ECS container instance health change events

The following scenarios cause container instance health change events.

**The Amazon ECS container agent detects a change in container runtime
health.**

The container agent periodically evaluates the health of the container runtime (for
example, the Docker daemon) on the container instance. If the runtime becomes unresponsive
or recovers, the agent reports the change and an event is generated.

Availability: EC2 launch type.

**The Amazon ECS container agent detects a change in accelerated compute
device health.**

On instances with accelerated compute devices such as GPUs, the container agent monitors
device health. If a device becomes impaired or recovers, an event is generated.

Availability: Amazon ECS Managed Instances launch type.

**The Amazon ECS container agent detects a change in daemon
health.**

The container agent monitors required daemon tasks on the container instance. If a
daemon task fails, an event is generated.

Availability: Amazon ECS Managed Instances launch type.

**The Amazon ECS container agent loses connectivity to the Amazon ECS control
plane.**

Amazon ECS continuously monitors the connectivity between the container agent and the Amazon ECS
control plane. When a container instance remains disconnected beyond a threshold, Amazon ECS
marks the instance as impaired.

Availability: Amazon ECS Managed Instances, AWS Fargate, and Amazon EC2 launch types.

**The overall health status of the container instance
changes.**

Amazon ECS computes an overall health status from the individual health check results. When the
overall status transitions, an event is generated.

Availability: Amazon ECS Managed Instances and EC2 launch type.

## Example container instance health change event

Container instance health change events are delivered in the following format. For
more information about parameters, see [AWS service event
metadata](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _User
Guide_.

**Sample container runtime health event**

```
{
    "version": "0",
    "id": "EXAMPLE-48f8-c0ff-0dab-EXAMPLE2ac34",
    "detail-type": "ECS Container Instance Health Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2026-04-11T00:49:09Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE"
    ],
    "detail": {
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "containerInstanceArn": "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE",
        "capacityProviderName": null,
        "ec2InstanceId": "i-0abcdef1234567890",
        "overallStatus": "OK",
        "healthChecks": [
            {
                "type": "CONTAINER_RUNTIME",
                "status": "OK",
                "lastStatusChange": "2026-04-11T00:48:53Z",
                "lastUpdated": "2026-04-11T00:48:09Z",
                "statusReason": null
            }
        ]
    }
}
```

**Sample accelerated compute health event**

```
{
    "version": "0",
    "id": "EXAMPLE-46c3-a48a-1bef-EXAMPLE72f3c",
    "detail-type": "ECS Container Instance Health Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2026-04-11T00:49:09Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE"
    ],
    "detail": {
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "containerInstanceArn": "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE",
        "capacityProviderName": "my-capacity-provider",
        "ec2InstanceId": "i-0abcdef1234567890",
        "overallStatus": "IMPAIRED",
        "healthChecks": [
            {
                "type": "ACCELERATED_COMPUTE",
                "status": "IMPAIRED",
                "lastStatusChange": "2026-04-11T00:48:53Z",
                "lastUpdated": "2026-04-11T00:48:09Z",
                "statusReason": "XID_46"
            }
        ]
    }
}
```

**Sample daemon health event**

```
{
    "version": "0",
    "id": "EXAMPLE-febc-b5e3-054b-EXAMPLE1a1f4f",
    "detail-type": "ECS Container Instance Health Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2026-04-11T00:49:09Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE"
    ],
    "detail": {
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "containerInstanceArn": "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE",
        "capacityProviderName": "my-capacity-provider",
        "ec2InstanceId": "i-0abcdef1234567890",
        "overallStatus": "IMPAIRED",
        "healthChecks": [
            {
                "type": "DAEMON",
                "status": "IMPAIRED",
                "lastStatusChange": "2026-04-11T00:48:53Z",
                "lastUpdated": "2026-04-11T00:48:09Z",
                "statusReason": "Daemon task: EXAMPLE-4af2-4b3c-b9c1-EXAMPLEb2bbf is unhealthy"
            }
        ]
    }
}
```

**Sample agent connectivity health event**

```
{
    "version": "0",
    "id": "EXAMPLE-7d2a-9f1c-4b6e-EXAMPLE9c8d1",
    "detail-type": "ECS Container Instance Health Change",
    "source": "aws.ecs",
    "account": "123456789012",
    "time": "2026-07-29T22:34:13Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE"
    ],
    "detail": {
        "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/my-cluster",
        "containerInstanceArn": "arn:aws:ecs:us-west-2:123456789012:container-instance/my-cluster/a1b2c3d4EXAMPLE",
        "capacityProviderName": "my-capacity-provider",
        "ec2InstanceId": "i-0abcdef1234567890",
        "overallStatus": "IMPAIRED",
        "healthChecks": [
            {
                "type": "AGENT_CONNECTIVITY",
                "status": "IMPAIRED",
                "lastStatusChange": "2026-07-29T22:34:13Z",
                "lastUpdated": "2026-07-29T22:34:09Z",
                "statusReason": "Agent disconnected since 2026-07-29T22:34:13Z"
            }
        ]
    }
}
```

# Amazon ECS container instance state change

events

The following scenarios cause container instance state change events:

You call the `StartTask`, `RunTask`, or
`StopTask` API operations, either directly or with the
AWS Management Console or SDKs.

Placing or stopping tasks on a container instance modifies the
available resources on the container instance, such as CPU, memory, and
available ports.

The Amazon ECS service scheduler starts or stops a task.

Placing or stopping tasks on a container instance modifies the
available resources on the container instance, such as CPU, memory, and
available ports.

The Amazon ECS container agent calls the `SubmitTaskStateChange` API
operation with a `STOPPED` status for a task with a desired
status of `RUNNING`.

The Amazon ECS container agent monitors the state of tasks on your
container instances, and it reports any state changes. If a task that is
supposed to be `RUNNING` is transitioned to
`STOPPED`, the agent releases the resources that were
allocated to the stopped task, such as CPU, memory, and available
ports.

You deregister the container instance with the
`DeregisterContainerInstance` API operation, either directly
or with the AWS Management Console or SDKs.

Deregistering a container instance changes the status of the container
instance and the connection status of the Amazon ECS container agent.

A task was stopped when an EC2 instance was stopped.

When you stop a container instance, the tasks that are running on it
are transitioned to the `STOPPED` status.

The Amazon ECS container agent registers a container instance for the first
time.

The first time the Amazon ECS container agent registers a container
instance (at launch or when first run manually), this creates a state
change event for the instance.

The Amazon ECS container agent connects or disconnects from Amazon ECS.

When the Amazon ECS container agent connects or disconnects from the Amazon ECS
backend, it changes the `agentConnected` status of the
container instance.

###### Note

The Amazon ECS container agent disconnects and reconnects several times
per hour as a part of its normal operation, so agent connection
events should be expected. These events are not an indication that
there is an issue with the container agent or your container
instance.

You upgrade the Amazon ECS container agent on an instance.

The container instance detail contains an object for the container
agent version. If you upgrade the agent, this version information
changes and generates an event.

###### Example Container instance state change event

Container instance state change events are delivered in the following format.
The `detail` section below resembles the [ContainerInstance](../APIReference/API_ContainerInstance.md "../APIReference/API_ContainerInstance.md")
object that is returned from a [DescribeContainerInstances](../APIReference/API_DescribeContainerInstances.md "../APIReference/API_DescribeContainerInstances.md") API operation in the
_Amazon Elastic Container Service API Reference_. For more information about EventBridge
parameters, see [AWS service event metadata](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the
_Amazon EventBridge User Guide_.

```
{
  "version": "0",
  "id": "8952ba83-7be2-4ab5-9c32-6687532d15a2",
  "detail-type": "ECS Container Instance State Change",
  "source": "aws.ecs",
  "account": "111122223333",
  "time": "2016-12-06T16:41:06Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ecs:us-east-1:111122223333:container-instance/b54a2a04-046f-4331-9d74-3f6d7f6ca315"
  ],
  "detail": {
    "agentConnected": true,
    "attributes": [
      {
        "name": "com.amazonaws.ecs.capability.logging-driver.syslog"
      },
      {
        "name": "com.amazonaws.ecs.capability.task-iam-role-network-host"
      },
      {
        "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
      },
      {
        "name": "com.amazonaws.ecs.capability.logging-driver.json-file"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.17"
      },
      {
        "name": "com.amazonaws.ecs.capability.privileged-container"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
      },
      {
        "name": "com.amazonaws.ecs.capability.ecr-auth"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.20"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.21"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.22"
      },
      {
        "name": "com.amazonaws.ecs.capability.docker-remote-api.1.23"
      },
      {
        "name": "com.amazonaws.ecs.capability.task-iam-role"
      }
    ],
    "clusterArn": "arn:aws:ecs:us-east-1:111122223333:cluster/default",
    "containerInstanceArn": "arn:aws:ecs:us-east-1:111122223333:container-instance/b54a2a04-046f-4331-9d74-3f6d7f6ca315",
    "ec2InstanceId": "i-f3a8506b",
    "registeredResources": [
      {
        "name": "CPU",
        "type": "INTEGER",
        "integerValue": 2048
      },
      {
        "name": "MEMORY",
        "type": "INTEGER",
        "integerValue": 3767
      },
      {
        "name": "PORTS",
        "type": "STRINGSET",
        "stringSetValue": [
          "22",
          "2376",
          "2375",
          "51678",
          "51679"
        ]
      },
      {
        "name": "PORTS_UDP",
        "type": "STRINGSET",
        "stringSetValue": []
      }
    ],
    "remainingResources": [
      {
        "name": "CPU",
        "type": "INTEGER",
        "integerValue": 1988
      },
      {
        "name": "MEMORY",
        "type": "INTEGER",
        "integerValue": 767
      },
      {
        "name": "PORTS",
        "type": "STRINGSET",
        "stringSetValue": [
          "22",
          "2376",
          "2375",
          "51678",
          "51679"
        ]
      },
      {
        "name": "PORTS_UDP",
        "type": "STRINGSET",
        "stringSetValue": []
      }
    ],
    "status": "ACTIVE",
    "version": 14801,
    "versionInfo": {
      "agentHash": "aebcbca",
      "agentVersion": "1.13.0",
      "dockerVersion": "DockerVersion: 1.11.2"
    },
    "updatedAt": "2016-12-06T16:41:06.991Z"
  }
}
```

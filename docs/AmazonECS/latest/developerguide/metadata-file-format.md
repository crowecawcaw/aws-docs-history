# Amazon ECS container metadata file format

The following information is stored in the container metadata JSON file.

`Cluster`

The name of the cluster that the container's task is running on.

`ContainerInstanceARN`

The full Amazon Resource Name (ARN) of the host container instance.

`TaskARN`

The full Amazon Resource Name (ARN) of the task that the container belongs to.

`TaskDefinitionFamily`

The name of the task definition family the container is using.

`TaskDefinitionRevision`

The task definition revision the container is using.

`ContainerID`

The Docker container ID (and not the Amazon ECS container ID) for the
container.

`ContainerName`

The container name from the Amazon ECS task definition for the
container.

`DockerContainerName`

The container name that the Docker daemon uses for the container (for
example, the name that shows up in **docker ps** command
output).

`ImageID`

The SHA digest for the Docker image used to start the container.

`ImageName`

The image name and tag for the Docker image used to start the
container.

`PortMappings`

Any port mappings associated with the container.

`ContainerPort`

The port on the container that is exposed.

`HostPort`

The port on the host container instance that is
exposed.

`BindIp`

The bind IP address that is assigned to the container by
Docker. This IP address is only applied with the
`bridge` network mode, and it is only accessible
from the container instance.

`Protocol`

The network protocol used for the port mapping.

`Networks`

The network mode and IP address for the container.

`NetworkMode`

The network mode for the task to which the container
belongs.

`IPv4Addresses`

The IP addresses associated with the container.

###### Important

If your task is using the `awsvpc` network
mode, the IP address of the container will not be returned.
In this case, you can retrieve the IP address by reading the
/etc/hosts file with the following command:

```
`tail -1 /etc/hosts | awk '{print $1}'`
```

`MetadataFileStatus`

The status of the metadata file. When the status is `READY`,
the metadata file is current and complete. If the file is not ready yet (for
example, the moment the task is started), a truncated version of the file
format is available. To avoid a likely race condition where the container
has started, but the metadata has not yet been written, you can parse the
metadata file and wait for this parameter to be set to `READY`
before depending on the metadata. This is usually available in less than 1
second from when the container starts.

`AvailabilityZone`

The Availability Zone the host container instance resides in.

`HostPrivateIPv4Address`

The private IP address for the task the container belongs to.

`HostPublicIPv4Address`

The public IP address for the task the container belongs to.

###### Example Amazon ECS container metadata file (`READY`)

The following example shows a container metadata file in the `READY`
status.

```
{
    "Cluster":"arn:aws:ecs:us-east-1:123456789012:cluster/MyCluster",
    "TaskARN":"arn:aws:ecs:us-east-1:123456789012:task/MyCluster/b593651c4d6b44a6b2b583f45c957e15",
    "Family":"curltest-container",
    "Revision":"2",
    "DesiredStatus":"RUNNING",
    "KnownStatus":"RUNNING",
    "Limits":
        {
            "CPU":0.25,
            "Memory":512
        },
    "PullStartedAt":"2025-01-17T20:56:17.394610044Z",
    "PullStoppedAt":"2025-01-17T20:56:25.282708213Z",
    "AvailabilityZone":"us-east-1b",
    "LaunchType":"FARGATE",
    "Containers":[
        {
            "DockerId":"b593651c4d6b44a6b2b583f45c957e15-3356213583",
            "Name":"curltest","DockerName":"curltest",
            "Image":"public.ecr.aws/amazonlinux/amazonlinux:latest",
            "ImageID":"sha256:7f371357694782356b65c7fd60dd1ca124c47bd5ed1b1ffe7c0e17f562898367",
            "Labels":
                {
                    "com.amazonaws.ecs.cluster":"arn:aws:ecs:us-east-1:123456789012:cluster/MyCluster",
                    "com.amazonaws.ecs.container-name":"curltest",
                    "com.amazonaws.ecs.task-arn":"arn:aws:ecs:us-east-1:123456789012:task/MyCluster/b593651c4d6b44a6b2b583f45c957e15",
                    "com.amazonaws.ecs.task-definition-family":"curltest-container","com.amazonaws.ecs.task-definition-version":"2"
               },
            "DesiredStatus":"RUNNING",
            "KnownStatus":"RUNNING",
            "Limits":
                {
                    "CPU":2
                },
            "CreatedAt":"2025-01-17T20:56:26.180347056Z",
            "StartedAt":"2025-01-17T20:56:26.180347056Z",
            "Type":"NORMAL",
            "LogDriver":"awslogs",
            "LogOptions":
                {
                    "awslogs-create-group":"true",
                    "awslogs-group":"/ecs/curltest-container",
                    "awslogs-region":"us-east-1",
                    "awslogs-stream":"ecs/curltest/b593651c4d6b44a6b2b583f45c957e15"
                       },
            "ContainerARN":"arn:aws:ecs:us-east-1:123456789012:container/MyCluster/b593651c4d6b44a6b2b583f45c957e15/934575e8-5bdb-478f-b763-2341a85b690e",
            "Networks":[
                {
                    "NetworkMode":"awsvpc",
                    "IPv4Addresses":["10.0.1.58"]
                }
            ],
            "Snapshotter":"overlayfs"
        }
    ],
    "ClockDrift":
        {
            "ClockErrorBound":0.487801,"ReferenceTimestamp":"2025-01-17T20:56:02Z",
            "ClockSynchronizationStatus":"SYNCHRONIZED"
        },
    "FaultInjectionEnabled":false
}
```

###### Example Incomplete Amazon ECS container metadata file (not yet `READY`)

The following example shows a container metadata file that has not yet reached the
`READY` status. The information in the file is limited to a few
parameters that are known from the task definition. The container metadata file
should be ready within 1 second after the container starts.

```
{
    "Cluster": "default",
    "ContainerInstanceARN": "arn:aws:ecs:us-west-2:012345678910:container-instance/default/1f73d099-b914-411c-a9ff-81633b7741dd",
    "TaskARN": "arn:aws:ecs:us-west-2:012345678910:task/default/d90675f8-1a98-444b-805b-3d9cabb6fcd4",
    "ContainerName": "metadata"
}
```

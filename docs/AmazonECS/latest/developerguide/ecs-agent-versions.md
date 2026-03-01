# Amazon ECS EC2 Container Instances

The Amazon ECS agent is a process that runs on every container instance that is registered with
your cluster. It facilitates the communication between your container instances and Amazon ECS.

###### Note

On Linux container instances, the agent container mounts top-level directories such as
`/lib`, `/lib64`, and `/proc`. This is necessary
for ECS features and functionalities such as Amazon EBS volumes, `awsvpc` network
mode, Amazon ECS Service Connect, and FireLens for Amazon ECS.

Each Amazon ECS container agent version supports a different feature set and provides bug fixes
from previous versions. When possible, we always recommend using the latest version of the
Amazon ECS container agent. To update your container agent to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

The Amazon ECS container agent contains the `amazon-ecs-pause` image.Amazon ECS uses this
image for tasks that use `awsvpc` network mode.

To see which features and enhancements are included with each agent release, see [https://github.com/aws/amazon-ecs-agent/releases](https://github.com/aws/amazon-ecs-agent/releases "https://github.com/aws/amazon-ecs-agent/releases").

###### Important

The minimum Docker version for reliable metrics is Docker version `v20.10.13` and
newer, which is included in Amazon ECS-optimized AMI `20220607` and newer.

Amazon ECS agent versions `1.20.0` and newer have deprecated support for
Docker versions older than `18.01.0`.

## Lifecycle

When the Amazon ECS container agent registers an Amazon EC2 instance to your cluster, the Amazon EC2
instance reports its status as `ACTIVE` and its agent connection status as
`TRUE`. This container instance can accept run task requests.

If you stop (not terminate) a container instance, the status remains
`ACTIVE`, but the agent connection status transitions to
`FALSE` within a few minutes. Any tasks that were running on the
container instance stop. If you start the container instance again, the container agent
reconnects with the Amazon ECS service, and you are able to run tasks on the instance
again.

###### Important

If you stop and start a container instance, or reboot that instance, some older
versions of the Amazon ECS container agent register the instance again without
deregistering the original container instance ID. In this case, Amazon ECS lists more
container instances in your cluster than you actually have. (If you have duplicate
container instance IDs for the same Amazon EC2 instance ID, you can safely deregister the
duplicates that are listed as `ACTIVE` with an agent connection status of
`FALSE`.) This issue is fixed in the current version of the Amazon ECS
container agent. For more information about updating to the current version, see
[Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

If you change the status of a container instance to `DRAINING`, new tasks
are not placed on the container instance. Any service tasks running on the container
instance are removed, if possible, so that you can perform system updates. For more
information, see [Draining Amazon ECS container instances](container-instance-draining.md "container-instance-draining.md").

If you deregister or terminate a container instance, the container instance status
changes to `INACTIVE` immediately, and the container instance is no longer
reported when you list your container instances. However, you can still describe the
container instance for one hour following termination. After one hour, the instance
description is no longer available.

###### Important

You can drain the instances manually, or build an Auto Scaling group lifecycle hook to
set the instance status to `DRAINING`. See [Amazon EC2 Auto Scaling lifecycle
hooks](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md") for more information about Auto Scaling lifecycle hooks.

## Docker Support

Amazon ECS supports the last two major versions of Docker published on Amazon Linux. Currently, this includes Docker 20.10.x and Docker 25.x.

The minimum required Docker version for Amazon ECS can be found in the [Amazon ECS Agent specification file](https://github.com/aws/amazon-ecs-agent/blob/dev/packaging/amazon-linux-ami-integrated/ecs-agent.spec#L53 "https://github.com/aws/amazon-ecs-agent/blob/dev/packaging/amazon-linux-ami-integrated/ecs-agent.spec#L53") on GitHub.

When using the Amazon ECS-optimized AMI, Docker is pre-installed and configured to work with the Amazon ECS container agent. The AMI includes a Docker version that is tested and supported by Amazon ECS.

###### Note

While Amazon ECS supports multiple Docker versions, we recommend using the Docker version that comes with the Amazon ECS-optimized AMI for the best compatibility and support.

## Amazon ECS-optimized AMI

The Linux variants of the Amazon ECS-optimized AMI use the Amazon Linux 2 AMI as their base. The
Amazon Linux 2 source AMI name for each variant can be retrieved by querying the Systems Manager
Parameter Store API. For more information, see [Retrieving Amazon ECS-optimized Linux AMI metadata](retrieve-ecs-optimized_AMI.md "retrieve-ecs-optimized_AMI.md").
When you launch our container instances from the most recent Amazon ECS-optimized Amazon Linux 2 AMI you receive the
current container agent version. To launch a container instance with the latest
Amazon ECS-optimized Amazon Linux 2 AMI, see [Launching an Amazon ECS Linux container instance](launch_container_instance.md "launch_container_instance.md").

## Additional information

The following pages provide additional information about the changes:

- [Amazon ECS Agent changelog](https://github.com/aws/amazon-ecs-agent/blob/master/CHANGELOG.md "https://github.com/aws/amazon-ecs-agent/blob/master/CHANGELOG.md") on GitHub
- The source code for the `ecs-init` application and the scripts and
  configuration for packaging the agent are now part of the agent repository. For
  older versions of `ecs-init` and packaging, see [Amazon
  ecs-init changelog](https://github.com/aws/amazon-ecs-init/blob/master/CHANGELOG.md "https://github.com/aws/amazon-ecs-init/blob/master/CHANGELOG.md") on GitHub
- [Amazon Linux 2 release
  notes](../../../AL2/latest/relnotes/relnotes-al2.md "../../../AL2/latest/relnotes/relnotes-al2.md").
- [Docker Engine
  release notes](https://docs.docker.com/engine/release-notes/27/ "https://docs.docker.com/engine/release-notes/27/") in the Docker documentation
- [NVIDIA Driver
  Documentation](https://docs.nvidia.com/datacenter/tesla/index.html "https://docs.nvidia.com/datacenter/tesla/index.html") in the NVIDIA documentation

## Amazon ECS container agent log configuration parameters

The Amazon ECS container agent stores logs on your container instances.

For container agent version 1.36.0 and later, by default the logs are located at
`/var/log/ecs/ecs-agent.log` on Linux instances and at
`C:\ProgramData\Amazon\ECS\log\ecs-agent.log` on Windows
instances.

For container agent version 1.35.0 and earlier, by default the logs are located at
`/var/log/ecs/ecs-agent.log.`timestamp``
 on Linux instances and at
 `C:\ProgramData\Amazon\ECS\log\ecs-agent.log.`timestamp``
on Windows instances.

By default, the agent logs are rotated hourly with a maximum of 24 logs being
stored.

The following are the container agent configuration variables that can be used to
change the default agent logging behavior. For detailed information about all available configuration parameters, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md") or the [Amazon ECS Agent README](https://github.com/aws/amazon-ecs-agent/blob/master/README.md "https://github.com/aws/amazon-ecs-agent/blob/master/README.md") on GitHub.

For container agent version 1.36.0 and later, the following is an example log file
when the `logfmt` format is used.

```
level=info time=2019-12-12T23:43:29Z msg="Loading configuration" module=agent.go
level=info time=2019-12-12T23:43:29Z msg="Image excluded from cleanup: amazon/amazon-ecs-agent:latest" module=parse.go
level=info time=2019-12-12T23:43:29Z msg="Image excluded from cleanup: amazon/amazon-ecs-pause:0.1.0" module=parse.go
level=info time=2019-12-12T23:43:29Z msg="Amazon ECS agent Version: 1.36.0, Commit: ca640387" module=agent.go
level=info time=2019-12-12T23:43:29Z msg="Creating root ecs cgroup: /ecs" module=init_linux.go
level=info time=2019-12-12T23:43:29Z msg="Creating cgroup /ecs" module=cgroup_controller_linux.go
level=info time=2019-12-12T23:43:29Z msg="Loading state!" module=statemanager.go
level=info time=2019-12-12T23:43:29Z msg="Event stream ContainerChange start listening..." module=eventstream.go
level=info time=2019-12-12T23:43:29Z msg="Restored cluster 'auto-robc'" module=agent.go
level=info time=2019-12-12T23:43:29Z msg="Restored from checkpoint file. I am running as 'arn:aws:ecs:us-west-2:0123456789:container-instance/auto-robc/3330a8a91d15464ea30662d5840164cd' in cluster 'auto-robc'" module=agent.go
```

The following is an example log file when the JSON format is used.

```
{"time": "2019-11-07T22:52:02Z", "level": "info", "msg": "Starting Amazon Elastic Container Service Agent", "module": "engine.go"}
```

For container agent versions 1.35.0 and earlier, the following is the format of the
log file.

```
2016-08-15T15:54:41Z [INFO] Starting Agent: Amazon ECS Agent - v1.12.0 (895f3c1)
2016-08-15T15:54:41Z [INFO] Loading configuration
2016-08-15T15:54:41Z [WARN] Invalid value for task cleanup duration, will be overridden to 3h0m0s, parsed value 0, minimum threshold 1m0s
2016-08-15T15:54:41Z [INFO] Checkpointing is enabled. Attempting to load state
2016-08-15T15:54:41Z [INFO] Loading state! module="statemanager"
2016-08-15T15:54:41Z [INFO] Detected Docker versions [1.17 1.18 1.19 1.20 1.21 1.22]
2016-08-15T15:54:41Z [INFO] Registering Instance with ECS
2016-08-15T15:54:41Z [INFO] Registered! module="api client"
```

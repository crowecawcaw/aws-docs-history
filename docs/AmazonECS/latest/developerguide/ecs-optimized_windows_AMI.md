# Amazon ECS-optimized Windows AMIs

The Amazon ECS-optimized AMIs are preconfigured with the necessary components that you need to
run Amazon ECS workloads. Although you can create your own container instance AMI that meets
the basic specifications needed to run your containerized workloads on Amazon ECS, the
Amazon ECS-optimized AMIs are preconfigured and tested on Amazon ECS by AWS engineers. It is the
simplest way for you to get started and to get your containers running on AWS
quickly.

The Amazon ECS-optimized AMI metadata, including the AMI name, Amazon ECS container agent
version, and Amazon ECS runtime version which includes the Docker version, for each variant can
be retrieved programmatically. For more information, see [Retrieving Amazon ECS-optimized Windows AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md").

###### Important

All ECS-optimized AMI variants produced after August 2022 will be migrating from
Docker EE (Mirantis) to Docker CE (Moby project).

To ensure that customers have the latest security updates by
default, Amazon ECS maintains at least the last three Windows
Amazon ECS-optimized AMIs. After releasing new Windows
Amazon ECS-optimized AMIs, Amazon ECS makes the Windows Amazon ECS-optimized
AMIs that are older private. If there is a private AMI that
you need access to, let us know by filing a ticket with Cloud
Support.

## Amazon ECS-optimized AMI variants

The following Windows Server variants of the Amazon ECS-optimized AMI are available for
your Amazon EC2 instances.

###### Important

All ECS-optimized AMI variants produced after August will be migrating from Docker
EE (Mirantis) to Docker CE (Moby project).

- **Amazon ECS-optimized Windows Server 2025 Full AMI**
- **Amazon ECS-optimized Windows Server 2025 Core AMI**
- **Amazon ECS-optimized Windows Server 2022 Full AMI**
- **Amazon ECS-optimized Windows Server 2022 Core AMI**
- **Amazon ECS-optimized Windows Server 2019 Full AMI**
- **Amazon ECS-optimized Windows Server 2019 Core AMI**
- **Amazon ECS-optimized Windows Server 2016 Full AMI**

###### Important

Windows Server 2016 does not support the latest Docker version, for example 25.x.x. Therefore the Windows Server 2016 Full AMIs will
not receive security or bug patches to the Docker runtime. We recommend that you move to one
of the following Windows platforms:

- Windows Server 2022 Full
- Windows Server 2022 Core
- Windows Server 2019 Full
- Windows Server 2019 Core

On August 9, 2022, the Amazon ECS-optimized Windows Server 20H2 Core AMI reached its end of support date. No new
versions of this AMI will be released. For more information, see [Windows Server release information](https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info").

Windows Server 2025, Windows Server 2022, Windows Server 2019, and Windows Server 2016
are Long-Term Servicing Channel (LTSC) releases. Windows Server 20H2 is a Semi-Annual
Channel (SAC) release. For more information, see [Windows Server release information](https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info "https://learn.microsoft.com/en-us/windows-server/get-started/windows-server-release-info").

### Considerations

Here are some things you should know about Amazon EC2 Windows containers and
Amazon ECS.

- Windows containers can't run on Linux container instances, and the
  opposite is also the case. For better task placement for Windows and Linux
  tasks, keep Windows and Linux container instances in separate clusters and
  only place Windows tasks on Windows clusters. You can ensure that Windows
  task definitions are only placed on Windows instances by setting the
  following placement constraint:
  `memberOf(ecs.os-type=='windows')`.
- Windows containers are supported for tasks that use the EC2
  and Fargate.
- Windows containers and container instances can't support all the task
  definition parameters that are available for Linux containers and container
  instances. For some parameters, they aren't supported at all, and others
  behave differently on Windows than they do on Linux. For more information,
  see [Amazon ECS task definition differences for EC2 instances running Windows](windows_task_definitions.md "windows_task_definitions.md").
- For the IAM roles for tasks feature, you need to configure your Windows
  container instances to allow the feature at launch. Your containers must run
  some provided PowerShell code when they use the feature. For more
  information, see [Amazon EC2 Windows instance additional configuration](task-iam-roles.md#windows_task_IAM_roles "task-iam-roles.md#windows_task_IAM_roles").
- The IAM roles for tasks feature uses a credential proxy to provide
  credentials to the containers. This credential proxy occupies port 80 on the
  container instance, so if you use IAM roles for tasks, port 80 is not
  available for tasks. For web service containers, you can use an Application Load Balancer and
  dynamic port mapping to provide standard HTTP port 80 connections to your
  containers. For more information, see [Use load balancing to distribute Amazon ECS service traffic](service-load-balancing.md "service-load-balancing.md").
- The Windows Server Docker images are large (9 GiB). So, your Windows
  container instances require more storage space than Linux container
  instances.
- To run a Windows container on a Windows Server, the container’s base image
  OS version must match that of the host. For more information, see [Windows container version compatibility](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-2022%2Cwindows-11 "https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility?tabs=windows-server-2022%2Cwindows-11") on the Microsoft
  documentation website. If your cluster runs multiple Windows versions, you
  can ensure that a task is placed on an EC2 instance running on the same
  version by using the placement constraint:
  `memberOf(attribute:ecs.os-family ==
WINDOWS_SERVER_<OS_Release>_<FULL or CORE>)`. For more
  information, see [Retrieving Amazon ECS-optimized Windows AMI metadata](retrieve-ecs-optimized_windows_AMI.md "retrieve-ecs-optimized_windows_AMI.md").

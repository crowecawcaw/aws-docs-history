# Amazon ECS clusters for external instances

Amazon ECS Anywhere provides support for registering an _external instance_
such as an on-premises server or virtual machine (VM), to your Amazon ECS cluster. External
instances are optimized for running applications that generate outbound traffic or process
data. If your application requires inbound traffic, the lack of ELB support makes running
these workloads less efficient. Amazon ECS added a new `EXTERNAL` launch type that you
can use to create services or run tasks on your external instances.

## Supported operating systems and system

architectures

The following is the list of supported operating systems and system
architectures.

- Amazon Linux 2
- Amazon Linux 2023
- CentOS Stream 9
- RHEL 7, RHEL 8, RHEL 9 — Neither Docker or RHEL's open package
  repositories support installing Docker natively on RHEL. You must ensure that
  Docker is installed before you run the install script that's described in this
  document.
- Fedora 32, Fedora 33, Fedora 40
- openSUSE Tumbleweed
- Ubuntu 18, Ubuntu 20, Ubuntu 22, Ubuntu 24
- Debian 10

###### Important

Debian 9 Long Term Support (LTS support) ended on June 30, 2022 and is no
longer supported by Amazon ECS Anywhere.

- Debian 11
- Debian 12
- SUSE Enterprise Server 15
- The `x86_64` and `ARM64` CPU architectures are
  supported.
- The following Windows operating system versions are supported:
  - Windows Server 2022
  - Windows Server 2019
  - Windows Server 2016
  - Windows Server 20H2

## Considerations

Before you start using external instances, be aware of the following
considerations.

- You can register an external instance to one cluster at a time. For
  instructions on how to register an external instance with a different cluster,
  see [Deregistering an Amazon ECS external instance](ecs-anywhere-deregistration.md "ecs-anywhere-deregistration.md").
- Your external instances require an IAM role that allows them to communicate
  with AWS APIs. For more information, see [Amazon ECS Anywhere IAM role](iam-role-ecsanywhere.md "iam-role-ecsanywhere.md").
- Your external instances should not have a preconfigured instance credential
  chain defined locally as this will interfere with the registration
  script.
- To send container logs to CloudWatch Logs, make sure that you create and specify a task
  execution IAM role in your task definition.
- When an external instance is registered to a cluster, the
  `ecs.capability.external` attribute is associated with the
  instance. This attribute identifies the instance as an external instance. You
  can add custom attributes to your external instances to use as a task placement
  constraint. For more information, see [Custom attributes](task-placement-constraints.md#ecs-custom-attributes "task-placement-constraints.md#ecs-custom-attributes").
- You can add resource tags to your external instance. For more information, see
  [Adding tags to External container
  instances for Amazon ECS](instance-details-tags-external.md "instance-details-tags-external.md").
- ECS Exec is supported on external instances. For more information, see [Monitor Amazon ECS containers with ECS Exec](ecs-exec.md "ecs-exec.md").
- The following are additional considerations that are specific to networking
  with your external instances. For more information, see [Networking](#ecs-anywhere-networking "#ecs-anywhere-networking") .
  - Service load balancing isn't supported.
  - Service discovery isn't supported.
  - Tasks that run on external instances must use the `bridge`,
    `host`, or `none` network modes. The
    `awsvpc` network mode isn't supported.
  - There are Amazon ECS service domains in each AWS Region. These service
    domains must be allowed to send traffic to your external
    instances.
  - The SSM Agent installed on your external instance maintains IAM
    credentials that are rotated every 30 minutes using a hardware
    fingerprint. If your external instance loses connection to AWS, the
    SSM Agent automatically refreshes the credentials after the connection
    is re-established. For more information, see [Validating on-premises servers and virtual machines using a
    hardware fingerprint](../../../systems-manager/latest/userguide/ssm-agent-technical-details.md#fingerprint-validation "../../../systems-manager/latest/userguide/ssm-agent-technical-details.md#fingerprint-validation") in the
    _AWS Systems Manager User Guide_.
  - You can run Linux tasks on external instances in an IPv6-only
    configuration as long as the instances are in IPv6-only subnets. For more information, see [Using a VPC in IPv6-only mode](task-networking.md#networking-ipv6-only "task-networking.md#networking-ipv6-only").

- The `UpdateContainerAgent` API isn't supported. For instructions on
  how to update the SSM Agent or the Amazon ECS agent on your external instances, see
  [Updating the AWS Systems Manager agent and Amazon ECS container
  agent on an external instance](ecs-anywhere-updates.md "ecs-anywhere-updates.md").
- Amazon ECS capacity providers aren't supported. To create a service or run a
  standalone task on your external instances, use the `EXTERNAL` launch
  type.
- SELinux isn't supported.
- Using Amazon EFS volumes or specifying an `EFSVolumeConfiguration` isn't
  supported.
- Integration with App Mesh isn't supported.
- If you use the console to create an external instance task definition, you
  must create the task definition with the console JSON editor.
- When you run ECS Anywhere on Windows, you must use your own Windows license on
  the on-premises infrastructure.
- When you use a non Amazon ECS-optimized AMI, run the following commands on the
  external container instance to configure rules to use IAM roles for tasks. For
  more information, see [External instance additional
  configuration](task-iam-roles.md#enable_task_iam_roles "task-iam-roles.md#enable_task_iam_roles").

```
$ sysctl -w net.ipv4.conf.all.route_localnet=1
$ iptables -t nat -A PREROUTING -p tcp -d 169.254.170.2 --dport 80 -j DNAT --to-destination 127.0.0.1:51679
$ iptables -t nat -A OUTPUT -d 169.254.170.2 -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 51679
```

### Networking

Amazon ECS external instances are optimized for running applications that generate
outbound traffic or process data. If your application requires inbound traffic, such
as a web service, the lack of ELB support makes running these workloads less
efficient because there isn't support for placing these workloads behind a load
balancer.

The following are additional considerations that are specific to networking with
your external instances.

- Service load balancing isn't supported.
- Service discovery isn't supported.
- Linux tasks that run on external instances must use the
  `bridge`, `host`, or `none` network
  modes. The `awsvpc` network mode isn't supported.

For more information about each network mode, see [Amazon ECS task networking options for EC2 instances](task-networking.md "task-networking.md").

- Windows tasks that run on external instances must use the
  `default` network mode.
- You can run Linux tasks on external instances in an IPv6-only
  configuration as long as the instances are in IPv6-only subnets. For more information, see [Using a VPC in IPv6-only mode](task-networking.md#networking-ipv6-only "task-networking.md#networking-ipv6-only").
- There are Amazon ECS service domains in each Region and must be
  allowed to send traffic to your external instances.
- The SSM Agent installed on your external instance maintains IAM
  credentials that are rotated every 30 minutes using a hardware fingerprint.
  If your external instance loses connection to AWS, the SSM Agent
  automatically refreshes the credentials after the connection is
  re-established. For more information, see [Validating on-premises servers and virtual machines using a hardware
  fingerprint](../../../systems-manager/latest/userguide/ssm-agent-technical-details.md#fingerprint-validation "../../../systems-manager/latest/userguide/ssm-agent-technical-details.md#fingerprint-validation") in the _AWS Systems Manager User Guide_.

The following domains are used for communication between the Amazon ECS service and the
Amazon ECS agent that's installed on your external instance. Make sure that traffic is
allowed and that DNS resolution works. For each endpoint,
`region` represents the Region identifier for an AWS
Region that's supported by Amazon ECS, such as `us-east-2` for the
US East (Ohio) Region. The endpoints for all Regions that you use should be
allowed. For the `ecs-a` and `ecs-t` endpoints, you should
include an asterisk (for example, `ecs-a-*`).

- `ecs-a-*.`region`.amazonaws.com`
  — This endpoint is used when managing tasks.
- `ecs-t-*.`region`.amazonaws.com`
  — This endpoint is used to manage task and container metrics.
- `ecs.`region`.amazonaws.com` —
  This is the service endpoint for Amazon ECS.
- `ssm.`region`.amazonaws.com` —
  This is the service endpoint for AWS Systems Manager.
- `ec2messages.`region`.amazonaws.com`
  — This is the service endpoint that AWS Systems Manager uses to communicate
  between the Systems Manager agent and the Systems Manager service in the cloud.
- `ssmmessages.`region`.amazonaws.com`
  — This is the service endpoint that is required to create and delete
  session channels with the Session Manager service in the cloud.
- If your tasks require communication with any other AWS services, make
  sure that those service endpoints are allowed. Example applications include
  using Amazon ECR to pull container images or using CloudWatch for CloudWatch Logs. For more
  information, see [Service
  endpoints](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the _AWS General
  Reference_.

### Amazon FSx for Windows File Server with ECS

Anywhere

In order to use the Amazon FSx for Windows File Server with Amazon ECS external instances you
must establish a connection between your on-premises data center and the
AWS Cloud. For information about the options for connecting your network to your
VPC, see [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md "../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md").

### gMSA with ECS Anywhere

The following use cases are supported for ECS Anywhere.

- The Active Directory is in the AWS Cloud - For this configuration, you
  create a connection between your on-premises network and the AWS Cloud
  using an AWS Direct Connect connection. For information about how to create the
  connection, see [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md "../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md").You create an Active Directory
  in the AWS Cloud. For information about how to get started with AWS Directory Service,
  see [Setting up
  AWS Directory Service](../../../directoryservice/latest/admin-guide/setting_up.md "../../../directoryservice/latest/admin-guide/setting_up.md") in the _AWS Directory Service
  Administration Guide_. You can then join your external
  instances to the domain using the AWS Direct Connect connection. For information
  about working with gMSA with Amazon ECS, see [Learn how to use gMSAs for EC2 Windows containers for Amazon ECS](windows-gmsa.md "windows-gmsa.md").
- The Active Directory is in the on-premises data center. - For this
  configuration, you join your external instances to the on-premises Active
  Directory. You then use the locally available credentials when you run the
  Amazon ECS tasks.

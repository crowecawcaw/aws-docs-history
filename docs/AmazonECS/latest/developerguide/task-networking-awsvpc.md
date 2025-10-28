# Allocate a network interface for an Amazon ECS

task

The task networking features that are provided by the `awsvpc` network mode
give Amazon ECS tasks the same networking properties as Amazon EC2 instances. Using the
`awsvpc` network mode simplifies container networking, because you have
more control over how your applications communicate with each other and other services
within your VPCs. The `awsvpc` network mode also provides greater security
for your containers by allowing you to use security groups and network monitoring tools
at a more granular level within your tasks. You can also use other Amazon EC2 networking
features such as VPC Flow Logs to monitor traffic to and from your tasks. Additionally,
containers that belong to the same task can communicate over the `localhost`
interface.

The task elastic network interface (ENI) is a fully managed feature of Amazon ECS. Amazon ECS
creates the ENI and attaches it to the host Amazon EC2 instance with the specified security
group. The task sends and receives network traffic over the ENI in the same way that
Amazon EC2 instances do with their primary network interfaces. Each task ENI is assigned a
private IPv4 address by default. If your VPC is enabled for dual-stack mode and you use
a subnet with an IPv6 CIDR block, the task ENI will also receive an IPv6 address. Each
task can only have one ENI.

These ENIs are visible in the Amazon EC2 console for your account. Your account can't
detach or modify the ENIs. This is to prevent accidental deletion of an ENI that is
associated with a running task. You can view the ENI attachment information for tasks in
the Amazon ECS console or with the [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md") API operation. When the task stops or if the service is
scaled down, the task ENI is detached and deleted.

When you need increased ENI density, use the `awsvpcTrunking` account
setting. Amazon ECS also creates and attaches a "trunk" network interface for your container
instance. The trunk network is fully managed by Amazon ECS. The trunk ENI is deleted when you
either terminate or deregister your container instance from the Amazon ECS cluster. For more
information about the `awsvpcTrunking` account setting, see [Prerequisites](container-instance-eni.md#eni-trunking-launching "container-instance-eni.md#eni-trunking-launching").

You specify `awsvpc` in the `networkMode` parameter of the task
definition. For more information, see [Network mode](task_definition_parameters.md#network_mode "task_definition_parameters.md#network_mode").

Then, when you run a task or create a service, use the
`networkConfiguration` parameter that includes one or more subnets to
place your tasks in and one or more security groups to attach to an ENI. For more
information, see [Network configuration](service_definition_parameters.md#sd-networkconfiguration "service_definition_parameters.md#sd-networkconfiguration"). The tasks are placed on compatible Amazon EC2
instances in the same Availability Zones as those subnets, and the specified security
groups are associated with the ENI that's provisioned for the task.

## Linux considerations

Consider the following when using the Linux operating system.

- If you use a p5.48xlarge instance in `awsvpc` mode, you can't
  run more than 1 task on the instance.
- Tasks and services that use the `awsvpc` network mode require
  the Amazon ECS service-linked role to provide Amazon ECS with the permissions to make
  calls to other AWS services on your behalf. This role is created for you
  automatically when you create a cluster or if you create or update a
  service, in the AWS Management Console. For more information, see [Using service-linked roles for
  Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md"). You can also create the
  service-linked role with the following AWS CLI command:

```
`aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com`
```

- Your Amazon EC2 Linux instance requires version `1.15.0` or later of
  the container agent to run tasks that use the `awsvpc` network
  mode. If you're using an Amazon ECS-optimized AMI, your instance needs at least
  version `1.15.0-4` of the `ecs-init` package as
  well.
- Amazon ECS populates the hostname of the task with an Amazon-provided
  (internal) DNS hostname when both the `enableDnsHostnames` and
  `enableDnsSupport` options are enabled on your VPC. If these
  options aren't enabled, the DNS hostname of the task is set to a random
  hostname. For more information about the DNS settings for a VPC, see [Using DNS
  with Your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
  _Amazon VPC User Guide_.
- Each Amazon ECS task that uses the `awsvpc` network mode receives
  its own elastic network interface (ENI), which is attached to the Amazon EC2
  instance that hosts it. There's a default quota for the number of network
  interfaces that can be attached to an Amazon EC2 Linux instance. The primary
  network interface counts as one toward that quota. For example, by default,
  a `c5.large` instance might have only up to three ENIs that can
  be attached to it. The primary network interface for the instance counts as
  one. You can attach an additional two ENIs to the instance. Because each
  task that uses the `awsvpc` network mode requires an ENI, you can
  typically only run two such tasks on this instance type. For more
  information about the default ENI limits for each instance type, see [IP addresses per
  network interface per instance type](../../../AWSEC2/latest/UserGuide/using-eni.md#AvailableIpPerENI "../../../AWSEC2/latest/UserGuide/using-eni.md#AvailableIpPerENI") in the
  _Amazon EC2 User Guide_.
- Amazon ECS supports the launch of Amazon EC2 Linux instances that use supported
  instance types with increased ENI density. When you opt in to the
  `awsvpcTrunking` account setting and register Amazon EC2 Linux
  instances that use these instance types to your cluster, these instances
  have higher ENI quota. Using these instances with this higher quota means
  that you can place more tasks on each Amazon EC2 Linux instance. To use the
  increased ENI density with the trunking feature, your Amazon EC2 instance must
  use version `1.28.1` or later of the container agent. If you're
  using an Amazon ECS-optimized AMI, your instance also requires at least version
  `1.28.1-2` of the `ecs-init` package. For more
  information about opting in to the `awsvpcTrunking` account
  setting, see [Access Amazon ECS features with account settings](ecs-account-settings.md "ecs-account-settings.md"). For more information about ENI
  trunking, see [Increasing Amazon ECS Linux container instance network
  interfaces](container-instance-eni.md "container-instance-eni.md").
- When hosting tasks that use the `awsvpc` network mode on Amazon EC2
  Linux instances, your task ENIs aren't given public IP addresses. To access
  the internet, tasks must be launched in a private subnet that's configured
  to use a NAT gateway. For more information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
  _Amazon VPC User Guide_. Inbound network access must be
  from within a VPC that uses the private IP address or routed through a load
  balancer from within the VPC. Tasks that are launched within public subnets
  do not have access to the internet.
- Amazon ECS recognizes only the ENIs that it attaches to your Amazon EC2 Linux
  instances. If you manually attached ENIs to your instances, Amazon ECS might
  attempt to add a task to an instance that doesn't have enough network
  adapters. This can result in the task timing out and moving to a
  deprovisioning status and then a stopped status. We recommend that you don't
  attach ENIs to your instances manually.
- Amazon EC2 Linux instances must be registered with the
  `ecs.capability.task-eni` capability to be considered for
  placement of tasks with the `awsvpc` network mode. Instances
  running version `1.15.0-4` or later of `ecs-init` are
  registered with this attribute automatically.
- The ENIs that are created and attached to your Amazon EC2 Linux instances
  cannot be detached manually or modified by your account. This is to prevent
  the accidental deletion of an ENI that is associated with a running task. To
  release the ENIs for a task, stop the task.
- There is a limit of 16 subnets and 5 security groups that are able to be
  specified in the `awsVpcConfiguration` when running a task or
  creating a service that uses the `awsvpc` network mode. For more
  information, see [AwsVpcConfiguration](../APIReference/API_AwsVpcConfiguration.md "../APIReference/API_AwsVpcConfiguration.md") in the
  _Amazon Elastic Container Service API Reference_.
- When a task is started with the `awsvpc` network mode, the
  Amazon ECS container agent creates an additional `pause` container for
  each task before starting the containers in the task definition. It then
  configures the network namespace of the `pause` container by
  running the [amazon-ecs-cni-plugins](https://github.com/aws/amazon-ecs-cni-plugins "https://github.com/aws/amazon-ecs-cni-plugins") CNI plugins. The agent then starts the
  rest of the containers in the task so that they share the network stack of
  the `pause` container. This means that all containers in a task
  are addressable by the IP addresses of the ENI, and they can communicate
  with each other over the `localhost` interface.
- Services with tasks that use the `awsvpc` network mode only
  support Application Load Balancer and Network Load Balancer. When you create any target groups for these
  services, you must choose `ip` as the target type. Do not use
  `instance`. This is because tasks that use the
  `awsvpc` network mode are associated with an ENI, not with an
  Amazon EC2 Linux instance. For more information, see [Use load balancing to distribute Amazon ECS service
  traffic](service-load-balancing.md "service-load-balancing.md").
- If your VPC is updated to change the DHCP options set it uses, you can't
  apply these changes to existing tasks. Start new tasks with these changes
  applied to them, verify that they are working correctly, and then stop the
  existing tasks in order to safely change these network
  configurations.

## Windows considerations

The following are considerations when you use the Windows operating
system:

- Container instances using the Amazon ECS optimized Windows Server 2016 AMI
  can't host tasks that use the `awsvpc` network mode. If you have
  a cluster that contains Amazon ECS optimized Windows Server 2016 AMIs and
  Windows AMIs that support `awsvpc` network mode, tasks that use
  `awsvpc` network mode aren't launched on the Windows 2016
  Server instances. Rather, they're launched on instances that support
  `awsvpc` network mode.
- Your Amazon EC2 Windows instance requires version `1.57.1` or later
  of the container agent to use CloudWatch metrics for Windows containers that use
  the `awsvpc` network mode.
- Tasks and services that use the `awsvpc` network mode require
  the Amazon ECS service-linked role to provide Amazon ECS with the permissions to make
  calls to other AWS services on your behalf. This role is created for you
  automatically when you create a cluster, or if you create or update a
  service, in the AWS Management Console. For more information, see [Using service-linked roles for
  Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md"). You can also create the
  service-linked role with the following AWS CLI command.

```
`aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com`
```

- Your Amazon EC2 Windows instance requires version `1.54.0` or later
  of the container agent to run tasks that use the `awsvpc` network
  mode. When you bootstrap the instance, you must configure the options that
  are required for `awsvpc` network mode. For more information, see
  [Bootstrapping Amazon ECS Windows container instances to pass data](bootstrap_windows_container_instance.md "bootstrap_windows_container_instance.md").
- Amazon ECS populates the hostname of the task with an Amazon provided
  (internal) DNS hostname when both the `enableDnsHostnames` and
  `enableDnsSupport` options are enabled on your VPC. If these
  options aren't enabled, the DNS hostname of the task is a random hostname.
  For more information about the DNS settings for a VPC, see [Using DNS
  with Your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
  _Amazon VPC User Guide_.
- Each Amazon ECS task that uses the `awsvpc` network mode receives
  its own elastic network interface (ENI), which is attached to the Amazon EC2
  Windows instance that hosts it. There is a default quota for the number of
  network interfaces that can be attached to an Amazon EC2 Windows instance. The
  primary network interface counts as one toward this quota. For example, by
  default a `c5.large` instance might have only up to three ENIs
  attached to it. The primary network interface for the instance counts as one
  of those. You can attach an additional two ENIs to the instance. Because
  each task using the `awsvpc` network mode requires an ENI, you
  can typically only run two such tasks on this instance type. For more
  information about the default ENI limits for each instance type, see [IP addresses per
  network interface per instance type](../../../AWSEC2/latest/WindowsGuide/using-eni.md#AvailableIpPerENI "../../../AWSEC2/latest/WindowsGuide/using-eni.md#AvailableIpPerENI") in the
  _Amazon EC2 User Guide_.
- When hosting tasks that use the `awsvpc` network mode on Amazon EC2
  Windows instances, your task ENIs aren't given public IP addresses. To
  access the internet, launch tasks in a private subnet that's configured to
  use a NAT gateway. For more information, see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
  _Amazon VPC User Guide_. Inbound network access must be
  from within the VPC that is using the private IP address or routed through a
  load balancer from within the VPC. Tasks that are launched within public
  subnets don't have access to the internet.
- Amazon ECS recognizes only the ENIs that it has attached to your Amazon EC2 Windows
  instance. If you manually attached ENIs to your instances, Amazon ECS might
  attempt to add a task to an instance that doesn't have enough network
  adapters. This can result in the task timing out and moving to a
  deprovisioning status and then a stopped status. We recommend that you don't
  attach ENIs to your instances manually.
- Amazon EC2 Windows instances must be registered with the
  `ecs.capability.task-eni` capability to be considered for
  placement of tasks with the `awsvpc` network mode.
- You can't manually modify or detach ENIs that are created and attached to
  your Amazon EC2 Windows instances. This is to prevent you from accidentally
  deleting an ENI that's associated with a running task. To release the ENIs
  for a task, stop the task.
- You can only specify up to 16 subnets and 5 security groups in
  `awsVpcConfiguration` when you run a task or create a service
  that uses the `awsvpc` network mode. For more information, see
  [AwsVpcConfiguration](../APIReference/API_AwsVpcConfiguration.md "../APIReference/API_AwsVpcConfiguration.md") in the
  _Amazon Elastic Container Service API Reference_.
- When a task is started with the `awsvpc` network mode, the
  Amazon ECS container agent creates an additional `pause` container for
  each task before starting the containers in the task definition. It then
  configures the network namespace of the `pause` container by
  running the [amazon-ecs-cni-plugins](https://github.com/aws/amazon-ecs-cni-plugins "https://github.com/aws/amazon-ecs-cni-plugins") CNI plugins. The agent then starts the
  rest of the containers in the task so that they share the network stack of
  the `pause` container. This means that all containers in a task
  are addressable by the IP addresses of the ENI, and they can communicate
  with each other over the `localhost` interface.
- Services with tasks that use the `awsvpc` network mode only
  support Application Load Balancer and Network Load Balancer. When you create any target groups for these
  services, you must choose `ip` as the target type, not
  `instance`. This is because tasks that use the
  `awsvpc` network mode are associated with an ENI, not with an
  Amazon EC2 Windows instance. For more information, see [Use load balancing to distribute Amazon ECS service
  traffic](service-load-balancing.md "service-load-balancing.md").
- If your VPC is updated to change the DHCP options set it uses, you can't
  apply these changes to existing tasks. Start new tasks with these changes
  applied to them, verify that they are working correctly, and then stop the
  existing tasks in order to safely change these network
  configurations.
- The following are not supported when you use `awsvpc` network
  mode in an EC2 Windows configuration:
  - Dual-stack configuration
  - IPv6
  - ENI trunking

## Using a VPC in dual-stack

mode

When using a VPC in dual-stack mode, your tasks can communicate over IPv4, or
IPv6, or both. IPv4 and IPv6 addresses are independent of each other. Therefore you
must configure routing and security in your VPC separately for IPv4 and IPv6. For
more information about how to configure your VPC for dual-stack mode, see [Migrating
to IPv6](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the _Amazon VPC User Guide_.

If you configured your VPC with an internet gateway or an outbound-only internet
gateway, you can use your VPC in dual-stack mode. By doing this, tasks that are
assigned an IPv6 address can access the internet through an internet gateway or an
egress-only internet gateway. NAT gateways are optional. For more information, see
[Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") and [Egress-only
internet gateways](../../../vpc/latest/userguide/egress-only-internet-gateway.md "../../../vpc/latest/userguide/egress-only-internet-gateway.md") in the _Amazon VPC User Guide_.

Amazon ECS tasks are assigned an IPv6 address if the following conditions are
met:

- The Amazon EC2 Linux instance that hosts the task is using version
  `1.45.0` or later of the container agent. For information
  about how to check the agent version your instance is using, and updating it
  if needed, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
- The `dualStackIPv6` account setting is enabled. For more
  information, see [Access Amazon ECS features with account settings](ecs-account-settings.md "ecs-account-settings.md").
- Your task is using the `awsvpc` network mode.
- Your VPC and subnet are configured for IPv6. The configuration includes
  the network interfaces that are created in the specified subnet. For more
  information about how to configure your VPC for dual-stack mode, see [Migrating to IPv6](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") and [Modify the
  IPv6 addressing attribute for your subnet](../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-ipv6 "../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-ipv6") in the
  _Amazon VPC User Guide_.

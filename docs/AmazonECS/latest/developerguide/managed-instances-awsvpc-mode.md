# Allocate a network interface for tasks

on Amazon ECS Managed Instances

Using the `awsvpc` network mode in Amazon ECS Managed Instances simplifies container
networking because you have more control over how your applications communicate with
each other and other services within your VPCs. The `awsvpc` network mode
also provides greater security for your containers by allowing you to use security
groups and network monitoring tools at a more granular level within your tasks.

By default, every Amazon ECS Managed Instances instance has a trunk Elastic Network Interface
(ENI) attached during launch as a primary ENI when the instance type supports trunking.
For more information about instance types that support ENI trunking, see [Supported instances for increased Amazon ECS container network
interfaces](eni-trunking-supported-instance-types.md "eni-trunking-supported-instance-types.md").

###### Note

When the chosen instance type doesn't support trunk ENIs, the instance will be
launched with a regular ENI.

Each task that runs on the instance receives its own ENI attached to the trunk ENI,
with a primary private IP address. If your VPC is configured for dual-stack mode and you
use a subnet with an IPv6 CIDR block, the ENI also receives an IPv6 address. When using
a public subnet, you can optionally assign a public IP address to the Amazon ECS Managed Instance
primary ENI by enabling IPv4 public addressing for the subnet. For more
information, see [Modify the IP addressing
attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md") in _Amazon VPC User Guide_. A task
can only have one ENI that's associated with it at a time.

Containers that belong to the same task can also communicate over the
`localhost` interface. For more information about VPCs and subnets, see
[How Amazon VPC
works](../../../vpc/latest/userguide/how-it-works.md "../../../vpc/latest/userguide/how-it-works.md") in the _Amazon VPC User Guide_

The following operations use the primary ENI attached to the instance:

- **Image downloads** - Container images are
  downloaded from Amazon ECR through the primary ENI.
- **Secrets retrieval** - Secrets Manager secrets and other
  credentials are retrieved through the primary ENI.
- **Log uploads** - Logs are uploaded to CloudWatch
  through the primary ENI.
- **Environment file downloads** - Environment
  files are downloaded through the primary ENI.
  Application traffic flows through the task ENI.

Because each task gets its own ENI, you can use networking features such as VPC Flow
Logs, which you can use to monitor traffic to and from your tasks. For more information,
see [VPC Flow
Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the _Amazon VPC User Guide_.

You can also take advantage of AWS PrivateLink. You can configure a VPC interface
endpoint so that you can access Amazon ECS APIs through private IP addresses. AWS PrivateLink
restricts all network traffic between your VPC and Amazon ECS to the Amazon network. You
don't need an internet gateway, a NAT device, or a virtual private gateway. For more
information, see [Amazon ECS interface VPC
endpoints (AWS PrivateLink)](vpc-endpoints.md "vpc-endpoints.md").

The `awsvpc` network mode also allows you to leverage Amazon VPC Traffic
Mirroring for security and monitoring of network traffic when using instance types that don't have trunk ENIs attached. For more information, see
[What is Traffic
Mirroring?](../../../vpc/latest/mirroring/what-is-traffic-mirroring.md "../../../vpc/latest/mirroring/what-is-traffic-mirroring.md") in the _Amazon VPC Traffic Mirroring Guide_.

## Considerations for

`awsvpc` mode

- Tasks require the Amazon ECS service-linked role for ENI management. This role
  is created automatically when you create a cluster or service.
- Task ENIs are managed by Amazon ECS and cannot be manually detached or
  modified.
- Assigning a public IP address to the task ENI using
  `assignPublicIp` when running a standalone task (`RunTask`) or creating or updating a service (`CreateService`/`UpdateService`) is not supported.
- When you configure `awsvpc` networking at the task level, you
  must use the same VPC that you specified as part of the Amazon ECS Managed Instances
  capacity provider's launch template. You can use different subnets and
  security groups from those specified in the launch template.
- For `awsvpc` network mode tasks, use `ip` target
  type when configuring load balancer target groups. Amazon ECS automatically
  manages target group registration for supported networking modes.

## Using a VPC in

dual-stack mode

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

- The Amazon ECS Managed Instances instance that hosts the task is using version
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

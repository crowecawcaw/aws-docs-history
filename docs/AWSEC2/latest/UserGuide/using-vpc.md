# Virtual private clouds for your EC2 instances

Amazon Virtual Private Cloud (Amazon VPC) enables you to define a virtual network in your own logically isolated
area within the AWS cloud, known as a _virtual private cloud_ or
_VPC_. You can create AWS resources, such as Amazon EC2 instances, into
the subnets of your VPC. Your VPC closely resembles a traditional network that you might
operate in your own data center, with the benefits of using scalable infrastructure from
AWS. You can configure your VPC; you can select its IP address range, create subnets,
and configure route tables, network gateways, and security settings. You can connect
instances in your VPC to the internet or to your own data center.

###### Contents

- [Your default VPCs](#default-vpcs "#default-vpcs")
- [Nondefault VPCs](#create-nondefault-vpcs "#create-nondefault-vpcs")
- [Internet access](#access-internet-from-vpc "#access-internet-from-vpc")
- [Shared subnets](#ec2-shared-VPC-subnets "#ec2-shared-VPC-subnets")
- [IPv6-only subnets](#ec2-ipv6-only-subnets "#ec2-ipv6-only-subnets")

## Your default VPCs

When you create your AWS account, we create a _default VPC_ in each
Region. A default VPC is a VPC that is already configured and ready for you to use. For
example, there is a default subnet for each Availability Zone in each default VPC, an
internet gateway attached to the VPC, and there's a route in the main route table that
sends all traffic (0.0.0.0/0) to the internet gateway. You can modify the configuration
of your default VPCs as needed. For example, you can add subnets and route tables.

![We create a default VPC in each Region, with a default subnet in each Availability Zone.](images/default-vpc.png)

## Nondefault VPCs

Instead of using a default VPC for your resources, you can create your own VPC, as described in
[Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the _Amazon VPC User Guide_.

Here are some things to consider when creating a VPC for your EC2 instances.

- You can use the default suggestion for the IPv4 CIDR block or enter the CIDR block
  required by your application or network.
- To ensure high availability, create subnets in multiple Availability Zones.
- If your instances must be accessible from the internet, do one of the following:
  - If your instances can be in a public subnet, add public subnets. Keep
    both DNS options enabled. You can optionally add private subnets
    now or later on.
  - If your instances must be in a private subnet, add only private subnets.
    You can add a NAT gateway to provide internet access to instances in the
    private subnets. If your instances send or receive a significant
    volume of traffic across Availability Zones, create a NAT gateway in each
    Availability Zone. Otherwise, you can create a NAT gateway in just one
    of the Availability Zones and launch instances that send or receive
    cross-zone traffic in the same Availability Zone as the NAT gateway.

## Internet access

Instances launched into a default subnet in a default VPC have access to the internet,
as default VPCs are configured to assign public IP addresses and DNS hostnames, and the
main route table is configured with a route to an internet gateway attached to the VPC.

For instances that you launch in nondefault subnets and VPCs, you can use one of
the following options to ensure that the instances that you launch in these subnets
have access to the internet:

- Configure an internet gateway. For more information, see [Connect to the internet using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
  _Amazon VPC User Guide_.
- Configure a public NAT gateway. For more information, see [Access the internet
  from a private subnet](../../../vpc/latest/userguide/nat-gateway-scenarios.md#public-nat-internet-access "../../../vpc/latest/userguide/nat-gateway-scenarios.md#public-nat-internet-access") in the _Amazon VPC User Guide_.

## Shared subnets

When launching EC2 instances into shared VPC subnets, note the following:

- Participants can run instances in a shared subnet by specifying the ID of the shared
  subnet. Participants must own any network interfaces that they specify.
- Participants can start, stop, terminate, and describe instances that they've created
  in a shared subnet. Participants can't start, stop, terminate, or describe instances
  that the VPC owner created in the shared subnet.
- VPC owners can't start, stop, terminate, or describe instances created by participants
  in a shared subnet.
- Participants can connect to an instance in a shared subnet using EC2 Instance Connect Endpoint. The
  participant must create the EC2 Instance Connect Endpoint in the shared subnet. Participants can't use
  an EC2 Instance Connect Endpoint that the VPC owner created in the shared subnet.

For information about shared Amazon EC2 resources, see the following:

- [Manage AMI sharing with an organization or OU](share-amis-org-ou-manage.md "share-amis-org-ou-manage.md")
- [Shared Capacity Reservations](capacity-reservation-sharing.md "capacity-reservation-sharing.md")
- [Shared placement groups](share-placement-group.md "share-placement-group.md")
- [Cross-account Amazon EC2 Dedicated Host sharing](dh-sharing.md "dh-sharing.md")

For more information about shared subnets, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md")
in the _Amazon VPC User Guide_.

## IPv6-only subnets

An EC2 instance launched in an IPv6-only subnet receives an IPv6 address but not an IPv4 address.
Any instances that you launch into an IPv6-only subnet must be [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").

# AWS PCS VPC and subnet requirements

and considerations

When you create an AWS PCS cluster, you specify a VPC a subnet in that VPC. This topic
provides an overview of AWS PCS specific requirements and considerations for the VPC and
subnet(s) that you use with your cluster. If you don't have a VPC to use with AWS PCS,
you can create one using an AWS-provided AWS CloudFormation template. For more information about VPCs, see
[Virtual private
clouds (VPC)](../../../vpc/latest/userguide/configure-your-vpc.md "../../../vpc/latest/userguide/configure-your-vpc.md") in the _Amazon VPC User Guide_.

## VPC requirements and

considerations

When you create a cluster, the VPC that you specify must meet the following requirements and
considerations:

- The VPC must have a sufficient number of IP addresses available for the cluster, any
  nodes, and other cluster resources that you want to create. For more information, see [IP
  addressing for your VPCs and subnets](../../../eks/latest/userguide/network_reqs.md#network-requirements-vpc "../../../eks/latest/userguide/network_reqs.md#network-requirements-vpc") in the
  _Amazon VPC User Guide_.
- If your cluster uses IPv6:
  - Associate an IPv6 CIDR block with your VPC. For more information, see
    [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the _Amazon VPC User Guide_.

  ###### Important

  Although you can configure your VPC with both IPv4 and IPv6, you can only choose 1 network type for your cluster.
  - Enable **auto-assign IPv6 address** for your subnets.
  - For more information, see:
    - [IPv6 on AWS](../../../whitepapers/latest/ipv6-on-aws/IPv6-on-AWS.md "../../../whitepapers/latest/ipv6-on-aws/IPv6-on-AWS.md")
    - [Understanding
      IPv6 addressing on AWS and designing a scalable addressing plan](https://aws.amazon.com/blogs/networking-and-content-delivery/understanding-ipv6-addressing-on-aws-and-designing-a-scalable-addressing-plan "https://aws.amazon.com/blogs/networking-and-content-delivery/understanding-ipv6-addressing-on-aws-and-designing-a-scalable-addressing-plan")

- The VPC must have a DNS hostname and DNS resolution support. Otherwise, nodes can't
  register the customer cluster. For more information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
  _Amazon VPC User Guide_.
- The VPC might require VPC endpoints using AWS PrivateLink to be able to contact the
  AWS PCS API. For more information, see [Connect your VPC to services using
  AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") in the _Amazon VPC User Guide_.

###### Important

AWS PCS doesn't support a VPC with dedicated instance tenancy. The VPC you use for AWS PCS
must use `default` instance tenancy. You can change the instance tenancy for an
existing VPC. For more information, see [Change the instance tenancy of a VPC](../../../AWSEC2/latest/UserGuide/change-tenancy-vpc.md "../../../AWSEC2/latest/UserGuide/change-tenancy-vpc.md")
in the _Amazon Elastic Compute Cloud User Guide_.

## Subnet requirements and

considerations

When you create a Slurm cluster, AWS PCS creates an [Elastic Network Interface(ENI)](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
subnet you specified. This network interface enables communication between the scheduler
controller and the customer VPC. The network interface also enables Slurm to communicate with the
components deployed in your account. You can only specify the subnet for a cluster at
creation time.

### Subnet requirements

for clusters

The [subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types") that you specify
when you create a cluster must meet the following requirements:

- The subnet must have at least 1 IP address for use by AWS PCS.
- If your cluster uses IPv6, all of the subnets in your cluster must use IPv6.

###### Important

Compute node groups configured with AWS PCS sample AMIs and multiple network
interfaces won't work currently if the subnets are only configured to use IPv6.
Use dual-stack subnets (IPv4 and IPv6) or IPv4-only subnets instead. For more information,
see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md "working-with_ami_samples.md").

- The subnet can't reside in AWS Outposts, AWS Wavelength, or an AWS Local
  Zone.
- The subnet can be a public or private. We recommend that you specify a private
  subnet, if possible. A public subnet is a subnet with a route table that includes a route to
  an [internet
  gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md"); a private subnet is a subnet with a route table that doesn't include
  a route to an internet gateway.

### Subnet requirements for

nodes

You can deploy nodes and other cluster resources to the subnet you specify
when you create your AWS PCS cluster, and to other subnets in the same VPC.

Any subnet that you deploy nodes and cluster resources to
must meet the following requirements:

- You must ensure that the subnet has enough available IP addresses to deploy all the
  nodes and cluster resources.
- If your cluster uses IPv4 and you plan to deploy nodes to a public subnet,
  that subnet must auto-assign IPv4 public addresses.

###### Note

Instances in a public subnet must use a security group with inbound rules
that permit traffic from public IP addresses. Unless you have specific source
address restrictions, this means an IPv4 source address of 0.0.0.0/0
or an IPv6 source address of ::/0.

- If the subnet where you deploy nodes to is a private subnet and its route table doesn't
  include a route to a network address translation [(NAT) device](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md") (IPv4), add VPC endpoints using
  AWS PrivateLink to the customer VPC. VPC endpoints are needed for all the AWS services that
  the nodes contact. The only required endpoint is for AWS PCS to allow the node to call the
  `RegisterComputeNodeGroupInstance` API action. For more information, see
  [RegisterComputeNodeGroupInstance](../APIReference/API_RegisterComputeNodeGroupInstance.md "../APIReference/API_RegisterComputeNodeGroupInstance.md")
  in the _AWS PCS API Reference_.
- Public or private subnet status doesn't impact AWS PCS;
  the required endpoints must be reachable.

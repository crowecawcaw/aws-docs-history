# Create a VPC that uses an IPAM pool CIDR

With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a
logically isolated virtual network that you've defined. This virtual network closely resembles
a traditional network that you'd operate in your own data center, with the benefits of using
the scalable infrastructure of AWS.

A _virtual private cloud_ (VPC) is a virtual network
dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS
Cloud. You can specify an IP address range for the VPC, add subnets, add gateways, and
associate security groups.

Follow the steps in [Create
a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md") in the _Amazon VPC User Guide_. When you reach the step to
choose a CIDR for the VPC, you will have an option to use a CIDR from an IPAM pool.

If you choose the option to use an IPAM pool when you create the VPC, AWS allocates a
CIDR in the IPAM pool. You can view the allocation in IPAM by choosing a pool in the content
pane of the IPAM console and viewing the Resources tab for the pool.

###### Note

For complete instructions using the AWS CLI, including creating a VPC, see the [Tutorials for Amazon VPC IP Address Manager](tutorials-ipam.md "tutorials-ipam.md") section.

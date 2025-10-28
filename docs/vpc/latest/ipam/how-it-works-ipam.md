# How IPAM works

This topic explains some of the key concepts to help you get started with IPAM.

The following diagram shows an IPAM pool hierarchy for multiple AWS Regions within a
top-level IPAM pool. Each AWS Regional pool has two IPAM development pools within it, one pool
for pre-production and one pool production resources. For more information about IPAM concepts, see the descriptions below the diagram.

![IPAM pool how it works](images/ipam-example-1-570px.png)
To use Amazon VPC IP Address Manager, you first create an IPAM.

When you create the IPAM, you choose which AWS Region to create it in. When you create an
IPAM, AWS VPC IPAM automatically creates two scopes for the IPAM. The scopes, together with
pools and allocations, are key components of your IPAM.

- A **scope** is the highest-level container within IPAM. When you create IPAM, a default public scope and a default private scope are automatically created for you. Each scope represents the IP space for a single network.
  The **private scope** is intended for all the IP addresses that can't be advertised to the internet. The
  **public scope** is generally intended for all the IP addresses that can be advertised to the internet from AWS. Note that when [provisioning BYOIPv6 addresses to an IPAM pool](tutorials-byoip-ipam-console-ipv6.md "tutorials-byoip-ipam-console-ipv6.md"), you can configure the addresses to not be publicly advertisable though they are in the public scope.
  Scopes enable you to reuse IP addresses across multiple unconnected networks without causing
  IP address overlap or conflict. Within a scope, you create IPAM pools.
- A **pool** is a collection of contiguous IP address ranges
  (or CIDRs). IPAM pools enable you to organize your IP addresses according to your routing
  and security needs. You can have multiple pools within a top-level pool. For example, if you
  have separate routing and security needs for development and production applications, you
  can create a pool for each. Within IPAM pools, you allocate CIDRs to AWS resources.
- An **allocation** is a CIDR assignment from an IPAM pool to
  another resource or IPAM pool. When you create a VPC and choose an IPAM pool for the VPC’s
  CIDR, the CIDR is allocated from the CIDR provisioned to the IPAM pool. You can monitor and manage the allocation
  with IPAM.
  IPAM can manage and monitor public and private IPv6 space. For more information about public
  and private IPv6 addresses, see [IPv6 addresses](../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses "../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses") in
  the _Amazon VPC User Guide_.

To get started and create an IPAM, see [Getting started with IPAM](getting-started-ipam.md "getting-started-ipam.md").

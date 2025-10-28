# Allocate CIDRs from an IPAM pool

One important feature of IPAM is the ability to allocate and manage IP address space. When
creating a VPC, you must specify an IP address CIDR block, which defines the range of IP
addresses available for that VPC. IPAM simplifies this process by providing a global view of
your entire IP address inventory, helping you strategically assign and reuse IP prefixes across
multiple VPCs.

This address space allocation is crucial for ensuring there are no overlapping IP ranges,
which could cause routing conflicts and connectivity issues. IPAM also enables you to reserve IP
address space for future VPC expansion, avoiding the need for complex renumbering later.

Follow the steps in this section to allocate a CIDR from an IPAM pool to a resource.

###### Note

The terms _provision_ and _allocate_ are used throughout this user guide and the IPAM console. _Provision_ is used when you add a CIDR to an IPAM pool. _Allocate_ is used when you associate a CIDR from an IPAM pool with a
resource.

You can allocate CIDRs from an IPAM pool in the following ways:

- Use an AWS service that's integrated with IPAM, such as Amazon VPC, and select the option
  to use an IPAM pool for the CIDR. IPAM automatically creates the allocation in the pool for
  you.
- Manually allocate a CIDR within an IPAM pool to reserve it for later use with an AWS service that's integrated with IPAM, such as Amazon VPC.
  This section walks you through both options: how to use the AWS services integrated with
  IPAM to provision an IPAM pool CIDR, and how to manually reserve IP address space.

###### Contents

- [Create a VPC that uses an IPAM pool CIDR](create-vpc-ipam.md "create-vpc-ipam.md")
- [Manually allocate a CIDR to a pool to reserve IP address space](manually-allocate-ipam.md "manually-allocate-ipam.md")

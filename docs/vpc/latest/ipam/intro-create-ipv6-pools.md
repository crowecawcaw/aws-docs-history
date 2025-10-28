# Create IPv6 address pools in your IPAM

AWS offers IPv6 connectivity across many of its services, including EC2, VPC, and S3,
enabling you to use the increased address space and enhanced security features of IPv6. IPv6
was designed to resolve this fundamental limitation of IPv4. By moving to a 128-bit address
space, IPv6 offers a large number of unique IP addresses. This massive address expansion
enables the continued proliferation of connected technologies, from smartphones and IoT
devices to cloud infrastructure.

In addition, you can use IPAM to ensure that you are using contiguous IPv6 CIDRs for VPC
creation. Contiguously-allocated CIDRs are CIDRs that are allocated sequentially. They
enable you to simplify your security and networking rules; the IPv6 CIDRs can be aggregated
in a single entry across networking and security constructs like access control lists, route
tables, security groups, and firewalls.

Follow the steps in this section to create an IPAM IPv6 pool hierarchy. When you create
the pool, you can provision a CIDR for the pool to use. The pool assigns space within that
CIDR to allocations within the pool. An allocation is a CIDR assignment from an IPAM pool to
another resource or IPAM pool.

###### Note

Both public and private IPv6 addressing is available in AWS. AWS considers public
IP addresses those advertised on the internet from AWS, while private IP addresses are
not and cannot be advertised on the internet from AWS. If you want your private
networks to support IPv6 and have no intention of routing traffic from these addresses
to the internet, create your IPv6 pool in a private scope. For more information about
public and private IPv6 addresses, see [IPv6
addresses](../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses "../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses") in the _Amazon VPC User Guide_.

The following example shows the hierarchy of the pool structure that you can create with
instructions in this guide. In this section, you are creating an IPv6 IPAM
pool hierarchy:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Scope




      	- Regional pool in AWS Region 1 (2001:db8::/52)




      		* Development pool (2001:db8::/54)




      			+ Allocation for a VPC (2001:db8::/56)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  the Development pool within the Regional pool is provisioned with a portion of the Regional
  pool CIDR.

###### Contents

- [Create a Regional IPv6 address pool in your IPAM](create-ipv6-reg-pool.md "create-ipv6-reg-pool.md")
- [Create a development IPv6 address pool in your IPAM](create-ipv6-dev-pool.md "create-ipv6-dev-pool.md")

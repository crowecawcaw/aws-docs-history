# Create IPv4 pools

Follow the steps in this section to create an IPv4 IPAM pool hierarchy.

The following example shows the hierarchy of the pool structure that you can create with
instructions in this guide. In this section, you are creating an IPv4 IPAM
pool hierarchy:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Private scope




      	- Top-level pool (10.0.0.0/8)




      		* Regional pool in AWS Region 2 (10.0.0.0/16)




      			+ Development pool (10.0.0.0/24)




      				- Allocation for a VPC (10.0.0.0/25)

  In the preceding example, the CIDRs that are used are examples only. They illustrate that
  each pool within the top-level pool is provisioned with a portion of the top-level
  CIDR.

###### Contents

- [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md")
- [Create a Regional IPv4 pool](create-reg-ipam.md "create-reg-ipam.md")
- [Create a development IPv4 pool](create-dev-ipam.md "create-dev-ipam.md")

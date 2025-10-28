# Example IPAM pool plans

You can use IPAM
to suit the needs of your organization. This section provides examples of how you might organize your IP addresses.

## IPv4 pools in multiple AWS Regions

The following example shows an IPAM pool hierarchy for multiple AWS Regions within a
top-level pool. Each AWS Regional pool has two IPAM development pools within it, one
pool for development resources and one pool for production resources.

![IPAM pool hierarchy example 1](images/ipam-example-pool-base.png)

## IPv4 pools for multiple lines of business

The following example shows an IPAM pool hierarchy for multiple lines of business within a top-level
pool. Each pool for each line of business contains three AWS Regional pools. Each
Regional pool has two IPAM development pools within it, one pool for pre-production resources and
one pool for production resources.

![IPAM pool hierarchy example 2](images/ipam-example-2-914px.png)

## IPv6 pools in an AWS Region

The following example shows an IPAM IPv6 pool hierarchy for multiple lines of business
within a Regional pool. Each Regional pool has three IPAM pools within it, one pool for
sandbox resources, one pool for development resources, and one pool for production
resources.

![IPAM pool hierarchy example 3](images/ipam-example-34.png)

## Subnet pools for multiple lines of business

The following example shows a resource planning pool hierarchy for multiple lines of business
and dev/ prod subnet pools. For more information on subnet IP address space planning using IPAM, see [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md "tutorials-subnet-planning.md").

![IPAM pool hierarchy example 4](images/ipam-example-pool-subnet-integ.png)

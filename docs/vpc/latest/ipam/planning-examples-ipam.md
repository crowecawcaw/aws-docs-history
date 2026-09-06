

# Example IPAM pool plans
<a name="planning-examples-ipam"></a>

You can use IPAM to suit the needs of your organization. This section provides examples of how you might organize your IP addresses. 

## IPv4 pools in multiple AWS Regions
<a name="w2aab9c15c23b5"></a>

The following example shows an IPAM pool hierarchy for multiple AWS Regions within a top-level pool. Each AWS Regional pool has two IPAM development pools within it, one pool for development resources and one pool for production resources.

![IPAM pool hierarchy example 1.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-example-pool-base.png)


## IPv4 pools for multiple lines of business
<a name="w2aab9c15c23b7"></a>

The following example shows an IPAM pool hierarchy for multiple lines of business within a top-level pool. Each pool for each line of business contains three AWS Regional pools. Each Regional pool has two IPAM development pools within it, one pool for pre-production resources and one pool for production resources.

![IPAM pool hierarchy example 2.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-example-2-914px.png)


## IPv6 pools in an AWS Region
<a name="w2aab9c15c23b9"></a>

The following example shows an IPAM IPv6 pool hierarchy for multiple lines of business within a Regional pool. Each Regional pool has three IPAM pools within it, one pool for sandbox resources, one pool for development resources, and one pool for production resources.

![IPAM pool hierarchy example 3.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-example-34.png)


## Subnet pools for multiple lines of business
<a name="w2aab9c15c23c11"></a>

The following example shows a resource planning pool hierarchy for multiple lines of business and dev/ prod subnet pools. For more information on subnet IP address space planning using IPAM, see [Tutorial: Plan VPC IP address space for subnet IP allocations](tutorials-subnet-planning.md).

![IPAM pool hierarchy example 4.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-example-pool-subnet-integ.png)

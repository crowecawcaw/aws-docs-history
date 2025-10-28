# Plan for IP address provisioning

Follow the steps in this section to plan for IP address provisioning by using IPAM pools. If
you have configured an IPAM account, these steps should be completed by that account. The pool
creation process is different for pools in public and private scopes. This section includes
steps for creating a regional pool in the private scope. For BYOIP and BYOASN tutorials, see
[Tutorials](tutorials-ipam.md "tutorials-ipam.md").

###### Important

To use IPAM pools across AWS accounts, you must integrate IPAM with AWS Organizations
or some features may not work properly. For more information,
see [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md").

In IPAM, a pool is a collection of contiguous IP address ranges (or CIDRs). Pools enable you
to organize your IP addresses according to your routing and security needs. You can create pools
for AWS Regions outside of your IPAM Region. For example, if you have separate routing and
security needs for development and production applications, you can create a pool for
each.

In the first step in this section, you’ll create a top-level pool. Then, you’ll create a
Regional pool within the top-level pool. Within the Regional pool, you can create additional
pools as needed, such as a production and development environment pools. By default, you can
create pools up to a depth of 10. For information on IPAM quotas, see [Quotas for your IPAM](quotas-ipam.md "quotas-ipam.md").

###### Note

The terms _provision_ and _allocate_ are used throughout this user guide and the IPAM console. _Provision_ is used when you add a CIDR to an IPAM pool. _Allocate_ is used when you associate a CIDR from an IPAM pool with a
resource.

The following is an example hierarchy of the pool structure that you will create by
completing the steps in this section:

- IPAM operating in AWS Region 1 and AWS Region 2

      + Private scope




      	- Top-level pool




      		* Regional pool in AWS Region 1




      			+ Development pool




      				- Allocation for a VPC

  This structure serves as an example of how you might want to use IPAM, but you can use IPAM
  to suit the needs of your organization. For more information on best practices, see [Amazon VPC
  IP Address Manager Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/ "https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/").

If you are creating a single IPAM pool, complete the steps in [Create a top-level IPv4 pool](create-top-ipam.md "create-top-ipam.md") and then skip to [Allocate CIDRs from an IPAM pool](allocate-cidrs-ipam.md "allocate-cidrs-ipam.md").

###### Contents

- [Example IPAM pool plans](planning-examples-ipam.md "planning-examples-ipam.md")
- [Create IPv4 pools](intro-create-ipv4-pools.md "intro-create-ipv4-pools.md")
- [Create IPv6 address pools in your IPAM](intro-create-ipv6-pools.md "intro-create-ipv6-pools.md")

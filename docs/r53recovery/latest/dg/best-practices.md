# Best practices for Region switch in ARC

We recommend the following best practices for recovery and failover preparedness with Region switch in Amazon Application Recovery Controller (ARC).

**Topics**

- [Keep purpose-built, long-lived AWS credentials secure and always accessible](#RSBestPracticeCredentials "#RSBestPracticeCredentials")
- [Choose lower TTL values for DNS records involved in failover](#RSBestPracticeLowerTTL "#RSBestPracticeLowerTTL")
- [Reserve required capacity for critical applications](#RSBestPracticeCapacity "#RSBestPracticeCapacity")
- [Use the extremely reliable data plane API operations to list and get information
  about Region switch plans](#RSBestPracticeUseDataPlane "#RSBestPracticeUseDataPlane")
- [Test failover with ARC](#RSBestPracticeTestFailover "#RSBestPracticeTestFailover")

**Keep purpose-built, long-lived AWS credentials secure and always accessible**
In a disaster recovery (DR) scenario, keep system dependencies to a minimum by using a simple approach to
accessing AWS and performing recovery tasks. Create [IAM long-lived credentials](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md") specifically for DR tasks, and keep the credentials securely in an on-premises physical
safe or a virtual vault, to access when needed. With IAM, you can centrally manage security credentials, such as access keys,
and permissions for access to AWS resources. For non-DR tasks, we recommend that you continue to use federated access, using AWS
services such as [AWS Single Sign-On](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/").

**Choose lower TTL values for DNS records involved in failover**
For DNS records that you might need to change as part of your failover mechanism, especially records that
are health checked, using lower TTL values is appropriate. Setting a TTL of 60 or 120 seconds is a common choice for this scenario.

The DNS TTL (time to live) setting tells DNS resolvers how long to cache a record before requesting a new one.
When you choose a TTL, you make a trade-off between latency and reliability,
and responsiveness to change. With a shorter TTL on a record, DNS resolvers notice updates to the record more quickly because
the TTL specifies that they must query more frequently.

For more information, see _Choosing TTL values for DNS records_ in
[Best practices for Amazon Route 53 DNS](../../../Route53/latest/DeveloperGuide/best-practices-dns.md "../../../Route53/latest/DeveloperGuide/best-practices-dns.md").

**Reserve required capacity for critical applications**
Region switch includes execution block types that help scale compute resources as part of recovery. If you
use these execution blocks in a plan, Region switch does not guarantee that the desired compute capacity with be attained.
If you have a critical application and need to guarantee access to capacity, we recommend that you reserve the capacity.

There are strategies that you can follow to reserve compute capacity in a secondary Region while also
limiting cost. To learn more, see [Pilot light with reserved capacity: How to optimize DR cost using On-Demand Capacity Reservations](https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/ "https://aws.amazon.com/blogs/architecture/pilot-light-with-reserved-capacity-how-to-optimize-dr-cost-using-on-demand-capacity-reservations/").

**Use the extremely reliable data plane API operations to list and get information about Region switch plans**
Use data plane API operations to work with and execute your Region switch plan during
an event. For a list of Region switch data plane operations, see [Region switch API operations](actions.md "actions.md").

The Region switch console in each Region uses data plane operations for executing Region switch plans. You can also
call data plane API operations by using the AWS CLI or by running code that you write using one of the AWS
SDKs. ARC offers extreme reliability with the API in the data plane.

**Test application recovery with ARC**
Test application recovery regularly with ARC Region switch,
to activate a secondary application stack in another AWS Region, or to switch over an active-active configuration by
running a Region switch plan to deactivate one of the Regions.

It's important to make sure that the Region switch plans that you've created are aligned with
the correct resources in your stack, and that everything works as you expect it to. You should test
this after you set up Region switch for your environment, and continue to test periodically, so that you validate
that your recovery processes work correctly. Do this testing regularly, before you experience a failure
situation, to help avoid downtime for your users.

**ARC Region switch DNS failover versus Route 53 Accelerated recovery**

Accelerated recovery provides a target RTO of 60-minutes for APIs used to update your public hosted zone records that are enabled for this capability.
If you need to maintain control over your RTO and not wait for AWS to complete recovery of the APIs needed,
you should use ARC Routing control or ARC Region switch Route 53 health check execution block.

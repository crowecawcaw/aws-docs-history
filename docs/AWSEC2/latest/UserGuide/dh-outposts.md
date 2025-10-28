# Amazon EC2 Dedicated Hosts on AWS Outposts

AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs,
and tools to your premises. By providing local access to AWS managed infrastructure,
AWS Outposts enables you to build and run applications on premises using the same programming
interfaces as in AWS Regions, while using local compute and storage resources for
lower latency and local data processing needs.

An Outpost is a pool of AWS compute and storage capacity deployed at a customer
site. AWS operates, monitors, and manages this capacity as part of an AWS Region.

You can allocate Dedicated Hosts on Outposts that you own in your account. This makes it easier
for you to bring your existing software licenses and workloads that require a dedicated
physical server to AWS Outposts. You can also target specific hardware assets on an Outpost to
help minimize latency between your workloads.

Dedicated Hosts allow you to use your eligible software licenses on Amazon EC2, so that you get the
flexibility and cost effectiveness of using your own licenses. Other software licenses
that are bound to virtual machines, sockets, or physical cores, can also be used on
Dedicated Hosts, subject to their license terms. While Outposts have always been a single-tenant
environments that are eligible for BYOL workloads, Dedicated Hosts allows you to limit the needed
licenses to a single host as opposed to the entire Outpost deployment.

Additionally, using Dedicated Hosts on an Outpost gives you greater flexibility in instance type
deployment, and more granular control over instance placement. You can target a specific
host for instance launches and use host affinity to ensure that the instance always runs
on that host, or you can use auto-placement to launch an instance onto any available
host that has matching configurations and available capacity.

###### Contents

- [Prerequisites](dh-outposts.md#dh-outpost-prereqs "dh-outposts.md#dh-outpost-prereqs")
- [Supported features](dh-outposts.md#dh-outpost-features "dh-outposts.md#dh-outpost-features")
- [Considerations](dh-outposts.md#dh-outpost-considerations "dh-outposts.md#dh-outpost-considerations")
- [Allocate an Amazon EC2 Dedicated Host on AWS Outposts](dh-outpost-allocate.md "dh-outpost-allocate.md")

## Prerequisites

You must have an Outpost installed at your site. For more information, see [Create an Outpost and order Outpost capacity](../../../outposts/latest/userguide/order-outpost-capacity.md "../../../outposts/latest/userguide/order-outpost-capacity.md") in the _AWS Outposts
User Guide_.

## Supported features

- The following instance families are supported: `C5`,
  `M5`, `R5`, `C5d`, `M5d`,
  `R5d`, `G4dn`, and `i3en`.
- Dedicated Hosts on Outposts can be configured to support multiple instance sizes.
  Support for multiple instance sizes is available for the following instance
  families: `C5`, `M5`, `R5`,
  `C5d`, `M5d`, and `R5d`. For more
  information, see [Amazon EC2 Dedicated Host instance capacity configurations](dedicated-hosts-limits.md "dedicated-hosts-limits.md").
- Dedicated Hosts on Outposts support auto-placement and targeted instance launches.
  For more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").
- Dedicated Hosts on Outposts support host affinity. For more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").
- Dedicated Hosts on Outposts support sharing with AWS RAM. For more information, see
  [Cross-account Amazon EC2 Dedicated Host sharing](dh-sharing.md "dh-sharing.md").

## Considerations

- Dedicated Host Reservations are not supported on Outposts.
- Host resource groups and AWS License Manager are not supported on Outposts.
- Dedicated Hosts on Outposts do not support burstable T3 instances.
- Dedicated Hosts on Outposts do not support host recovery.
- Simplified automatic recovery is not supported for instances with Dedicated Host tenancy on Outposts.

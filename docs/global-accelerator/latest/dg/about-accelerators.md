# Standard accelerators in AWS Global Accelerator

A _standard accelerator_ in AWS Global Accelerator directs traffic over the
AWS global network to endpoints that you include in specified AWS Regions. Each accelerator includes
one or more listeners. A listener processes inbound connections from clients to Global Accelerator, based on the protocol (or
protocols) and port (or port range) that you configure.

For standard accelerators, Global Accelerator directs traffic to the optimal regional endpoint based
on health, client location, and policies that you configure, which increases the availability of your applications.
Endpoints for standard accelerators can be Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses that are located in
one AWS Region or multiple Regions.

###### Important

By default, Global Accelerator provides you with static IP addresses that are associated with your accelerator
The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and
it no longer accepts or routes traffic. However, when you _delete_ an accelerator, you lose the
Global Accelerator static IP addresses that are assigned to the accelerator, so that you can no longer route traffic by using them.
As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators.
You can use IAM policies with Global Accelerator, for example, tag-based permissions, to limit the users who have permissions to delete
an accelerator. For more information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

This section includes procedures for working with a standard accelerator on the Global Accelerator console. If you want to use
API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

###### Contents

- [Create accelerator](about-accelerators.md "about-accelerators.md")
- [Update accelerator](about-accelerators.md "about-accelerators.md")
- [Delete accelerator](about-accelerators.md "about-accelerators.md")
- [View your accelerators](about-accelerators.md "about-accelerators.md")
- [Adding an accelerator
  when you create a load balancer](about-accelerators.md "about-accelerators.md")
- [Compare using global
  static IP addresses to regional static IP addresses](about-accelerators.md "about-accelerators.md")

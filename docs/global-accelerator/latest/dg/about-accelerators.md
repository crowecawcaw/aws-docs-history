# Compare using global

static IP addresses to regional static IP addresses

If you want to use a static IP address in front of an AWS resource, such as an Amazon EC2 instance, you have several
options. For example, you can allocate an Elastic IP address, which is a static IPv4 or IPv6 address that you can associate
with an Amazon EC2 instance or network interface in a single AWS Region.

If you have a global audience, you can create an accelerator with Global Accelerator to get global static addresses that are
announced from AWS edge locations around the world. For IPv4, Global Accelerator provides two global static IPv4 addresses. For
dual-stack, Global Accelerator provides a total of four global static IP addresses: two IPv4
addresses and two IPv6 addresses. If you already have AWS resources set up for your applications,
in one or multiple Regions, including Amazon EC2 instances, Network Load Balancers, and Application Load Balancers, you can easily add those to Global Accelerator to front
them with global static IP addresses. For more information, see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

Opting to use global static IP addresses provisioned by Global Accelerator can also improve the availability and
performance of your applications. With Global Accelerator, static IP addresses accept incoming traffic onto the AWS global
network from the edge location that is closest to your users. Maximizing time that traffic is on the AWS network
can provide a faster and better customer experience. For more information, see [How AWS Global Accelerator works](introduction-how-it-works.md "introduction-how-it-works.md") .

You can add an accelerator from the AWS Management Console or by using API operations with the AWS CLI or SDKs.
For more information, see [Create accelerator](about-accelerators.md "about-accelerators.md").

Note the following when you add an accelerator:

- The global static IP addresses provisioned by Global Accelerator remain assigned to you for as long as your accelerator exists,
  even if you disable the accelerator and it no longer accepts or routes traffic. However, if you delete an accelerator, you
  lose the static IP addresses that are assigned to it. For more information, see [Delete accelerator](about-accelerators.md "about-accelerators.md").
- With Global Accelerator, you pay only for what you use. You are charged an hourly rate and data transfer costs for
  each accelerator in your account. For more information, see [AWS Global Accelerator Pricing](https://aws.amazon.com/global-accelerator/pricing "https://aws.amazon.com/global-accelerator/pricing").

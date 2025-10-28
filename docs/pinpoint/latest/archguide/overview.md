**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Resilient architecture overview

This chapter contains introductory information related to the development of resilient,
high availability architectures. It includes terms, concepts, and best practices.

###### Topics in this chapter:

- [Is a resilient, multi-Region architecture necessary
  for your use case?](#overview-usecase "#overview-usecase")
- [High availability concepts](#overview-terms "#overview-terms")
- [When to fail over to another AWS Region](#overview-failover "#overview-failover")

## Is a resilient, multi-Region architecture necessary

for your use case?

AWS was designed to help you achieve your system availability goals. Even if you
only deploy services in a single AWS Region, those services are distributed across
several Availability Zones in that Region. The result is high availability, geographical
redundancy, and fault tolerance.

For critical use cases, consider using a resilient, multi-Region architecture. The
primary benefit of using a multi-Region architecture is that it protects you against
disruptions that impact an entire AWS Region. However, deploying this type of
architecture requires you to make deeper investments in building your applications and
regularly testing your failover capabilities. Weigh these benefits and drawbacks
carefully against the criticality of your use case.

For more information about AWS Regions and Availability Zones, see [Regions and
Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") on the AWS Global Infrastructure website.

## High availability concepts

This guide uses several terms to describe common concepts in high availability
architecture:

**Recovery Time Objective (RTO)**

The maximum acceptable delay between service interruption and service
restoration. RTO determines what is considered an acceptable amount of time
for the service to be unavailable.

**Recovery Point Objective (RPO)**

The maximum acceptable time since the last data recovery point. RPO
determines what is considered an acceptable loss of data between the last
recovery point and the service outage.

**Warm standby**

A high availability architecture in which a fully functional environment
is always running in a secondary AWS Region. Business-critical systems are
fully duplicated and are always on. If the primary Region becomes
unavailable, you can use services such as Amazon Route 53 or AWS Global Accelerator to route
all user traffic to the standby Region. The RPO for this architecture is
typically measured in seconds, and the RTO is typically measured in
minutes.

**Active-active**

A high availability architecture in which a workload is deployed in and
actively serves traffic from multiple AWS Regions. An active-active design
requires you to synchronize users and data between the Regions that you use.
If one Region becomes unavailable, you can use services such as Amazon Route 53 or
AWS Global Accelerator to route all user traffic to the other Region. The RPO and RTO for
this type of architecture are measured in seconds.

There are other high availability architecture strategies that aren't described here,
such as _pilot light_ and _backup and restore_.
However, these strategies aren't preferable for architectures that use Amazon Pinpoint. For that
reason, this guide focuses on [warm
standby](architectures.md#architectures-warmstandby "architectures.md#architectures-warmstandby") and [active-active](architectures.md#architectures-activeactive "architectures.md#architectures-activeactive")
architectures.

## When to fail over to another AWS Region

Several factors could cause your architecture to fail over to a different
AWS Region. For example, a Regional outage could prevent you from accessing the Amazon Pinpoint
console, or from accessing its API operations. You could also configure your
architecture to fail over when your messages are being sent but aren't receiving event
notifications (or the number of event notifications is unexpectedly low).

In certain situations, failing over won't provide any benefit. For example, if you
send SMS messages, and a specific mobile carrier is having an outage, then delivery
issues will persist, regardless of which AWS Region you use. The same is true for
email: if an email provider has a temporary issue that prevents the delivery of email to
its domain, that issue will persist across Regions.

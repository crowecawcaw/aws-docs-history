

# Resiliency
<a name="nx-sms-scale-resiliency"></a>

The global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications that automatically fail over between zones without interruption. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the global infrastructure, AWS End User Messaging offers several features that help support the resilience of your SMS messaging.

## Resilience in SMS routing
<a name="nx-sms-scale-resiliency-routing"></a>

AWS End User Messaging is committed to improving the resilience and deliverability of SMS messages. The service maintains multiple routes and adjusts SMS routing based on route trustworthiness, message deliverability, and message cost. These adjustments are applied automatically to the SMS messages you send, and do not require any configuration on your part.

## Improve resilience with phone pools
<a name="nx-sms-scale-resiliency-pools"></a>

You can improve delivery resilience by configuring phone pools that contain multiple origination identities. The service monitors delivery receipts (DLRs) for each identity in a pool and automatically routes messages away from identities that are experiencing delivery failures. When the affected identity recovers, normal routing resumes without manual intervention. For the broadest coverage, include different number types in the same pool, such as a short code and a toll-free number, because each number type uses an independent delivery path. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md).

## Design with redundancy across AWS Regions
<a name="nx-sms-scale-resiliency-multi-region"></a>

For mission-critical messaging programs, we recommend that you configure AWS End User Messaging in more than one AWS Region. The phone numbers that you use for SMS or MMS messages — including short codes, long codes, toll-free numbers, and 10DLC numbers — can't be replicated across AWS Regions. To use AWS End User Messaging in multiple AWS Regions, you must request separate phone numbers in each AWS Region where you want to send messages. In some countries, you can also use multiple types of phone numbers for added redundancy, because each number type takes a different route to the recipient. For a complete list of AWS Regions where AWS End User Messaging is available, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html).


# Resiliency
<a name="nx-mms-scale-resiliency"></a>

The global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications that automatically fail over between zones without interruption. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the global infrastructure, AWS End User Messaging offers several features that help support the resilience of your MMS messaging.

## Improve resilience with phone pools
<a name="nx-mms-scale-resiliency-pools"></a>

You can improve delivery resilience by configuring phone pools that contain multiple origination identities. The service monitors delivery receipts (DLRs) for each identity in a pool and automatically routes messages away from identities that are experiencing delivery failures. When the affected identity recovers, normal routing resumes without manual intervention. Because MMS in AWS End User Messaging is sent from the same origination identities as SMS, you can include MMS-capable number types in a pool to spread sending across more than one identity. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md).

## Design with redundancy across AWS Regions
<a name="nx-mms-scale-resiliency-multi-region"></a>

For mission-critical messaging programs, we recommend that you configure AWS End User Messaging in more than one AWS Region. The phone numbers that you use for SMS or MMS messages — including short codes, long codes, and toll-free numbers — can't be replicated across AWS Regions. To use AWS End User Messaging in multiple AWS Regions, you must request separate phone numbers in each AWS Region where you want to send messages. In some countries, you can also use multiple types of phone numbers for added redundancy, because each number type takes a different route to the recipient. For a complete list of AWS Regions where AWS End User Messaging is available, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html).
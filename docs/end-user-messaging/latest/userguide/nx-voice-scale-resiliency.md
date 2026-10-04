

# Resiliency
<a name="nx-voice-scale-resiliency"></a>

The global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications that automatically fail over between zones without interruption. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the global infrastructure, AWS End User Messaging offers several features that help support the resilience of your voice messaging.

## Improve resilience with phone pools
<a name="nx-voice-scale-resiliency-pools"></a>

You can improve delivery resilience by configuring phone pools that contain multiple origination identities. When you send a voice message with a pool as the origination identity, the service selects an available identity from the pool, so a single degraded identity does not stop your traffic. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md).

## Design with redundancy across AWS Regions
<a name="nx-voice-scale-resiliency-multi-region"></a>

For mission-critical voice programs, we recommend that you configure AWS End User Messaging in more than one AWS Region. The phone numbers that you use for voice messages can't be replicated across AWS Regions. To use AWS End User Messaging in multiple AWS Regions, you must request separate phone numbers in each AWS Region where you want to send voice messages. For a complete list of AWS Regions where AWS End User Messaging is available, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html).
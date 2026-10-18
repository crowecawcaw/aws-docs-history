

# Resiliency
<a name="nx-rcs-scale-fallback"></a>

The global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications that automatically fail over between zones without interruption. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the global infrastructure, AWS End User Messaging offers several features that help support the resilience of your RCS messaging. Because RCS is not available on every device or carrier, the most important of these is SMS fallback, which keeps your messages reaching every recipient even when RCS delivery is not possible.

## SMS fallback
<a name="nx-rcs-scale-fallback-how-it-works"></a>

SMS fallback lets a single send reach recipients whether or not their device and carrier support RCS. AWS End User Messaging attempts RCS delivery first, and when the recipient cannot receive RCS, because the device or carrier does not support it or the message exceeds what RCS can deliver, the service delivers the message as SMS instead. You send once, and the service chooses the delivery path. A message that falls back is reported with the `RCS_FALLEN_BACK_TO_SMS` event and counted in the `RCS.MessagesFallenBackToSMS` metric, so you can measure how often fallback occurs. For more information about tracking fallback, see [Monitoring](nx-rcs-scale-monitoring.md).

AWS End User Messaging gives you two ways to set up fallback. You can let a phone pool handle it automatically, or you can define the exact fallback message on each send with a fallback configuration.

### Automatic fallback with a phone pool
<a name="nx-rcs-scale-fallback-pool-based"></a>

When you send through a phone pool that contains both your AWS RCS Agent and one or more SMS phone numbers, the service attempts RCS delivery first and automatically resends the message as SMS using an SMS number in the same pool when RCS delivery is not possible. You do not define the fallback message. The service reuses your original text and sends it from a number in the pool. Because all identities in the pool are registered for the same use case, the fallback is always sent from an appropriate number. This is the recommended way to send, and it applies to both the `SendTextMessage` and `SendRcsMessage` operations.

To enable pool-based fallback, create a phone pool whose first origination identity is your AWS RCS Agent, then add one or more SMS phone numbers to the same pool. Send with the pool as the origination identity. For complete steps to create and manage phone pools, see [Phone pools](nx-features-phone-pools.md).

**To set up pool-based SMS fallback**

1. Create a phone pool and choose your AWS RCS Agent as the first origination identity.

1. Add one or more SMS phone numbers to the pool to use for fallback. Every identity you add must have the same settings as the first identity in the pool.

1. Send your RCS messages with the pool as the origination identity. AWS End User Messaging attempts RCS first and falls back to SMS on a number in the pool when RCS delivery is not possible.

For the console and AWS CLI commands to create the pool and associate SMS numbers (`create-pool` and `associate-origination-identity`), see the pool creation step in [How to get set up](nx-rcs-get-set-up.md).

### Define the fallback message with a fallback configuration
<a name="nx-rcs-scale-fallback-rule"></a>

When you send rich RCS content with the `SendRcsMessage` operation, you can set a fallback configuration on the request to control exactly what the recipient receives if RCS delivery does not succeed. This is useful when the fallback message needs to differ from the RCS content, for example sending a plain SMS summary in place of a rich card, or sending an MMS with an image. The service sends the fallback message when the RCS message fails or when its `TimeToLive` expires without a delivery confirmation.

A fallback configuration contains the following rule:


| Field | Required | Description | 
| --- | --- | --- | 
| Channel | Required | The fallback channel to use, either `SMS` or `MMS`. The two channels are mutually exclusive. | 
| Message body | Required for SMS | The text of the fallback message. A message body is required for SMS fallback. For MMS fallback, provide a message body, one or more media URLs, or both. | 
| Media URLs | MMS only | One or more Amazon S3 URIs that point to the media files to send. Media URLs apply only when the channel is MMS. | 
| Origination identity | Optional | The identity that sends the fallback message, such as a phone number or sender ID. A pool is not accepted here. If you do not set an origination identity and you sent the original message through a pool, the service selects a suitable number from that pool. | 

Because a fallback configuration is set on the send request, it works whether you send with a pool or directly with an AWS RCS Agent ARN. If you send with an AWS RCS Agent ARN and do not set a fallback configuration, the message is delivered over RCS only, with no fallback.

For the full list of `SendRcsMessage` request parameters, including the fallback configuration fields, see [SendRcsMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendRcsMessage.html) in the SMS and Voice v2 API Reference.

## Improve resilience with phone pools
<a name="nx-rcs-scale-fallback-pools"></a>

Beyond enabling SMS fallback, phone pools improve delivery resilience by letting you send from a set of origination identities rather than a single one. When you send with a pool, the service selects an available identity from the pool, so a single degraded identity does not stop your traffic. Keeping agent and number selection in the pool, rather than hard-coded in your application, lets you add, remove, or replace identities without changing your send code. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md).

## Design with redundancy across AWS Regions
<a name="nx-rcs-scale-fallback-multi-region"></a>

For mission-critical RCS programs, we recommend that you configure AWS End User Messaging in more than one AWS Region. The AWS RCS Agents and phone numbers that you use for RCS messages can't be replicated across AWS Regions. To use AWS End User Messaging in multiple AWS Regions, you must register a separate RCS Agent and request separate phone numbers in each AWS Region where you want to send messages. For a complete list of AWS Regions where AWS End User Messaging is available, see the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html).


# Limits and quotas
<a name="nx-mms-scale-limits"></a>

MMS messaging is subject to several limitations and restrictions. There are limits on the size and type of media that each MMS message can carry, limits on the length of the message text body, and throughput limits on how quickly you can send. When you set up MMS messaging in AWS End User Messaging, you must consider these limitations and restrictions, and you should also follow the techniques described in [Best practices](nx-mms-scale-best-practices.md). For the per-account service quotas that apply across channels, and how to request an increase, see [Quotas](nx-features-quotas.md).

**Topics**
+ [MMS file types, size, and character limits](#nx-mms-scale-limits-media)
+ [Message Parts per Second (MPS) limits](#nx-mms-scale-limits-mps)
+ [Route type](#nx-mms-scale-limits-routes)

## MMS file types, size, and character limits
<a name="nx-mms-scale-limits-media"></a>

A single MMS media file can be up to 2 MB for all image types (gif, jpeg, png) and 600 KB for all audio and video media file types. The text message body of an MMS can contain 1,600 characters from any character set. Unlike SMS, MMS messages are not broken into multiple parts when they are sent. If you are sending a large text message, you might get better throughput by sending an MMS message, because it is not broken into multiple parts.

## Message Parts per Second (MPS) limits
<a name="nx-mms-scale-limits-mps"></a>

Throughput limits in AWS End User Messaging, also referred to as throttling, are measured in Message Parts per Second (MPS) — that is, the maximum number of message parts that you can send in a second. MMS messages are delivered as a single message part and are not broken into multiple message parts, so each MMS message counts as one message part against your MPS limit. If you are sending SMS messages that have more than three message parts, consider sending an MMS message instead, because you are billed for each SMS message part and sending a single MMS part also increases your message throughput. The MPS that applies to your messaging varies by origination identity type and by country. For the detailed per-country and per-number-type throughput values, and the account-level throughput quotas, see [Quotas](nx-features-quotas.md).

## Route type
<a name="nx-mms-scale-limits-routes"></a>

Currently, all messages are sent through the **Standard** route type. AWS End User Messaging maintains multiple routes and adjusts routing automatically based on route trustworthiness, message deliverability, and message cost, as described in [Resiliency](nx-mms-scale-resiliency.md).
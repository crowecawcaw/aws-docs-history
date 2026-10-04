

# Limits and quotas
<a name="nx-sms-scale-limits"></a>

The SMS protocol is subject to several limitations and restrictions. There are technical limitations on the length of each SMS message, and there are throughput limits on how quickly you can send. When you set up SMS and MMS messaging in AWS End User Messaging, you must consider these limitations and restrictions, and you should also follow the techniques described in [Best practices](nx-sms-scale-best-practices.md). For the per-account service quotas that apply across channels, and how to request an increase, see [Quotas](nx-features-quotas.md).

**Topics**
+ [SMS character limits](#nx-sms-scale-limits-character)
+ [MMS file types, size, and character limits](#nx-sms-scale-limits-mms)
+ [Message Parts per Second (MPS) limits](#nx-sms-scale-limits-mps)
+ [Route type](#nx-sms-scale-limits-routes)

## SMS character limits
<a name="nx-sms-scale-limits-character"></a>

A single SMS message can contain up to 140 bytes of information. The number of characters you can include in a single SMS message depends on the type of characters the message contains. If your message uses only characters in the GSM 03.38 character set, also known as the GSM 7-bit alphabet, it can contain up to 160 characters. If your message contains any characters that are outside the GSM 03.38 character set, it can have up to 70 characters. When you send an SMS message, AWS End User Messaging automatically determines the most efficient encoding to use.

When a message contains more than the maximum number of characters, the message is split into multiple parts. When messages are split, the number of characters in each part is reduced to 153 for messages that only contain GSM 03.38 characters, or 67 for messages that contain other characters, because each part carries additional information used to reassemble the message on the recipient's device. The maximum supported size of any message is 1,530 GSM characters or 630 non-GSM characters. If the message size is greater than the supported size, the message fails and AWS End User Messaging returns an **Invalid Message Exception**.

**Important**  
When you send a message that contains more than one message part, you're charged for the number of message parts contained in the message.

## MMS file types, size, and character limits
<a name="nx-sms-scale-limits-mms"></a>

A single MMS media file can be up to 2 MB for all image types (gif, jpeg, png) and 600 KB for all audio and video media file types. The text message body of an MMS can contain 1,600 characters from any character set. Unlike SMS, MMS messages are not broken into multiple parts when they are sent. If you are sending a large text message, you might get better throughput by sending an MMS message, because it is not broken into multiple parts.

## Message Parts per Second (MPS) limits
<a name="nx-sms-scale-limits-mps"></a>

SMS messages are delivered in 140-byte sections known as message parts. For this reason, SMS throughput limits, also referred to as throttling, are measured in Message Parts per Second (MPS) — that is, the maximum number of message parts that you can send in a second. Your MPS limit depends on the destination country of your messages and the type of origination identity that you use to send the message. For example, if you use a United States short code to send messages to recipients in the US, you can send 100 MPS, but if you use a US toll-free number to send to US recipients, you are throttled to 3 MPS.

MMS messages are delivered as a single message part and are not broken into multiple message parts. If you are sending SMS messages that have more than three message parts, consider sending an MMS message instead, because you are billed for each SMS message part and sending a single MMS part also increases your message throughput. The MPS that applies to your messaging varies by origination identity type and by country. For the detailed per-country and per-number-type throughput values, and the account-level throughput quotas, see [Quotas](nx-features-quotas.md).

## Route type
<a name="nx-sms-scale-limits-routes"></a>

Currently, all messages are sent through the **Standard** route type. AWS End User Messaging maintains multiple routes and adjusts routing automatically based on route trustworthiness, message deliverability, and message cost, as described in [Resiliency](nx-sms-scale-resiliency.md).
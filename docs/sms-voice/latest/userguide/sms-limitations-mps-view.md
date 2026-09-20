

# View your current messaging limits
<a name="sms-limitations-mps-view"></a>

The preceding tables show the general message parts per second (MPS) limits by origination number type and country. You can also view the messaging limits that apply to a specific origination identity, such as a phone number, sender ID, or RCS agent. The messaging limits include the following:
+ **Send rate limits** – The maximum send rate for each supported capability, in message parts per second. A capability can be `SMS`, `MMS`, `VOICE`, or `RCS`.
+ **Daily message caps** – An advisory maximum number of messages that can be sent per day, listed by provider (for example, `T-MOBILE`). Daily message caps apply to 10DLC phone numbers and are not shown when no daily cap applies.

To request an increase to these limits, open a case in the Support Center Console. For more information, see [Requesting a quota increase with Support](quotas.md#quotas-increase).

**To view the messaging limits for a phone number (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**.

1. Choose the phone number that you want to view.

1. Choose the **Messaging limits** tab to view the current send rate limits for the phone number.

**To view the messaging limits for a sender ID (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Sender IDs**.

1. Choose the sender ID that you want to view.

1. Choose the **Messaging limits** tab to view the current send rate limits for the sender ID.

**To view the messaging limits for an RCS agent (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **RCS agents**.

1. Choose the RCS agent that you want to view.

1. Choose the **Messaging limits** tab to view the current send rate limits for the RCS agent.

To view the messaging limits programmatically, use the `DescribePhoneNumbers`, `DescribeSenderIds`, or `DescribeRcsAgents` operation in the AWS End User Messaging SMS API. The response includes a `MessagingLimits` field that contains the send rate limits and, for supported phone numbers, any advisory daily message caps.
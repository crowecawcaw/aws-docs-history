

# Inbound messaging
<a name="nx-sms-send-inbound"></a>

With two-way SMS, you receive incoming messages from your customers. When a customer sends a message to your phone number, AWS End User Messaging delivers the message body to an Amazon SNS topic or an Connect Customer instance that you designate, where your application processes it – for example with Lambda or Amazon Lex to build interactive experiences.

When you use two-way SMS, consider the following:
+ Two-way SMS is only available in certain countries and regions. For more information, see [Launch in a country](nx-sms-country-support.md).
+ Sender IDs do not support two-way SMS messaging.
+ Two-way MMS is not supported, but your phone number can still receive incoming SMS messages in response to an outbound MMS message.
+ Connect Customer for two-way SMS is available in the AWS Regions listed in [Chat messaging: SMS subtype](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#chatmessaging_region) in the *Connect Customer administrator guide*.
+ Inbound SMS messages are not guaranteed to arrive in the order they were sent. Amazon SNS Standard topics deliver with best-effort ordering; if your application requires ordered processing, use the timestamp from the Amazon SNS notification metadata to order messages at the application layer.

## Enable two-way messaging
<a name="nx-sms-send-two-way-enable"></a>

Enable two-way SMS on a phone number, or on a phone pool to apply it to every number in the pool. Use the AWS End User Messaging console or the AWS CLI.

------
#### [ Console ]

**To enable two-way SMS**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers** (or **Phone pools** to enable it for a pool), and then choose the phone number or pool.

1. On the **Two-way SMS** tab, choose **Edit settings**, and then choose **Enable two-way message**.

1. For **Destination type**, choose **Amazon SNS** or **Connect Customer**. For Amazon SNS, choose a new or existing topic, and for **Two-way channel role** choose **Choose existing IAM role** or **Use Amazon SNS topic policies**. For Connect Customer, choose an existing IAM role.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

Use [update-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.html) for a phone number, or [update-pool](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/update-pool.html) for a pool. The destination and role options are the same for both.

```
$ aws pinpoint-sms-voice-v2 update-phone-number \
> --phone-number-id {{PhoneNumber}} \
> --two-way-enabled {{True}} \
> --two-way-channel-arn {{TwoWayARN}} \
> --two-way-channel-role {{TwoChannelWayRole}}
```
+ Replace {{PhoneNumber}} with the phone number ID or ARN (for a pool, run `update-pool` with `--pool-id` and the pool ID instead).
+ Replace {{TwoWayARN}} with the ARN that receives incoming messages. For Connect Customer, set it to `connect.{{region}}.amazonaws.com`.
+ Replace {{TwoChannelWayRole}} with the IAM role ARN. This is only required when you use an IAM role rather than an Amazon SNS topic policy.

------

**Note**  
AWS End User Messaging needs permission to publish to your destination. Grant it with an Amazon SNS topic policy, or with an IAM role that trusts the `sms-voice.amazonaws.com` service principal and allows `sns:Publish` (or the equivalent for Connect Customer). For the policy details and event-record routing, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

## Example inbound message payload
<a name="nx-sms-send-two-way-payload"></a>

When your number receives an SMS message, AWS End User Messaging sends a JSON payload to the Amazon SNS topic you designated, as in the following example:

```
{
  "originationNumber":"+14255550182",
  "destinationNumber":"+12125550101",
  "messageKeyword":"JOIN",
  "messageBody":"EXAMPLE",
  "inboundMessageId":"cae173d2-66b9-564c-8309-21f858e9fb84",
  "previousPublishedMessageId":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}
```



| Property | Description | 
| --- | --- | 
| originationNumber | The customer's phone number that sent the incoming message. | 
| destinationNumber | Your dedicated phone number that the customer sent to. | 
| messageKeyword | The registered keyword associated with your dedicated phone number. | 
| messageBody | The message the customer sent. | 
| inboundMessageId | The unique identifier for the incoming message. | 
| previousPublishedMessageId | The unique identifier of the message the customer is responding to. | 
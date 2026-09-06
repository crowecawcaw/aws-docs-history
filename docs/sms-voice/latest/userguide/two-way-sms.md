

# Two-way SMS messaging in AWS End User Messaging SMS
<a name="two-way-sms"></a>

AWS End User Messaging SMS includes support for two-way SMS. When you set up two-way SMS, you can receive incoming messages from your customers. You can also use two-way messaging together with other AWS services, such as Lambda and Amazon Lex, to create interactive text messaging experiences.

When one of your customers sends a message to your phone number, the message body is sent to an Amazon SNS topic or Connect Customer for processing.

When using two-way SMS, consider the following:
+ Two-way SMS is only available in certain countries and regions. For more information, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md).
+ Sender IDs do not support two-way SMS messaging.
+ Two-way MMS is not supported, but your phone number can still receive incoming SMS messages in response to an outbound MMS message.
+ Connect Customer for two-way SMS is available in the AWS Regions listed in [Chat messaging: SMS subtype](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#chatmessaging_region) in the *Connect Customer administrator guide*.
+ Inbound SMS messages are not guaranteed to arrive in the order they were sent. SMS protocols do not provide message ordering guarantees across carrier networks, and Amazon SNS Standard topics deliver messages with best-effort ordering. If your application requires ordered message processing, use the timestamp from the Amazon SNS notification metadata to approximate message ordering at the application layer.

**Topics**
+ [Set up two-way SMS messaging for a phone number](two-way-sms-phone-number.md)
+ [Set up two-way SMS messaging for a phone pool](two-way-sms-pool.md)
+ [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md)
+ [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md)
+ [IAM policies for Connect Customer](two-way-connect-iam-policy.md)
+ [Example two-way SMS message payload](two-way-sms-payload.md)
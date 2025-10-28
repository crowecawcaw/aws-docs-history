# Two-way SMS messaging in AWS End User Messaging SMS

AWS End User Messaging SMS includes support for two-way SMS. When you set up two-way SMS, you can receive
incoming messages from your customers. You can also use two-way messaging together
with other AWS services, such as Lambda and Amazon Lex, to create interactive text messaging
experiences.

When one of your customers sends a message to your phone number, the message body is sent
to an Amazon SNS topic or Amazon Connect for processing.

Two-way SMS is only available in certain countries and regions. For more information about
two-way SMS support by country or region, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md").

Sender IDs do not support two-way SMS messaging.

###### Note

Two-way SMS is only available in certain countries and regions. For more information
about two-way SMS support by country or region, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md").

Two-way MMS is not supported but your phone number can still receive incoming SMS messages in response to an outbound MMS message.

Amazon Connect for two-way SMS is available in the AWS Regions listed in [Chat messaging: SMS subtype](../../../connect/latest/adminguide/regions.md#chatmessaging_region "../../../connect/latest/adminguide/regions.md#chatmessaging_region") in the _Amazon Connect
administrator guide_.

###### Topics

- [Set up two-way SMS messaging for a phone number](two-way-sms-phone-number.md "two-way-sms-phone-number.md")
- [Set up two-way SMS messaging for a phone pool](two-way-sms-pool.md "two-way-sms-pool.md")
- [IAM policies for Amazon SNS topics](two-way-sms-iam-policy.md "two-way-sms-iam-policy.md")
- [Topic policies for Amazon SNS topics](two-way-sms-iam-policy-auto.md "two-way-sms-iam-policy-auto.md")
- [IAM policies for
  Amazon Connect](two-way-connect-iam-policy.md "two-way-connect-iam-policy.md")
- [Example two-way SMS message payload](two-way-sms-payload.md "two-way-sms-payload.md")

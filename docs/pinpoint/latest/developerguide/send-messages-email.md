**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Send transactional emails using Amazon Pinpoint

This section provides complete code samples that you can use to send transactional email
messages through Amazon Pinpoint:

- [By using the SendMessages operation in the Amazon Pinpoint
  API](send-messages-sdk.md "send-messages-sdk.md"): You can use the `SendMessages` operation in the Amazon Pinpoint API
  to send messages in all of the channels that Amazon Pinpoint supports, including the push
  notification, SMS, voice, and email channels.

The advantage of using this operation is that the request syntax for sending
messages is very similar across all channels. This makes it easier to repurpose your
existing code. The `SendMessages` operation also lets you to substitute
content in your email messages, and lets you send email to Amazon Pinpoint endpoint IDs rather
than to specific email addresses.
This section includes example code in several programming languages that you can use to
start sending transactional emails.

For more code examples on endpoints, segments, and channels see [Code examples](service_code_examples.md "service_code_examples.md").

## Choose a method to send email

The best method to use for sending transactional email depends on your use case. For
example, if you need to send email by using a third-party application, or if there isn't
an AWS SDK available for your programming language, you might have to use the SMTP
interface. If you want to send messages in other channels that Amazon Pinpoint supports, and you
want to use consistent code for making those requests, you should use the
`SendMessages` operation in the Amazon Pinpoint API.

## Choose between Amazon Pinpoint and Amazon SES

If you send a large number of transactional emails, such as purchase confirmations or
password reset messages, consider using Amazon SES. Amazon SES has an API and an SMTP
interface, both of which are well suited to sending email from your applications or
services. It also offers additional email features, including email receiving
capabilities, configuration sets, and sending authorization capabilities.

Amazon SES also includes an SMTP interface that you can integrate with your existing
third-party applications, including customer relationship management (CRM) services such
as Salesforce. For more information about sending email using Amazon SES, [Amazon
Simple Email Service Developer Guide](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md") for more information.

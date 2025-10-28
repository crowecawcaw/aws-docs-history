# Using the Amazon SNS SMS sandbox

Newly created Amazon SNS SMS accounts are automatically placed into the SMS sandbox to ensure
the security of both AWS customers and recipients by mitigating the risk of
fraud and abuse. This environment serves as a secure space for testing and development
purposes. While operating within the SMS sandbox, you have access to all Amazon SNS features but
are subject to certain limitations:

- You can only send SMS messages to verified destination phone numbers.
- You can have up to 10 verified destination phone numbers.
- You can delete destination phone numbers only after a minimum of 24 hours have
  passed since verification, or the last verification attempt.
  Once your account transitions out of the sandbox, these restrictions are removed, and you
  can send SMS messages to any recipient.

## First steps

New Amazon SNS SMS accounts are placed into an SMS sandbox. Use the following steps to
create and manage phone numbers in your sandbox, create origination numbers and
sender IDs, and register your company.

1. Add a **destination phone number** to the SMS sandbox. For
   details on adding, managing and moving phone numbers out of the Amazon SNS SMS
   sandbox, see [Adding and verifying phone numbers
   in the Amazon SNS SMS sandbox](sns-sms-sandbox-verifying-phone-numbers.md "sns-sms-sandbox-verifying-phone-numbers.md").
2. Create an **origination identity** that your
   recipients see on their devices when you send them an SMS message. To learn more
   about origination identities, including the different types you can use, see the
   [Origination identities for Amazon SNS SMS
   messages](channels-sms-originating-identities.md "channels-sms-originating-identities.md") documentation.
3. **Register** your company. Some countries require
   you to register your company's identity to be able to purchase phone numbers or
   sender IDs and review the messages you send to recipients in their country. For
   information on which countries require registration, see [Supported
   countries and regions for SMS messaging with AWS End User Messaging SMS](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the
   _AWS End User Messaging SMS User Guide_.
4. **Send** your messages to a topic or mobile
   phone. For more information, see [Sending SMS messages using Amazon SNS](sms_sending-overview.md "sms_sending-overview.md").

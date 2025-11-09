End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Using the Lambda function provided by

AWS IoT Events

With alarm notifications, you can use the Lambda function provided by AWS IoT Events for
managing alarm notifications.

The following requirements apply when you use the Lambda function provided by AWS IoT Events
to manage your alarm notifications:

- You must verify the email address that sends the email notifications in
  Amazon Simple Email Service (Amazon SES). For more information, see [Verifying an email address identity](../../../ses/latest/dg/creating-identities.md#just-verify-email-proc "../../../ses/latest/dg/creating-identities.md#just-verify-email-proc"), in the
  _Amazon Simple Email Service Developer Guide_.

If you receive a verification link, click the link to verify your email
address. You might also check your spam folder for a verification
email.

- If your alarm sends SMS notifications, you must use E.164 international
  phone number formatting for phone numbers. This format contains
  `+<country-calling-code><area-code><phone-number>`.

Example phone numbers:

| Country        | Local phone number | E.164 formatted number |
| -------------- | ------------------ | ---------------------- |
| United States  | 206-555-0100       | +12065550100           |
| United Kingdom | 020-1234-1234      | +442012341234          |
| Lithuania      | 8+601+12345        | +37060112345           |

To find a country calling code, go to [countrycode.org](https://countrycode.org/ "https://countrycode.org/").

The Lambda function provided by AWS IoT Events checks if you use E.164 formatted
phone numbers. However, it doesn't verify the phone numbers. If you ensure
that you entered accurate phone numbers but didn't receive SMS
notifications, you might contact the phone carriers. The carriers may block
the messages.

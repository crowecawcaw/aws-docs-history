# Release a phone number in AWS End User Messaging SMS

If you don't need a phone number that you had previously requested through AWS End User Messaging SMS anymore, you can release it from your AWS End User Messaging SMS account. When you
release a number, AWS stops charging you for it in your bill for the next calendar
month.

###### Important

Releasing a phone number from your AWS End User Messaging SMS account is permanent and can't be undone. If you
release a phone number, you won't be able to obtain the same number again in the
future.

Deletion protection has to be disabled before you can release a phone number. For more
information on deletion protection, see [Using phone number deletion protection in AWS End User Messaging SMS](phone-numbers-deletion-protection.md "phone-numbers-deletion-protection.md").

Release a phone number (Console)
To release a phone number from your AWS End User Messaging SMS account using the AWS End User Messaging SMS console, follow these steps:

###### Release a phone number (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone numbers**.
3. Choose the phone number that you want to release and then choose
   **Release phone number**.
4. On the **Release phone number** window enter
   `release` and choose **Release phone
   number**.

Release a phone number (AWS CLI)
You can use the [release-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/release-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/release-phone-number.md") CLI to _release_ phone
numbers from your account.

```
`$` aws pinpoint-sms-voice-v2 release-phone-number \
`>` --phone-number-id `phoneNumberId`

```

In the preceding command, replace `phoneNumberId`
with the unique ID or Amazon Resource Name (ARN) of the phone number.

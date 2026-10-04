

# Release a phone number in AWS End User Messaging
<a name="nx-features-phone-numbers-release"></a>

If you don't need a phone number that you had previously requested through AWS End User Messaging anymore, you can release it from your AWS End User Messaging account. When you release a number, AWS stops charging you for it in your bill for the next calendar month.

**Important**  
Releasing a phone number from your AWS End User Messaging account is permanent and can't be undone. If you release a phone number, you won't be able to obtain the same number again in the future.  
Deletion protection has to be disabled before you can release a phone number. For more information on deletion protection, see [Using phone number deletion protection in AWS End User Messaging](nx-features-phone-numbers-deletion-protection.md).

------
#### [ Release a phone number (Console) ]

To release a phone number from your AWS End User Messaging account using the AWS End User Messaging console, follow these steps:

**Release a phone number (Console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**.

1. Choose the phone number that you want to release and then choose **Release phone number**.

1. On the **Release phone number** window enter **release** and choose **Release phone number**.

------
#### [ Release a phone number (AWS CLI) ]

You can use the [release-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/release-phone-number.html) CLI to *release* phone numbers from your account.

```
$ aws pinpoint-sms-voice-v2 release-phone-number \
> --phone-number-id {{phoneNumberId}}
```

In the preceding command, replace {{phoneNumberId}} with the unique ID or Amazon Resource Name (ARN) of the phone number.

------
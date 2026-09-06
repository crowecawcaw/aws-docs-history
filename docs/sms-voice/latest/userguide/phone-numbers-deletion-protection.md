

# Using phone number deletion protection in AWS End User Messaging SMS
<a name="phone-numbers-deletion-protection"></a>

When you turn on deletion protection you will not be able to release the phone number until deletion protection is disabled. By default deletion protection is turned off.

------
#### [ Enable deletion protection (Console) ]

To change deletion protection using the AWS End User Messaging SMS console, follow these steps:

**Enable deletion protection (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**.

1. On the **Phone numbers** page, choose the phone number that will have deletion protection enabled.

1. On the **Deletion protection** tab, choose the **Edit settings** button.

1. Choose **Enable deletion protection** and then **Save changes**.

------
#### [ Disable deletion protection (Console) ]

To change deletion protection using the AWS End User Messaging SMS console, follow these steps:

**Enable deletion protection (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**.

1. On the **Phone numbers** page, choose the phone number that will have deletion protection enabled.

1. On the **Deletion protection** tab, choose the **Edit settings** button.

1. Clear **Enable deletion protection** and then **Save changes**.

------
#### [ Enable deletion protection (AWS CLI) ]

You can use the [update-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.html) command to enable deletion protection the phone number.

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 update-phone-number --phonenumber-id {{PhoneNumberid}} --deletion-protection-enabled
```

In the preceding command, make the following changes:
+ Replace {{PhoneNumberid}} with the PhoneNumberID or Amazon Resource Name (ARN) of the phone number.

------
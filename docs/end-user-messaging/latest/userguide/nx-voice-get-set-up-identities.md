

# Step 1: Get a voice-capable phone number
<a name="nx-voice-get-set-up-identities"></a>

To send voice messages, you need a voice-capable phone number. Request a phone number that supports the voice channel in your destination country. The number types and country availability for voice are described under [Country support](nx-voice-scale-country-support.md). For the full phone number request and management operations, see [Phone numbers](nx-features-phone-numbers.md).

After you request the number, you add it to a phone pool in Step 2.

**Note**  
New accounts start in the voice sandbox, where you can only place calls to verified destination phone numbers. This lets you test before you request production access. For more information about the sandbox and how to request production access, see [Move out of the sandbox](nx-voice-scale-sandbox.md).

To request a number from the console or the AWS CLI, choose the tab that matches how you want to work.

------
#### [ Console ]

**To request a phone number (console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**, and then choose **Request originator**.

1. For **Country**, choose the destination country, and for **Number settings** select the capabilities you need (such as **VOICE**). Choose a number type that supports your destination, then follow the prompts to request the number. Some number types require registration before you can send.

1. To finish without waiting for registration, request a **Simulator number** instead. Simulator numbers send realistic events without using the carrier network.

------
#### [ AWS CLI ]

Use the [request-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.html) command. Replace {{XX}} with the two-letter ISO country code and {{NUMBER\_TYPE}} with a type that supports your destination (such as `LONG_CODE`, `TOLL_FREE`, or `SHORT_CODE`).

```
$ aws pinpoint-sms-voice-v2 request-phone-number \
> --iso-country-code {{XX}} \
> --message-type {{TRANSACTIONAL}} \
> --number-capabilities {{VOICE}} \
> --number-type {{NUMBER_TYPE}}
```

------
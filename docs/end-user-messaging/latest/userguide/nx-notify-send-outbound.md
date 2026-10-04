

# Send OTP code
<a name="nx-notify-send-outbound"></a>

Notify sends one-time passcode (OTP) and verification messages from pre-approved templates over SMS, voice, and WhatsApp. You send a code with the **Send OTP code** actions, and, when AWS End User Messaging generates the code for you, you confirm what the recipient entered with the **Validate OTP code** action.

Who generates the passcode determines which actions you use. When you generate the code, you create it in your application and send it with `SendNotifyTextMessage` or `SendNotifyVoiceMessage` (the `sms-voice` namespace); you validate it yourself, so there is no validate API call. When AWS End User Messaging generates the code, the service creates and sends it with `SendNotifyCodeVerification` and checks it with `ValidateNotifyCodeVerification` (the `endusermessaging` namespace).

Each send uses a pre-approved message template. You set a default template on your Notify configuration, or pass a template ID in the send request. For how templates work and how to browse them, see [Step 2: Create a Notify configuration](nx-notify-get-set-up-create.md).

## Send a code you generate (SMS or voice)
<a name="nx-notify-send-otp-text"></a>

You create the passcode in your application and pass it as a template variable. Use `SendNotifyTextMessage` for SMS or `SendNotifyVoiceMessage` for voice.

------
#### [ Console ]

**To send a test message**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Navigate to a Notify configuration and choose the **Test** tab.

1. For **Destination phone number**, enter a phone number in E.164 format, for example `+12065550100`.

1. (Optional) For **Configuration set**, choose a configuration set to track message events.

1. For **Channel**, choose **Text** or **Voice**. Text automatically uses RCS or SMS based on the recipient's capability.

1. Under **Template**, search or filter by language, then select a template from the table.

1. Choose **Send test message**. Expand **API preview** to see the request body before you send.

------
#### [ AWS CLI ]

Use `send-notify-text-message` for SMS. For voice, use `send-notify-voice-message` and add `--voice-id` to choose an Amazon Polly voice. For voice, separate the digits with periods or spaces, for example `"1. 2. 3. 4. 5. 6."`, so the text-to-speech engine reads each digit individually.

```
$ aws pinpoint-sms-voice-v2 send-notify-text-message \
    --notify-configuration-id {{nc-1234567890abcdef0}} \
    --destination-phone-number {{+12065550100}} \
    --template-id {{notify-code-verification-english-001}} \
    --template-variables '{"code":"123456"}'
```

------
#### [ Python (Boto3) ]

```
import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_notify_text_message(
    NotifyConfigurationId='nc-1234567890abcdef0',
    DestinationPhoneNumber='+12065550100',
    TemplateId='notify-code-verification-english-001',
    TemplateVariables={
        'code': '123456'
    }
)

print(f"Message ID: {response['MessageId']}")
print(f"Resolved body: {response.get('ResolvedMessageBody')}")
```

------

## Send a code that AWS End User Messaging generates
<a name="nx-notify-send-otp-generated"></a>

AWS End User Messaging generates the passcode, delivers it over the channel you choose, and tracks it for validation, backed by a notify code configuration that defines the policy (code length, validity period, and templates). Use the `SendNotifyCodeVerification` operation in the `endusermessaging` namespace.

------
#### [ Console ]

**To send a test verification code**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Under **Notify**, choose **Code configurations**, and then choose **Testing** to open **Send a test verification**. This sends and validates a passcode without creating any resources.

1. On the **Send code** tab, for **Channel** choose **Text**, **Voice**, or **WhatsApp**. For **Send using**, choose **Use Notify Configuration** to send from a preconfigured bundle, or **Bring your own origination** to supply your own origination identity and an inline template body.

1. For **Destination phone number**, enter the number that receives the code, in E.164 format.

1. (Optional) For **Code configuration**, choose a code configuration to control how the code is generated, how long it stays valid, and the maximum attempts. Use **Advanced options** to override the policy defaults, add request context, or restrict destination countries.

1. Choose **Send verification code**.

------
#### [ AWS CLI ]

Send a passcode with the [send-notify-code-verification](https://docs.aws.amazon.com/cli/latest/reference/endusermessaging/send-notify-code-verification.html) command. Set `--channel` to `TEXT`, `VOICE`, or `WHATSAPP`, and use the same `--reference-id` on the send and validate requests to bind them together.

```
$ aws endusermessaging send-notify-code-verification \
> --channel {{TEXT}} \
> --origination-identity {{+15550000000}} \
> --destination-identity {{+15550123456}} \
> --notify-code-configuration {{cc-3bnvvqhwq05xr3fkj}} \
> --reference-id {{signup-flow-1}}
```

The response returns a `messageId` and a `verificationId`. Validate the code the recipient submits as described in [Validate OTP code](nx-notify-send-validate.md).

------

For the full console procedures, policy overrides, and parameters, see [Send a passcode](nx-features-notify-code-config-send.md).

## Related information
<a name="nx-notify-send-related"></a>

These capabilities apply across AWS End User Messaging and are documented in the Messaging Features section:
+ [Configuration sets](nx-features-configuration-sets.md) and [Messaging Events](nx-features-messaging-events.md) – route and read delivery events for your messages.
+ [Opt-out lists](nx-features-opt-out-list.md) – opt-out behavior, which applies when you associate your own phone pool. Notify selects the best origination identity automatically, preferring customer-owned identities in an associated pool and falling back to AWS-managed identities; two-way messaging requires your own pool.
+ For the full send request parameters, see the `SendNotifyTextMessage`, `SendNotifyVoiceMessage`, and `SendNotifyCodeVerification` operations in the API reference.
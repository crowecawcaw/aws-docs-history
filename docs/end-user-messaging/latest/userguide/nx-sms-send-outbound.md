

# Outbound messaging
<a name="nx-sms-send-outbound"></a>

After you set up an origination identity and a configuration set, you send an SMS message with the `SendTextMessage` operation. Use the AWS End User Messaging console to send a test message, or the AWS CLI to send from your application. The examples use a phone pool as the origination identity, which is the recommended approach; you can also specify a single phone number or sender ID instead.

**Note**  
A single SMS message carries up to 140 bytes. Longer messages are split into multiple parts and billed per part, and AWS End User Messaging automatically selects the most efficient encoding. For character encoding, message size, and throughput, see [Limits and quotas](nx-sms-scale-limits.md).

------
#### [ Console ]

Use the console to send a test message without writing any code. This is the fastest way to confirm that your origination identity and configuration set work. While your account is in the sandbox, you can only send to verified destination phone numbers, or between simulator numbers.

**To send a test message from the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Overview**, in the **Quick start** section, choose **Test SMS sending**.

1. For **Originator**, choose **Phone pool** and select your pool. To send from a specific resource instead, choose **Phone number** or **Sender ID**. If you need a simulator phone number, choose **Request simulator number**, choose a **Country**, and then choose **Request number**.

1. For **Destination number**, choose **Simulator number** or **Verified number** and select the number from the list.

1. For **Configuration set**, choose the configuration set that receives the event data.

1. For **Message body**, enter a custom SMS message, and then choose **Send test message**.

**Important**  
Simulator phone numbers can only send to other simulator destination phone numbers. They behave like actual phone numbers without sending over the carrier network, and you cannot use a simulator phone number to verify a destination phone number. For example, US simulator phone numbers can only send to US destination simulator phone numbers.

------
#### [ AWS CLI ]

Use the [send-text-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-text-message.html) command. The example sends from a phone pool.

```
$ aws pinpoint-sms-voice-v2 send-text-message \\
> --destination-phone-number {{+14255550168}} \\
> --origination-identity {{pool-a1b2c3d4e5f6g7h8i}} \\
> --message-body {{"This is a test message."}} \\
> --message-type {{TRANSACTIONAL}} \\
> --configuration-set-name {{MyConfigurationSet}}
```

In the preceding command, make the following changes:
+ Replace {{\+14255550168}} with the destination phone number, in E.164 format.
+ Replace {{pool-a1b2c3d4e5f6g7h8i}} with your origination identity. Using a phone pool is recommended. To send from a specific resource instead, provide a phone number or sender ID.
+ Replace the value of `--message-body` with the message to send.
+ Set `--message-type` to `TRANSACTIONAL` for critical or time-sensitive messages, or `PROMOTIONAL` otherwise.
+ Replace {{MyConfigurationSet}} with the name or ARN of the configuration set that captures delivery events.

------
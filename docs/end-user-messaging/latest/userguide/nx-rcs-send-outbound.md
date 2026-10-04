

# Outbound messaging
<a name="nx-rcs-send-outbound"></a>

You send an RCS message with the `SendTextMessage` operation. Use the AWS End User Messaging console to send a test message from your AWS RCS Agent, or the AWS CLI to send from your application. The examples use a phone pool as the origination identity, which is the recommended approach: when the pool contains both an AWS RCS Agent and SMS phone numbers, the service attempts RCS first and automatically falls back to SMS from the same pool. To send from a specific resource instead, specify an AWS RCS Agent ARN, which delivers over RCS only with no fallback. For details on configuring pools with AWS RCS Agents, see [Resiliency](nx-rcs-scale-fallback.md).

------
#### [ Console ]

After your test device has accepted the tester invitation, you can send a test message from the console.

**To send a test message from the console**

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and choose the **Testing** tab.

1. Choose **Outbound test messages**. The console displays a preview of how your message renders on the recipient device, along with the JSON request body and CLI command.

1. Choose a verified test device from the list.

1. Enter your message text.

1. Choose **Send test message**.

------
#### [ AWS CLI ]

Use the `send-text-message` command. The example sends through a phone pool, so the service selects the best identity and falls back to SMS if RCS delivery is not possible.

```
aws pinpoint-sms-voice-v2 send-text-message \\
    --destination-phone-number {{+12065550100}} \\
    --origination-identity {{pool-a1b2c3d4e5f6g7h8i}} \\
    --message-body {{"Your appointment is confirmed for tomorrow at 2:00 PM."}} \\
    --message-type {{TRANSACTIONAL}}
```

Replace {{pool-a1b2c3d4e5f6g7h8i}} with your origination identity. Using a phone pool is recommended. To send over RCS only with no SMS fallback, specify an AWS RCS Agent ARN instead, for example `arn:aws:sms-voice:us-east-1:123456789012:rcs-agent/rcs-a1b2c3d4`. The `send-text-message` command is the same one you use for SMS; the origination identity you provide determines how the message is routed.

To send rich RCS content such as cards, carousels, media, and suggestions, use the `SendRcsMessage` operation instead.

------

RCS provides device-level delivery receipts through Amazon EventBridge and configuration set event destinations, including the final delivery status and whether the message was delivered over RCS or SMS. For delivery status values and channel attribution, see [Monitoring](nx-rcs-scale-monitoring.md).
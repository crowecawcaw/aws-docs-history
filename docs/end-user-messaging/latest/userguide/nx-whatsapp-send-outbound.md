

# Outbound messaging
<a name="nx-whatsapp-send-outbound"></a>

WhatsApp business messaging is template-first. To open a conversation with a recipient, you send a message built from a Meta-approved template by calling `SendWhatsAppMessage` with your originating phone number ID, the recipient, and the approved template. After the first template message, you can exchange free-form messages within the open conversation window.

Before you send, make sure you have an approved template. For how to create and submit one, see [Step 3: Get a message template](nx-whatsapp-gsu-template.md).

------
#### [ Console ]

Use the console to send a test message without writing code.

**To send a test message from the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. Under **Social messaging**, choose **Send test message**.

1. Choose the WhatsApp Business Account and the originating phone number to send from.

1. For the recipient, enter a phone number in E.164 format. While your account is in the sandbox, the recipient must be a verified test number.

1. Choose an approved template, choose its language, and provide any values the template requires.

1. Choose **Send test message**.

------
#### [ AWS CLI ]

Use the `send-whatsapp-message` command. Pass the originating phone number ID and a Meta-formatted message payload. The following example sends an approved template to a recipient.

```
aws socialmessaging send-whatsapp-message \
    --origination-phone-number-id {{phone-number-id-abc123}} \
    --meta-api-version {{v20.0}} \
    --message '{
        "messaging_product": "whatsapp",
        "to": "{{+14085551234}}",
        "type": "template",
        "template": {
            "name": "{{order_update_basic}}",
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "{{Jane}}"},
                        {"type": "text", "text": "{{12345}}"}
                    ]
                }
            ]
        }
    }'
```

In the preceding command, make the following changes:
+ Replace {{phone-number-id-abc123}} with the ID of the originating WhatsApp phone number on your linked WhatsApp Business Account.
+ Replace the `to` value with the recipient phone number, in E.164 format.
+ Set `template.name` and `language.code` to your approved template and its language, and provide a parameter for each variable the template declares.

After the conversation window is open, you can set `type` to `text` (or another supported message type) to exchange free-form messages without a template. For the full message payload reference, see the `SendWhatsAppMessage` operation in the AWS End User Messaging Social Messaging API Reference.

------
# Message and event format in AWS End User Messaging Social

The JSON object for an event contains the AWS event header and WhatsApp JSON payload.
For a list of the JSON WhatsApp notification payload and values, see [Webhooks Notification Payload Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components "https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components") and [Message Status](https://developers.facebook.com/docs/whatsapp/conversation-types#message-status "https://developers.facebook.com/docs/whatsapp/conversation-types#message-status") in the _WhatsApp Business Platform Cloud API Reference_.

## AWS End User Messaging Social event header

The JSON object for an event contains the AWS event header and WhatsApp JSON. The
header contains the AWS identifiers and ARNs of your WhatsApp Business Account (WABA) and
phone number.

```
{
  "context": {
    "MetaWabaIds": [
      {
        "wabaId": "1234567890abcde",
        "arn": "arn:aws:social-messaging:us-east-1:123456789012:waba/fb2594b8a7974770b128a409e2example"
      }
    ],
    "MetaPhoneNumberIds": [
      {
        "metaPhoneNumberId": "abcde1234567890",
        "arn": "arn:aws:social-messaging:us-east-1:123456789012:phone-number-id/976c72a700aac43eaf573ae050example"
      }
    ]
  },
  "whatsAppWebhookEntry": "{\"...JSON STRING....",
  "aws_account_id": "123456789012",
  "message_timestamp": "2025-01-08T23:30:43.271279391Z",
  "messageId": "6d69f07a-c317-4278-9d5c-6a84078419ec"
}
//Decoding the contents of whatsAppWebhookEntry
{
//WhatsApp notification payload
}

```

In the preceding example event:

- `1234567890abcde` is the WABA id from Meta.
- `abcde1234567890` is the phone number id from Meta.
- `fb2594b8a7974770b128a409e2example` is the ID of the WhatsApp Business Account (WABA).
- `976c72a700aac43eaf573ae050example` is the ID of the phone number.

## Example WhatsApp JSON

for receiving a message

The following shows the event record for an incoming message from WhatsApp. The JSON
received from WhatsApp in the `whatsAppWebhookEntry` is received as a JSON string
and can be converted to JSON. For a list of fields and their meaning, see [Webhooks
Notification Payload Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components "https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components") in the _WhatsApp Business Platform Cloud API
Reference_.

```
{
  "context": {
    "MetaWabaIds": [
      {
        "wabaId": "1234567890abcde",
        "arn": "arn:aws:social-messaging:us-east-1:123456789012:waba/fb2594b8a7974770b128a409e2example"
      }
    ],
    "MetaPhoneNumberIds": [
      {
        "metaPhoneNumberId": "abcde1234567890",
        "arn": "arn:aws:social-messaging:us-east-1:123456789012:phone-number-id/976c72a700aac43eaf573ae050example"
      }
    ]
  },
  "whatsAppWebhookEntry": "{\"...JSON STRING....",
  "aws_account_id": "123456789012",
  "message_timestamp": "2025-01-08T23:30:43.271279391Z",
  "messageId": "6d69f07a-c317-4278-9d5c-6a84078419ec"
}
```

You can use a tool, such as [jq](https://jqlang.org/ "https://jqlang.org/"), to convert the
JSON string to JSON. The following is the `whatsAppWebhookEntry` in JSON
form:

```
{
  "id": "503131219501234",
  "changes": [
    {
      "value": {
        "messaging_product": "whatsapp",
        "metadata": {
          "display_phone_number": "14255550123",
          "phone_number_id": "46271669example"
        },
        "statuses": [
          {
            "id": "wamid.HBgLMTkxNzM5OTI3MzkVAgARGBJBMTM4NDdGRENEREI5Rexample",
            "status": "sent",
            "timestamp": "1736379042",
            "recipient_id": "01234567890",
            "conversation": {
              "id": "62374592e84cb58e52bdaed31example",
              "expiration_timestamp": "1736461020",
              "origin": {
                "type": "utility"
              }
            },
            "pricing": {
              "billable": true,
              "pricing_model": "CBP",
              "category": "utility"
            }
          }
        ]
      },
      "field": "messages"
    }
  ]
}

```

## Example WhatsApp JSON for receiving a media message

The following shows the event record for an incoming media message. To retrieve the
media file, use the GetWhatsAppMessageMedia API command. For a list of fields and their
meaning, see [Webhooks
Notification Payload Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components "https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components")

```
{
//AWS End User Messaging Social header
}
//Decoding the contents of whatsAppWebhookEntry
{
  "id": "365731266123456",
  "changes": [
    {
      "value": {
        "messaging_product": "whatsapp",
        "metadata": {
          "display_phone_number": "12065550100",
          "phone_number_id": "321010217760100"
        },
        "contacts": [
          {
            "profile": {
              "name": "Diego"
            },
            "wa_id": "12065550102"
          }
        ],
        "messages": [
          {
            "from": "14255550150",
            "id": "wamid.HBgLMTQyNTY5ODgzMDIVAgASGCBDNzBDRjM5MDU2ODEwMDkwREY4ODBDRDE0RjVGRkexample",
            "timestamp": "1723506230",
            "type": "image",
            "image": {
              "mime_type": "image/jpeg",
              "sha256": "BTD0xlqSZ7l02o+/upusiNStlEZhA/urkvKf143Uqjk=",
              "id": "530339869524171"
            }
          }
        ]
      },
      "field": "messages"
    }
  ]
}
```

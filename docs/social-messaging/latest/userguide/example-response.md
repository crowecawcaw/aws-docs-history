# Example of responding to a message with a read receipt

and reaction

In this example, your customer, Diego, sent you a message saying "Hi" and you respond to
him with a read receipt and hand wave emoji.

## Prerequisites

To receive a notification that Diego sent a message, you must have set up an event
destination Amazon SNS topic and subscribed to a topic endpoint.

## Responding

1. When the message from Diego is received, an event is published to the
   endpoints of the topic. The following is a snippet of what the topic
   publishes.

###### Note

Because Diego initiated the conversation, it doesn't count against the quota for your business
initiated conversations.

The `whatsAppWebhookEntry` in this example is shown in JSON
notation. For an example of converting the
`whatsAppWebhookEntry` from JSON sting to JSON, see [Example WhatsApp JSON
for receiving a message](managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-text "managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-text").

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
  "message_timestamp": "2025-01-08T23:30:43.271279391Z"
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
          "phone_number_id": "321010217712345"
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
            "timestamp": "1723506035",
            "text": {
              "body": "Hi"
            },
            "type": "text"
          }
        ]
      },
      "field": "messages"
    }
  ]
}
```

2. To show Diego you received the message, set the status to `read`.
   Diego will see two blue check marks next to the message on his device.

###### Note

You must specify base64 encoding when you use the AWS CLI version 2. This
can be done by adding the AWS CLI paramater `--cli-binary-format
 raw-in-base64-out` or changing the AWS CLI global configuration file. For more
information, see [`cli_binary_format`](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings") in the
_AWS Command Line Interface User Guide for Version
2_.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","message_id":"'`{MESSAGE_ID}`'","status":"read"}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

In the preceding command, do the following:

    * Replace `{ORIGINATION_PHONE_NUMBER_ID}` with
     the phone number ID that Diego sent his message to
     `phone-number-id-976c72a700aac43eaf573ae050example`.
    * Replace `{MESSAGE_ID}` with the unique
     identifier of the message. This is the same value of the `id`
     field in the received message
     `wamid.HBgLMTQyNTY5ODgzMDIVAgASGCBDNzBDRjM5MDU2ODEwMDkwREY4ODBDRDE0RjVGRkexample`.

3. You can send Diego a hand wave reaction.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","recipient_type":"individual","to":"'`{PHONE_NUMBER}`'","type": "reaction","reaction": {"message_id": "'`{MESSAGE_ID}`'","emoji":"\uD83D\uDC4B"}}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

In the preceding command, do the following:

    * Replace `{PHONE_NUMBER}` with Diego's phone
     number, `14255550150`.
    * Replace `{MESSAGE_ID}` with the unique
     identifier of the message. This is the same value of the `id`
     field in the received message
     `wamid.HBgLMTQyNTY5ODgzMDIVAgASGCBDNzBDRjM5MDU2ODEwMDkwREY4ODBDRDE0RjVGRkexample`.
    * Replace `{ORIGINATION_PHONE_NUMBER_ID}` with
     the phone number ID that Diego sent his message to:
     `phone-number-id-976c72a700aac43eaf573ae050example`.

## Additional resources

- Enable [event destinations](managing-event-destinations.md "managing-event-destinations.md") to log events and receive incoming messages.
- For a list of WhatsApp
  message objects, see [Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#message-object "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages#message-object") in the _WhatsApp Business Platform Cloud API
  Reference_.

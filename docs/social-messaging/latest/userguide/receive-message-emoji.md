

# Example of responding to a message with a reaction in AWS End User Messaging Social
<a name="receive-message-emoji"></a>

You can add a reaction to the message, like a thumbs up. 

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","recipient_type":"individual","to":"'{{{PHONE_NUMBER}}}'","type": "reaction","reaction": {"message_id": "'{{{MESSAGE_ID}}}'","emoji":"\uD83D\uDC4D"}}' --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --meta-api-version v20.0
```

In the preceding command, do the following:
+ Replace {{{PHONE\_NUMBER}}} with your customer's phone number.
+ Replace {{{MESSAGE\_ID}}} with the unique identifier of the message. Use the value of the `id` field in the message object of the Amazon SNS topic.
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.
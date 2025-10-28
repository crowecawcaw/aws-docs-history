# Example of changing a message's status to read

in AWS End User Messaging Social

You can set the [status of the message](managing-event-destinations-status.md "managing-event-destinations-status.md") to `read` to show the end user two blue check marks on their screen.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","message_id":"'`{MESSAGE_ID}`'","status":"read"}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

In the preceding command, do the following:

- Replace `{ORIGINATION_PHONE_NUMBER_ID}` with your phone number's ID.
- Replace `{MESSAGE_ID}` with the unique identifier of the message. Use the value of the `id` field in the message object of the Amazon SNS topic.

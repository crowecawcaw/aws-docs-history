# WhatsApp message status

When you send a message, you receive status updates about the message. You have to enable
event logging to receive these notifications, see [Message and event destinations in AWS End User Messaging Social](managing-event-destinations.md "managing-event-destinations.md").

## Message statuses

The following table contains possible message statuses.

| Status name | Description                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| deleted     | The customer deleted the message, and you should also delete the message if it was downloaded to your server. |
| delivered   | The message was successfully delivered to the customer.                                                       |
| failed      | The message failed to send.                                                                                   |
| read        | The customer read the message. This status is only sent if the customer has read receipts turned on.          |
| sent        | The message has been sent but is still in transit.                                                            |
| warning     | The message contains an item that is unavailable or doesn't exist.                                            | ## Additional resources For more information, see [Message Status](https://developers.facebook.com/docs/whatsapp/conversation-types#message-status "https://developers.facebook.com/docs/whatsapp/conversation-types#message-status") in the _WhatsApp Business Platform Cloud API Reference_. |

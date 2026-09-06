

# WhatsApp message status
<a name="managing-event-destinations-status"></a>

When you send a message, you receive status updates about the message. You have to enable event logging to receive these notifications, see [Message and event destinations in AWS End User Messaging Social](managing-event-destinations.md).

## Message statuses
<a name="managing-event-destinations-status_body"></a>

The following table contains possible message statuses.



| Status name | Description | 
| --- | --- | 
| accepted | The message has been accepted by WhatsApp for processing. | 
| deleted | The customer deleted the message, and you should also delete the message if it was downloaded to your server. | 
| delivered | The message was successfully delivered to the customer. | 
| failed | The message failed to send. | 
| Message retries exhausted, dropping message. | The message could not be handed off to WhatsApp within the 180-minute retry period and was dropped. | 
| read | The customer read the message. This status is only sent if the customer has read receipts turned on. | 
| sent | The message has been sent but is still in transit. | 
| warning | The message contains an item that is unavailable or doesn't exist. | 

## Additional resources
<a name="managing-event-destinations-status_additional_resources"></a>

For more information, see [Message Status](https://developers.facebook.com/docs/whatsapp/conversation-types#message-status) in the *WhatsApp Business Platform Cloud API Reference*.


# Send a message
<a name="nx-whatsapp-send"></a>

WhatsApp business messaging is template-first: you start a conversation by sending an approved message template, and then you exchange free-form messages within the open conversation window. You send WhatsApp messages with the `SendWhatsAppMessage` operation in the AWS End User Messaging Social Messaging API (the `social-messaging` namespace).

## API operations
<a name="nx-whatsapp-send-operations"></a>

Use the following API operation to send WhatsApp messages.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendWhatsAppMessage` | Sends a WhatsApp message – an approved template to open a conversation, or free-form content within an open conversation window. | All outbound WhatsApp. | 

## In this section
<a name="nx-whatsapp-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-whatsapp-send-outbound.md) | Create and submit a message template for approval, then send WhatsApp messages and exchange free-form content within the conversation window. | 

**Inbound messaging**



|  |  | 
| --- |--- |
| [Inbound messaging](nx-whatsapp-send-inbound.md) | Route inbound messages and status events to an event destination so your application can respond within the conversation window. | 
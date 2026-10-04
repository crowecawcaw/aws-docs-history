

# Setup WhatsApp
<a name="nx-whatsapp"></a>

WhatsApp lets your business reach customers on WhatsApp with rich, interactive messaging and two-way conversations. You message customers from a WhatsApp Business Account using approved message templates to start conversations, and you can respond to inbound messages in a session window. Common use cases include order and shipping updates, appointment reminders, customer support conversations, and interactive flows that collect information without leaving WhatsApp.

You send WhatsApp messages with the AWS End User Messaging Social API (the `social-messaging` namespace, which you call as `aws socialmessaging` on the AWS CLI). The main send operation is `SendWhatsAppMessage`, which sends a message from a phone number on your linked WhatsApp Business Account.

**Key concepts**


| Concept | Description | 
| --- | --- | 
| WhatsApp Business Account (WABA) | The Meta business account you link to AWS End User Messaging to send and receive WhatsApp messages. You link your WABA during setup. | 
| Phone number | The business phone number on your WABA that messages are sent from and received on. | 
| Message template | A preformatted, Meta-approved message you use to start a conversation or send a notification outside an open session window. | 
| Configuration set | A set of rules applied to the messages you send, including where to send delivery and message-status events. | 
| Two-way messaging | Inbound messages from customers, routed to your application so you can respond within the session window. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-whatsapp-get-set-up.md) | Link a WhatsApp Business Account, add a phone number, and send a test message. | You are new to WhatsApp and want a working test send. | 
| [Send a message](nx-whatsapp-send.md) | Send template and session messages from your application, and handle inbound replies. | You have a linked WABA and want to send from your own code. | 
| [Scale](nx-whatsapp-scale.md) | Monitor delivery, manage message templates, and apply best practices. | You are sending in production and want to keep it healthy and grow. | 
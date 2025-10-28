# WhatsApp Business messaging capabilities and

limitations with Amazon Connect

The WhatsApp Business messaging integration provides the following capabilities:

- Text messages
- Interactive messages. For more information, see [Add Amazon Lex interactive messages for customers in
  chat](interactive-messages.md "interactive-messages.md").
- Messages with rich link previews
- Delivered and read receipts for business messages
- Attachments

## Limitations

When integrating WhatsApp Business messaging with Amazon Connect, be aware of the following
limitations:

###### Delivery receipt limitations

- Read receipts for customer messages are not supported.
- Delivery receipts for customer messages are not supported. The delivery receipts that
  appear in WhatsApp indicate that WhatsApp has received the message, not Amazon Connect.

###### Text message limitations

- Inbound text messages from customers greater than 1024 characters are not supported.

###### Unsupported message types

- Inbound contact messages sent by customers are not supported.
- Inbound location messages sent by customers are not supported.
- Reaction messages sent by customers are not supported.
- Reply messages sent by customers are not supported. New message content is delivered
  without the reply context.
- Receiving message statuses that a message was deleted by the customer is not supported.

###### Attachment limitations

- All attachments from customers when initiating a new contact or conversation are not
  supported. Customers can only send attachments during an existing contact.
- Attachments from customers greater than 20MB are not supported.
- Attachments with captions are not supported. Amazon Connect removes any captions and delivers the
  attachment.
- Sticker attachments are not supported.

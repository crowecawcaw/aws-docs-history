# Adding webhooks to a chat room

Webhooks send messages to chat rooms programmatically. For example, a webhook can notify a customer service team about the creation of a new,
high-priority ticket and add a link to the ticket in the chat message. Webhooks require custom development or third-party tools that can help integrate
external systems with Amazon Chime.

Webhooks only work with chat rooms. You can't share them. Amazon Chime chat room administrators can add up to 10 webhooks to a chat room.

###### Note

Chat room members can't interact with webhooks or send messages back to them.

###### To add a webhook to a chat room

1. In the sidebar, open the chat room.
2. Choose the ellipsis menu located to the right of the chat room name, then choose **Manage webhooks and bots**.
3. In the **Manage incoming webhooks and bots in** _chat room name_ dialog box, choose
   **Add webhook**.
4. In the **Create webhook for** _chat room name_ dialog box, enter a name for the bot.
5. Choose **Create**.
6. Choose the **Copy URL** link to copy the webhook's URL.
7. Send the webhook URL to the webhook developer.
   The webhook developer uses the webhook URL in their application to allow it to send messages to the Amazon Chime chat room.
   The webhook appears in the chat room roster with a webhook icon next to its name. Chat room messages sent by the webhook appear in the
   chat room under the webhook name followed by (**Webhook**).

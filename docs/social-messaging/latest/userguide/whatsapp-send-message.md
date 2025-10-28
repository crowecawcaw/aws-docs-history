# Sending messages through WhatsApp with AWS End User Messaging Social

Before sending a message, you must set up your WhatsApp Business Account (WABA), and your
user must opt in to receive messages from you. For more information, see [Obtain permission](whatsapp-best-practices.md#best-practices-whatsapp-obtain-permission "whatsapp-best-practices.md#best-practices-whatsapp-obtain-permission").

When a user messages you, a 24-hour timer called a customer service window starts or
refreshes. All message types, except for template messages, can only be sent when a customer
service window is open between you and the user. Template messages can be sent at any time,
as long as the user has opted in to receive messages from you.

For each message that you send or receive, a message status is generated and sent to the
event destination. If your customer has not signed up for WhatsApp, an event is generated
with a message status of `fail`. You must turn on a [message and event destination](managing-event-destinations.md "managing-event-destinations.md") to receive
the [message status](managing-event-destinations-status.md "managing-event-destinations-status.md").

For a list of
message types, see [Messages](https://developers.facebook.com/docs/whatsapp/conversation-types/ "https://developers.facebook.com/docs/whatsapp/conversation-types/")
in the _WhatsApp Business Platform Cloud API Reference_.

###### Important

###### Working with Meta/WhatsApp

- Your use of the WhatsApp Business Solution is subject to the terms and
  conditions of the [WhatsApp Business Terms of Service](https://www.whatsapp.com/legal/business-terms "https://www.whatsapp.com/legal/business-terms"), the [WhatsApp
  Business Solution Terms](https://www.whatsapp.com/legal/business-solution-terms "https://www.whatsapp.com/legal/business-solution-terms"), the [WhatsApp Business Messaging
  Policy](https://business.whatsapp.com/policy "https://business.whatsapp.com/policy"), the [WhatsApp Messaging
  Guidelines](https://www.whatsapp.com/legal/messaging-guidelines "https://www.whatsapp.com/legal/messaging-guidelines"), and all other terms, policies, or guidelines
  incorporated therein by reference. These might be updated from time to time.
- Meta or WhatsApp may at any time prohibit your use of the WhatsApp Business
  Solution.
- In connection with your use of the WhatsApp Business Solution, you will not
  submit any content, information, or data that is subject to safeguarding or
  limitations on distribution pursuant to applicable laws or regulations.

###### Topics

- [Example of sending a template message in AWS End User Messaging Social](send-message-text.md "send-message-text.md")
- [Example of sending a media message in
  AWS End User Messaging Social](send-message-media.md "send-message-media.md")

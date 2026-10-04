

# Choosing a messaging service
<a name="nx-overview-choosing"></a>

Several AWS services can send messages to your end users, and it is not always obvious which one to use. AWS End User Messaging is the layer responsible for delivering messages to end users across AWS, so when another service such as Amazon SNS, Amazon Cognito, or Amazon Connect sends a message, that message is delivered through AWS End User Messaging. Use the following table to decide whether to work with AWS End User Messaging directly, so that you control the channel and send across SMS, MMS, RCS, WhatsApp, push, and voice, or through a service that sends messages on your behalf as part of a larger workflow, such as user authentication or a contact-center interaction.

Regardless of which service you use, you must still set up your sending resources in AWS End User Messaging. You get a phone number, sender ID, or WhatsApp Business Account (WABA) through AWS End User Messaging, and your messaging spend appears under AWS End User Messaging on your AWS bill. When you want granular control of your messaging, AWS End User Messaging is where you configure it directly. The other services use AWS End User Messaging for message transport, but each adds its own handling of concerns such as rate limiting, opt-outs, and protection against fraud and artificially inflated traffic.


**Choosing a messaging service**  

| Service | Channels | Use it when | 
| --- | --- | --- | 
| AWS End User Messaging | SMS, MMS, RCS, WhatsApp, push, voice | You want a wide selection of channels and end-to-end control over them to build conversational experiences across SMS, MMS, RCS, WhatsApp, push, and voice. You configure opt-outs, manage number configurations such as two-way messaging, and send with operations such as `SendTextMessage`, `SendMediaMessage`, `SendVoiceMessage`, `SendWhatsAppMessage`, and `SendMessages`. The send APIs are synchronous, so a call returns immediately and tells you when you have hit a rate limit, which lets your application react in real time. This is the service that this guide documents. | 
| Amazon SNS | SMS, RCS\*, push | You already use the Amazon SNS publish/subscribe model and want to send a high volume of messages with built-in queue management. | 
| Amazon Cognito | SMS | SMS is part of user authentication, such as sign-up confirmation, multi-factor authentication (MFA), or one-time passwords (OTP), and Amazon Cognito is your identity provider. | 
| Amazon Connect | SMS, WhatsApp | Messaging is part of a contact-center or customer-service conversation, both outbound and inbound. | 
| Amazon Pinpoint | SMS, RCS\*, push, voice | You are an existing Amazon Pinpoint customer sending transactional SMS, MMS, voice, or push messages with the `SendMessages` API as part of your current application. Amazon Pinpoint is closed to new customers as of May 20, 2025, and support ends on October 30, 2026. For new messaging work, use AWS End User Messaging directly. | 

\* Supports limited RCS capability, including the ability to send basic text with an RCS agent, and does not include rich media support.
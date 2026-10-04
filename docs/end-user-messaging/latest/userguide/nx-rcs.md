

# Setup RCS
<a name="nx-rcs"></a>

RCS (Rich Communication Services) for business is a mobile messaging channel that upgrades SMS with verified brand identity and rich, interactive content, and automatically falls back to SMS when a recipient's device or carrier does not support RCS. Messages appear in the same messaging app recipients already use, but carry your verified brand name, logo, and colors. Common use cases include branded notifications and promotions, rich cards and carousels, interactive suggested replies and actions, and two-way conversations.

You send RCS with the AWS End User Messaging SMS and Voice v2 API (the `sms-voice` namespace, which you call as `aws pinpoint-sms-voice-v2` on the AWS CLI). Send plain text RCS with the same `SendTextMessage` operation you use for SMS, and send rich content such as rich cards, carousels, and media with `SendRcsMessage`.

**Key concepts**


| Concept | Description | 
| --- | --- | 
| AWS RCS Agent | The top-level resource that represents your brand for RCS. It binds together your testing agent and your per-country launch agents, and holds keyword and two-way messaging configuration. | 
| RCS for Business ID | The per-country agent identity created with the RCS infrastructure provider during registration. AWS End User Messaging manages these for you under your AWS RCS Agent. | 
| Phone pool with SMS fallback | A pool that contains both your AWS RCS Agent and SMS phone numbers. When you send through the pool, AWS End User Messaging attempts RCS first and falls back to SMS automatically. | 
| Configuration set | A set of rules applied to the messages you send, including where to send delivery, read, and interaction events. | 
| Delivery receipts (DLRs) | Device-level delivery confirmations. With RCS you are billed for messages confirmed delivered to the device, unlike SMS where charges apply when the carrier accepts the message. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-rcs-get-set-up.md) | Create and register an AWS RCS Agent, add a testing agent, and send a test RCS message. | You are new to RCS and want a working test send. | 
| [Send a message](nx-rcs-send.md) | Send text and rich RCS messages from your application, with SMS fallback. | You have a registered agent and want to send from your own code. | 
| [Scale](nx-rcs-scale.md) | Launch in additional countries, monitor delivery, and apply best practices. | You are sending in production and want to grow your reach. | 
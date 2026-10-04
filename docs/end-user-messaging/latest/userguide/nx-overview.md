

# What is AWS End User Messaging?
<a name="nx-overview"></a>

AWS End User Messaging helps you integrate scalable, reliable messaging into your applications so you can reach your customers on the channels they use and trust. Across SMS, MMS, WhatsApp, RCS, push, and voice, you can power conversational experiences that go beyond one-way alerts–from time-sensitive notifications and one-time passcodes to two-way conversations and the AI agents that drive them. AWS End User Messaging delivers your messages globally and brings your agents into the conversation so you can respond to customers in real time.

## What you can do with AWS End User Messaging
<a name="nx-overview-what-is-use-cases"></a>

You can use AWS End User Messaging to support a wide range of use cases across SMS, MMS, RCS, push, voice, and WhatsApp. The following table lists common use cases and the channels that fit each one.


| Use case | What it is | Channels that fit | 
| --- | --- | --- | 
| One-time passcodes and verification | Send one-time passcodes and verification codes for login, sign-up, and transaction authentication. With Notify, you can start sending in minutes without provisioning your own phone numbers. | SMS, voice, WhatsApp, Notify | 
| Order confirmations | Confirm a purchase or booking the moment it happens. | All channels | 
| Shipping and delivery updates | Keep customers informed as an order ships, moves, and arrives. | All channels | 
| Appointment reminders | Remind customers of upcoming appointments and reservations to reduce no-shows. | All channels | 
| Account alerts | Notify customers of security events, balance changes, and status updates on their account. | All channels | 
| Marketing and promotions | Reach your audience with product launches, limited-time offers, and event invitations, using rich media and verified brand identity to drive engagement. | All channels | 
| Alerts and public outreach | Deliver time-sensitive alerts, citizen or member outreach, and must-deliver operational messages at global scale. | All channels | 
| Two-way conversations | Let customers reply to and interact with your business, with inbound messages routed to your own applications. | SMS, RCS, WhatsApp | 
| Conversational AI and agents | Bring AI agents into the conversation to answer questions, resolve requests, and act on the customer's behalf in real time. | SMS, RCS, WhatsApp | 

## How this guide is organized
<a name="nx-overview-how-organized"></a>

This guide is organized around how you build with AWS End User Messaging, in three parts.


| Part | What it covers | 
| --- | --- | 
| Agent setup guide | The Agent setup guide shows you how to build with AWS End User Messaging using AI coding assistants such as Claude Code, Codex, Cursor, and Kiro. AWS End User Messaging publishes agent skills that give your assistant validated, step-by-step guidance for common tasks, including creating a Rich Communication Services (RCS) branded agent, sending a one-time passcode, registering to send SMS, and connecting a WhatsApp Business Account. When you configure your assistant with your AWS credentials, it can also run the underlying API calls for you. | 
| Channel setup chapters | The channel setup chapters walk you through getting each channel working from end to end, so that you set up the channel, send your first message, and scale your sending. Each of the SMS, RCS, MMS, voice, WhatsApp, push, and Notify channels has its own setup chapter. | 
| Messaging Features | The Messaging Features chapters are the reference for each capability: how to use phone numbers, sender IDs, pools, registrations, configuration sets, Protect, and the rest, grouped by what you do with them (identities you send from, registration and compliance, sending and configuration, tracking and delivery, and more). Each feature page shows you how to use that functionality through the console, the AWS CLI, and the API. | 
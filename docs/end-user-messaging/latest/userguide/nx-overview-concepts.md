

# Concepts
<a name="nx-overview-concepts"></a>

AWS End User Messaging provides a set of features that you use to send messages, manage the identities you send from, register to send in each country, and track delivery. The following table introduces each feature and links to where it is documented. For the full details of any feature, see its page under Messaging features.


**AWS End User Messaging features**  

| Feature | Description | 
| --- | --- | 
| [Brand profiles](nx-features-brand-profiles.md) | A container that stores your business identity once so you can reuse it across registrations, holding attributes such as company information, addresses, and compliance documents. | 
| [Carrier lookup](nx-features-carrier-lookup.md) | A service that returns information about a phone number, including whether it is valid, its type, and its carrier. | 
| [Configuration sets](nx-features-configuration-sets.md) | A set of rules that you apply to the messages you send, including where to send delivery and engagement events. | 
| [Keywords](nx-features-keywords.md) | The words that recipients text to your number, and the responses you return. Keywords support opt-in, opt-out, and help flows. | 
| [Message feedback](nx-features-message-feedback.md) | A way to report the final outcome of a message so you can monitor SMS and MMS delivery. | 
| [Message part preview](nx-features-message-part-preview.md) | A preview of how an SMS message is encoded and split into message parts before you send it, so you can anticipate throughput and billing. | 
| [Messaging Events](nx-features-messaging-events.md) | The delivery and engagement events that AWS End User Messaging emits for SMS, MMS, and RCS messages, and their formats. | 
| [Notify code configurations](nx-features-notify-code-config.md) | A reusable one-time passcode policy and channel templates that a Notify configuration uses to send and validate verifications. | 
| [Notify configurations](nx-features-notify-config.md) | The central Notify resource that holds your brand identity and messaging settings for sending code-verification messages. | 
| [Opt-out lists](nx-features-opt-out-list.md) | A list of phone numbers that have opted out. AWS End User Messaging does not send messages to a number while it is on an opt-out list. | 
| [Phone numbers](nx-features-phone-numbers.md) | An identity that recipients see when you send an SMS or MMS message, including long codes, toll-free numbers, short codes, and 10DLC. | 
| [Phone pools](nx-features-phone-pools.md) | A collection of phone numbers or sender IDs that share the same settings. When you send through a pool, it chooses an appropriate origination identity for you. | 
| [Quotas](nx-features-quotas.md) | The quotas for AWS End User Messaging resources and sending, and how to manage them. | 
| [RCS Agents](nx-features-rcs-agents.md) | The top-level resource that represents your brand for RCS messaging, binding together your testing agent and your per-country launch agents. You define keywords and two-way messaging configuration on the RCS agent. | 
| [Registration reviewer](nx-features-registration-reviewer.md) | AI-powered feedback that reviews your phone number or sender ID registration before you submit it for downstream review. | 
| [Registrations](nx-features-registrations.md) | The registration process that many countries and channels require before you can send, covering sender IDs, dedicated numbers, and RCS. | 
| [Resource sharing](nx-features-resource-sharing.md) | Sharing AWS End User Messaging resources with other AWS accounts or services. | 
| [Sender IDs](nx-features-senders.md) | An alphanumeric name that identifies the sender of an SMS message. You request and manage sender IDs for the countries that support them. | 
| [Simulator numbers](nx-features-simulator-numbers.md) | Test phone numbers you use to simulate sending and receiving messages without delivering to a real device. | 
| [SMS Protect](nx-features-sms-protect.md) | A control that lets you send only to the countries or specific phone numbers that you allow, and helps protect against unexpected traffic. | 
| [WhatsApp Flows](nx-features-whatsapp-flows.md) | Interactive, multi-screen experiences that users complete without leaving WhatsApp, supporting data collection and form submissions. | 
| [WhatsApp Message Templates](nx-features-whatsapp-templates.md) | Preformatted WhatsApp message templates that you use to start conversations and send notifications to your customers. | 
| [WhatsApp Voice](nx-features-whatsapp-voice.md) | Voice calling that lets your business place and receive calls with WhatsApp users in the conversation, using the same business phone number you use for messaging. | 
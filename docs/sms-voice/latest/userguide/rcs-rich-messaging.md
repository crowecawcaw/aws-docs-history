

# Sending rich RCS messages
<a name="rcs-rich-messaging"></a>

With the `SendRcsMessage` API action in AWS End User Messaging, you can send rich, interactive content to recipients over RCS (Rich Communication Services). Rich RCS messages go beyond plain text to include rich cards, carousels, media files, and suggestions that recipients choose to take action. These interactive elements turn one-way notifications into two-way conversational experiences, such as letting a recipient confirm an appointment, browse a product catalog, or share their location without leaving the conversation.

Use `SendRcsMessage` when you need to deliver visually rich, interactive content, such as product cards with images and action buttons, appointment confirmations with a calendar suggestion, file attachments, or multi-item carousels that recipients scroll through. Each `SendRcsMessage` request includes a separate text body for any text content, and can include an optional SMS or MMS fallback for recipients whose devices do not support RCS.

For plain-text messages that do not require rich formatting, use the `SendTextMessage` API action instead. `SendTextMessage` accepts only text content, which makes the request simpler, and it works with messaging pools that automatically select between RCS and SMS based on recipient capability. For details, see [Sending RCS messages](rcs-send-message.md).

**Important**  
You can use RCS messaging with `SendRcsMessage` in all countries where RCS is supported. For the current list, see [Supported countries for RCS](rcs-supported-countries.md).

**Topics**
+ [Prerequisites](#rcs-rich-messaging-prerequisites)
+ [Choosing between SendTextMessage and SendRcsMessage](#rcs-rich-messaging-choosing)
+ [Content types](#rcs-rich-messaging-content-types)
+ [Suggestions](#rcs-rich-messaging-suggestions)
+ [SendRcsMessage request overview](#rcs-rich-messaging-api)
+ [Message size and count limits](#rcs-rich-messaging-limits)
+ [Delivery events and recipient actions](#rcs-rich-messaging-events)
+ [Best practices](#rcs-rich-messaging-best-practices)
+ [Text messages](rcs-text-messages.md)
+ [File messages](rcs-file-messages.md)
+ [Rich cards](rcs-rich-cards.md)
+ [Carousels](rcs-carousels.md)
+ [Suggestions](rcs-suggestions.md)
+ [Message expiration](rcs-message-expiration.md)
+ [Per-message fallback](rcs-fallback-per-message.md)
+ [Message events](rcs-events.md)
+ [Inbound media](rcs-inbound-media.md)
+ [Best practices](rcs-best-practices.md)
+ [Console rich messaging](rcs-console-rich-messaging.md)

## Prerequisites
<a name="rcs-rich-messaging-prerequisites"></a>

Before you send rich RCS messages, complete the RCS setup steps in [Getting started with RCS](rcs-getting-started.md). In addition to a registered AWS RCS Agent in the **Active** state, confirm the following:
+ To validate rich content before you send to production recipients, add a registered test device to your testing agent and send test messages to it. For details, see [Testing RCS messages](rcs-testing.md).
+ Configure an event destination (an Amazon SNS topic or Amazon Data Firehose delivery stream) to receive delivery status events. An event destination is required if your messages include interactive elements such as suggestions, because recipient selections are delivered to your application as postback events. For details, see [Event destinations in AWS End User Messaging SMS](configuration-sets-event-destinations.md).
+ If you configure an SMS or MMS fallback and you send to destinations with SMS pumping risk, associate a protect configuration to apply opt-out and country rules to the fallback message. For details, see [Fraud Protection in AWS End User Messaging SMS](protect.md).

## Choosing between SendTextMessage and SendRcsMessage
<a name="rcs-rich-messaging-choosing"></a>

Both API actions can deliver messages over RCS, but they serve different purposes. `SendTextMessage` assumes every message is deliverable as SMS and can also deliver it over RCS, which gives it a simpler request contract. `SendRcsMessage` assumes rich RCS content and adds capabilities that `SendTextMessage` does not have, including media and structured content types, message expiration with time-to-live (TTL), and per-message SMS or MMS fallback.


**SendTextMessage compared to SendRcsMessage**  

| Capability | SendTextMessage | SendRcsMessage | 
| --- | --- | --- | 
| Message content | Plain text only | Text, files, rich cards, and carousels, each with optional suggestions | 
| Delivery channels | RCS or SMS | RCS, with optional SMS or MMS fallback | 
| Channel selection | Pool selects RCS or SMS automatically by recipient capability | RCS first, then your configured SMS or MMS fallback | 
| Fallback | Automatic, pool based | Explicit, per message | 
| Origination identity | Pool, phone number, sender ID, or AWS RCS Agent | Pool or AWS RCS Agent | 
| Message expiration (TTL) | No | Yes | 
| Request contract | Simpler. Same API as SMS and MMS sending | Dedicated RCS API with a separate text body and content types | 

Choose `SendTextMessage` for plain-text notifications, when you want pool-based automatic channel selection, or when you are migrating existing SMS workflows with minimal code changes. Choose `SendRcsMessage` when you need rich cards, carousels, media files, or suggestions, when you want a defined per-message fallback, or when you need TTL-based expiration for time-sensitive content.

## Content types
<a name="rcs-rich-messaging-content-types"></a>

The `RcsMessageContent` parameter contains a `Content` object with exactly one content type, and an optional message-level `Suggestions` list. You cannot combine multiple content types in a single request.


**RCS content types**  

| Content type | Description | More information | 
| --- | --- | --- | 
| TextMessage | Text body of up to 3,072 characters, with optional suggestions. Unlike an SMS message, an RCS text message can include suggestions and is delivered as a single message rather than being split into segments. | [Sending RCS text messages](rcs-text-messages.md) | 
| FileMessage | A single media file (image, video, audio, or PDF) referenced by an HTTPS or Amazon S3 URL. | [Sending RCS file messages](rcs-file-messages.md) | 
| RichCard | A structured card with optional media, a title, a description, and up to 4 suggestions. | [Sending RCS rich cards](rcs-rich-cards.md) | 
| Carousel | A scrollable set of 2 to 10 cards, each with its own media, text, and suggestions. | [Sending RCS carousels](rcs-carousels.md) | 

## Suggestions
<a name="rcs-rich-messaging-suggestions"></a>

Suggestions are interactive chips that recipients choose to take an action. You can add suggestions to any content type: message-level suggestions apply to the whole message (up to 11), and card-level suggestions apply to an individual rich card or carousel card (up to 4). AWS End User Messaging supports six suggestion types, including replies, links, and actions such as dialing a phone number or sharing a location. For the full list of suggestion types, their parameters, and how to receive suggestion taps, see [Configuring RCS suggestions](rcs-suggestions.md).

## SendRcsMessage request overview
<a name="rcs-rich-messaging-api"></a>

The `SendRcsMessage` request uses the following key parameters.


**Key SendRcsMessage parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| DestinationPhoneNumber | Yes | The recipient phone number in E.164 format, for example \+12065550100. | 
| OriginationIdentity | Yes | The ID or ARN of a pool or an AWS RCS Agent to send from. The agent must be in the Active state. | 
| RcsMessageContent | No | The message content. Contains a Content object with exactly one of TextMessage, FileMessage, RichCard, or Carousel, and an optional top-level Suggestions list. | 
| FallbackConfiguration | No | The SMS or MMS message to send if RCS delivery does not succeed. Includes a required Channel (SMS or MMS), a MessageBody, optional MediaUrls for MMS, and an OriginationIdentity that is a phone number or sender ID. | 
| TimeToLive | No | The time in seconds before the message expires if it is not delivered. The minimum is 1 second and the maximum is 172,800 seconds (48 hours). A value of 10 seconds or more is recommended. | 
| MessageFeedbackEnabled | No | Set to true to enable message feedback for the message. When the recipient receives the message, update the message status by calling the PutMessageFeedback operation. | 

A successful response returns a `MessageId` that you use to correlate delivery status events.

**Note**  
Fallback for `SendRcsMessage` is configured per message through `FallbackConfiguration`. For the full fallback behavior, see [Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md).

## Message size and count limits
<a name="rcs-rich-messaging-limits"></a>


**RCS message limits**  

| Limit | Value | 
| --- | --- | 
| Text message body | 3,072 characters | 
| Rich card title | 200 characters | 
| Rich card description | 2,000 characters | 
| Media file size | 100 MB | 
| Media URL length | 2,000 characters | 
| Suggestions per message | 11 | 
| Suggestions per card | 4 | 
| Suggestion display text | 25 characters | 
| Postback data | 2,048 characters | 
| Carousel cards | 2 to 10 cards | 
| Time-to-live | 1 second to 172,800 seconds (48 hours) | 

For RCS limits and restrictions across all content types, see [Messaging limits and restrictions](sms-limitations.md).

## Delivery events and recipient actions
<a name="rcs-rich-messaging-events"></a>

AWS End User Messaging generates events that report message delivery status and recipient actions, including delivered, read, failed, expired, and postback events. A postback event is generated when a recipient chooses a suggestion and includes the `PostbackData` value. Route these events to an Amazon SNS topic, an Amazon Data Firehose delivery stream, or Amazon CloudWatch Logs. For details, see [RCS message events](rcs-events.md).

## Best practices
<a name="rcs-rich-messaging-best-practices"></a>

Design rich RCS messages as conversational, interactive experiences. Set a `TimeToLive` for time-sensitive content such as one-time passwords, configure an SMS or MMS fallback for messages that must reach the recipient even when their device does not support RCS, keep suggestion labels short (the limit is 25 characters), and include structured identifiers in `PostbackData` so your application can route responses without additional lookups. For detailed guidance, see [RCS best practices](rcs-best-practices.md).
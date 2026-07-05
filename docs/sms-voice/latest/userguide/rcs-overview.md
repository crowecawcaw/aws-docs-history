# What is RCS?

Rich Communication Services (RCS) for business is a messaging protocol that enhances
traditional SMS with verified brand identity. With AWS End User Messaging, you can send RCS text messages
to recipients in 22 supported countries, with automatic SMS fallback for devices or
carriers that don't support RCS.

RCS messages appear in the same messaging app that recipients use for SMS, but include
your verified brand name, logo, and colors. This makes RCS an in-place upgrade rather
than a new channel to adopt. Customers using the `SendTextMessage` API can
start using RCS with minimal to no code changes, and end users don't change their
messaging flow. Verified identities inspire trust, encourage conversations, enhance
existing messaging use cases, and open the door for new use cases like conversational
experiences.

###### Important

Google is part of the message delivery chain for delivering your RCS
messages. Accordingly, your use of the RCS messaging channel in AWS End User Messaging is
also subject to the
[Google
RCS for Business Terms of Service](https://developers.google.com/business-communications/rcs-business-messaging/terms-and-policies/tos "https://developers.google.com/business-communications/rcs-business-messaging/terms-and-policies/tos"), which includes information on
how Google may use your RCS message content.

###### Topics

- [Key benefits of RCS](#rcs-overview-benefits "#rcs-overview-benefits")
- [How RCS differs from SMS](#rcs-overview-how-rcs-differs "#rcs-overview-how-rcs-differs")
- [Why SMS fallback is essential](#rcs-overview-sms-fallback "#rcs-overview-sms-fallback")
- [Supported RCS capabilities](#rcs-overview-phase1-scope "#rcs-overview-phase1-scope")
- [Understanding the two-level identity model](#rcs-overview-identity-model "#rcs-overview-identity-model")

## Key benefits of RCS

RCS messaging through AWS End User Messaging provides the following benefits over traditional
SMS:

**Verified brand identity**

RCS messages display your brand logo, name, and colors alongside a
verified badge on Android devices. Recipients can confirm that the message is from your
organization, which reduces the risk of phishing and improves
engagement.

**Delivery receipts (DLRs)**

RCS provides device-level delivery receipts that confirm when a
message has been delivered to the recipient's device. Unlike SMS,
where delivery confirmation comes from the carrier network, RCS DLRs
report directly from the device, giving you stronger assurance of
actual delivery. This is also tied to billing. With RCS, you
only pay for messages that are confirmed delivered to the device,
whereas SMS charges are incurred when the message is accepted by the
carrier.

**Improved messaging performance**

Messages delivered via RCS tend to achieve better business results
compared to SMS because verified brand identity increases recipient
trust and engagement. While RCS is not yet as universally available
as SMS, the subset of messages delivered via RCS typically sees higher
open rates and conversions. For recipients whose devices or carriers
do not support RCS, automatic SMS fallback ensures your messages still
reach them.

**Automatic SMS fallback**

When you send messages through a phone pool that contains both an
AWS RCS Agent and SMS phone numbers, AWS End User Messaging automatically falls back
to SMS if RCS delivery is not possible. This ensures your messages reach
recipients regardless of their device or carrier support for RCS.

## How RCS differs from SMS

The following table compares RCS and SMS messaging capabilities in AWS End User Messaging.

RCS compared to SMS| Feature | RCS | SMS |
| --- | --- | --- |
| Brand identity | Verified brand name, logo, colors, and badge | Phone number or sender ID only |
| Delivery confirmation | Device-level delivery receipts: the recipient's device reports back directly, confirming actual delivery. You are only billed for confirmed deliveries. | Carrier-level confirmation: the carrier network acknowledges receipt, but this does not guarantee the message reached the device. You are billed when the carrier accepts the message. |
| Message content | Text messages, plus rich content (rich cards, carousels, media files, and interactive suggestions), in all countries where RCS is supported. | Text messages, MMS for media |
| Rich media and interactivity | Rich cards, carousels, image, video, audio, and PDF files, and interactive suggestions (suggested replies and actions). Available in all countries where RCS is supported, with the `SendRcsMessage` API. | MMS media only. No interactive elements. |
| Device support | Android devices with RCS enabled, iPhone with iOS 18 or later | All mobile devices |
| Supported countries | 22 countries including the United States, Canada, United Kingdom, Germany, France, Brazil, and more | Over 200 countries and regions |

## Why SMS fallback is essential

Not all mobile devices and carriers support RCS. For example, older Android devices,
some carriers, and iPhones running iOS versions earlier than 18 cannot receive RCS
messages. For most use cases, you need a reliable way to reach all recipients regardless
of their device or carrier.

Phone pools solve this problem. A pool is a container of messaging identities
that provides an abstraction layer between your API requests and your origination
identities. Instead of putting SMS fallback number selection logic in your application,
you add RCS agents and phone numbers to a pool and AWS End User Messaging handles the rest. This
gives you three advantages:

- Easy RCS-to-SMS fallback without worrying about which numbers work in
  which country. Add your identities to a pool and the service selects the
  right one automatically.
- Number and agent selection logic stays out of your application code and
  in easy-to-manage configuration. You can add or remove identities
  without changing your sending integration.
- While simple to set up, pools also allow complete control over how you
  use numbers and RCS agents together, including per-use-case pools for
  compliance-safe routing.

To use SMS fallback, create a phone pool that contains both your AWS RCS Agent and one
or more SMS phone numbers. When you send a message using the pool, AWS End User Messaging attempts
RCS delivery first and automatically falls back to SMS if needed. We recommend
pool-based sending for all messaging use cases, not just RCS, because it provides
flexibility to add or change origination identities without modifying your application
code.

###### Note

If you send a message directly to an AWS RCS Agent (without using a pool),
SMS fallback is not available. Use direct sending only when you require
RCS-or-nothing delivery or when you manage fallback logic outside of
AWS End User Messaging.

## Supported RCS capabilities

RCS in AWS End User Messaging supports both text and rich, interactive messaging in all countries
where RCS is supported. You send and receive plain text RCS messages using the same
`SendTextMessage` API that you use for SMS. To send rich content such as
rich cards, carousels, media files, and suggestions, use the
`SendRcsMessage` API. For more information, see [Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").

###### Important

RCS messaging with `SendRcsMessage`, including rich cards, carousels,
file messages, suggestions, per-message SMS or MMS fallback, and message
expiration, works in all countries where RCS is supported.

RCS in AWS End User Messaging currently supports the following:

- Sending and receiving text messages through RCS
- Sending rich content with the `SendRcsMessage` API, including rich
  cards, carousels, and file messages (image, video, audio, and PDF), in all
  countries where RCS is supported
- Interactive suggestions (suggested replies and actions) on any message
  type
- Per-message SMS or MMS fallback and message expiration (time-to-live)
- Receiving inbound RCS media, and message events such as delivery, read, and
  suggestion-tap (postback) events
- Verified brand identity (logo, name, colors, and verified badge)
- Delivery receipts (DLRs)
- Automatic SMS fallback with pool-based sending
- Two-way messaging (receiving inbound RCS text messages)
- Keyword management for auto-responses
- CloudWatch metrics for RCS message monitoring
- Country launches in 22 supported countries across North America,
  South America, Europe, and Asia Pacific
- RCS testing agents for testing without carrier approval
- Phone mockups in the console to preview how your brand appears on
  devices
- A single AWS RCS Agent resource that manages country-specific registrations across all supported countries
- Shared registration details across countries, with per-country
  customization
- All AWS End User Messaging capabilities including configuration sets, phone pools,
  opt-out lists, and keywords

###### Note

RCS testing agents are typically created and approved within minutes,
compared to SMS phone number registrations which can take days or weeks.
This allows you to start testing RCS messaging quickly.

## Understanding the two-level identity model

RCS in AWS End User Messaging uses a two-level identity model: the
**AWS RCS Agent** (a container you create and
manage) and one or more **RCS for Business IDs**
(per-country agent identities created during registration). For complete details
on how these identities relate, including lifecycle states and the comparison
table, see
[Understanding the two-level identity model](rcs-agents.md#rcs-agents-identity-model "rcs-agents.md#rcs-agents-identity-model").

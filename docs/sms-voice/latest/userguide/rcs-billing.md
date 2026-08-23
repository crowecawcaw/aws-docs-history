# RCS billing and pricing model

RCS messaging in AWS End User Messaging uses a pricing model with two cost components: an AWS
message fee and a carrier fee that is passed through with no markup. This chapter explains
the pricing structure for RCS messaging. For current rates, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

AWS End User Messaging charges for RCS messages only when they are successfully delivered to the
recipient's device. You are not charged for delivery attempts that fail. If an RCS
message fails and falls back to SMS, you are charged for the SMS message that is
delivered, not for the failed RCS attempt.

###### Topics

- [Billing overview](#rcs-billing-overview "#rcs-billing-overview")
- [United States pricing model](#rcs-billing-us-pricing "#rcs-billing-us-pricing")
- [Pricing for countries outside the United States](#rcs-billing-row-pricing "#rcs-billing-row-pricing")
- [Conversational pricing](#rcs-billing-conversational "#rcs-billing-conversational")
- [Registration fees](#rcs-billing-registration-fees "#rcs-billing-registration-fees")
- [RCS message spending limits](#rcs-billing-spend-limits "#rcs-billing-spend-limits")
- [Double-delivery billing](#rcs-billing-double-delivery "#rcs-billing-double-delivery")
- [Content violation fees](#rcs-billing-content-violations "#rcs-billing-content-violations")
- [Bill transparency](#rcs-billing-transparency "#rcs-billing-transparency")

## Billing overview

RCS billing in AWS End User Messaging has the following components:

- **Message fees** — Per-message charges
  for outbound and inbound RCS messages, based on message segments.
- **Carrier fees** — Pass-through charges
  from carriers with no AWS markup.
- **Registration fees** — One-time and
  recurring fees for agent setup, brand vetting, and maintenance.

Each component appears as a separate line item on your AWS bill, giving you
visibility into your RCS messaging costs.

## United States pricing model

RCS messaging in the United States uses a message type called
**Rich RCS**. Rich RCS messages are metered per
160-character segment, similar to SMS. Messages exceeding 160 characters are
charged for multiple segments.

Each outbound or inbound Rich RCS message has two cost components:

**Message transport fee**

The per-segment fee charged by AWS for processing and delivering the
RCS message.

**Carrier fee (pass-through)**

The per-segment fee charged by the carrier for RCS message delivery.
AWS passes this fee through to you with no markup. Carrier fees are
separate from message transport costs.

The total cost per message is the message transport fee plus the carrier fee.
Inbound RCS messages (messages sent from end users to your AWS RCS Agent) follow
the same two-component pricing structure.

###### Note

RCS messages are charged only for delivered messages. This differs from SMS,
which charges for requested messages.

For current per-segment rates, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Pricing for countries outside the United States

For all countries outside the United States (including Canada), RCS messaging
uses two message types:

**RCS Basic**

Messages up to 160 characters. Charged per message.

**RCS Single**

Messages exceeding 160 characters. Billed as a single message, not
as multiple segments. This differs from the United States, where Rich
RCS messages exceeding 160 characters are metered per 160-character
segment similar to SMS.

Each outbound or inbound RCS message in these countries has two cost components:
a message transport fee and a carrier pass-through fee.

###### Note

RCS messages are charged only for delivered messages. This differs from SMS,
which charges for requested messages.

For current rates, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Conversational pricing

For supported countries outside the United States, you can register an RCS agent to
use **conversational pricing**. With conversational
pricing, AWS End User Messaging charges a single session fee for all messages exchanged with a recipient
during a 24-hour conversation session, instead of charging for each message
individually. Conversational pricing is not available in the United States.

You choose the billing model when you register your RCS agent. Set the agent's billing
category to conversational or non-conversational in the console, or set the
`billingCategory` parameter to `CONVERSATIONAL` or
`NON_CONVERSATIONAL` when you register the agent with the API. This setting
applies to all traffic from that agent.

**Conversation session**

A fixed 24-hour window that begins when a conversation starts between your
agent and a recipient. A single session fee covers all outbound and inbound
messages exchanged during the window. The window does not extend when you
send more messages. After it expires, the next interaction starts a new
session.

**How a conversation starts**

A conversation starts in one of two ways. When your agent sends the first
message and the recipient replies within 24 hours, the conversation is
business-initiated. When the recipient sends the first message and your
agent responds, the conversation is user-initiated.

At send time, AWS End User Messaging cannot determine whether a message will become part of a
conversation, so billing for messages from a conversational agent works as
follows:

- If a conversation starts within 24 hours of the message, the session fee
  covers the message and AWS End User Messaging does not charge for it individually.
- If no conversation starts within 24 hours, AWS End User Messaging charges for the message
  individually after the 24-hour period ends.
- After a conversation session ends, this per-message behavior resumes until a
  new conversation starts.

When a message is part of an active conversation session, its delivery event reports
a `totalMessagePrice` and `totalCarrierFee` of `0.0`
and includes a `conversationSessionFee` field with the one-time session fee.
AWS End User Messaging also sends a `CONVERSATION_STARTED` event when a session begins. For
details on these events and fields, see [RCS message events](rcs-events.md "rcs-events.md").

Conversational pricing is available in a specific set of countries outside the United
States. For the list of supported countries and current session fees, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Registration fees

Launching an AWS RCS Agent requires registration with the RCS infrastructure
provider. The following carrier pass-through fees apply to the registration
process:

**One-time agent setup fee**

A one-time fee charged when you create and register your AWS RCS Agent.
This covers the initial setup and verification of your agent with the
RCS infrastructure provider.

**Annual brand vetting fee**

An annual fee for verifying your brand identity. Brand vetting confirms
that your organization is legitimate and authorized to send RCS messages
under your brand name.

**Monthly agent maintenance fee**

A recurring monthly fee for maintaining your active AWS RCS Agent
registration with the RCS infrastructure provider.

These registration fees are carrier pass-through charges. For current registration
fee amounts, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

###### Important

RCS registration fees are excluded from Enterprise Discount Program (EDP)
discounts. These fees are pass-through charges from the RCS infrastructure
provider and are not eligible for AWS volume discounts.

Registration fees appear as separate line items on your AWS bill. For
details on how charges are categorized, review your AWS Cost and Usage
Report.

## RCS message spending limits

AWS End User Messaging applies a monthly spending limit to RCS messaging, separate from your SMS,
MMS, and voice spending limits. This limit caps the amount, in US dollars, that you
can spend sending RCS messages each month.

**Maximum limit**

The maximum monthly RCS spend that AWS allows for your account. To
raise it, request a spending limit increase. For more information, see
[Requesting an RCS spending limit increase](#rcs-billing-spend-limit-increase "#rcs-billing-spend-limit-increase").

**Spend limit override**

An optional limit that you set at or below the maximum limit to control
your own RCS spending. Use the `SetRcsMessageSpendLimitOverride`
operation to set the monthly override, and
`DeleteRcsMessageSpendLimitOverride` to remove it. Removing the
override resets your enforced limit to the maximum limit. When you reach
the enforced limit, AWS End User Messaging stops sending RCS messages until you raise the
override or the next month begins.

You can adjust the override up or down at any time without contacting Support, as
long as it stays at or below your maximum limit. To set billing alarms for your
spending, see [Monitoring SMS, MMS, and voice spending activity with AWS End User Messaging SMS](monitor-spending.md "monitor-spending.md").

### Requesting an RCS spending limit increase

To raise your maximum monthly RCS spending limit, request a spending limit
increase as described in [Quotas for AWS End User Messaging SMS](quotas.md "quotas.md").
Requests above the amount that can be approved automatically are routed to
AWS Support for review.

## Double-delivery billing

When AWS End User Messaging sends an RCS message with SMS fallback enabled (through pool-based
or account-level sending), the service attempts RCS delivery first. If RCS delivery
fails, the service falls back to SMS.

Under normal circumstances, the RCS message is revoked before the SMS fallback
message is delivered. In this case, you are charged only for the SMS message that
was successfully delivered.

In rare cases, both the RCS message and the SMS fallback message may be delivered
to the recipient. This can happen if the RCS message is delivered after the revocation
window but before the SMS message arrives. When dual delivery occurs, you are charged
for both the RCS message and the SMS message.

###### Note

Dual delivery is uncommon. AWS End User Messaging is designed to revoke the RCS message
before initiating SMS fallback. Monitor your delivery receipts and CloudWatch
metrics to track delivery channel attribution. For more information about RCS
metrics, see
[RCS CloudWatch metrics and monitoring](rcs-monitoring.md "rcs-monitoring.md").

## Content violation fees

It is the responsibility of any RCS message sender to comply with country laws
and regulations for messaging, as well as carrier policies. Carriers may impose
penalty fees for RCS messages that violate their message content
policies. These penalties are carrier-imposed charges that AWS may pass through
to customers that send RCS messages that carriers flag as violating their message
content policies.

Carriers typically categorize content violations into the following tiers:

**Tier 1 — Phishing, smishing, and social
engineering**

Social engineering refers to the practice of targeting individuals
in a way that manipulates them to reveal private information such as
credit card numbers or social security numbers.

**Tier 2 — Illegal content**

Content must be legal in all 50 states and federally. Illegal content
includes, but is not limited to, cannabis, marijuana, CBD, illegal
prescriptions, and solicitation.

**Tier 3 — Other violations**

All other commercial messaging violations that breach federal, state,
or local laws, regulations, or carrier codes of conduct on prohibited
content.

For more information about content violation fee amounts, see
[AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Bill transparency

RCS charges appear as separate line items on your AWS bill, allowing you to
distinguish between the following cost categories:

- RCS message fees (AWS charges)
- RCS carrier fees (pass-through charges)
- RCS registration fees (pass-through charges)
- SMS message fees (for messages that fell back from RCS to SMS)

This separation helps you understand your messaging costs and identify
opportunities to optimize your spending. For detailed billing information, review
your AWS Cost and Usage Report.

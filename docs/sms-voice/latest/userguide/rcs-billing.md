# RCS billing and pricing model

RCS messaging in AWS End User Messaging uses a pricing model with two cost components: an AWS
message fee and a carrier fee that is passed through with no markup. This chapter explains
the pricing structure for RCS messaging. For current rates, see
[AWS End User Messaging
Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/").

AWS End User Messaging charges for RCS messages only when they are successfully delivered to the
recipient's device. You are not charged for delivery attempts that fail. If an RCS
message fails and falls back to SMS, you are charged for the SMS message that is
delivered, not for the failed RCS attempt.

###### Topics

- [Billing overview](#rcs-billing-overview "#rcs-billing-overview")
- [United States pricing model](#rcs-billing-us-pricing "#rcs-billing-us-pricing")
- [Canada pricing model](#rcs-billing-ca-pricing "#rcs-billing-ca-pricing")
- [Registration fees](#rcs-billing-registration-fees "#rcs-billing-registration-fees")
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
Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/").

## Canada pricing model

RCS messaging in Canada uses two message types:

**RCS Basic**

Messages up to 160 characters. Charged per message.

**RCS Single**

Messages exceeding 160 characters. Billed as a single message, not
as multiple segments. This differs from the United States, where Rich
RCS messages exceeding 160 characters are metered per 160-character
segment similar to SMS.

Each outbound or inbound RCS message in Canada has two cost components: a
message transport fee and a carrier pass-through fee.

###### Note

RCS messages are charged only for delivered messages. This differs from SMS,
which charges for requested messages.

For current rates, see
[AWS End User Messaging
Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/").

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
Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/").

###### Important

RCS registration fees are excluded from Enterprise Discount Program (EDP)
discounts. These fees are pass-through charges from the RCS infrastructure
provider and are not eligible for AWS volume discounts.

Registration fees appear as separate line items on your AWS bill. For
details on how charges are categorized, review your AWS Cost and Usage
Report.

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
Pricing](https://aws.amazon.com//end-user-messaging/pricing/ "https://aws.amazon.com//end-user-messaging/pricing/").

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



# RCS to SMS fallback using phone pools
<a name="rcs-sms-fallback"></a>

A phone pool is a container of messaging identities, such as AWS RCS Agents and SMS phone numbers, that provides an abstraction layer between your API requests and the underlying origination identities. Pools simplify configuration changes, number type migration, and RCS-to-SMS fallback. You send a single API call to the pool, and AWS End User Messaging handles channel selection for you.

This chapter explains how RCS delivery can fail, what makes SMS fallback possible, the fallback logic and priority order, and billing implications. It also covers pool-per-use-case best practices and how to add and remove AWS RCS Agents from pools. For general information about phone pools, see [Phone pools in AWS End User Messaging SMS](phone-pool.md). For information about managing AWS RCS Agents, see [Managing RCS agents](rcs-agents.md).

**Topics**
+ [How RCS delivery can fail](#rcs-sms-fallback-how-rcs-fails)
+ [What makes SMS fallback possible](#rcs-sms-fallback-what-makes-possible)
+ [Why use pools](#rcs-sms-fallback-why-pools)
+ [Pool-per-use-case model](#rcs-sms-fallback-pool-per-use-case)
+ [Compliance risk with account-level sending](#rcs-sms-fallback-compliance-risk)
+ [Fallback logic and priority order](#rcs-sms-fallback-logic)
+ [Billing implications of SMS fallback](#rcs-sms-fallback-billing)
+ [Testing SMS fallback](#rcs-sms-fallback-testing)
+ [Managing AWS RCS Agents in pools](#rcs-sms-fallback-pool-management)

## How RCS delivery can fail
<a name="rcs-sms-fallback-how-rcs-fails"></a>

RCS delivery can fail for several reasons. Understanding these failure modes helps you plan your fallback strategy:
+ **Carrier does not support RCS** — The recipient's mobile carrier has not enabled RCS messaging on their network.
+ **Device does not support RCS** — The recipient's device does not have RCS capability (for example, an older Android device or an iPhone running iOS earlier than 18).
+ **Agent not active on carrier** — Your AWS RCS Agent has not yet been approved by the recipient's carrier, or the agent is in PARTIAL status for that country.
+ **Device temporarily unreachable** — The recipient's device supports RCS but is temporarily offline or has no data connection. RCS messages require a data connection for delivery.

When any of these conditions occur and you are using pool-based or account-level sending, AWS End User Messaging automatically falls back to SMS delivery using a phone number from the same pool or account.

## What makes SMS fallback possible
<a name="rcs-sms-fallback-what-makes-possible"></a>

SMS fallback requires both an AWS RCS Agent and at least one SMS phone number in the same pool. When you send a message to the pool, AWS End User Messaging attempts RCS delivery first. If RCS delivery fails, the service retries the message via SMS using a phone number from the same pool. A pool with only an AWS RCS Agent (and no phone numbers) does not support SMS fallback. If RCS fails, the message is not delivered.

**Important**  
For SMS fallback to work, your pool must contain both an AWS RCS Agent and one or more SMS phone numbers. A pool with only a single identity type does not provide cross-channel fallback.

## Why use pools
<a name="rcs-sms-fallback-why-pools"></a>

We recommend using a phone pool for all messaging use cases, not just RCS. Pools provide the following advantages:
+ **Automatic SMS fallback** — When a pool contains both an AWS RCS Agent and SMS phone numbers, AWS End User Messaging attempts RCS delivery first. If RCS delivery fails (for example, the recipient's device or carrier does not support RCS), the service automatically retries the message via SMS using a phone number from the same pool. You do not need to implement fallback logic in your application.
+ **Intelligent routing** — The service selects the best origination identity from the pool based on the destination, channel availability, and sticky sending history. This routing happens transparently with each `SendTextMessage` call.
+ **Single API call** — You specify the pool ID as the origination identity in your `SendTextMessage` request. The service determines whether to deliver via RCS or SMS without any additional logic on your side.
+ **Flexibility for future changes** — You can add or remove phone numbers and AWS RCS Agents from a pool at any time without changing your application code. For example, you can add a toll-free number for SMS fallback or swap out a 10DLC number without modifying your sending integration.
+ **No cost or downside** — Creating a pool and adding origination identities to it does not incur additional charges. Even with a single phone number or a single AWS RCS Agent, using a pool gives you the flexibility to add more identities later without application changes.

**Note**  
We recommend always using a pool for messaging. There is no cost or downside to using a pool, even with a single origination identity. For RCS-to-SMS fallback, the pool must contain both an AWS RCS Agent and at least one SMS phone number. Starting with a pool from the beginning means you can add SMS fallback numbers or additional AWS RCS Agents later without modifying your sending code.

## Pool-per-use-case model
<a name="rcs-sms-fallback-pool-per-use-case"></a>

We recommend creating one pool per use case. Each pool should contain all of the phone numbers and the AWS RCS Agent that serve a single messaging purpose. For example:
+ A **transactional pool** for OTP codes and account notifications, containing your AWS RCS Agent and a 10DLC number registered for transactional messaging.
+ A **marketing pool** for promotional messages, containing the same AWS RCS Agent (or a different one) and a toll-free number registered for marketing.
+ An **appointment reminders pool** for scheduling notifications, containing your AWS RCS Agent and a dedicated phone number for appointment-related messages.

This model ensures that when RCS delivery fails and the service falls back to SMS, the fallback message is sent from a phone number that is registered and approved for the same use case. This keeps your messaging compliant with carrier requirements and registration terms.

## Compliance risk with account-level sending
<a name="rcs-sms-fallback-compliance-risk"></a>

When you send messages at the account level (without specifying a pool or origination identity), AWS End User Messaging selects an origination identity from all available identities in your account. If your account has multiple phone numbers registered for different use cases, the service may select a phone number that does not match the content of your message.

**Important**  
Account-level sending with mixed use cases creates a compliance risk. For example, if your account has a 10DLC number registered for OTP messages and a toll-free number registered for appointment reminders, an OTP message that falls back to SMS could be sent from the appointment reminders toll-free number. This violates the registration terms for that number and can result in carrier filtering or number suspension.

To avoid this risk, use pool-based sending with one pool per use case. When you specify a pool ID in your `SendTextMessage` request, the service only selects origination identities from that pool. Because all identities in the pool are registered for the same use case, the fallback message is always sent from an appropriate number.


**Sending approach compliance comparison**  

| Sending approach | SMS fallback behavior | Compliance risk | 
| --- | --- | --- | 
| Pool-based (recommended) | Falls back to a phone number in the same pool, registered for the same use case | Low — fallback number matches the message use case | 
| Account-level | Falls back to any available phone number in the account | High — fallback number may not match the message use case if multiple use cases share the account | 
| Direct (AWS RCS Agent ARN) | No SMS fallback | None — message is delivered via RCS only or not at all | 

## Fallback logic and priority order
<a name="rcs-sms-fallback-logic"></a>

When AWS End User Messaging selects an origination identity for a message (either from a pool or from all account identities), it evaluates identities in the following priority order:

1. **Sticky identity** — If a sticky sending pairing exists for the destination phone number and the identity is still available, the service uses that identity.

1. **AWS RCS Agent** — If no sticky pairing exists, the service attempts RCS delivery through an available AWS RCS Agent.

1. **SMS Short Code** — If RCS is not available, the service selects an SMS short code.

1. **SMS 10DLC** — If no short code is available, the service selects a 10DLC number.

1. **SMS Toll-Free Number** — If no 10DLC number is available, the service selects a toll-free number.

1. **SMS Sender ID** — If no other identity is available, the service selects a sender ID.

This priority order applies within the scope of the sending pattern you use. For pool-based sending, the service only considers identities in the specified pool. For account-level sending, the service considers all identities in your account.

### Automatic SMS fallback
<a name="rcs-sms-fallback-automatic"></a>

When you send a message through a pool or at the account level, AWS End User Messaging automatically falls back to SMS if RCS delivery is not possible. Fallback is asynchronous:

If AWS End User Messaging successfully submits the RCS message but does not receive a delivery confirmation or failure signal within 25 seconds, the service falls back to SMS. This handles cases where the RCS infrastructure accepts the message but delivery stalls (for example, the recipient's device is temporarily unreachable, the carrier does not support RCS, or the device is not RCS-capable).

**Note**  
Direct sending (specifying an AWS RCS Agent ARN as the origination identity) does not support automatic SMS fallback. If you need SMS fallback, use pool-based sending.

### Sticky sending
<a name="rcs-sms-fallback-sticky"></a>

Sticky sending is a routing optimization that improves delivery consistency. When AWS End User Messaging successfully delivers a message to a destination phone number using a specific origination identity, the service remembers that pairing for 25 hours. Subsequent messages to the same destination within the 25-hour window are routed through the same origination identity, provided it is still available in the pool or account.

Sticky sending applies to both RCS and SMS delivery. For example, if a message is delivered via RCS through your AWS RCS Agent, the next message to the same destination within 25 hours is also attempted via RCS through the same agent. If the previous message was delivered via SMS (after RCS fallback), the next message is attempted via SMS through the same phone number.

The service periodically retries RCS delivery even when the sticky identity is an SMS phone number. This ensures that recipients whose devices gain RCS support (for example, after a carrier rollout or device upgrade) begin receiving RCS messages without manual intervention.

Key characteristics of sticky sending:
+ **25-hour TTL** — The sticky pairing expires 25 hours after the last successful delivery. After expiration, the service re-evaluates the origination identity priority order for the next message.
+ **Automatic RCS retry** — Even when the sticky identity is an SMS phone number, the service periodically attempts RCS delivery to check whether the recipient now supports RCS.
+ **No manual flushing** — You cannot manually flush or reset sticky sending pairings. The pairing expires automatically after the 25-hour TTL.

### Delivery receipts during fallback
<a name="rcs-sms-fallback-delivery-receipts"></a>

When SMS fallback occurs, AWS End User Messaging generates a single delivery receipt for the final channel that delivered the message. If the message is delivered via SMS after RCS fallback, the delivery receipt indicates SMS as the delivery channel. You can determine the delivery channel by inspecting the `originationPhoneNumber` field in the event. If the value is an RCS agent ID, the message was delivered via RCS. If the value is an E.164 phone number or short code, the message was delivered via SMS. For more information about event fields, see [Example AWS End User Messaging SMS event data](configuration-sets-event-format.md).

Under normal circumstances, AWS End User Messaging revokes the RCS message before the SMS fallback message is delivered. This prevents the recipient from receiving the same message twice. However, in rare cases, both the RCS message and the SMS fallback message may be delivered. This can happen if the RCS message is delivered after the 25-second timeout but before the revocation completes. In these rare dual-delivery scenarios, you may receive delivery receipts for both channels.

For information about how dual delivery affects billing, see [RCS billing and pricing model](rcs-billing.md).

## Billing implications of SMS fallback
<a name="rcs-sms-fallback-billing"></a>

When a message falls back from RCS to SMS, you are charged for the SMS delivery, not the failed RCS attempt. RCS messages are billed only when successfully delivered to the recipient's device. If RCS delivery fails and the message falls back to SMS, you pay the SMS rate for that message.

In rare dual-delivery scenarios (where both the RCS message and the SMS fallback message are delivered), you may be charged for both deliveries. For complete billing details, see [RCS billing and pricing model](rcs-billing.md).

## Testing SMS fallback
<a name="rcs-sms-fallback-testing"></a>

You can test SMS fallback behavior to verify that your messages are delivered via SMS when RCS delivery is not possible. There are two approaches to testing SMS fallback, depending on whether you have an approved SMS phone number.

### Testing without an approved SMS number
<a name="rcs-sms-fallback-testing-without-sms"></a>

You can verify that AWS End User Messaging correctly triggers the fallback mechanism without an approved SMS phone number. Even without an approved number, you can see the retry and failure events via SMS, which confirms that fallback is working.

**To test SMS fallback without an approved SMS number**

1. Take your test device offline by disabling mobile data and Wi-Fi, or enable airplane mode.

1. Send an RCS message to the test device using the `SendTextMessage` API with your AWS RCS Agent ARN as the origination identity.

1. Check the message event in CloudWatch or your event destination. You should see a failed delivery event indicating that RCS delivery was not possible and that the service attempted SMS fallback.

Because there is no SMS phone number available for fallback, the SMS delivery also fails. However, the event confirms that AWS End User Messaging correctly triggered the fallback mechanism.

### Testing with an approved SMS number
<a name="rcs-sms-fallback-testing-with-sms"></a>

For a complete end-to-end SMS fallback test, add an approved SMS phone number and your AWS RCS Agent to the same phone pool. This allows you to verify that messages are delivered via SMS when RCS is not available.

**To test SMS fallback with an approved SMS number**

1. Create a phone pool that contains both your AWS RCS Agent and an approved SMS phone number (such as a 10DLC, toll-free, or short code number).

1. Take your test device offline by disabling mobile data and Wi-Fi, or enable airplane mode.

1. Send a message using the `SendTextMessage` API with the pool ID as the origination identity.

1. Verify that the message is delivered via SMS to your test device.

1. Check the delivery event to confirm that the message was delivered through the SMS channel after RCS fallback.

## Managing AWS RCS Agents in pools
<a name="rcs-sms-fallback-pool-management"></a>

For step-by-step instructions on creating pools with AWS RCS Agents, adding agents to existing pools, understanding pool configuration requirements, and removing agents from pools, see [Managing AWS RCS Agents in pools](phone-pool-rcs-agents.md).
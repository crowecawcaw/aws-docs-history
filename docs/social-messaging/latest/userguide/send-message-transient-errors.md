

# Handling transient eligibility errors (WhatsApp error code 131042)
<a name="send-message-transient-errors"></a>

When sending messages through WhatsApp, you might receive error code `131042` with the message `Business eligibility payment issue` (also reported as `Eligibility read failed due to a transient error on Meta side`). This error originates from Meta's systems and indicates a temporary failure when Meta checks the sender's payment eligibility for the WhatsApp Business Account (WABA).

## Retry strategy
<a name="send-message-transient-errors-retry"></a>

Because this error is transient, it often resolves on its own. Implement an exponential backoff retry strategy for messages that fail with error code `131042`:

1. Wait 1 second, then retry the message.

1. If the retry fails, wait 2 seconds and retry again.

1. Continue doubling the wait time (4 seconds, 8 seconds, and so on) up to a maximum of 5 retries.

In most cases, the message sends successfully after one or two retries.

## Persistent errors
<a name="send-message-transient-errors-persistent"></a>

If error code `131042` persists after multiple retries across several hours, the cause might not be transient. A persistent `131042` error can indicate that credit line sharing has been revoked for the WABA. Credit line sharing is a Meta feature. It allows the WABA to send messages without a pre-funded balance. If credit line sharing is revoked, all outbound messages fail with this error until the issue is resolved.

To diagnose a persistent error:

1. Confirm that the error occurs consistently across multiple recipients, not just a single phone number.

1. Check the [Meta Business Suite](https://business.facebook.com/) for any alerts or notifications related to billing or credit line sharing for your WABA.

1. Verify that your Meta Business Account is in good standing and that there are no outstanding billing issues.

1. Verify that credit line sharing is still active for your WABA.

## When to contact support
<a name="send-message-transient-errors-support"></a>

Contact AWS Support if the error persists after you have retried with exponential backoff, confirmed the error across multiple recipients, and verified your Meta Business Account billing status. When you open a support case, include the following information:
+ Your WABA ID
+ The phone number ID associated with the failing messages
+ Timestamps (in UTC) of example failed message attempts
+ The scope of the error (all recipients or specific phone numbers)
+ Any error details returned in the WhatsApp message status events
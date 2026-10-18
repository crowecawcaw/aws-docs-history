

# Best practices
<a name="nx-rcs-scale-bestpractices"></a>

RCS lets you send richer, more interactive messages than SMS, and the practices that make an RCS program successful are different as a result. Design your messages as conversations, reach every recipient with SMS fallback, keep your media efficient, and test before you launch. The following practices help you get the most from the channel.

**Topics**
+ [Design messages as conversations](#nx-rcs-scale-bp-conversational)
+ [Plan SMS fallback for every send](#nx-rcs-scale-bp-fallback)
+ [Optimize media and respect content limits](#nx-rcs-scale-bp-media)
+ [Test before you launch](#nx-rcs-scale-bp-test)
+ [Track RCS versus SMS delivery rates](#nx-rcs-scale-bp-delivery-rates)

## Design messages as conversations
<a name="nx-rcs-scale-bp-conversational"></a>

Design RCS messages as conversations, not one-way notifications. Open with enough context that the recipient knows who you are and why you are messaging, and offer suggested replies and actions so the recipient can respond with a tap rather than typing. Keep each message concise, give every interactive path a clear next step so the recipient never reaches a dead end, and address the recipient directly. Use rich cards and carousels for structured content, such as a set of products or appointment options, rather than forcing that content into plain text.

## Plan SMS fallback for every send
<a name="nx-rcs-scale-bp-fallback"></a>

Not every recipient can receive RCS, because their device or carrier may not support it. Plan SMS fallback so that every recipient is reached even when RCS delivery is not possible. Send through a phone pool that contains both your AWS RCS Agent and an SMS number, or set a fallback configuration on the send, so that a message that cannot be delivered over RCS is delivered as SMS instead. Write your content so that it still makes sense if it arrives as plain SMS. For how fallback works and how to configure it, see [Resiliency](nx-rcs-scale-fallback.md).

## Optimize media and respect content limits
<a name="nx-rcs-scale-bp-media"></a>

Rich cards, carousels, and media files make your messages more engaging, but large media slows delivery and rendering on the recipient's device. Optimize images and other media for mobile before you send, and keep card titles and descriptions within the content limits so your message renders as intended. For the full set of content limits, see [Limits and quotas](nx-rcs-scale-limits.md).

## Test before you launch
<a name="nx-rcs-scale-bp-test"></a>

Validate your integration with a testing agent and a test device before you launch in a country. Testing lets you confirm that your rich content renders correctly, that your suggested actions behave as expected, and that your SMS fallback works, before you send to real recipients. For how to set up testing and move to production, see [Move out of the sandbox](nx-rcs-scale-sandbox.md).

## Track RCS versus SMS delivery rates
<a name="nx-rcs-scale-bp-delivery-rates"></a>

Compare `RCS.MessagesDelivered` against `RCS.MessagesFallenBackToSMS` to understand what percentage of your messages are delivered via RCS versus SMS. A high fallback rate may indicate that many of your recipients are on carriers or devices that don't support RCS. Use the following formulas to calculate key rates:

```
RCS delivery rate = 100 * SUM(RCS.MessagesDelivered) / SUM(RCS.MessagesSent)

SMS fallback rate = 100 * SUM(RCS.MessagesFallenBackToSMS) / SUM(RCS.MessagesSent)
```

Track these rates over time to identify trends as carrier and device support for RCS expands. A decreasing fallback rate indicates that more of your recipients are receiving messages via RCS.
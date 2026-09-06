# Testing RCS messages

Before you launch RCS messaging in production, you can test your integration using
a testing agent. The testing agent is an RCS for Business ID that is created
when you submit a testing registration for your AWS RCS Agent. It provides full API
access identical to production, but restricts message delivery to registered test
devices only. No carrier approval is needed for testing.

This chapter focuses on the testing agent itself, including how to manage
test devices and how to troubleshoot common issues. For a step-by-step walkthrough
of creating your first AWS RCS Agent and sending a test message, see
[Getting started with RCS](rcs-getting-started.md "rcs-getting-started.md"). For
details on creating an AWS RCS Agent and submitting a testing registration, see
[Managing RCS agents](rcs-agents.md "rcs-agents.md").

###### Important

Testing messages are charged at standard RCS rates. The testing agent provides
a testing environment for validating your integration, but message delivery to
test devices incurs the same charges as production messages.

###### Topics

- [What is a testing agent?](#rcs-testing-what-is "#rcs-testing-what-is")
- [Adding test devices](#rcs-testing-add-devices "#rcs-testing-add-devices")
- [Tester invitation flow](#rcs-testing-tester-invitation "#rcs-testing-tester-invitation")
- [Viewing test devices](#rcs-testing-view-devices "#rcs-testing-view-devices")
- [Sending test messages](#rcs-testing-send-messages "#rcs-testing-send-messages")
- [Testing SMS fallback](#rcs-testing-sms-fallback "#rcs-testing-sms-fallback")
- [Troubleshooting RCS testing](#rcs-testing-troubleshooting "#rcs-testing-troubleshooting")

## What is a testing agent?

A testing agent is an RCS for Business ID that AWS End User Messaging creates when
you submit a testing registration for your AWS RCS Agent. The testing agent
allows you to:

- Send RCS messages to registered test devices without carrier
  approval
- Use the `SendTextMessage` API to send test messages,
  the same API you use in production
- Configure pools, configuration sets, opt-out lists, keywords, and
  other AWS End User Messaging capabilities for your testing workflow
- Test two-way messaging by sending messages with auto-response
  keywords
- Test SMS fallback behavior with or without an approved SMS phone
  number

Test devices that you register for a testing agent work across all
countries for that AWS RCS Agent. You do not need to register test devices
separately for each country. Conversely, the testing agent can send messages
to test devices in any country, regardless of whether you have submitted a
country launch registration for that country.

## Adding test devices

Before you can send test RCS messages, you must register one or more test
devices as verified destination numbers. You can add test devices using the
AWS End User Messaging console or the `CreateVerifiedDestinationNumber` API.

Console
In the console, test devices are managed on the
**RBM tester management** sub-tab
within the **Testing** tab of your
AWS RCS Agent. For step-by-step console instructions, see
[Step 2: Add a test device](rcs-getting-started.md#rcs-getting-started-add-test-device "rcs-getting-started.md#rcs-getting-started-add-test-device").

AWS CLI
Use the `create-verified-destination-number` command
with the `--rcs-agent-id` parameter to register a test
device for your AWS RCS Agent:

```
aws pinpoint-sms-voice-v2 create-verified-destination-number \
    --destination-phone-number +12065550100 \
    --rcs-agent-id rcs-a1b2c3d4
```

###### Note

The `--origination-identity` parameter is not
required. When you specify `--rcs-agent-id`, the
command registers the phone number for RCS testing with that
agent. When you omit `--rcs-agent-id` and use
`--origination-identity` instead, the command
sends an OTP SMS for SMS verification. The two parameters
are mutually exclusive.

## Tester invitation flow

After you add a test device, AWS End User Messaging sends a tester invitation from an RCS
agent called RBM Tester Management. The invitation contains buttons to accept
or decline. For details on the tester invitation flow, including the 120-second
wait requirement and iOS-specific behavior, see
[Step 2: Add a test device](rcs-getting-started.md#rcs-getting-started-add-test-device "rcs-getting-started.md#rcs-getting-started-add-test-device").

## Viewing test devices

You can view the test devices registered for your AWS RCS Agent using the
AWS End User Messaging console or the `DescribeVerifiedDestinationNumbers`
API.

Console
To view your registered test devices in the console, navigate to the
details page for your AWS RCS Agent and choose the
**Testing** tab. Choose the
**RBM tester management** sub-tab to
see all verified destination numbers associated with the agent,
including their verification status and phone number.

AWS CLI
Use the `describe-verified-destination-numbers` command
to list test devices for your AWS RCS Agent. Use the
`--filters` parameter with `rcs-agent-id` to
show only RCS test devices:

```
aws pinpoint-sms-voice-v2 describe-verified-destination-numbers \
    --filters Name=rcs-agent-id,Values=rcs-a1b2c3d4
```

Test devices that you register for a testing agent work globally for
that AWS RCS Agent. A test device registered in one AWS Region can
receive test messages sent from any AWS Region where your AWS RCS Agent is
available.

## Sending test messages

After a test device has accepted the tester invitation, you can send RCS
messages to it. You can send test messages using the AWS End User Messaging console or the
`SendTextMessage` API.

Console

###### To send a test message using the console

1. Open the AWS End User Messaging console.
2. In the navigation pane, under
   **Configurations**, choose
   **RCS agents**.
3. Choose the AWS RCS Agent that you want to test.
4. Choose the **Testing** tab.
5. In the **Send test message** section,
   choose a verified test device from the list.
6. Enter your message text.
7. Choose **Send test message**.

AWS CLI
Use the `send-text-message` command to send a test
message to a verified destination number. Specify the AWS RCS Agent
ARN as the origination identity:

```
aws pinpoint-sms-voice-v2 send-text-message \
    --destination-phone-number +12065550100 \
    --origination-identity arn:aws:sms-voice:us-east-1:123456789012:rcs-agent/rcs-a1b2c3d4 \
    --message-body "Hello from RCS testing!"
```

## Testing SMS fallback

You can test SMS fallback behavior to verify that your messages are delivered
via SMS when RCS delivery is not possible. For complete instructions on testing
SMS fallback, including testing without an approved SMS number and the full
end-to-end flow, see
[Testing SMS fallback](rcs-sms-fallback.md#rcs-sms-fallback-testing "rcs-sms-fallback.md#rcs-sms-fallback-testing").

## Troubleshooting RCS testing

The following sections describe common issues that you might encounter when
testing RCS messages and how to resolve them.

### Test device is not receiving RCS messages

If your test device is not receiving RCS messages, check the
following:

- Verify that the test device has accepted the tester invitation.
  Use the `DescribeVerifiedDestinationNumbers` API with
  the `rcs-agent-id` filter to check the verification
  status of the device.
- Verify that the test device has RCS enabled. On Android, check
  the messaging app settings for RCS or Chat features. On iPhone,
  RCS requires iOS 18 or later.
- Verify that the test device has an active data connection. RCS
  messages are delivered over data, not the SMS channel.
- Verify that you are sending to the correct phone number in E.164
  format.

### Message delivered as SMS instead of RCS

If your test message is delivered as SMS instead of RCS, check the
following:

- Verify that you are sending the message using the AWS RCS Agent
  ARN or a pool that contains the AWS RCS Agent as the origination
  identity. If you specify only an SMS phone number, the message is
  sent via SMS.
- Verify that the test device has accepted the tester invitation
  and is registered as a verified destination number for the correct
  AWS RCS Agent.
- Check the delivery event to determine whether the message was
  initially attempted via RCS and fell back to SMS, or whether it
  was sent directly via SMS.

### Tester invitation not received

If a test device does not receive the tester invitation, check the
following:

- The tester invitation can take up to 20 minutes to arrive
  after adding a test device. If the invitation has not arrived
  after 20 minutes, remove the test device and add it again.
- Verify that the phone number is in the correct E.164 format and
  is a valid mobile number.
- Verify that the test device has an active data connection and
  RCS is enabled.

### iOS: Tester invitation in Unknown Senders

On iOS devices (iPhone with iOS 18 or later), the tester invitation from
RBM Tester Management may be filtered into the
**Unknown Senders** folder in the Messages
app. This is a default iOS behavior for messages from unknown
contacts.

To find the invitation:

###### To find the tester invitation on iOS

1. Open the Messages app on the iPhone.
2. Tap **Filters** in the upper-left
   corner (or swipe right from the message list).
3. Tap **Unknown Senders**.
4. Look for the RBM Tester Management message and tap
   **Make me a tester** to accept the
   invitation.

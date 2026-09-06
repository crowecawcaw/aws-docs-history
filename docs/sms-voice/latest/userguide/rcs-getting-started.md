# Getting started with RCS

This guide walks you through setting up your first RCS agent in AWS End User Messaging,
and sending and receiving your first RCS message. By the end, you will have a
working RCS testing environment. Estimated time to complete: 15–30
minutes.

Here is what this guide covers:

1. Create an AWS RCS Agent and submit a testing registration
2. Add a test device and accept the tester invitation
3. Send your first outbound RCS message
4. Test inbound (two-way) messaging with keywords
   For background on how RCS works in AWS End User Messaging, including the two-level identity model
   (AWS RCS Agent and RCS for Business IDs), see
   [What is RCS?](rcs-overview.md "rcs-overview.md").

## Setting up and testing RCS

This section guides you through creating an AWS RCS Agent, registering a test
device, sending your first RCS message, and verifying delivery. After completing
these steps, you can proceed to launch RCS in production countries.

### Prerequisites

Before you begin, make sure you have the following:

- **An AWS account with AWS End User Messaging
  access** — You need an AWS account with
  permissions to use AWS End User Messaging. If you don't have an account,
  see the
  [AWS account setup guide](../../../accounts/latest/reference/welcome-first-time-user.md "../../../accounts/latest/reference/welcome-first-time-user.md").
- **A phone with RCS enabled** —
  You need an Android phone with RCS messaging enabled in the default
  messaging app, or an iPhone running iOS 18 or later. This phone
  serves as your test device for receiving RCS messages.
- **(Optional) AWS CLI configured**
  — If you want to test using the API instead of the console,
  install and configure the AWS CLI or use an AWS SDK such as
  boto3 for Python.

### Step 1: Create your AWS RCS Agent and submit a testing registration

The first step is to create an AWS RCS Agent and submit a testing
registration. The testing registration creates an RCS for Business ID
(testing agent) that you can use to send messages to registered test devices
without carrier approval.

For full details on AWS RCS Agent management, including the agent lifecycle
and API operations, see
[Managing RCS agents](rcs-agents.md "rcs-agents.md").

#### Creating an AWS RCS Agent (console)

###### To create an AWS RCS Agent and submit a testing registration

1. Open the
   [AWS End User Messaging console](https://console.aws.amazon.com/sms-voice/home "https://console.aws.amazon.com/sms-voice/home").
2. In the navigation pane, under
   **Configurations**, choose
   **RCS agents**.
3. Choose **Create RCS Agent**.
   This creates an AWS RCS Agent and then immediately
   guides you through creating a testing registration in a single
   workflow.
4. The next screen shows an introduction to RCS and explains
   the setup process. Review the information and choose
   **Next** to continue.
5. On the **Agent details** page,
   set the following:

   - **Friendly name** —
     A console-only label for your AWS RCS Agent. This is
     an internal name for your reference (stored as a tag)
     and is not the name displayed on recipients'
     phones. The friendly name is not available through the
     API.
   - **Deletion protection**
     — (Optional) Enable to prevent accidental deletion
     of the agent.
   - **Tags** —
     (Optional) Add tags to organize and identify your
     agent.

6. In the **Brand information**
   section of the same page, enter the following:

   - **Display name** —
     The brand name that recipients see alongside your RCS
     messages.
   - **Description** —
     A brief description of your brand or business.
   - **Use case** —
     Select the primary use case for your RCS messaging (for
     example, transactional notifications, marketing, or
     customer support).

7. In the **Brand assets** section
   of the same page, upload the following:

   - **Logo** —
     224 × 224 pixels, PNG with transparency, under
     50 KB.
   - **Banner image** —
     1440 × 448 pixels, PNG or JPEG, under
     200 KB.
   - **Brand color** —
     A hex color code (for example,
     `#1A73E8`) with a minimum contrast ratio of
     4.5:1 against a white background.

###### Important

Some brand assets cannot be changed after the agent is
submitted for registration. Prepare your final brand assets
before creating the agent. If you want to experiment first,
you can quickly create a test agent using this flow, then
create a fresh AWS RCS Agent with finalized brand assets
later. 8. On the **Compliance keywords**
page, configure your keywords and auto-response messages. 9. On the **Review** page, verify
all your settings. 10. Choose **Validate and submit**
to create the AWS RCS Agent and submit the testing
registration.

###### Note

You have successfully created an AWS RCS Agent and submitted a
testing registration. Your testing agent is typically approved
within minutes. Now let's enable test messaging to your
device.

#### Creating an AWS RCS Agent (CLI)

You can also create an AWS RCS Agent using the AWS CLI. First,
create the agent, then submit a testing registration.

Step 1: Create the AWS RCS Agent:

```
aws pinpoint-sms-voice-v2 create-rcs-agent \
    --deletion-protection-enabled
```

Step 2: Submit a testing registration for the agent. Use the
`CreateRegistration` API with the registration type for
RCS testing. You can use the
`DescribeRegistrationFieldDefinitions` API to
programmatically retrieve all available registration form fields
before submitting. Provide your brand assets, description, and
contact details as part of the registration form fields.

For details on the registration API, see
[Managing RCS agents](rcs-agents.md "rcs-agents.md").

### Step 2: Add a test device

After your testing registration is approved, add your phone as a test
device so you can receive RCS messages from your testing agent.

###### Note

After you add a test device, the tester invitation is not sent
immediately. The system delays activation for at least 120 seconds,
and it can take up to 20 minutes for the invitation to arrive. The
console shows an approximate activation time. You do not need to
wait before adding the device — the system handles the delay
automatically.

Console

###### To add a test device

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and
   choose the **Testing** tab.
2. Choose the **RBM tester management**
   sub-tab.
3. Choose **Add RBM tester**.
4. Enter the phone number of your test device in E.164 format (for
   example, `+12065550100`).
5. Choose **Send verification code**.

AWS CLI
Use the `CreateVerifiedDestinationNumber` API with
the `--rcs-agent-id` parameter to register a test
device for your AWS RCS Agent:

```
aws pinpoint-sms-voice-v2 create-verified-destination-number \
    --destination-phone-number +12065550100 \
    --rcs-agent-id rcs-a1b2c3d4
```

After you add the test device, AWS End User Messaging sends a tester invitation to the
phone number. The invitation comes from an RCS agent called
**RBM Tester Management** and contains
two buttons to accept or decline:
**Make me a tester** and
**Decline**. The recipient must tap
**Make me a tester** to complete
verification.

###### Note

On iOS devices (iPhone with iOS 18 or later), the tester invitation
may appear in the **Unknown Senders**
folder in the Messages app rather than the main inbox. If you don't
see the invitation, check the Unknown Senders folder.

For more details on managing test devices, including the API approach and
troubleshooting, see
[Testing RCS messages](rcs-testing.md "rcs-testing.md").

### Step 3: Send your first RCS message

After your test device has accepted the tester invitation, you can send
your first RCS message. You can use the AWS End User Messaging console or the API.

Console

###### To send a test message using the console

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and
   choose the **Testing** tab.
2. Choose **Outbound test messages**.
   The console displays a preview of how your message will render
   on the recipient's device, along with the JSON request
   body and CLI command.
3. Choose a verified test device from the list.
4. Enter your message text.
5. Choose
   **Send test message**.

###### Note

You can optionally set a configuration set for message events.
Configuration sets let you consume granular delivery receipts
(DLRs) and other message events in the event destination of
your choice. This is optional for testing but recommended for
production use. For details, see
[RCS CloudWatch metrics and monitoring](rcs-monitoring.md "rcs-monitoring.md").

AWS CLI
Use the `send-text-message` command to send a test
message. Specify your AWS RCS Agent ARN as the origination
identity:

```
aws pinpoint-sms-voice-v2 send-text-message \
    --destination-phone-number +12065550100 \
    --origination-identity arn:aws:sms-voice:us-east-1:123456789012:rcs-agent/rcs-a1b2c3d4 \
    --message-body "Hello from RCS! This is my first test message."
```

The `send-text-message` command is the same command
you use for SMS. When you specify an AWS RCS Agent ARN as the
origination identity, AWS End User Messaging delivers the message via RCS.

### Step 4: Test inbound (two-way) messaging

You can test inbound RCS messaging by configuring a keyword with an
auto-response and then sending a message from your test device that matches
that keyword.

###### To test inbound messaging with auto-response keywords

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and
   configure a keyword. For example, set the keyword
   `RCSINBOUNDTESTING` with an auto-response message
   such as "Inbound test successful! Your message was
   received."
2. On the **Testing** tab, choose
   **Inbound deep link**.
3. In the **Default message body**
   field, enter the keyword you configured (for example,
   `RCSINBOUNDTESTING`).
4. Choose **Generate link**. The
   console generates an inbound deep link URL using the GSMA
   standard `sms:` URI scheme. This deep link is
   embedded in the QR code displayed on the screen.
5. Scan the QR code with your verified tester phone. This opens
   the native messaging app with a pre-populated message addressed
   to your AWS RCS Agent.
6. Send the message from your test device.
7. Verify that you receive the auto-response message on your test
   device.

Testing auto-response keywords does not require setting up an event
destination or Amazon SNS topic. The auto-response is handled entirely by
AWS End User Messaging based on the keyword configuration on your AWS RCS Agent.

To receive and process arbitrary inbound messages (not just keyword
matches), you need to configure an Amazon SNS topic for two-way messaging.
For details, see
[Receiving inbound RCS messages](rcs-inbound.md "rcs-inbound.md").

### What you accomplished

By completing the steps in this guide, you have:

- Created an AWS RCS Agent with your brand assets and submitted a
  testing registration
- Registered a test device and accepted the tester invitation
- Sent your first RCS message and verified delivery
- Tested inbound messaging using auto-response keywords

Your testing environment is now ready. Here are ways to integrate RCS
messaging into your application or fine-tune how RCS messaging works:

- **Receive and process inbound messages**:
  Configure an Amazon SNS topic to receive inbound RCS messages and
  process them with Lambda functions. See
  [Receiving inbound RCS messages](rcs-inbound.md "rcs-inbound.md").
- **Track delivery events**:
  Set up configuration sets to consume granular delivery receipts (DLRs)
  and other message events in the event destination of your choice. See
  [RCS CloudWatch metrics and monitoring](rcs-monitoring.md "rcs-monitoring.md").
- **Enable SMS fallback**:
  Create a phone pool with your AWS RCS Agent and SMS phone numbers to
  automatically fall back to SMS when RCS delivery is not possible. See
  [RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md").
- **Launch in production countries**:
  Submit country launch registrations to send RCS messages to all
  recipients in supported countries. See
  [Launching RCS in countries](rcs-country-launch.md "rcs-country-launch.md").

## AI agent prompt for RCS setup

If you use a generative AI coding assistant or AI agent, you can use the
following prompt to get help creating an AWS RCS Agent, submitting a testing
registration, and sending your first test message using the AWS CLI.

###### Note

Copy the following prompt and paste it into your AI agent or coding
assistant:

```

## RCS Setup Assistant Prompt

Help me set up RCS messaging in AWS End User Messaging using the AWS CLI.
The service is `pinpoint-sms-voice-v2`. Walk me through each step with exact
CLI commands. Ask me for all required details before generating any commands.

**Important rules for generating commands:**
- All commands use the `pinpoint-sms-voice-v2` service.
- Use `create-rcs-agent` exactly as spelled — NOT `create-r-c-s-agent`.
- Use the term "testing" — NOT "sandbox".
- There is NO `describe-messages` API. Do not generate it.
- `create-rcs-agent` does NOT accept brand asset parameters (no display name,
  no logo, no banner, no color). Brand assets are registration fields only.
- `create-verified-destination-number` uses `--rcs-agent-id`, NOT
  `--origination-identity`.

### Step 1: Create an RCS Agent

Use `create-rcs-agent`. This creates the agent resource only.
Optional parameters: `--deletion-protection-enabled`, `--opt-out-list-name`,
`--tags`.
The response returns `RcsAgentId` and `RcsAgentArn` — save both.

### Step 2: Create and submit a testing registration

This configures brand assets and submits for approval. It requires multiple
API calls in sequence:

a. `create-registration --registration-type TEST_RCS_LAUNCH_REGISTRATION`
   → returns `RegistrationId`. Save it.

b. `create-registration-association --registration-id <id> --resource-id <agent-id>`
   → links the registration to the agent.

c. Upload images as attachments (two calls):
   `create-registration-attachment --attachment-body fileb://<logo-path>`
   `create-registration-attachment --attachment-body fileb://<banner-path>`
   → each returns `RegistrationAttachmentId`. Save both.

d. Set ALL required registration fields using `put-registration-field-value`
   with `--registration-id`, `--field-path`, and the appropriate value flag
   (`--text-value`, `--select-choices`, or `--registration-attachment-id`).

   Required fields (ALL must be set or registration will be DENIED):
   - `agentDetails.brandName` (text, 2-65 chars)
   - `agentDetails.serviceName` (text, 1-100 chars)
   - `agentDetails.senderDisplayName` (text, 1-40 chars)
   - `agentDetails.useCase` (select: OTP, TRANSACTIONAL, PROMOTIONAL, MULTI_USE)
   - `agentDetails.agentDescription` (text, 1-100 chars)
   - `agentDetails.logoImage` (attachment ID from step c, 224x224 PNG)
   - `agentDetails.bannerImage` (attachment ID from step c, 1440x448 PNG/JPEG)
   - `agentDetails.accentColor` (text, hex code e.g. #0066CC)
   - `agentDetails.privacyPolicyUrl` (text, valid URL)
   - `agentDetails.termsAndConditionsUrl` (text, valid URL)
   - `agentDetails.averageMonthlyRcsFrequency` (select: 10, 100, 1000+)
   - `agentDetails.monthlyRcsVolume` (text, 1-100000)
   - At least ONE contact method WITH its label:
     agentDetails.contactWebsite + agentDetails.contactWebsiteLabel, OR
     agentDetails.contactPhoneNumber + agentDetails.contactPhoneLabel, OR
     agentDetails.contactEmailAddress + agentDetails.contactEmailLabel

e. Verify all fields: `describe-registration-field-values --registration-id <id>`
   Any field showing `DeniedReason: MISSING_REQUIRED_FIELD` must be set.

f. Submit: `submit-registration-version --registration-id <id>`

g. Poll status: `describe-registrations --registration-ids <id>`
   Wait for `RegistrationStatus: COMPLETE`.

**Error recovery:** If registration is DENIED, you must:
1. `create-registration-version --registration-id <id>` (creates new draft)
2. Re-populate ALL fields from scratch (new versions do NOT inherit values)
3. Fix the issue noted in `DeniedReasons`
4. Re-submit

### Step 3: Add a test device

**Prerequisite:** Step 2 must be COMPLETE and the agent's `TestingAgent.Status`
must be `ACTIVE` (check with `describe-rcs-agents`). Then wait at least 120
seconds after the agent becomes ACTIVE.

Use `create-verified-destination-number --destination-phone-number <E.164>
--rcs-agent-id <agent-id>`.

The device status will be `PENDING`. The user must accept the RCS tester
invitation on their physical device. Check status with
`describe-verified-destination-numbers` — wait for `VERIFIED`.

### Step 4: Send a test RCS message

**Prerequisite:** Step 3 device must be `VERIFIED`.

Use `send-text-message --destination-phone-number <E.164>
--origination-identity <agent-arn> --message-body "<text>"
--message-type TRANSACTIONAL`.

Returns `MessageId`.

### Step 5: Verify delivery

For testing: check the test device — the message appears from the branded
RCS agent.

For production monitoring: set up event destinations BEFORE sending messages
using `create-event-destination` (SNS, CloudWatch Logs, or Firehose). Event
destinations do not retroactively capture events for already-sent messages.
CloudWatch metrics in the `AWS/SMSVoice` namespace provide aggregate stats.

---

**Before generating commands, ask me for:**
- Brand name, service name, and sender display name
- Agent description (what the agent does, what messages users receive)
- Use case type: OTP, TRANSACTIONAL, PROMOTIONAL, or MULTI_USE
- Logo file path (224x224 PNG) and banner file path (1440x448 PNG/JPEG)
- Brand accent color hex code (e.g. #0066CC)
- Privacy policy URL and terms & conditions URL
- One contact method with label: website URL, phone number, or email
- Estimated monthly RCS volume and per-user message frequency
- Test device phone number in E.164 format (e.g. +12065550100)

```

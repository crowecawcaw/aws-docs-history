

# Troubleshoot contact flows that don't behave as expected in Connect Customer
<a name="troubleshoot-contact-flow-behavior"></a>

A contact flow can look correct in the visual editor and still behave unexpectedly: it takes an unexpected branch, contact attributes don't take effect or aren't passed, a contact disconnects when you didn't intend it to, the contact enters the wrong queue, or an announcement plays to only one party. The cause is usually a block's behavior, prerequisites, published state, channel compatibility, an edit made outside the UI (through the API or an import), or a dependency such as a Lambda function. Some symptoms come from a block's design constraints, a known issue, or a service-side regression. This page covers the resolution steps by block and dependency. To first isolate *where* the problem occurs, start from the hub.

**Parent page (symptom-based entry point)**  
For the full picture of narrowing down a symptom, determining scope, and delegating boundary issues, see the hub, [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md).

**Routing-configuration issues**  
If contacts don't reach an agent at all, or are distributed to the wrong agent because of your *routing configuration*, see [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).

**Audio quality issues**  
If a contact connects but the audio quality is poor (one-way audio, echo, choppy audio, or delay), see [Troubleshoot audio quality issues in Connect Customer](troubleshoot-audio-quality.md).

**Intended audience**  
This guide assumes you are a Connect Customer administrator who can create and edit contact flows, and who can access contact flow logs (in CloudWatch) and contact records (CTRs).

## Before you begin: gather this information
<a name="troubleshoot-contact-flow-behavior-before-you-begin"></a>

Collect the following before you start. You need it to isolate the problem and, if necessary, to open a case with AWS Support.
+ **Description of the symptom** – what happened (an unexpected branch, attributes that don't take effect, a disconnect, the wrong queue, or an announcement you can't hear), the block you suspect, and the affected channel (voice, chat, or task).
+ **Instance Amazon Resource Name (ARN)** – see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
+ **ContactId** of each affected contact (provide 3–5 examples).
+ **Time of occurrence** in Coordinated Universal Time (UTC).
+ **The target contact flow name and its export (JSON)** – export the latest version from the editor so you can review the content of the published flow.
+ **Confirmation that contact flow logs are enabled** – if they aren't, enable logging with the Set logging behavior block in the flow, then reproduce the problem. See [Flow block in Connect Customer: Set logging behavior](set-logging-behavior.md).

## Step 1: Identify the symptom (quick reference)
<a name="troubleshoot-contact-flow-behavior-step1"></a>

The hub has a more complete symptom table. This table lists only the flow-side symptoms that this page resolves. If your symptom isn't listed, or you're not sure, continue to Step 2.


| Symptom | Where to go | 
| --- | --- | 
| Input (DTMF or voice) is captured, but the flow returns Timeout, Error, or an unexpected branch | [Input is captured but the flow returns Timeout, Error, or an unexpected branch (Get or Store customer input)](#troubleshoot-contact-flow-behavior-customer-input) | 
| Attributes don't take effect, values aren't passed, or they appear duplicated | [Attributes don't take effect, aren't passed, or appear duplicated (Set or Check contact attributes)](#troubleshoot-contact-flow-behavior-attributes) | 
| The contact enters the wrong queue, or a change to the queue setting has no effect | [The contact enters the wrong queue, or a queue-setting change has no effect (Set working queue)](#troubleshoot-contact-flow-behavior-working-queue) | 
| A contact disconnects unexpectedly, skips the queue wait, or the call runs abnormally long | [A contact disconnects unexpectedly, skips the queue wait, or runs abnormally long](#troubleshoot-contact-flow-behavior-disconnect) | 
| Branching breaks, or a Lambda dependency sends the contact down an unexpected branch | [Branching breaks or takes an unexpected path (a Lambda dependency in the flow)](#troubleshoot-contact-flow-behavior-lambda) | 
| You deleted a flow by mistake, or you want to restore one from a backup | [You deleted a flow by mistake, or want to restore one from a backup](#troubleshoot-contact-flow-behavior-backup) | 
| An announcement (Play prompt or whisper) plays to only one party, or a whisper doesn't fire | [An announcement or whisper plays to only one party, or doesn't fire](#troubleshoot-contact-flow-behavior-whisper) | 
| A callback reaches voicemail, or you want to restrict outbound hours | [Callback, voicemail detection, or time restriction](#troubleshoot-contact-flow-behavior-callback) | 

## Step 2: Determine the scope
<a name="troubleshoot-contact-flow-behavior-step2"></a>
+ **A single flow or a single block** – suspect that block's configuration, its published state, and the attributes or Lambda function it references. See the matching section in Step 5.
+ **Multiple flows, or organization-wide, with no customer-side change** – suspect a service-side regression or a Regional service issue, and check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status). If you don't see a related event but the symptoms persist across flows or sites, open a support case.

**Check what changed on a specific date**  
If the flow worked before but stopped on a specific date, check what changed that day: the **flow's edit history** (a UI edit, or an edit made outside the UI with the `UpdateContactFlowContent` API), or a **service update**. For how to detect edits made outside the UI, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

## Step 3: Localize the problem using contact flow logs and CTRs
<a name="troubleshoot-contact-flow-behavior-step3"></a>

The fields to read—and the common pitfalls—in contact flow logs (block execution order, branch `Results`, the QueueId ARN set by Set working queue, the Invoke Lambda response, and the `Loop` count) and in CTRs (such as `DisconnectReason`) are consolidated in the dedicated isolation reference. See [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

The key points for this page (see that reference for details):
+ `DisconnectReason=CONTACT_FLOW_DISCONNECT` indicates that the flow ended the contact. In the flow log, identify the terminal block that the contact reached—a Disconnect block, or an End flow / Resume block in an inbound or disconnect flow—and which branch routed to it. Step 5 covers the common causes.
+ The draft can differ from the published version (a change that wasn't published), and Set working queue is determined by the **QueueId ARN and not the display name**.

## Step 4: Collect diagnostic data
<a name="troubleshoot-contact-flow-behavior-step4"></a>

For how to read each field, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

1. **Contact flow logs (CloudWatch)** – with logging enabled, reproduce the problem, download the logs for the affected ContactId, and check which block returned which `Results`.

1. **CTR / DescribeContact** – review `DisconnectReason` and the queue or agent reached.

1. **Compare the published flow with the exported JSON** – match the QueueId ARN in the Actions section against the output of `describe-queue`.

1. **CloudTrail** – check for `UpdateContactFlowContent` calls. A UI edit is recorded with `invokedBy` = `connect.amazonaws.com` and a principal that is the service-linked role `AWSServiceRoleForAmazonConnect` (the `userAgent` is also `connect.amazonaws.com`). An event with no `invokedBy` is a direct call made outside the UI (through the API, an import, CI/CD, CloudFormation, or Lambda), and its `userIdentity.type` can be `IAMUser` or `AssumedRole`. As an exception, events from the service-linked role `AWSServiceRoleForAmazonConnectSynchronization` are managed cross-Region synchronization, not a UI edit.

1. **Compare a successful contact with a failed contact** – when the same flow or block produces different results, identify the difference (attribute key, line of business, or a direct call compared with a transfer).

## Step 5: Resolve by cause
<a name="troubleshoot-contact-flow-behavior-step5"></a>

### Input is captured but the flow returns Timeout, Error, or an unexpected branch (Get or Store customer input)
<a name="troubleshoot-contact-flow-behavior-customer-input"></a>

Use the Get customer input and Store customer input blocks to resolve these symptoms. For more information about these blocks, see [Flow block in Connect Customer: Get customer input](get-customer-input.md).
+ **The timeout is too short.** The Set timeout on the Get customer input block is the time the block waits for the first DTMF digit. It must be a static integer between 1 and 180 seconds. If it's too short, the block can time out before the caller responds; increase the Set timeout value.
+ **You need to see what the customer actually pressed and when.** To confirm the keypad selections and their timing relative to the prompt, review the automated interaction logs. They appear on the Contact details page, list the keypad selections and the prompts that played, and let you play a specific prompt against the call recording. Customer timeouts also appear there. Automated interaction logs require Enable Automated Interaction Logs on the instance and call recording storage, and viewing keypad inputs requires the Automated interaction voice (IVR) transcripts (unredacted) security profile permission. Allow up to 30 minutes after the contact ends for the log to appear. See [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md).
+ **DTMF isn't detected on some calls.** Check whether the calls where input isn't detected are forwarded to Connect Customer from another system. If so, check whether the issue also occurs when you dial the Connect Customer number directly, without forwarding.

### Attributes don't take effect, aren't passed, or appear duplicated (Set or Check contact attributes)
<a name="troubleshoot-contact-flow-behavior-attributes"></a>

For more information about these blocks, see [Flow block in Connect Customer: Set contact attributes](set-contact-attributes.md).
+ **A mismatch in the key name, type (string compared with number), or namespace** (such as External or User Defined) sends Check contact attributes down an unexpected branch. Compare the values and correct them. Don't use `$` in attribute keys. Connect Customer treats `$` as a special character: text-to-speech reads it literally, and you can't retrieve a value whose key contains `$`. If you set attributes by using the `UpdateContactAttributes` API, keys can include only alphanumeric, dash, and underscore characters. For more information, see ["$" is a special character](what-is-a-contact-attribute.md#dollar-sign-special).
+ **Attributes appear to be written more than once.** The same key can appear on more than one line in the CloudWatch flow logs (see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md)). Make downstream processing idempotent by key name (last-write-wins), and consume the **final attribute from the CTR (Kinesis stream)** rather than counting log entries.

### The contact enters the wrong queue, or a queue-setting change has no effect (Set working queue)
<a name="troubleshoot-contact-flow-behavior-working-queue"></a>

This can be caused by a Set working queue change that wasn't published (the flow still uses the old state), or by a display name that doesn't match the QueueId ARN. An edit made outside the UI with the `UpdateContactFlowContent` API can replace the ARN while leaving the display name unchanged. The flow logs show no error. Set working queue is determined by the QueueId ARN. Match the ARN in the exported JSON against `describe-queue`. If the ARN isn't the intended queue, open the Set working queue block, re-select the queue, and then save and publish the flow. For details, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

### A contact disconnects unexpectedly, skips the queue wait, or runs abnormally long
<a name="troubleshoot-contact-flow-behavior-disconnect"></a>
+ **The menu repeats many times when there's no input.** If you repeat Get customer input by using a Loop block, the menu is replayed according to the loop count that's set on the Loop block when the caller doesn't respond. Check the loop count and the block that the Complete branch connects to when the loop finishes.
+ **An Error on a channel-incompatible block leads to a disconnect.** The Loop prompts block is voice-only. When a chat contact hits a Loop prompts block that has voice prompts, the block returns Error, and a connected Disconnect block ends the contact immediately. This happens when the main flow doesn't explicitly set a customer queue flow and falls back to the instance default (voice-only). Create a chat-compatible customer queue flow, and place a Set customer queue flow block explicitly before Transfer to queue. Connect Customer resolves the customer queue flow in this order: first the Set customer queue flow block, then the instance default.
+ **An orphaned or stalled callback.** A callback that's created when no agent is available can remain in the queue unassigned. If a custom prompt reads out the longest wait time, it announces an enormous wait (for example, hundreds or thousands of minutes) to new callers. Disconnect the stalled contact with **End** on the contact details page or with the `StopContact` API, and remove the cause.

### Branching breaks or takes an unexpected path (a Lambda dependency in the flow)
<a name="troubleshoot-contact-flow-behavior-lambda"></a>
+ The status codes in the Invoke Lambda block's log are the responses from your own Lambda function, and Connect Customer treats a call-level failure differently from a value that the function returns. A call-level failure—an HTTP `500`, throttling, or a timeout—causes the Invoke Lambda block to retry and then take the **Error** branch. Always connect the Error branch of the Invoke AWS Lambda function block to a block that handles the error. A status code that the function returns in its response payload, such as `404` or `503`, comes back on the **Success** branch, and your flow branches on that value. Compare the logs of a successful contact and a failed contact to find the difference in the values that the function returned. For the IAM permissions that a Lambda function in a flow requires (including KMS), see [Flow block in Connect Customer: AWS Lambda function](invoke-lambda-function-block.md).
+ **The 8-second timeout on a synchronous Lambda invocation.** If execution exceeds this limit, consider an asynchronous pattern.

### You deleted a flow by mistake, or want to restore one from a backup
<a name="troubleshoot-contact-flow-behavior-backup"></a>

Deleted flows can't be restored, but archived flows can be restored. To import a flow from a JSON export, choose **Routing**, **Contact flows**, and then choose **Save**, **Import flow**. See [Import and export flows between flow designers in Connect Customer](contact-flow-import-export.md). To prevent loss, implement a periodic backup with the `describe-contact-flow` API.

### An announcement or whisper plays to only one party, or doesn't fire
<a name="troubleshoot-contact-flow-behavior-whisper"></a>
+ **The agent whisper doesn't play.** Create an agent whisper flow. For voice, the default agent whisper flow (Default agent whisper) runs even if you don't add a Set whisper flow block. For chat, there's no default whisper, so the agent whisper plays only if you add a Set whisper flow block.
+ **On outbound calls, the agent whisper doesn't play for some dialing methods.** On inbound calls, the agent whisper flow plays when the agent accepts the contact. On outbound calls, it plays for callbacks, and for calls placed with the `StartOutboundVoiceContact` API when the flow transfers the contact to an agent. It doesn't play for calls that an agent places manually from the CCP or for campaign preview dialing (in preview dialing, the outbound whisper flow can play the whisper to the agent).
+ **The Transfer to Agent (beta) block isn't visible.** It's available only in the Transfer to Agent and Transfer to Queue flow types, not in the standard contact flow type.
+ On a voice call, the **beep** that the customer hears when the contact is connected to an agent is the initial behavior of the default customer whisper flow (Default customer whisper). You can override or disable it with the Set whisper flow block.

### Callback, voicemail detection, or time restriction
<a name="troubleshoot-contact-flow-behavior-callback"></a>
+ **A queued callback reaches voicemail.** In the default agent-first callback mode, the Check call progress block isn't supported and the contact routes to its Error branch, so voicemail can't be detected. The Check call progress block supports only outbound campaign calls and customer-first callbacks. Switch to customer-first callback mode (available only in next-generation Connect Customer instances), and connect to the agent only after you detect a live answer. Treat the Not detected branch of Check call progress as possibly either voicemail or a live person.
+ **You want to restrict callback dialing to certain hours.** For an example architecture that lets callers choose a time within your hours of operation and schedules the callback for that time, see [Caller Scheduled Callback in Amazon Connect](https://aws.amazon.com/blogs/contact-center/caller-scheduled-callback-in-amazon-connect/) on the AWS Contact Center Blog.

## Step 6: Isolate carrier issues (boundary)
<a name="troubleshoot-contact-flow-behavior-step6"></a>

You can't resolve the following with contact flow configuration. The hub's Step 5 lists where to delegate each boundary issue.
+ **Rule out Connect Customer-side configuration first.** Before you attribute a failure to the carrier, check the Connect Customer-side configuration. For example, Connect Customer doesn't allow anonymous calls (calls without caller ID), so if the queue's Outbound caller ID number isn't set to a number that you've claimed or ported to your instance, the call fails. When an agent places the call from the CCP, the CCP shows an Invalid outbound configuration error. For how to fix it, see [CCP outbound configuration issues](common-ccp-issues.md#ccp-outbound-issues). For the other items to check, see Step 5 of the hub.
+ **Routing-configuration issues.** If the contact reaches the queue but isn't distributed to an agent, see [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).

## Before you contact AWS Support
<a name="troubleshoot-contact-flow-behavior-step7"></a>

If the issue persists after troubleshooting, open a case with **3–5 examples**, and include:
+ Instance ARN and a description of the symptom (which block, which branch, and what happened).
+ ContactIds, timestamps (UTC), and a contact-record snapshot (including `DisconnectReason`).
+ The target contact flow export (JSON) and the contact flow logs for the affected ContactIds.
+ A comparison of a successful contact and a failed contact (when the same flow produces different results).
+ If you use Lambda: the function name and the response status or return value on failure.
+ The frequency of the issue and the date and time it started (UTC).
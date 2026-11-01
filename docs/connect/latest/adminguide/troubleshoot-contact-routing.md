

# Troubleshoot contact routing and handling in Connect Customer
<a name="troubleshoot-contact-routing"></a>

Routing and contact-handling problems—contacts that don't reach the intended queue or agent, contacts routed to the wrong queue or agent, contacts stuck in a queue, contacts that disconnect before reaching an agent, contact flows that take an unexpected branch, transfers or quick connects that fail, or callbacks that reach voicemail—can originate at any point along the call path. The cause can be a routing profile, a queue, a priority or delay setting, Set routing criteria, a contact flow block, a Lambda function invoked from a flow, or a carrier or device outside Connect Customer. This page is the starting point for diagnosing them. It helps you narrow down *where* in the path the problem occurs, then directs you to the specialized topic that resolves it.

**Audio quality issues**  
This page covers *where* and *to whom* a contact connects (routing and handling). If a contact connects but has an audio *quality* problem—one-way audio, echo, choppy or robotic audio, or delay—see [Troubleshoot audio quality issues in Connect Customer](troubleshoot-audio-quality.md).

**Call disconnects**  
If a contact disconnects unexpectedly *after* it is routed, see [Troubleshoot call disconnects by using DisconnectDetails in the contact record](troubleshoot-call-disconnects.md).

**Intended audience**  
This guide assumes you are a Connect Customer administrator who can manage routing profiles, queues, and contact flows, and who can access contact records (CTRs) and contact flow logs.

## Before you begin: gather this information
<a name="troubleshoot-contact-routing-before-you-begin"></a>

Collect the following for the affected contacts before you start. You need it to isolate the problem and, if necessary, to open a case with AWS Support.
+ **Description of the symptom** – what happened (didn't reach the intended queue or agent, routed to the wrong queue, stuck in a queue, disconnected before reaching an agent, uneven distribution, flow took an unexpected branch, transfer or callback failed) and the affected channel (voice, chat, task, email, or callback). You use this in Step 1.
+ **Instance Amazon Resource Name (ARN)** – see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
+ **ContactId** of each affected contact (provide 3–5 examples).
+ **Time of occurrence**, including time zone (record in Coordinated Universal Time (UTC) where possible).
+ **Intended queue name, routing profile name, and agent** – both the routing target you expected and the actual values.
+ Where applicable, the **target contact flow name and its export (JSON)**, and the **contact flow logs** for the affected ContactIds.

**Prerequisites**  
Before troubleshooting, confirm the basics: the target queue is associated with a routing profile; the agent is assigned to that routing profile and is set to **Available**; the security profile of the administrator who changes or deletes settings has the required permissions (for example, Edit and Delete for the Routing section); and contact flow logs are enabled.

## Step 1: Identify the symptom
<a name="troubleshoot-contact-routing-step1"></a>

Use the symptom to jump to the most likely cause. If your symptom isn't listed, or you're not sure, continue to Step 2.

**Check for an active AWS event first**  
Before you work through the symptom table, rule out an active AWS service event. If multiple symptoms (misrouting, login failures, or no incoming contacts) appear at the same time with no change on your side, check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status). This is the quickest, highest-impact cause to rule out. If none matches but the problem persists, open a support case.


| Symptom | Most likely area | Where to go | 
| --- | --- | --- | 
| Outbound calls fail and the CTR DisconnectReason is TELECOM\_PROBLEM, TELECOM\_BUSY, TELECOM\_NUMBER\_INVALID, TELECOM\_UNANSWERED, or TELECOM\_TIMEOUT, and ConnectedToSystemTimestamp is null (the destination never answered). | Destination or carrier (PSTN side)—outside Connect Customer | Confirm and open a support case—see [Step 5: Delegate boundary issues (carrier, device, audio, or disconnect)](#troubleshoot-contact-routing-step5). | 
| Outbound calls are rejected or flagged as spam, and DisconnectReason is TELECOM\_POTENTIAL\_BLOCKING | Carrier spam or reputation blocking—outside Connect Customer | Register your numbers with carrier reputation services; see [Optimize your reputation for outbound calling in Connect Customer](optimize-outbound-calling.md). AWS can't unblock carrier networks for you. | 
| The CTR DisconnectReason is TELECOM\_ORIGINATOR\_CANCEL. For inbound calls, the caller cancelled before connecting to Connect Customer (often within a second or two). For outbound calls, either the destination didn't answer—in which case Connect Customer sends the cancel after about a 60-second timeout, not a carrier fault—or the agent or API cancelled before connecting. The about-60-second timeout applies only to the outbound-unanswered case. | Originating side—an inbound caller who cancelled, or an outbound no-answer or agent or API cancel | Check the destination path. If you transfer with the Transfer to phone number block, you can set its Timeout to control this below 60 seconds—see [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md). | 
| After a number is ported, inbound calls flow into the contact flow of a different number (the number the customer dialed and the contact record's SystemEndpoint.Address, shown as System address or number in contact search, don't match) | Carrier number mapping | See [How to port your numbers to Connect Customer](about-porting.md). | 
| Contacts never reach a specific queue or agent, or get stuck in a queue | Routing profile association, concurrency, or the agent's status (Available, Offline, or a custom status) | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) | 
| Contacts are routed to the wrong queue or agent | Set working queue in the contact flow (display name and ARN mismatch) or branching | Step 3. If the ARN is wrong, see [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md). If the contact reaches the queue but isn't distributed, see [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md). | 
| Contacts aren't distributed according to queue priority, overflow, or delay, or they concentrate on one agent | Routing order (Connect Customer first offers a new contact to the agent handling the fewest contacts across all channels, and compares time in Available status only to break a tie, routing to the agent who has been Available the longest; the routing profile's Set routing order setting determines whether outbound contacts reset that time), routing profile priority and delay, remaining after-contact work (ACW), or status changes from an external integration | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) (distribution section) | 
| Contacts aren't distributed according to the specified skill or proficiency | Routing criteria has no effect if the contact is transferred into an agent queue; Set routing criteria takes effect when the contact is transferred to a standard queue (with Transfer to queue); an expiry set too short competes with default queue-based routing. (A non-expiring step is allowed only as the final step.) | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) (proficiency section) | 
| Cross-channel routing isn't delivered (for example, an agent handling a chat doesn't receive a voice contact) | Cross-channel concurrency, or a missed contact that must be cleared before other channels route to that agent | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) | 
| A contact flow takes an unexpected branch, attributes don't take effect or aren't passed, or the flow disconnects the contact | Contact flow block behavior, prerequisites, published state, or channel compatibility | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) | 
| Input (DTMF or voice) is captured but the flow returns Timeout, Error, or an unexpected branch | Get customer input or Store customer input (timeout or Error branch) | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) (customer input section) | 
| A transfer or quick connect fails, or behavior is unexpected after a transfer | Transfer destination flow type, concurrent call slots, or quick connect association | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) (transfer section) and [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) (whisper and transfer section) | 
| Callbacks, voicemail, or tasks don't work as expected (callbacks reach voicemail, contacts stall, or you want to set a time limit) | Voicemail can't be detected with agent-first callbacks, or in-queue callback design | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) (callback section) and [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) | 
| Branching within a flow breaks, or contacts fall back to default routing | Invoke Lambda failure—for your Lambda function's responses, a call-level failure (500, throttling, or timeout) takes the Error branch after retries, while a status your function returns (such as 404 or 503) is a value on the Success branch; or a missing error branch | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) (Lambda section) | 
| Routing is limited by concurrent calls, instance limits, or quotas (for example, ServiceQuotaExceededException) | Service quotas or concurrency—verify the effective Concurrent active calls per instance value in Service Quotas (new-instance default quotas can be lower than production needs) | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) (the "contacts never reach a specific queue or agent" section for queue-channel quotas, and the transfer section for concurrent active calls) | 
| Multiple symptoms (misrouting, login failures, and no incoming contacts) occur at the same time with no customer-side change | An AWS service event or a Regional service issue | Check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status); if none, open a support case. | 

## Step 2: Determine the scope
<a name="troubleshoot-contact-routing-step2"></a>

The extent of the impact changes where you look first.
+ **A single agent** – suspect that agent's **routing profile association** and **status** (Available, Offline, or a custom status). See [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).
+ **A single queue or line of business (LOB)** – suspect that queue's configuration, the target contact flow's **Set working queue, branching, or proficiency**, and any Lambda function that references the queue. See [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).
+ **Multiple queues or sites, or multiple symptoms at once with no customer-side change** – suspect an **AWS service event** or a service-side regression, and check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status). If you don't see a related event but the symptoms persist across queues or sites, open a support case.

To size the impact, use real-time metrics to see how many agents are affected. To inspect one agent's activity and status in detail, use the agent activity audit report, which covers a single agent at a time. The [AgentHierarchyGroups](ctr-data-model.md#ctr-AgentHierarchyGroups) field in the contact record shows the hierarchy of the agent on an affected contact, which helps you correlate affected contacts to a team or location.

**Check for changes made on a specific date**  
If the issue started on a specific date across all affected agents, check for **routing configuration changes, service updates, external integration changes** (for example, Salesforce Service Cloud Voice omni-channel), or **agent authentication changes** (SAML or SSO) made on that date.

## Step 3: Localize the problem using CTRs and contact flow logs
<a name="troubleshoot-contact-routing-step3"></a>

Just as audio quality troubleshooting uses the call recording as a dividing line, routing troubleshooting uses **contact records (CTRs) and contact flow logs as the dividing line**. They help you determine whether the problem occurred inside Connect Customer routing and flows, or outside it (carrier or device).

For the fields to read and how to draw conclusions from them—along with the common pitfalls—see the dedicated isolation reference, [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md). The main pitfalls relevant to this page are:
+ Set working queue is determined by the QueueId ARN, not the display name.
+ The draft version of a contact flow can differ from the published version.
+ A call transferred from an upstream carrier or private branch exchange (PBX) doesn't create a contact record until it reaches a phone number claimed in your Connect Customer instance, so a missing record is itself a diagnostic signal—not a failure to find the data.

Follow the conclusion from that page, then continue:
+ If `DisconnectReason` is `TELECOM_PROBLEM`, `TELECOM_BUSY`, `TELECOM_NUMBER_INVALID`, `TELECOM_UNANSWERED`, `TELECOM_TIMEOUT`, or `TELECOM_POTENTIAL_BLOCKING`, or `ConnectedToSystemTimestamp` is null and the destination never answered, the problem is on the destination or carrier side (or, for `TELECOM_ORIGINATOR_CANCEL`, the originating side). A null `ConnectedToSystemTimestamp` on its own can also occur for a queued callback that is still waiting in queue (for a CALLBACK contact, this field is set only when the customer answers), which isn't a carrier problem—confirm the `DisconnectReason` first (as the spoke page notes). Continue to Step 5 (boundary).
+ The contact enters the queue but isn't distributed to an agent → a **routing configuration problem**. See [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).
+ An unexpected branch, `DisconnectReason=CONTACT_FLOW_DISCONNECT`, or a wrong QueueId ARN → a **contact flow problem**. See [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).

## Step 4: Collect diagnostic data
<a name="troubleshoot-contact-routing-step4"></a>

Run these in order. Each links to its full procedure.

1. **Contact flow logs (CloudWatch)** – with logging enabled, reproduce the problem, download the logs for the affected ContactId, and check which block returned which `Results` (Success, Timeout, Error, or a branch name), which **QueueId ARN** the Set working queue block set, and the response from Invoke Lambda—these are your Lambda function's responses, where a call-level failure (500, throttling, or timeout) takes the Error branch after retries, while a status your function returns (such as 200, 404, or 503) is a value on the Success branch. See [Search flow logs stored in an Amazon CloudWatch log group](search-contact-flow-logs.md).

1. **CTR / DescribeContact** – call [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) and review `DisconnectReason`, `ConnectedToSystemTimestamp`, the `Queue` and `Agent` reached, `InitiationMethod`, and `InitialContactId` or `PreviousContactId`. For how to read these, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

1. **Real-time metrics and the agent activity audit report** – check the target agent's **status** (Available, Offline, or a custom status) and when it changed. The agent activity audit report and the agent event stream show *when* the status changed, but not *who* changed it. To find who changed it, check CloudTrail for a `PutUserStatus` event at that time: a change that a supervisor makes in the real-time metrics report, or that an application makes through the API, is recorded there, while an agent's own status change in the Contact Control Panel (CCP) is not. The CCP logs show the agent's own client-side actions.

1. **Routing configuration APIs** – check `DescribeRoutingProfile` (queue associations, per-channel concurrency, and `AgentAvailabilityTimer`).

1. **CloudTrail** – check for `UpdateContactFlowContent` (a misconfiguration from editing outside the UI).

Then branch on what you found:
+ **Contact reaches the queue but isn't distributed to an agent, or drops out of the eligible set** → [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md).
+ **Unexpected branch, attributes don't take effect, the flow disconnects, or a wrong ARN** → [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).
+ **Abnormal metrics, a `TELECOM_*` `DisconnectReason`, or a null `ConnectedToSystemTimestamp` together with a `TELECOM_*` reason** → Step 5 (delegate to the boundary). A null `ConnectedToSystemTimestamp` on its own isn't enough—confirm the `DisconnectReason` first, because a null value can also come from a queued callback that is still waiting in queue (for a CALLBACK contact, this field is set only when the customer answers). Most `TELECOM_*` reasons point to the destination or carrier side; `TELECOM_ORIGINATOR_CANCEL` points to the originating side.

## Step 5: Delegate boundary issues (carrier, device, audio, or disconnect)
<a name="troubleshoot-contact-routing-step5"></a>

Most of the following are outside Connect Customer routing and flow configuration. Confirm the cause, then delegate or open a support case. (One exception: for outbound transfers, you set the Transfer to phone number block Timeout in the flow—see [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md).)
+ **Rule out Connect Customer-side configuration first** (before you attribute a failure to the carrier). Confirm that:
  + Outbound calling is enabled on the instance.
  + The destination country is allowed (country allowlisting is default-deny; see [Countries that call centers using Connect Customer can call by default](country-code-allow-list.md)).
  + The destination number is in E.164 format.
  + You're within the concurrent-active-calls quota (see [Connect Customer service quotas](amazon-connect-service-limits.md)).
  + The agent has the CCP outbound-calls permission.
  + The queue has an outbound caller ID.

  A call can fail outside Connect Customer yet not be a carrier problem – for example, a customer-side PBX or an external voice connector path.
+ **Destination or carrier causes** (`TELECOM_PROBLEM`, `TELECOM_BUSY`, `TELECOM_NUMBER_INVALID`, `TELECOM_UNANSWERED`, or `TELECOM_TIMEOUT`, or a null `ConnectedToSystemTimestamp` when the destination never answered, a wrong flow after porting, or an unclaimed number)—these occur outside Connect Customer. Rule out Connect Customer-side configuration first (the preceding bullet). When a `TELECOM_*` reason appears in the CTR, all retry attempts have already failed; a successful retry would instead show an agent or customer disconnect. Confirm destination-country coverage and number-type restrictions in the Connect Customer [Telecoms Coverage guide](https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf); if number porting is involved, see [How to port your numbers to Connect Customer](about-porting.md); if the cause still isn't found, open a support case with the details listed in the Before you contact AWS Support section.
+ **Carrier spam or reputation blocking** (`TELECOM_POTENTIAL_BLOCKING`)—register your numbers with carrier reputation services and review your outbound calling practices; see [Optimize your reputation for outbound calling in Connect Customer](optimize-outbound-calling.md). AWS can't unblock carrier networks for you.
+ **Originating-side causes** (`TELECOM_ORIGINATOR_CANCEL`)—for inbound calls, the caller cancelled before connecting to Connect Customer (often within a second or two), which is unrelated to the 60-second timeout. For outbound calls, the destination didn't answer, or the agent or API cancelled before connecting; in the outbound-unanswered case the call ends after about 60 seconds. Check the destination path. For an outbound transfer, review the Transfer to phone number block Timeout; see [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md).
+ **Audio quality problems** (continuous ringing, one-way audio, echo, or delay)—see [Troubleshoot audio quality issues in Connect Customer](troubleshoot-audio-quality.md).
+ **Unexpected disconnects after routing** – see [Troubleshoot call disconnects by using DisconnectDetails in the contact record](troubleshoot-call-disconnects.md).

## Before you contact AWS Support
<a name="troubleshoot-contact-routing-step6"></a>

If the issue persists after troubleshooting, open a case with **3–5 examples**, and include:
+ Instance ARN and a description of the symptom (didn't reach, wrong queue, stuck, disconnected before reaching an agent, uneven distribution, unexpected flow branch, or transfer or callback failure, and the affected channel).
+ ContactIds, timestamps (UTC), and a contact-record snapshot (including `DisconnectReason`, `Queue`, `Agent`, `ConnectedToSystemTimestamp`, and `InitiationMethod`).
+ The target contact flow export (JSON) and the contact flow logs for the affected ContactIds.
+ The configuration of the routing profile, queue, and proficiency (Set routing criteria).
+ The extent of the impact (single agent, single queue, or organization-wide) and the date and time the issue started (UTC).
+ If you use Lambda: the function name and the response status or return value on failure.
+ If you suspect a carrier cause: the source and destination numbers (the last 4 digits can be masked) and the times and ContactIds the carrier needs to investigate.


# Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer
<a name="troubleshoot-routing-not-reached"></a>

Contacts that don't reach the intended queue or agent, that are routed to the wrong queue or agent, that get stuck in a queue, or that disconnect before reaching an agent can originate at any of several points on the call path: the routing profile, the queue, a priority or delay setting, Set routing criteria (proficiency), the per-channel concurrency, a contact flow branch, or a carrier, device, or authentication method outside Connect Customer. This page covers the cause-based resolution steps for the *routing-configuration* side. To narrow down *where* the problem occurs, start from the hub, [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md).

**Contact flow block behavior**  
Problems that come from *flow configuration* – a contact flow block takes an unexpected branch, attributes don't take effect, or the flow disconnects the contact—are covered in [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).

**Audio quality issues**  
If a contact connects but has an audio *quality* problem—one-way audio, echo, choppy or robotic audio, or delay—see [Troubleshoot audio quality issues in Connect Customer](troubleshoot-audio-quality.md).

**Enable contact flow logs before the problem occurs**  
This page relies on contact flow logs, which exist only if the Set logging behavior block was enabled in the flow before the contact you're investigating ran. If an intermittent problem (for example, an occasional misroute) already happened while logging was off, you can't diagnose that specific contact from the logs. You can only enable logging and wait for the problem to recur. We recommend that you enable logging on your production flows proactively so the data is available when you need it. See [Flow block in Connect Customer: Set logging behavior](set-logging-behavior.md).

**Intended audience**  
This guide assumes you are a Connect Customer administrator who can manage routing profiles, queues, and contact flows, and who can access contact records (CTRs) and contact flow logs.

## Before you begin: gather this information
<a name="troubleshoot-routing-not-reached-before-you-begin"></a>

Collect the following for the affected contacts before you start. You use it both to isolate the problem and, if necessary, to open a case with AWS Support.
+ **Description of the symptom** – what happened (didn't reach the intended queue or agent, routed to the wrong queue, stuck in a queue, disconnected before reaching an agent, or uneven distribution) and the affected channel (voice, chat, task, or callback).
+ **Instance Amazon Resource Name (ARN)** – see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
+ **ContactId** of each affected contact (provide 3–5 examples).
+ **Time of occurrence**, including time zone (record in Coordinated Universal Time (UTC) where possible).
+ **Intended queue name, routing profile name, and agent** – both the routing target you expected and the actual values.
+ **Contact flow logs** for the affected contacts. Steps 3 and 4 rely on these logs to isolate the problem. For more information, see [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md).

**Prerequisites**  
Before you isolate the problem, confirm the basics: contact flow logging is enabled (see [Flow block in Connect Customer: Set logging behavior](set-logging-behavior.md)); the target queue is associated with a routing profile; the agent is assigned to that routing profile and is set to **Available**; and the security profile of the administrator who changes or deletes settings has the required permissions (for example, Edit and Delete for the Routing section).

## Step 1: Identify the symptom (quick reference)
<a name="troubleshoot-routing-not-reached-step1"></a>

The hub has a more complete symptom table. This table lists only the symptoms that the routing-configuration side handles. Use it to jump to the most likely cause.


| Symptom | Where to go | 
| --- | --- | 
| Contacts never reach a specific queue or agent, or get stuck in a queue | [Contacts never reach a specific queue or agent](#troubleshoot-routing-not-reached-not-reaching) | 
| Contacts are routed to the wrong queue | [Contacts are routed to the wrong queue (Set working queue)](#troubleshoot-routing-not-reached-wrong-queue) (for flow-block detail, see [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md)) | 
| Contacts aren't distributed according to queue priority, delay, or overflow | [Contacts aren't distributed according to priority, delay, or overflow](#troubleshoot-routing-not-reached-priority-delay) | 
| Contacts aren't distributed according to the specified skill or proficiency (skilled agents aren't preferred, or contacts don't wait) | [Contacts aren't distributed according to proficiency or skill (Set routing criteria)](#troubleshoot-routing-not-reached-proficiency) | 
| Contacts concentrate on one agent, or the distribution isn't as even as you expect | [Contacts concentrate on one agent, or the distribution isn't as even as you expect](#troubleshoot-routing-not-reached-distribution) | 
| Cross-channel routing doesn't deliver (for example, no voice contact arrives while an agent handles a chat) | [Cross-channel routing doesn't deliver](#troubleshoot-routing-not-reached-cross-channel) | 
| The CTR DisconnectReason is TELECOM\_PROBLEM, TELECOM\_BUSY, TELECOM\_NUMBER\_INVALID, TELECOM\_UNANSWERED, TELECOM\_TIMEOUT, or TELECOM\_POTENTIAL\_BLOCKING, ConnectedToSystemTimestamp is null together with one of these reasons, or a flow is wrong after number porting | Hub Step 5 (delegate to the boundary): [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md) | 

## Step 2: Determine the scope
<a name="troubleshoot-routing-not-reached-step2"></a>

The extent of the impact changes where you look first.
+ **A single agent** – suspect that agent's routing profile association and the agent's status (Available, Offline, or a custom status). See [Contacts never reach a specific queue or agent](#troubleshoot-routing-not-reached-not-reaching).
+ **A single queue or line of business (LOB)** – suspect that queue's configuration, the target contact flow's Set working queue, branching, or proficiency settings, and any Lambda function that references the queue. See [Contacts never reach a specific queue or agent](#troubleshoot-routing-not-reached-not-reaching) and [Contacts aren't distributed according to proficiency or skill (Set routing criteria)](#troubleshoot-routing-not-reached-proficiency).
+ **Multiple queues or organization-wide, or multiple symptoms at once with no customer-side change** – suspect an AWS service event, and review your service health notifications and the [AWS Health Dashboard](https://health.aws.amazon.com/health/status). If you don't see a related event but the symptoms persist across queues or sites, open a support case.

To size the impact, use real-time metrics to see how many agents are affected. To inspect one agent's activity and status in detail, use the agent activity audit report, which covers a single agent at a time. The [AgentHierarchyGroups](ctr-data-model.md#ctr-AgentHierarchyGroups) field in the contact record shows the hierarchy of the agent on an affected contact, which helps you correlate affected contacts to a team or location.

**Check for changes made on a specific date**  
If the issue started on a specific date across all affected agents, check for a routing configuration change, a service update, an external integration change (for example, Salesforce Service Cloud Voice omni-channel), or an agent authentication change made on that date.

## Step 3: Localize the problem using CTRs and contact flow logs
<a name="troubleshoot-routing-not-reached-step3"></a>

Routing troubleshooting uses **contact records (CTRs) and contact flow logs as the dividing line**. They help you determine whether the problem occurred inside Connect Customer routing, or outside it (carrier or device).

For the fields to read, how to draw conclusions from them, and the common pitfalls—Set working queue is determined by the QueueId ARN, not the display name, and the draft can differ from the published version—see the dedicated isolation reference, [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

Follow the conclusion from that page, then continue:
+ The contact enters the queue but isn't distributed to an agent → continue to [Step 4: Collect diagnostic data](#troubleshoot-routing-not-reached-step4) and [Step 5: Resolve the problem by cause](#troubleshoot-routing-not-reached-step5) on this page.
+ `DisconnectReason` of `TELECOM_PROBLEM`, `TELECOM_BUSY`, `TELECOM_NUMBER_INVALID`, `TELECOM_UNANSWERED`, `TELECOM_TIMEOUT`, or `TELECOM_POTENTIAL_BLOCKING` together with a null `ConnectedToSystemTimestamp` → a carrier or number problem. Confirm the `DisconnectReason` before you delegate: a null `ConnectedToSystemTimestamp` alone isn't a carrier signal. For a CALLBACK contact, it stays null until the customer answers (for example, while a queued callback is still waiting for an agent). See hub Step 5 (boundary), [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md).
+ A wrong QueueId ARN or an unexpected branch → a contact flow problem. See [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).

## Step 4: Collect diagnostic data
<a name="troubleshoot-routing-not-reached-step4"></a>

Run these in order. Use them to isolate cases where a contact doesn't reach an agent or a queue at all. For how to read each field, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

1. **Real-time metrics and the agent activity audit report** – check the target agent's status (Available, Offline, or a custom status) and when it changed. The agent activity audit report and the agent event stream show *when* the status changed, but not WHO changed it. To find who changed it, check CloudTrail for a `PutUserStatus` event at that time: a change that a supervisor makes in the real-time metrics report, or that an application makes through the API, is recorded there, while an agent's own status change in the CCP is not. The CCP logs show the agent's own client-side actions.

1. **`DescribeRoutingProfile` (API or CLI)** – check the queue associations, the per-channel concurrency, and the routing order (the API field is `AgentAvailabilityTimer`). You can also set the routing order in the console on the routing profile—see [Create a routing profile in Connect Customer to link queues to agents](routing-profiles.md).

1. **CloudTrail** – check for `UpdateContactFlowContent` (a misconfiguration from editing outside the UI).

1. **Contact flow logs** – check the QueueId ARN that the Set working queue block set, the `Results` of the Set routing criteria block, and the status of any Invoke Lambda block.

Then branch on what you found:
+ The agent doesn't appear for an eligible queue → [Contacts never reach a specific queue or agent](#troubleshoot-routing-not-reached-not-reaching) (quota or association).
+ Distribution doesn't match the specified skill or proficiency → [Contacts aren't distributed according to proficiency or skill (Set routing criteria)](#troubleshoot-routing-not-reached-proficiency).
+ A wrong QueueId ARN or an unexpected branch → [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).

## Step 5: Resolve the problem by cause
<a name="troubleshoot-routing-not-reached-step5"></a>

Find your cause in the following sections, then apply the resolution.

### Contacts never reach a specific queue or agent
<a name="troubleshoot-routing-not-reached-not-reaching"></a>

Check the following.
+ **Routing profile queue association** – confirm that the target queue is associated with the agent's routing profile and that the association is applied.
+ **Per-channel concurrency** – confirm that the target channel (for example, voice with a concurrency of 1) isn't already occupied by another contact.
+ **Queue-channel combination quota** – the **Queues per routing profile per instance** quota counts the number of queue-and-channel combinations, not the number of unique queues. The default value is 50, and queues that use manual assignment have a separate limit of the same size. Request a limit increase in Service Quotas. For the current defaults, see [Connect Customer service quotas](amazon-connect-service-limits.md).
+ **You can't perform an administrative action** (for example, you can't delete a queue)—the administrator's security profile might lack the permission. Enable the target action (for example, Delete) in the Routing section under **Users**, **Security profiles**.
+ **A dependency in the flow fails** – if the customer's Lambda function that determines the queue fails and breaks routing, see the Lambda dependency guidance in [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md). A call-level failure (a 500, throttling, or a timeout) takes the Error branch after retries, while a 404 or 503 that the function returns as a value takes the Success branch.

### Contacts are routed to the wrong queue (Set working queue)
<a name="troubleshoot-routing-not-reached-wrong-queue"></a>

Contacts are misrouted to a different queue—even when the UI looks correct—when the Set working queue change isn't applied to the flow (unpublished or stale), or when the display name doesn't match the actual QueueId ARN. Editing outside the UI with the `UpdateContactFlowContent` API can replace the ARN while leaving the display name unchanged. To fix a stale queue reference, open the block and re-select the queue, then save and publish. For detail, see the Set working queue guidance in [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md), and for the isolation procedure, see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md).

### Contacts aren't distributed according to priority, delay, or overflow
<a name="troubleshoot-routing-not-reached-priority-delay"></a>

Changing a queue's priority or delay in a routing profile changes the order in which agents are offered contacts. When two queues have different priorities and the same delay of 0, agents are offered contacts from the Priority 2 queue only when the Priority 1 queue has no contacts. When two queues have the same priority and different delays, a contact in the delayed queue is treated as the same priority once it ages past the delay. Before you reconfigure, review the examples in [Queue priority and delay examples to help you load balance Connect Customer contacts](concepts-routing-profiles-priority.md).

### Contacts aren't distributed according to proficiency or skill (Set routing criteria)
<a name="troubleshoot-routing-not-reached-proficiency"></a>

With proficiency-based (skills-based) routing, the following are common causes.
+ **All steps use timed expiry.** When every step expires, the contact becomes unconstrained and is distributed by standard queue routing, regardless of skill. Connect Customer first offers the contact to the agent who is handling the fewest contacts across all channels, and it compares how long each agent has been in **Available** status only to break a tie (the routing profile's Set routing order setting—the `AgentAvailabilityTimer` field in the API—determines whether outbound contacts reset this time). For more information about priority and delay, see [Queue priority and delay examples to help you load balance Connect Customer contacts](concepts-routing-profiles-priority.md). To keep the contact waiting for a skilled agent, set only the final step to **Never expire** (for example, steps 1–3 at 10s, 60s, and 60s, and step 4 at proficiency 1–5 with Never expire).
  + You can set **Never expire** only on the final step. If you set it on a non-final step, the configuration is rejected when you save it.
+ **A step's expiry is shorter than the ring timeout.** A voice contact is treated as not answered if it rings for 20 seconds with no answer (see [Isolate routing problems by using the contact record (CTR) and contact flow logs](sop-routing-ctr-flowlog.md), Section 4.5). When a step's expiry is shorter than that, the routing criteria advance to the next step before it is settled whether the first agent answered, so Connect Customer can't properly route the contact to the next most proficient agent when the first agent misses the call. The default queue-based routing then competes with proficiency-based routing, and distribution becomes inconsistent between the two methods.
+ **The overflow time is too short.** A setting that falls back to a non-skilled agent after, for example, 90 seconds sends contacts to non-skilled agents during busy periods. Consider extending the expiry time, adding multiple steps that lower the skill threshold gradually, using Never expire, or controlling routing explicitly with skill-specific queues.
+ **The contact was transferred into an agent queue.** Routing criteria has no effect when the contact is transferred into an agent queue. Route the contact to a standard queue for proficiency-based routing to apply.
+ **Set routing criteria isn't paired with Transfer to queue.** Use the Set routing criteria block with the Transfer to queue block: routing criteria take effect when the contact is transferred to a standard queue.

For more information, see [Flow block in Connect Customer: Set routing criteria](set-routing-criteria.md).

### Contacts concentrate on one agent, or the distribution isn't as even as you expect
<a name="troubleshoot-routing-not-reached-distribution"></a>
+ Connect Customer first offers the contact to the agent who is handling the fewest contacts across all channels, and compares how long agents have been in **Available** status only to break a tie. When agents are tied, routing prefers the agents that have been in **Available** status the longest (the routing profile's Set routing order setting—the `AgentAvailabilityTimer` field in the API—determines whether outbound contacts reset this time); contacts aren't spread evenly turn by turn. Under identical conditions, distribution can appear to concentrate on one agent. Each time an agent accepts a contact, that agent's availability timer resets and the agent moves to the end of the list, even when the agent has remaining concurrency.
+ What looks like concentration on one agent can be the result of the other agents not being truly Available (for example, remaining After call work (ACW)). When you test, confirm that every agent is truly Available with no ACW.
+ **ACW consumes a concurrency slot.** With a chat concurrency of 2, a second chat can still be delivered while one contact is in ACW. A slot with a contact in ACW is unavailable, but a free slot can still take a new contact (see the Availability metric in the real-time metrics report). If remaining ACW is skewing distribution, set the ACW timeout in the agent's user settings under **Contact handling**, separately per channel—see [Configure agent settings in Connect Customer](configure-agents.md).
  + If ACW continues for a long time, the contact doesn't become **Completed**. An ACW timeout resolves this.

### Cross-channel routing doesn't deliver
<a name="troubleshoot-routing-not-reached-cross-channel"></a>

If cross-channel concurrency is enabled but contacts still aren't delivered (for example, no voice contact arrives while an agent handles a chat), check for a missed contact that hasn't been cleared. For an agent configured for cross-channel concurrency, a missed contact must be cleared before contacts on other channels can be routed to that agent. Confirm that the cross-channel concurrency settings and the queue priority and delay match.

### Transfer and quick connect (routing side)
<a name="troubleshoot-routing-not-reached-transfer"></a>
+ A quick connect transfer needs a second concurrent call slot. If **Concurrent active calls per instance** is 1, internal transfers to a queue or agent fail. External transfers—a quick connect to an external phone number—aren't counted against this quota.
+ For which flows run for each type of quick connect, see [Quick connect scenarios for transferring contacts](how-quick-connects-work.md).
+ Outside the US, use a Connect Customer number as the outbound caller ID. Toll-free numbers are designed for national use, and in some countries (for example, Australia) a toll-free caller ID can be rejected. See [Toll-free numbers for caller ID](queues-callerid.md#tfn-callerid) and [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md).

### Callback, voicemail, and task (routing side)
<a name="troubleshoot-routing-not-reached-callback"></a>
+ The priority of the callback queue in the routing profile determines whether callbacks keep their place relative to inbound calls. At the same priority as the original inbound queue, Connect Customer offers the oldest call first across both queues, using the original call start time, so a callback keeps its position. At a lower priority, agents are offered callbacks only after contacts in the higher-priority inbound queue—unless a delay is set, in which case a contact that ages past the delay is treated as the higher priority. See [Set up queued callback by creating flows, queues, and routing profiles in Connect Customer](setup-queued-cb.md) and [Queue priority and delay examples to help you load balance Connect Customer contacts](concepts-routing-profiles-priority.md).
+ For an example architecture that schedules callbacks within your hours of operation, see the callback section in [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md).
+ In customer-first callback mode, Connect Customer dials the customer before an agent is confirmed available; agent-first callback mode (the default) offers the callback to an agent first. If callbacks are dialing customers when no agent is ready, confirm which dial mode the Transfer to queue block uses. See [Set up queued callback by creating flows, queues, and routing profiles in Connect Customer](setup-queued-cb.md).

## Step 6: Isolate carrier, device, or audio problems (boundary)
<a name="troubleshoot-routing-not-reached-step6"></a>

Most of the following are outside Connect Customer routing and flow configuration. Confirm the cause, then delegate or open a support case. These include a `DisconnectReason` of `TELECOM_PROBLEM`, `TELECOM_BUSY`, `TELECOM_NUMBER_INVALID`, `TELECOM_UNANSWERED`, `TELECOM_TIMEOUT`, or `TELECOM_POTENTIAL_BLOCKING` together with a null `ConnectedToSystemTimestamp` (as Step 3 notes, a null `ConnectedToSystemTimestamp` on its own isn't a carrier signal), a wrong flow after number porting, an unclaimed number, or a difference in the audio experience. The hub collects the boundary delegation targets in its Step 5, [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md).
+ **Carrier or number causes** – see the hub Step 5 (boundary), [Step 5: Delegate boundary issues (carrier, device, audio, or disconnect)](troubleshoot-contact-routing.md#troubleshoot-contact-routing-step5). Confirm coverage and number-type restrictions in the [Amazon Connect Telecoms Coverage guide](https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf) on the Amazon Connect website.
+ **A difference in the audio experience** (for example, continuous ringing)—see [Troubleshoot audio quality issues in Connect Customer](troubleshoot-audio-quality.md).
+ **Unexpected disconnects after routing** – see [Troubleshoot call disconnects by using DisconnectDetails in the contact record](troubleshoot-call-disconnects.md).

## Before you contact AWS Support
<a name="troubleshoot-routing-not-reached-before-support"></a>

If the issue persists after troubleshooting, open a case with **3–5 examples**, and include:
+ Instance ARN and a description of the symptom (didn't reach, wrong queue, stuck, disconnected, or uneven distribution, and the affected channel).
+ ContactIds, timestamps (UTC), and a contact-record snapshot (including `DisconnectReason`, `Queue`, `Agent`, `ConnectedToSystemTimestamp`, and `InitiationMethod`).
+ The target contact flow export (JSON) and the configuration of the routing profile, queue, and proficiency (Set routing criteria).
+ The contact flow logs for the affected contact ids.
+ The extent of the impact (single agent, single queue, or organization-wide) and the date and time the issue started (UTC).
+ If you suspect a carrier cause: the source and destination numbers (the last 4 digits can be masked) and the times and ContactIds the carrier needs to investigate.
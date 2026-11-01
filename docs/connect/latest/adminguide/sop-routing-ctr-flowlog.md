

# Isolate routing problems by using the contact record (CTR) and contact flow logs
<a name="sop-routing-ctr-flowlog"></a>

The contact record (CTR) and contact flow logs are the **dividing line** that tells you whether a routing or contact-handling problem occurred inside Connect Customer (routing configuration and contact flows) or outside it (carrier or device). This is the same approach that audio quality troubleshooting uses when it treats the call recording as the dividing line. This page shows you which fields to read, what to conclude from them, and where to go next.

**Intended audience**  
This reference assumes you are a Connect Customer administrator who can access contact records (CTRs) and contact flow logs and who can run APIs and CLI commands such as `DescribeContact`.

Use this reference as follows:

1. You arrive here from a step in the routing troubleshooting hub or one of its spokes.

1. You read the relevant fields in Section 1 (the CTR) and Section 2 (contact flow logs).

1. You use the dividing-line conclusion table in Section 3 to decide which page to go to next.

1. If a reading doesn't match what you expected, you check the isolation pitfalls in Section 4.

## Section 1: Fields to read in the contact record (CTR) with DescribeContact
<a name="sop-routing-ctr-flowlog-ctr"></a>

Call [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html), or review the contact records that you stream to Kinesis, and check the following fields. For the field definitions, see [Data model for Connect Customer contact records](ctr-data-model.md).

### 1.1 `DisconnectReason`
<a name="sop-routing-ctr-flowlog-disconnectreason"></a>

Read this field first to isolate where the disconnect occurred. Each value points in a different direction.


| `DisconnectReason` | What it indicates | Where to look next | 
| --- | --- | --- | 
| TELECOM\_PROBLEM, TELECOM\_BUSY, TELECOM\_NUMBER\_INVALID, TELECOM\_UNANSWERED, or TELECOM\_TIMEOUT | A destination or carrier cause on the PSTN side (a third-party network problem, a busy destination, an invalid destination number, an unanswered destination, or a network timeout). You can't resolve these with Connect Customer routing or flow configuration. | Rule out Connect Customer-side configuration first, then confirm coverage and number-type restrictions and open a support case if needed; see [Step 5: Delegate boundary issues (carrier, device, audio, or disconnect)](troubleshoot-contact-routing.md#troubleshoot-contact-routing-step5). | 
| TELECOM\_POTENTIAL\_BLOCKING | Possible spam or reputation blocking by the destination carrier. AWS can't unblock carrier networks for you. | Review your outbound calling practices; see [Optimize your reputation for outbound calling in Connect Customer](optimize-outbound-calling.md). | 
| TELECOM\_ORIGINATOR\_CANCEL | An originating-side cause. For inbound calls, the caller cancelled before connecting to Connect Customer (often within a second or two). For outbound calls, either the destination didn't answer—in which case Connect Customer sends the cancel after about a 60-second timeout, not a carrier fault—or the agent or API cancelled before connecting. The about-60-second timeout applies only to the outbound-unanswered case. | Check the destination path. For an outbound transfer, review the Transfer to phone number block Timeout; see [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md). | 
| CONTACT\_FLOW\_DISCONNECT | The flow ended the contact. | In the flow log, identify the terminal block that the contact reached—a Disconnect block, or an End flow / Resume block in an inbound or disconnect flow—and which branch routed to it. Then see [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md). | 
| CUSTOMER\_DISCONNECT | The caller disconnected. In most cases this isn't a flow or routing problem. | The customer side | 
| AGENT\_DISCONNECT | For voice contacts, the agent side of the call initiated the disconnect after the customer and agent were connected. This value identifies which side disconnected, not why. The [Data model for Connect Customer contact records](ctr-data-model.md) notes that CUSTOMER\_DISCONNECT can't distinguish poor reception from deliberate disconnection; treat AGENT\_DISCONNECT the same way. | For uneven distribution or contacts that don't reach an agent, see [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md). To determine whether a media or device problem caused the disconnect, check the DisconnectDetails section of the contact record: a PotentialDisconnectIssue of AGENT\_CONNECTIVITY\_ISSUE or AGENT\_DEVICE\_ISSUE identifies an agent-side network or workstation cause. See [Troubleshoot call disconnects by using DisconnectDetails in the contact record](troubleshoot-call-disconnects.md). Also compare with the agent activity audit report and the agent's status and activity state (see the agent audit report pitfall in [Section 4: Isolation pitfalls](#sop-routing-ctr-flowlog-blindspots)). | 
| OTHER | For voice contacts, OTHER covers disconnect reasons that the preceding codes don't address—for example, a disconnect that an API call initiates. Chat doesn't use OTHER: a reason outside its documented list is recorded as null. Chat, task, and email have a distinct API code. | Confirm which disconnect reasons apply to the channel in [Data model for Connect Customer contact records](ctr-data-model.md). Because OTHER doesn't identify the disconnecting party, isolate from the other fields in this section (ConnectedToSystemTimestamp, Queue, and Agent) and from the flow logs in Section 2. | 

### 1.2 `ConnectedToSystemTimestamp`
<a name="sop-routing-ctr-flowlog-connectedtimestamp"></a>
+ `null`—for an outbound, callback, or API contact, the customer endpoint never answered. This often occurs together with a `TELECOM_*` `DisconnectReason`, but not always: when the call was never placed at all—for example, an outbound campaign contact that reports `OUTBOUND_ATTEMPT_FAILED` or `OUTBOUND_PREVIEW_DISCARDED`, or a call blocked by country allowlisting, a quota, or a missing outbound caller ID—this field is also `null`. Read `DisconnectReason` and this field together rather than inferring one from the other, and confirm which reasons apply to the contact type in [Data model for Connect Customer contact records](ctr-data-model.md).
+ A value is present—what this means depends on `InitiationMethod`:
  + For `OUTBOUND`, `CALLBACK`, and `API`, the customer endpoint answered, so the contact reached Connect Customer. Continue isolating the problem inside Connect Customer (routing or flow).
  + For `INBOUND`, this timestamp matches the initiation timestamp—the time the contact arrived—so a value being present carries no information about the far end and does not rule out an outside cause.

  Check `DisconnectReason` first: a `TELECOM_*` reason points outside Connect Customer even when this timestamp is present. For other initiation methods (for example, `TRANSFER` or `QUEUE_TRANSFER`), see [Data model for Connect Customer contact records](ctr-data-model.md).

### 1.3 `Queue` and `Agent`
<a name="sop-routing-ctr-flowlog-queue-agent"></a>

Read these two fields together: `Queue` is present only if the contact was queued, and `Agent` is present only if the contact was connected to an agent. The combination tells you how far the contact got.


| `Queue` | `Agent` | What it indicates | 
| --- | --- | --- | 
| Present | Present | The contact was queued and connected to an agent. Compare the queue and agent with the routing target you expected—a different queue points to misrouting (see the Set working queue pitfall in [Section 4: Isolation pitfalls](#sop-routing-ctr-flowlog-blindspots) and [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md)). | 
| Present | Absent | The contact reached the queue but was never connected to an agent. Read DisconnectReason before you conclude this is a routing problem: CUSTOMER\_DISCONNECT means the customer hung up while waiting (an abandoned contact rather than a misconfiguration; see [Data model for Connect Customer contact records](ctr-data-model.md)). Other reasons point to routing configuration. | 
| Absent | Absent | The contact never reached a queue. Look upstream in the flow—the contact was disconnected, or it never reached a Transfer to queue block. Use the flow logs in Section 2. | 
| Absent | Present | The contact wasn't routed through a queue. Check InitiationMethod: MONITOR produces this shape (see [1.4 `InitiationMethod`](#sop-routing-ctr-flowlog-initiationmethod)). | 

### 1.4 `InitiationMethod`
<a name="sop-routing-ctr-flowlog-initiationmethod"></a>

This field shows how the contact was established. For the flow types associated with each initiation method, see [Contact initiation methods and flow types in your Connect Customer contact center](contact-initiation-methods.md).
+ Use it to confirm that a contact for a specific path (for example, `CALLBACK_CUSTOMER_FIRST_QUEUED`) was created at all.
+ `MONITOR` indicates a monitoring contact, which Connect Customer records separately from the contact that the supervisor monitored. On this contact record:
  + The Agent field describes the supervisor, not the agent who handled the customer. StateTransitions confirms this—it records the state transitions of a supervisor, with a state of `SILENT_MONITOR` or `BARGE`.
  + `Queue` is null, because the contact wasn't routed through a queue.
  + `InitialContactId` and `PreviousContactId` point to the monitored contact, so you can trace back to it.

  Use this to isolate reports that the agent field isn't what you expected.

### 1.5 `InitialContactId` and `PreviousContactId`
<a name="sop-routing-ctr-flowlog-contactids"></a>
+ `InitialContactId` and `PreviousContactId` are both `null`—this contact wasn't created from another contact. `InitialContactId` names the first contact in a chain; it isn't set to the contact's own id, so a contact that is itself the first one leaves it empty. To check whether another contact was created from this one—for example, a transfer destination—read `NextContactId`. Use all three together to isolate duplicate inbound contacts from a single contact that produced a second record. Each genuinely duplicated inbound contact is its own standalone record—both `InitialContactId` and `PreviousContactId` are `null` and it has no `NextContactId`—so duplicated inbound contacts each appear as a separate standalone record, distinct from one contact that produced a second record through a transfer.
+ `PreviousContactId` or `NextContactId` has a value—the contact is part of a chain. Connect Customer sets both fields for the same events: an agent using a quick connect or the CCP number pad, a Transfer to flow, Transfer to queue, or Set disconnect flow block running, or an additional WebRTC participant being added. `PreviousContactId` names the contact this one came from; `NextContactId` names the contact created from this one.
+ Follow the chain. For example, a customer first callback spans three contacts: the inbound customer contact (C1), the queued callback contact (C2, with the initiation method `CALLBACK_CUSTOMER_FIRST_QUEUED`), and the dialed callback contact (C3, with `CALLBACK_CUSTOMER_FIRST_DIALED`). Each retry creates another dialed callback contact. See [Use customer first callback mode in Connect Customer](customer-first-cb.md).

## Section 2: Items to read in contact flow logs (CloudWatch)
<a name="sop-routing-ctr-flowlog-flowlogs"></a>

With contact flow logs enabled, reproduce the problem, and then download the logs for the affected ContactId. For how to retrieve them, see [Search flow logs stored in an Amazon CloudWatch log group](search-contact-flow-logs.md) and [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md).

Read these main items:
+ **The block execution order, and the `Results` on the blocks that report one** – `Success`, `Timeout`, `Error`, a branch name, or an exception message from the block. Not every block reports a `Results`; many emit only an entry line with their parameters. Treat a missing `Results` as "this block doesn't report one," not as a gap in the log. Identify unexpected branches and the point where the flow ended the contact. A single flow log line can contain both a Parameters object and a Results object; the two are not always on separate lines.
+ **The QueueId ARN that Set working queue set** – routing is determined by the **QueueId ARN, not the display name**. Compare the ARN in the log with the `describe-queue` output to confirm it's the intended queue (see also the pitfall in [Section 4: Isolation pitfalls](#sop-routing-ctr-flowlog-blindspots)).
+ **The response status of Invoke AWS Lambda function**. The Invoke AWS Lambda function block has `Success` and `Error` branches (and a `Timeout` branch in synchronous mode); it has no default branch. Read the response status in two separate categories rather than as one flat list. A call-level failure—a `500`, throttling, or a timeout—is retried by Connect Customer (up to three times, up to the configured Timeout) and then takes the `Error` branch. A `404` or `503` that the function returns as a value means the invocation itself succeeded, so the block takes the `Success` branch. These codes are the customer's Lambda function responses, not Connect Customer-defined log fields. Where the contact goes next depends on how the flow author wired the branch.
+ **The Loop count** – a high `LoopCount` can mean a no-input menu repeated until the contact disconnected (`CONTACT_FLOW_DISCONNECT`), making the call abnormally long.

### 2.1 When a transferred contact produces no logs
<a name="sop-routing-ctr-flowlog-external-outbound"></a>

A transfer produces no contact flow logs for the child contact for two different reasons. Confirm which case you are in before you conclude that logging is misconfigured.
+ **`EXTERNAL_OUTBOUND`** – a quick connect transfer to an external phone number, or the Transfer to phone number block. No flow type is associated with this initiation method, so the child contact runs no flow and produces no contact flow logs. There is nothing to enable. A missing record here is itself a signal, not a logging misconfiguration.
+ **`TRANSFER`** – an agent transfer through a CCP quick connect to an agent or queue. This creates a **new contact record**, and the transfer-destination flow (for example, the agent transfer flow) needs its own [Flow block in Connect Customer: Set logging behavior](set-logging-behavior.md) block for the child contact to emit logs. Logging is a per-contact state: within one contact it carries into the queue, whisper, and hold flows, but it does not carry into a separate (child) contact.

### 2.2 Retrieve all flow logs for a specific ContactId
<a name="sop-routing-ctr-flowlog-retrieve-all"></a>

To retrieve every block log for a specific ContactId without gaps, query CloudWatch Logs Insights with the ContactId as the key. Common reasons that logs aren't found are that Set logging behavior is disabled in the target flow, that logging isn't enabled in the flow for a child contact (the transfer destination), or that you're searching the wrong log group or time range.

## What a healthy contact looks like
<a name="sop-routing-ctr-flowlog-healthy"></a>

Before you look for an abnormal reading, know the baseline. The following annotated examples show a normal inbound voice contact that queued and connected to an agent. Values are examples.

**Contact record (CTR)** – only the relevant fields are shown:

```
{
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Channel": "VOICE",
    "InitiationMethod": "INBOUND",
    "DisconnectReason": "CUSTOMER_DISCONNECT",
    "ConnectedToSystemTimestamp": "2026-01-15T10:00:03Z",
    .
    .
    "Queue": {
        "Name": "BasicQueue"
    },
    "Agent": {
        "Username": "Agent1"
    },
    "InitialContactId": null,
    "NextContactId": null,
    "PreviousContactId": null
}
```

In this healthy reading:
+ `ConnectedToSystemTimestamp` is present, so the contact reached Connect Customer.
+ `Queue` and `Agent` are both present, so the contact was queued and connected to an agent.
+ `DisconnectReason` is `CUSTOMER_DISCONNECT`—a normal end (the customer hung up), not a routing fault.

**Contact flow log** – the Set working queue block logs an entry line that records the QueueId ARN it set:

```
{
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "ContactFlowModuleType": "SetQueue",
    "Timestamp": "2026-01-15T10:00:05.581Z",
    "Parameters": {
        "Queue": "{{queue-arn}}"
    }
}
```

A block that reports an outcome adds a result line. In a healthy flow, the `Results` value is `Success` (not `Timeout` or `Error`):

```
{
    "Results": "Success",
    "ContactId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "ContactFlowModuleType": "{{block-type}}",
    "Timestamp": "2026-01-15T10:00:06.012Z"
}
```

Confirm that the `Queue` ARN matches the queue you intended (see the Set working queue pitfall in [Section 4: Isolation pitfalls](#sop-routing-ctr-flowlog-blindspots)), that the blocks ran in the order you expect, and that no block reports `Timeout` or `Error`. Use this baseline when you compare a successful contact with a failed one. For the full set of contact record fields, see [Data model for Connect Customer contact records](ctr-data-model.md); for more flow-log examples, see [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md).

## Section 3: Dividing-line conclusion table—go from observation to next step
<a name="sop-routing-ctr-flowlog-conclusion"></a>

Use the following table to map what you read in Sections 1 and 2 to a destination.


| Observation (CTR or flow log) | Where the problem is | Where to go next | 
| --- | --- | --- | 
| DisconnectReason is TELECOM\_PROBLEM, TELECOM\_BUSY, TELECOM\_NUMBER\_INVALID, TELECOM\_UNANSWERED, TELECOM\_TIMEOUT, or TELECOM\_POTENTIAL\_BLOCKING, or ConnectedToSystemTimestamp is null for a contact that was dialed but not answered—a queued callback that was never dialed also has a null value (see Section 1.2) | Destination or carrier (outside Connect Customer); for TELECOM\_POTENTIAL\_BLOCKING, carrier spam or reputation blocking | Rule out Connect Customer-side configuration first, then confirm coverage and number-type restrictions and open a support case if needed; see [Step 5: Delegate boundary issues (carrier, device, audio, or disconnect)](troubleshoot-contact-routing.md#troubleshoot-contact-routing-step5). For spam or reputation blocking, see [Optimize your reputation for outbound calling in Connect Customer](optimize-outbound-calling.md). | 
| DisconnectReason is TELECOM\_ORIGINATOR\_CANCEL | Originating side. For inbound calls, the caller cancelled before connecting to Connect Customer (often within a second or two). For outbound calls, the destination didn't answer (Connect Customer sends the cancel after about a 60-second timeout, which applies only to this outbound-unanswered case), or the agent or API cancelled before connecting | Check the destination path. For an outbound transfer, review the Transfer to phone number block Timeout; see [Flow block in Connect Customer: Transfer to phone number](transfer-to-phone-number.md). | 
| After porting, inbound calls flow into the contact flow of a different number (the number the customer dialed and the contact record's SystemEndpoint.Address—shown as System address or number in contact search—don't match) | Carrier number mapping | See [How to port your numbers to Connect Customer](about-porting.md). | 
| The contact enters the queue but isn't distributed to an agent, and DisconnectReason isn't CUSTOMER\_DISCONNECT | Routing configuration (routing profile association or concurrency) or the agent's status (Available, Offline, or a custom status). | [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md) | 
| The contact never reached a queue (Queue is absent) | The flow—the contact was disconnected, or never reached a Transfer to queue block | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) | 
| DisconnectReason=CONTACT\_FLOW\_DISCONNECT, an unexpected branch, or a wrong QueueId ARN | Contact flow (block behavior, branching, Set working queue, or a dependent Lambda) | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) | 
| Invoke Lambda returns an error or an unexpected value, and the Error or No Match branch isn't wired to the intended queue | The flow (Lambda integration and the Error / No Match branch wiring) | [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md) | 
| The problem occurs across multiple queues or sites at once, with no customer-side change | An AWS service event or a Regional service issue | Check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status) and any service health notifications. If none matches but the problem persists, open a support case. | 

## Section 4: Isolation pitfalls
<a name="sop-routing-ctr-flowlog-blindspots"></a>

These are points that are easy to misread. When a reading doesn't match what you expected, check here first.

4.1 The draft isn't the same as the published version (unpublished changes)  
The visual editor shows the **draft**; the contact runs the **published version**. These can differ when a draft change (for example, a Set working queue change) was never published. For a flow that has been published, [DescribeContactFlow](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContactFlow.html) returns the published version by default, and returns the draft when you pass the `:$SAVED` alias. Retrieve both and compare them to find unpublished changes; if they differ, republish from the UI. The flow `Status` field (`PUBLISHED` versus `SAVED`) does not indicate whether there are unpublished draft changes—a flow can be `PUBLISHED` yet still have a newer draft. A `Status` of `SAVED` means that the flow has never been published.

4.2 Set working queue is determined by the QueueId ARN, not the display name (out-of-UI edits can leave the display name stale)  
When you update a flow through the [UpdateContactFlowContent](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactFlowContent.html) API or an import, the QueueId ARN can be replaced while the display name in the UI stays the same. The UI looks correct, but the contact is misrouted to a different queue. Compare the ARN in the exported JSON with `describe-queue`. To fix a stale queue reference, open the block and re-select the queue, and then save and publish.

4.3 Detect out-of-UI edits (CloudTrail `UpdateContactFlowContent`)  
When behavior changed on a specific date after previously working, check CloudTrail for [UpdateContactFlowContent](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactFlowContent.html) calls. A UI edit is recorded with `invokedBy` = `connect.amazonaws.com` and a principal that is the service-linked role `AWSServiceRoleForAmazonConnect` (its `userAgent` is also `connect.amazonaws.com`). An event with no `invokedBy` is a direct out-of-UI call (API, import, CI/CD, CloudFormation, or Lambda), and its `userIdentity.type` can be either `IAMUser` or `AssumedRole`. Note the exception: events from the service-linked role `AWSServiceRoleForAmazonConnectSynchronization` are Connect Customer managed cross-Region synchronization, not a UI edit.

4.4 A transfer from an upstream carrier or PBX doesn't create a CTR until it reaches a phone number claimed in your Connect Customer instance  
A call transferred from an upstream carrier or PBX creates a `SearchContacts` entry and a CTR **only after it reaches a phone number claimed in your Connect Customer instance**. A call that fails before that point leaves no record in Connect Customer. Interpret "no record" as possibly meaning "the call failed before it reached Connect Customer."

4.5 The agent audit report status and the 20-second no-answer timeout  
The Agent Activity Audit report distinguishes **Agent Disconnected**, **Contact Missed**, and **Rejected**. For voice, a contact that isn't answered and a contact that is rejected are both recorded as **Agent Disconnected**. For chat, both are recorded as **Contact Missed**. For task and email, a contact that isn't answered is recorded as **Contact Missed**, and a rejected contact is recorded as **Rejected**. For details, see [When is the status Agent Disconnected, Contact Missed, or Rejected?](agent-activity-audit-report.md#rejected-missed-disconnected). The time an available agent has to answer before the contact is counted as not answered is 20 seconds for voice or chat, and 30 seconds for a task. This ring time is fixed and can't be configured. A contact that isn't answered is routed to the next available agent.  
Because the audit report records both a no-answer and a reject as **Agent Disconnected** for voice (and both as **Contact Missed** for chat), the audit report status alone can't separate a missed contact from a rejected one on those channels. To distinguish them, use the Contact State in the agent event stream, where `MISSED` and `REJECTED` are separate states (`REJECTED` also covers a customer who abandoned the contact while it was connecting to the agent); the audit report is a report version of the same data. Read the CTR `DisconnectReason` together with these signals.

## Related topics
<a name="sop-routing-ctr-flowlog-related"></a>
+ Hub: [Troubleshoot contact routing and handling in Connect Customer](troubleshoot-contact-routing.md)
+ Spoke: [Troubleshoot contacts that are not routed, misrouted, or not reaching an agent in Connect Customer](troubleshoot-routing-not-reached.md)
+ Spoke: [Troubleshoot contact flows that don't behave as expected in Connect Customer](troubleshoot-contact-flow-behavior.md)
+ [Data model for Connect Customer contact records](ctr-data-model.md)
+ [Search flow logs stored in an Amazon CloudWatch log group](search-contact-flow-logs.md), [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md), and [Flow block in Connect Customer: Set logging behavior](set-logging-behavior.md)
+ [Flow block in Connect Customer: Set disconnect flow](set-disconnect-flow.md)
+ [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html)
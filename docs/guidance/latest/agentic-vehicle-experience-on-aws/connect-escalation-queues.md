

# Escalation by priority
<a name="connect-escalation-queues"></a>

Escalation follows the P0–P3 criticality taxonomy. The deterministic classifier sets the level from vehicle state (active DTCs, telemetry thresholds, open recalls), and the language model cannot set or change it.


| Priority | Meaning | Escalation behavior | Human handoff timing | 
| --- | --- | --- | --- | 
|  **P0 — Stop driving**  | Safety-critical: brake failure, airbag fault, overheating, loss of steering assist | The safety instruction ("pull over when it is safe to do so") comes first, automatically and word for word. The driver is then offered a chat with the tenant’s support queue, at high priority, and roadside assistance, each one tap. `escalation.autoOpenHumanChatOnP0` makes the chat automatic. The LLM cannot downgrade a deterministic P0 classification. | Offered immediately; one tap by the driver, or automatic if the tenant opts in | 
|  **P1 — Service now**  | Active fault code with degradation risk within 24–48 hours | The supervisor recommends service and creates a STAR ticket. The card offers **Talk to an agent**. | Offered with the recommendation; the driver may decline | 
|  **P2 — Service soon**  | Non-critical fault, wear indicator, or open recall | The supervisor creates a STAR ticket; no card. A driver who asks for a person gets a service escalation. Most P2 conversations resolve autonomously. | On request | 
|  **P3 — Monitor**  | Informational; documented reset condition | No escalation card. The supervisor explains the condition and closes the session. | On request | 

## P0 safety invariant
<a name="p0-safety-invariant"></a>

The P0 safety rule is a hard invariant on the classification and the safety instruction, not on the handoff. When the triage classifier returns P0, the platform sends the stop-driving instruction to the driver word for word, and the language model cannot soften, restate or withhold it. The escalation itself is recommended: the app shows a card with **Request roadside** and **Talk to an agent**, and the driver’s tap reaches `/escalate`, which opens a chat on the tenant’s chat queue with the triage context attached. Roadside dispatch sends physical equipment and false-positive P0s exist (sensor faults), so the driver confirms it; a human chat is a channel choice. Tenants whose duty-of-care rules require a human on the line immediately set `escalation.autoOpenHumanChatOnP0`, and those that require a truck on every P0 set `escalation.autoRequestRoadsideOnP0`. Both default to `false`.

Even if the supervisor’s language model assigns low confidence to the P0 finding, the classification stands. Downgrading a safety classification is a human decision, not an LLM judgment.

## What `/escalate` checks before a P0 side effect
<a name="connect-p0-side-effects"></a>

 `POST /escalate` sits behind a Cognito authorizer. The request body carries `severity`, `vin`, `vehicleId` and `driverId`, and the Lambda function treats all four as untrusted. The chat opens at every severity, but the two P0 side effects, a roadside request and a callback, happen only when all of these hold:
+  `triageSessionId` names a recent P0 decision the platform recorded for this tenant and VIN; the body’s `severity` alone is not enough.
+ The CMS vehicles row for `vehicleId` carries that VIN.
+  `driverId` is the driver assigned to that vehicle, matching the caller’s `custom:driverId` claim.

A verified P0 roadside request writes a `REQUESTED` row to `vsa-{stage}-rsa-dispatch`, with the vehicle’s position when it is fresh; the app polls `GET /rsa/dispatch/{dispatchId}` for its status. A failed roadside request or callback never stops the chat from opening.

## P0 callback
<a name="connect-p0-callback"></a>

If the tenant configures `escalation.callback`, Amazon Connect also calls the assigned driver’s registered phone number on a verified P0, so the driver reaches a person even if they lose the chat. The number dialed comes from the driver’s record, never from the request. Service escalations never call.

The callback needs a contact flow of type **Contact flow (inbound)**, which `StartOutboundVoiceContact` runs once the driver answers, and a caller ID: a queue with an outbound caller-ID number (`queueArn`) or a claimed number (`sourcePhoneNumber`). `/escalate` places the call before it starts the chat. Because Connect offers an agent one contact at a time, `escalation.callback.chatContactFlowId` names a chat flow that routes to a queue with a routing-profile delay, so the agent is offered the call first. `scripts/connect-p0-call-first.py` creates that queue and flow; it is a dry run unless `--apply` is given.

```
"escalation": {
  "tier2QueueArn": "arn:aws:connect:<region>:<account-id>:instance/<instance-id>/queue/<chat-queue-id>",
  "autoOpenHumanChatOnP0": false,
  "autoRequestRoadsideOnP0": false,
  "callback": {
    "contactFlowId": "<inbound-type-callback-flow-id>",
    "queueArn": "arn:aws:connect:<region>:<account-id>:instance/<instance-id>/queue/<callback-queue-id>",
    "sourcePhoneNumber": "<claimed-number-E.164>",
    "chatContactFlowId": "<delayed-chat-flow-id>"
  }
}
```

Write the change as a new tenant config version and repoint `current`; the table is pointer-to-version, so rollback is one flip.
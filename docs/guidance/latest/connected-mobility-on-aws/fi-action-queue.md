

# Fleet Intelligence Action Queue
<a name="fi-action-queue"></a>

The three Fleet Intelligence features share one Action Queue. Their agents run in the companion Agentic Vehicle Experience (AVX) accelerator as Tier 2 components: each runs on a schedule or an event, with nobody waiting, and writes its recommendations to AVX’s findings table. Operator and rule decisions are AVX Actions. CMS reads both and renders the queue screens, the overview’s Action Queue summary and the Agent activity feed. No agent reasons inside a chat turn; an operator’s question about a recommendation goes to the fleet assistant, which reads the stored recommendation and its evidence.

Each feature splits its work three ways:


| Layer | Built from | Does | 
| --- | --- | --- | 
| Data and predictions | Flink processors, Redis, Athena, SageMaker models, deterministic recall and warranty rules | Measures cost, utilization and recall exposure, and scores anomalies, demand and degradation. | 
| Reasoning | An AVX Tier 2 agent on Amazon Bedrock with tools and the ADP knowledge base | Decides what the numbers mean for this fleet, which action to take, and what it is worth. | 
| Approval | The Action Queue, per-fleet rules and four guardrails | Decides whether an action runs, and records who decided. | 


| Agent |  `agent_id`  | Recommendation kinds | 
| --- | --- | --- | 
| Cost |  `agent-fi-cost`  |  `fleet.cost.anomaly`, `fleet.cost.sell_timing`  | 
| Recall and warranty |  `agent-fi-recall-warranty`  |  `fleet.recall.vehicle`, `fleet.warranty.claim_candidate`  | 
| Rebalancing |  `agent-fi-rebalancing`  |  `fleet.rebalance.move`  | 

## The recommendation record
<a name="fi-aq-record"></a>

Each recommendation is a Finding in `vsa-{stage}-avx-findings`, written through AVX’s `write_finding()` helper. It carries the Tier 2 artifact fields (`computed_at`, `confidence`, `evidence[]`, `agent_version`, `inputs_hash`) and a `recommended_action`: the action kind, its target system, its parameters, and the estimated saving or recovery with its basis.
+  **Scope.** A recommendation about one vehicle is VIN-scoped and also indexed under the vehicle’s fleet. A recommendation that spans vehicles or locations, such as a rebalancing move, is fleet-scoped: the vehicles are listed in the evidence and the locations in the action’s parameters.
+  **Several per fleet.** A `subject_key` distinguishes recommendations of the same kind for one fleet, so a fleet can hold three open moves at once.
+  **No duplicates.** Re-running an agent on the same inputs updates the open recommendation in place.

## Status
<a name="fi-aq-status"></a>


| Status | Meaning | 
| --- | --- | 
| Pending | The recommendation is live and no one has decided. | 
| Approved | The operator approved the recommended action as proposed. | 
| Overridden | The operator approved with different parameters. AVX compares the parameters itself; the screen does not declare an override. | 
| Auto-approved | A fleet rule approved it. | 
| Executed | The target system completed the action. | 
| Rejected | The operator declined it, with an optional reason. | 
| Blocked | A guardrail refused it. The audit trail names the guardrail. | 
| Failed | The target system could not be reached or refused the request as malformed. | 
| Expired | The recommendation passed its expiry with no decision. | 

Every decision records who made it: the operator, identified from their verified token, or the rule, identified by fleet and rule ID.

## Approvals and auto-approval rules
<a name="fi-aq-approvals"></a>

The screens call the CMS Fleet Intelligence API at `/api/v1/fleet-intelligence/actions`. CMS checks that the operator can act on the fleet and passes the decision to AVX, which records it and dispatches the action. A `fleet-viewer` sees the queue but cannot approve.

Auto-approval rules are per-fleet configuration:
+ Each rule names one action kind and its limit, for example the largest transfer cost a move may have.
+ A fleet with no rules auto-approves nothing, and a new rule is created disabled.
+ Limit defaults come from configuration, not code.
+ A rule for a guarded action kind is refused.

A rule evaluator reads new recommendations from the findings table’s DynamoDB stream. When a fleet’s enabled rule matches and the recommendation is within the limit, it records an auto-approved Action and dispatches it. Replaying a stream record adds nothing.

## Guardrails
<a name="fi-aq-guardrails"></a>

Four checks run in AVX’s dispatch path, which every approved Action passes through, before any target system is called. No rule overrides them, and each is pinned by a test that fails when the check is removed.


| Guardrail | Check | 
| --- | --- | 
| A safety recall is never auto-exempted. |  `exempt_recall` needs an operator decision. | 
| Grounding a vehicle needs the operator. |  `ground_vehicle` needs an operator decision. | 
| Sending a warranty claim needs the operator. |  `submit_warranty_claim` needs an operator decision. | 
| A recall is never marked complete without a service record. |  `complete_recall` needs a completed service record for the vehicle, whoever decided. | 

A missing or malformed decision record counts as "not an operator". A refused Action is recorded as blocked and never reaches a target system.

## Execution
<a name="fi-aq-execution"></a>


| Action kind | Target | Effect | 
| --- | --- | --- | 
|  `book_recall_service`  | DMS | Creates a repair order at the chosen dealer in the Dealer Management System accelerator. | 
|  `submit_warranty_claim`  | DMS | CMS drafts the claim with its telemetry evidence; after the operator approves, DMS files the claim and records the recovery. | 
|  `ground_vehicle`, `move_vehicles`, `exempt_recall`, `complete_recall`  | CMS | CMS updates its own records: the vehicle’s status or location in the fleet record, or the recall’s state. | 
|  `apply_cost_action`  | CMS | Records the cost action against the vehicle. | 
|  `acknowledge_only`  | None | Records the decision only. | 

## What the screens show
<a name="fi-aq-screens"></a>
+ Each recommendation shows its evidence, its estimated value and its "as of" time.
+ Each agent writes a run record per run (`vsa-{stage}-avx-agent-runs`). A queue whose agent has not run says when it last ran, and a missed run shows as stale; an empty queue never reads as "nothing to do".
+ The Agent activity feed is the fleet’s recommendations in time order, plus each decision’s audit trail.
+ Operators see only their own fleets' recommendations.
+ Each agent and the rule evaluator have alarms with a subscribed person.
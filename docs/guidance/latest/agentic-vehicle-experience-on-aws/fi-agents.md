

# Fleet Intelligence agents
<a name="fi-agents"></a>

Five more Tier 2 agents work for fleet operators and product engineers rather than vehicle owners. Four run daily and feed the Fleet Intelligence Action Queue in the CMS Fleet Intelligence portal. The fifth runs when a product engineer asks it to, and its recommendations go to the Connected Services portal. All five use the same platform, Finding contract and executors as the owner-facing agents in [The loyalty flywheel — four autonomous agents](loyalty-flywheel.md).


| Agent |  `agent_id` and runs | Reads | Finding kinds | Recommended actions | 
| --- | --- | --- | --- | --- | 
| Cost |  `agent-fi-cost`, component `cost`, daily at 04:00 UTC | ADP `vehicle_cost_monthly` and `vehicle_cost_baseline` (`adp_{stage}_fleet_cost`), built from `fleet_cost_events`, `service_records` and `fleet_ops.daily_usage`  |  `fleet.cost.anomaly`, `fleet.cost.sell_timing`  |  `apply_cost_action`  | 
| Recall and warranty |  `agent-fi-recall-warranty`, components `recall` (05:00 UTC) and `warranty` (05:20 UTC) | ADP recall views (`adp_{stage}_fleet_recall`); DMS `warranty_candidates` and parts stock per rooftop; CMS groundings |  `fleet.recall.vehicle`, `fleet.warranty.claim_candidate`  |  `book_recall_service`, `ground_vehicle`, `submit_warranty_claim`  | 
| Fleet health |  `agent-fi-fleet-health`, component `service`, daily at 05:40 UTC | ADP `vehicle_fault_status` and `pm_vehicle_status` (`adp_{stage}_fleet_health`); Agent 2 Findings for the fleet’s vehicles; CMS groundings |  `fleet.health.service`  |  `book_fleet_service`, `ground_vehicle`  | 
| Rebalancing |  `agent-fi-rebalancing`, component `rebalance`, daily at 06:00 UTC | ADP `supply_demand_gaps` and `move_outcomes` (`adp_{stage}_fleet_rebalance`), built from CMS fleet locations, the move log and the `fleet_bookings` demand forecast |  `fleet.rebalance.move`, `fleet.rebalance.gap`  |  `move_vehicles`  | 
| Fleet quality |  `agent-fi-quality`, component `investigation`, on request from an Amazon SQS queue | ADP `fault_patterns`, build components and the engineering corpus (`adp_{stage}_engineering`); recall and software campaigns on the affected vehicles |  `quality.investigation`, `quality.issue`  |  `record_engineering_decision`, `issue_recall`, `issue_software_campaign`  | 

Rebalancing works on rental and car-share fleets, and moves stay inside a metro. Distances to dealer rooftops and between locations are measured from each vehicle’s assigned location in CMS. Each component writes a run record and has a staleness alarm (see the operational controls in [Tier 2 platform — autonomous agent-reasoning layer](tier-2-platform.md)), so the portal says when an agent last ran and shows a missed run as stale.

## How a fleet agent run works
<a name="how-a-fleet-agent-run-works"></a>

Every fleet agent follows the same six steps. The data and the arithmetic are deterministic, the model makes the judgment calls, and approval and dispatch are deterministic again.

1.  **Select.** A paged Athena query picks the items to work on: outlier vehicles, unremedied recalls, warranty candidates, vehicles with an open need, or rental locations short of vehicles.

1.  **Gather evidence.** A second query builds an evidence bundle for each item. The bundle is everything the model sees.

1.  **Skip unchanged.** The agent hashes the evidence into `inputs_hash`. When the live Finding carries the same hash and the model wrote it, the run skips the item: no model call and no write. A Finding written by the rules fallback stays eligible for a model call on a later run, highest severity first, so a first-day backlog drains over a few runs.

1.  **Decide.** One Amazon Bedrock Converse call per item (per metro for rebalancing) to Claude Sonnet 4.6 through the us-west-2 inference profile. The model answers by calling exactly one tool, and the tool’s input schema lists everything the model can say. No tool has a field for severity or money. Only the cost agent’s tool writes a headline; the other agents use fixed headline templates.

1.  **Validate.** AVX checks the tool input against the schema and the bundle: every referenced id exists, every choice is one the bundle offered, and the choice is allowed for the item’s severity. Bedrock Guardrails filter the model’s text for PII and denied topics. On a failure the agent retries once with the validation error, then writes a rules answer with `confidence: low` and evidence `diagnosis_source: rules`. A run never depends on the model being available.

1.  **Write.** `write_finding()` writes the Finding with a severity from a configured band table, money from a formula, and the model’s narration in `detail`.

## What each agent decides
<a name="what-each-agent-decides"></a>


| Agent | Model tool | What the model decides | What stays deterministic | 
| --- | --- | --- | --- | 
| Cost |  `record_diagnosis`  | Which cause explains the excess when several cost categories moved (`charging_rate`, `charging_mix`, `repeat_repair`, `low_utilisation`, `efficiency`, or `unclear`); whether the evidence supports acting at all; which action fits the cause (`shift_to_depot_off_peak`, `schedule_inspection`, `reassign_or_remarket`, `driver_coaching`, or `no_action`); the headline and explanation | Outlier selection: at least 1.30 times both the vehicle’s 6-month mean and its fleet-model median, with at least 300 miles in the month. A check that the cause agrees with the numbers. The monthly saving, one formula per action. Severity from the ratio to the cohort. Sell timing has no model call: a vehicle whose maintenance cost will overtake its depreciation within 3 months gets a `reassign_or_remarket` recommendation with fixed text | 
| Recall booking |  `record_recall_plan`  | Which of three candidate rooftops that hold every remedy part; which of the vehicle’s other open items (recalls, health Findings, coverage ending within 30 days) to combine into the same visit; the urgency (`this_week`, `this_month`, or `next_visit`) | Recall-to-vehicle matching (`CONFIRMED` or `POPULATION`) in ADP SQL. Severity and whether to ground, from a fixed band table. The catalog’s safety text, verbatim, in `disclosure_txt`. A `p0` item allows only `this_week`. Grounding items get fixed text and no model call | 
| Warranty claim |  `record_claim_draft`  | The complaint, cause and correction narrative that becomes the DMS claim’s notes; whether the evidence supports filing (`file` or `insufficient_evidence`) | Eligibility and verdict from DMS’s rules engine. The recoverable amount, which is DMS’s `recoverable_usd` whatever the model writes | 
| Fleet health |  `record_service_plan`  | Which of three candidate rooftops; the urgency; which lower-severity needs to leave for a later visit | The needs list (open faults, Agent 2 Findings, PM tasks due or overdue), each need’s labor op and parts, and the severity band. A stop-driving fault always gets a grounding item, with the fault catalog’s directive verbatim. A `p0` or `attention` need is never deferred | 
| Rebalancing |  `record_rebalance_plan`  | Which candidate moves to make in a metro, which vehicles from each candidate’s eligible list, the timing (`today` or `within_3_days`), and which shortfalls to hold instead, with a reason (`temporary_event`, `returns_expected`, `not_worth_cost`, or `unclear`) | Candidates: surplus locations in the same metro, nearest first, cut to the destination’s parking. Vehicle eligibility: no grounding, no open `p0` or `attention` item, no booking in the next 24 hours, no service in the next 3 days. Transfer cost, revenue gained and lost, net benefit, and confidence from the forecast’s error and past move outcomes | 
| Fleet quality |  `record_root_cause`, then `record_design_options`  | Which ranked candidate cause explains a fault pattern (for example, a supplier lot against the plant and build window that share its vehicles) and which failure mode; two to four remedy options with their trade-offs, one of them recommended | Pattern detection (90-day rate ratio and a one-sided Poisson test, corrected for the number of cohorts tested), the affected and control vehicles, and each option’s vehicle count, cost, lead time and whether it ships over the air | 

Model calls are capped per run: 50 for cost, 60 for recall, 30 for warranty, 60 for fleet health, and 12 for rebalancing. Investigations are capped at 20 a day, with two calls each. At every cap, the five agents together spend about $6 a day on model calls.

## Findings, approval and execution
<a name="findings-approval-and-execution"></a>
+  **Recommendations, not actions.** Each Finding carries a `recommended_action` (action kind, target system, parameters, estimated value and its basis). Approving the Finding dispatches that action. A Finding with nothing to act on, such as a `fleet.rebalance.gap` or a cost diagnosis of `unclear`, is informational.
+  **Scope.** Cost, recall, warranty and fleet-health Findings are VIN-scoped. The writer projects the vehicle’s fleet from the CMS registry, and a vehicle whose fleet does not resolve is in no queue. Rebalancing Findings are fleet-scoped, with both locations in the Finding and each vehicle in `evidence[]`. Fleet-quality Findings are population-scoped (`population_id` is the vehicle maker’s id) and carry no fleet, so no fleet queue shows them.
+  **One item per subject.** `subject_key` lets one scope hold several open Findings of one kind: the data month for cost, `<campaign_id>/<book or ground>/<attempt>` for a recall, `<ro_id>/<line_no>` for a warranty line, `service/<attempt>` and `ground/<attempt>` for fleet health, and `<from>/<to>/<ISO week>` for a move. A re-run updates the item in place and keeps its decision.
+  **Expiry.** Cost Findings last 35 days, so they outlive one missed monthly refresh. Recall, warranty and fleet-health Findings last 3 days and moves 2 days. Each daily run refreshes a Finding while its condition lasts.
+  **Never on a phone.** The broker skips any Finding whose `agent_id` starts with `agent-fi-` or that carries `recommended_action` (`skip_reason: fi_item`), and the owner-facing iOS routes exclude them.
+  **Who decides.** Fleet operators approve fleet items in the Fleet Intelligence portal, and product engineers approve fleet-quality items in the Connected Services portal. Both go through CMS’s Fleet Intelligence API with the person’s own token, and AVX records `decided_by.kind` as `operator` or `engineer` from the verified token.
+  **Server-set parameters.** For each action kind, the policy table lists the parameters AVX sets from the recommendation: the vehicle, the recall, the repair-order line, the locations. An approve that changes one is refused with `400`. Changing one of the fields the policy table leaves open (a different rooftop, fewer vehicles in a move, different claim notes, a different engineering option) records the decision as `overridden`.
+  **Bookings that don’t happen.** When DMS closes a booked repair order before the work is done, the Action becomes `cancelled` within seconds. The next daily run raises a new attempt for a vehicle that still needs the work. An item the operator declined comes back after 14 days for a safety recall or a `p0` or `attention` service item, and after 30 days otherwise. After 5 attempts, an informational item says bookings keep failing.
+  **Warranty claims.** After the operator approves, DMS creates the claim and validates it. An approved claim is submitted, a claim that needs review waits for the dealer’s warranty administrator, and a denied claim is refused with DMS’s reason. DMS computes the claimed amount itself and records the recovery.
+  **Auto-approval.** Only `move_vehicles` is auto-approvable, within a per-fleet transfer-cost limit. See [Auto-approval rules](cross-surface-actions.md#fi-approval-rules).
+  **Guardrails.** Five checks in the dispatch path that no rule overrides, plus CMS’s refusal to move a grounded vehicle. See [Guardrails in the dispatch path](cross-surface-actions.md#fi-guardrails).
+  **"Why did you recommend this?"** The Tier 1 `fleet_recommendation` tool reads the stored Finding and its decision Action, with no model call. For a recall or a stop-driving fault it returns the safety text for the assistant to read word for word.

## From an engineering decision to a recall
<a name="from-an-engineering-decision-to-a-recall"></a>

A product engineer presses Investigate on a fault pattern in the Connected Services portal. CMS checks the engineer’s scope and forwards the request to AVX’s `POST /investigations`, which records it in `vsa-{stage}-avx-investigations` and queues it on Amazon SQS. One investigation runs per pattern at a time. The fleet-quality agent writes a `quality.investigation` Finding with the root cause and the options.

When the engineer approves an option, `AdpExecutor` invokes ADP’s `adp-{stage}-digital-thread-writer` Lambda function, the only component that can write a thread record. The writer checks every link against ADP, copies the affected vehicle set from `fault_patterns` itself, and appends a version to the digital thread record in `adp-{stage}-digital-thread`, which streams to `adp_{stage}_engineering.digital_thread`. For a software-update or hardware-recall option, it also creates a draft campaign whose content comes from templates and the failure mode, never from model text. AVX then writes a `quality.issue` Finding, and a second engineer approval issues the campaign. An issued recall joins the recall catalog, and the recall agent raises booking and grounding items in each affected fleet’s queue the next morning.


# Cross-surface Actions framework
<a name="cross-surface-actions"></a>

Findings are what Tier 2 agents write. Actions are what customers and dealers do with Findings. An owner approves a Finding on their iOS card → an Action is created → an executor dispatches to the target system → Action status propagates back to all surfaces.

## Finding \+ Action schema (canonical)
<a name="finding-action-schema-canonical"></a>

 **Finding** (Tier 2 output):

```
{
  "finding_id": "FIND-{uuid}",
  "finding_key": "sha256:{agent_id}:{scope_field}:{scope_value}:{finding_kind}[:{subject_key}]",
  "subject_key": null,
  "agent_id": "agent-1-energy | agent-2-vehicle-health | agent-3-ownership-cost | agent-4-concierge | agent-fi-cost | agent-fi-recall-warranty | agent-fi-fleet-health | agent-fi-rebalancing | agent-fi-quality",
  "agent_version": "agent-2-vehicle-health@v1.0.2",
  "scope": {
    "vin": "1MERIDIAN00A000001",
    "owner_id": null,
    "fleet_id": null,
    "dealership_id": null,
    "district_id": null,
    "population_id": null
  },
  "severity": "p0 | attention | soon | routine | informational",
  "finding_kind": "health.tires | health.brakes | health.battery | energy.range_context | coverage.warranty_gap | concierge.position | fleet.cost.anomaly | fleet.cost.sell_timing | fleet.recall.vehicle | fleet.warranty.claim_candidate | fleet.health.service | fleet.rebalance.move | fleet.rebalance.gap | quality.investigation | quality.issue | ...",
  "recommended_action": {
    "action_kind": "book_recall_service",
    "target_system": "dms",
    "parameters": {},
    "estimated_value_usd": null,
    "estimated_value_basis": null
  },
  "headline": "Left front tire: 8,000 km to threshold, slow leak indicated",
  "detail": "## Tire Health\n\n...",
  "evidence": [
    {
      "kind": "adp_tire_prediction",
      "source": "ADP",
      "source_ref": "adp://tire-health/vsa-staging/2026-10-01",
      "value": "remaining_km: 8000",
      "computed_at": "2026-10-01T02:00:00Z",
      "provenance": "live",
      "vin": "1MERIDIAN00A000001"
    }
  ],
  "computed_at": "2026-10-01T02:15:00Z",
  "expires_at": "2026-10-02T02:15:00Z",
  "confidence": "high",
  "inputs_hash": "sha256:...",
  "tokens_used": 8750,
  "cost_usd": 0.042,
  "disclosure_txt": null,
  "audit_trail": [
    {
      "at": "2026-10-01T02:15:00Z",
      "event": "finding_written",
      "agent_version": "agent-2-vehicle-health@v1.0.2",
      "inputs_hash": "sha256:..."
    }
  ]
}
```

 `finding_key` is the persistent-condition identity. Two runs for the same VIN, component, and `finding_kind` produce the same key; an optional `subject_key` joins the hash when one scope needs several open Findings of one kind. `recommended_action` is optional and states what approving the Finding dispatches. A worsening condition updates the existing Finding in place rather than creating a second row.

 **Action** (approval from customer or dealer):

```
{
  "action_id": "AVX-ACT-{uuid}",
  "finding_id": "FIND-...",
  "created_by": "owner-{id} | dealer-{id} | fleet-manager-{id} | engineer-{id}",
  "decided_by": {"kind": "operator | engineer | user | rule", "id": "{token sub} | {fleet_id}/{rule_id}"},
  "decision": "approved | overridden | auto_approved | declined",
  "created_at": "2026-10-01T14:32:00Z",
  "updated_at": "2026-10-01T14:35:00Z",
  "target_system": "dms | vehicle-command | retail | none | chat | ios-owner | cms | adp",
  "target_ref": "DMS-RO-12345",
  "status": "pending_execution | executed | in_progress | completed | cancelled | declined | dismissed | failed",
  "action_kind": "book_combined_visit | schedule_inspection | acknowledge_only | book_recall_service | ground_vehicle | submit_warranty_claim | book_fleet_service | move_vehicles | apply_cost_action | exempt_recall | complete_recall | record_engineering_decision | issue_recall | issue_software_campaign | lead_capture | configurator_recommend | ...",
  "parameters": {},
  "evidence": [],
  "audit_trail": [
    {
      "at": "2026-10-01T14:32:00Z",
      "by": "owner-{id}",
      "from_status": "pending_execution",
      "to_status": "in_progress",
      "note": "dms executor dispatched",
      "failure_kind": null,
      "retry_count": 0
    }
  ]
}
```

 `dismissed` means the customer dismissed the Finding without acting. `failed` means the target could not be reached after the retry budget, or refused the request as malformed; it triggers dual escalation: an owner iOS card update and a `vsa.avx.action.terminal_failure` event with a CloudWatch metric. `decided_by` comes from the verified token for an operator, never from the request body. Approving with parameters that differ from `recommended_action.parameters` is recorded as `overridden`; AVX compares the two itself.

## API
<a name="api"></a>


| Endpoint | Purpose | 
| --- | --- | 
|  `GET /findings/me`  | Owner’s Findings across all agents, paginated, sorted by severity | 
|  `GET /findings/vehicle/{vin}`  | Vehicle-scoped Findings — used by fleet manager and dealer personas | 
|  `GET /findings/fleet/{fleet_id}`  | Fleet-scoped Findings, including the fleet’s VIN-scoped Findings | 
|  `POST /findings/{id}/approve`  | Creates an Action and dispatches to the executor for the specified `target_system`. Refuses an action kind with no working executor before writing anything. | 
|  `POST /findings/{id}/decline`  | Records the operator’s decision not to act, with an optional reason (`status=declined`, `decision=declined`) | 
|  `GET`, `PUT`, `DELETE /approval-rules/fleet/{fleet_id}[/{rule_id}]`  | Per-fleet auto-approval rules; same fleet check as approve | 
|  `POST /investigations`  | Queues a fleet-quality investigation of a fault pattern. CMS calls it with the product engineer’s token; AVX checks `product-engineer` membership again and takes `requested_by` from the token | 
|  `POST /actions/{id}/dismiss`  | Sets `status=dismissed`; broker records the dismissal for demotion in the 30-day scoring window | 
|  `GET /actions/{owner_id}`  | Owner’s Action feed — status ladder for iOS card rendering | 

## Executor pattern — pluggable dispatch
<a name="executor-pattern"></a>

Each `target_system` maps to an `Executor` class registered in `agents/executors/registry.py`. Executor modules are not importable from agent modules — this boundary is test-enforced. Agents write Findings through `write_finding()`; they do not dispatch Actions or call channel APIs. The boundary makes pull-only rollout safe: a new agent writes Findings that Tier 1 surfaces on request, with no delivery side effects until proactive delivery is enabled.


| Executor | Target system | Dispatch behavior | 
| --- | --- | --- | 
|  `dms`  | DMS repair-order API | Creates a repair order with `avx_action_id` in the RO metadata: an owner’s service visit, a fleet recall remedy, or a fleet service visit. Files fleet warranty claims through `POST /api/dms/fleet/warranty-claims`, where DMS validates the claim and computes the amount (`201` submitted, `202` waiting for the dealer’s warranty administrator, `422` denied). Status updates feed back through `dms.ro.status_changed` EventBridge events to update the Action record. Refusal (4xx) → `declined`; client-error 4xx or exhausted retries on 5xx / timeout → `failed` \+ dual escalation (owner card \+ `vsa.avx.action.terminal_failure` event). | 
|  `vehicle-command`  | CMS remote command API | Sends a remote command (charge schedule, lock, OTA trigger). Returns `executed` on acknowledgement. Status tracked through CMS command-status events. | 
|  `retail`  | AVX Acquire `lead_capture` / `configurator_recommend`  | Pre-fills a lead record and optionally selects a configurator target. Routes the owner to the Acquire checkout flow on approval. | 
|  `none`  | No external call | Advisory Findings with no action path. The Action row is stored for audit; no downstream call is made. Used for Agent 1 range advisories and Agent 3 informational coverage items. | 
|  `chat`  | Tier 1 drill-down conversation | Injects `avx_finding_id` into `POST /assistant/chat`, pre-seeding the Tier 1 session with the Finding’s `evidence[]`. The owner taps "Tell me more" and enters a conversation grounded in that specific Finding. | 
|  `ios-owner`  | iOS owner inbox and push via broker | For dealer-proposed Findings: the executor writes to the owner’s Action feed table. The broker delivers push and in-app card. Direction: dealer → owner. | 
|  `cms`  | CMS Fleet Intelligence API | Records cost actions, groundings (recall or fault) and vehicle moves. Forwards the operator’s token; a rule-approved move goes to an IAM-authorized CMS route signed with AWS SigV4 by the executor’s role. | 
|  `adp`  | ADP digital-thread writer (`adp-{stage}-digital-thread-writer`, us-east-1) | Records a product engineer’s decision in the digital thread and creates the linked draft campaign; a second approval issues it. The writer is the only component that writes thread records. | 

One policy table (`agents/executors/policy.py`) holds a row per `action_kind`: its target system, whether it has a working executor, whether it needs an operator (or, for engineering kinds, a product engineer), whether a rule may auto-approve it, the name of its rule limit, and the parameters AVX sets from the recommendation rather than from the request body. The approve route, the rule API, the rule evaluator and `dispatch()` all read it, so they cannot disagree.

### Guardrails in the dispatch path
<a name="fi-guardrails"></a>

Every Action passes through `registry.dispatch()`, whoever or whatever approved it. Five guardrails run there before any executor:


| \# | Guardrail | Check | 
| --- | --- | --- | 
| G1 | A safety recall is never auto-exempted |  `exempt_recall` with `decided_by.kind` other than `operator` is refused | 
| G2 | Grounding a vehicle needs the operator |  `ground_vehicle` with `decided_by.kind` other than `operator` is refused, for a recall grounding and a stop-driving fault grounding alike | 
| G3 | Sending a warranty claim needs the operator |  `submit_warranty_claim` with `decided_by.kind` other than `operator` is refused | 
| G4 | A recall is never marked complete without a service record |  `complete_recall` is refused, whoever decided, unless `parameters.service_record_ref` resolves to a completed DMS repair order (`Ready`, `Delivered` or `Invoiced`) for the vehicle | 
| G5 | An engineering decision needs a product engineer |  `record_engineering_decision`, `issue_recall` and `issue_software_campaign` with `decided_by.kind` other than `engineer` are refused, with the sentence "Blocked: engineering decisions need a product engineer." | 

A missing or malformed `decided_by` counts as "not an operator" and "not an engineer". G1 to G4 compare against `operator`, so an engineer cannot pass them. A refused Action is recorded `declined` with the guardrail’s number in its audit entry; it never reaches an executor and never escalates. The tests name the guarded action kinds literally, and removing either the policy flag or the check makes a test fail.

A recall counts as complete only when a service record says so: a DMS repair order carrying the recall line, or a recall service record in ADP. Every fleet booking carries its campaign, so a booking DMS completes needs no extra step. `complete_recall` and `exempt_recall` have no executor; G1 and G4 still guard them in `dispatch()`.

One more check sits in CMS rather than in `dispatch()`, because CMS records the groundings: the move route refuses any move that includes a grounded vehicle, whoever approved it, a rule included. The rebalancing agent never offers a grounded vehicle in the first place. A grounding also lifts only through a service record: CMS refuses Return to service while a do-not-drive or confirmed safety recall is open, or until a repair order dated after the fault’s latest sighting is recorded for each stop-driving code. A fault that clears by itself does not count.

### Auto-approval rules
<a name="fi-approval-rules"></a>

Rules live in `vsa-{stage}-avx-approval-rules` (partition key `fleet_id`, sort key `rule_id`): the action kind, its limit, `enabled`, `created_by` and `updated_at`. A fleet with no rules auto-approves nothing; a new rule is created disabled; limit defaults come from the `auto_approval` section of the policy defaults configuration. A rule for a guarded kind, or a kind the policy table marks not auto-approvable, is refused.

The rule evaluator is the second consumer of the findings stream, next to the broker. For a Finding with a `recommended_action` and a fleet, it loads the fleet’s enabled rules for that kind and checks the limit. On a match it writes an Action (`decided_by.kind = rule`, `decision = auto_approved`) with an `action_id` derived from the Finding, action kind and rule, so a replayed stream record adds nothing, then calls `registry.dispatch()`.

 `move_vehicles` is the auto-approvable fleet kind. The rule’s limit is the largest transfer cost it approves, bounded at $500 by the deployment configuration, and no rule approves more than 5 vehicles in one move. Cost actions, recall and service bookings, groundings, warranty claims and engineering decisions are never auto-approved.

A rule-approved move has no operator token to forward. `CmsExecutor` sends it to a second CMS route, `POST /api/v1/fleet-intelligence/internal/moves`, signed with AWS SigV4 by the AVX executor’s IAM role; the API Gateway method uses IAM authorization with a resource policy naming only that role. CMS does not take AVX’s word for it. Before acting, the route reads AVX’s tables to confirm the Action is `auto_approved` for `move_vehicles` in the same fleet, that the rule it names exists, is enabled and has a limit at or above the move’s transfer cost, and that the vehicle count is within the bound. Then it runs the same checks as the operator route, including the grounding refusal.

Adding an executor is one class, a policy-table row and an integration test. No supervisor redeploy is required.
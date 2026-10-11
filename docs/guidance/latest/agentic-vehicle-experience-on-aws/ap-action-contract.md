

# The Action Contract
<a name="ap-action-contract"></a>

An Action represents what an owner has done with a Finding: approved it (dispatching an executor), dismissed it, or initiated a drill-down conversation. Approvals write a new row to `vsa-{stage}-avx-actions`. The Action carries a copy of the Finding’s evidence so its audit record stands independently of subsequent Finding updates.


| Field | Type | Semantics | 
| --- | --- | --- | 
|  `action_id`  | String (`AVX-ACT-{uuid}`) | Stable UUID, set on creation. | 
|  `finding_id`  | String | Foreign key to the originating Finding. Never null. | 
|  `created_by`  | String | The identity that created the Action: owner, dealer, fleet operator, or product engineer. | 
|  `decided_by`  | Object | Who decided, from the verified token, never from the request body: `kind` is `operator` (fleet-operator standing for the Finding’s fleet, or `platform-admin`), `engineer` (a `product-engineer` member, for population-scoped items), `user` (any other person the approve check admits), or `rule` (an auto-approval rule); `id` is the token’s `sub` or `{fleet_id}/{rule_id}`. A missing or malformed value counts as "not an operator". | 
|  `decision`  | String (enum) |  `approved`, `overridden` (approved with changed parameters), `auto_approved`, or `declined`. | 
|  `created_at`  | ISO-8601 UTC | Immutable creation timestamp. | 
|  `updated_at`  | ISO-8601 UTC | Set on creation; updated on every status transition. Callers use this to surface staleness. | 
|  `target_system`  | String (enum) | Which executor handles this Action: `dms`, `vehicle-command`, `retail`, `none`, `chat`, `ios-owner`, `cms`, or `adp`. | 
|  `target_ref`  | String | The downstream system’s reference ID, populated by the executor after successful dispatch. For `dms`, this is the repair-order number. | 
|  `status`  | String (state machine) |  `pending_execution` → `executed` → `in_progress` → `completed`. Terminal states: `cancelled` (owner cancelled after approval, or DMS closed the repair order before the work was done), `declined` (downstream target refused — a refusal 4xx — or a guardrail blocked it), `dismissed` (owner tapped Dismiss before approving), `failed` (executor exhausted retries, or the request itself was malformed). `dismissed` is distinct from `cancelled`; `declined` is distinct from `failed`. See the failure model in [The Executor Pattern](ap-executor-pattern.md). | 
|  `action_kind`  | String (enum) | The intent: `book_combined_visit`, `schedule_inspection`, `update_charging_schedule`, `file_warranty_pre`, `surface_recall`, `acknowledge_only` and others for the flywheel agents; `apply_cost_action`, `book_recall_service`, `ground_vehicle`, `submit_warranty_claim`, `book_fleet_service`, `move_vehicles`, `record_engineering_decision`, `issue_recall` and `issue_software_campaign` for the Fleet Intelligence agents. Enum is test-pinned per executor. | 
|  `parameters`  | JSON object | Executor-specific payload. For `dms`: `{vin, service_center_id, service_type, customer_availability}`. For `retail`: `{model, variant, configuration_id}`. For `chat`: `{seed_finding_id}`. | 
|  `evidence[]`  | Array of objects | Copied from the originating Finding at approval time. Later Finding updates do not modify an approved Action’s evidence. | 
|  `audit_trail[]`  | Array of objects | Immutable log of every status transition. Each entry carries `at`, `by`, `from_status`, `to_status`, optional `note`, and — on failure transitions — `failure_kind` (`target_refused`, `executor_exhausted_retries`, or `executor_terminal_error`) and `retry_count`. | 

## Action lifecycle
<a name="action-lifecycle"></a>

1.  **Approval** — An owner, fleet operator or product engineer approves a Finding, or a fleet’s auto-approval rule matches it. The Action row is written at `pending_execution` with `decided_by` and `decision`, then passes through `registry.dispatch()`.

1.  **Guardrails** — `dispatch()` refuses a guarded action kind that the required person did not decide (an operator for fleet kinds, a product engineer for engineering kinds), and `complete_recall` without a completed service record. A refused Action is recorded `declined` with the guardrail named; it never reaches an executor. See [Guardrails in the dispatch path](cross-surface-actions.md#fi-guardrails).

1.  **Dispatch** — The executor calls the target system, sets `target_ref` on success, and transitions to `executed` or `in_progress` depending on whether the target confirms completion immediately or defers it.

1.  **Progress** — For deferred targets such as a DMS repair order, incoming status events project forward: `in_progress` → `completed`. A repair order DMS closes from `Draft`, `InProgress` or `AwaitingParts` projects to `cancelled`, with the sentence "DMS closed the repair order before the work was done."

1.  **Terminal failure** — A target that refuses the work sets `declined`. Exhausted retries or a malformed request set `failed`, which fires the dual escalation described in [The Executor Pattern](ap-executor-pattern.md).

1.  **Dismissal** — The owner taps Dismiss before approving. The route transitions a synthetic Action to `dismissed`, writes feedback to the demotion table, and closes the card.
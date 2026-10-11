

# The Executor Pattern
<a name="ap-executor-pattern"></a>

An executor is a stateless component that calls one target system and records the outcome. It does not reason, does not re-interpret the action, and applies no policy beyond its retry configuration.

Two structural rules are test-enforced:
+ Executor classes are not importable from agent modules. A Tier 2 agent writes Findings; it does not dispatch Actions.
+ No agent code calls a channel API directly. SNS `Publish` calls for AVX Findings go through the broker only.

## Eight executor targets
<a name="eight-executor-targets"></a>


| Target | Description | Trigger | Failure model | 
| --- | --- | --- | --- | 
|  `dms`  | Creates a repair order in the dealer management system: an owner’s service visit, a fleet recall remedy (with the recall line), or a fleet service visit (with one line per need). Files a fleet warranty claim through DMS’s fleet claims route, where DMS validates the claim and computes the amount. The body carries `avx_action_id`. The `dms.ro.status_changed` EventBridge event projects `in_progress` → `completed`, or `cancelled` when DMS closes the order before the work is done. | Owner approves a service Finding; fleet operator approves a recall booking, a fleet service booking or a warranty claim | Refusal 4xx (`400`, `409`, …) → `declined` / `target_refused`. Client-error 4xx (`401`, `403`, `404`, `405`, `415`) → `failed` / `executor_terminal_error`. Transient failures (5xx, timeout, `408`, `425`, `429`) → retry per per-target SSM config; exhaustion → `failed` / `executor_exhausted_retries`. `failed` fires dual escalation. | 
|  `vehicle-command`  | Calls the CMS remote commands API. Used when an agent recommendation warrants an immediate vehicle action. | Agent recommends a remote command | Same 4xx/5xx model as `dms`. | 
|  `retail`  | Calls the Acquire `lead_capture` and `configurator_recommend` endpoints. | Owner approves a concierge or coverage Finding | Same failure model. | 
|  `none`  | Advisory only. No external call. Records the Action for audit and surfaces it on the owner’s ledger. | Informational Finding requiring acknowledgement | Cannot fail; transitions directly to `completed`. | 
|  `chat`  | Writes a pre-seed marker that the Tier 1 supervisor reads at session initialisation. The drill-down conversation starts with the Finding’s evidence already in context. | Owner taps "Drill down" | If the marker write fails, the conversation opens unseeded rather than blocking. | 
|  `ios-owner`  | Writes an inbox row on the owner’s Action feed. Used for reverse-direction proposals from dealers and for `failed` escalation cards. Channel delivery is still the broker’s decision — this executor writes the row. | Dealer proposes action to owner; or `failed` escalation | If the inbox write fails, the operator event still fires. | 
|  `cms`  | Applies fleet changes to CMS’s own records through CMS’s Fleet Intelligence API: records an approved cost action on the vehicle, grounds a vehicle for a recall or a stop-driving fault, and moves vehicles between locations. CMS re-checks the fleet, groundings, the origin location and parking before a move. `complete_recall` and `exempt_recall` target CMS in the policy table and have no executor. | Fleet operator approves a fleet recommendation, or a fleet rule auto-approves a move | Same failure model as `dms`. CMS answering `409` (for example, a grounded vehicle in a move) is a refusal. | 
|  `adp`  | Invokes ADP’s `adp-{stage}-digital-thread-writer` Lambda function with the approved engineering decision. The writer records the decision in the digital thread and creates or issues a draft software campaign or recall. | Product engineer approves an investigation option or a campaign issue |  `422` (a link that doesn’t exist in ADP) is a refusal; `400` is `failed`. | 

## Failure model
<a name="failure-model"></a>

Retry policy and escalation targets are per-target SSM configuration, not code constants. The keys `/vsa/{stage}/avx/executor/{target}/retry-policy` and `/vsa/{stage}/avx/executor/{target}/escalation` are read at Lambda cold start.

 `classify_status()` in `agents/executors/base.py` is the single source of truth for which HTTP status codes are transient, which are client errors, and which are refusals:
+  **Transient** (retry): 5xx, connection errors, timeouts, `408`, `425`, `429`.
+  **Client error** (terminal, `failed`): `401`, `403`, `404`, `405`, `415`. The request was malformed or the credentials were wrong; nothing reached the target. Reporting these as `declined` would tell the owner "the dealer refused" when in fact our token had expired.
+  **Refusal** (terminal, `declined`): any other 4xx such as `400` or `409`. The target received the request and chose to say no.

On `failed`, dual escalation fires:
+  **Owner-visible** — an `ios-owner` inbox card is written, routed through the broker. Headline pattern: "We couldn’t reach {target} to {action\_kind\_verb}. You can retry with a different {target} or contact us." Category: `service`. Consent is still enforced.
+  **Operator-visible** — an `vsa.avx.action.terminal_failure` EventBridge event (source `vsa.avx.executor`) is emitted, plus a `AVXActionTerminalFailure` CloudWatch metric dimensioned by `target_system`. The operator alarm SNS topic must have an active subscriber; an alarm that fires into an empty topic does not page anyone.
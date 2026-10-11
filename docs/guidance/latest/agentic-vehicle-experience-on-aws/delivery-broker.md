

# Delivery broker
<a name="delivery-broker"></a>

The AVX broker Lambda (`vsa-{stage}-avx-broker`) subscribes to the DynamoDB stream on `vsa-{stage}-avx-findings`. When a Finding is written or updated, the broker applies its policy stack to decide whether to deliver, which channel to use, and when.

Agents do not call channel APIs. This is test-enforced. The broker is the only component that promotes a Finding into an unsolicited notification.

Fleet Intelligence Findings never reach a phone. The broker’s first check skips any Finding whose `agent_id` starts with `agent-fi-` or that carries a `recommended_action` (`skip_reason: fi_item`), before owner resolution, consent or counters. The iOS routes apply the same test. Fleet operators see these items in the Fleet Intelligence portal, and product engineers in the Connected Services portal.

**Note**  
Push carries roughly 40 characters. The notification is a hook that deep-links into a Tier 1 conversation pre-seeded with `avx_finding_id`. The reasoning is in the conversation, not in the push text.

## Broker policy stack
<a name="broker-policy-stack"></a>


| Policy | Configuration | 
| --- | --- | 
| Channel selection | Urgency × context × per-category consent → channel (see channel matrix below) | 
| Per-category consent | Three categories registered at `POST /notifications/register-device`: `safety`, `coverage`, `service`. The broker checks owner consent for the relevant category before delivering. | 
| Quiet hours | SSM `/vsa/{stage}/avx/broker/quiet-hours`; default 22:00–07:00 local. `p0` severity overrides quiet hours. | 
| Rate limit | SSM `/vsa/{stage}/avx/broker/rate-limit`; default 10 per day, 3 per hour per owner. | 
| Cardinality cap | SSM `/vsa/{stage}/avx/broker/cardinality-cap`; default 15 active Findings per owner. The oldest `informational` Finding is expired when the cap is reached. | 
| APNs push threshold | SSM `/vsa/{stage}/avx/broker/apns-severity-threshold`; default `p0`. At the default, only `p0` Findings trigger APNs push. All severities create an in-app card. | 
| Priority arbitration | When multiple Findings are pending in the same delivery window, the broker sends the highest-severity item first and defers the rest to the next window. | 
| Dismissal demotion | Dismissals in the trailing 30 days reduce the broker priority score for the corresponding `finding_kind`. Safety Findings (`p0`) are not demotable. | 

Device tokens and per-category consent are stored in `vsa-{stage}-notification-devices`, registered via `POST /notifications/register-device`. The notification service is shared — DMS dealer-facing notifications use the same broker.

## Channel matrix
<a name="channel-matrix"></a>


| Channel | Role | Conditions | 
| --- | --- | --- | 
| iOS push (Amazon SNS mobile push → APNs) | Primary proactive notification | All agents; severity at or above APNs threshold (default `p0`); per-category consent required | 
| In-app AVX Cards tab | Persistent Finding and Action feed; badge updated on silent push | All agents; all severities; no consent gate; always created | 
| In-app conversation (Tier 1, WebSocket) | Full explanation after tap; `avx_finding_id` pre-seeds the Tier 1 session | All agents; triggered by push tap or card "Tell me more" | 
| Amazon Connect outbound voice | Safety-adjacent urgency — for example, blowout risk, P0 callback | Agent 2, `p0`; per-category consent required; tenant-configured | 
| SMS / email | Customers without the app; booking and warranty confirmations | Agents 2 and 3; confirmation messages only | 
| In-vehicle display (Meridian OS) | Contextual, at-the-wheel advisories; OEM integration required | Agents 1 and 2; `routine` and `informational` only | 

## iOS card surfaces
<a name="ios-card-surfaces"></a>

The companion app renders three card types in the AVX Cards tab:


| Card type | Content | 
| --- | --- | 
| Finding card | Headline, severity badge, `computed_at` timestamp ("checked 2 hours ago"), agent name, evidence summary. Action buttons: Approve, Dismiss, Tell me more (opens drill-down conversation). | 
| Action card (status ladder) | Action kind, target system, status badge (`pending_execution → in_progress → completed`), DMS RO reference when available. Dismiss changes to View Receipt on `completed`. | 
| Owner-inbox card | Dealer-proposed Finding (ios-owner executor path). Same layout as Finding card; source labelled "From your dealer". | 

Silent push refreshes the badge count without an alert. A tapped notification deep-links to the relevant Finding or Action card.
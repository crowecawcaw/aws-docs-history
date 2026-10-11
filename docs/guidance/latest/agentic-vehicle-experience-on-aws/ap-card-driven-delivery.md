

# Card-Driven Delivery
<a name="ap-card-driven-delivery"></a>

Every Finding produces at least one in-app card. The push notification, when it fires, is a hook that tells the owner something is waiting and deep-links into the card or into a Tier 1 conversation pre-seeded from the Finding’s evidence. The notification is not the message; the card and the conversation are.

## Three card variants
<a name="three-card-variants"></a>

The companion app’s AVX Cards tab renders three variants:


| Variant | When it appears | Affordances | 
| --- | --- | --- | 
| Finding card | A Tier 2 agent has written a Finding the owner has not yet acted on. | Approve (`POST /findings/{id}/approve` with target selection); Dismiss (`POST /actions/{id}/dismiss`); Drill down (opens Tier 1 chat pre-seeded with the Finding’s evidence). | 
| Action card | The owner approved a Finding and an Action is in progress. | Status ladder (`pending_execution` → `in_progress` → `completed`); `target_ref` when available; audit trail on expansion. | 
| iOS-owner card | A dealer or the system has proposed an action to the owner (reverse direction). | Same affordances as the Finding card. | 

## Push notifications
<a name="push-notifications"></a>

The broker decides whether a Finding triggers a push. The APNs threshold is SSM-configurable (`/vsa/{stage}/avx/broker/apns-severity-threshold`, default `p0`). Below the threshold, the broker creates an in-app card only.

Alert notifications carry a short headline (about 40 characters) and the `finding_id` in the payload. Tapping routes directly to the relevant Finding card. For `p0` alerts, the app also opens a Tier 1 session pre-seeded from the Finding’s evidence.

Silent push (`content-available: 1`) refreshes the badge count from the findings summary endpoint without displaying an alert.

Per-category consent (safety, coverage, service) is recorded in `vsa-{stage}-notification-devices` at device registration and enforced by the broker. The app does not duplicate consent checks.

## Drill-down conversation seeding
<a name="drill-down-conversation-seeding"></a>

The `chat` executor writes a pre-seed marker that the Tier 1 supervisor reads at session initialisation. The supervisor loads the Finding’s `evidence[]` before the first user turn. The owner does not re-explain the card; the agent already has the context.

## In-vehicle display
<a name="in-vehicle-display"></a>

For vehicles whose OEM API supports it, a Finding card can be rendered on the in-vehicle head unit. The OEM display adapter translates `headline`, `detail`, and `disclosure_txt` (where present) into the OEM’s display format. Approval interactions route back through the same `/findings/{id}/approve` surface. The Finding contract is unchanged.
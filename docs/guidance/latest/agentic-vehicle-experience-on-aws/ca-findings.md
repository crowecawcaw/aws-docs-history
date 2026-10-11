

# Findings and Actions
<a name="ca-findings"></a>

Findings are produced by Tier 2 agents and read by the app; the app performs no reasoning over them. The Finding and Action contracts are documented in [The Finding contract](ap-finding-contract.md) and [The Action contract](ap-action-contract.md). The broker — which decides channel, consent, and timing independently of any agent — is documented in [Broker Boundaries](ap-cross-account-iam.md).

## The AVX Cards tab
<a name="the-avx-cards-tab"></a>

Findings appear in the AVX Cards tab, not the Alerts tab. Alerts is for real-time signals — DTCs, safety events, triage outcomes. Cards is for the conclusions of agent reasoning, which arrive asynchronously on a schedule or event trigger and warrant deliberate owner attention rather than an immediate interruption.

Three card variants populate the tab:
+  **Finding card** — a Tier 2 agent has written a Finding the owner has not yet acted on. The owner sees the headline, confidence, and a distilled evidence summary. The full detail and evidence are in the drawer. Three affordances: approve (`POST /findings/{id}/approve` with target selection), dismiss (`POST /actions/{id}/dismiss`), and drill down (opens a Tier 1 conversation pre-seeded from the Finding’s evidence).
+  **Action card** — the owner approved a Finding and an Action is in progress. Shows a status ladder (`pending_execution` → `in_progress` → `completed`) and the target reference when available — for example, a DMS repair-order number. Audit trail is visible on expansion.
+  **iOS-owner card** — a dealer or the system proposed an action to the owner (reverse direction). Presents the same affordances as the Finding card.

Three client-side properties govern how the tab reads and writes:

 **Standing, not filtering.** The app requests the Findings the signed-in user has standing over and receives exactly those. A driver identity sees Findings scoped to the vehicle assigned to them.

 **Contract-shaped responses.** Findings arrive with the scope attributes used for server-side indexing stripped out. The client decodes a stable shape and does not depend on projection details that exist for query reasons.

 **Explicit transitions.** Approval sends a minimal, fixed body — nothing inferred, nothing optional. Dismissal is a dedicated sub-resource. The vocabulary distinguishes an owner declining to act (`dismissed`) from an owner cancelling something already approved (`cancelled`) from a downstream target refusing the work (`declined`). A summary endpoint supplies open counts and recency for the tab badge without loading full Findings.

## Push notifications and deep-link seeding
<a name="push-notifications-and-deep-link-seeding"></a>

A push notification carries a short headline — about 40 characters — and the `finding_id` in its payload. Its purpose is to tell the owner something is waiting. The reasoning is in the card; the full conversation is in Tier 1.

Tapping an alert notification routes directly to the relevant Finding card via a dedicated deep-link router. The router lives outside the SwiftUI environment hierarchy because the notification callback predates the application lifecycle and has no access to the environment object.

Tapping a `p0` alert opens a Tier 1 session pre-seeded with the Finding’s evidence. The app passes the `finding_id` in the `POST /assistant/chat` payload; the supervisor loads `evidence[]` before the first user turn. The owner does not re-explain the card; the agent already has the context.

Silent push (`content-available: 1`) refreshes the badge count from the findings summary endpoint without displaying an alert. The badge reflects open Findings and pending Actions.

Push delivery is consent-gated per category (safety, coverage, service). Consent is captured at device registration via `POST /notifications/register-device` and is revisitable in Account settings. The broker enforces consent; the app does not duplicate that check.
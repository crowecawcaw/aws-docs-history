

# Stage 4 — Service
<a name="service-stage"></a>

The Service stage is the prescriptive heart of AVX. When a customer calls because their check-engine light is on, the agent must determine urgency, diagnose the likely cause, quote the repair, identify a service center, book the appointment, and verify warranty coverage — all in a single conversational turn, grounded in real vehicle data.

The following subsections trace the full flow from session start to appointment confirmation.

## Session start: context fusion
<a name="session-start-context-fusion"></a>

Before the first agent response, the session-init flow fuses three data sources:

1.  **Live vehicle state** — read from CMS Redis LKS via the `vehicle_live_state()` Lambda (`GET /vehicles/{id}/live-state`). This returns the sub-millisecond snapshot of active DTCs, sensor readings (coolant temp, tire pressure, fuel level), and odometer.

1.  **Service and trip history** — read from CMS DynamoDB via `GET /vehicles/{id}/service-history` and `GET /vehicles/{id}/trips`. This gives the agent the repair history and mileage context it needs to assess whether a current fault is recurrent.

1.  **LTM persona context** — the AgentCore Memory session-init hydration (described in [Stage 3 — Onboard / Own](onboard-own.md)) provides the vehicle identity snapshot, open recall status, and customer profile.

The agent begins every Service conversation with this fused context already loaded — no tool calls required for context in the first turn.

## Triage: deterministic P0–P3 classification
<a name="triage-deterministic-p0p3-classification"></a>

The first agent action on any service-related inquiry is a call to the `triage()` tool. Triage is **deterministic-first**: the classification is computed from structured inputs, not from an LLM judgment. This is a deliberate safety constraint — the LLM narrates the result but cannot downgrade it.

![The Vehicle health view in the sample iOS app: a health score of 22 marked Action required, a breakdown showing how each active diagnostic trouble code lowers the score by severity (low, medium, high, critical), and a card per code with its recommended next step.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-vehicle-health.png)


![The Assistant screen in the sample iOS app after a P0 classification: a Critical issue detected card that recommends roadside assistance, with Request roadside and Talk to an agent buttons, above the live session transcript and an appointment confirmation.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-p0-card.png)



| Level | Meaning | Default agent action | 
| --- | --- | --- | 
|  **P0 — Stop driving**  | Safety-critical: brake failure, overheating, airbag fault, loss of steering assist | Instruct pull-over immediately; dispatch roadside assistance; `escalate()` to tier-2 P0 Connect queue; no booking offer | 
|  **P1 — Service now**  | Active DTC in degraded mode; measurable risk if ignored > 24–48 hours | Schedule within 48 hours; create STAR ticket; the card offers **Talk to an agent**  | 
|  **P2 — Service soon**  | Non-critical DTC, wear indicator, open recall | Schedule within 1–2 weeks; create STAR ticket; offer booking | 
|  **P3 — Monitor**  | Informational; reset conditions documented | No action required; log event; educate customer | 

 **Triage inputs.** The `triage()` tool accepts: active DTCs with severity codes from CMS live-state, telemetry thresholds (coolant temp delta, brake wear percentage, tire pressure deviation), open recalls from the CMS recall-integration service, and the tenant’s policy overrides from `vsa-tenant-config`. Tenant policy can raise — but never lower — the default classification for a given DTC code.

 **Safety invariant.** A P0 classification cannot be downgraded, and the stop-driving instruction is always delivered word for word. The driver is then offered a human agent and roadside assistance, each one tap, or automatically if the tenant opts in. The classification is enforced outside the LLM, at the Lambda level, so a prompt injection or model error cannot suppress it. See [Security](security.md) for the guardrail implementation.

## Diagnose: grounded KB retrieval
<a name="diagnose-grounded-kb-retrieval"></a>

After triage produces a classification, the `knowledge()` RAG tool retrieves the relevant reference content from the ADP Bedrock Knowledge Base.

The KB is organized into source categories (`dtc_guide`, `tsb_recall`, `owner_manual`, `service_policy`, `parts_catalog`). Enable source-category filtering (`VSA_KB_SOURCE_CATEGORY_FILTER=true`) so the agent retrieves only the categories relevant to the current intent — for a P1 DTC, retrieve `dtc_guide` \+ `tsb_recall` \+ `service_policy`; for a warranty question, retrieve `tsb_recall` \+ `service_policy`.

A well-grounded diagnose turn presents:
+ The DTC’s plain-English explanation and likely causes (from `dtc_guide`).
+ Any Technical Service Bulletins that match the specific DTC and model year (from `tsb_recall`).
+ Whether the fault is covered by the manufacturer’s warranty (from `service_policy`; confirmed by ADP Vehicle Lifecycle warranty record).

The agent synthesizes this into a customer-facing explanation grounded in citations from the KB, not from LLM parametric knowledge. Require the `knowledge()` tool to return `citations[]` in its response and surface them in the reasoning drawer (if the Connect chat or web channel is active).

## Quote: parts pricing and service center selection
<a name="quote-parts-pricing-and-service-center-selection"></a>

With the diagnosis in hand, the agent proceeds to quote and locate.

 **Parts pricing.** Call `parts_lookup()` with the DTC code, the vehicle’s year/make/model/trim (from the `vehicle_identity()` tool response), and the tenant’s pricing tier. The ADP Parts Catalog returns OEM part number, OEM price, optional equivalent-part price, and estimated labor hours. For fleet operators, a negotiated fleet-pricing tier from the tenant config is applied automatically.

 **Service center selection.** Call `service_network()` with the vehicle’s current GPS position (from CMS live-state), the required repair capability (derived from the DTC category), and the tenant’s service-network filter (authorized dealers only, preferred-shop network, or any certified shop within N miles). The ADP Service Network returns a ranked list of service centers with distance, estimated wait time, and capability match.

 **Quote assembly.** Combine parts price \+ estimated labor hours × tenant labor rate → total estimated repair cost. The agent presents the quote conversationally: "Replacing the wastegate actuator runs roughly \\$180–\\$250 in parts plus about 1.2 hours of labor at your dealer." The quote is included in the STAR ticket as the `EstimatedRepairCost` field.

## Book: phased STAR-JSON booking
<a name="book-phased-star-json-booking"></a>

Booking works at three levels. The agent’s `book()` tool emits STAR-shaped JSON, so tenants already using STAR (Standard for Transmission, Exchange, and Retrieval of automotive data) get a clean integration path.

![The first booking step in the sample iOS app: the customer picks the service they need, such as oil change, tire pressure, brakes, battery, check engine diagnostics, or body damage.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-book-service.png)


![The second booking step in the sample iOS app: nearby dealers with distance and rating, each offering available appointment times to pick from.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-book-slot.png)



| Phase | Capability | Customer experience | Tenant integration required | 
| --- | --- | --- | --- | 
|  **STAR service request**  |  `book()` builds a STAR `ServiceRequestAdd` envelope and writes a `scheduled` row to the CMS service-history table | "I’ve created service request VSA-2026-10-08-4F2A for your dealer. It’s in the Service tab of your app." | None beyond CMS | 
|  **Appointment time**  | In the companion app the customer picks a service, a nearby dealer and a time; `POST /book` writes a `scheduled` row to the CMS service-history table, which the app’s Service tab and the CMS portal both show | "Tire pressure check at your dealer, Tuesday at 10 am — booked." | A dealer list with appointment times for the app to offer | 
|  **DMS booking**  | To write the confirmed appointment into the dealer’s DMS, extend `book()` with a DMS adapter | "Booked — confirmation AB-991-2026, Tuesday 10 am, 2101 Main St." | Direct DMS integration (CDK Global, Reynolds, Tekion, Dealertrack, Fleetio, or Whip Around) — per-tenant, per-DMS setup | 

 **STAR ticket fields.** The `book()` tool emits a STAR `ServiceRequestAdd` envelope: the tenant ID, session and message IDs, a `correlation` block with the triage decision ID and VIN, and a payload with the reported symptom, the driver’s actions, the narrative, the priority and the preferred service center. Tenants that require STAR XML for legacy DMS consumers add a per-tenant STAR XML converter.

 **Booking failures.** If the CMS write fails, `book()` still returns the envelope with `status: sink-error`, so the failure is visible to the agent instead of reading as a booking. A repeat call in the same session at the same priority returns the same request rather than a second one, and a more urgent booking already held for the session is returned instead of a less urgent one. Never suppress a failure — a failed silent booking is worse than an explicit one.

## Warranty verification
<a name="warranty-verification"></a>

Warranty lookup runs in parallel with (or immediately after) the quote step. Call `vehicle_identity()` to retrieve the ADP Vehicle Lifecycle warranty record for the specific VIN. The record includes: powertrain warranty end date/mileage, bumper-to-bumper end date/mileage, and any extended or CPO warranty terms.

Compare the open repair against the warranty coverage:
+ If covered: present as "covered under powertrain warranty, no cost to you" and note this in the STAR ticket `WarrantyClaimPreCheck` field.
+ If expired or not covered: present the quoted out-of-pocket cost.
+ If coverage is ambiguous (for example, a grey-area component): flag for tier-2 review rather than making a coverage determination the agent is not qualified to make.

## Escalation to tier-2
<a name="escalation-to-tier-2"></a>

The `escalate()` tool routes the session to a tier-2 Amazon Connect queue when:
+ The driver confirms a P0 recommendation (**Talk to an agent** or **Request roadside**), or the tenant has enabled `escalation.autoOpenHumanChatOnP0`. See the safety invariant above.
+ The customer explicitly requests a human.
+ The supervisor encounters a policy exception it cannot resolve.
+ The warranty coverage determination is ambiguous and requires a specialist.

The escalation handoff carries: transcript, triage output (classification \+ reason trace), VIN and vehicle context snapshot, open recalls, warranty coverage summary, recommended action, and the draft STAR ticket. The tier-2 agent receives this context pre-populated on their Connect desktop before the call connects, eliminating re-authentication and context re-gathering.

For the Connect queue configuration and the handoff, see [Contact Center Integration](contact-center-integration.md).

## Service stage data and tool summary
<a name="service-stage-data-and-tool-summary"></a>


| Element | Detail | 
| --- | --- | 
|  **CMS live data**  | Redis LKS (active DTCs, sensor readings, odometer), DynamoDB `vehicles` / `service-history` / `trips` tables | 
|  **ADP reference data**  | Bedrock KB (`dtc_guide`, `tsb_recall`, `owner_manual`, `service_policy`, `parts_catalog`), ADP Parts Catalog, ADP Service Network, ADP Vehicle Lifecycle (warranty) | 
|  **Agent tools**  |  `triage()`, `vehicle_identity()`, `knowledge()`, `parts_lookup()`, `service_network()`, `book()`, `escalate()`  | 
|  **Booking artifact**  | STAR-shaped JSON `ServiceRequestAdd`; scheduled rows in the CMS service-history table | 
|  **Escalation target**  | Amazon Connect chat on the tenant’s chat queue, P0 at high priority (configured per tenant) | 
|  **Partner integrations**  | Document processing: CDK Global, Reynolds, Tekion, Dealertrack, Fleetio, Whip Around (per-tenant, per-DMS setup required); digital commerce: Salesforce Service Cloud, ServiceNow (to add delivery of STAR service requests) | 


|  |  | 
| --- |--- |
| Building blocks | The triage → diagnose (KB grounded) → quote (parts and service center) → book (STAR-JSON) → warranty → escalate flow: the deterministic triage classifier (`lambdas/triage-classifier/`), `retrieve()` against the ADP Knowledge Base, `book()` (STAR-JSON `ServiceRequestAdd`), and `escalate()`. Agent 2 (`agent-2-vehicle-health`) and Agent 3 (`agent-3-ownership-cost`) produce the Findings above, read through `get_health_findings()` and `get_coverage()`. `vsa-{stage}-service-plans` holds Agent 2’s service plans; `vsa-{stage}-loyalty-ledger` holds Agent 3’s credit records. The `dms` executor creates the dealer repair order when the owner approves. | 

## Card-driven proactive Service workflows
<a name="card-driven-proactive-service-workflows"></a>

Beyond reactive, on-demand service triage, AVX emits asynchronous Findings that reach the customer as cards — visual alerts that the customer reviews on their own timeline rather than through a voice or chat conversation.

 **Pattern.** Agent 2 (Vehicle Health and Service Agent) runs on a schedule — daily per component — and on ADP prediction arrivals, DTC-threshold crossings, and service-interval approaches. It owns the Service care arc as a single relationship: notice → explain → price → apply coverage → find a slot → book → follow up. When two or more service items are due in proximity — for example, a tire replacement and a brake inspection due in 3,000 km — Agent 2 bundles them into a single service plan in `vsa-{stage}-service-plans` so the `book()` tool commits against the plan rather than booking each item independently. Findings are written to `vsa-{stage}-avx-findings` (see [The Finding Contract](ap-finding-contract.md) for the full contract) and rendered as cards in the customer’s mobile app or in-vehicle display.

Agent 3 (Ownership Cost and Coverage Advocate) runs as a companion for coverage-adjacent Findings: warranty-verdict follow-up, open recalls, prepaid-balance expiry, and loyalty-credit events. Agent 3 is the only agent whose Findings may carry `discount_applied`. When Agent 2 identifies a service item that may be covered, it flags the coverage need in its Finding evidence; Agent 3 evaluates the claim and produces a separate Finding that authorizes the credit. Agent 3 narrates DMS warranty verdicts verbatim and manages the loyalty ledger in `vsa-{stage}-loyalty-ledger`. Its Tier 1 read tools are `get_coverage()` and `get_loyalty_standing()`.

![The Alerts tab in the sample iOS app: an Agent Findings card with a severity tag, a one-line finding, readable evidence chips, and an Ask assistant action, followed by the vehicle’s active faults and recent safety events.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-alerts.png)


 **Example card workflows.** 


| Finding kind | Agent | Trigger | Card headline (subject) | CTA (recommended\_action) | 
| --- | --- | --- | --- | --- | 
|  `health.tires`  | Agent 2 | Tire pressure low, or wear approaching limit (ADP tire-health prediction) | "Tire Pressure Low (Front Left)" | "Find Nearby Service" / "Dismiss" | 
|  `health.brakes`  | Agent 2 | Brake interval approaching; DTC indicating brake system; EV rotor-corrosion threshold (corrosion from regen underuse) | "Brake Inspection Due in 3,000 km" | "Book Service" | 
|  `health.battery`  | Agent 2 | Battery state-of-health deviation from model (ADP battery prediction) | "Battery Health Check Recommended" | "Book Service" | 
|  `dtc_diagnosis`  | Agent 2 | Persistent P1 DTC in live state (e.g., P0171 System Too Lean) | "Engine Issue: P0171 System Too Lean" | "Learn More" / "Book Service" | 
|  `maintenance_interval_due`  | Agent 2 | Oil-change or service interval reached (ADP Vehicle Lifecycle maintenance schedule \+ CMS mileage tracking) | "Scheduled Maintenance Due: 75,000-Mile Service" | "Book Service" | 
|  `coverage.recall_open`  | Agent 3 | New recall released for the vehicle’s VIN (ADP Recall data product) | "Recall: Seatbelt Inflator — Schedule Remedy" | "Schedule Remedy" → `initiate_recall_remedy` action | 
|  `coverage.warranty_gap`  | Agent 3 | Warranty expiration date within 30 days, or mileage threshold within 1,000 miles | "Powertrain Warranty Expires Soon" | "Review Coverage" → chat transfer to Tier 1 | 
|  `coverage.prepaid_expiring`  | Agent 3 | Prepaid service balance nearing expiry (loyalty ledger daily sweep) | "Prepaid Service Credits Expiring" | "View Options" → `retail` executor | 
|  `energy.battery_context`  | Agent 1 | Charging efficiency below target, or degradation curve deviates from model (ADP energy-usage data) | "Charging Efficiency Below Baseline" | "Learn How" → in-app educational content | 

 **Card rendering and delivery.** 

1. The agent writes the Finding to `vsa-{stage}-avx-findings` through `write_finding()`.

1. The outreach broker reads the write from the table’s DynamoDB stream. It builds the card from the Finding’s `headline`, `detail` and `evidence[]` (see [The Finding Contract](ap-finding-contract.md)); `finding_kind` selects the card template.

1. The broker picks the channel:
   +  **AVX Cards tab** — every Finding becomes an in-app card.
   +  **Push** — a Finding at or above the APNs severity threshold (default `p0`) also sends a push, if the owner consented to that category. The push deep-links into the card.
   +  **SMS or email** — for owners without the app, and for confirmations of record.
   +  **In-vehicle display** — where the OEM’s connected-vehicle API supports it.

1. Customer taps the card to expand and read the full Finding body and evidence.

1. Customer taps the CTA button ("Book Service," "Schedule Remedy") if they want to act.

1. If a CTA is tapped, an Action is created from the Finding’s `recommended_action` template and dispatched to the appropriate executor (see [The Executor Pattern](ap-executor-pattern.md)).

 **Consent and customer control.** 

Cards are delivered proactively, but actions are not. If a Finding’s `recommended_action` has `customer_consent_required: true`, the action does not execute until the customer explicitly taps the button. For example:
+ A tire-pressure-low Finding delivers a card with "Find Nearby Service" button. Tapping it creates a `schedule_appointment` action routed to the DMS, with customer consent implicit in the button tap.
+ A warranty-expiration Finding delivers a card with "Review Coverage" button. Tapping it creates an action that transfers the customer to a Tier 1 chat agent for coverage questions — not a transactional action.
+ A maintenance-interval Finding with tenant policy "only notify, do not auto-book" delivers a card with no CTA button; the card is informational only.

 **Staleness and freshness signals.** 

Every card displays the Finding’s `computed_at` timestamp, so the customer knows the Finding is fresh (e.g., "as of today at 2 pm") or stale (e.g., "from yesterday morning; re-check for updates"). This transparency is a requirement of the Finding contract — Tier 2 agents must not suppress staleness.

 **Card lifecycle and archival.** 

Cards are rendered from Findings with a default 90-day TTL. After 90 days, the Finding is archived to S3 (via Glue) for long-term vehicle history audit, and the card is removed from the customer’s active list. This TTL is configurable per tenant in `vsa-tenant-config`.
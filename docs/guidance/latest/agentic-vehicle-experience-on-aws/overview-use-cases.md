

# Use Cases
<a name="overview-use-cases"></a>

## Fleet Vehicle Service Triage
<a name="overview-uc-fleet-service"></a>

A fleet operator deploys AVX to give drivers a voice-first way to report vehicle problems. The Tier 1 supervisor triages the fault, creates a service ticket against the operator’s configured DMS, and routes P0 and P1 cases to the operator’s dispatch team via Amazon Connect. Agent 2 (Vehicle Health and Service Agent) runs daily per vehicle, evaluates tire wear, brake intervals, and battery state against ADP predictions and service history, and writes service Findings before a driver calls. Dispatchers receive structured, pre-triaged work orders; drivers get answers without waiting in a call queue.

## Proactive Recall Outreach
<a name="overview-uc-recall-outreach"></a>

When ADP’s recall data product receives a new recall, Agent 3 (Ownership Cost and Coverage Advocate) fires on the recall-publication event, evaluates coverage impact per affected owner, and writes `coverage.recall_open` Findings. The outreach broker delivers each Finding through the appropriate channel: an iOS push for owners with the app, or an outbound Amazon Connect contact for those without. The Tier 1 supervisor handles the resulting conversation — confirming parts availability, scheduling the remedy, and applying any available prepaid-service credits — with the Finding’s evidence already loaded in session context.

## Connected Vehicle Owner Experience
<a name="overview-uc-vehicle-owner"></a>

An OEM deploys AVX to give vehicle owners a branded assistant from the OEM’s mobile app or website. The Tier 1 supervisor answers ownership questions drawing on Findings that the Tier 2 agents have already written. Agent 1 (Energy and Charging Advocate) runs daily per vehicle and on charging-session-end events, writing `energy.range_context`, `energy.battery_context`, and `energy.charging_plan` Findings so the owner receives range and charging advice specific to their usage pattern. Agent 2 (Vehicle Health and Service Agent) evaluates tire wear, brake intervals, and battery health, writes service Findings, and produces service plans the `book()` tool commits against on approval. The vehicle owner persona draws on ADP Customer 360, Vehicle Lifecycle, and the Bedrock Knowledge Base.

## Rental In-Trip Assistance
<a name="overview-uc-rental-assist"></a>

A rental company deploys AVX to handle in-trip customer requests: tire pressure warnings, range anxiety on EV rentals, and minor incidents. The agent resolves the issue or connects the customer to roadside assistance via the operator’s Amazon Connect contact flow, with the vehicle’s live state pre-populated for the operator’s agent.

## Service Advisor and Technician Support
<a name="overview-uc-service-advisor"></a>

A dealership or fleet maintenance shop deploys AVX to the service advisor and technician roles. The service advisor uses the agent to prepare for an upcoming appointment — pulling the vehicle’s service history, open recalls, and active DTCs before the customer arrives. The technician uses it during the repair to look up DTC procedures, TSBs, and torque specifications from the knowledge base without leaving the bay.

## Household Mobility Concierge
<a name="overview-uc-household-concierge"></a>

Agent 4 (Household Mobility Concierge) maintains a continuous ownership-position picture for each customer. It reads equity and valuation data from ADP, the owner’s finance or lease state, household vehicle graph, and loyalty standing, and writes `concierge.position` and `concierge.trade_in_timing` Findings to the owner’s card feed. When an equity threshold or lease-maturity date is crossed, Agent 4 triggers a `retail` executor that pre-populates a Tier 1 conversation with valuation context. Trade-in valuation uses ADP condition data and market comparables and produces an indicative range — not a binding offer — with a mandatory verbatim disclosure. When comparables are mocked or unavailable, the monetary figure is withheld or watermarked as illustrative; the condition score renders separately regardless. See [Stage 5 — Sell / Trade-in](sell-trade-in.md) for the trade-in pattern and the provenance guard design.
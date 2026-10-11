

# Features and Benefits
<a name="overview-features-benefits"></a>

## Agentic Voice and Text on One Platform
<a name="overview-feature-agentic-voice"></a>

AVX runs on Amazon Bedrock AgentCore with Nova 2 Sonic for speech-to-speech voice. The same agent code that handles a voice call over Amazon Connect also handles a web chat session or a REST API call from a mobile app. Channel type is an attribute on the session — there is no separate code path per channel.

## Deterministic-First Triage
<a name="overview-feature-deterministic-triage"></a>

Criticality classification is a tool call, not an LLM judgment. The triage classifier reads active DTCs with severity codes, telemetry thresholds (coolant temperature, brake wear, tire pressure delta), open recalls, and tenant policy overrides. It returns a structured P0–P3 classification with a reason trace. The LLM narrates the result; it does not produce it. This makes triage auditable and consistent regardless of how the customer phrases the complaint.

## Grounded, Citable Answers
<a name="overview-feature-grounded-answers"></a>

Every factual answer — DTC interpretation, TSB match, parts price, warranty coverage — cites the source document or data product that produced it. The API response includes a `citations` field listing the knowledge-base documents and ADP data products consulted. This supports compliance audit trails and lets tier-2 agents verify the answer the customer received.

## First-Class Multi-Tenancy
<a name="overview-feature-multitenant"></a>

One AVX deployment serves multiple tenant segments: fleet operators, OEM owners, and rental companies. Tenant identity is resolved at session start from the signed-in user’s session (the `custom:tenantId` claim on the user’s token). From that point, every downstream call — knowledge base selection, branding, service policy, escalation queue, booking destination — is parameterized by tenant. Onboarding a new tenant is a configuration operation, not a code change.

## Native Amazon Connect Integration
<a name="overview-feature-connect-integration"></a>

AVX integrates with Amazon Connect for the human handoff: a Connect chat from the in-app voice or text session, and a callback to the driver’s phone on a verified P0. Each tenant configures one chat queue, whose contact flow sends P0 to a high-priority branch, and optionally a callback flow and queue for the P0 callback. The triage result and a conversation summary travel in the contact attributes.

## Autonomous Tier 2 Agents
<a name="overview-feature-tier2-agents"></a>

AVX includes four Tier 2 agents for vehicle owners that run on schedules and business events — an ADP prediction arrival, a DMS warranty-verdict change, a recall publication — and write evidence-carrying Findings to `vsa-{stage}-avx-findings`.

Agent 1 (Energy and Charging Advocate) evaluates charging history, range data, ambient temperature, and tariff feeds and writes `energy.range_context`, `energy.battery_context`, and `energy.charging_plan` Findings per VIN. Agent 2 (Vehicle Health and Service Agent) evaluates tire wear, brake intervals, battery state-of-health, and DTC history, writes service-plan Findings, and bundles related service items so a single `book()` call covers them. Agent 3 (Ownership Cost and Coverage Advocate) evaluates warranty coverage, open recalls, prepaid-service balances, and loyalty credits; it is the only agent whose Findings may carry `discount_applied`. Agent 4 (Household Mobility Concierge) evaluates equity, finance state, and household vehicle data and writes `concierge.position` and `concierge.trade_in_timing` Findings.

Five more Tier 2 agents work for fleets. Each morning the cost, recall and warranty, fleet health and rebalancing agents read ADP views and write recommendations to the Fleet Intelligence Action Queue in the CMS portal: a cost action for an outlier vehicle, a recall or service booking at a rooftop with the parts, a warranty claim, a grounding, or a vehicle move between locations. A fleet operator approves each one, and an executor carries it out in DMS or CMS. The fleet-quality agent runs when a product engineer asks it to investigate a fault pattern; the engineer’s decision is recorded in ADP’s digital thread and can issue a recall to the affected fleets. See [Fleet Intelligence agents](fi-agents.md).

Each agent module provides its own goal scope, read stack, and agent factory. Adding an agent means registering a module; the runner, Finding contract, and delivery infrastructure do not change. See [Tier 2 Autonomous Agents](avx-agent-pattern.md) for the agent registry design and artifact contract.

## Outreach Broker
<a name="overview-feature-proactive-broker"></a>

The outreach broker (`vsa-{stage}-avx-broker`) owns all proactive delivery decisions: channel selection, per-category consent (safety, coverage, service), quiet-hours policy, frequency caps (default: 10 per day, 3 per hour), cardinality cap (default: 15 active cards), priority arbitration across competing Findings, and feedback demotion based on dismissals in the trailing 30 days.

Agents write Findings; the broker decides whether and how to deliver each one. P0 safety Findings bypass the broker queue and go to immediate delivery. All other Findings enter the broker’s policy evaluation. A push notification carries approximately 40 characters and deep-links into a Tier 1 conversation pre-seeded with the Finding’s `avx_finding_id`, so the owner opens the conversation at the Finding’s depth rather than from a blank session.

Device tokens and per-category consent are stored in `vsa-{stage}-notification-devices`, registered via `POST /notifications/register-device`.

## Deployable as a Composition Layer
<a name="overview-feature-composable-stack"></a>

AVX deploys on top of CMS and ADP. Without CMS, AVX falls back to embedded DTC and recall corpora. Without ADP, VIN decode, parts pricing, and service center lookup are unavailable but triage, booking (ticket-only), and escalation still function.
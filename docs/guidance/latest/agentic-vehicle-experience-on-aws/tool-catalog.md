

# Tool catalog
<a name="tool-catalog"></a>

The following table lists the tools registered in the AVX supervisor agent. Tools are assigned per-persona in `PERSONA_TOOL_FACTORIES` (`agents/supervisor/tools/init.py`).


| Tool name | Description | Returns | 
| --- | --- | --- | 
|  `triage`  | Deterministic P0–P3 criticality classification. Inputs: DTC codes, telemetry flags, recall IDs, tenant policy overrides. Does not make an LLM call. Returns a structured classification result with reason trace. |  `{level, reason, inputs_consulted, recommended_action}`  | 
|  `retrieve`  | Retrieves reference content from the ADP Bedrock Knowledge Base. Filters by `source_category` (dtc\_guide, tsb\_recall, service\_policy, owner\_manual, warranty\_terms, parts\_catalog). Returns ranked passages with S3 URI citations and relevance scores. |  `[{snippet, source, score}]`  | 
|  `vehicle_identity`  | Fetches vehicle identity record (make, model, year, trim, powertrain) from AgentCore Memory LTM, filtered by `vehicle_id`. |  `{vin, make, model, year, …​}`  | 
|  `service_history`  | Retrieves the 12 most-recent service records for a VIN from AgentCore Memory LTM, filtered by `vehicle_id` and `data_source=service_records`. |  `[{serviceId, date, type, cost, provider}]`  | 
|  `find_service_center`  | Finds nearby service centers for a given vehicle issue, using the caller’s current location (latitude/longitude) and the service-network seed data. Returns the top candidates with distance and availability. |  `{centers: [{name, address, distance, phone}], narration}`  | 
|  `book`  | Builds a STAR-JSON `ServiceRequestAdd` envelope and writes a `scheduled` row to the CMS service-history table (gated on `VSA_BOOK_WRITE_CMS`, default on). One request per session and priority: a repeat call returns the same request. |  `{requestNumber, messageId, status, envelope}`; `status` is `sink-accepted` when the CMS row is written, `sink-error` when the write fails, `draft-created` when it is skipped | 
|  `escalate_to_human`  | Hands the session to a tier-2 human agent through a Connect chat on the tenant’s chat queue, with the triage output and a summary in the contact attributes. Takes no severity: the level comes from the classifier’s verdict in session context, and a request with no verdict is refused. `escalate_for_service` covers a request for a person with no vehicle fault. |  `{status, contactId, participantToken}`  | 
|  `lookup_knowledge`  | Per-persona knowledge retrieval wrapper over the ADP KB. Returns grounded reference passages for owner-manual, service-policy, and charging-narrative queries. |  `{passages: [{text, source, score}]}`  | 
|  `lookup_parts`  | Parts catalog lookup from the ADP KB. Filters by `source_category=parts_catalog`. Returns part numbers, prices, and availability for a given service type. |  `{parts: [{partNumber, name, price, source}]}`  | 
|  `diy_repair_advisor`  | Retrieval-only tool for driver self-service guidance. Returns owner-manual reference content for Nova to summarize in voice. Optionally emits a `chat_message` with structured reference data for display on the companion app screen alongside Nova’s brief spoken response. |  `{reference_material, source, chat_message?}`  | 
|  `customer_profile`  | Retrieves the customer’s 360-degree profile from AgentCore Memory LTM (filtered by `customer_id`, `data_source=customer_360`). Used by consumer and vehicle-owner personas. |  `{customerId, name, preferences, vehicles}`  | 
|  `interaction_history`  | Retrieves the 50 most-recent customer interactions from AgentCore Memory LTM. Used by service-advisor and retail-advisor personas for context continuity. |  `[{date, channel, summary, outcome}]`  | 
|  `ota_history`  | Retrieves OTA campaign and software update history for a VIN from AgentCore Memory LTM, covering a six-month window. |  `[{campaignId, date, component, status}]`  | 
|  `charging_history`  | Retrieves 30-day charging session history for an EV from AgentCore Memory LTM. |  `[{sessionId, date, kwh, duration, location}]`  | 
|  `catalog_query`  | Discover / Find. Accepts natural-language vehicle criteria (body style, tow capacity, fuel type, target MSRP range) and returns the top-3 matching models from the OEM’s ADP-sourced catalog via the `vsa-acquire-catalog` DynamoDB table. Returns `{available: false}` when the catalog is not configured. |  `{results: [{vin, year, make, model, trim, price, …​}]}`  | 
|  `offers_lookup`  | Discover / Find. Retrieves active promotional offers for a catalog model from `vsa-acquire-catalog`. Applies a deterministic validity-window filter. Every returned offer includes a `disclosure_txt` field the supervisor must narrate verbatim. |  `{offers: [{offerId, type, terms, expiry, disclosure_txt}]}`  | 
|  `lead_capture`  | Discover / Find. Writes a STAR-JSON lead record to `vsa-acquire-leads` when the customer provides contact information. Idempotent: returns the existing `leadId` if a matching `contactHash` exists. Requires `contact_consent=True`; returns a validation error otherwise. |  `{leadId, status}`  | 
|  `resolve_or_create_owner_identity`  | Acquire / Ownership. Resolves or creates an owner identity for an Acquire session. It looks up the owner in the OEM Cognito user pool by `(tenantId, email)` and creates the account when none exists, returning `isNewIdentity`. When a `leadId` is provided, hydrates contact info from the lead record before resolution. |  `{ownerSub, isNewIdentity}`  | 
|  `health_findings`  | Tier 1 read surface for Agent 2 (Vehicle Health & Service) Findings. Queries `vsa-{stage}-avx-findings` for the newest `health.*` Finding per component for a given VIN. Returns `computed_at` so the supervisor can narrate staleness ("we checked this yesterday at 2 AM"). No LLM call; DynamoDB read only. |  `{findings: [{component, headline, detail, severity, computed_at, confidence}]}`  | 
|  `get_energy_advice`  | Tier 1 read surface for Agent 1 (Energy & Charging Advocate) Findings. Queries `vsa-{stage}-avx-findings` for the newest `energy.*` Finding for a given VIN. Returns `computed_at` for staleness narration. No LLM call; DynamoDB read only. |  `{findings: [{finding_kind, headline, detail, severity, computed_at, confidence}]}`  | 
|  `get_coverage`  | Tier 1 read surface for Agent 3 (Ownership Cost & Coverage Advocate) Findings. Returns the newest `coverage.*` Findings for the owner — warranty gap, open recalls, prepaid-balance status. Returns `computed_at` per Finding. |  `{findings: [{finding_kind, headline, detail, severity, computed_at, confidence, disclosure_txt}]}`  | 
|  `get_loyalty_standing`  | Tier 1 read surface for Agent 3 loyalty Findings. Returns the current `loyalty.*` Finding for the owner — earned credits, tier standing, expiring benefits. No LLM call; DynamoDB read only. |  `{standing: {headline, detail, computed_at, confidence}}`  | 
|  `get_ownership_position`  | Tier 1 read surface for Agent 4 (Household Mobility Concierge) Findings. Returns the newest `concierge.*` Finding — equity position, finance state, trade-in range when available. Every monetary field carries the `provenance` tag from the Finding’s evidence entries. Returns `disclosure_txt` when a monetary figure is included. |  `{position: {headline, detail, severity, computed_at, confidence, disclosure_txt}}`  | 
|  `fleet_lifecycle`  | Fleet Intelligence read for the `fleet_manager` persona. Returns vehicle lifecycle summary — end-of-life count, compliance status, service-due count — from CMS Fleet Intelligence API. Text persona only (response time \~2.6 s exceeds Nova Sonic’s tool budget). |  `{available, lifecycle_summary, computedAt, provenance}`  | 
|  `fleet_cost_outliers`  | Fleet Intelligence read for the `fleet_manager` persona. Returns vehicles whose cost per mile is above the outlier threshold (a multiple of the fleet mean), highest first, from the CMS Fleet Intelligence API. |  `{available, fleetId, fleetMeanCostPerMile, threshold, outlierMultiple, outliers, provenance, computedAt}`  | 
|  `fleet_recommendation`  | Fleet Intelligence read for the `fleet_manager` persona. Reads one Action Queue Finding and its decision Action from DynamoDB, with no model call, and returns the safety text of a recall or stop-driving fault for verbatim narration. |  `{available, finding, queue_status, action}`  | 

## Tool extensions
<a name="tool-extensions"></a>

To add any of the following capabilities, implement a `@tool`-decorated callable and register it in `PERSONA_TOOL_FACTORIES`:
+  **Calendar slot proposal** — Query the tenant’s availability feed and return open appointment slots for the recommended service type. Requires a per-tenant availability feed endpoint (iCal or REST).
+  **Direct in-call DMS booking (`dms_book`)** — Write an appointment directly to the DMS during a voice conversation, without going through an Agent 2 service plan. This is a Tier 1 shortcut; the standard DMS write path is the `dms` executor dispatched when the owner approves an Agent 2 Finding. Use this extension only for tenants that require in-call booking without an agent-managed plan in `vsa-{stage}-service-plans`. Requires a per-tenant DMS connector endpoint in tenant config.
+  **Finance qualification** — Call the OEM’s captive finance arm and return a qualification tier and rate range. Requires a per-tenant lender API credential.
+  **Reservation deposit (`payment_initiate`)** — Initiate a refundable online reservation deposit scoped to the deposit amount only. Full purchase payment routes through the dealer DMS.
+  **Reservation handoff (`reservation_handoff`)** — Hand off a reservation and pre-qualification package to the dealer’s DMS for e-contracting and full-purchase-payment collection.

## Sub-agent tool design guidelines
<a name="sub-agent-tool-design-guidelines"></a>

When building a new tool for the supervisor, follow these guidelines derived from production constraints:

1.  **Return fast.** Tools must complete within \~1 second during voice sessions. Use the Knowledge Base for reference lookups (sub-100ms for cached warm queries) rather than LLM synthesis inside the tool.

1.  **Return structured data.** Return a dict with well-named fields. Avoid free-form prose in tool output — let the supervisor LLM compose the voice response from structured facts.

1.  **Include a `narration` field for booking and action tools.** The narration-injection pattern requires a ready-made string. Include `"narration": "I’ve created ticket …​"` in the tool return dict so the output handler can inject it without additional LLM synthesis.

1.  **Do not include PII in tool output.** Tool output is logged for audit. Redact driver names, phone numbers, and addresses before returning.

1.  **Fail gracefully.** Return a structured error dict rather than raising an exception. The supervisor LLM can handle a `{"status": "error", "reason": "service unavailable"}` return and compose an appropriate response; an unhandled exception drops the session.

1.  **Register the correct wire name.** The `@tool(name=…​)` decorator sets the name the LLM sees and the wire name emitted in `tool.call` events. Verify the wire name matches the eval harness expectations before deploying.
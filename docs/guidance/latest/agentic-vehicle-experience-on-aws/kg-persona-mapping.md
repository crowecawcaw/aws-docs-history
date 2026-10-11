

# Persona-to-grounding mapping
<a name="kg-persona-mapping"></a>

The six AVX personas vary in their grounding needs. The following table summarizes which grounding surface each persona primarily uses and what data it expects at session initialization. The table is the prescriptive implementation guide; the authoritative code lives in `agents/supervisor/persona_definitions.py` and `lambdas/api-assistant-chat/persona_map.py`.


| Persona | Primary segment | LTM products loaded at session init | KB grounding in use | 
| --- | --- | --- | --- | 
| Fleet Driver | Fleet operator | vehicle\_identity, service\_records, charging\_sessions, ota\_campaigns, vehicle\_telemetry\_aggregated, energy\_usage | LTM \+ unfiltered KB (generic `retrieve` tool) — no pre-scoped source\_category filter; the `retrieve` tool returns semantically matched passages across all content (e.g. DTC guides, recall bulletins, owner manual) relevant to the query | 
| Consumer | Rental | vehicle\_identity, charging\_sessions, customer\_360, customer\_interactions, ota\_campaigns, energy\_usage | LTM \+ unfiltered KB (generic `retrieve` tool) — rental context, interaction history, and charging data are the primary sources; `retrieve` is available for policy and manual lookups | 
| Retail Advisor | OEM | vehicle\_identity, customer\_360, customer\_interactions | LTM \+ unfiltered KB (generic `retrieve` tool) — retail advisor queries center on customer history and vehicle sales context; `retrieve` is available for brand policy and warranty lookups | 
| Vehicle Owner | OEM | vehicle\_identity, service\_records, charging\_sessions, customer\_360, ota\_campaigns, vehicle\_telemetry\_aggregated | LTM \+ unfiltered KB (generic `retrieve` tool) — owner queries are anchored to the specific vehicle’s history and campaign status; `retrieve` is available for recall and manual lookups | 
| Service Advisor | Fleet (mixed) | vehicle\_identity, service\_records, customer\_360, customer\_interactions | LTM \+ pre-scoped filtered KB — source categories pre-scoped via `PERSONA_KB_FILTERS`: tsb\_recall, owner\_manual, service\_policy, charging\_narrative; service advisors need reference content alongside the vehicle’s record to make and justify service decisions | 
| Technician | Fleet (mixed) | vehicle\_identity, service\_records | LTM \+ pre-scoped filtered KB — source categories pre-scoped via `PERSONA_KB_FILTERS`: dtc\_guide, parts\_catalog, service\_policy; technicians need diagnostic reference and parts data alongside the service record for the vehicle under investigation | 

All six AVX personas have KB grounding available, but the mechanism differs. Fleet Driver, Consumer, Retail Advisor, and Vehicle Owner use the generic unfiltered `retrieve` tool — the supervisor passes an optional `source_category` keyword argument or retrieves across all categories based on the query. Service Advisor and Technician use pre-scoped KB access defined in `PERSONA_KB_FILTERS` in `persona_definitions.py`, which restricts the Retrieve filter to the source categories appropriate for each role. When a mixed persona’s query does not require reference lookup — for example, "when was this vehicle last serviced?" — the supervisor omits the KB Retrieve call and answers from Memory alone, saving both latency and token cost.

Persona is always inferred server-side from validated Cognito claims, never accepted from client-supplied parameters. The mapping logic is described in [Personas and Tenancy](personas-and-tenancy.md); the security rationale is covered in [Security](security.md).
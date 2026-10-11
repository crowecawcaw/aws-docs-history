

# Personas at a Glance
<a name="overview-personas-at-a-glance"></a>

AVX defines six personas. Each persona configures the agent’s data access scope (which ADP data products to load into LTM), its knowledge base filters (which categories of reference content to retrieve), and its communication style.


| Persona | Tenant segment | Primary grounding | KB filters | 
| --- | --- | --- | --- | 
|  **Fleet Driver**  | Fleet operator | Vehicle Identity, Service Records, Charging Sessions, OTA Campaigns | None (LTM only) | 
|  **Vehicle Owner**  | OEM | Vehicle Identity, Service Records, Charging Sessions, OTA Campaigns | None (LTM only) | 
|  **Consumer**  | Rental | Vehicle Identity, Charging Sessions, Customer 360, Customer Interactions | None (LTM only) | 
|  **Service Advisor**  | Fleet / OEM | Service Records, Customer 360, Customer Interactions | TSBs/recalls, owner manuals, service policy, charging narratives | 
|  **Technician**  | Fleet / OEM | Service Records, Customer 360 | DTC guides, parts catalog, service policy | 
|  **Retail Advisor**  | OEM | Vehicle Identity, Service Records, Customer 360, Customer Interactions | None (LTM only) | 

A seventh role — the **Contact Center Agent** (tier-2 human) — is not an agent persona but a human Amazon Connect agent who receives escalations from AVX with full context pre-populated.

Persona is inferred server-side from the caller’s authenticated session (Amazon Cognito groups and custom claims) so the client application does not need to specify it explicitly. The mapping table is documented in `docs/persona-mapping.md` in the AVX repository.
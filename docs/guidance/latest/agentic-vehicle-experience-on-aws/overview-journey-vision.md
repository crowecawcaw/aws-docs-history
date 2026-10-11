

# The Customer-Journey Vision
<a name="overview-journey-vision"></a>

AVX is designed around the full vehicle ownership lifecycle. The guidance organizes the customer journey into five stages:


| Stage | What happens | AVX role | 
| --- | --- | --- | 
|  **Find**  | A prospective buyer researches vehicles — inventory, financing pre-qualification, EV range for their commute | Retail advisor persona surfaces relevant inventory and financing options via `catalog_query()`, `offers_lookup()`, and `lead_capture()` tools | 
|  **Acquire**  | Purchase or lease financing, digital contracting, delivery scheduling | Partner integration with commerce, payments, and contract-management platforms; `resolve_or_create_owner_identity()` bridges lead records to durable accounts at ownership transfer | 
|  **Own**  | Day-to-day ownership — live vehicle health, charging, OTA updates, maintenance scheduling | Fleet driver and vehicle owner personas; proactive outreach on recalls and maintenance due | 
|  **Service**  | Triage a warning light, diagnose a fault, book a repair appointment, check warranty coverage | Core capability — triage → knowledge lookup → booking → escalation; fleet-driver and vehicle-owner personas functional | 
|  **Sell**  | End-of-ownership transition — trade-in valuation, history report, commerce platform handoff | End-of-ownership journey endpoint; the vehicle’s complete service history accumulated through CMS and ADP provides a verifiable provenance record for commerce or trade-in flows | 

This guide covers all five journey stages. The **Own** and **Service** stages have the most fully developed tool catalog; **Find** and **Acquire** have full tool implementations that depend on tenant-provided catalog feeds and partner integrations for their complete end-to-end flow.
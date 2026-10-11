

# The Customer Journey
<a name="the-customer-journey"></a>

The connected vehicle customer journey spans multiple stages, each with distinct customer intents, data requirements, and interaction channels. AVX provides the agentic patterns and integration layer that delivers coherent, personalized experiences across all stages.

This chapter is the prescriptive spine of the guidance. It maps the vehicle-ownership lifecycle to concrete AVX build patterns: which data sources to wire, which agent tools to deploy, and which partner integration points to instrument. The stages are described in order from earliest to latest in the vehicle lifecycle.

**Important**  
Each stage below is described as a **definitive architectural pattern** for how to build that stage on AVX — the AgentCore Runtime, AgentCore Memory, Nova 2 Sonic voice channel, and Amazon Connect escalation surface compose the same way at every stage; only the per-stage tool catalog and data-product wiring differ. A `Building blocks::` callout at the end of each stage lists the components that stage composes. Build order typically runs Service first, then Onboard / Own, then Discover / Acquire, then Sell / Trade-in as your organization’s priorities and data-product availability permit; the stages share one architecture and can be read in any order.

The following table summarizes how each stage maps to AVX building blocks. Subsequent sections detail each stage prescriptively.


| Stage | CMS / ADP Data | Agent Tools & Patterns | Partner Integration Points | 
| --- | --- | --- | --- | 
|  [Discover / Find](discover-find.md)  | ADP Vehicle Identity Graph, Campaigns/Offers |  `catalog_query()`, `offers_lookup()`, `lead_capture()`  | OEM CRM / lead-management system (Path A identity promotion); DMS inventory feeds; Amazon Connect outbound (Path B re-engagement push, reused from Onboard / Own) | 
|  [Acquire / Finance](acquire-finance.md)  | ADP Vehicle Lifecycle, ADP Customer 360 |  `finance_qualify()`, `payment_initiate()`, `reservation_handoff()`, `resolve_or_create_owner_identity()`, `VehicleOwnershipTransfer`  | OEM captive finance arm (primary credit decisioning); Payments (Stripe, Plaid — reservation deposit only); Dealer DMS e-contracting \+ full purchase payment (Reynolds, CDK Global, Tekion); dealer F&I desk (escalation) | 
|  [Onboard / Own](onboard-own.md)  | CMS DynamoDB (vehicle record, driver), ADP Vehicle Identity Graph, AgentCore Memory LTM |  `vehicle_identity()`, session-init LTM hydration, proactive-notification pattern | Subscription management (Zuora); OEM-branded Cognito tenant pool | 
|  [Service](service-stage.md)  | CMS Redis live-state, CMS DynamoDB (service history, trips), ADP KB (DTC guides, TSBs, recalls, manuals, service policy), ADP Parts Catalog, ADP Service Network, ADP Vehicle Lifecycle (warranty) |  `triage()`, `knowledge()`, `vehicle_identity()`, `parts_lookup()`, `service_network()`, `book()`, `escalate()`  | Document processing (CDK Global, Reynolds, Tekion); Connect tier-2 queues; DMS booking (per-tenant, per-DMS setup required); Digital commerce webhooks (Salesforce Service Cloud, ServiceNow) | 
|  [Sell / Trade-in](sell-trade-in.md)  | ADP Vehicle Lifecycle, service history |  `commerce_handoff()` (partner integration pattern) | Commerce marketplace integration | 
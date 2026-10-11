

# Stage 1 — Discover / Find
<a name="discover-find"></a>

A single OEM tenant already owns the surfaces where vehicle discovery happens: a public brand website with a build-and-price configurator and dealer inventory search, an OEM-branded mobile app, and a dealer network that is the actual point of sale. AVX’s role at this stage is not to build a new discovery channel — it is to embed a conversational sales agent directly into the surfaces the OEM already operates, and to recognize that Discover has three structurally different entry paths with different identity preconditions and, for fleet buyers, a different channel entirely.

## Path A — Anonymous / new-prospect Discover
<a name="path-a-anonymous-new-prospect-discover"></a>

A visitor with no existing relationship to the OEM lands on the OEM’s public website or app and starts a conversation with the embedded sales agent.

 **Channel: embedded directly in the OEM’s own website and app.** The agent is invoked client-side from the OEM’s website or app via API Gateway, with Amazon Cognito used only for optional sign-in rather than as a session precondition. Voice, when offered, is Nova 2 Sonic invoked directly from the browser or app’s microphone through the same API Gateway path — an interaction modality embedded in the site itself. The agent’s framing is closer to a knowledgeable dealership salesperson standing at the configurator than to a Service-stage triage bot: it answers feature, tow-capacity, pricing, and lease-offer questions conversationally.

 **Identity: none required to start.** An ephemeral session identifier is created at first interaction — no Cognito authentication precondition. AgentCore Memory holds this as short-term, session-scoped state only: stated preferences, viewed configurations, current-turn context. There is no persona to hydrate from LTM at session start, because for an anonymous visitor no persona record exists yet.

 **AgentCore Runtime dispatches per-turn tools.** The same AgentCore Runtime described in [Agentic Architecture](agentic-architecture.md) dispatches `catalog_query()` and, when the utterance is offer-aware, `offers_lookup()` on every turn — both scoped to the OEM’s own inventory and incentive data, not delegated to a third-party commerce platform. For a single-OEM deployment, the OEM’s own website **is** the commerce system of record; there is no separate digital-commerce partner to delegate catalog ownership to.

 **Identity promotion — the entity-resolution boundary.** If the visitor saves a configuration, requests a callback, or authenticates, the ephemeral session is **linked**, not looked up — a deliberate write, not an automatic resolution. The join key is contact information (email or phone) captured at the moment of linking, or a Cognito `sub` if the visitor authenticates into an existing or new OEM account. That link produces a structured lead/reservation record — contact info, saved configuration, dealer of choice if selected, and an OEM-issued lead ID — written to the **OEM’s own CRM / lead-management system**, which is the OEM’s existing infrastructure, not new AVX infrastructure. AVX does not write directly into a dealer’s DMS: DMS systems (Reynolds, CDK Global, Tekion, Dealertrack) are dealer-owned and per-vendor, the same per-tenant, per-DMS setup that DMS booking in the Service stage needs. The OEM’s CRM already has the dealer-routing logic and per-DMS-vendor integrations built; AVX’s integration surface is the one system it can reasonably own talking to — the OEM’s CRM — not the fan-out to N dealer DMS vendors.

 **Handoff shape: a warm lead.** The lead/reservation record is a structured, asynchronously consumed record — the same shape as the Service stage’s `book()` STAR-JSON pattern. A licensed advisor picks it up from the OEM’s CRM on their own timeline; the customer receives a confirmation and, if they requested a callback, hears from a dealer directly.

## Path B — Existing-owner re-engagement
<a name="path-b-existing-owner-re-engagement"></a>

A current OEM owner, already known to AVX through the LTM established at Onboard, receives a proactively pushed lease-maturity or upgrade offer and enters a new Discover cycle from a warm start.

 **Channel: push notification into the OEM’s existing app.** The owner already has the app from onboarding; no new channel is needed.

 **Identity: already resolved.** This is the same OEM-owner persona from [Personas and Tenancy](personas-and-tenancy.md), re-entering a different journey stage — not a new persona category and not a new identity-resolution problem.

 **Trigger: the same proactive-engagement pipeline Onboard / Own already uses.** A business-rule event — lease-maturity date, mileage threshold suggesting trade-in value, new-model-year launch matching the owner’s trim history — is evaluated through the **same** CMS Flink → MSK → threshold-evaluation → push pipeline described in [Stage 3 — Onboard / Own](onboard-own.md), with a different rule set and a different offer source (dealer/OEM incentive data rather than maintenance/recall content). This reuse is deliberate and correct: the precondition that makes Onboard’s proactive pattern work — an existing owner with LTM already hydrated — is genuinely satisfied here, unlike Path A’s anonymous visitor.

 **What follows is Discover-shaped, from a warm start.** Once the pushed offer opens a conversation, the tool catalog is the same as Path A — `catalog_query()`, `offers_lookup()` — but the session bootstrap is completely different: warm, LTM-hydrated, persona-and-vehicle-history-known, versus Path A’s cold, session-only, anonymous start.

![The Buy tab in the sample iOS app for an existing owner: upgrade offers with monthly payments, the owner’s current vehicle with an estimated trade-in value, and a While you were away section listing updates on a saved build.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-buy.png)


## Path C — Fleet / B2B sourcing
<a name="path-c-fleet-b2b-sourcing"></a>

A fleet sourcing manager evaluating vehicles for a commercial fleet is a structurally different buyer than Path A’s retail visitor, and does not enter through the same consumer configurator surface. Fleet purchasing is a B2B motion: named account relationships, RFQ-style volume-pricing requests, multi-vehicle order quantities, and (commonly) an existing fleet account manager at the OEM or a fleet-focused dealer group — not an anonymous website visit.

 **Channel: an OEM fleet-sales portal or a named account manager’s own tools, not the retail configurator.** Large OEMs of any real scale already operate a fleet-sales function — a dedicated fleet portal, a named account-manager relationship, or both — entirely separate from the consumer-facing website Path A embeds into. The AVX agent’s role here, if any, is to assist an already-identified fleet account (authenticated via a business Cognito pool or federated from the OEM’s existing fleet-sales identity system) with catalog and offer questions scoped to fleet pricing and volume-order inventory — not to serve as the fleet’s initial discovery surface, which the OEM’s existing fleet-sales relationship already owns.

 **Identity: a business account, not anonymous.** Unlike Path A, a Path C session starts from an already-resolved business/fleet identity — the fleet sourcing manager is a known account, not a first-time anonymous visitor. Persona resolution here is the existing `fleet_driver`/fleet-operator persona machinery this IG already defines elsewhere ([Personas and Tenancy](personas-and-tenancy.md)), applied to a sourcing conversation rather than an operations conversation — not a new identity problem, but also not Path A’s anonymous-session model.

 **Data and tools: the same catalog/offers surface, scoped differently.** `catalog_query()` and `offers_lookup()` are the same tools Path A and Path B use, filtered by the fleet’s negotiated pricing tier and available fleet-inventory pool rather than retail inventory — the tool catalog does not change; the identity precondition and the pricing/inventory scope do.

 **What comes next.** A fleet RFQ that converts to a purchase enters Acquire / Finance the same way Path B does — from an already-established identity, with fleet-specific finance terms (master lease agreements, fleet financing programs) rather than individual consumer financing. Path C’s Acquire-stage financing needs are materially different from an individual retail buyer’s (see [Stage 2 — Acquire / Finance](acquire-finance.md)) and are called out there rather than assumed to be the same flow with a different label.

 **What comes next (any path).** Once the customer converges on a specific vehicle and initiates a transaction, the session transitions into the Acquire / Finance stage. For Path A, the bridge across that transition is the lead/reservation record’s contact info and OEM lead ID — not an AVX-native identity, since none exists yet. For Path B, the bridge is the already-established Cognito identity and LTM persona snapshot. For Path C, the bridge is the fleet account’s existing business identity, carrying an RFQ or negotiated-quote reference rather than an individual lead ID.

 **Data wiring.** Connect the agent to two ADP data products via the cross-account Lake Formation grant pattern described in [Building on CMS and ADP](building-on-cms-and-adp.md):
+  **ADP Vehicle Identity Graph** — provides year/make/model/trim attributes, powertrain and feature flags, and certified-pre-owned status that the agent uses to answer feature-matching questions. Sourced from the OEM’s own dealer DMS inventory feeds (CDK Global, Reynolds, Tekion, Dealertrack, Fleetio).
+  **ADP Campaigns/Offers** — provides the OEM’s own curated offers (lease rates, incentive packages) that the agent surfaces in response to price or availability questions.

 **Agent tools to implement.** At minimum, implement a `catalog_query()` tool that accepts natural-language vehicle criteria (body style, tow capacity, fuel type, target MSRP range) and returns a ranked list of matching inventory or models from the OEM’s own ADP-sourced data. For offer-aware responses, a companion `offers_lookup()` tool queries the Campaigns/Offers product. Add a `lead_capture()` tool that performs the identity-promotion write described above — session-to-lead linking, contact-info capture, and the write to the OEM’s CRM/lead-management system.

 **Persona inference.** Path A is a retail/individual-buyer channel — there is no persona to infer at session start, since the visitor has no identity claim yet, but the segment itself is retail by construction: nobody reaches a public configurator-and-inventory-search widget as a fleet sourcing manager submitting an RFQ. A rental operator’s individual customer choosing an upgrade fits Path A the same way a retail buyer does — both are individual consumers browsing a consumer surface. For Path B, persona inference is already complete — it is the existing OEM-owner resolution from Onboard. Fleet buying is a structurally different B2B motion and does not enter through Path A at all — see Path C below.

 **Entity resolution across the AVX-to-dealer boundary.** The join key that survives the boundary between AVX’s identity space (Cognito `sub`, ephemeral session ID) and the dealer’s identity space (DMS customer record) is contact information plus an OEM-issued lead ID — not a single canonical identity in the agent layer, because the two systems only agree on contact info and a lead reference until a sale closes. Once `VehicleOwnershipTransfer` fires at Acquire completion (see [Stage 2 — Acquire / Finance](acquire-finance.md)), the `resolve_or_create_owner_identity()` tool resolves or provisions a VIN-linked Cognito identity from the lead record’s contact info, and the customer’s onward relationship becomes Onboard / Own’s familiar LTM-hydrated model.

 **Scope.** Discover is a catalog-and-offers query surface plus lead capture, not a full configure-price-quote (CPQ) workflow. Personalized recommendation ranking, purchase-intent scoring, and configuration-and-order flows build on the same tools.


|  |  | 
| --- |--- |
| Building blocks | Tools `catalog_query()`, `offers_lookup()` and `lead_capture()`, bound to the `consumer`, `vehicle_owner` and `retail_advisor` personas in `PERSONA_TOOL_FACTORIES`. Path B’s proactive trigger comes from the Tier 2 agents and the outreach broker — see [Stage 3 — Onboard / Own](onboard-own.md). The ADP Campaigns/Offers feeds and the OEM CRM endpoint are per-tenant configuration. | 
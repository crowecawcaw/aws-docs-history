

# Stage 2 — Acquire / Finance
<a name="acquire-finance"></a>

At the Acquire stage, a customer who has selected a vehicle — arriving from either Discover path, or from any other funnel — needs to complete the purchase or lease transaction. For a single OEM, most of the regulated heavy lifting already exists outside AVX: the OEM’s own captive finance arm already underwrites credit, and the dealer’s existing DMS already handles e-contracting. AVX’s role is to orchestrate a conversation on top of those existing systems, not to rebuild financial or contracting infrastructure inside the agent.

## Entry paths into Acquire
<a name="entry-paths-into-acquire"></a>

A customer arrives at Acquire from one of Discover’s three paths, or from any other funnel entirely — Acquire does not require having gone through Discover first. Unlike Discover, where the three paths diverge in channel, identity model, and mechanism throughout, Acquire’s paths diverge in exactly one place — how the session establishes identity at start — and converge immediately afterward onto the same tool dispatch, memory model, and escalation architecture described below.

 **From Discover Path A (anonymous).** The session starts from the lead/reservation record’s contact info and OEM lead ID — there may not yet be a Cognito identity. The customer authenticates (or completes authentication) before any regulated financial action proceeds; Acquire has a real, non-optional identity requirement that Discover Path A does not. This is also the path that later needs `resolve_or_create_owner_identity()` (see **Cognito identity resolution** below) to bridge the lead record into a durable AVX account once the sale closes.

 **From Discover Path B (existing-owner re-engagement) or an existing OEM account.** The session starts from the already-established Cognito identity and LTM persona snapshot — authentication is already complete, and no identity-bridging step is needed later.

 **From Discover Path C (fleet / B2B sourcing) or an RFQ that converts to a purchase.** The session starts from the fleet account’s existing business identity, carrying an RFQ or negotiated-quote reference. Fleet financing needs are materially different from an individual retail buyer’s — master lease agreements and fleet financing programs rather than individual consumer credit qualification — and are called out specifically in **Persona and finance-segment resolution** below rather than assumed to be the same flow with a different label.

Once identity is established by whichever path the customer arrived from, every following subsection — tool dispatch, memory model, voice, escalation, ownership transfer — applies identically regardless of entry path.

 **Persona and finance-segment resolution.** Once authenticated, Cognito claims resolve the persona and, together with a tenant config entry, the finance segment: individual, business, lease-only, or cash for a retail buyer (Path A or Path B); fleet master-lease or fleet-financing-program for a Path C business account. Finance-segment configuration is stored in `vsa-tenant-config` and can be extended to support additional segment taxonomies. A Path C fleet segment routes `finance_qualify()` to the OEM’s fleet-financing program (a distinct product from individual retail captive financing, even at the same OEM) rather than to individual consumer underwriting — this is a genuinely different qualification flow, not the same tool call with a different label.

 **AgentCore Runtime dispatches Acquire-specific tools against existing OEM and dealer systems.** The same AgentCore Runtime described in [Agentic Architecture](agentic-architecture.md) dispatches the following per-turn tool surfaces:

1.  `finance_qualify()` — calls the **OEM’s own captive finance arm** (the pattern established by manufacturer-owned finance companies at major automakers) as the primary target. This is an already-existing, already-regulated underwriting system operating outside AVX; the tool accepts customer consent plus stated income and employment and returns a qualification tier and available rate range. If the captive arm declines or returns a subprime tier the customer does not accept, the tool falls through to a secondary lender (illustrative: a credit union or a third-party decisioning partner such as FICO or Experian) **within the same conversation** — this is a per-customer runtime decision the tool makes on a decline outcome, not a static choice of "which lender this OEM uses" fixed at tenant-config time. OEMs without a captive finance arm at all configure only the secondary-lender path as primary. The agent presents each result conversationally; it does not interpret or modify either decisioning output.

1.  `payment_initiate()` — scoped to a refundable online reservation deposit only (illustrative: a $500 hold to secure a configuration or a specific dealer-lot vehicle before an in-person visit), via a payments partner (illustrative: Stripe, Plaid, or the tenant’s payment processor). This is genuinely an AVX-owned transaction: a lightweight, small-dollar e-commerce hold, the same pattern many OEMs' existing "reserve online" flows already use. The **full purchase payment** (down payment or full amount at deal close) is not this tool’s job — it is a dealer-transaction-scoped payment that flows through the dealer’s existing point-of-sale/DMS payment processing as part of `reservation\_handoff()’s e-contracting step, the same way a dealer already collects payment on any in-person sale today. Building a separate generic-partner payment integration for the full purchase amount would duplicate a capability the dealer’s DMS already has.

1.  `reservation_handoff()` — hands off a reservation and pre-qualification package to the **dealer’s existing DMS e-contracting capability** (Reynolds, CDK Global, and Tekion all have this today), which handles both contract execution and full-amount payment collection as part of the same in-dealer transaction, rather than AVX generating a contract or processing the full payment itself. This replaces a from-scratch `contract_generate()` tool against a generic contract-management partner — that pattern is over-scoped for what a single OEM needs, because the dealer’s DMS already does e-contracting and payment collection.

1.  `VehicleOwnershipTransfer` emission — on successful acquisition completion (qualifying decisioning, successful payment, and the dealer’s DMS confirming a signed contract), a STAR-compatible payload is written across the ADP cross-account boundary into the ADP Vehicle Lifecycle data product.

The `escalate()` tool is also available at this stage for compliance-load-bearing handoffs to a dealer’s finance and insurance (F&I) desk (see below).

 **AgentCore Memory as bounded transaction state, not open-ended LTM.** Acquire’s session state — qualification result, payment status, contract state — is a bounded, resumable transaction ("working with a specific dealer on a specific reservation") with an explicit lifecycle: created → qualified → contracted → closed or abandoned. AgentCore Memory holds this transaction state for session-continuity purposes so a multi-turn financing conversation can resume without re-qualification, but it should be modeled as transaction state with that lifecycle, not as a generic persona snapshot extended with extra fields — the two have different retention, staleness, and correctness requirements. For a customer who already has an established identity (Discover Path B, Path C’s fleet business account, or a repeat individual buyer), the transaction state is additive to that existing persona or account snapshot; for a Discover Path A customer with no prior persona, the transaction record is the first durable state this customer has in AVX.

 **Nova 2 Sonic for voice-mediated Acquire.** If the acquire conversation continues in voice — for example, if it began as a voice conversation embedded in the OEM’s app during Discover Path A, or as an app-based voice session for Path B — the bidi AgentCore Runtime carries it over Nova 2 Sonic, the same speech-to-speech model the Service stage uses. An illustrative voice turn: *"Given my income and this trade-in, what’s my qualified rate range and monthly payment for the configuration I saved yesterday?"* The approximately 1-second tool-completion budget documented in [Agentic Architecture](agentic-architecture.md) matters especially at this stage — long-running partner API calls (in particular `finance_qualify()` against a captive finance arm or third-party decisioning partner, if slow) risk exceeding it. See [Agentic Architecture](agentic-architecture.md) for the mitigation pattern (async tool wrapping with a keep-alive signal during long waits).

 **Amazon Connect for compliance-load-bearing escalation to the dealer’s F&I desk.** This is the one place Amazon Connect legitimately enters the Acquire architecture — unlike Discover’s browse phase, a live handoff to a human during a regulated finance conversation is a real requirement. Escalation is a standard path at the Acquire stage: the LLM narrates and does not decide.

The **transport mechanism** is the same as Service’s escalation — `/escalate` starts a Connect chat with the context in contact attributes and a first message, and the receiving human agent sees it before answering. The **context payload**, however, is not the same, and should not be described as such: Service’s escalation (see [Stage 4 — Service](service-stage.md)) carries the triage classification, reason, VIN and vehicle, driver, and conversation summary — fields specific to vehicle diagnosis that have no bearing on a finance handoff. An Acquire escalation needs a distinct payload shape:
+  **Transaction state** — finance segment, qualification tier and rate range if `finance_qualify()` has already returned a result, payment status if `payment_initiate()` is in flight, and which dealer or reservation record the session is tied to.
+  **Consent and disclosure record** — what the customer explicitly consented to (credit pull, stated income disclosure) and what the agent told them, timestamped — a regulated-lending conversation carries an audit requirement Service’s safety-triage handoff does not.
+  **The specific question that triggered escalation** — verbatim, not summarized, since it is often the exact wording of an unusual credit-history question or a contract-terms question that determines whether the F&I specialist needs additional information before answering.

Service’s contact attributes have no field for qualification tier, consent record, or dealer reference. To add the Acquire handoff, add an `escalationType` for finance and the attributes above, within Connect’s 32 KB attribute limit; reusing Service’s attributes as they are does not cover it.

The receiving party is the **dealer’s finance and insurance (F&I) desk**, not a generic OEM-level tier-2 queue — the dealer is who actually closes finance deals in most OEM retail models. (OEMs that sell direct-to-consumer rather than through an independent dealer network route to an OEM-side finance desk instead; the tenant config’s queue-ARN entry determines which, so this is a routing choice per tenant, not an assumption baked into the architecture.) See [Contact Center Integration](contact-center-integration.md) for the Connect queue configuration. The agent’s role is to present partner-API and dealer-system outputs accurately and to route to a licensed human specialist when the customer has questions the agent cannot safely answer.

 **What comes next.** On successful acquisition completion, the STAR-compatible `VehicleOwnershipTransfer` payload writes across the ADP cross-account boundary into the ADP Vehicle Lifecycle data product. The moment that write is durable is the moment a prospective customer becomes an owner.

 **Cognito identity resolution — the mechanism, not just the outcome.** For a customer who already had a Cognito identity (Path B, Path C, or a Path A visitor who authenticated mid-Discover), this is straightforward: the existing `sub` is attached to the new VIN in ADP Customer 360, and the customer’s onward relationship becomes Onboard / Own’s familiar LTM-hydrated model. For a Discover Path A customer who stayed anonymous through the entire lead-to-sale flow, no Cognito identity exists yet, and "establishing one with certainty" requires an explicit step this IG has not previously named: a `resolve_or_create_owner_identity()` tool, invoked at `VehicleOwnershipTransfer` completion, that:

1. Looks up the lead record’s contact info (email or phone) against existing Cognito users in the OEM’s user pool.

1. If a match exists — the customer already had an account for another reason, or authenticated at some point in the Discover-to-Acquire flow without AVX’s session tracking it through to this step — links the new VIN to that existing `sub`.

1. If no match exists, provisions a new Cognito user from the lead record’s contact info, with the customer completing verification (email/SMS confirmation) at the point their account is first surfaced to them — typically the app-download or first-login prompt that follows a purchase.

1. Writes the resulting `sub`-to-VIN link to ADP Customer 360, which is what makes the customer discoverable to every downstream stage.

Without this explicit resolution step, a Path A customer’s sale closes but no AVX-native account exists to receive Onboard’s session-init LTM hydration — the STAR write to ADP records the sale, but nothing bridges it to a Cognito identity the customer can actually log into. This is genuinely new tool surface, not a byproduct of the `VehicleOwnershipTransfer` write itself.

Every downstream stage (Onboard / Own, Service, eventual Sell / Trade-in) can find their vehicle in ADP from this point forward. This is the same STAR-JSON convention the Service stage uses for `book()`, applied to a different record type and a different destination.

 **Data wiring.** 
+  **ADP Vehicle Lifecycle** — records the transition from inventory to titled ownership, which downstream stages (Onboard, Service, Warranty) depend on. The `book` tool writes the completed sale event to this product via a STAR-compatible `VehicleOwnershipTransfer` payload.
+  **ADP Customer 360** — links the customer identity to their new vehicle and anchors the LTM persona context that all future interactions will draw on. The `sub`-to-VIN link written by `resolve_or_create_owner_identity()` is what makes this linkage possible for a Path A customer.

 **Agent tools to implement.** 

Finance workflows must be deterministic at the decision boundaries — the LLM narrates, but qualification decisions are made by certified systems the OEM or dealer already operates. Implement four tool shells:

1.  `finance_qualify()` — calls the OEM’s captive finance arm as the primary integration; falls through to a third-party credit-decisioning API (FICO, Experian, or a credit union) within the same conversation on a decline or an unaccepted subprime tier — a per-customer runtime decision, not a static OEM-level configuration choice. The tool accepts customer consent plus stated income/employment and returns a qualification tier and available rate range for each lender it queries. The LLM presents each result conversationally; it does not interpret or modify either decisioning output.

1.  `payment_initiate()` — initiates a refundable online reservation deposit only (not the full purchase payment) via Stripe or Plaid (or the tenant’s payment processor). The tool returns a transaction reference that anchors the STAR-format acquisition record. Full purchase payment is collected by the dealer’s DMS as part of `reservation_handoff()`, not by this tool.

1.  `reservation_handoff()` — hands off a reservation and pre-qualification package to the dealer’s DMS for e-contracting. Returns a signed-contract reference once the dealer’s DMS confirms completion.

1.  `resolve_or_create_owner_identity()` — invoked at `VehicleOwnershipTransfer` completion. Looks up the customer’s contact info against the OEM’s Cognito user pool; links the new VIN to an existing account if found, or provisions a new account and returns a verification prompt if not. This is the mechanism a Discover Path A customer needs to become a durable, loggable-in AVX identity — it does not happen automatically as a side effect of the STAR write.

 **Compliance and safety guardrails.** Finance workflows are regulated in most jurisdictions. Apply Bedrock Guardrails to block the agent from making specific credit offers, guaranteeing approval, or providing personalized financial advice. The agent’s role is to present partner-API and dealer-system outputs accurately and to route to a licensed human specialist when the customer has questions the agent cannot safely answer. P0-style safety logic applies here: if the customer’s question exceeds the agent’s safe scope, `escalate()` to the dealer’s F&I desk (or the OEM-side finance desk for direct-to-consumer tenants).

 **Partner and system integration points.** 


| Domain | Integration Target | Integration Pattern | 
| --- | --- | --- | 
| Credit decisioning (primary) | OEM captive finance arm (the manufacturer-owned finance company pattern common among major automakers) | REST API call from `finance_qualify()` tool; already-regulated underwriting system operating outside AVX | 
| Credit decisioning (secondary) | Third-party lenders (illustrative: FICO, Experian, a credit union) — used within the same conversation on a captive-arm decline or unaccepted subprime tier, or as the sole path for OEMs without a captive finance arm | REST API call from `finance_qualify()` tool on decline fallthrough; tenant provides API key \+ decisioning product ID via tenant config | 
| Payments (reservation deposit only) | Payments partner (illustrative: Stripe, Plaid, or the tenant’s payment processor) | REST API call from `payment_initiate()` tool; scoped to a refundable online hold, not the full purchase amount | 
| Contract execution \+ full purchase payment | Dealer’s existing DMS e-contracting (illustrative: Reynolds, CDK Global, Tekion) | Reservation/pre-qualification package handoff from `reservation_handoff()` tool; the dealer’s DMS collects the full purchase payment as part of the same in-dealer transaction; signed-contract reference returned once confirmed | 
| Escalation | Dealer’s F&I desk (or OEM-side finance desk for direct-to-consumer tenants) | Amazon Connect `StartChatContact`; the tenant config’s contact flow and queue determine routing | 


|  |  | 
| --- |--- |
| Building blocks | The deterministic Acquire handlers `finance_qualify`, `payment_initiate` and `reservation_handoff` (`lambdas/acquire/`), the `resolve_or_create_owner_identity()` tool, AgentCore Runtime and Memory, Nova 2 Sonic, and the Connect `escalate()` transport. Finance-domain integrations (OEM captive finance arm, payments partner, dealer DMS e-contracting) use each tenant’s own API credentials and endpoints. | 
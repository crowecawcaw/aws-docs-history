

# Stage 5 — Sell / Trade-in
<a name="sell-trade-in"></a>

The vehicle’s complete service history, accumulated via CMS and ADP throughout the ownership tenure, is the data foundation for end-of-ownership transactions. At this stage, the primary Tier 2 agent is Agent 4 (Household Mobility Concierge), which maintains a continuous ownership-position picture and signals when the conditions for a trade-in or upgrade are favorable.

## Agent 4 — ownership position and trade-in readiness
<a name="agent-4-ownership-position-and-trade-in-readiness"></a>

Agent 4 runs on a continuous-position trigger and on equity-threshold and finance-milestone events. It reads equity and valuation data from ADP (vehicle condition score and partner market comparables), the owner’s finance or lease state, household vehicle graph, driver profiles, and loyalty standing, and writes two Finding kinds:
+  `concierge.position` — the owner’s current ownership picture: equity level, remaining finance term, loyalty standing, and household vehicle overview.
+  `concierge.trade_in_timing` — triggered when an equity threshold or lease-maturity date is crossed; includes an indicative trade-in range and a recommended next step.

The Tier 1 read tool is `get_ownership_position()`. When the broker delivers a `concierge.trade_in_timing` Finding and the owner taps the card, the resulting Tier 1 session opens with the ownership-position evidence already in context.

## Trade-in valuation
<a name="trade-in-valuation"></a>

Trade-in valuation is a capability of Agent 4, not a separate agent. The output is an **indicative range** derived from ADP vehicle-condition data and partner market comparables. It is not a binding offer.

Two controls apply to every valuation.

 **M8 — mandatory verbatim disclosure.** The surface attaches the disclosure text from `disclosure_txt` in the Finding verbatim. The supervisor presents the disclosure text word for word; it does not paraphrase it.

 **M14 — mock-provenance guard.** Every valuation input carries a `provenance` field: `live` (drawn from a current market-data API), `mocked` (a placeholder used during configuration or testing), or `absent` (the data source was unavailable at evaluation time). When any comparable input carries `provenance: mocked` or `provenance: absent`, the surface has two safe options, configured per tenant: withhold the monetary figure, or display it watermarked as illustrative only. The vehicle condition score, which is derived from the vehicle’s own history and does not depend on market comparables, is always safe to display and renders separately regardless of comparable provenance. The `disclosure_txt` field states which part of the estimate comes from live data and which is estimated.

## Commerce handoff
<a name="commerce-handoff"></a>

When an owner acts on a trade-in or upgrade, Agent 4 triggers a `retail` executor action that calls the Acquire `lead_capture` tool with the ownership-position context pre-populated. This re-enters the Discover / Acquire flow from a warm start: a resolved identity, a vehicle with complete service history in ADP, and a valuation in hand.

A `commerce_handoff()` tool integrates with a commerce marketplace platform via a tenant-configured partner API, using the ADP Vehicle Lifecycle and service-history data to populate a trade-in valuation request or a certified listing. This follows the same partner-integration pattern used in the Acquire stage.


|  |  | 
| --- |--- |
| Building blocks | STAR-shaped service history in the ADP Vehicle Lifecycle data product, built up through the Service stage. Agent 4’s valuation Findings carry per-input `provenance` and the M8 disclosure in the shared Finding schema; the M14 guard sits in the read path that renders them (`get_ownership_position()`). Commerce integration adds a `commerce_handoff()` tool following the partner-integration pattern in [Extend and Customize](extend-and-customize.md). | 
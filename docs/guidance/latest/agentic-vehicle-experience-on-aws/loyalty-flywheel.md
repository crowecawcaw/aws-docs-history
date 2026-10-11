

# The loyalty flywheel — four autonomous agents
<a name="loyalty-flywheel"></a>

The four agents address different points in the ownership lifecycle. Five more agents work for fleet operators and product engineers; see [Fleet Intelligence agents](fi-agents.md). Agent 1 covers daily energy use and cost. Agent 2 covers vehicle health and service. Agent 3 covers coverage entitlements and loyalty. Agent 4 covers household mobility position.


| \# | Agent (`agent_id`) | Trigger | Reads | Tier 1 read tool(s) | 
| --- | --- | --- | --- | --- | 
| 1 | Energy & Charging Advocate (`agent-1-energy`) | Daily per VIN; charging-session end; tariff change | ADP charging history, energy usage, battery SoH, telemetry range, ambient temperature, tariff and weather feeds, tenure |  `get_energy_advice()`  | 
| 2 | Vehicle Health & Service Agent (`agent-2-vehicle-health`) — tires, brakes, battery | ADP prediction / alert arrival; DTC event; telemetry threshold; service-interval approach; daily per component | ADP tire predictions \+ alerts, battery `state_of_health_pct`, brake intervals / DTCs / recalls from the vehicle knowledge base, DTC history, service records, service-network capacity, parts |  `get_health_findings()`; `book()` commits against the agent’s service plan | 
| 3 | Ownership Cost & Coverage Advocate (`agent-3-ownership-cost`) | Service event; warranty verdict change; recall publication; tenure milestone; daily prepaid sweep | DMS warranty claims, ADP recalls, loyalty ledger (prepaid balance, goodwill, credits), tenure, service adherence, referrals |  `get_coverage()`, `get_loyalty_standing()`  | 
| 4 | Household Mobility Concierge (`agent-4-concierge`) | Continuous position; finance milestone; household change; equity threshold | Equity / valuation (ADP condition \+ partner market comps), finance / lease state, household vehicle graph, driver profiles, loyalty standing |  `get_ownership_position()`  | 

## Agent 1: Energy & Charging Advocate
<a name="agent-1-energy"></a>

For an all-electric fleet, charging is the highest-frequency ownership event. Agent 1 reads that data daily and produces Findings about range, battery health, and charging cost.

 **Goal**: minimize running cost and range anxiety for each owner’s actual usage pattern.

 **Example Finding**: the owner’s winter range is down 20%, the Finding explains that this is within the expected temperature coefficient for the vehicle — not a battery fault — and recommends no action. This avoids an unnecessary service visit.

 **Finding kinds**: `energy.range_context`, `energy.battery_context`, `energy.charging_plan`.

 **Severity guidance**: Agent 1 does not emit `p0`. Any stop-driving condition routes through the deterministic triage classifier. Range advisories are `informational`; battery check-ins are `routine` or `attention`.

 **Seam with Agent 2**: Agent 1 covers how the owner uses and charges the vehicle. Agent 2 covers whether the vehicle is mechanically sound.

 **Executor hints**: `none` (advisory, audit only), `chat` (drill-down conversation), `vehicle-command` (charge-schedule adjustment via CMS remote commands).

## Agent 2: Vehicle Health & Service Agent
<a name="agent-2-vehicle-health"></a>

Agent 2 covers the complete service arc for a vehicle issue: detect → explain → price → apply coverage → find a slot → book → follow up. The arc stays with one agent because the meaningful split is between data-platform predictions and agent-side reasoning — not between detection and scheduling.

 **Goal**: no vehicle health issue surprises the owner, and acting on it is straightforward.

 **Component bundling**: when a tire alert arrives, Agent 2 checks whether brake or battery attention is also due, prices the combined visit, and proposes a single appointment. The owner approves once; the `dms` executor creates the repair order.

 **EV brakes**: for electric vehicles, the main brake failure mode is rotor corrosion from regenerative braking underuse — not pad wear. Agent 2’s reasoning accounts for this and explains it clearly to owners used to pad-wear framing.

 **P0 embed**: when a Finding involves a P0-severity item, the `headline` field contains the verbatim phrase from the triage classifier. The agent adds context; it does not rephrase the classifier’s output.

 **Service plans**: Agent 2 writes proposed service plans to `vsa-{stage}-service-plans`. The `book()` tool commits against this plan rather than creating an unconnected ticket.

 **Fleet vehicles first**: each nightly component takes the managed fleet vehicles in its priority pool first (`cms_ingest.vin_cms_fleet`, tier `managed`), then sweeps the rest of the population with what is left of its cap, so every managed vehicle is checked every night. The Findings keep their shape: VIN-scoped and informational, with no `recommended_action`, so owners keep their health cards. The fleet-health agent reads them as one of its inputs and books the work ([Fleet Intelligence agents](fi-agents.md)).

 **Finding kinds**: `health.tires`, `health.brakes`, `health.battery`.

 **Executor hints**: `dms` (creates repair order on approval, stores `avx_action_id`, receives status updates from `dms.ro.status_changed` events), `chat` (drill-down conversation pre-seeded with evidence), `vehicle-command` (charge-schedule adjustment after battery work).

## Agent 3: Ownership Cost & Coverage Advocate
<a name="agent-3-ownership-cost"></a>

Agent 3 is the only agent that writes `discount_applied` in a Finding. When Agent 2 identifies a coverage question — does the tire fall under warranty? does the prepaid plan cover it? — Agent 3 resolves it and writes the authoritative answer.

 **Goal**: the owner does not pay for something already covered, and earned loyalty benefits apply at the right time.

 **Warranty verdicts**: Agent 3 narrates DMS warranty verdicts verbatim. The exact verdict text — "Your repair is approved" or "Your repair is denied" — is carried through unchanged. The agent may add context (cost breakdown, coverage window, next steps) but does not rephrase the verdict itself.

 **Loyalty ledger**: Agent 3 owns `vsa-{stage}-loyalty-ledger`. Prepaid-maintenance balances, goodwill items, referral credits, and tenure-milestone benefits are tracked and applied here.

 **Finding kinds**: `coverage.warranty_gap`, `coverage.recall_open`, `coverage.prepaid_expiring`, `coverage.verdict_followup`, `loyalty.standing`, `loyalty.credit_expiring`.

 **Executor hints**: `none` (advisory, audit only), `retail` (extended-coverage purchase), `dms` (recall work, apply prepaid balance), `chat` (coverage explanation conversation).

## Agent 4: Household Mobility Concierge
<a name="agent-4-concierge"></a>

Agent 4 tracks household vehicle position over time — financing state, equity, household composition, driver profiles — and identifies when circumstances make a vehicle change worth considering.

 **Goal**: give the owner an accurate view of their current automotive position and reduce friction for a future Meridian purchase.

 **Portable identity**: Meridian OS driver profiles, preferences, IVE packages, and loyalty standing are tied to the owner identity, not the vehicle. The next Meridian inherits them. Agent 4 makes that continuity visible in its Findings.

 **Trade-in valuation**: Agent 4 provides indicative trade-in ranges, not offers. Every `concierge.trade_in_timing` or `concierge.position` Finding that includes a monetary figure must carry `disclosure_txt` with the mandatory verbatim disclosure. See [Deterministic Seams and Guards](ap-deterministic-seams.md).

 **Mock-provenance guard (M14)**: Agent 4 blends internal condition signal (ADP service history, DTC history, `state_of_health_pct`) with external market comparables from a partner comps seam. Each evidence entry carries `provenance: live | mocked | absent`. When the comps seam returns mocked data, the customer-visible surface either omits the monetary figure or labels it as illustrative. The internal condition score can still render, since it comes from real ADP data. The default behavior is to omit rather than display an unverified figure.

 **Onboarding advisories**: Agent 4 covers the first 90 days of ownership with connected-services activation, IVE package setup, and charging-habit advisories.

 **Finding kinds**: `concierge.position`, `concierge.trade_in_timing`, `concierge.onboarding`.

 **Executor hints**: `none` (advisory), `chat` (drill-down conversation), `retail` (approve → Acquire `lead_capture` and `configurator_recommend`).
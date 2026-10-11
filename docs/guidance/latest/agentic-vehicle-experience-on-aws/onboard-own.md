

# Stage 3 — Onboard / Own
<a name="onboard-own"></a>

Once a vehicle is purchased, the Onboard / Own stage spans the entire ownership tenure. At Onboard, the agent establishes the vehicle’s digital identity, activates connected services, and orients the owner to their vehicle’s features. During the Ownership phase, the agent delivers proactive outreach — maintenance reminders, recall notifications, energy-usage insights for EVs — without waiting for the owner to call.

## Vehicle identity and connected-services setup
<a name="vehicle-identity-and-connected-services-setup"></a>

 **Data wiring.** The first act of onboarding is resolving the vehicle to a rich identity record. Wire the agent to the ADP Vehicle Identity Graph via the `vehicle_identity()` tool. A call with the new VIN decodes year/make/model/trim, powertrain, factory-fitted features, and certified-pre-owned status. This record anchors every downstream interaction; without it the agent operates in a reduced mode.

Also at onboarding:
+ Write the vehicle and customer record to CMS DynamoDB (`vehicles` and `drivers` tables). This is the registration step that enables live-state reads (Redis LKS) and service-history accumulation from this point forward.
+ Activate the tenant’s connected-service subscription via the Zuora integration (if applicable). The `subscription_activate()` tool calls the Zuora API and records the activation in ADP Customer 360.

 **Session-init LTM hydration.** AgentCore Memory LTM is the mechanism that makes every future conversation context-aware without requiring the customer to re-introduce themselves. At onboarding, populate the LTM with the persona’s initial data snapshot:

1. Invoke the cross-account Lake Formation query to pull vehicle identity, initial service records (if a CPO), and customer profile from ADP Athena tables.

1. Write these as metadata-tagged LTM records keyed by `persona_id` and `vehicle_id`.

1. Set the LTM TTL to match your tenant’s policy (default 15 minutes for cache freshness; longer TTLs reduce Athena cost at the expense of staleness).

On every subsequent session, the session-init flow re-hydrates the LTM automatically, so the agent greets the customer with current vehicle context on the first turn.

![The Home tab in the sample iOS app: a personalized greeting, a critical vehicle alert banner, the owner’s vehicle with its connection status, quick actions (Controls, Health, Book service, Ask Meridian, Explore), and vehicle state such as odometer, fuel level, engine temperature, and trip count.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-ios-vehicle-home.png)


## Proactive engagement
<a name="proactive-engagement"></a>

Proactive engagement at the Onboard / Own stage is driven by two Tier 2 agents — Agent 1 and Agent 4 — that write Findings to `vsa-{stage}-avx-findings` on schedules and events. The outreach broker (`vsa-{stage}-avx-broker`) reads the Findings stream and decides which channel to use for delivery; neither agent calls a channel API directly.

 **Agent 1 — Energy and Charging Advocate.** Agent 1 runs daily per VIN and on charging-session-end events. It reads ADP charging history, energy-usage data (battery state of health), telemetry range, ambient temperature, and tariff feeds, and writes three Finding kinds:
+  `energy.range_context` — distinguishes seasonal range variation from a hardware fault. For example: an owner’s Meridian Windrose range reduction in winter is within the normal temperature curve, not battery degradation. Range advisories carry `severity: informational`.
+  `energy.battery_context` — battery state-of-health check-ins that flag a deviation from the degradation model. These carry `severity: routine` or `severity: attention` and route to the `chat` or `dms` executor based on the finding.
+  `energy.charging_plan` — tariff-aware charging schedule recommendations.

Agent 1 does not emit P0 severity. Any condition that requires the owner to stop driving goes through the `triage()` classifier in the Tier 1 supervisor. The Tier 1 read tool is `get_energy_advice()`.

 **Agent 4 — Household Mobility Concierge (onboarding findings).** Agent 4 covers the first 90 days of ownership with `concierge.onboarding` Findings. These are orientating advisories specific to the vehicle model: first tire rotation interval, charging-profile setup, available OTA update schedule, and Cognito account linkage confirmation. At day 90 the onboarding scope closes and Agent 4 transitions to `concierge.position` and `concierge.trade_in_timing` Findings described in [Stage 5 — Sell / Trade-in](sell-trade-in.md).

 **Channel selection and consent.** The broker applies the owner’s per-category consent (safety, coverage, service), quiet-hours policy, frequency caps, and cardinality limits before dispatching to any channel. Informational energy advisories surface as in-app cards. Attention-level battery findings may trigger an iOS push that deep-links into a pre-seeded Tier 1 conversation with the Finding’s evidence already loaded. Device-token registration and per-category consent are managed in `vsa-{stage}-notification-devices` via `POST /notifications/register-device`.


|  |  | 
| --- |--- |
| Building blocks | Vehicle identity resolution (`vehicle_identity()`), session-init AgentCore Memory hydration, push-device registration (`POST /notifications/register-device`), Agent 1 (`agent-1-energy`) and Agent 4 (`agent-4-concierge`) on the Tier 2 platform with their read tools `get_energy_advice()` and `get_ownership_position()`, and the outreach broker (`vsa-{stage}-avx-broker`). Subscription-management partner integration (illustrative: Zuora) uses tenant-specific API credentials. | 

## Ownership advisory Findings as cards
<a name="ownership-advisory-findings-as-cards"></a>

Agents 1, 2, 3 and 4 produce the ownership-stage Findings in the table below. Every Finding routes through the outreach broker before it reaches a channel.

 **Ownership Finding kinds.** 


| Finding kind | Agent | Trigger | Card headline | CTA | 
| --- | --- | --- | --- | --- | 
|  `concierge.onboarding`  | 4 | New owner within the first 90 days; specific to the vehicle | "Welcome: Your First 90 Days" | "View Checklist" → first service, tire rotation, account setup | 
|  `concierge.position`  | 4 | Lease or subscription end date within 60 days (ADP Vehicle Lifecycle) | "Lease Ends in 45 Days — Plan Ahead" | "Review End-of-Lease Options" → renewal and upgrade offers | 
|  `coverage.warranty_gap`  | 3 | Warranty coverage entering its final month or final 1,000 miles | "Powertrain Warranty Expires Next Month" | "Review Extended Warranty Options" → `retail` executor | 
|  `loyalty.subscription_renewal`  | 3 | Connected-services subscription renewal approaching, or free trial ending | "Complimentary Connected Services Ending" | "Extend Service" → subscription renewal flow | 
|  `energy.battery_context`  | 1 | Battery state of health or range drop outside the expected curve for the temperature and tenure | "Your Winter Range Drop Is Normal" | "See Why" → drill-down conversation | 
|  `health.software_update`  | 2 | OTA software update available for the vehicle (ADP Vehicle Lifecycle) | "Software Update Available: V2.1 → V2.2" | "Install Update" or "Schedule Installation" | 

 **Delivery and customer interaction.** 

Ownership Findings are delivered via:
+  **Mobile app cards** — appear in the "Milestones" or "Ownership" section (distinct from the "Alerts" section where reactive Service Findings appear).
+  **Email digest** — weekly or monthly summary (tenant-configurable) of upcoming milestones, warranty expirations, and renewal reminders.
+  **In-vehicle notifications** — for time-sensitive events like OTA campaign availability, if the OEM’s connected-vehicle API supports it.

Customer interaction is the same as Service cards: tap to expand, tap CTA button to act, or dismiss. For Ownership Findings, CTAs typically lead to in-app educational content, renewal/upgrade flows, or partner integrations — not operational actions like "Book Service."
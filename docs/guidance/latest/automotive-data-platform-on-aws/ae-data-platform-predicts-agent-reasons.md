

# ADP’s role: the data platform predicts, the agent reasons
<a name="ae-data-platform-predicts-agent-reasons"></a>

The patterns described above — grounding a customer-facing agent, enabling business-user queries, and delivering proactive briefings — all share a common architectural seam. ADP’s role in the agent-plus-data-platform system is to **predict and emit statistical inferences**. The consuming agent’s role is to **reason about what those inferences mean** and decide what to do.

This boundary is not a limitation; it is the correct design. Statistical inference and judgment are fundamentally different things, and confusing them inside a single component is where agentic systems break.

## The inference layer: ADP’s tire predictive-maintenance stack
<a name="the-inference-layer-adps-tire-predictive-maintenance-stack"></a>

ADP’s tire health monitoring is the canonical example. The tire predictive-maintenance stack — located at `guidance-for-predictive-maintenance/source/lambda/daily_tire_check`, `guidance-for-predictive-maintenance/source/lambda/realtime_blowout_risk`, `guidance-for-predictive-maintenance/source/lambda/transform_predictions_to_alerts`, and `guidance-for-predictive-maintenance/source/lambda/alerts_processor` — performs statistical inference on aggregated telemetry. It ingests vehicle signal data from the `vehicle_telemetry_aggregated` data product, which contains normalized vehicle sensor readings including odometer, speed, acceleration, tire pressure, and temperature. The stack’s ML model runs statistical inference to predict tire health degradation, identifies blowout risk, and emits structured alerts with a specific signal: **"left front tire, 8,000 km to remaining life threshold; slow leak suspected."** 

That signal carries a statistical probability, not a judgment. It says what the data suggests is happening, not what the owner should do about it.

## The judgment layer: what the agent decides
<a name="the-judgment-layer-what-the-agent-decides"></a>

When that prediction reaches a consuming agent — whether a fleet operator’s real-time alert dashboard, a vehicle owner’s proactive recommendation, or a service advisor’s next-visit planner — the agent makes the judgment call. The agent decides:
+  **Is this prediction relevant to this owner right now?** — perhaps the vehicle is leased and tire replacement is the lessor’s responsibility, or perhaps the owner is already scheduling maintenance.
+  **Does it combine with other findings?** — the same agent might surface a brake inspection due at 10,000 km, a warranty-expiring service at 12,000 km, and a recall investigation that requires a dealer visit. The judgment is whether to group them, defer some, or escalate.
+  **When is the moment to raise it?** — the data predicts a problem; the agent decides whether now is the right time to recommend action, or whether the owner should hear about it at the next scheduled service instead.
+  **What does the owner’s coverage look like?** — ADP’s `vehicle_knowledge_base` data product contains warranty terms, service-contract coverage, and recall definitions; the agent threads this through to tell the owner what they pay and what the OEM covers.

The tire prediction itself is deterministic — the ML model produces the same output for the same telemetry every time. The judgment of what to do with it is not. That judgment lives with the agent, not with the data platform.

## Why this boundary exists
<a name="why-this-boundary-exists"></a>

Asking the data platform to decide what action an owner should take is a category error. The data platform does not know the owner’s preferences, budget constraints, vehicle usage patterns, or warranty status. It is designed to emit accurate, governed, reproducible inferences — not to reason about human decision-making.

Equally, asking an agent (especially a latency-sensitive conversational agent) to re-run statistical inference inside a tool call is wasteful and fragile. The tire-prediction model trains on months of telemetry, requires GPU compute, and produces outputs meant to be cached and reused across multiple queries. Running inference inside a Tier 1 conversational loop would break both performance and the architecture.

The `tire_health` data product codifies this boundary. It is ADP’s inference layer — a set of periodic predictions that feed into alerts, recommendations, and structured findings. Consuming agents subscribe to it and make judgment decisions on top of the platform’s predictions. The platform does not make the judgment; it makes the prediction and emits the evidence.

## ADP’s reference pattern for Tier 2: the scheduled briefing agent
<a name="adps-reference-pattern-for-tier-2-the-scheduled-briefing-agent"></a>

The scheduling agent pattern described in [Example 3 — Proactive executive briefings, not dashboards](ae-worked-example-quick.md) illustrates this exact principle in pattern form. When deployed, the scheduled agent **would** run on a cadence with no human waiting. It **would** reason across multiple ADP data products to answer standing business questions, **compare** each cycle’s answer to the prior cycle to detect change, and **deliver** synthesized insights to decision-makers. In this pattern, the agent would operate in Tier 2 — it would own a goal, reason across multiple steps, and write a reasoned artifact (the briefing, with its evidence) that Tier 1 consumers (a human executive or a downstream system) would then read and act on. For the current state of this pattern in the reference implementation, see the `Demonstrated in [repo]::` note in that same section, which records the scheduled-agent layer as the unimplemented consumer step.

The tire predictions and the briefing-agent pattern demonstrate two sides of the same principle: ADP provides the governed, reproducible inferences and data products that make the judgment layer possible. An agent (conversational or scheduled) makes the judgment and decides what the inference means for this specific situation.


# Deterministic-first P0–P3 triage
<a name="triage-classifier"></a>

AVX classifies every vehicle interaction on a four-level criticality taxonomy **before** the LLM composes a response. Classification is a **tool call**, not a free-form LLM judgment. This is a safety invariant: the LLM can narrate a classification but cannot change it.

## Criticality taxonomy
<a name="criticality-taxonomy"></a>


| Level | Meaning | Default action | Examples | 
| --- | --- | --- | --- | 
|  **P0 — Stop driving**  | Safety-critical fault; risk of injury or loss of vehicle control | Pull over immediately, said word for word; offer a human chat and roadside assistance, each one tap | Brake failure, airbag fault, overheating, loss of steering assist, SRS deployment | 
|  **P1 — Service now**  | Active DTC in degraded operating mode; measurable risk if ignored more than 24–48 hours | Schedule service within 48 hours; create STAR ticket; offer **Talk to an agent**  | Active catalyst-efficiency fault with active `CHECK_ENGINE`, coolant temperature above threshold, transmission slip code | 
|  **P2 — Service soon**  | Non-critical DTC, wear indicator, or open recall | Schedule service within 1–2 weeks; create STAR ticket; educate caller | Minor emissions code, brake-pad wear indicator, NHTSA recall outreach | 
|  **P3 — Monitor**  | Informational; reset conditions documented; no immediate action required | Log; educate caller; no ticket created unless caller requests | Tire pressure within tolerance, fuel-economy advisory, routine maintenance reminder | 

## Deterministic-first rule engine
<a name="deterministic-first-rule-engine"></a>

The triage classifier executes as a deterministic rule engine, not as an LLM prompt. Inputs:
+ Active DTC codes with severity flags from the vehicle’s OBD-II data
+ Telemetry threshold breaches (coolant temperature, brake-wear sensor, tire pressure delta, battery voltage)
+ Open NHTSA recall IDs for the VIN
+ Tenant policy overrides (for example, a fleet operator may escalate any P1 to roadside by default)

The classifier returns a structured result:

```
{
  "level": "P1",
  "reason": "Active DTC P0420 (catalyst efficiency below threshold) in degraded mode.",
  "inputs_consulted": ["dtc:P0420", "telemetry:catalyst_monitor_ready:false"],
  "tenant_override_applied": false,
  "recommended_action": "Schedule service within 48 hours."
}
```

The LLM receives this result as a tool output and uses it to compose the spoken response. It cannot modify the `level` field. This is enforced at the system-prompt level and — for P0 — additionally at the safety guardrail layer (Bedrock Guardrails prevents any LLM output that could be interpreted as "continue driving" when the triage level is P0).

## Safety invariant: P0 is irrevocable
<a name="safety-invariant-p0-is-irrevocable"></a>

 **The LLM cannot downgrade a P0 classification.** On a P0:

1. The instruction to pull over safely is delivered immediately and word for word. It is never held back waiting for a tap.

1. The driver is offered two one-tap actions: talk to a human agent in a Connect chat on the tenant’s chat queue, and request roadside assistance (if the tenant has a roadside partner configured). Roadside dispatch sends physical equipment and false-positive P0s exist (sensor faults), so the driver confirms it. A tenant whose duty-of-care rules require it can make either action automatic with `escalation.autoOpenHumanChatOnP0` or `escalation.autoRequestRoadsideOnP0`; both default to `false`.

1. Suppression of any DIY guidance — the safety guardrail blocks all responses that include repair steps when criticality is P0.

This invariant holds regardless of anything in the conversation transcript or the caller’s stated preference. If the caller insists "it’s probably fine", the agent acknowledges the concern and restates the P0 recommendation without changing the classification.

### Roadside-assistance dispatch: simulated provider
<a name="roadside-assistance-dispatch-simulated-provider"></a>

Roadside-assistance dispatch goes through a provider client shaped like a real vendor API. On a P0 with the tenant configured for roadside dispatch, `/escalate` writes a request to the `vsa-{stage}-rsa-dispatch` DynamoDB table with `simulated: true`, a stream consumer moves the row through the `REQUESTED → DISPATCHED → EN_ROUTE → ARRIVED` (or `FAILED`) state machine, and the tenant-scoped `GET /rsa/dispatch/{dispatchId}` route returns the current status. Every stored row and every status response carries the `simulated` marker so surfaces cannot silently present the simulator as a real dispatch; a `VSA_RSA_CLIENT=real` mode raises on every call. The reference provider is a simulator; connecting a roadside vendor replaces the provider client.

## Tenant policy overrides
<a name="tenant-policy-overrides"></a>

Two tenant flags in the `vsa-tenant-config` record’s `escalation` block change what happens on a P0, and both default to `false`:
+  `escalation.autoOpenHumanChatOnP0` opens the human chat without waiting for the driver’s tap, for fleets whose duty-of-care rules require a human on the line.
+  `escalation.autoRequestRoadsideOnP0` requests roadside assistance without the tap.

The flags act after the deterministic classification. They change what follows a P0; they cannot change the classification level.
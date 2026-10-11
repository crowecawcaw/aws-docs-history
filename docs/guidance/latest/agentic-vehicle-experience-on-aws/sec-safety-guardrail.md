

# The P0 safety guardrail
<a name="sec-safety-guardrail"></a>

The P0 safety guardrail is AVX’s most consequential security control. It governs the boundary between autonomous AI response and mandatory human escalation for safety-critical vehicle situations.

## What P0 means
<a name="sec-p0-definition"></a>

P0 — "Stop driving" — covers situations in which the vehicle presents an immediate physical safety risk to occupants or other road users: brake-system failures, overheating conditions that risk engine seizure or fire, airbag deployment faults, and loss of power-steering assist. The DTC severity catalog and telemetry-threshold table that define the P0 classification set are deterministic tables in the AVX codebase, not model-inferred labels.

## The safety invariant
<a name="sec-p0-invariant"></a>

**Important**  
A P0 classification always delivers the stop-driving instruction immediately and word for word. The language model cannot downgrade, override, reframe or withhold it. Roadside assistance and a human agent are offered as one-tap actions, or happen automatically when the tenant enables `escalation.autoRequestRoadsideOnP0` or `escalation.autoOpenHumanChatOnP0`.

The invariant is enforced structurally, not by prompt instruction:

1. The triage tool executes as a tool call that returns a structured classification record containing `{"severity": "P0", "reason": "<DTC codes and thresholds that fired>", "recommended_action": "pull_over_and_call_roadside"}`.

1. On a P0, the supervisor runtime sends the stop-driving instruction to the client itself, as a platform message, and asks the model for the same words. The model may not soften, restate or omit it.

1. The client shows a recommendation card with **Request roadside** and **Talk to an agent**. The driver’s tap reaches `/escalate`, which opens a Connect chat on the tenant’s chat queue, routed at high priority, with the triage reason, VIN, vehicle, driver and summary attached, and, for **Request roadside**, writes the roadside dispatch record.

1.  `/escalate` performs P0 side effects (roadside dispatch, the outbound callback) only for the vehicle’s assigned driver, verified from the caller’s identity token. The chat stays open to anyone.

1. The chat flow’s P0 branch does not return to the IVR or to any automated node; it routes directly to a human agent.

The model is the narrator, not the decision-maker, for P0 outcomes. It translates the deterministic classification into a clear, calm instruction to the driver and presents the handoff options. It does not assess whether the classification "makes sense" or hedge with phrases like "it might be okay to continue driving."

## Why the LLM cannot downgrade P0
<a name="sec-p0-no-downgrade"></a>

Deterministic safety rules and probabilistic language models serve different functions in AVX’s architecture. The triage classifier consults DTC severity codes, telemetry thresholds, recall data, and tenant policy overrides — all structured, auditable inputs — and produces a classification that is reproducible given the same inputs. A language model, by contrast, generates plausible text conditioned on context and cannot guarantee that a safety-critical signal is never rationalized away under an unusual prompt framing or an unusually confident model response.

Allowing the model to override P0 would make the safety boundary probabilistic. The AVX design makes it structural: the escalation path is triggered by a data value in a tool response, not by the model’s judgment about that value.
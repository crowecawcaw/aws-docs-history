

# Request and data flow
<a name="arch-request-flow"></a>

Regardless of the entry channel, every AVX interaction follows the same high-level flow.

## Channel ingress
<a name="arch-flow-channels"></a>

A request enters AVX through one of four channels:
+  **Voice (Amazon Connect \+ Nova 2 Sonic)** — the caller’s speech is streamed to the AgentCore bidi runtime. Amazon Nova 2 Sonic performs speech-to-speech transcription and synthesis within the runtime container. The supervisor receives the transcribed text; its response is synthesized back to speech before being streamed to the caller.
+  **Chat (Amazon Connect Chat)** — text messages from the Connect Chat widget arrive at the supervisor via a Lambda integration. The response is returned as text.
+  **Web / mobile** — a `POST` to the REST API endpoint `{vsaApiEndpoint}/assistant/chat` carries the user prompt, session ID, and VIN. The Cognito authorizer validates the caller’s JWT and injects verified claims into the Lambda context; the Lambda proxy infers the persona server-side from `cognito:groups` and `custom:role` claims, and forwards to the text AgentCore runtime.

## Supervisor orchestration
<a name="arch-flow-steps"></a>

Once the supervisor receives an utterance, it executes the following sequence:

1.  **Session context load** (first turn only) — `persona_loader` pre-fetches ADP tabular data via cross-region Athena and seeds the result into AgentCore Memory LTM. On subsequent turns within the session, all persona context is read from Memory without Athena round trips.

1.  **Live state read** — for vehicle-linked sessions, the supervisor reads the Redis LKS snapshot from CMS. This snapshot includes active DTCs, telemetry readings, and open-recall flags. The snapshot is attached to the session context and passed as structured arguments to tools that need it.

1.  **Intent classification and triage** — for any message that references vehicle symptoms, warning lights, or service urgency, the supervisor calls `triage()` first. The triage result constrains the rest of the turn: a P0 result delivers the stop-driving instruction word for word and offers the driver a human agent and roadside assistance, each one tap; P1 and P2 results shape the urgency framing of the booking recommendation.

1.  **Domain tool dispatch** — based on intent and triage result, the supervisor dispatches to the relevant domain tools (`vehicle_identity()`, `knowledge()`, `parts_lookup()`, `service_network()`). Tool calls are sequential by default and parallel where dependencies allow; Strands' native tool-call streaming returns partial results as they arrive.

1.  **Booking or escalation** — if the interaction reaches a booking decision point, the supervisor calls `book()`. If it reaches an escalation trigger (P0, customer request, policy exception), it calls `escalate()`.

1.  **Response synthesis** — the supervisor synthesizes a grounded response from tool results. For voice, Nova 2 Sonic streams audio back to the caller. For text/web/chat, a JSON response carries the assistant text, triage classification, VIN, and citation references.

## Grounding data path
<a name="arch-flow-grounding"></a>

AVX’s two grounding surfaces are architecturally independent:
+  **Tabular data (AgentCore Memory LTM)** — ADP Athena queries → session-init LTM seed → per-turn metadata-filtered Memory Retrieve. Latency: \~6–7 seconds for session-init; sub-100ms for per-turn Memory reads.
+  **Reference data (Bedrock KB Retrieve)** — cross-account resource policy → Bedrock Retrieve with source-category filter → top-k passage retrieval from the Amazon S3 Vectors index. Latency: 200–600ms per Retrieve call, depending on index load and query complexity.

If Memory is unavailable or returns no records, tools return structured unavailable messages; the session degrades gracefully without a hard failure. If KB Retrieve fails, the `knowledge()` tool returns an error trace and the supervisor informs the customer that reference lookup is temporarily unavailable.

## Tier 2 trigger and artifact flow
<a name="arch-tier2-flow"></a>

Tier 2 agent flows run independently from the Tier 1 request-response path. An EventBridge Scheduler rule or event rule fires the trigger; a Lambda invokes the agent module; the agent queries ADP Athena tables or DMS APIs; the result is written to `vsa-{stage}-avx-findings`; the DynamoDB stream fires the outreach broker. No customer session is open during this flow.

The Tier 1 flow intersects the Tier 2 platform at two points:

1.  **Finding read tools** — `get_energy_advice()`, `get_health_findings()`, `get_coverage()`, `get_loyalty_standing()`, and `get_ownership_position()` retrieve the most recent Finding for the current session’s scope from `vsa-{stage}-avx-findings` via DynamoDB point reads. The supervisor calls these tools the same way it calls any other domain tool; the result is a pre-computed conclusion with evidence attached, not a live reasoning call.

1.  **Proactive session entry** — when the broker delivers a push notification and the owner taps it, the mobile client issues a `POST /assistant/chat` with `avx_finding_id` in the body. The supervisor loads the referenced Finding’s evidence into session context before the first response, so the conversation opens at the Finding’s depth.
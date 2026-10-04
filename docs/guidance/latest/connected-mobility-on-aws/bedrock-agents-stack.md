

# Conversational fleet assistant
<a name="bedrock-agents-stack"></a>

The in-UI conversational assistant that surfaces in the Fleet Manager is **not** deployed by any stack in this repository. It is deployed by the companion Agentic Vehicle Experience (AVX) accelerator, and CMS consumes it by pointing the Fleet Manager web application at the AVX API endpoint. This section describes only the CMS-side integration surface; the supervisor agent, its specialist tools, and the AgentCore runtimes are owned by AVX.

**Note**  
The Virtual Fleet Operator (VFO) Bedrock multi-agent stack and its supporting Fleet Command Center UI were retired in the v0.4.0 release. The fleet-view landing surface it fed is now rendered deterministically by the CMS-native Fleet Intelligence services (see [Fleet Intelligence](fleet-intelligence.md)). No `cms-{stage}-bedrock-agents` stack is deployed today; the retired `make deploy-bedrock-agents` target survives only as a no-op stub for backward compatibility with continuous integration callers.

## Amazon Bedrock AgentCore runtime
<a name="bedrock-agents-agentcore-runtime"></a>

The conversational assistant is surfaced in the Fleet Manager UI through two Amazon Bedrock AgentCore runtimes deployed from the companion Agentic Vehicle Experience (AVX) repo:
+  **Bidirectional (voice)** — `vsa_supervisor_bidi_staging` — WebSocket-based streaming for voice interactions in the iOS companion app.
+  **Text (HTTP)** — `vsa_supervisor_text_staging` — HTTP unary runtime used by the Fleet Manager web UI `/assistant/chat` endpoint.

The Fleet Manager UI `ChatAgent` component calls `/assistant/chat` on the AVX API Gateway (resolved from the `vsaApiEndpoint` field in `runtimeConfig.json`). AVX proxies the request to the AgentCore text runtime, which invokes the supervisor agent. Persona is inferred from Cognito claims: `fleet_driver` is the default; a `custom:role=service-advisor` claim selects the service-advisor persona.

## Cross-account ADP Knowledge Base retrieval
<a name="bedrock-agents-adp-kb"></a>

The AVX supervisor agent grounds its responses in the Automotive Data Platform (ADP) Knowledge Base — vehicle-specific diagnostic trouble code guides, maintenance bulletins, and recall notices — retrieved through cross-account `bedrock:Retrieve` calls. Both the knowledge base identifier and the cross-account trust are configured on the AVX side; CMS does not carry any Bedrock agent IAM. Operators who prefer to run without the assistant can leave `runtimeConfig.json’s `vsaApiEndpoint` unset — the chat panel then reports the assistant as not configured and the rest of the Fleet Manager application continues to function normally.
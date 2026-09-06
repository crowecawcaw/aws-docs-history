

# Conversational fleet assistant (BedrockAgentsStack)
<a name="bedrock-agents-stack"></a>

The BedrockAgentsStack is an optional, opt-in deployment (`make deploy-bedrock-agents`) that provisions the Bedrock multi-agent system powering the Fleet Manager in-UI conversational assistant. It is not included in `deploy-all` and can be added to an existing deployment at any time.

## Agent architecture
<a name="bedrock-agents-architecture"></a>

The stack deploys one supervisor agent and four specialist agents, all using the `us.anthropic.claude-sonnet-4-6` cross-region inference profile.

 **Specialist agents:** 
+  `cms-cost-agent` — Analyzes fleet cost and total cost of ownership queries.
+  `cms-maintenance-agent` — Answers maintenance schedule and vehicle health questions.
+  `cms-rebalancing-agent` — Provides fleet utilization and rebalancing recommendations.
+  `cms-recall-warranty-agent` — Surfaces recall and warranty information for enrolled vehicles.

 **Supervisor agent (`cms-virtual-fleet-operator`):** 

The supervisor receives user questions from the Fleet Manager UI, determines which specialist to invoke (or answers directly), and assembles the final response. Specialists are wired as agent collaborators in the supervisor configuration.

## Amazon Bedrock AgentCore runtime
<a name="bedrock-agents-agentcore-runtime"></a>

The conversational assistant is surfaced in the Fleet Manager UI through two Amazon Bedrock AgentCore runtimes deployed from the companion CVX repo:
+  **Bidirectional (voice)** — `vsa_supervisor_bidi_staging` — WebSocket-based streaming for voice interactions in the iOS companion app.
+  **Text (HTTP)** — `vsa_supervisor_text_staging` — HTTP unary runtime used by the Fleet Manager web UI `/assistant/chat` endpoint.

The Fleet Manager UI `ChatAgent` component calls `/assistant/chat` on the CMS API Gateway, which proxies to the AgentCore text runtime. Persona is inferred from Cognito claims: `fleet_driver` is the default; a `custom:role=service-advisor` claim selects the service-advisor persona.

## IAM — inference-profile and foundation-model ARNs
<a name="bedrock-agents-iam"></a>

Bedrock cross-region inference requires two separate IAM `PolicyStatement` resource entries. Using the wrong ARN form for either entry prevents model invocation.

 **Inference-profile ARN (includes account ID):** 

```
arn:aws:bedrock:*:{account}:inference-profile/us.anthropic.claude-sonnet-4-6
```

This ARN grants permission to use the cross-region inference profile within the account. The `{account}` placeholder must be the 12-digit AWS account number where the profile is registered. The wildcard region (`*`) permits the inference profile to route requests across regions within the account.

 **Foundation-model ARN (no account ID):** 

```
arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-6
```

This ARN grants permission to invoke the underlying foundation model in whichever region the inference profile dispatches to. Notice the empty account segment (`::`) — including an account ID in this ARN causes authorization failures because foundation-model resources are not account-scoped.

Both statements must grant `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream`, because the Bedrock Converse API uses streaming internally.

## Cross-account ADP Knowledge Base retrieval
<a name="bedrock-agents-adp-kb"></a>

When the ADP Knowledge Base (identified by its knowledge base ID, deployed in the Automotive Data Platform account) is configured, the agent role receives an additional `bedrock:Retrieve` policy statement scoped to the cross-account KB ARN. This enables the supervisor to ground responses in vehicle-specific knowledge articles (diagnostic trouble code guides, maintenance bulletins, recall notices) retrieved from the ADP OpenSearch Serverless index.

The KB ID and ADP account ID are injected at deploy time via CDK context flags. The ADP account must grant the CMS agent role trust via a resource-based policy on the KB.
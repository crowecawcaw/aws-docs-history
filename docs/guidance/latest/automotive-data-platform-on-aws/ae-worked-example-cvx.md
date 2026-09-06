

# Example 1: Grounding a customer-facing agent
<a name="ae-worked-example-cvx"></a>

The Connected Vehicle Experience (CVX) accelerator contains a production implementation of a customer-facing vehicle service agent grounded on ADP’s `vehicle_knowledge_base` data product. This section describes the integration pattern demonstrated there. It is a reference implementation, not a prescriptive architecture — it is not the only way to build an agent on ADP, and deploying this ADP foundation does not require deploying CVX.

**Note**  
CVX is in progress and not yet available as a public accelerator. The pattern described in this section — cross-account Bedrock Knowledge Base Retrieve, grounding-transparency as a system-prompt rule — is stable and safe to build against today; only the CVX accelerator’s own public availability is pending.

## The agent architecture
<a name="the-agent-architecture"></a>

The CVX supervisor agent is built with [Strands](https://github.com/strands-agents/sdk-python), an open-source agentic framework, backed by Claude Sonnet 4.6 as the language model, served via Amazon Bedrock. The Strands `Agent` class wraps the model, the registered tools, and a system prompt that encodes the agent’s behavior rules. The BedrockModel constructor takes a model ID (a cross-region inference profile ARN), a region, and a max-tokens budget — these come from environment variables so the deployment can swap models or regions without code changes.

The agent registers three tools per session: `triage`, `retrieve`, and `book`. The `retrieve` tool is the cross-account knowledge base integration — it calls Amazon Bedrock’s Knowledge Base Retrieve API against ADP’s `vehicle_knowledge_base` product, which is hosted in the ADP account. The `triage` tool classifies vehicle issues by severity (P0–P3). The `book` tool creates service tickets.

## Cross-account Bedrock Knowledge Base Retrieve
<a name="cross-account-bedrock-knowledge-base-retrieve"></a>

The knowledge base lives in the ADP AWS account. The CVX agent runs in a separate AWS account — the channel layer. Connecting them requires three configuration values that the agent reads from environment variables at startup:
+  `VSA_ADP_KB_ID` — the Bedrock Knowledge Base ID for ADP’s `vehicle_knowledge_base` product
+  `VSA_ADP_REGION` — the AWS region where the knowledge base is deployed (typically `us-east-1`)
+  `VSA_ADP_ACCOUNT_ID` — the AWS account ID of the ADP deployment; used to construct the cross-account IAM principal; if not set, the agent resolves it via STS `GetCallerIdentity` at startup

The account ID is treated as sensitive configuration: it is stored in a `repr=False` dataclass field so it does not appear in log output even if the config object is inadvertently printed. In production, all three values come from environment variables injected at deploy time; they are never hardcoded.

The cross-account Bedrock Knowledge Base Retrieve pattern requires the ADP account to grant the CVX agent’s execution role permission to call `bedrock:Retrieve` on the knowledge base resource. The `docs/cvx-integration-contract.md` file in the ADP repository documents the IAM resource policy and Lake Formation cross-account share configuration that enables this grant. That document is the authoritative technical contract between ADP and CVX; this section describes the pattern without duplicating its contents.

## Grounding-transparency hard rule
<a name="grounding-transparency-hard-rule"></a>

The CVX supervisor’s system prompt encodes a grounding-transparency requirement as a hard rule, not a suggestion. The rule, verbatim from the agent’s system prompt:

Grounding transparency: if you answer a factual question WITHOUT having called `retrieve` (or another KB-backed tool such as `knowledge`, `parts_lookup`, or `diy_repair_advisor`) in the current turn, you MUST prefix or suffix the answer with a short, explicit non-grounded disclosure — e.g. "From general knowledge (not retrieved from the vehicle knowledge base):". Never present model-recalled facts as if they came from the KB. This lets the operator see, from the response text alone, whether the answer is grounded.

This is a genuinely useful design pattern for any agent grounded on a knowledge base. Language models can answer questions about DTC codes, recalls, and service procedures from training data alone — and those answers may be outdated or incorrect for a specific vehicle model year. By requiring the agent to explicitly flag answers that come from model memory rather than retrieved documents, the operator can tell at a glance whether a given response was grounded in the governed knowledge base or in the model’s prior training. The disclosure is visible in the response text and does not require log inspection.

The rule also covers the triage-first discipline: the agent must call the `triage` tool before narrating any criticality level to the user, and must call `retrieve` before answering any question involving a recall, a DTC code, a warranty term, or a service procedure. The agent narrates results; tools make decisions.

## What this demonstrates
<a name="what-this-demonstrates"></a>

This pattern demonstrates two things that are independently useful for any team building an agent on ADP:

1.  **Cross-account Bedrock KB Retrieve as the ADP↔agent boundary** — the knowledge base is the governed, subscription-based surface through which the agent consumes ADP data. The agent does not query ADP’s Glue databases or S3 lake directly; it retrieves pre-indexed knowledge from the Bedrock KB product. This separation of concerns means ADP can evolve the underlying lake without changing the agent’s access pattern, and the agent can be redeployed or replaced without touching the ADP data layer.

1.  **Grounding-transparency as an operational pattern** — requiring agents to explicitly disclose non-grounded answers is a practical approach to the problem of AI systems that confidently answer questions from training data when they should be retrieving from a governed source. The disclosure text appears in the response itself, making it auditable without additional tooling.

For the 17 sample SQL blocks and detailed Athena query patterns that define the full ADP↔CVX data contract, see `docs/cvx-integration-contract.md` in the ADP repository. This chapter describes the grounding pattern; that document is the executable technical contract.
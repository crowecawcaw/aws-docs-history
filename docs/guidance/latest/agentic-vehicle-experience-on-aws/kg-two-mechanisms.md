

# Two grounding mechanisms
<a name="kg-two-mechanisms"></a>

## Bedrock Knowledge Base RAG
<a name="kg-bedrock-kb"></a>

The ADP-hosted Bedrock Knowledge Base backs the `knowledge()` tool and, for parts-related queries, the `parts_lookup()` tool. It is the right choice for content that is:
+  **Unstructured or semi-structured** — diagnostic guides, Technical Service Bulletins (TSBs), recall notices, owner manuals, service policy documents, parts catalog narratives. This content cannot be expressed as DynamoDB rows or Athena columns without losing contextual meaning.
+  **Reference in nature** — it describes how things work, what a diagnostic code means, what a recall requires, or what a service policy permits. It is written once and read many times; the query pattern is semantic ("what does this DTC mean?") rather than exact lookup ("what is this vehicle’s mileage?").
+  **Updated independently of agent code** — new recall bulletins, revised TSBs, and updated manuals are added to the S3 content source, the Knowledge Base is re-synced, and the agents immediately reflect the new content without any code change or runtime redeployment.
+  **Shared across tenants at some content levels** — NHTSA recall bulletins apply across all tenants; VSS catalog content is generic across the automotive domain. Centralizing this content in a shared KB layer avoids duplication and ensures consistency.

The Knowledge Base is backed by an Amazon S3 Vectors index. Content is chunked, embedded using Amazon Titan Embeddings, and stored per document with metadata tags (document type, source category, applicable persona roles). At query time, a Bedrock Retrieve API call returns the top-k semantically matched passages. Results are passed as grounding context to the supervisor, which synthesizes a persona-appropriate response.

## AgentCore Memory metadata-tagged LTM
<a name="kg-agentcore-memory"></a>

AgentCore Memory backs the tabular, per-persona data that defines the specific customer, vehicle, and relationship being served in a given session. It is the right choice for content that is:
+  **Structured and row-oriented** — vehicle identity records, service records, charging sessions, customer profile, interaction history. Each record has a stable primary key (VIN, customer ID) and a defined schema.
+  **Session-personalized** — the same agent handles many sessions simultaneously, but each session sees only the records for the specific persona and vehicle scoped to that interaction. LTM isolation is enforced by `actor_id` and metadata-filter tags.
+  **Loaded once per session, read many times per turn** — at session initialization, the `persona_loader` pre-fetches the relevant ADP Athena records and seeds them into AgentCore Memory under the session’s `actor_id`. Subsequent tool calls within the session retrieve records from Memory with sub-100ms latency, without re-querying Athena on every turn. This bounds both cross-region data-transfer cost and per-turn latency.
+  **Sourced from ADP data products** — the tabular content in LTM originates from ADP Glue tables queried via Lake Formation v4 cross-account grants. AVX never writes to ADP; it reads ADP data into session-scoped Memory at the start of each session.

**Note**  
The `vehicle_telemetry_aggregated` and `energy_usage` products depend on the `PySpark via Glue` data pipeline in ADP. The corresponding tools (`telemetry_summary`, `energy_summary`) are deployed and query AgentCore Memory; until the upstream ADP Glue tables are registered, the `persona_loader` skips the Athena fetch and each tool returns `{"available": false}`.

## Choosing the right mechanism
<a name="kg-choosing"></a>

The decision rule is simple and should be applied when designing any new grounding path:


| Question | Bedrock Knowledge Base | AgentCore Memory LTM | 
| --- | --- | --- | 
| Is the content unstructured or document-form? | Yes — use KB | No — use Memory for tabular data | 
| Does it vary per customer or per vehicle? | No — use KB for shared reference | Yes — use Memory (session-scoped by actor\_id) | 
| Is it updated independently of agent code? | Yes — KB S3 sync is code-free content update | No — Memory is seeded per session from live ADP data | 
| Is the query semantic ("what does X mean")? | Yes — KB RAG matches semantic queries | No — Memory serves exact-key record retrieval | 
| Is the record reused across many turns in the session? | Sometimes — KB is called per tool invocation | Yes — Memory reduces Athena re-query cost across turns | 

In practice, the two mechanisms complement each other in the same response. A service advisor asking "is this DTC covered under the vehicle’s warranty?" requires Memory (vehicle identity and warranty record loaded at session init) AND a KB Retrieve call (`source_category=service_policy`, `source_category=dtc_guide`). The supervisor synthesizes a single answer from both sources.
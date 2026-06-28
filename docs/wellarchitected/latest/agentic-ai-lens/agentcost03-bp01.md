# AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory

Agent memory has to serve two opposing needs at once: fast access
for active context, and cheap storage for history that is rarely
touched. Tiered memory matches each class of data to infrastructure
priced for its actual access pattern, and selective retrieval keeps
token costs proportional to what the current task needs.

**Desired outcome:**

- You have short-term working memory on high-performance storage
  and long-term memory on cost-effective tiers, with automatic
  lifecycle transitions between them.
- You retrieve only top-K relevant items per reasoning step rather
  than loading full memory stores into context.
- You track retrieval operations per session and use the data to
  tune tier assignments and access patterns.

**Common anti-patterns:**

- Storing all agent memory in expensive high-performance storage
  regardless of access frequency, incurring unnecessary costs for
  rarely accessed historical interactions.
- Retrieving entire memory stores for each reasoning step,
  consuming excessive input tokens when targeted top-K retrieval
  would suffice.
- Using single-tier storage for all memory regardless of access
  pattern, wasting resources on uniform infrastructure for data
  with distinct access profiles.
- Deploying memory systems without retrieval cost monitoring,
  hiding inefficient access patterns inside aggregate session
  cost.

**Benefits of establishing this best
practice:**

- Tiered storage matches each memory category to its access
  pattern, reducing costs for historical data without sacrificing
  active session performance.
- Selective top-K retrieval limits context to the most pertinent
  items, avoiding token charges for irrelevant historical data.
- Automated tier lifecycle management scales across thousands of
  sessions without manual intervention or over-provisioning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The cost of agent memory comes from two decisions: where data
lives and how much of it you pull into the model's context window.
[Amazon
Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") handles the first decision as a
managed service. Short-term memory stores turn-by-turn session
context on fast storage, while long-term memory extracts and
consolidates key insights across sessions into cheaper tiers.

For agents on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md"), this removes the need to build
storage tiers and promotion policies by hand. When a custom
implementation is required, define explicit promotion and demotion
policies based on access frequency so frequently accessed items
stay on low-latency storage and rarely accessed items migrate to
lower-cost tiers automatically.

Retrieval volume is the second decision, and it has a direct
effect on input token cost.
[Amazon
Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") provides managed vector retrieval
with semantic search. _K_ (the number of chunks
returned per query) is the central cost-quality knob: higher K
gives the agent more context but pushes more tokens into every
invocation. Start with K=5 and tune against the
trade-off between completeness and cost, not from a preference for
safety.

Index design is a less obvious but still important cost
consideration. For
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/ "https://aws.amazon.com/opensearch-service/features/serverless/")-backed Knowledge Bases, HNSW
parameters (ef\_construction and
m) balance index build cost against query
accuracy and recall. OpenSearch Serverless charges based on
indexed data volume and query compute, so tuning these parameters
is a direct cost decision, not just a quality decision. Higher
ef\_construction values improve recall but raise
both build and query cost, while lower values reduce cost but risk
missing relevant items.

Additionally, consider retrieval batching. Pre-fetching the full
task context at initiation and caching it in the agent's working
memory avoids per-step retrieval overhead.
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") provides
OpenTelemetry-compatible telemetry that identifies which retrieval
patterns drive the most token consumption, and Amazon CloudWatch Logs Insights queries reveal access patterns that should inform
tier reassignments.

### Implementation steps

1. **Adopt managed tiered
   memory:** Integrate
   [Amazon
   Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") for short-term and long-term
   memory with automatic lifecycle management, and document
   which namespaces each agent writes to and reads from.
2. **Configure selective
   retrieval:** Use
   [Amazon
   Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") with top-K semantic search,
   starting at K=5 and tuning based on observed reasoning
   quality and token cost.
3. **Tune vector index
   parameters:** Adjust HNSW ef\_construction and m on
   the
   [Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/ "https://aws.amazon.com/opensearch-service/features/serverless/") backing store to balance index
   build cost, query latency, and recall accuracy for your
   workload.
4. **Pre-fetch context at task
   initiation:** Replace per-step retrievals with a
   single batch pre-fetch at task start, cached in working
   context so the model doesn't pay retrieval overhead on every
   reasoning step.
5. **Instrument retrieval
   operations:** Enable
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") and set Amazon CloudWatch alarms when retrieval frequency exceeds expected
   bounds per session.
6. **Review access patterns
   weekly:** Run CloudWatch Logs Insights queries to
   reveal expensive retrieval patterns and never-accessed
   items, and use the results to reassign tiers and retire dead
   entries.

## Resources

**Related best practices:**

- [AGENTCOST01-BP02
  Optimize multi-agent collaboration cost through efficient
  handoff patterns](agentcost01-bp02.md "agentcost01-bp02.md")
- [AGENTCOST02-BP03
  Use intelligent caching to reduce redundant model
  invocations](agentcost02-bp03.md "agentcost02-bp03.md")
- [AGENTCOST03-BP02 Cost
  optimize through intelligent compression and pruning of
  context windows](agentcost03-bp02.md "agentcost03-bp02.md")
- [AGENTCOST03-BP03
  Implement cost-optimized state persistence and lifecycle
  management](agentcost03-bp03.md "agentcost03-bp03.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md")
- [Amazon
  Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md")
- [Economics
  for agentic AI on AWS](../../../prescriptive-guidance/latest/agentic-ai-economics/index.md "../../../prescriptive-guidance/latest/agentic-ai-economics/index.md")
- [Guidance
  for Cost Analysis and Optimization with Amazon Bedrock
  Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/ "https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/")

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA "https://www.youtube.com/watch?v=-N4v6-kJgwA")
- [AWS 2025 - AgentCore Memory: Episodic Memory & Patterns](https://www.youtube.com/watch?v=1EEIGsKIjGA "https://www.youtube.com/watch?v=1EEIGsKIjGA")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Memory
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory")

**Related workshops:**

- [Getting
  started with Amazon Bedrock AgentCore - Lab 2: Memory](https://catalog.workshops.aws/agentcore-getting-started/en-US/30-add-memory "https://catalog.workshops.aws/agentcore-getting-started/en-US/30-add-memory")
- [Diving
  Deep into Bedrock AgentCore - Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory "https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")

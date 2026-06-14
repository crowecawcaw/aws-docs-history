# AGENTSUS02-BP01 Optimize context management and memory utilization

Agent memory that grows without bounds forces every retrieval to
search through increasingly large stores and every turn to reprocess
history the agent has already seen. Tiered memory with retention
policies keeps infrastructure scaled to the context that actually
matters, so memory operations stay fast and memory cost stays
proportional to use.

**Desired outcome:**

- You have tiered memory with active session context separated
  from archival data, so hot and cold tiers are not competing for
  the same storage.
- Retention, archival, and pruning policies keep memory bounded
  and automatically move aging context to the appropriate tier.
- Multi-agent systems share persistent context through namespaces
  rather than duplicating it per agent.
- Agents incrementally build context rather than reprocessing full
  interaction histories on every turn.

**Common anti-patterns:**

- Implementing flat memory without tiering, so hot session context
  competes with archival data for the same storage and access
  path.
- Skipping retention, archival, and pruning policies, letting
  memory accumulate indefinitely and forcing each retrieval to
  scan a larger and larger store.
- Reprocessing complete historical context on every turn instead
  of pulling only the relevant slice, producing redundant
  retrieval operations that don't improve response quality.
- Duplicating shared context across each agent's memory store
  rather than reading from a shared namespace, producing linear
  storage growth with agent count.

**Benefits of establishing this best
practice:**

- Memory infrastructure scales with the context that actually
  matters, not with cumulative history.
- Semantic retrieval returns the relevant slice of context in
  constant time rather than scaling with store size.
- Multi-agent systems share storage for common context, reducing
  duplicated memory across the fleet.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Not all agent context is equally active. A recent turn in an
ongoing session behaves very differently from a transcript from
three months ago. The first needs millisecond access on every
turn, and the second needs availability for occasional retrieval.
[Amazon
Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") provides built-in tiering that
separates these cases, with working memory optimized for active
sessions and long-term storage for older context. Retention
policies move context between tiers automatically, so the hot tier
stays small and the cold tier stays cheap.

Shared persistent context is a part of the architecture where many
multi-agent systems fail. When five agents each maintain their own
copy of the same reference material, storage grows five times
faster than the organizational demand warrants. AgentCore Memory's
namespace-based organization lets multiple agents read from and
write to common namespaces scoped by IAM policies, one store and
many readers. This is shared storage, not shared in-process
memory, so consistency and access control stay explicit.
Separately,
[Amazon
Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") is the right home for
organizational knowledge, FAQs, and reference documentation that
agents query to enrich context. It complements AgentCore Memory
rather than replaces it.

Sending the full interaction history into every model call looks
correct but pays to reprocess information the model already saw.

The better pattern is incremental. Maintain stateful sessions that
preserve working context across turns, summarize older segments
into compact representations when they age out of the immediate
window, and use semantic search through Knowledge Bases with
vector embeddings to retrieve only the relevant slice of history
rather than the whole transcript.
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") exposes which memory
operations are frequent and which tiers are under- or
over-utilized, so allocation stays grounded in actual usage.

### Implementation steps

1. **Configure tiered memory with
   lifecycle policies:** Use
   [Amazon
   Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") for active session context
   with retention policies that automatically move aging
   context to long-term storage.
2. **Set up shared namespaces for
   multi-agent context:** Create AgentCore Memory
   namespaces that multiple agents read from and write to,
   scoped by IAM policies, so shared persistent context is
   stored once rather than duplicated per agent.
3. **Use semantic retrieval for
   historical context:** Configure
   [Amazon
   Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") with vector embeddings so
   queries retrieve only the relevant slice of historical
   context rather than full transcripts.
4. **Compress aging context:**
   Apply summarization using Amazon Bedrock foundation models
   to condense older interaction segments into compact
   representations that preserve meaning at a fraction of the
   token cost.
5. **Monitor memory access patterns and
   rebalance tiers:** Track tier hit rates, retrieval
   latency, and store size through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") and adjust retention
   windows and tier allocations based on observed usage.

## Resources

**Related best practices:**

- [AGENTSUS02-BP02
  Establish efficient agent caching strategies](agentsus02-bp02.md "agentsus02-bp02.md")
- [AGENTSUS02-BP03
  Appropriately scale data, networking, and compute
  dependencies](agentsus02-bp03.md "agentsus02-bp03.md")
- [SUS02-BP01
  Scale workload infrastructure dynamically](../sustainability-pillar/sus_sus_user_a2.md "../sustainability-pillar/sus_sus_user_a2.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md")
- [Amazon
  Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/")
- [Building
  smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/ "https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/")
- [Amazon
  Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md")
- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA "https://www.youtube.com/watch?v=-N4v6-kJgwA")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Memory
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")

# Memory, context, and RAG optimization

Agentic AI systems depend on efficient access to contextual
information through short-term conversational memory, long-term
knowledge stores, retrieval-augmented generation pipelines, and
LLM context windows to produce accurate, relevant responses.
Memory and context management directly impacts both performance
and quality. Overstuffing context windows increases inference
latency and cost, and insufficient context leads to poor reasoning
and hallucination. Optimizing this layer requires implementing
tiered memory architectures that match storage and retrieval
characteristics to access patterns, managing context windows to
maximize information density without exceeding token limits,
designing RAG pipelines that retrieve relevant information with
minimal latency, and establishing caching strategies that reduce
redundant retrievals. These optimizations matter because memory
and context operations occur on every reasoning iteration, making
their efficiency a multiplier across the agent lifecycle.

| AGENTPERF03: How do you optimize memory management,<br>context windows, and retrieval-augmented generation? |
| ----------------------------------------------------------------------------------------------------------- |
|                                                                                                             |

## Capability intent

- Agent memory is organized into tiers that match storage
  technology to access pattern, so session reads and long-term
  semantic queries don't compete on the same hot path.
- Context windows are composed from discrete, budgeted
  components (system instructions, conversation history,
  retrieved knowledge, and tool schemas), with summarization,
  dynamic tool selection, and relevance-filtered retrieval
  keeping prompt size decoupled from session length.
- Retrieval-augmented generation pipelines combine semantic
  chunking, hybrid search, query transformation, and
  re-ranking so the agent receives precise context with
  sub-second latency on the first retrieval.
- Multi-layer caching (prompt prefixes, retrieval results,
  tool outputs) reduces redundant work across iterations and
  sessions, with TTLs and keys tuned per layer against
  measured hit rates and staleness tolerance.
- Retrieval is expressed as a set of agent-invoked tools with
  bounded iteration, sufficiency checks, and parallel
  sub-query execution so complex questions converge within the
  workload's latency budget.

## Maturity levels

These levels summarize what each stage of maturity looks like
for memory, context, and RAG optimization as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Memory, context, and retrieval are treated as<br>single-tier concerns. Full conversation history and the<br>entire tool catalog flow into every prompt, RAG chunks<br>are fixed-size with no relevance filtering, and no<br>caching exists beyond what individual services provide<br>by default. Token consumption and retrieval latency are<br>reviewed only after a cost spike or a user-reported<br>slowdown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2     | Emerging  | Teams have separated short-term from long-term memory<br>and adopted basic summarization of conversation history.<br>RAG is running through a managed service such as<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md"), and prompts are<br>structured so that system instructions and stable tool<br>definitions sit in a reusable prefix. Per-component<br>token usage and retrieval latency are measured for<br>production agents but tuning is still manual and<br>reactive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 3     | Defined   | Memory tiers use storage matched to access pattern, with<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") or<br>[Amazon ElastiCache](../../../AmazonElastiCache/latest/dg/WhatIs.md "../../../AmazonElastiCache/latest/dg/WhatIs.md") serving short-term state and<br>[AgentCore<br>Memory long-term strategies](../../../bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.md "../../../bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.md") or<br>[Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/application-agentic-memory.md "../../../opensearch-service/latest/developerguide/application-agentic-memory.md") serving cross-session<br>knowledge. RAG pipelines use semantic chunking, hybrid<br>search, and a re-ranking stage, with top-k caps and<br>per-passage thresholds enforced. Prompts compose with<br>[Amazon<br>Bedrock prompt caching](../../../bedrock/latest/userguide/prompt-caching.md "../../../bedrock/latest/userguide/prompt-caching.md"), and prompt templates are<br>versioned in<br>[Amazon<br>Bedrock Prompt management](../../../bedrock/latest/userguide/prompt-management-create.md "../../../bedrock/latest/userguide/prompt-management-create.md") with per-component<br>token budgets. |
| 4     | Proactive | Retrieval is expressed as a set of agent tools through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") with sufficiency<br>evaluation, bounded iteration, and parallel sub-query<br>execution for complex questions. Multi-layer caching is<br>active across prompt prefixes, semantic retrieval keys,<br>and tool outputs, with per-layer hit rates monitored<br>against floors. Memory extraction, eviction, and<br>prompt-template promotion run through automated<br>pipelines, and per-tier latency and cache hit rate feed<br>continuous tuning in<br>[Amazon CloudWatch generative AI observability](../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md "../../../AmazonCloudWatch/latest/monitoring/GenAI-observability.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 5     | Optimized | Memory tier sizing, retrieval budgets, and cache TTLs<br>are recalibrated continuously from production telemetry<br>rather than by scheduled review. Prompt components, tool<br>selection, and retrieval routing are evaluated through<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") gated in CI/CD, and<br>optimization patterns flow back to internal communities<br>of practice. The organization contributes memory and<br>retrieval patterns to the broader agentic AI community.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Common issues to watch for

- Teams store all agent memory in a single database regardless
  of access pattern, which forces sub-millisecond session
  reads and large-scale semantic searches to compete on the
  same backend and degrades both.
- Conversation history and the full tool catalog are included
  in every prompt without summarization or dynamic selection,
  so prompt size and latency grow linearly with session length
  even after the information stops being useful.
- RAG pipelines rely on fixed-size chunking and raw top-k
  passages without a re-ranking stage or per-passage relevance
  thresholds, diluting useful context with low-signal chunks
  that crowd out higher-signal passages.
- Caching is either absent or applied at a single layer with a
  single TTL, missing the stacked savings available when
  prompt prefixes, semantic retrieval keys, and tool outputs
  are cached independently with data-type-specific policies.
- Agentic retrieval loops run without iteration caps,
  sufficiency evaluation, or parallel sub-query execution,
  which either cuts off complex questions prematurely or lets
  iterations grow unbounded and consume the workload's latency
  budget.

###### Best practices

- [AGENTPERF03-BP01 Implement tiered memory management systems](agentperf03-bp01.md "agentperf03-bp01.md")
- [AGENTPERF03-BP02 Optimize context window utilization and prompt management](agentperf03-bp02.md "agentperf03-bp02.md")
- [AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision](agentperf03-bp03.md "agentperf03-bp03.md")
- [AGENTPERF03-BP04 Establish efficient agent caching and data access patterns](agentperf03-bp04.md "agentperf03-bp04.md")
- [AGENTPERF03-BP05 Implement agentic retrieval patterns for dynamic, agent-driven knowledge access](agentperf03-bp05.md "agentperf03-bp05.md")

# Agent memory and state cost management

Agents with well-tiered memory architectures maintain reasoning
quality while keeping storage and retrieval costs proportional to
actual usage rather than total history size. Agent memory systems
can become expensive through uncontrolled context accumulation,
inefficient retrieval patterns, and persistent state storage.
Long-running conversations consume growing context windows, and
episodic memory retrieval can trigger vector database queries on
every reasoning step.

| AGENTCOST03: How do you manage agent memory and state<br>costs efficiently? |
| --------------------------------------------------------------------------- |
|                                                                             |

## Capability intent

- Memory storage is aligned to access frequency, with active
  context on high-performance stores and historical data on
  lower-cost tiers.
- Retrieval is selective rather than bulk, so the tokens spent
  per reasoning step reflect the context that actually matters
  to the current task.
- Long-running sessions compress and prune history
  continually, keeping token cost sub-linear as conversation
  length grows.
- Session state and durable agent learning are persisted
  through managed lifecycle controls, helping prevent
  unbounded storage growth without discarding knowledge that
  improves future reasoning.
- Memory and state costs are observable per agent and per
  session, with alarms surfacing retrieval patterns and
  storage growth before they become material.

## Maturity levels

These levels summarize what each stage of maturity looks like
for agent memory and state cost management as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Memory is a single undifferentiated layer. Full<br>conversation history is passed into every invocation,<br>and there is no retrieval filtering, compression, or<br>lifecycle policy. Per-session memory and state cost<br>isn't measured, so token growth and storage growth are<br>detected only when a bill or context overflow forces the<br>issue.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2     | Emerging  | Short-term and long-term memory are separated, and a<br>basic rolling summarization keeps the longest sessions<br>from unbounded growth. Retrieval uses<br>[Amazon<br>Bedrock Knowledge Bases](../../../bedrock/latest/userguide/knowledge-base.md "../../../bedrock/latest/userguide/knowledge-base.md") or equivalent vector<br>search with a fixed top-K. Baseline dashboards expose<br>token usage per session, but tuning is one-time and<br>applied by individual teams.                                                                                                                                                                                                                                                                                                                        |
| 3     | Defined   | Tiered memory is the standard across agent teams, with<br>managed services such as<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") used for short-term and<br>long-term storage. Retrieval is relevance-scored, chunk<br>sizes are right-sized, and context utilization is<br>monitored against a defined target. Lifecycle policies<br>archive or purge stale state on<br>[Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") or equivalent, and<br>[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") dashboards cover most agents. |
| 4     | Proactive | Memory compression, pruning, and selective retrieval are<br>automated defaults, and session lifecycle parameters are<br>tuned per workload.<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") provides<br>per-agent and per-session cost attribution, with alarms<br>for context overflow, retrieval hot spots, and<br>unexpected storage growth. Vector index parameters and<br>top-K are reviewed regularly against recall and cost<br>data.                                                                                                                                                                                                                                |
| 5     | Optimized | Memory architecture is continuously optimized from<br>observed access patterns. Top-K, chunk size, tier<br>placement, and checkpoint frequency adapt to workload<br>signals rather than static configuration. Cost<br>regressions on memory and state are caught in<br>pre-production by automated checks against historical<br>baselines, and insights from operations feed back into<br>reasoning pattern and retrieval design.                                                                                                                                                                                                                                                                                                                                                                     |

## Common issues to watch for

- Memory is treated as a single undifferentiated store, so
  every byte pays high-performance storage rates regardless of
  whether it is ever read again.
- Full conversation history is injected into every invocation,
  causing token cost to grow linearly with session length and
  pushing long sessions toward context overflow.
- Retrieval is coarse and indiscriminate, returning large,
  low-relevance context when a smaller, relevance-scored
  result set would preserve reasoning quality at a fraction of
  the cost.
- Session state and durable memory accumulate without a
  defined lifecycle, leaving storage to grow indefinitely
  until a cost review forces reactive cleanup.
- Memory and state cost are invisible at the per-agent and
  per-session level, so regressions such as expensive
  retrieval patterns, unexpected state growth, and idle
  session bloat are detected only after they show up on an
  invoice.

###### Best practices

- [AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory](agentcost03-bp01.md "agentcost03-bp01.md")
- [AGENTCOST03-BP02 Cost optimize through intelligent compression and pruning of context windows](agentcost03-bp02.md "agentcost03-bp02.md")
- [AGENTCOST03-BP03 Implement cost-optimized state persistence and lifecycle management](agentcost03-bp03.md "agentcost03-bp03.md")

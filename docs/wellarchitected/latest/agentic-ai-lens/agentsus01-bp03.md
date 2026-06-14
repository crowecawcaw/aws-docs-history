# AGENTSUS01-BP03 Optimize resource utilization through shared services

Every agent that provisions its own connection pool, cache, or
processing queue pays the cost of infrastructure nobody else in the
fleet benefits from. Shared services turn those duplications into
one piece of infrastructure that every agent uses, so infrastructure
scales with organizational demand rather than agent count.

**Desired outcome:**

- You have common infrastructure, connection pools, caches, and
  processing queues, consolidated into shared service layers that
  every agent invokes rather than duplicates.
- Agents consume shared services through a tool abstraction, so
  implementations can change without coupling to the callers.
- Shared caching and pooling reduce the total number of redundant
  calls to external systems.
- Utilization of shared services is monitored so capacity scales
  with actual demand rather than theoretical peaks.

**Common anti-patterns:**

- Deploying a separate cache, connection pool, and queue per
  agent, so infrastructure cost scales linearly with agent count.
- Letting each agent open its own connections to external services
  and fetch the same reference data repeatedly, producing
  redundant network traffic and wasted compute.
- Treating each agent workflow as an isolated system, missing
  opportunities to consolidate common functions like
  authentication, logging, or queuing into a shared layer.
- Maintaining static allocations regardless of actual demand, so
  shared infrastructure carries peak capacity even during
  low-utilization periods.

**Benefits of establishing this best
practice:**

- A single optimization to shared infrastructure improves every
  agent that uses it, amortizing operational work across the
  fleet.
- Infrastructure investment grows with organizational demand
  rather than proportional to agent count.
- Dynamic scaling on shared components contracts resources when
  demand is low, which is hard to do when each agent runs its own
  isolated stack.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The infrastructure agents need is more repetitive than the work
they do. Authentication, caching, queuing, connection pooling, and
cross-agent retrieval all look the same no matter which agent is
calling them. When every agent provisions its own copy of this
plumbing, the organization pays for the same infrastructure N
times and optimizes it one team at a time. Consolidating into
shared layers reverses this. Infrastructure is optimized once and
every caller benefits.

A shared cache that agents call directly by host name creates
tight coupling. Swapping the implementation means updating every
caller. Exposing shared services through
[Amazon
Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") MCP server capabilities puts a
stable interface in front of the implementation. The cache tier,
queue backend, or connection pool can change without the agents
noticing.
[Amazon
Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md") centralizes authentication so
individual agents don't manage credentials independently, which is
the simplest form of shared infrastructure with immediate return.

For caching specifically, the implementation choice depends on the
data pattern.
[Amazon ElastiCache](../../../AmazonElastiCache/latest/UserGuide/BestPractices.md "../../../AmazonElastiCache/latest/UserGuide/BestPractices.md") fits general-purpose hot data with flexible
access patterns, and
[Amazon DynamoDB Accelerator (DAX)](../../../amazondynamodb/latest/developerguide/DAX.md "../../../amazondynamodb/latest/developerguide/DAX.md") fits DynamoDB-backed agent state
that needs microsecond reads without a separate cache layer. Both
are shared across agents once provisioned.
[Amazon
Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") distributes foundation model
requests across Regions so availability is shared at the inference
tier, not just at the application tier.

Deploy the agents themselves on
[Amazon
Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/runtime.md "../../../bedrock-agentcore/latest/devguide/runtime.md"). Its serverless model means there
is no infrastructure footprint for each agent to consolidate in
the first place, which complements the shared-services pattern on
the supporting tier.
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") exposes cache hit rates,
queue depth, and invocation frequency for each shared service, so
utilization data drives scaling decisions rather than theoretical
peak estimates.

### Implementation steps

1. **Identify common infrastructure
   needs:** List the plumbing duplicated across
   current deployments and consolidate each into a shared
   service layer:

   - Connection pools
   - Caches
   - Queues
   - Authentication

2. **Deploy shared caching:**
   Provision
   [Amazon ElastiCache](../../../AmazonElastiCache/latest/UserGuide/BestPractices.md "../../../AmazonElastiCache/latest/UserGuide/BestPractices.md") for general-purpose hot data or
   [Amazon DynamoDB Accelerator (DAX)](../../../amazondynamodb/latest/developerguide/DAX.md "../../../amazondynamodb/latest/developerguide/DAX.md") for DynamoDB-backed state,
   so frequently accessed data is read from one cache rather
   than refetched per agent.
3. **Expose shared services through a
   stable interface:** Publish shared infrastructure
   as MCP tools through
   [Amazon
   Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") so agents consume it
   without coupling to the implementation.
4. **Centralize
   authentication:** Use
   [Amazon
   Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md") to manage credentials once
   rather than having every agent manage its own.
5. **Distribute model
   inference:** Turn on
   [Amazon
   Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md") so foundation model
   capacity is pooled across Regions for availability.
6. **Track utilization and scale on
   data:** Monitor the following through
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), and adjust capacity
   based on observed usage rather than worst-case estimates:

   - Cache hit rates
   - Queue depth
   - Invocation patterns

## Resources

**Related best practices:**

- [AGENTSUS01-BP01 Design
  specialized agents with explicit resource boundaries](agentsus01-bp01.md "agentsus01-bp01.md")
- [AGENTSUS01-BP02
  Implement reusable workflow patterns](agentsus01-bp02.md "agentsus01-bp02.md")
- [SUS03-BP02
  Remove or refactor workload components with low or no
  use](../sustainability-pillar/sus_sus_software_a3.md "../sustainability-pillar/sus_sus_software_a3.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md")
- [Amazon ElastiCache best practices](../../../AmazonElastiCache/latest/UserGuide/BestPractices.md "../../../AmazonElastiCache/latest/UserGuide/BestPractices.md")
- [Amazon DynamoDB Accelerator (DAX)](../../../amazondynamodb/latest/developerguide/DAX.md "../../../amazondynamodb/latest/developerguide/DAX.md")
- [Amazon
  Bedrock cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md")
- [Strands
  Agents Tools](https://github.com/strands-agents/tools "https://github.com/strands-agents/tools")

**Related examples:**

- [GitHub:
  aws-samples/serverless-patterns](https://github.com/aws-samples/serverless-patterns "https://github.com/aws-samples/serverless-patterns")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")

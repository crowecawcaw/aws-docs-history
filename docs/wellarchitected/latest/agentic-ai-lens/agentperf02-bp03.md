

# AGENTPERF02-BP03 Optimize agent execution paths for reduced latency
<a name="agentperf02-bp03"></a>

 Most of an agent request's total latency time is spent waiting on model inference, retrieval, tool invocations, and memory lookups rather than on CPU work inside the agent process. Executing independent operations concurrently, reusing warm connections and runtimes, and deduplicating repeated lookups within a single request cut total latency without changing models or prompts. 

 **Desired outcome:** 
+  You have independent operations within an agent request executed concurrently sequential execution is reserved for operations with genuine data dependencies. 
+  You have connections to downstream services, model endpoints, tool APIs, memory stores, vector indexes, pooled and reused across requests rather than reestablished per invocation. 
+  You have runtime cold starts removed from the critical path or bounded through provisioned capacity, pre-warming, or persistent execution environments. 
+  You have repeated lookups within a single request resolved from a request-scoped cache, so duplicate work isn't paid twice inside one invocation. 

 **Common anti-patterns:** 
+  Executing independent operations sequentially when they share no data dependencies, making total latency the sum of operation durations rather than the slowest operation. 
+  Establishing new connections to model endpoints, tool APIs, or data stores on every invocation, paying connection setup and TLS handshake costs on the critical path. 
+  Running agent code on compute that pays a cold-start penalty on the critical path without provisioned capacity, pre-warming, or a persistent runtime to absorb it. 
+  Re-executing the same lookup multiple times within a single request, for example, fetching the same knowledge base passage or user profile across consecutive reasoning steps, with no request-scoped cache to deduplicate the work. 
+  Introducing parallelism without respecting downstream rate limits or connection pool capacity, so concurrent calls throttle or queue and the intended latency win turns into added latency plus failures. 

 **Benefits of establishing this best practice:** 
+  Overlapping independent operations makes the critical path track the slowest operation rather than the sum of every operation. 
+  Amortizing connection setup and runtime initialization across requests avoids paying those costs on every invocation. 
+  Parallel calls that respect downstream capacity avoid the throttling and retry storms naive parallelism triggers. 
+  Overlapping I/O-bound waits, retrievals and tool calls, with compute-bound work such as inference and parsing keeps the agent productive during waits. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Most of an agent request's total latency time is spent waiting, on model inference, retrieval, tool invocations, and memory lookups, rather than on CPU work inside the agent process. The structure of how those waits are composed dominates total latency more than the speed of any single downstream dependency. Four structural decisions typically affect latency: 

1.  Running independent operations concurrently rather than sequentially 

1.  Reusing warm connections and runtimes across invocations 

1.  Removing cold starts from the critical path 

1.  Deduplicating repeated lookups within a single request. 

 Each decision is independent of model and prompt choices, so the gains compound with the reasoning-loop and model-selection optimizations addressed elsewhere in this pillar. 

 Concurrency is the largest impact when the agent fans out across independent data sources or tool calls. Dependency analysis identifies operations that share no data dependency (for example, a personalization lookup and a knowledge-base query issued from the same reasoning step, and executes them in parallel so the step's latency equals the slowest operation rather than the sum). 

 Agent frameworks expose this directly. Strands Agents executes independent tool calls emitted in a single reasoning step concurrently, and graph-based orchestrators such as LangGraph fan out across independent edges. The constraint is downstream capacity, where concurrent model calls and tool invocations must respect [Amazon Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) (requests-per-minute and tokens-per-minute) and tool-API rate limits, or parallelism converts into throttling and retry storms that undo the latency win. 

 Connection reuse and cold-start removal address the per-invocation setup costs that compound with concurrency. HTTP connections to model endpoints and tool APIs should persist across invocations through the SDK or HTTP-client connection pool rather than be opened and torn down per request. Each fresh connection pays TLS-handshake and connection-setup overhead on the critical path that a pooled connection avoids entirely, and that overhead accumulates across fan-out and across invocations. 

 Database connections follow the same principle. [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) pools connections to Aurora and RDS so serverless agents don't exhaust database connection limits or pay connection-setup latency per invocation. At runtime, [Amazon Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated microVM across invocations that share a session identifier, which removes cold starts while a session is active and preserves in-memory state across reasoning steps. 

 For agents hosted on AWS Lambda, [Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution environments and [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on supported runtimes, reducing first-invocation latency to sub-second at the cost of continuous capacity or per-restoration charges. 

 Request-scoped caching addresses redundant work that happens inside a single invocation rather than across invocations. A reasoning loop that calls the same tool twice, retrieves the same passage across successive steps, or refetches the same user profile in the planner and the executor wastes latency budget on repeated I/O. A cache keyed by the request or session identifier deduplicates these lookups for the remainder of the request without the consistency complexity of a cross-request cache. 

 The scope is deliberately narrow, persistent and cross-request caches such as Amazon Bedrock prompt caching and semantic caches are higher-level optimizations addressed in context- and memory-focused best practices. However, request-scoped deduplication is frequently the lowest-risk caching optimization available, because the cache is discarded at the end of the invocation and can't serve stale data to a subsequent request. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Profile the critical path to identify parallelizable operations:** Trace a representative sample of production requests with the performance telemetry already in place to decompose each invocation into per-operation durations and dependencies. Identify operations that share no data dependency, separate tool calls, independent retrievals, personalization lookups alongside knowledge queries, and flag the sequential segments where concurrency would collapse wall-clock latency onto the slowest operation. Revisit the inventory as prompts and tools change, because dependency graphs shift with them. 

1.  **Execute independent operations concurrently within downstream capacity limits:** Configure the agent framework to fan out independent tool calls and retrievals in the same reasoning step, Strands Agents, LangGraph, and similar frameworks expose this as a native primitive. Bound concurrency to the downstream service's capacity, [Amazon Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html), tool-API rate limits, and database connection ceilings, so a step that fans out to 10 concurrent calls doesn't trigger throttling that costs more latency than it saves. 

1.  **Reuse connections to model endpoints and external APIs across invocations:** Configure the HTTP client's connection pool so TLS sessions to Amazon Bedrock and tool APIs persist across invocations rather than being reestablished per request. On runtimes that preserve memory across invocations, [AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html), container-based services, and long-running services, initialize the client once per execution environment rather than per invocation so its connection pool survives across calls. A warm invocation should pay zero connection-setup latency on downstream calls. 

1.  **Pool database connections through a managed connection pool:** For agents that read from or write to relational data, front Aurora and RDS databases with [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) so serverless invocations share a bounded pool of database connections rather than opening a new connection each time. Without a pooler, concurrent agent invocations exhaust the database's connection ceiling and pay per-invocation setup latency on the critical path, both failure modes worsen as parallelism increases. 

1.  **Remove cold starts from the agent execution runtime:** Select a runtime that keeps the agent's execution environment warm on the critical path. [Amazon Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated microVM across invocations that share a session identifier, preserving in-memory state and avoiding per-invocation cold starts while the session is active. For Lambda-hosted agents, [Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution environments and [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on supported runtimes. Always-on container services such as Amazon ECS or Amazon EKS avoid cold starts entirely at the cost of continuous capacity. Choose based on traffic shape rather than runtime preference. 

1.  **Deduplicate repeated lookups within a single request using a request-scoped cache:** Add an in-memory cache scoped to the lifetime of the request or session that memoizes idempotent lookups, tool responses, retrieved passages, user-profile reads, keyed by input. A reasoning loop that calls the same tool twice or retrieves the same passage across successive steps resolves the second call from the cache, recovering that latency without the consistency complexity of a cross-invocation cache. The cache is discarded at the end of the request, so it can't serve stale data to a subsequent invocation. 

1.  **Re-measure the critical path after each structural change and as traffic grows:** After applying concurrency, pooling, cold-start, or caching changes, re-profile the critical path under representative production load to confirm the optimization held and did not introduce new failure modes such as throttling or connection-pool saturation. Repeat the measurement as traffic grows, because parallelism bounded correctly at launch frequently exceeds quotas at higher scale and the latency profile silently regresses before an SLO is exceeded. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets](agentperf01-bp03.html) 
+  [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html) 
+  [AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions](agentperf02-bp04.html) 
+  [AGENTPERF03-BP04 Establish efficient agent caching and data access patterns](agentperf03-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) 
+  [Amazon Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) 
+  [Amazon Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) 
+  [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) 
+  [AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) 
+  [AWS Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) 
+  [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) 
+  [Building serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) 
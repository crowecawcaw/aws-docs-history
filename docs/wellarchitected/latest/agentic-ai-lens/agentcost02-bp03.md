

# AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations
<a name="agentcost02-bp03"></a>

 Agents repeat work constantly: identical prompts, semantically equivalent requests, the same planning steps across similar tasks. Caching at the prompt, semantic, and plan-template layers changes repetition from a recurring expense into a one-time cost paid on the first invocation. 

 **Desired outcome:** 
+  You have prompt caching enabled for stable system prompts so the cacheable prefix is reused across invocations at reduced rates. 
+  You have a semantic cache that serves responses for functionally equivalent requests above a configurable similarity threshold. 
+  You have plan templates cached and instantiated for recurring task patterns rather than regenerated each time. 
+  You track cache hit rates and cost savings per caching layer. 

 **Common anti-patterns:** 
+  Transmitting identical system prompts and tool descriptions on every invocation at full input token cost rather than cached prefix rates. 
+  Using exact-match lookups when functionally equivalent requests use different wording, causing cache misses on semantically identical tasks. 
+  Applying one cache TTL across all task types without distinguishing static reference data from time-sensitive information, returning stale responses that degrade quality. 
+  Deploying customized models without monitoring cache-assisted performance, missing opportunities to validate that expected cost reductions actually materialize. 

 **Benefits of establishing this best practice:** 
+  Prompt caching reduces input token costs by reusing cached system instructions across invocations at reduced rates. 
+  Semantic caching helps prevent redundant reasoning by serving cached responses for functionally equivalent tasks. 
+  Plan template reuse reduces model invocations for the planning phase of recurring task patterns. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Caching for agents works at three distinct layers, and each layer has a different failure mode. 

 [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) is the highest-impact layer for agents with large stable system prompts. Amazon Bedrock stores the key-value state of the cached prefix and reuses it at reduced rates. Design so that the cacheable prefix (system prompt, tool descriptions) is stable across invocations, because any dynamic content mixed in invalidates the cache. Refactor to move user-specific or session-specific content out of the cacheable prefix. 

 Semantic caching addresses the idea that two requests that mean the same thing are rarely identical in wording. Generate an embedding of each incoming request with a lightweight model and query [Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) for similar prior requests above a configurable threshold such as cosine similarity greater than 0.95. The threshold helps you tune, as higher values reduce false positives but lower hit rates, and the right value depends on how much response variance your agent tolerates. Store cache entries with TTLs calibrated to each task type's freshness requirements, so reference data cached for hours doesn't pollute tasks that need up-to-date market or inventory information. 

 Don't overlook plan template caching. Agent planning outputs are highly repeatable for recurring task patterns, like an onboarding checklist, a support triage decomposition, or a reporting workflow plan. Store these plans keyed by task type and input parameter signature, and instantiate cached templates with current parameters rather than regenerating new plans each time. [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state by extracting and persisting key information, reducing input token costs from repeated history transmission. 

 Cache correctness depends on invalidation. Event-driven invalidation purges stale entries the moment source data changes, which is what makes aggressive caching safe for moderately volatile data. Measure impact with AWS Cost Explorer and Amazon CloudWatch integrated with [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and alarm when hit rates fall below targets. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable prompt caching for stable prefixes:** Turn on [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for agents with system prompts larger than 1,000 tokens, and refactor the prompt to move dynamic content out of the cacheable prefix. 

1.  **Deploy a semantic cache layer:** Stand up an OpenSearch Serverless index with embedding-based similarity, configure similarity thresholds per task type, and set per-task TTLs. Accept quantization only when accuracy loss remains below two percent on task success rate. 

1.  **Cache plan templates:** Key plan templates by task type and input parameter signature, and perform a pre-invocation lookup before generating a new plan. 

1.  **Use managed memory for session state:** Configure [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) session identifiers so multi-turn conversation state is maintained without manual history concatenation. 

1.  **Design event-driven invalidation and monitor hit rates:** Wire event-driven cache invalidation to source data changes, and create CloudWatch dashboards that display hit rates across prompt, semantic, and plan-template caches with alarms when hit rates fall below target. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html) 
+  [AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering](agentcost02-bp02.html) 
+  [AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory](agentcost03-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock Prompt Caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) 
+  [Effectively use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/) 
+  [Optimize LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/) 
+  [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) 
+  [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) 
+  [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Balance cost, performance & reliability for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
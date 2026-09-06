

# AGENTSUS01-BP04 Scale cognitive processing pathways appropriately
<a name="agentsus01-bp04"></a>

 Foundation model inference is the single most energy-intensive operation in an agent workflow, and it runs hundreds or thousands of times a day. Matching model size, retrieval depth, and memory scope to actual task complexity keeps cognitive resource consumption proportional to the value delivered, rather than defaulting every call to the largest available model. 

 **Desired outcome:** 
+  You have tiered model routing in place, so each task goes to the smallest model that meets its quality bar. 
+  Retrieval depth and context window size are scoped to task complexity, so routine tasks don't carry the retrieval overhead of complex reasoning. 
+  Multimodal extraction uses purpose-built services where applicable, not raw vision models for every document. 
+  Agents operate within token budgets and rate limits enforced at the runtime layer for each agent. 

 **Common anti-patterns:** 
+  Routing every request to the largest foundation model without checking whether a smaller model or cached response would meet the quality bar, which is the largest single opportunity for energy reduction. 
+  Allowing agents to call models without token budgets or concurrency limits, enabling single agents to consume disproportionate resources under load. 
+  Configuring retrieval-augmented generation to return the same context depth for every task regardless of complexity, producing oversized context windows and redundant vector queries. 
+  Sending raw document images to large vision models when a purpose-built extraction service would return the same structured data at a fraction of the compute cost. 

 **Benefits of establishing this best practice:** 
+  Cognitive resource consumption scales with task demand rather than agent count, so the energy cost of scaling up agent fleets stays proportional to the work they do. 
+  Token budgets for each agent help prevent one agent from starving the rest of the fleet under load. 
+  Right-sizing across hundreds of daily model calls compounds into substantial energy savings that are not visible on a single-call basis. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The Performance Efficiency pillar covers tiered model selection in [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html). The Cost Optimization pillar covers model cascading in [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html). The sustainability view adds one thing. The objective isn't latency or cost alone, but total energy and compute footprint per unit of business value delivered. A task taxonomy that ranks requests by reasoning complexity, then routes them to appropriately sized [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) models, makes the routing data-driven rather than default-to-biggest. 

 Tracking successful task completions divided by total compute consumed gives a better signal than either metric alone. A workflow that gets the right answer on the first try with a small model is more sustainable than one that uses the largest model and still retries. Tag invocations so this ratio can be calculated per task category, and use it to shift routing thresholds over time. With [Amazon Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html), you can distribute non-urgent requests to Regions with favorable energy profiles when latency constraints permit. 

 Retrieval depth in [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) should be a parameter of the task, not a constant. A routine question with a bounded answer doesn't need the same retrieval fanout as a complex reasoning task. Oversized retrieval wastes vector queries and bloats context windows. For document-heavy workloads, [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) extracts structured data from documents at a fraction of the compute cost of routing raw images through a vision model. The cheaper path is often the better one. 

 Configure AgentCore Memory with tiered TTLs and automated pruning so working memory doesn't grow unboundedly, and add semantic caching so similar queries serve cached responses instead of repeated invocations. Enforce token budgets and concurrency limits for each agent through AgentCore Runtime execution constraints. Measure actual consumption through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so thresholds stay tied to observed reality. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement tiered model routing:** Follow the patterns in [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html) and [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html) to direct tasks to appropriately sized [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) models based on a complexity taxonomy. 

1.  **Scope retrieval depth to task complexity:** Parameterize [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) retrieval so vector queries and context tokens scale with the work. Use tighter limits for routine tasks and broader retrieval only for complex reasoning. 

1.  **Route document extraction to purpose-built services:** For multimodal tasks, use [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) instead of sending raw images through large vision models. 

1.  **Apply memory lifecycle policies:** Configure AgentCore Memory with tiered TTLs and automated pruning so working memory stays bounded and stale entries are removed automatically. 

1.  **Enforce budgets and track efficiency:** Set token budgets and rate limits for each agent through AgentCore Runtime execution constraints, and track successful completions per unit of compute consumed through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to adjust routing thresholds from data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html) 
+  [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](agentcost02-bp01.html) 
+  [AGENTSUS01-BP01 Design specialized agents with explicit resource boundaries](agentsus01-bp01.html) 
+  [SUS02-BP02 Align SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html) 

 **Related documents:** 
+  [Amazon Bedrock model support](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) 
+  [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 
+  [Effective cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/) 
+  [Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Agentic AI patterns and workflows on AWS - Routing dynamic dispatch patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/routing.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Evaluations tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
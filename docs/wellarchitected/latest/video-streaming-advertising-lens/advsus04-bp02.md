

# ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use

 The most capable foundation models consume the most resources per inference, and many advertising agents do not need that capability. Match model capability to task complexity to reduce energy consumption without sacrificing output quality. 

 **Desired outcome:** 
+  Each advertising agent runs on the least resource-intensive foundation model that still meets its quality threshold, and those assignments are evidence-based and periodically revisited. 
+  Each advertising agent is matched to the smallest model that satisfies its quality bar for its specific task. 
+  Model assignments are grounded in quality benchmarks and resource proxies such as model size and token usage, rather than a blanket default to the most capable model. 
+  Model selections are reviewed on a regular cadence so newer, more efficient models are adopted as they become available. 

 **Common anti-patterns:** 
+  Defaulting every agent to a single high-capability model regardless of whether its task is basic classification or complex multi-channel generation. 
+  Choosing models on perceived quality alone, without measuring quality against resource proxies such as model size or token consumption per task. 
+  Treating model selection as a one-time decision and never re-evaluating it as more efficient models are released. 

 **Benefits of establishing this best practice:** 
+  Lower energy consumption and carbon footprint across the agent fleet by matching model capability to actual task demand. 
+  Reduced inference cost as a direct consequence of right-sizing model capability. 
+  Maintained output quality, because models are selected against explicit quality thresholds rather than downsized blindly. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Agentic advertising workflows span tasks of widely varying cognitive demand, from deterministic brand-safety classification to open-ended multi-channel media planning. The foundation models that serve these tasks consume very different resources per inference. A frontier model applies far more parameters and compute to every token than a compact model does. Serving a basic label with a large model spends resources the task never required. In video-streaming advertising this waste compounds quickly. Ad decisioning, creative generation, and audience work run at large volumes across a fleet of agents. An excess per inference that looks negligible in one call is multiplied by billions. 

 For each task, candidate models trade output quality against resource intensity. Right-sizing assigns each agent the smallest model that meets its quality threshold. The result is a heterogeneous fleet. You can right-size by fixing a model per agent, by routing individual requests to smaller or larger models based on difficulty, or by distilling a large model into a compact one for narrow high-volume tasks. 

 Aim for the smallest model that meets each agent's quality bar. Dropping below that bar can waste the impression through an irrelevant creative, a brand-safety miss, or additional regeneration and human review. A heterogeneous fleet also adds operational overhead, because more distinct models mean more assignments to justify, monitor, and keep current. New foundation models are released frequently, so an assignment that was efficient at design time can become wasteful if it is never reviewed. 

 Match inference capacity to each agent's invocation pattern in the same way. For advertising agents, where invocation volume swings with campaign cycles, the gap between allocated and used capacity accounts for most avoidable energy and carbon. Categorize each agent as bursty (campaign planning, which spikes during planning cycles), steady-state (brand-safety monitoring, with consistent around-the-clock volume), or scheduled (nightly reporting, with predictable batch windows). The mechanics of provisioned, on-demand, and batch inference, prompt caching, and knowledge base retrieval tuning are not specific to advertising and are covered by the Sustainability pillar of the Generative AI Lens and by the agentic AI cost practices in ADVCOST05. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Catalog and classify each agent's task complexity:** Inventory every advertising agent and classify its task complexity. A brand safety monitoring agent performing classification tasks is low complexity. A media planning agent generating multi-channel strategies is high complexity. 

1.  **Benchmark candidate models on quality and resource proxies:** Use Amazon Bedrock Model Evaluation to benchmark output quality across at least three candidate models for each agent. Record quality scores alongside resource proxies such as model size and token usage per task. 

1.  **Assign the most energy-efficient qualifying model:** Assign the most energy-efficient model that meets your quality threshold to each agent. For example, assign a lightweight model (such as Amazon Nova Lite or Claude Haiku) to the brand safety classifier, and a more capable model (such as Claude Sonnet or Amazon Nova Pro) to the media planning agent. 

1.  **Automate routing within a model family:** Use Amazon Bedrock Intelligent Prompt Routing to automatically direct simpler advertising queries to smaller, more efficient models and complex queries to more capable models within the same model family, optimizing resource consumption without manual intervention. 

1.  **Distill models for high-volume repetitive tasks:** For high-volume, repetitive agent tasks such as ad format classification or audience segment matching, use Amazon Bedrock Model Distillation to create smaller, faster, and more energy-efficient models that retain the accuracy of larger models. 

1.  **Re-validate assignments when the workload changes:** Treat each assignment as valid only for the task shape it was measured against. Re-run the benchmark for an agent whose prompt structure, output format, or quality bar changes, since a model that was sufficient for the previous task may not clear the new one. Ongoing re-evaluation as new models and features are released is a separate discipline, covered by ADVSUS04-BP01. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS04-BP01 Continually measure resource consumption of agentic AI advertising workloads, and adjust model and agent allocation accordingly](advsus04-bp01.md) 
+  [ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption](advcost05-bp03.md) 
+  [ADVCOST05-BP06 Use provisioned throughput for steady-state agents and on-demand pricing for variable workloads](advcost05-bp06.md) 
+  [GENSUS01-BP01 Implement auto scaling and serverless architectures to optimize resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus01-bp01.html) 
+  [GENSUS03-BP01 Leverage smaller models and optimized inference techniques to reduce carbon footprint](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus03-bp01.html) 

 **Related documents:** 
+  [Guidance for Advertising Agents on AWS](https://docs.aws.amazon.com/solutions/advertising-agents-on-aws/) 
+  [Amazon Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) 
+  [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) 
+  [Reduce costs and latency with Amazon Bedrock Intelligent Prompt Routing and prompt caching](https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) (Model Inference, Model Evaluation, Model Distillation, Intelligent Prompt Routing) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 


# AGENTPERF02-BP02 Implement task-appropriate model selection strategies
<a name="agentperf02-bp02"></a>

 Agent tasks vary widely in the reasoning they require, but default routing often sends every task to the same large model, paying the latency cost of a heavyweight model even for work a smaller one resolves as well. Matching model capability to task demand is one of the highest-use performance decisions in an agent system, because inference latency and throughput scale directly with model size. Done systematically, model selection reduces per-task latency without sacrificing quality on complex reasoning. 

 **Desired outcome:** 
+  You have agent tasks classified by reasoning complexity, with each class mapped to the smallest model that meets its quality bar. 
+  You have routing logic that directs each request to its assigned model at runtime, with a cascading fallback to a more capable model when the assigned model produces low-confidence or failed outputs. 
+  You have model assignments validated against benchmarked quality and latency on the workload's own task distribution rather than on generic leaderboard rankings. 
+  You have model selection treated as a runtime-configurable parameter so new model releases can be evaluated and rolled out without redeploying the agent. 
+  You have inference latency and task quality tracked per task class, so routing decisions are continually validated against both. 

 **Common anti-patterns:** 
+  Using a single large model for every agent task regardless of complexity, paying the latency and cost premium of a heavyweight model on work a smaller one resolves as well. 
+  Using a small or general-purpose model for tasks that require deeper reasoning, producing low-quality outputs that trigger retries, extra reasoning iterations, or manual escalation and eroding the latency savings the small model was meant to provide. 
+  Selecting models from general benchmark rankings rather than from benchmarks run on the workload's own task distribution, producing choices that are optimal for the leaderboard but suboptimal for actual traffic. 
+  Treating model choice as a one-time architectural decision baked into application code, so evaluating or rolling out a newly released model requires a code change and redeploy rather than a configuration update. 
+  Operating without a fallback path when the assigned model returns low-confidence or failing outputs, forcing the pipeline to return a poor answer or fail entirely rather than escalating that request to a more capable model. 

 **Benefits of establishing this best practice:** 
+  Routing lightweight work to smaller, faster models avoids paying the inference time of a large model for tasks that don't require it. 
+  Explicit routing to capable models and cascading fallback when a smaller model underperforms protect user-facing accuracy on complex tasks. 
+  Benchmarks against the workload's actual task distribution continually improve assignments as new evaluation data accumulates. 
+  Runtime-configurable selection lets capability and latency improvements from new models reach production without redeploy cycles. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The reasoning pipeline's dominant cost component is the inference call, and inference latency and throughput scale directly with model size. Typical agent workloads have heterogeneous task mixes and simple classification alongside multi-step reasoning, so applying the largest model uniformly forces the blended latency and cost to track the most capable option even though most requests don't need it. Systematic model selection shifts this by assigning each task to the smallest model that still meets its quality bar. 

 Two approaches fit together: 

1.  Explicit task classification, where the agent assigns each task to a class and each class to a model or model tier, gives fine-grained control and works across providers and model families. 

1.  Managed routing such as [Amazon Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) predicts response quality per request within a model family and routes to the smallest model predicted to meet the quality bar, which hands off the per-request pick when the decision is purely capability-compared to-cost inside one family. 

 Many workloads combine both. The agent picks the tier by task type while the router selects the specific model within that tier. Purpose-built services such as [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for intelligent document processing are also worth considering as a model for document-heavy tasks, where a dedicated pipeline is typically faster and more accurate than routing documents through a general-purpose vision model. 

 Routing decisions are only as good as the benchmarks behind them. Public leaderboards rank models on averages across heterogeneous benchmarks whose task distributions can bear little resemblance to a specific workload, so a model that leads a general benchmark can underperform on the traffic a particular agent actually serves. 

 [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) provides built-in evaluators, LLM-as-a-Judge, ground-truth correctness, and trajectory matching that make it practical to benchmark candidate models against an evaluation set representative of actual traffic. Without workload-specific evaluation, routing choices are effectively guesses. 

 Selection is the starting point of a request, not the end of the decision. Cascading fallback preserves quality without forcing the whole task class to the larger model. Fallback differs from retry: retries repeat the same call hoping for a better draw, while fallback changes a variable by switching models. To promote new models through progressive rollouts with automated rollback, hold model identifiers, tier mappings, and fallback rules as runtime configuration in [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or a comparable config service), combined with [deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) gated by CloudWatch alarms on latency and quality. 

 Per-class latency, token consumption, quality scores, and fallback-escalation rate belong on the same performance dashboards as total latency and reasoning iteration counts. A rising fallback rate on a class is an early indicator that the primary model no longer fits, either because traffic has shifted or because a newly available model would serve the class better. This typically shows up before the user-facing regression is large enough to alarm. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify agent tasks by reasoning complexity:** Group the workload's tasks into classes based on the reasoning they require, for example, single-step extraction or classification, structured multi-step reasoning over known steps, and open-ended investigation. Document representative examples per class so routing decisions are auditable and can be revisited as task distributions shift. Use the classification as the input to model assignment rather than letting each caller pick a model case by case. 

1.  **Benchmark candidate models on the workload's own task distribution:** Build an evaluation set representative of production traffic and score candidate models against it using [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) or an equivalent evaluation harness. Capture quality signals (correctness, goal success rate, tool-trajectory match) alongside latency and tokens so you can identify the smallest model meeting the quality bar for each class. Treat leaderboard rankings as a starting shortlist, not as the decision. 

1.  **Map each task class to a model or model tier:** Define a small set of tiers, for example, fast, standard, and advanced, and assign each class to the tier that benchmarks demonstrate is sufficient. For each tier, select a specific model or Amazon Bedrock inference profile. Where routing within a family is the goal, [Amazon Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) can make the per-request pick automatically. For document-heavy tasks, consider [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) as the right example rather than a general-purpose vision LLM. 

1.  **Implement routing logic that dispatches requests to the assigned model at runtime:** Resolve the task-class-to-model mapping at the start of each request and issue the inference call against the chosen model. When crossing providers or model families, a framework abstraction such as [Strands Agents model providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/) keeps the routing code stable as providers change underneath it. 

1.  **Configure a cascading fallback to a more capable model for low-confidence or failing outputs:** Define structured signals, confidence score below a threshold, schema validation failure, parse error, or an explicit incomplete response, that escalate the specific request to a more capable model. Limit the escalation to a single step so tail latency stays predictable, and log both the primary and fallback decision for each request that escalates. 

1.  **Externalize model assignments and routing rules as runtime configuration:** Hold model identifiers, task-class-to-tier mappings, and fallback rules in [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or an equivalent config service) and read them at request time. Decoupling selection from deployment lets new models be evaluated, promoted, or rolled back without redeploying the agent. 

1.  **Roll out model changes progressively with automated rollback:** Use [AWS AppConfig deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) to shift traffic to a new model in steps with bake-time validation, and attach CloudWatch alarms on latency and quality so the change rolls back automatically when the alarm fires. Treating a model swap as a monitored deployment makes frequent model updates safe. 

1.  **Emit per-task-class telemetry for latency, tokens, quality, and fallback rate:** Publish per-class metrics so the effect of each routing decision is visible on dashboards and can be alarmed. Use [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) together with [AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) to attribute latency, tokens, and evaluation scores to the class and model that served each request. 

1.  **Review routing decisions against production telemetry on a defined cadence:** Schedule periodic reviews of per-class latency distributions, fallback-escalation rates, and quality scores, and re-run AgentCore Evaluations against newly released models using the same task-distribution benchmark. Promote, demote, or re-tier models based on observed data rather than provider release cadence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets](agentperf01-bp03.html) 
+  [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 
+  [AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions](agentperf02-bp04.html) 

 **Related documents:** 
+  [Understanding intelligent prompt routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) 
+  [Evaluate agent performance with Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 
+  [What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) 
+  [Create a deployment strategy (AWS AppConfig)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) 
+  [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) 
+  [Foundations of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html) 
+  [Economics for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/introduction.html) 
+  [Blog: Build reliable AI agents with Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/) 
+  [Strands Agents Model Providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Mastering model choice: The 3-step Amazon Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock AgentCore samples, Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations) 

 **Related workshops:** 
+  [Diving Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 


# AGENTPERF02-BP01 Design efficient reasoning pipelines
<a name="agentperf02-bp01"></a>

 Each iteration of the perceive-reason-act loop typically involves an LLM inference call, so the number of iterations an agent takes multiplies both latency and cost. An efficient pipeline reaches accurate decisions in the fewest iterations the task requires, uses bounded iteration limits and confidence-based early termination to help prevent runaway loops, and handles retries within explicit performance budgets rather than silently eroding them. 

 **Desired outcome:** 
+  You have per-task iteration limits and confidence-based early termination configured, so reasoning loops can't run without bounds. 
+  You have pipeline shapes that scale reasoning depth to task complexity, with simple tasks resolving in one or two iterations and complex tasks receiving the iterations they need. 
+  You have retry strategies bounded by explicit latency budgets, with semantic re-prompting or graceful degradation engaged before the end-to-end SLO is exceeded. 
+  You have average reasoning iterations per task tracked as a first-class KPI, visible alongside latency and token metrics. 

 **Common anti-patterns:** 
+  Allowing agents to reason indefinitely without iteration limits or early termination conditions, producing runaway loops that consume tokens and time without improving output quality. 
+  Designing reasoning pipelines that always execute the same sequence of steps regardless of task complexity, applying heavyweight reasoning to simple tasks that could be resolved with a single inference call. 
+  Designing retry strategies without performance budgets, so exponential backoff retries accumulate latency that exceeds the end-to-end SLO when semantic re-prompting or graceful degradation would preserve performance targets. 
+  Retrying a failed LLM call with the identical prompt and model, rather than re-prompting semantically, rephrasing the instruction, simplifying the task, or falling back to a more capable model, to increase the chance that the retry succeeds inside the remaining latency budget. 

 **Benefits of establishing this best practice:** 
+  Efficient pipeline design reduces the number of LLM inference calls per task, which is one of the highest-impact optimizations for agent latency and cost. 
+  Adaptive pipeline shape makes simple tasks resolve quickly while complex tasks receive the iterations they need. 
+  Explicit retry budgets and semantic re-prompting keep tail latency within SLO even when a tool or model call fails on the first attempt. 
+  Iteration caps produce tighter latency distributions that simplify capacity planning, auto scaling thresholds, and cost forecasting. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Total latency and token spend scale with the number of iterations the pipeline takes to reach an accepted output, so pipeline design, how the loop is structured, when it terminates, and how failures are handled has a multiplicative effect on both latency and cost. A well-designed pipeline reaches an accepted output in the fewest iterations the task actually requires. 

 The right pipeline shape depends on task complexity and predictability. [Basic reasoning agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) handle single-turn classification, extraction, or summarization in one inference call and should not be wrapped in iterative reasoning loops. [ReAct-style loops](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html), in which the agent interleaves reasoning, tool calls, and observation, fit open-ended tasks where the next step can't be predicted at design time. 

 Plan-then-execute shapes such as ReWOO and plan-and-solve hybrids separate planning from execution and bound iteration by plan length rather than by the model's willingness to keep looping, and reflect-and-revise shapes such as Reflexion introduce explicit critique cycles with hard caps on revision passes. Both patterns are described in [Customize agent workflows with advanced orchestration techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/). 

 Iteration caps and early termination are the two controls that keep a loop from consuming resources without producing value, and they serve complementary roles. A per-task iteration cap is an upper bound that helps prevent pathological runaway (a model that keeps calling tools without converging), and it must be set per task class because a ceiling appropriate for multi-step research is wasteful for a simple lookup. 

 Early termination ends the loop before the cap when additional iterations would not improve the output. For example, when a critique step returns a structured "no further revision needed" signal, when the agent's own confidence assessment exceeds a threshold, or when a deterministic validator (schema check, grounding check, policy check) confirms the output is acceptable. 

 Together, caps help prevent the worst case while termination removes the common case of paying for unnecessary iterations. 

 Failure recovery is part of the latency budget, not an exception to it. When a tool call or model inference fails, naive exponential backoff can consume more time than the end-to-end target allows. Every retry strategy should be bounded by an explicit performance budget that specifies how much latency and how many tokens retries can consume before the pipeline falls back to a degraded response. 

 Identical retries against the same prompt and model frequently fail for the same reasons: 
+  Semantic re-prompting (rephrasing the instruction, simplifying the task, or tightening the output contract) 
+  Model escalation (routing the retry to a more capable model) 
+  Tool substitution (using an alternative data source) 

 Each of these failures change a variable in the failure mode and increase the chance that the retry succeeds within the remaining budget. To preserve user trust, implement strategies like graceful degradation, returning a partial answer with marked gaps, a lower-confidence answer with explicit uncertainty, or a clear "can't complete" response before the latency target is exceeded. 

 Average reasoning iterations per task belongs alongside latency, tokens, and cost as a first-class performance KPI. It is the earliest signal that pipeline shape, prompt quality, or upstream tool reliability has drifted, because a rising iteration count typically precedes a latency or cost regression. Each extra iteration compounds with the others downstream before the user-facing metric shifts enough to trigger an alarm. 

 Tracked by task class and by pipeline shape, iteration count also reveals misrouted tasks like simple requests running through heavyweight loops or complex tasks capped before they converge. Both of these patterns are invisible to metrics that only measure the end result. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify each agent task by reasoning complexity:** Group tasks by the reasoning depth they require, single-step extraction or classification, multi-step reasoning over known steps, and open-ended investigation where the path isn't knowable in advance. Use this classification as the input to pipeline-shape selection and iteration budgets, because applying the same shape and budget to every class either wastes iterations on simple work or under-reasons on complex work. Document the classification alongside the workload's success criteria so routing decisions can be audited and revisited as task distributions change. 

1.  **Select a pipeline shape that matches each task class:** Map each class to a reasoning pattern documented in [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html), a [basic reasoning pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) for single-step tasks, a [ReAct loop](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) for open-ended reasoning where tool use drives the next step, and a plan-then-execute or reflect-and-revise shape for tasks that benefit from an explicit planner or critique stage as described in [Customize agent workflows with advanced orchestration techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/). Avoid wrapping single-step tasks in iterative loops, which inflates cost and latency with no accuracy gain. 

1.  **Set per-task iteration caps sized to the complexity class:** Configure a hard maximum on reasoning iterations for each task class using the iteration-control primitive exposed by the agent framework in use, and size the cap to a value the workload will hit only on pathological cases. Caps are a floor on the worst case, tasks that converge early still terminate early through the confidence signals configured next, so tune caps to the most complex variant of each class rather than to the typical case. 

1.  **Define early-termination conditions so loops stop when iterations stop adding value:** Specify structured signals that end the loop before the cap, a critique step returning a boolean "revision needed" flag, a confidence score exceeding a defined threshold, or a deterministic validator (schema, grounding, or policy check) confirming the output is acceptable. Treat these signals as data the pipeline produces and logs, not as implicit model behavior, so termination decisions are observable and auditable rather than hidden inside a chain of thought. 

1.  **Establish a retry budget bounded by the end-to-end latency target:** Allocate an explicit portion of the end-to-end latency target to retry handling and enforce it at the pipeline level so accumulated retries can't silently exceed the target. Decompose the budget into latency and token components, because a retry that stays inside the latency budget but triples token consumption still degrades unit economics. Align the budget with the service level objective the workload is graded on so retry behavior is measured against the same target as everything else in the pipeline. 

1.  **Replace identical retries with semantic re-prompting, model escalation, or tool substitution:** When a call fails, retry with a rephrased instruction, a simpler task decomposition, a more capable model, or an alternative tool, each changes a variable in the failure mode instead of repeating the same failing call. Select the substitution based on the failure signal: a timeout suggests model escalation or tool substitution, a parsing failure suggests re-prompting with a stricter output contract, and a grounding failure suggests retrieval expansion. 

1.  **Configure graceful degradation paths that return before the target is exceeded:** Define the fallback response for each task class, a partial answer with marked gaps, a lower-confidence answer with explicit uncertainty, or a clear "unable to complete" response, and invoke the fallback when the retry budget is exhausted or the latency budget is within a configured safety margin of being exceeded. Predictable tail behavior and a clear failure response preserve user trust better than maximizing the chance of an eventual success on every request. 

1.  **Emit reasoning iterations, retries, and terminations as first-class telemetry:** Publish iteration count, termination cause (early termination, cap hit, retry-budget exhausted, graceful degradation), and retry count for every invocation as metrics that can be thresholded and alarmed alongside latency and token metrics using a capability such as [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) or an equivalent pipeline on the agent's runtime. Put average iterations per task on the same dashboards as latency percentiles and cost per completion, since it is the earliest indicator that pipeline shape, prompt quality, or tool reliability has drifted. 

1.  **Review pipeline shape, caps, and budgets against production telemetry on a defined cadence:** Schedule regular reviews of iteration distributions, early-termination rates, retry-budget consumption, and degradation frequency so pipeline parameters track actual behavior rather than launch-time assumption. Tighten caps that are consistently under-utilized, relax caps that are being hit on legitimate complex tasks, and re-classify tasks whose iteration distribution reveals they belong to a different complexity class than originally assigned. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 
+  [AGENTPERF03-BP02 Optimize context window utilization and prompt management](agentperf03-bp02.html) 

 **Related documents:** 
+  [Blog: Customize agent workflows with advanced orchestration techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/) 
+  [Foundations of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html) 
+  [Agentic AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html) 
+  [Agentic AI - Generative AI Lens (Well-Architected Framework)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) 
+  [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
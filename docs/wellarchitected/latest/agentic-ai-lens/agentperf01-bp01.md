

# AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads
<a name="agentperf01-bp01"></a>

 Agent workloads are harder to measure than traditional applications because a single user request fans out into multiple inference calls, tool invocations, and memory retrievals, each with its own latency, quality, and cost signature. Without explicit performance targets, teams optimize against a moving reference and can't tell when an agent is ready for production. 

 **Desired outcome:** 
+  You have documented performance success criteria for every agent workload, with specific, measurable targets that are reviewed as business requirements evolve. 
+  Your teams objectively assess whether an agent meets performance expectations before deployment and continually validate performance in production. 
+  You have performance criteria integrated into CI/CD pipelines as quality gates, helping prevent regressions from reaching production. 

 **Common anti-patterns:** 
+  Defining success criteria only around infrastructure metrics such as CPU utilization or memory consumption, without measuring agent-specific dimensions like reasoning latency, token efficiency, or task completion quality. 
+  Applying a single latency target across streaming and non-streaming agents, or across interactive and batch workloads, when time-to-first-token and end-to-end completion are primary KPIs for different agent classes. 
+  Establishing performance targets after deployment rather than during design, producing architectures that can't meet requirements without significant rework. 

 **Benefits of establishing this best practice:** 
+  Explicit success criteria establish concrete targets against which telemetry can be evaluated, making downstream performance work measurable rather than speculative. 
+  Performance-aligned criteria direct teams to optimize the reasoning pipeline for the metrics that matter, rather than pursuing generic optimizations that don't improve business outcomes. 
+  Quality gates tied to measurable targets convert success criteria into enforceable artifacts that block regressions from reaching production rather than detecting them after the fact. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Success criteria for an agent workload must be concrete enough to evaluate a build against and specific enough to drive architectural decisions. A performance-aligned criterion names the signal, the threshold, the percentile or attainment goal, the evaluation window, and the business outcome it helps protect. Without that specificity, teams can't decide whether to swap models, add caching, split a workflow, or reject a release, as there is no reference against which the change can be judged. 

 Agent workloads have a wider KPI surface than traditional applications because a single user request expands into multiple inference calls, retrieval queries, tool invocations, and, for multi-agent systems, inter-agent handoffs, each with its own latency, error mode, and cost. A complete set of success criteria spans four dimensions: 

1.  Latency (time-to-first-token for streaming agents, end-to-end completion time for task-oriented agents, and per-phase budgets across the reasoning pipeline) 

1.  Throughput (concurrent sessions, sustained requests per second, and queue depth under load) 

1.  Quality (task completion rate, tool selection and parameter accuracy, reasoning grounding, and response faithfulness) 

1.  Efficiency (tokens per task, cost per completion, and cache hit rate). 

 Layered [agent evaluation frameworks](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) decompose quality further into component-level signals that infrastructure-only monitoring can't see, like tool use, memory retrieval, multi-turn topic adherence, reasoning accuracy, responsibility, and safety. 

 The primary latency KPI differs by agent class. For streaming, conversational agents, users perceive responsiveness through time-to-first-token and inter-token latency, so those are the KPIs that gate releases. For task-oriented agents that return a single structured result, task completion time is primary and time-to-first-token is largely irrelevant. For batch or asynchronous workflows, throughput and cost-per-task dominate, and strict p99 latency matters less than predictable completion-within-SLA. A single latency target across these classes either over-provisions some agents or sets unachievable goals for others. [AWS Well-Architected Performance Efficiency guidance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html) reinforces that tail behavior matters more than the mean, p90 and p99 anchor latency targets because averages mask the slow responses that drive user-perceived poor experience. 

 A measurable target has more structure than a number. A service-level objective (SLO) combines a service-level indicator (the metric), a threshold, an attainment goal (the percentage of time or requests that must meet the threshold), an interval (calendar or rolling window), and an error budget (the allowable shortfall). 

 [Amazon CloudWatch Application Signals service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) formalize this structure and add burn-rate alarms that fire when the budget is being consumed faster than expected, which matters for agent workloads whose latency distribution shifts subtly as prompts, tools, or models drift. SLOs should be decomposed into per-phase latency budgets, inference, retrieval, tool calls, inter-agent coordination, so that when a budget is exceeded, attribution to the offending phase is already encoded in the criteria rather than investigated after the fact. 

 Success criteria are not static. Agent behavior is shaped by prompts, memory, tools, and the models behind them, all of which drift, so criteria that are correct at launch erode as the system evolves. Integrating targets into CI/CD as quality gates, latency budgets checked against load-test results, task-completion rate checked against a curated evaluation set, cost-per-task checked against a ceiling, converts them from documents into enforceable artifacts that block regressions at the boundary. 

 [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) frames this lifecycle discipline as mandatory rather than optional, because continuous measurement is the only mechanism that keeps criteria aligned with the business outcomes they were designed to protect. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Capture business outcomes and user expectations with stakeholders:** Work with product, business, and user-experience owners to document the outcomes the agent must produce, the scenarios in which it operates, and the user expectations for responsiveness, quality, and cost. Use this intake to frame every downstream target so latency, throughput, quality, and efficiency KPIs trace back to a stated business or user need. The [AWS Well-Architected Performance Efficiency process guidance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html) treats this stakeholder alignment as the first step in establishing credible KPIs. 

1.  **Classify each agent workload by interaction pattern:** Determine whether the agent is streaming or non-streaming, interactive or batch, synchronous or asynchronous, and single-agent or multi-agent. The classification dictates which latency KPI is primary, time-to-first-token for streaming conversational agents, end-to-end completion for task-oriented agents, throughput and cost-per-task for batch workflows, and whether multi-agent coordination metrics such as handoff latency and collaboration success belong in the criteria set. 

1.  **Define the KPI taxonomy spanning latency, throughput, quality, and efficiency:** For each workload, enumerate the specific signals to measure along the four dimensions, including agent-specific signals that infrastructure metrics can't cover. Structure quality signals in layers, final-response quality, task completion, tool use accuracy, memory and retrieval relevance, reasoning grounding, and responsibility and safety, following the [agent evaluation framework described by Amazon teams](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/). Include efficiency signals such as tokens per task, cost per completion, and cache hit rate to connect performance to unit economics. 

1.  **Set quantitative targets with thresholds, percentiles, and attainment goals:** Attach a numeric target to every KPI, specifying the percentile (p50, p90, p99) for latency and throughput signals and the attainment goal (for example, 99.5 percent of requests) for quality and availability signals. Anchor latency targets to p90 and p99 rather than averages, because tail behavior drives user-perceived performance, the [AWS Well-Architected Performance Efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) cautions that averages hide the slow responses that matter most. 

1.  **Allocate per-phase latency budgets within the end-to-end budget:** Decompose the end-to-end latency target into per-phase budgets, context retrieval, LLM inference, tool invocation, inter-agent coordination, output generation, so each phase has its own ceiling that sums to the overall target. Per-phase budgets make exceedances attributable at criteria-definition time and give engineering teams clear optimization targets when a phase drifts. Validate the decomposition against measured traces so the budgets reflect real behavior rather than assumption. 

1.  **Formalize targets as service level objectives with error budgets and burn-rate alerts:** For each customer-facing KPI, encode the target as an SLO with an SLI, threshold, attainment goal, interval, and period using [Amazon CloudWatch Application Signals service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html). Configure burn-rate alarms so the service signals when the error budget is being consumed faster than expected, giving operators time to respond before an SLO is exceeded. Group related SLIs into composite SLOs where a single user-facing outcome depends on multiple operations meeting their individual targets. 

1.  **Operationalize quality and cost KPIs through GenAI-aware monitoring:** Publish token consumption, per-invocation latency percentiles, cost attribution, and agent-level quality metrics through [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html), which surfaces these signals natively for Amazon Bedrock model invocations and accepts structured traces from agents running on any runtime through the [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction). Emit agent-specific quality signals, task completion rate, tool selection accuracy, reasoning grounding, as custom metrics so they can be thresholded, alarmed, and tied to SLOs the same way infrastructure signals are. 

1.  **Integrate targets as quality gates in the deployment pipeline:** Convert each success criterion into an automated check in CI/CD so releases that exceed a latency, quality, or cost target are blocked before they reach users. Run load tests against the latency and throughput targets and curated evaluation sets against the quality targets as part of the pipeline, following the lifecycle-management framing in [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html). Gates turn written criteria into enforceable artifacts that help prevent regressions rather than detecting them in production. 

1.  **Revisit targets on a defined cadence as the workload evolves:** Schedule regular reviews of each success criterion against production telemetry, changes in user expectations, and shifts in the underlying models, prompts, or tools. Tighten targets that are consistently exceeded, relax targets that are blocking legitimate improvements, and retire signals that no longer map to a business outcome, agent behavior drifts, and criteria that were correct at launch need to be revalidated against current reality. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF01-BP02 Implement comprehensive performance telemetry](agentperf01-bp02.html) 
+  [AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets](agentperf01-bp03.html) 
+  [AGENTOPS05-BP04 Define and track KPIs for agent workflows](agentops05-bp04.html) 
+  [AGENTOPS06-BP02 Evaluate and track ongoing agent performance](agentops06-bp02.html) 
+  [AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution](agentcost05-bp01.html) 

 **Related documents:** 
+  [AWS Well-Architected Framework: Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) 
+  [Amazon CloudWatch Application Signals: Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) 
+  [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Blog: Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Elevate application and generative AI observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-monitoring/) 
+  [AWS Distro for OpenTelemetry (ADOT)](https://aws.amazon.com/otel/) 
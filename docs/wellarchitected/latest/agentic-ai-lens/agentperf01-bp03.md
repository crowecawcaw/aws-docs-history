

# AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets
<a name="agentperf01-bp03"></a>

 The dominant contributor to agent latency varies by task type: a simple question-and-answer request can be inference-bound, a retrieval-heavy request can be retrieval-bound, and a multi-agent workflow can be coordination-bound. Without decomposing total latency into per-phase contributions, teams optimize assumed bottlenecks rather than measured ones, and engineering effort lands on work that doesn't move performance for users. 

 **Desired outcome:** 
+  You have a latency profile for every agent workload that decomposes latency into per-phase contributions, with the dominant phase identified and targeted for optimization. 
+  Your teams diagnose performance issues by examining the phase breakdown rather than guessing at which component is slow. 
+  You have per-phase regression alerts that fire on phase-level drift before the end-to-end service level objective is exceeded. 

 **Common anti-patterns:** 
+  Measuring only total latency without decomposing it into phases, making it impossible to tell whether slowness is caused by inference, retrieval, tool calls, or coordination overhead. 
+  Optimizing inference latency (model selection, prompt compression) when the actual bottleneck is retrieval or tool call latency, wasting engineering effort on a phase that contributes a small fraction of total time. 
+  Profiling under synthetic test conditions without validating against production traffic patterns, missing bottlenecks that only appear under concurrent load. 

 **Benefits of establishing this best practice:** 
+  Phase-level visibility directs engineering effort at the actual bottleneck rather than assumed bottlenecks. 
+  Per-phase trend monitoring pinpoints which phase degraded, making latency regressions faster to diagnose. 
+  Before-and-after phase profiles validate that an optimization actually shrank the targeted phase without regressing others. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Profiling an agent is the operation of aggregating span-based telemetry the reasoning pipeline already emits into contributions per phase, and then asking which phase dominates the budget. The decomposition is a grouping over existing trace data, provided every span maps cleanly to a phase in a shared taxonomy. When that mapping is ambiguous, a single span that covers both retrieval and output formatting, or a reasoning iteration that hides an inline tool call, the profile becomes untrustworthy and optimization decisions drift. The pre-work is in defining the phases once, aligning span types to them, and making the mapping visible to every team contributing to the agent. 

 The dominant phase varies by workload and shifts over time. For example: 
+  A conversational question-and-answer agent is usually inference-bound 
+  A retrieval-heavy agent that reads across several knowledge bases can be retrieval-bound 
+  A multi-agent workflow that serially hands off context between supervisor and workers is typically coordination-bound 
+  An agent that invokes external APIs can be tool-bound when a downstream service degrades 

 Optimizing the wrong phase produces no measurable user-facing improvement. For example, a 30 percent inference speedup is invisible when inference accounts for 10 percent of the budget and retrieval accounts for 60. Phase-level attribution helps prevent that mistargeting, and it remains necessary even after a workload has been tuned because the dominant phase at launch rarely stays dominant after prompts, tools, and models evolve. 

 Compute profiles at the distribution level, not the mean. Averages hide the tail, and tail latency is what users experience when an agent feels slow. Compute p50, p90, and p99 for each phase separately, and for total latency. The dominant phase at the median is often not the dominant phase at p99, because the slow tail typically concentrates in one or two phases, inference during model throttling, retrieval during index rebuilds or cold caches, tool calls during downstream-service incidents. A profile that reports means only by phase can point a team at the wrong target, because the phase that hurts users at the tail is usually smaller than the phase that dominates the average. 

 Run profiling against production traffic patterns for credible results. Synthetic load tests can exercise the request path, but they rarely reproduce the prompt distributions, tool-selection behaviors, and concurrency patterns real users generate. This means that bottlenecks that only appear under contention stay invisible, like thread-pool starvation during fan-out, cache-miss bursts after warmup expires, or queueing in shared inference endpoints. 

 With [Amazon CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) ingesting 100 percent of spans to the aws/spans log group, you can reconstruct a production profile from real traffic using [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries over span durations without standing up dedicated profiling infrastructure. Agents on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) produce compatible span data automatically when AgentCore Observability is enabled, and agents on Amazon ECS, Amazon EKS, AWS Lambda, or self-hosted infrastructure produce it through the [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction) collector, so both populations share a single surface. 

 Rank optimization targets by contribution multiplied by addressable variance, not by contribution alone. A phase that contributes 40 percent of the budget but is already near its theoretical floor offers less headroom than a phase that contributes 25 percent but has high variance driven by implementation choices, sequential retrieval that could be parallelized, or tool calls that could be cached. 

 Profiling also makes it possible to detect regression by phase. Once a baseline distribution exists for each phase, [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) alarms on a phase drifting outside its expected band before the change shows up in the SLO, so regressions are attributed to the offending phase at alert time rather than during an incident retrospective. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the phase taxonomy for the workload:** Enumerate the phases that make up end-to-end execution, input processing, context and memory retrieval, LLM inference, tool invocation, output generation or streaming, and inter-agent coordination, and map every span type emitted by the agent to exactly one phase, aligning span attributes with the [OpenTelemetry generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). Document the taxonomy so every team contributing spans groups them the same way, and add workload-specific phases such as guardrail evaluation or structured-output post-processing when they sit outside the common set. 

1.  **Aggregate spans into per-phase duration metrics:** Derive per-phase durations from the span log group using [CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) and [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries that sum span durations grouped by phase and trace, then emit the result as [CloudWatch custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) with a phase dimension. Publishing the profile as metrics, rather than only as ad-hoc log queries, lets the same signal flow into dashboards, alarms, and anomaly detection alongside native runtime metrics. 

1.  **Compute percentile-level profiles for every phase:** Calculate p50, p90, and p99 per phase and for end-to-end latency over a rolling window that matches the service level objective interval, and display the percentiles side by side. The dominant phase at the median is often not the dominant phase at p99, and profiling against only the mean hides the tail where user-perceived slowness concentrates. 

1.  **Visualize the contribution of each phase to end-to-end latency:** Build a stacked per-phase contribution view on a [customized CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) using the per-phase metrics emitted in the previous step, and use [dashboard variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html) to pivot the same view across the standard dimension set, agent ID, workflow, environment, task type, model ID, so dominant-phase analysis runs per slice rather than against a fleet average that can obscure tenant-specific or workflow-specific bottlenecks. Pair the custom view with the pre-built [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) views for session, trace, and span drill-down when a specific slow request needs investigation. 

1.  **Profile under production traffic rather than only synthetic tests:** Run the profile against real production trace data so concurrency effects, prompt-mix variance, and downstream contention appear in the distribution. Use synthetic load from tools such as the [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html) solution to stress-test specific hypotheses, for example, to confirm that a proposed parallel-retrieval change removes an observed p99 tail, and anchor the phase-contribution view itself to production traffic so decisions reflect how users actually exercise the agent. 

1.  **Rank optimization targets by contribution and addressable variance:** For each phase, estimate the contribution to the end-to-end budget and the fraction of that contribution that is addressable by engineering effort. Prioritize phases where both are high, a large contribution with room to shrink, over phases that are large but already near their theoretical floor, so engineering time moves user-visible latency rather than a metric that doesn't affect the tail. 

1.  **Set per-phase baselines and alarm on drift:** Establish a steady-state baseline distribution for each phase, then apply [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to the per-phase percentile metrics so deviations fire with the offending phase already attributed. Pair the phase-level alarms with the end-to-end service level objective so a phase drifting inside its per-phase budget triggers investigation before the end-to-end budget is exceeded. 

1.  **Measure before and after every optimization:** Capture the profile for each phase before an optimization is rolled out and compare it against the same profile under production traffic after the change lands. Validate that the targeted phase actually shrank, check that no other phase regressed to absorb the budget, and retain the comparison in the change record so future regressions can be diagnosed against a known-good profile. 

1.  **Revisit the profile as the workload evolves:** Agent behavior drifts as prompts, tools, memory, and models change, and the dominant phase at launch rarely stays dominant six months later. Refresh the phase-based profile after every significant prompt or model change and at least quarterly, then re-rank optimization targets against the current profile so engineering effort continues to land on the phase that actually limits user-visible performance. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads](agentperf01-bp01.html) 
+  [AGENTPERF01-BP02 Implement comprehensive performance telemetry](agentperf01-bp02.html) 
+  [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Blog: Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) 
+  [Observability and monitoring, Building serverless architectures for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Elevate application and generative AI observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs) 

 **Related examples:** 
+  [GitHub: Amazon Bedrock AgentCore samples, Observability tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
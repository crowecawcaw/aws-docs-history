

# AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions
<a name="agentperf02-bp04"></a>

 User-facing agents are judged on perceived latency, not total processing time. Time-to-first-token (TTFT), the delay before the first output reaches the user, is the dominant perceived-performance signal, and streaming delivery keeps TTFT short even when total processing takes several seconds. Agentic streaming is complicated by reasoning loops that must pause mid-stream to invoke tools and by multi-agent workflows where the final agent streams while upstream agents are still producing. 

 **Desired outcome:** 
+  You have TTFT tracked as a distinct KPI from end-to-end latency, with a target bounded by the interaction type. 
+  You have LLM output streamed to the user as it is generated, so the user begins seeing output well before the reasoning loop finishes. 
+  You have pre-inference latency, context assembly, prompt construction, retrieval, kept short enough that it doesn't dominate TTFT. 
+  You have tool invocations handled within streams so the user receives progress feedback rather than an unexplained pause when the agent calls a tool mid-response. 
+  You have multi-agent workflows designed so the user-facing agent begins streaming as soon as its inputs are available, rather than blocking until every upstream agent fully completes. 

 **Common anti-patterns:** 
+  Waiting for the complete agent response before delivering any output, making perceived latency equal to total processing time rather than time-to-first-token. 
+  Streaming the LLM inference call but not the pre-inference pipeline, so context retrieval and prompt construction add seconds of delay before the first token reaches the user. 
+  Pausing the output stream with no indication when the agent invokes a tool mid-response, so the user sees partial output followed by an unexplained pause. 
+  Blocking multi-agent workflows until every upstream agent finishes before the user-facing agent begins streaming, converting sequential coordination delay into user-visible latency. 
+  Treating TTFT as interchangeable with end-to-end latency in KPIs and alarms, so regressions in time-to-first-token go unnoticed while total-duration metrics look unchanged. 

 **Benefits of establishing this best practice:** 
+  Sub-second time-to-first-token keeps the agent feeling fast even when total processing time spans several seconds. 
+  Progress feedback replaces the unexplained pauses that would otherwise appear to the user as a stall when tools run mid-stream. 
+  Tracking TTFT as a distinct KPI surfaces drift in perceived responsiveness that end-to-end latency dashboards would otherwise hide. 
+  Progressive streaming in multi-agent workflows lets the user-facing agent deliver output concurrently with upstream processing rather than blocking until every upstream step completes. 
+  A short TTFT reduces the share of users who abandon interactive workloads before any output appears. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Time-to-first-token (TTFT) is typically the performance metric that most directly shapes user perception of an interactive agent. A response that begins within a few hundred milliseconds typically feels fast to users even when total generation takes several seconds. End-to-end latency and TTFT move independently. A faster model improves total duration but leaves TTFT unchanged when the pre-inference pipeline is the bottleneck, so tracking only total latency hides the regressions users actually feel. The difference lies in instrumenting TTFT as a distinct metric, separate from total-duration dashboards. 

 Streaming the model's output is necessary but not sufficient: by the time the first token leaves the model, the agent can already have consumed the entire TTFT budget on work that happens before inference begins. Context assembly, prompt construction, retrieval, and serial pre-checks all count, and streaming recovers nothing from that window. 

 The pre-inference path is usually where the most significant TTFT improvements come from: compressing retrieval, narrowing retrieved context, and parallelizing independent pre-inference steps. The same concurrency and warm-connection patterns that reduce total latency elsewhere in this pillar apply to the pre-inference path, and they pay back specifically against TTFT. Post-inference filtering is also in the budget. [Amazon Bedrock Guardrails streaming modes](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) introduce an explicit trade-off between moderation accuracy and TTFT that must be tuned to the workload rather than left at default. 

 On Amazon Bedrock, [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) is the model-agnostic streaming inference API recommended for chat and agent workloads, while [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) remains available when a model-specific payload shape is required. Both emit an event stream of content-block start, delta, and stop events that the agent layer translates into user-visible output. 

 Tool invocation introduces a discontinuity. When the model decides to call a tool, the event stream opens a content block of type toolUse, streams the tool's input as deltas, and then pauses while the agent runs the tool and feeds results back. A client that receives no signal during this gap shows the user partial output followed by a silent stall. The baseline pattern, buffer-and-resume with an explicit progress indicator, forwards a user-visible status the moment a tool-use block appears and resumes streaming when the next content block starts. More advanced patterns such as speculative streaming exist, but the baseline is that no silent pause reaches the user. 

 Multi-agent pipelines amplify the TTFT problem when every upstream agent must fully complete before the user-facing agent begins. Each serial handoff contributes its full duration to TTFT rather than overlapping with downstream work. Progressive streaming is the alternative, where the user-facing agent begins reasoning as soon as its minimum required inputs are available, and upstream agents' intermediate outputs stream into its context as they are produced. 

 Agent frameworks expose this pattern directly: [Strands Agents](https://strandsagents.com/) yields agent events (tokens, tool calls, messages) as an async iterator that downstream consumers can subscribe to, and graph-based orchestrators such as LangGraph expose equivalent streaming primitives. Reserve synchronous full-response handoff for workflows where the downstream agent genuinely can't begin until the upstream result is complete. 

 Two AWS capabilities reduce inter-token latency and coordination overhead beyond what API choice alone can deliver. [Amazon Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at publication) reduces inter-token latency on supported models through routing and capacity optimizations, at the cost of tighter throughput limits and model-specific token ceilings. For voice and real-time interactive workloads, [Amazon Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html) over WebSocket or WebRTC allows the client to send input while the agent is still streaming output, the prerequisite for natural interrupt and turn-taking behavior in voice agents. 

 [Amazon Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html) provides a speech-to-speech path on Amazon Bedrock. You can route voice through Amazon Nova Sonic rather than separate speech-to-text, text-generation, and text-to-speech stages, collapsing multiple sequential stages into one bidirectional stream. This approach typically provides substantial TTFT improvements for voice workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define TTFT targets for each user-facing interaction type:** Set a TTFT target per workload based on how the user consumes output, text chat tolerates hundreds of milliseconds, voice tolerates far less, batch pipelines have no user-facing TTFT at all. Treat the target as a budget to be allocated across pre-inference work, model first-token latency, and any post-processing, and anchor it to user research or published interaction-design norms rather than a round number. 

1.  **Instrument TTFT as two distinct metrics, pipeline TTFT and model TTFT:** Emit *pipeline TTFT* at the user-facing boundary (the first output byte reaching the client) as the SLO KPI, and *model TTFT* at the first text delta from the inference call whose output first streams to the user, which isolates model and routing behavior from pre-inference and post-processing contributions. Publish both through [OpenTelemetry through the CloudWatch OTLP endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) or [CloudWatch Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html). When pipeline TTFT and model TTFT diverge, the gap points at the non-model contributors. 

1.  **Extend TTFT instrumentation to multi-inference and voice workloads:** When an agent makes multiple inference calls per request, planners, routers, sub-agent fan-outs, treat silent upstream calls as part of the pre-inference budget and emit per-call TTFT as a tagged dimension so the contribution of each inference call remains visible for diagnosis. For voice workloads, add time-to-first-audio-chunk because text-token arrival is an upstream signal, not the user boundary. 

1.  **Reduce pre-inference latency on the critical path to the first token:** Profile the work that happens between request arrival and the first inference call, context assembly, retrieval, prompt construction, pre-checks, and compress or parallelize it so most of the TTFT budget remains when the model begins generating. The concurrency and connection-reuse patterns applied elsewhere to reduce end-to-end latency pay back specifically against TTFT when applied to the pre-inference path. Streaming token delivery can't recover any time lost before the first model call. 

1.  **Use streaming inference APIs rather than synchronous inference for user-facing agents:** Call [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) as the model-agnostic default for chat and agent workloads. Use [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) only when a model-specific payload shape is required. Consume the event stream as it arrives and forward each content-block delta to the client rather than buffering the full response server-side. 

1.  **Tune Amazon Bedrock Guardrails streaming mode when guardrails are in the critical path:** If [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) filters output on the user-facing path, choose the stream processing mode based on the workload's policy tolerance, synchronous processing raises moderation accuracy and raises TTFT, asynchronous processing preserves TTFT at the cost of potentially emitting a token that is later retracted. Drive the decision for mode by the content-risk profile of the workload. 

1.  **Surface tool-invocation events to the user rather than pausing the stream silently:** When the model emits a tool-use event mid-stream, forward a user-visible progress indicator to the client before the agent begins executing the tool, and resume streaming when the next content block starts. Use the explicit start and stop boundaries of the tool-use content block as the signal to transition the UI between streaming and working states, rather than letting the client see a silent gap. 

1.  **Stream multi-agent workflows progressively rather than blocking on upstream completion:** Design the orchestration so the user-facing agent begins reasoning as soon as its minimum required inputs are available, and pipe upstream intermediate events into its context as they are produced. Agent frameworks expose this streaming-handoff pattern directly through async-iterator primitives such as [Strands Agents'](https://strandsagents.com/) streaming API and equivalent mechanisms in graph-based orchestrators. Reserve synchronous full-response handoff for workflows where the downstream agent genuinely can't begin until the upstream result is complete. 

1.  **Evaluate latency-optimized inference for inter-token latency on supported models:** [Amazon Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at publication) reduces inter-token latency on supported models, Amazon Nova Pro, Anthropic Claude 3.5 Haiku, and Meta Llama 3.1 70B/405B, through routing and capacity optimizations, at the cost of tighter throughput limits and model-specific token ceilings. Enable the latency mode on the runtime API and validate with the two-metric TTFT instrumentation that the reduction is real for the workload rather than a cache-warmed artifact. 

1.  **Use AgentCore Runtime bi-directional streaming and Amazon Nova Sonic for voice and real-time workloads:** For voice agents and other workloads where the user must interrupt or turn-take, run the agent on [Amazon Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html) over WebSocket or WebRTC so the client can send input while the agent is streaming output. Route voice specifically through [Amazon Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html), which collapses the separate speech-to-text, text-generation, and text-to-speech stages of a traditional voice pipeline into a single bidirectional stream, typically a substantial TTFT improvement for voice workloads. 

1.  **Re-measure TTFT after each change and as traffic shifts:** Re-profile both pipeline TTFT and model TTFT under representative production load after applying streaming, pre-inference, tool-handling, or runtime changes, because optimizations that work in isolation frequently regress at scale. Alert on TTFT percentile violations distinct from end-to-end latency SLOs so regressions in perceived responsiveness surface before they reach users. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets](agentperf01-bp03.html) 
+  [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 
+  [AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns](agentperf05-bp04.html) 

 **Related documents:** 
+  [Amazon Bedrock ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) 
+  [Amazon Bedrock InvokeModelWithResponseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) 
+  [Amazon Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) 
+  [Amazon Bedrock Guardrails streaming](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) 
+  [Amazon Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html) 
+  [Get started with bidirectional streaming using WebSocket on AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-websocket.html) 
+  [Amazon Nova Sonic, real-time conversational speech](https://docs.aws.amazon.com/nova/latest/userguide/speech.html) 
+  [CloudWatch Embedded Metric Format specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html) 
+  [Publishing custom metrics to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [AWS blog: Bi-directional streaming for real-time agent interactions now available in Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/bi-directional-streaming-for-real-time-agent-interactions-now-available-in-amazon-bedrock-agentcore-runtime/) 

 **Related examples:** 
+  [Amazon Bedrock AgentCore samples, Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime) 
+  [Amazon Bedrock AgentCore samples, Nova Sonic integration](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/nova/nova-sonic) 

 **Related workshops:** 
+  [Diving Deep into Bedrock AgentCore, Runtime](https://catalog.workshops.aws/agentcore-deep-dive/en-US/20-agentcore-runtime) 

 **Related tools:** 
+  [Strands Agents](https://strandsagents.com/) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
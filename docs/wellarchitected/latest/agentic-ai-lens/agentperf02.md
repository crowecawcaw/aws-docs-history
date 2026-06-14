# Core processing and reasoning pipeline optimization

A well-optimized reasoning pipeline is what makes agents feel
fast, responsive, and worth using. It is the difference between an
agent that users rely on and one they abandon. The reasoning
pipeline (encompassing perception, reasoning, planning,
decision-making, and action execution) is the performance-critical
path of every agentic AI system. Each iteration of the agent loop
involves an LLM inference call, which is typically the most
latency-intensive and resource-consuming operation in the stack.
Optimizing core processing requires designing efficient reasoning
pipelines that minimize unnecessary iterations, selecting models
appropriate to task complexity, reducing execution path latency
through architectural decisions, and optimizing streaming delivery
to minimize perceived latency for user-facing interactions. Poor
pipeline design produces agents that are slow, expensive, and
unresponsive, regardless of how well the underlying infrastructure
is provisioned.

For the actor model as a foundational execution pattern, see
[AGENTREL01-BP03](agentrel01-bp03.md "agentrel01-bp03.md").

| AGENTPERF02: How do you optimize core agent processing and<br>reasoning pipelines? |
| ---------------------------------------------------------------------------------- |
|                                                                                    |

## Capability intent

- Reasoning pipelines are bounded by iteration caps and
  confidence-based early termination so simple tasks resolve
  in one or two iterations while complex tasks receive the
  iterations they need.
- Each task class is routed to the smallest model that meets
  its quality bar, with cascading fallback to a more capable
  model when the assigned model produces low-confidence
  outputs.
- Independent operations execute concurrently, connections and
  runtimes are warm across invocations, and repeated lookups
  within a single request are deduplicated through
  request-scoped caches.
- User-facing agents stream tokens with sub-second
  time-to-first-token, pre-inference work is compressed to
  preserve the TTFT budget, and tool invocations mid-stream
  surface progress to the user rather than unexplained pauses.
- Retry strategies and graceful degradation paths are bounded
  by explicit latency budgets so failure recovery stays inside
  the end-to-end service level objective rather than eroding
  it silently.

## Maturity levels

These levels summarize what each stage of maturity looks like
for core processing and reasoning pipeline optimization as a
whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agents run without iteration limits or confidence-based<br>termination, and a single large model serves every task<br>regardless of complexity. Independent operations run<br>sequentially, connections are re-established per<br>invocation, and user-facing agents wait for the complete<br>response before any output reaches the user. Failures<br>propagate without explicit retry budgets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2     | Emerging  | Iteration caps and basic retry limits are in place for<br>flagship agents, and task classification is documented<br>but not consistently routed. Streaming is enabled for<br>some user-facing interactions but the pre-inference path<br>isn't optimized for time-to-first-token. Model selection<br>happens at design time rather than benchmarked against<br>the workload's task distribution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 3     | Defined   | Task classes are mapped to model tiers benchmarked on<br>the workload's own distribution through<br>[Amazon<br>Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md"), with cascading<br>fallback configured for low-confidence outputs.<br>Independent operations execute concurrently inside<br>framework primitives such as the<br>[Strands<br>Agents](https://strandsagents.com/ "https://strandsagents.com/"), and<br>[Amazon<br>Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") streaming APIs deliver output<br>token-by-token. Retry strategies are bounded by explicit<br>latency and token budgets.                                                                                                                                                                                                  |
| 4     | Proactive | Model assignments and routing rules are externalized as<br>runtime configuration in<br>[AWS AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md") and promoted through progressive<br>rollouts gated by CloudWatch alarms. Connection pooling<br>through<br>[Amazon RDS Proxy](../../../AmazonRDS/latest/UserGuide/rds-proxy.md "../../../AmazonRDS/latest/UserGuide/rds-proxy.md") and warm runtimes through<br>[Amazon<br>Bedrock AgentCore Runtime sessions](../../../bedrock-agentcore/latest/devguide/runtime-sessions.md "../../../bedrock-agentcore/latest/devguide/runtime-sessions.md") or<br>[AWS Lambda provisioned concurrency](../../../lambda/latest/dg/provisioned-concurrency.md "../../../lambda/latest/dg/provisioned-concurrency.md") remove cold starts<br>on the critical path. Tool invocations during streaming<br>surface structured progress events to the client.               |
| 5     | Optimized | Pipeline shape, caps, model routing, and fallback rules<br>are recalibrated continuously from production telemetry,<br>and<br>[Amazon<br>Bedrock latency-optimized inference](../../../bedrock/latest/userguide/latency-optimized-inference.md "../../../bedrock/latest/userguide/latency-optimized-inference.md") is evaluated<br>for each eligible model. Voice and real-time workloads<br>run on<br>[Amazon<br>Bedrock AgentCore Runtime bi-directional<br>streaming](../../../bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.md "../../../bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.md") through<br>[Amazon<br>Nova Sonic](../../../nova/latest/userguide/speech.md "../../../nova/latest/userguide/speech.md"). Reasoning iteration counts, TTFT, and<br>fallback-escalation rates sit alongside latency and cost<br>on every dashboard, and the organization contributes<br>pipeline patterns back to its communities of practice. |

## Common issues to watch for

- Agents reason without iteration caps or early termination
  signals, producing runaway loops that consume tokens and
  time without improving output quality.
- A single large model serves every task regardless of
  complexity, paying the latency and cost premium of a
  heavyweight model for work a smaller one resolves as well.
- Independent operations execute sequentially and connections
  are re-established per invocation, so end-to-end latency
  becomes the sum of every operation duration plus repeated
  setup overhead.
- User-facing agents wait for the complete response before any
  output reaches the user, so perceived latency equals total
  processing time rather than the shorter time-to-first-token
  streaming would deliver.
- Tool invocations mid-stream pause the output without
  user-visible progress, creating perceived stalls where users
  see partial output followed by silence for several seconds.

###### Best practices

- [AGENTPERF02-BP01 Design efficient reasoning pipelines](agentperf02-bp01.md "agentperf02-bp01.md")
- [AGENTPERF02-BP02 Implement task-appropriate model selection strategies](agentperf02-bp02.md "agentperf02-bp02.md")
- [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.md "agentperf02-bp03.md")
- [AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions](agentperf02-bp04.md "agentperf02-bp04.md")

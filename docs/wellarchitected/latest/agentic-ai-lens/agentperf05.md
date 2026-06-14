# Workflow orchestration and multi-agent collaboration

The most impactful agent use cases (complex research, multi-domain
customer service, and process automation) require multiple agents
working together, and well-designed orchestration is what makes
the whole greater than the sum of its parts. Complex agentic AI
systems often involve multiple agents collaborating to solve tasks
that exceed the capability of any single agent. Workflow
orchestration coordinates these multi-agent interactions through
patterns like supervisor-worker hierarchies, peer-to-peer
collaboration, and pipeline-based task decomposition. The
performance of multi-agent systems depends on how efficiently work
is distributed, how agents are selected and invoked, how
intermediate results are passed between agents, and how parallel
execution is used to reduce latency.

| AGENTPERF05: How do you optimize workflow orchestration<br>and multi-agent collaboration for performance? |
| --------------------------------------------------------------------------------------------------------- |
|                                                                                                           |

## Capability intent

- Multi-agent workflows run with minimal orchestration
  overhead, so end-to-end latency approaches the critical path
  of dependent operations rather than the sum of every step.
- Orchestration patterns are matched to task shape, with
  dynamic graphs for reasoning-driven flows, Step Functions
  for deterministic skeletons, and hybrid layers for workflows
  that combine both.
- Independent subtasks run in parallel and large intermediate
  results are passed by reference, keeping the orchestration
  layer small and the critical path short.
- Collaboration models are matched to task characteristics
  (supervisor-worker, pipeline, peer-to-peer, swarm), and
  capabilities default to tools rather than sub-agents unless
  they need independent reasoning.
- Multi-stage pipelines use streaming and micro-batching to
  overlap stage processing, with right-sized compute per stage
  and end-to-end tracing that makes bottlenecks attributable.
- Delegation and handoff operations transfer only the context
  the receiving agent needs, through shared context stores and
  standardized interfaces, and handoff latency is a
  first-class metric.

## Maturity levels

These levels summarize what each stage of maturity looks like
for workflow orchestration and multi-agent collaboration as a
whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Multi-agent workflows run sequentially without explicit<br>orchestration. Teams chain agent calls in application<br>code, pass full payloads and conversation history<br>between steps, and use sub-agents for work that a tool<br>could do in milliseconds. There is no cycle detection,<br>no timeout, and no per-step telemetry, so runaway<br>delegation chains and slow branches surface only as<br>user-visible failures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2     | Emerging  | Workflows are classified as dynamic, deterministic, or<br>hybrid, and each is placed on a suitable orchestrator.<br>[AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") is adopted for deterministic<br>flows, and native framework orchestration is used for<br>dynamic graphs. Basic parallelism is enabled for<br>independent subtasks, and shared stores on<br>[Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") or<br>[Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") replace inline payloads for large<br>results. Timeouts and fallback paths exist for the most<br>critical workflows.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3     | Defined   | Dynamic graph workflows run with cycle detection,<br>maximum depth limits, and bounded fan-out cardinality.<br>Collaboration models are selected per workflow<br>(supervisor-worker, pipeline, peer-to-peer, swarm) using<br>framework-native primitives such as<br>[Strands<br>Agents](https://strandsagents.com/ "https://strandsagents.com/") agent-as-tool and<br>[Amazon<br>Bedrock Agents multi-agent collaboration](../../../bedrock/latest/userguide/agents-multi-agent-collaboration.md "../../../bedrock/latest/userguide/agents-multi-agent-collaboration.md").<br>Multi-stage pipelines use streaming through the<br>[Amazon<br>Bedrock streaming inference API](../../../bedrock/latest/userguide/api-methods-run-inference.md "../../../bedrock/latest/userguide/api-methods-run-inference.md") and<br>micro-batching, with right-sized compute per stage.<br>Shared context stores on<br>[Amazon<br>Bedrock AgentCore Memory](../../../bedrock-agentcore/latest/devguide/memory.md "../../../bedrock-agentcore/latest/devguide/memory.md") carry delegation context<br>instead of inline transfers.                                                                                                                                                      |
| 4     | Proactive | Per-step, per-branch, and workflow-level timeouts are<br>derived from the task SLO, and slow branches terminate<br>with the best partial result rather than blocking.<br>End-to-end distributed tracing through<br>[Amazon<br>Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") or<br>[AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") makes the critical path attributable, and<br>stage rebalancing is a routine practice. Delegation<br>happens through standardized interfaces on<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md"), asynchronous<br>delegation with<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") callbacks is used where the parent<br>has parallel work, and predictable receivers are<br>pre-warmed using<br>[AWS Lambda provisioned concurrency](../../../lambda/latest/dg/provisioned-concurrency.md "../../../lambda/latest/dg/provisioned-concurrency.md") or warm session<br>pools. |
| 5     | Optimized | Orchestration patterns, collaboration models, and<br>context schemas are continuously refined against<br>measured data. Handoff latency, parallel efficiency,<br>state payload size, and collaboration overhead metrics<br>sit on shared dashboards that drive design iteration.<br>New workflows start from reusable patterns, and the<br>organization contributes reference implementations for<br>dynamic graph orchestration, hybrid Step Functions<br>skeletons, and standardized delegation interfaces back<br>into the internal community.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Common issues to watch for

- Teams default to sub-agents for capabilities that a tool
  call would handle in milliseconds, paying full
  reasoning-loop cost for deterministic, single-step work.
- Workflows run steps sequentially even when the dependency
  graph permits parallel execution, pushing end-to-end latency
  to the sum of step durations rather than the critical path.
- Dynamic graph orchestrations run without cycle detection,
  depth limits, or bounded fan-out, so the reasoning loop
  occasionally produces unbounded delegation chains or
  excessive concurrent branches.
- Orchestrators carry large payloads inline between steps
  rather than passing references, inflating state size and
  forcing the orchestrator's context window to hold raw data
  it doesn't need.
- Multi-stage pipelines use identical compute configurations
  for every stage, over-provisioning lightweight stages and
  starving compute-intensive ones, and skip streaming or
  micro-batching that could overlap stage processing.
- Delegation transfers the full conversation history on every
  handoff, receiving agents re-derive context the parent
  already had, and handoff latency isn't measured so the
  overhead grows silently.

###### Best practices

- [AGENTPERF05-BP01 Design efficient workflow orchestration patterns](agentperf05-bp01.md "agentperf05-bp01.md")
- [AGENTPERF05-BP02 Implement optimized multi-agent collaboration models](agentperf05-bp02.md "agentperf05-bp02.md")
- [AGENTPERF05-BP03 Optimize multi-stage AI pipeline execution](agentperf05-bp03.md "agentperf05-bp03.md")
- [AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns](agentperf05-bp04.md "agentperf05-bp04.md")

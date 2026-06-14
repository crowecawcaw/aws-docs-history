# Communication and protocol efficiency

Efficient communication between agents, tools, and services scales
multi-agent systems from prototypes to production without latency
growing alongside complexity. Agentic AI systems rely on
communication between agents, tools, services, and users through
various protocols and messaging patterns. The efficiency of these
communication channels directly impacts agent performance. Every
message exchange adds latency, every protocol handshake consumes
time, and every serialization or deserialization operation uses
compute resources. Optimizing communication requires selecting
appropriate protocols for each interaction pattern, implementing
efficient asynchronous messaging, and designing event-driven
architectures that minimize polling and unnecessary processing.

| AGENTPERF04: How do you achieve efficient communication<br>and protocol usage across agent interactions? |
| -------------------------------------------------------------------------------------------------------- |
|                                                                                                          |

## Capability intent

- Agent-to-agent and agent-to-service communication uses
  asynchronous messaging by default, with synchronous calls
  reserved for interactions that genuinely require an
  immediate response.
- Protocols are selected per interaction pattern, with MCP for
  tool integration, A2A for agent-to-agent coordination, and
  streaming transports such as WebSocket for real-time user
  interactions.
- Event-driven integration is push-based and precisely
  filtered, so agents are invoked only for events that match
  their processing requirements and consume no compute when
  idle.
- Message and event payloads carry references to durable
  stores rather than embedded data, keeping transfer times low
  and letting consumers skip work on events that have become
  irrelevant.
- Connection pooling, protocol-level compression, and token
  caching keep per-interaction overhead flat as the number of
  agent-to-agent hops and tool invocations grows.

## Maturity levels

These levels summarize what each stage of maturity looks like
for communication and protocol efficiency as a whole.

| Level | Name      | What it looks like                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Initial   | Agent communications run over synchronous HTTP/REST with<br>full JSON payloads on every call. Polling is the default<br>event-detection mechanism. Connections are opened per<br>call, and protocol choice, payload size, and<br>authentication overhead are not tracked. Scaling<br>problems surface only after an outage or a timeout<br>cascade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2     | Emerging  | Teams have introduced asynchronous messaging through<br>[Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") for point-to-point workflows and<br>[Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") for fan-out. Dead letter queues are attached<br>to critical queues and queue depth is monitored. Most<br>event triggers still use polling, and protocol selection<br>is inconsistent across agents.                                                                                                                                                                                                                                                                                                               |
| 3     | Defined   | MCP is standardized for agent-to-tool communication<br>through<br>[Amazon<br>Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md"), and<br>[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") with content-based filtering routes<br>push-based events to the agents that need them. Message<br>payloads pass references rather than data, and agents on<br>[Amazon<br>Bedrock AgentCore Runtime](../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md "../../../bedrock-agentcore/latest/devguide/agents-tools-runtime.md") use the runtime's<br>session management for within-workflow communication.<br>Protocol selection guidelines are documented and<br>followed. |
| 4     | Proactive | A2A through AgentCore Runtime handles structured<br>agent-to-agent coordination, and<br>[Amazon API Gateway WebSocket APIs](../../../apigateway/latest/developerguide/apigateway-websocket-api.md "../../../apigateway/latest/developerguide/apigateway-websocket-api.md") serve streaming user<br>interactions. Connection pooling, protocol-level<br>compression, and token caching through<br>[Amazon<br>Bedrock AgentCore Identity](../../../bedrock-agentcore/latest/devguide/identity.md "../../../bedrock-agentcore/latest/devguide/identity.md") are standard.<br>Idempotency keys protect against duplicate event<br>delivery. Backpressure on queues and event-to-invocation<br>latency are alerted on and drive automated scaling.                                                                                                           |
| 5     | Optimized | Protocol selection, queue sizing, and event filtering<br>are recalibrated continuously from production telemetry.<br>Per-hop authentication and serialization overhead is<br>budgeted and optimized at the workflow level rather than<br>per service. Communication patterns and interoperability<br>work feed back into internal standards and are shared<br>with the broader agentic AI community.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Common issues to watch for

- Teams default to synchronous HTTP/REST for every agent
  communication, creating tight coupling where a slow
  downstream component blocks the entire upstream chain and
  propagates scaling issues across the workflow.
- Agents receive broad event streams without content-based
  filtering and spend compute receiving, parsing, and
  discarding events they never act on, which inflates cost and
  obscures the latency of events that do matter.
- Message and event payloads inline full data (documents,
  base64-encoded files, entire records) rather than passing
  references, so queue throughput and network transfer are
  consumed by payloads that consumers could fetch on demand.
- Backpressure and dead letter queues are missing, which lets
  fast producers overwhelm slow consumers and hides persistent
  message failures until a downstream timeout or data-loss
  incident forces investigation.
- Authentication overhead, connection setup, and serialization
  costs are tracked as service-level metrics rather than
  per-hop overheads, so a workflow with many agent-to-agent
  hops accumulates silent latency that no single service's
  telemetry surfaces.

###### Best practices

- [AGENTPERF04-BP01 Optimize asynchronous message handling patterns](agentperf04-bp01.md "agentperf04-bp01.md")
- [AGENTPERF04-BP02 Implement efficient protocol-based agent communications](agentperf04-bp02.md "agentperf04-bp02.md")
- [AGENTPERF04-BP03 Design high-performing event-driven integration patterns](agentperf04-bp03.md "agentperf04-bp03.md")

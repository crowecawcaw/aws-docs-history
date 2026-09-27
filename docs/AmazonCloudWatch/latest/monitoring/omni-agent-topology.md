

# Agent topology
<a name="omni-agent-topology"></a>

The agent topology shows how the parts of your agent connect — agents, tools, and models — as a graph built from your traces. Where a trace shows one run in sequence, the topology aggregates the paths your agent took across runs: which components exist, which call which, and where latency concentrates.

The agent topology is in **preview release** and is subject to change.

For the map of your services and their dependencies, see [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md).

**How the graph is built**

Omni derives the graph from your spans: each agent, tool, and model that appears in your traces becomes a node, and the transitions between them (which component ran after which) become the edges. The graph is only as complete as your instrumentation: if tool calls are not instrumented as spans, those tools do not appear in the graph. See [Supported environments, languages, and frameworks](omni-supported-environments-languages-and-frameworks.md).

**Choose a view**

The **Flow** and **Graph** toggle changes how the same nodes and transitions are drawn:
+ **Flow**, the view the map opens in, reads left to right as the sequence of steps your agent ran, aggregated across runs.
+ **Graph** draws the components and transitions as a network diagram. Use it to inspect the branching structure and the connections between components.

**Group spans into nodes**

The selector next to the view toggle offers two ways to group spans into the map's nodes:
+ **Default** builds the map from the span kinds your instrumentation already emits: agent, tool, and model spans in the order they ran, with parallel calls grouped into a single step. It works with traces from any supported framework and needs no additional span attributes.
+ **Steps** builds the map from explicit graph metadata on your spans: `agent_graph.node` names the node a span belongs to, `agent_graph.step` orders the nodes, and `agent_graph.kind` optionally sets a node's type. Step spans must be direct children of the trace's root span. LangGraph instrumentation adds this metadata automatically; for other frameworks, set the attributes yourself (for example, in a span processor). Choose **Steps** when your agent is authored as an explicit graph and you want the map to mirror the nodes you defined. If the selected traces carry no step metadata, the map reports it. Switch back to **Default**.

**To view the agent topology**

1. Open your space, then choose **Agent topology**.

1. Select a node to see its trace volume and average latency.

1. From a node with high latency, open its related traces to see those calls in context. See [Agent traces](omni-agent-traces.md).

![The agent topology showing agents, tools, and models as connected nodes, with one tool node selected and its trace volume and average latency shown.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-agent-topology.png)



# Monitor agents in the web UI
<a name="omni-monitor-agents-in-the-web-ui"></a>

Use the Omni web UI to monitor your agents in production, including individual agent traces and sessions, aggregate metrics such as request volume, errors, latency, and token usage, and dependency relationships through the application map (see [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md)).

Aggregate views are available in the Omni web UI only. For monitoring and troubleshooting during development in the IDE, see [Develop with the IDE extension](omni-develop-with-the-ide-extension.md).

**Aggregate metrics**
+ **Request volume** — the number of times the agent is invoked.
+ **Errors** — the number of traces that contain errors.
+ **Latency** — the duration of each run.
+ **Token usage** — the total input and output tokens consumed.

**To monitor your agents**

1. Sign in to your space. To set up users and permissions, see [Set up Omni](omni-set-up-omni.md).

1. Review the aggregate views for request volume, errors, latency, and token usage across your agents. Filter by agent or time range.

1. Select a metric or a spike to view the underlying traces in [Agent traces](omni-agent-traces.md), or follow a multi-turn conversation in [Agent sessions](omni-agent-sessions.md). If you do not yet know which runs to inspect, use the agent topology to see which components take part. See [Agent topology](omni-agent-topology.md).

1. Check your evaluation results for the same period. To find evaluation trends, see [Evaluators and evaluations](omni-agents-evaluators.md).

![The aggregate monitoring view showing request volume, errors, latency, and token usage across several agents, with a visible error spike on one agent.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-monitor-overview.png)


Combine these views with evaluation results. An agent can be fast, low-cost, and error-free but still give wrong answers. To measure response quality, see [Evaluate agent quality](omni-agents-evaluate.md). When you find a quality regression here, follow [Tutorial: Fix a production quality regression](omni-agents-close-the-loop.md).
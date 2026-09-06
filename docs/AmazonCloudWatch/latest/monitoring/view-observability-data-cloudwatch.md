

# View observability data in CloudWatch
<a name="view-observability-data-cloudwatch"></a>

After you enable observability for your agentic resources, you can view the collected data in CloudWatch.

## View the GenAI Observability dashboard
<a name="view-genai-observability-dashboard"></a>

1. Open the CloudWatch console.

1. Under the GenAI Observability dashboard, view data related to model invocations and agents on Amazon Bedrock AgentCore.

1. In the Amazon Bedrock AgentCore sub-menu, you can choose the following views:
   + **Agents View** – Lists all your agents, both on and off runtime. Choose an agent to view runtime metrics, sessions, traces, and evaluations specific to that agent
   + **Sessions View** – Navigate across all sessions associated with agents
   + **Traces View** – View traces and span information for agents. Choose a trace to explore the trace trajectory and timeline

## View logs
<a name="view-logs"></a>

1. Open the CloudWatch console.

1. In the navigation pane, expand **Logs** and choose **Log groups**.

1. Search for your agent's log group:
   + Standard logs (stdout/stderr) – `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs] <UUID>`
   + OTEL structured logs – `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs`

## View traces and spans
<a name="view-traces-spans"></a>

1. Open the CloudWatch console.

1. In the navigation pane, choose **Transaction Search**.

1. Navigate to `/aws/spans/default`.

1. Filter by service name or other criteria.

1. Choose a trace to view the detailed execution graph.

## View metrics
<a name="view-metrics"></a>

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**.

1. Navigate to the **bedrock-agentcore** namespace.

1. Explore the available metrics.
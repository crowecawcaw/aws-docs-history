# View observability data in CloudWatch

After you enable observability for your agentic resources, you can view the collected data in CloudWatch.


## View the GenAI Observability dashboard


1. Open the CloudWatch console.
2. Under the GenAI Observability dashboard, view data related to model invocations and agents on Amazon Bedrock AgentCore.
3. In the Amazon Bedrock AgentCore sub-menu, you can choose the following views:




	* **Agents View** – Lists all your agents, both on and off runtime. Choose an agent to view runtime metrics, sessions, and traces specific to that agent
	* **Sessions View** – Navigate across all sessions associated with agents
	* **Traces View** – View traces and span information for agents. Choose a trace to explore the trace trajectory and timeline

## View logs


1. Open the CloudWatch console.
2. In the navigation pane, expand **Logs** and choose **Log groups**.
3. Search for your agent's log group:




	* Standard logs (stdout/stderr) – `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs] <UUID>`
	* OTEL structured logs – `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/runtime-logs`

## View traces and spans


1. Open the CloudWatch console.
2. In the navigation pane, choose **Transaction Search**.
3. Navigate to `/aws/spans/default`.
4. Filter by service name or other criteria.
5. Choose a trace to view the detailed execution graph.

## View metrics


1. Open the CloudWatch console.
2. In the navigation pane, choose **Metrics**.
3. Navigate to the **bedrock-agentcore** namespace.
4. Explore the available metrics.

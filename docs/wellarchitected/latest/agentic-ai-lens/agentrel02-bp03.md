

# AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring
<a name="agentrel02-bp03"></a>

 Generic logs miss what matters most for agents: decision points, tool invocations, and LLM interactions. Structured telemetry with behavioral baselines exposes anomalies early and gives operators the audit trail they need to reconstruct why an agent did what it did. 

 **Desired outcome:** 
+  You capture decision points, tool invocations, and LLM interactions for every agent invocation. 
+  You have behavioral baselines per agent and automated alarms that fire when metrics drift outside expected ranges. 
+  You detect behavioral drift through periodic evaluation, not only through infrastructure errors. 

 **Common anti-patterns:** 
+  Running generic logging that doesn't capture agent-specific decision points, leaving teams unable to understand why an agent produced an unexpected outcome. 
+  Operating without behavioral baselines, so there is no basis for deciding when agent behavior has actually deviated. 
+  Relying only on manual log review, which delays detection of reliability issues until users complain. 

 **Benefits of establishing this best practice:** 
+  Automated anomaly detection catches reliability issues before they cascade. 
+  Full execution transparency through decision-point logging speeds up root-cause analysis. 
+  Structured audit trails reconstruct agent decision-making for compliance and debugging. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Behavioral monitoring starts with capturing the execution path, not the final response. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides OpenTelemetry-compatible telemetry that covers the full path of each agent invocation, from initial request through LLM inference, tool calls, memory access, and response generation. Tag traces with agent-specific metadata such as agent ID, task type, model used, and tool calls made, so filtering and analysis target the agent or failure scenario of interest. 

 Raw telemetry is necessary but not sufficient. Enable [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) to capture every LLM request and response, including prompts, model parameters, token counts, and latency. Without that depth, reconstructing "why did the agent choose this tool" reduces to guessing from summary metrics. 

 Collect agent-specific metrics over a representative period, including tool invocation frequency, output token count distribution, task completion rate, and error rate by type. Apply [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) so the system learns the expected range rather than relying on fixed thresholds. Configure alarms on anomaly detection bands. Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to periodically assess agent behavior against quality benchmarks so behavioral drift that doesn't show up as infrastructure errors still gets caught. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable AgentCore Observability across every invocation:** Turn on [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with OpenTelemetry tracing and tag traces with agent-specific metadata. 

1.  **Capture full LLM request/response data:** Enable [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) for anomaly analysis and audit. 

1.  **Establish behavioral baselines:** Collect representative agent-specific metrics and apply [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) so thresholds are learned rather than hand-tuned. 

1.  **Configure alarms on anomaly detection bands:** Trigger investigation workflows when metrics drift outside expected ranges. 

1.  **Run AgentCore Evaluations on a periodic cadence:** Use [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to detect behavioral drift against quality benchmarks, not only infrastructure signals. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL02-BP01 Design agents for specific and atomic tasks](agentrel02-bp01.html) 
+  [AGENTREL02-BP02 Limit agent permissions to minimum required access](agentrel02-bp02.html) 
+  [AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing](agentrel08-bp02.html) 
+  [AGENTCOST07-BP02 Establish proactive anomaly detection for agent cost patterns](agentcost07-bp02.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 
+  [Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Amazon Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) 
+  [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
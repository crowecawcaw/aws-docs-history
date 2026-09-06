

# AGENTSEC06-BP04 Monitor and detect coordination anomalies
<a name="agentsec06-bp04"></a>

 Distributed tracing tells you what happened on one request. Coordination monitoring tells you when many requests start behaving differently from the baseline. Tracking inter-agent message rates, workflow frequencies, and topology changes against established baselines catches issues through their observable impact on coordination before they escalate into security events. 

 **Desired outcome:** 
+  You detect anomalous coordination patterns such as unexpected agent communication paths, unusual interaction frequencies, or coordination latency spikes in near real time and trigger alerts for investigation. 
+  You establish baseline coordination profiles for each agent workflow, so statistical anomaly detection catches deviations before they cause significant impact. 

 **Common anti-patterns:** 
+  Monitoring only infrastructure metrics (CPU, memory, and network) without tracking agent-specific coordination metrics, missing the coordination-level signals most indicative of multi-agent issues. 
+  Not establishing coordination baselines before deploying anomaly detection, which produces either excessive false positives or missed detections. 
+  Treating Amazon GuardDuty findings and agent coordination logs as separate data streams, leaving investigators without the multi-agent context that turns API-level anomalies into useful signal. 

 **Benefits of establishing this best practice:** 
+  Behavioral baselines catch coordination deviations before they propagate across the multi-agent system. 
+  Service maps compare observed communication paths against the expected trust boundary architecture, validating topology continually. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Distributed tracing (AGENTSEC05-BP02) reconstructs what happened during a specific request. Coordination anomaly detection is a different problem. It is a proactive early-warning system that watches whether coordination patterns across many requests over time are drifting from the baseline. Tracing is reactive and investigation-focused. Coordination monitoring is preventive and baseline-focused. 

 Start by defining coordination metrics for each multi-agent workflow: 
+  Inter-agent message rates 
+  Workflow execution frequencies 
+  Agent response latencies 
+  Error rates per agent pair 
+  Coordination graph topology changes 

 Publish these as Amazon CloudWatch custom metrics, establish baselines by collecting them during normal operation, and configure Amazon CloudWatch anomaly detection to automatically identify statistical deviations. 

 [Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) provides the foundation. The session, trace, and span hierarchy captures inter-agent interactions, and the default metrics on the Amazon CloudWatch generative AI observability page surface session-level patterns. For agents using the A2A protocol on AgentCore Runtime, the structured request lifecycle (agent card discovery, task delegation, result collection) generates observable events at each coordination step, which you can use to build coordination topology maps and detect when agents communicate outside their expected patterns. 

 [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) complements coordination monitoring by continually scoring agent behavior on tool selection accuracy, correctness, and other quality dimensions. If a coordinating agent starts selecting unexpected tools or producing incorrect outputs, evaluation-score drops can serve as an early warning signal before the coordination anomaly becomes visible at the workflow level. Amazon CloudWatch alarms on evaluation scores layered with coordination metrics give you a two-stage detection approach. 

 Amazon GuardDuty monitors API call patterns for all agent IAM roles. Its machine learning models detect unusual call patterns: an agent suddenly calling services it has never accessed before, or calling APIs at unusual times or from unexpected locations. Integrate GuardDuty findings with AWS Security Hub CSPM for centralized prioritization, and correlate them with agent coordination logs to connect API-level anomalies to specific multi-agent workflows. Amazon CloudWatch Logs Insights queries add another layer, analyzing agent coordination logs for patterns such as agents receiving instructions from unexpected sources, coordination loops that may indicate runaway behavior, and agents attempting to access resources outside their defined scope. Schedule these queries to run periodically and publish results to a security dashboard. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define and publish coordination metrics:** Capture inter-agent message rates, execution frequencies, response latencies, and error rates per agent pair through Amazon CloudWatch custom metrics for each multi-agent workflow. 

1.  **Establish baselines and enable anomaly detection:** Collect metrics during normal operation and configure Amazon CloudWatch anomaly detection on key metrics. 

1.  **Build topology maps:** Use [Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) service maps and A2A request lifecycle events to build coordination topology maps, and alert on unexpected topology changes that deviate from the documented trust boundary architecture. 

1.  **Layer evaluations as early warning:** Deploy [Amazon Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) to continually score agent behavior, and configure Amazon CloudWatch alarms on evaluation scores as an early-warning layer for coordination issues. 

1.  **Correlate GuardDuty with coordination logs:** Enable Amazon GuardDuty for all agent accounts, integrate findings with AWS Security Hub CSPM, and create correlation rules that connect API anomalies to specific agent coordination logs. 

1.  **Run Logs Insights queries on a schedule:** Build Amazon CloudWatch Logs Insights queries for coordination security event patterns and publish results to a security dashboard on a scheduled cadence. 

1.  **Document the response runbook:** Establish an incident response runbook for coordination anomaly alerts that defines investigation steps, escalation paths, and remediation actions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTSEC06-BP01 Encrypt and sign inter-agent messages](agentsec06-bp01.html) 
+  [AGENTSEC06-BP03 Establish trust boundaries between agents](agentsec06-bp03.html) 
+  [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](agentsec07-bp04.html) 
+  [AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html) 

 **Related documents:** 
+  [Build trustworthy AI agents with Amazon Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) 
+  [Amazon Bedrock AgentCore adds quality evaluations and policy controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) 
+  [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) 
+  [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
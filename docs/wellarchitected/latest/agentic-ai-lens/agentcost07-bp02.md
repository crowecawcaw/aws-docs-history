# AGENTCOST07-BP02 Establish proactive anomaly detection for agent cost patterns

Generic billing alerts help you find cost escalation more quickly
after it starts. Agent-specific anomaly detection catches reasoning
loop token spikes, tool invocation storms, and memory growth
quickly, and routing those alerts correctly means that you can alert
the team that owns the agent instead of the operations team.

**Desired outcome:**

- You establish ML-based anomaly detection with statistical
  baselines and deviation thresholds.
- You have custom detectors for agent-specific failure modes
  beyond generic infrastructure monitoring.
- You pair every anomaly type with an investigation runbook to
  accelerate resolution.
- You correlate anomalies to route agent-driven issues to
  development teams and infrastructure issues to operations teams.

**Common anti-patterns:**

- Deploying anomaly detection without sufficient baseline data,
  generating excessive false positives that undermine team
  confidence.
- Relying solely on generic infrastructure monitoring that misses
  agent-specific failure modes driving the highest costs.
- Detecting anomalies without investigation runbooks, leaving
  costs escalating while teams figure out diagnostic procedures as
  issues occur.
- Treating all cost spikes as equivalent when agent spikes have
  different root causes (reasoning loops, tool storms, memory
  growth) that require different remediation.
- Collecting anomaly insights without feeding them back into agent
  design changes (tighter iteration limits, better prompts, tool
  caching) that help prevent recurrence.

**Benefits of establishing this best
practice:**

- Proactive detection identifies cost escalation from
  agent-specific failure modes within minutes rather than days.
- Investigation runbooks reduce mean time to resolution by
  replacing ad-hoc analysis with guided diagnostic execution.
- Correlation analysis routes alerts to the right team (agent
  development or operations), helping prevent triage delays.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Anomaly detection needs real baselines before it is useful.
Collect 2 to 4 weeks of baseline operational data before setting
thresholds, because detectors configured on insufficient history
produce false positives that erode confidence in the whole system.
[Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") automatically learns
statistical baselines for agent cost metrics and generates dynamic
anomaly bands that adapt to seasonality and trends. Apply it to
[Amazon
Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md") metrics including token
consumption per session, tool invocation frequency, memory growth,
and cost-per-task-completion. Use 2σ for
warning and 3σ for critical alerts.

Generic infrastructure monitoring doesn't catch the failure modes
that cost agents the most money. Reasoning loop token spikes, tool
invocation storms, and memory growth are agent-specific patterns,
and they need agent-specific detectors. Reasonable initial
thresholds include:

- Reasoning loop token spikes at 5x session average
- Tool invocation storms at 3x baseline rate
- Memory storage growth at 2x per hour
- Multi-agent workflow cost escalation at 2x historical average

These catch pathological behavior early enough to help prevent
material cost impact.

Correlation analysis helps make routing a sensible choice. An
agent-driven anomaly correlates with specific agent IDs in cost
allocation tags and shows up in AgentCore Observability token
consumption or invocation patterns. An infrastructure anomaly
happens independently of agent behavior and shows up in generic
service metrics. Routing agent-driven anomalies to development
teams (with context about which reasoning pattern triggered the
spike) and infrastructure anomalies to operations teams (with
context about constrained resources) keeps alerts in front of the
people who can act on them. AgentCore Observability span analysis
drills further. Is the spike in planning tokens, tool calls, or
memory growth? That determines whether the fix is a prompt change,
a tool cache, or a tighter memory policy.

[AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/manage-ad.md "../../../cost-management/latest/userguide/manage-ad.md") provides a billing-level backstop.
Configured per agent cost allocation tag, it catches gradual
escalations that are not visible in operational metrics.
Investigation runbooks for each anomaly type (diagnostic queries,
likely root causes, and immediate mitigation actions) live in AWS Systems Manager OpsCenter, with CloudWatch Logs Insights queries
for traces, AWS X-Ray for distributed workflows, and AgentCore
Observability span analysis for token patterns.

### Implementation steps

1. **Baseline, then detect:**
   Collect 2 to 4 weeks of baseline data using
   [Amazon
   Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md"), then configure
   [Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md") on key cost indicators
   with 2σ warning and 3σ critical thresholds.
2. **Implement agent-specific
   detectors:** Deploy Lambda-based detectors for
   reasoning loop token spikes (5x session average), tool
   invocation storms (3x baseline rate), memory growth
   anomalies (2x per hour), and workflow cost escalation (2x
   historical average), publishing structured anomaly events to
   Amazon EventBridge.
3. **Add billing-level anomaly
   coverage:** Configure
   [AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/manage-ad.md "../../../cost-management/latest/userguide/manage-ad.md") monitors per agent cost
   allocation tag as a backstop for gradual escalations.
4. **Create investigation
   runbooks:** Store runbooks for each anomaly type in
   AWS Systems Manager OpsCenter, with diagnostic queries
   (Amazon CloudWatch Logs Insights for traces, AWS X-Ray for
   distributed workflows, AgentCore Observability span analysis
   for token patterns) and mitigation actions.
5. **Route anomalies through correlation
   analysis:** Classify anomalies using cost
   allocation tags and AgentCore Observability dimensions,
   routing agent-driven anomalies to development teams and
   infrastructure anomalies to operations teams.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
  Use the reflection pattern to design efficient agent reasoning
  loops](agentcost01-bp01.md "agentcost01-bp01.md")
- [AGENTCOST05-BP01
  Establish agent-level reasoning cost tracking and
  attribution](agentcost05-bp01.md "agentcost05-bp01.md")
- [AGENTCOST07-BP01
  Implement automated cost controls with intelligent
  cutoffs](agentcost07-bp01.md "agentcost07-bp01.md")
- [AGENTCOST07-BP03 Create
  systematic optimization feedback loops for continuous
  improvement](agentcost07-bp03.md "agentcost07-bp03.md")

**Related documents:**

- [Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md")
- [AWS Cost Anomaly Detection](../../../cost-management/latest/userguide/manage-ad.md "../../../cost-management/latest/userguide/manage-ad.md")
- [Amazon
  Bedrock AgentCore Observability](../../../bedrock-agentcore/latest/devguide/observability.md "../../../bedrock-agentcore/latest/devguide/observability.md")

**Related examples:**

- [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Observability
  tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Cost Management](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/")
- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")

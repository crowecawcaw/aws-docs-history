

# AGENTOPS05-BP04 Define and track KPIs for agent workflows
<a name="agentops05-bp04"></a>

 Infrastructure metrics like CPU, memory, and invocation count explain whether an agent is running. However, these metrics don't determine whether an agent is actually working. Key performance indicators (KPIs) tied to business outcomes give teams and stakeholders a shared language for discussing and improving agent performance. 

 **Desired outcome:** 
+  Every agent workflow has a defined set of KPIs tracked continually against established baselines. 
+  Teams identify performance degradation early and correlate KPI changes with configuration or model updates. 
+  Optimization efforts are prioritized based on measurable impact rather than intuition. 
+  Business stakeholders have regular visibility into how agent workflows contribute to business outcomes. 

 **Common anti-patterns:** 
+  Tracking only infrastructure metrics (like CPU, memory, and invocation count) without agent-specific KPIs that measure business outcomes like task completion rate and user satisfaction. 
+  Defining KPIs at deployment and never revisiting them as business objectives evolve, measuring metrics that no longer reflect what matters. 
+  Collecting KPI data without establishing baselines or alerting thresholds, producing dashboards that no one monitors proactively. 
+  Weighting operational and business metrics equally when one matters ten times more than the other, creating dashboards that feel balanced but mislead. 

 **Benefits of establishing this best practice:** 
+  KPIs provide the quantitative foundation for evidence-based decisions, so teams measure change impact and prioritize improvements based on data. 
+  Trend tracking reveals patterns of degradation or improvement that inform continuous refinement of prompts, configurations, and integrations. 
+  Business outcome metrics connect agent work to value delivered, giving stakeholders regular, concrete updates instead of vague reassurance. 
+  Anomaly-based alerting catches gradual degradation that static thresholds miss. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A usable KPI framework covers four dimensions rather than one. 
+  Operational KPIs, like task completion rate, resolution time, error rate, and escalation rate, measure whether the agent runs reliably. 
+  Quality KPIs, like decision accuracy, hallucination rate, and user satisfaction, measure whether its outputs are correct. [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) scores for correctness, helpfulness, safety, and tool selection accuracy, which provides automated quality signals. 
+  Efficiency KPIs, like tokens per task, tool invocations per task, and cost per task, measure whether the agent is economical. 
+  Business KPIs, like outcome achievement rate, SLA compliance, and customer satisfaction impact, measure whether the agent is worth the investment. 

 Skipping any dimension produces a dashboard that looks complete and can be misleading. 

 Baselines make KPIs useful by providing context for comparison. Establish baselines during an initial observation period (two to four weeks is usually enough), then configure [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Anomaly Detection so baselines adjust automatically as workflows mature. Set warning and critical alerting thresholds, where warnings initiate review and critical alerts dictate the need for action. 

 Weekly KPI reports through [Amazon Quick Suite](https://aws.amazon.com/quicksuite/) share the same dashboard with technical and business stakeholders. The same metrics serve both audiences so that everyone sees the same trajectory and conversations about investment and prioritization have shared data to ground them. Quarterly reviews verify that KPI definitions still reflect up-to-date business objectives and metrics. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a four-dimensional KPI framework:** Cover operational, quality, efficiency, and business dimensions for each agent workflow, with use-case-specific weighting. 

1.  **Collect KPIs through [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) custom metrics:** Add dimensions for agent, workflow, and environment so the same metric can be sliced multiple ways. 

1.  **Establish baselines and configure anomaly detection:** Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) Anomaly Detection with warning and critical alerting thresholds. 

1.  **Build weekly KPI dashboards:** Use [Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/user/welcome.html) reports shared with technical and business stakeholders. 

1.  **Review KPI alignment quarterly:** Verify that definitions still reflect current business objectives, and retire or replace metrics that no longer apply. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations](agentops05-bp01.html) 
+  [AGENTOPS05-BP05 Create workflow-specific dashboards for operational health](agentops05-bp05.html) 
+  [AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement](agentops02-bp04.html) 

 **Related documents:** 
+  [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) 
+  [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) 
+  [Guidance for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/) 
+  [From AI agent prototype to product: Lessons from building AWS DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon Quick](https://aws.amazon.com/quicksuite/) 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
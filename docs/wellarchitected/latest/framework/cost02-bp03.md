

# COST02-BP03 Monitor cost proactively

 Waiting for the monthly invoice means an inefficiency has already run for weeks before anyone sees it. Proactive monitoring reviews cost and usage on a regular cadence and surfaces changes as they happen. The goal is to make spend visible to the teams that create it, as well as the teams that pay for it. 

 **Desired outcome:** 
+  You review cost and usage on a defined cadence, not only when an alert or an invoice arrives. 
+  Your cost data is visible to the teams that create the spend, not just to finance. 
+  Your unusual spend is detected close to when it occurs. 
+  Your cost review is a standing practice with clear owners and follow-up actions. 
+  Your predictable overruns trigger an automated guardrail, not only an alert. 

 **Common anti-patterns:** 
+  Teams review costs only when the monthly statement arrives. 
+  Monitoring relies on default billing notifications alone. 
+  Cost management sits entirely with finance, with no engineering involvement. 
+  No regular cost review meeting exists. 
+  Granular tracking and visualization tools go unused, so spikes hide inside aggregate totals. 
+  Cost optimization is treated as a one-time project rather than a continuous practice. 

 **Benefits of establishing this best practice:** 
+  You catch unexpected spend within days instead of at month end. 
+  You give resource owners the visibility to act on their own cost. 
+  You reduce the risk of budget overruns. 
+  You build cost awareness into everyday engineering decisions. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Reactive cost management waits for a signal, usually the invoice or a threshold breach, and by then the spend is already committed. Proactive management inspects cost and usage on a schedule to find both problems and successes, so decisions rest on current data. 

 Granularity determines what you can see. A monthly total for an account hides a resource that doubled in cost overnight, because the spike averages out across weeks and services. Review spend by hour and by individual resource, grouped by tag, to find which resources drive cost and when. This depends on a consistent tagging strategy. 

 Use both budgets and anomaly detection. Budgets are threshold-based: you set an expected level of cost or usage, and an alert fires when actual or forecasted spend crosses it. Anomaly detection is statistical: it learns each segment's usual pattern and flags unexpected deviations, such as a misconfigured resource or an unplanned usage spike. Budgets catch the overruns you can predict, and anomaly detection catches the ones you cannot. 

 Thresholds set too low or subscriptions routed too widely produce noise, and teams learn to dismiss the alerts, including the ones that matter. Tune thresholds to a cost impact worth acting on. Route each alert to the team that owns the affected account or service. Choose a frequency that matches the audience: immediate alerts for engineers, summaries for management. 

 An alert still waits for a person to act. For the overruns you can define in advance, attach an automated response. [AWS Budgets actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) run when a budget threshold is crossed. They can apply a restrictive IAM policy or a service control policy (SCP), or stop targeted Amazon EC2 or Amazon RDS instances, automatically or after manual approval. Preventive controls belong earlier. Apply an SCP at the workload's account or organizational unit to deny expensive instance families or restrict Regions before the spend happens. Pair each budget with an action so detective and preventive controls work together. 

 Proactive monitoring is also an organizational practice. Cost owned by finance alone stays invisible to the engineers whose decisions create it. Dashboards shared where teams already work put spend in front of the people who can change it. That visibility also gives you a place to promote efficiency wins other teams can reuse. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a regular cost review cadence:** Set up a recurring cycle to review workload efficiency using the metrics you already track, reporting on the outcomes achieved and the cost of achieving them. Identify and correct negative trends, and highlight positive ones to repeat elsewhere. Include representatives from application teams, finance, and management so decisions have the right owners. 

1.  **Build dashboards for shared visibility:** Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to visualize and analyze cost over time, and build [AWS Quick](https://aws.amazon.com/quick/) dashboards for tailored views. The [Cloud Intelligence Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html) are a pre-built, customizable starting point. Place these dashboards where teams already work so cost stays visible. 

1.  **Create daily-granularity budgets with alerts:** Configure [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) at daily granularity and set your expected cost and usage as the limits, so anything above the limit reads as overspend. Route alert notifications to the stakeholders who can act before the period closes. 

1.  **Enable anomaly detection:** Turn on [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) and define monitors for the segments you care about, such as individual services, member accounts, cost allocation tags, and cost categories. Attach subscriptions with a cost impact threshold and an alert frequency for each audience, and route findings to the teams that own the affected resources. Use its root cause analysis to attribute each anomaly to the driver behind it, which shortens investigation. 

1.  **Attach automated guardrails for predictable overruns:** Configure [AWS Budgets actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) so a threshold breach triggers a response, such as applying a restrictive IAM policy or SCP, or stopping targeted resources, automatically or after approval. To block spend before it starts, apply a service control policy at the workload's account or organizational unit to deny expensive instance families or restrict Regions. 

1.  **Analyze granular cost and promote findings:** Drill into spend at hourly and resource level, using tags to find the highest-cost resources and confirm cost matches expectations. Feed what you learn back into the review cadence, correcting inefficiencies and sharing repeatable wins across the organization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 
+  [COST02-BP02 Allocate costs based on workload metrics and business outcomes](cost02-bp02.md) 
+  [COST01-BP01 Establish cloud budgets and forecasts](cost01-bp01.md) 

 **Related documents:** 
+  [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) 
+  [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) 
+  [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) 
+  [Configuring AWS Budgets actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) 

 **Related examples:** 
+  [Cloud Intelligence Dashboards on AWS](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html) 
+  [AWS Cost Anomaly Detection alerts with Slack](https://aws.amazon.com/aws-cost-management/resources/slack-integrations-for-aws-cost-anomaly-detection-using-aws-chatbot/) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs): Foundations and Governance](https://catalog.workshops.aws/awscff/) 

 **Related services:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) 
+  [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) 
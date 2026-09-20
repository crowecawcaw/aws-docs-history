

# DSOPS04-BP01 Maintain continuous visibility of your compliance status
<a name="dsops04-bp01"></a>

 Point-in-time audits and periodic assessments don't reflect the real state of compliance. A workload that meets regulatory requirements today may fall out of compliance the next day. Continuous visibility into compliance status across jurisdictions helps teams detect drift early, prioritize remediation by regulatory impact, and demonstrate ongoing adherence to auditors. 

 **Desired outcome:** 
+  Compliance status is visible in near real-time across jurisdictions. 
+  Teams receive alerts when resources drift from compliance baselines, with findings scored by severity and scoped by jurisdiction so that remediation is prioritized by regulatory impact. 

 **Common anti-patterns:** 
+  Compliance status is assessed only during audit periods rather than continuously. 
+  Findings from multiple sources are not correlated, making it difficult to identify the regulatory impact of a compliance drift. 
+  Compliance metrics are not tracked over time, so teams can't demonstrate improvement or identify recurring issues. 
+  Compliance visibility isn't scoped by jurisdiction, making it difficult for regional teams or auditors to assess a specific Region independently. 

 **Benefits of establishing this best practice:** 
+  Early detection of configuration drift and policy violations before they become audit findings. 
+  Reduced manual audit effort through continuous, automated compliance monitoring. 
+  Data-driven remediation prioritization based on severity scores and regulatory impact. 
+  Jurisdiction-level compliance visibility for regional teams and auditors. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 With continuous evidence collection in place, the operational challenge shifts from gathering data to making it usable. Compliance findings from multiple services, accounts, and jurisdictions need to be correlated, scored, and presented to the teams responsible for remediation. Without this operational layer, findings accumulate in disparate tools and teams lack the context to prioritize effectively. 

 Compliance findings carry different weight depending on the regulatory context in which they occur. Effective scoring accounts for both the technical severity of the finding and the regulatory impact of non-compliance in the jurisdiction where the affected resource operates. Static severity alone produces noisy prioritization that doesn't reflect actual risk. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Aggregate compliance findings across jurisdictions:** 
   +  Use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) with [cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) to consolidate compliance findings from multiple Regions into a single view. Be aware of data residency restrictions before enabling cross-Region aggregation. Make sure cross-Region aggregation is enabled only within approved jurisdictional boundaries. 
   +  Enable [consolidated controls view](https://docs.aws.amazon.com/securityhub/latest/userguide/asff-changes-consolidation.html) in Security Hub CSPM to reduce findings noise by producing a single finding per control, even if the control applies to multiple enabled standards. 
   +  For workloads that generate application-level compliance data, aggregate selected [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) logs from workload accounts into a centralized Log Archive account using CloudWatch Logs subscription filters and [Amazon Data Firehose](https://aws.amazon.com/firehose/) delivery streams. Where data residency requirements restrict cross-Region log transfers, use Region-specific Log Archive buckets. 

1.  **Score and prioritize findings:** 
   +  Security Hub CSPM uses a standardized scoring system to prioritize compliance findings based on severity and impact. Each finding receives a severity score from 0-100: informational (0), low (1-39), medium (40-69), high (70-89), and critical (90-100). The scoring considers the potential impact of the security issue, the exploitability of the vulnerability, and the confidence level of the detection mechanism. 
   +  Security Hub CSPM calculates a security score for each enabled standard, representing the percentage of passed security checks. Track this measure over time and compare across jurisdictions to quantify compliance posture. When reviewing findings, consider the regulatory context. A finding that an Amazon SQS queue isn't encrypted at rest may be informational for one workload but a critical compliance violation for another, depending on the data it processes and the regulatory frameworks that apply. 
   +  Use Security Hub CSPM [custom insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-insights.html) to create jurisdiction-specific views. For example, to track critical findings in a specific Region open for more than 30 days: 

     ```
     AWS securityhub create-insight --region <your-region> \
       --name "CriticalFindingsOver30Days" \
       --filters '{"SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}], "RecordState": [{"Value": "ACTIVE", "Comparison": "EQUALS"}], "WorkflowStatus": [{"Value": "NEW", "Comparison": "EQUALS"}], "CreatedAt": [{"DateRange": {"Value": 30, "Unit": "DAYS"}}]}' \
       --group-by-attribute "ResourceType"
     ```

1.  **Set up metrics, alarms, and notifications:** 
   +  [AWS Config](https://aws.amazon.com/config/) automatically publishes compliance metrics to CloudWatch, enabling you to create alarms based on the number of non-conforming resources, compliance percentage by rule, or configuration changes across your environment. 
   +  Security Hub CSPM findings are automatically sent to [Amazon EventBridge](https://aws.amazon.com/eventbridge/), where you can create rules to filter findings by severity, resource type, Region, or compliance standard. Route findings to [AWS Lambda](https://aws.amazon.com/lambda/) functions for custom processing, [Amazon SNS](https://aws.amazon.com/sns/) topics for notifications, or directly to EventBridge API destination partners such as [Slack](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destination-partners.html#eb-api-destination-slack). 
   +  Use [CloudWatch composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) to create alerting logic that combines multiple compliance metrics. For example, trigger an alarm when both the compliance drift rate and the critical finding backlog age exceed thresholds in a specific Region. 

    The following are some example metrics. These are not exhaustive and are shown for illustrative purposes. 


<table>
<thead>
  <tr><th> Name </th><th> Category </th><th> Measurement </th><th> Engineering value </th><th> Audit value </th></tr>
</thead>
<tbody>
  <tr><td> <b>Mean Time to Detection (MTTD)</b> </td><td> Operational efficiency </td><td> Average time from when a compliance violation occurs to when it is detected </td><td> Optimize monitoring coverage and alert tuning </td><td> Shows proactive monitoring effectiveness </td></tr>
  <tr><td> <b>Mean Time to Identification (MTTI)</b> </td><td> Operational efficiency </td><td> Average time from detection to identification of the root cause </td><td> Plug gaps in compliance data collection </td><td> Evidence of timely identification </td></tr>
  <tr><td> <b>Mean Time to Remediation (MTTR)</b> </td><td> Operational efficiency </td><td> Average time from detection to full remediation. Includes MTTI. </td><td> Identifies bottlenecks in remediation workflows </td><td> Evidence of timely corrective action </td></tr>
  <tr><td> <b>Critical finding backlog age</b> </td><td> Risk and impact </td><td> How long high and critical severity findings remain unresolved </td><td> Prioritizes technical debt and resource allocation </td><td> Shows that high-risk issues are addressed promptly </td></tr>
  <tr><td> <b>Compliance drift rate</b> </td><td> Risk and impact </td><td> Percentage of resources that drift from compliance over time </td><td> Indicates configuration management effectiveness </td><td> Demonstrates ongoing continuous compliance efforts </td></tr>
  <tr><td> <b>Repeat violation rate</b> </td><td> Risk and impact </td><td> Percentage of compliance issues that recur after remediation </td><td> Identifies need for better root cause analysis </td><td> Shows effectiveness of remediation scripts </td></tr>
</tbody>
</table>


## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS03-BP02 Automate evidence collection and reporting](dsops03-bp02.html) 
+  [DSOPS05-BP01 Enable independent root cause analysis and remediation](dsops05-bp01.html) 
+  [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) 
+  [SEC04-BP02 Capture logs, findings, and metrics in standardized locations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html) 
+  [SEC04-BP03 Correlate and enrich security alerts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html) 

 **Related documents:** 
+  [Analyzing AWS CloudTrail in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/) 
+  [Metrics for automated compliance and guardrails](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-automated-compliance-and-guardrails.html) 
+  [Visualize AWS Security Hub CSPM Findings using Analytics and Business Intelligence Tools](https://aws.amazon.com/blogs/architecture/visualize-aws-security-hub-findings-using-analytics-and-business-intelligence-tools/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Best practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE) 

 **Related examples:** 
+  [Cloud Intelligence Dashboards - AWS Config Resource Compliance Dashboard](https://github.com/aws-samples/config-resource-compliance-dashboard) 
+  [Security Hub CSPM Compliance Analyzer](https://github.com/awslabs/security-hub-compliance-analyzer) 

 **Related services:** 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 
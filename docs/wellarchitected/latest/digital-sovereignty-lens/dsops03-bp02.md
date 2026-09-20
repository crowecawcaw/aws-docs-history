

# DSOPS03-BP02 Automate evidence collection and reporting
<a name="dsops03-bp02"></a>

 Manual evidence collection is time-consuming, error-prone, and doesn't scale across jurisdictions. Automating evidence collection and reporting improves accuracy, reduces audit preparation effort, and provides continuous visibility into compliance status. 

 **Desired outcome:** 
+  Evidence is collected continuously and stored in Regions that meet data residency requirements. 
+  Compliance reports can be generated on demand, scoped by jurisdiction, so that auditors can assess each Region independently. 

 **Common anti-patterns:** 
+  Relying solely on manual screenshots and documentation for audit evidence. 
+  Collecting evidence only during audit periods rather than continuously. 
+  Storing evidence in formats that are not readily searchable or retrievable. 
+  Storing evidence in a single Region without considering data residency requirements for audit data. 

 **Benefits of establishing this best practice:** 
+  Reduces audit preparation time from weeks to hours or days. 
+  Provides real-time visibility into compliance status and security posture. 
+  Reduces human error and maintains consistent quality of documentation. 
+  Enables proactive identification and remediation of compliance gaps. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automated evidence collection helps organizations maintain audit-ready documentation continuously rather than assembling it reactively when an audit is announced. In multi-jurisdictional environments, the volume of evidence required grows with each regulatory authority, each jurisdiction, and each compliance framework. Automation scales this collection without proportional growth in manual effort, capturing compliance findings, configuration states, access logs, and policy evaluations as they occur. 

 Consider applying a structured approach towards automating evidence collection. For example, you can divide evidence automation into four incremental stages that build toward audit-ready outputs: sourcing, analysis, visualization, and evidence packaging. **Sourcing** establishes the raw data feeds (logs from operational activity and findings from compliance evaluation services). **Analysis** applies intelligence to that raw data, identifying patterns, correlating events, and generating insights that would be impractical to derive manually. **Visualization** makes compliance status accessible to different audiences (operations teams monitoring drift, leadership reviewing posture, auditors assessing specific controls). **Evidence** packages the outputs into audit-ready artifacts with the provenance, immutability, and jurisdiction-scoping that auditors require. Each stage builds on the previous one, and gaps at any stage limit the value of subsequent stages. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Source**: Begin by identifying sources. There are two types of sources: 
   +  **Logs**: AWS CloudTrail records actions taken by a user, role, or an AWS service as events. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs. If you have already set up a landing zone with a structure similar to the one suggested in the AWS Security Reference Architecture (AWS SRA), you will have a Security OU with a [Log Archive Account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html). 

      Using AWS CloudTrail, create an organization trail that logs all events for all AWS accounts in your organization to an Amazon S3 bucket in the Log Archive account. All trails created using the CloudTrail console are multi-Region trails. CloudTrail delivers log files for account activity from all enabled AWS Regions to the single Amazon S3 bucket that you specify, and, optionally, to a CloudWatch Logs log group. 

      Carefully consider your log aggregation set up when you also need to cater to strict data localization mandates (that include audit log of user actions). Use AWS Organizations to [enable only those AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#manage-acct-regions-enable-organization) that fall within the same jurisdictional boundary. For example ap-south-1 and ap-south-2. 

      Other log sources that assist with audit of user actions include: [Amazon Virtual Private Cloud (Amazon VPC) Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [AWS WAF logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html), [Amazon Route 53 resolver query logs](https://docs.aws.amazon.com/Route 53/latest/DeveloperGuide/resolver-query-logs.html), and [Amazon Elastic Kubernetes Service (Amazon EKS) Audit Logs](https://docs.aws.amazon.com/eks/latest/best-practices/auditing-and-logging.html). 

      [Amazon Security Lake](https://aws.amazon.com/security-lake/) can collect logs and events from several supported AWS services. Security Lake automatically converts logs and events sourced from supported AWS services to the open source Open Cybersecurity Schema Framework [(OCSF)](https://github.com/ocsf) schema. 
   +  **Findings**: [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), [Amazon Macie](https://aws.amazon.com/macie/), and [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) can automatically detect and generate findings. These findings are derived from compliance drifts, threats, vulnerabilities, and over-permissive configurations. Consider enabling [built-in security standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html), with AWS Security Hub CSPM to automatically collect and correlate findings related to well-known security standards (for example, NIST 800-53 Rev. 5). 

1.  **Analyze**: You can use AWS services and third-party security information and event management (SIEM) tools to run analytical queries and discover new insights from logs. You can also use AWS services and third-party providers (known as finding providers) to conduct advanced analytics. 
   +  **Run custom analytics**: Amazon Security Lake offers [several integrations](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-integrations.html) with downstream analytics tools including: 
     +  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) can generate AI-powered insights from Security Lake data. 
     +  [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html) can investigate and identify the root cause of security findings or suspicious activities. 
     +  [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) and [Amazon OpenSearch Service ingestion pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html) can generate security insights from Security Lake data by using OpenSearch Service ingestion. 
     +  Since Security Lake normalizes logs into the OCSF format, you can forward data to several [popular SIEM and analytics tools](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) without having to build transformations. 
   +  **Use built-in intelligence**: Find providers like [AWS services](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html) and [third parties](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html) that use built-in intelligence to generate and send new findings to Security Hub CSPM. For AWS Security Hub CSPM, a finding is an observable record of a security check or a security-related detection. The provider analyzes your data and delivers findings, reducing the need for custom query development. 

      For example, Amazon GuardDuty analyzes AWS logs and network traffic to detect threats and malicious activity in your AWS environment. It uses machine learning, anomaly detection, and integrated threat intelligence to identify unexpected and unauthorized activities like cryptocurrency mining, credential harvesting, and potentially compromised instances. 

      Security Hub CSPM ingests and groups related findings to generate [insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html). 

1.  **Visualize:** Use built-in dashboards or build your own visualizations and make them available through self-service portals. Allow auditors access to self-service portals so that they can collect the evidence they need without having to rely on your teams. 
   +  **Use built-in dashboards**: AWS Config, Amazon GuardDuty, and Amazon Inspector provide built-in summary dashboards over findings. When you consolidate your findings to Security Hub CSPM, it can contextualize those findings, map them to known security standards, and present overall security scores. Security Hub CSPM also supports creating [own insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-insights.html) and building visualizations over those insights. 
   +  **Build your own visualizations**: Explore and interpret logs in Security Lake by combining with a query tool like [Amazon Athena](https://aws.amazon.com/athena/). Build visualizations and dashboards using business intelligence and reporting tools like [Quick](https://aws.amazon.com/quicksight/). With [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-security-lake.html), you can create a subscription that replicates data from Security Lake to your ingestion pipeline and build visualizations on top. 

1.  **Evidence:** A traditional audit process follows a pattern like the one below and can take multiple weeks. With an automated solution you can potentially reduce this effort. The timelines shown here are for illustration purposes. These timelines will vary with the complexity of your workloads and the compliance requirements they are subject to. 


<table>
<thead>
  <tr><th> Stages </th><th> Without automation </th><th> With automation </th><th> Automation capabilities </th></tr>
</thead>
<tbody>
  <tr><td> Planning </td><td> 1-2 weeks </td><td> &lt;1 week </td><td> Pre-built mapping frameworks. Lists cloud provider technical controls mapping to known security standards. </td></tr>
  <tr><td> Evidence requests </td><td> 2-3 weeks </td><td> Immediate. No delays. </td><td> Pre-provisioned auditor roles. Auditors have real-time access to compliance dashboards. </td></tr>
  <tr><td> Evidence review </td><td> 3-4 weeks </td><td> 1-2 weeks </td><td> Pre-organized and categorized by security standards. </td></tr>
  <tr><td> Report writing </td><td> 2-3 weeks </td><td> 1-2 weeks </td><td> Automated report generation. </td></tr>
  <tr><td> <b>Total</b> </td><td> <b>8-12 weeks</b> </td><td> <b>3-5 weeks</b> </td><td> – </td></tr>
</tbody>
</table>


    Use [AWS Config conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) to map detective controls to compliance frameworks. Conformance packs provide [pre-built templates](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html) for frameworks such as NIST SP 800-53 Rev 5, PCI DSS v4.0, and HIPAA. AWS Config is [extensible](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html), allowing you to develop custom rules that evaluate sovereignty-specific requirements. Use [AWS Config Advanced Query](https://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html) to export compliance evaluation results and resource configurations as audit evidence. For long-term evidence retention, enable [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) to centralize Security Hub CSPM findings, CloudTrail events, and other security data in OCSF format on Amazon S3. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS03-BP01 Plan and prepare for audits](dsops03-bp01.html) 
+  [SEC04-BP01 Configure service and application logging](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html) 
+  [SEC04-BP02 Analyze logs, findings, and metrics centrally](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html) 
+  [OPS08-BP02 Analyze workload logs](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.html) 

 **Related documents:** 
+  [Automate evidence gathering for compliance audit reports](https://maturitymodel.security.aws.dev/en/4.-optimized/automate-evidence-gathering/) 
+  [How to visualize Amazon Security Lake findings with Quick](https://aws.amazon.com/blogs/security/how-to-visualize-amazon-security-lake-findings-with-amazon-quicksight/) 
+  [Introducing Amazon OpenSearch Service and Amazon Security Lake integration to simplify security analytics](https://aws.amazon.com/blogs/aws/introducing-amazon-opensearch-service-zero-etl-integration-for-amazon-security-lake/) 

 **Related videos:** 
+  [Visualizing Security Lake Data with Quick: 2024 Quick Learning Series](https://www.youtube.com/watch?v=vxvMHnfCCGw) 
+  [Remediating Amazon GuardDuty and AWS Security Hub CSPM Findings](https://youtu.be/nyh4imv8zuk) 
+  [AWS re:Invent 2025 - Observability & Security unite: Unify your data in Amazon CloudWatch (COP361)](https://www.youtube.com/watch?v=5-_l3MYJdLs) 
+  [AWS re:Invent 2025 - Building agentic workflows for augmented observability (COP405)](https://www.youtube.com/watch?v=fLDjHr6eEIw) 

 **Related examples:** 
+  [Workshop: AWS Cloud – An Auditors Lens](https://catalog.us-east-1.prod.workshops.aws/workshops/be5ac274-af86-47ef-b3ae-efae7fad136c/en-US) 
+  [Workshop: AWS Config Resource Compliance Dashboard - Part of Cloud Intelligence Dashboards Framework](https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard/) 

 **Related services:** 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [Amazon Macie](https://aws.amazon.com/macie/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
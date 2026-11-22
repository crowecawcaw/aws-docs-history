

# FND03-BP02 Establish central, cross-account observability capabilities

 Central, cross-account observability brings telemetry from every account in your environment into a shared location. Foundation, workload, and security teams can read it without signing into each account. This best practice covers the architecture, automation, and access model needed to architect a single, consistent view of operations across a multi-account environment. 

 **Desired outcome:** 
+  Your foundation provides central observability across all accounts. Foundation, workload, and security teams can access telemetry without direct access to individual workload accounts. 
+  New accounts and workloads inherit observability automatically. Telemetry collection, sharing, and baseline monitoring are set up without manual steps. 
+  Automated onboarding and enforcement produce consistent cross-account coverage with low operational overhead for workload teams. 

 **Common anti-patterns:** 
+  Relying on telemetry collected inside each account on its own, which leads to fragmented or siloed visibility. 
+  Working without cross-account correlation, which forces responders to stitch together incident timelines from disconnected accounts. 
+  Building central dashboards on top of incomplete or inconsistent cross-account data sharing, which produces partial metrics. 
+  Onboarding new accounts into observability tools by hand, or skipping onboarding entirely. 
+  Failing to monitor the observability infrastructure itself, which creates blind spots when central monitoring components fail. 

 **Benefits of establishing this best practice:** 
+  Foundation and workload telemetry is visible across accounts without switching between them. 
+  Incident response and operational reporting cover the whole environment rather than one account at a time. 
+  New accounts join observability tooling automatically rather than through manual setup. 
+  Telemetry gaps are found and closed across accounts and workloads. 
+  Aggregating telemetry in a controlled environment supports audit and regulatory needs. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Without central observability, organizations face fragmented visibility. Each account produces its own telemetry, but there is no complete visualization of activity across the environment. This fragmentation slows incident response, makes it hard to correlate events across workloads, and forces security teams to request access to individual accounts to investigate issues. As organizations grow, each new account adds more operational load, and manual coordination becomes unsustainable. 

 Designate observability accounts that aggregate telemetry from all source accounts through automated cross-account sharing. This separates telemetry production (workload accounts) from telemetry consumption (observability accounts). Apply role-based access controls at the observability layer so teams get telemetry without workload account access. Foundation, security, and workload teams draw from the same aggregated source, giving everyone a consistent view during incidents and operational reviews. [Amazon CloudWatch Observability Access Manager (OAM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) provides the sharing mechanism for metrics, logs, traces, and alarms without resource-based policies on every log group or metric namespace. 

 Automate cross-account linking through your account provisioning pipelines so new accounts inherit observability without manual steps. Telemetry must follow consistent naming conventions, metric namespaces, and tagging strategies across all accounts. Without this, aggregated data becomes hard to query, filter, and correlate during investigations. For workloads instrumented with OpenTelemetry, CloudWatch [native OpenTelemetry support](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html) sends metrics using OTLP, combines them with AWS vended metrics, and queries them with PromQL. 

 Protect the observability accounts with least-privilege IAM roles and service control policies that limit who accesses aggregated telemetry and which accounts can link to the monitoring infrastructure. Consider keeping production and non-production observability data separate when security or compliance calls for isolation. Clear ownership of central dashboards and alerts keeps them from going stale. Establish naming and tagging conventions when accounts are created, because adding them later across many accounts requires significant rework. Ingestion, storage, and query charges scale with telemetry volume, so set retention, [log group retention settings](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention), and sampling strategies early to control spend at scale. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a central monitoring account:** Designate one or more accounts as central observability accounts, following [AWS multi-account strategy best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html). Consider separate accounts for production and non-production observability data if isolation is required. Enable [Amazon CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) to aggregate metrics, logs, traces, and alarms from source accounts, and set up [IAM roles and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for the monitoring account to access cross-account telemetry. For large environments, roll out in phases. Start with non-production accounts or a pilot organizational unit before expanding to production workloads so you can validate configuration, cost, and operational procedures before full-scale deployment. 

1.  **Link source accounts to the central monitoring account:** Configure source accounts by using [CloudWatch Observability Access Manager (OAM)](https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html) to securely share observability data. Create [sharing configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html) that define which telemetry types (metrics, logs, and traces) are shared with the monitoring account. Automate the linking process by using infrastructure as code templates ([CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)) and integrate with [CI/CD pipelines](https://aws.amazon.com/what-is/ci-cd-pipeline/) to onboard new accounts consistently without manual steps. 

1.  **Standardize telemetry sharing across accounts:** Verify that all source accounts emit the required logs, metrics, and traces to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). For workloads instrumented with OpenTelemetry, use CloudWatch [native OpenTelemetry (OTel) support](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html) to send metrics directly using OTLP without custom conversion logic. Apply consistent [metric namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace), [log group naming conventions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html), and [resource tagging strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) aligned with your observability standards to support cross-account correlation during investigations. Establish workload readiness reviews that check telemetry configuration before production deployment. 

1.  **Implement central dashboards and alerts:** Build [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the monitoring account that bring telemetry together across source accounts, giving unified views to foundation, workload, and security teams. Create [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) that watch cross-account metrics and produce practical alerts. Route notifications by using [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) to deliver alerts to incident management systems, and use [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) when you want alerts and interactive operations to land directly in team chat channels. 

1.  **Secure cross-account observability access:** Use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) to define least-privilege roles for access to cross-account observability data. Apply [AWS Organizations service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to restrict which accounts can link to monitoring accounts and control who can reach aggregated telemetry. Follow [AWS security best practices for cross-account access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html), including external IDs and session policies where appropriate. 

1.  **Automate cross-account observability onboarding:** Make observability account linking a standard part of your account creation pipelines and landing zone automation (such as [AWS Control Tower customizations](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-overview.html) or [Account Factory for Terraform](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html)). Automatically configure new accounts to link to the central monitoring account by using OAM through infrastructure as code. Add validation checks to your account provisioning process to confirm successful observability integration before marking accounts ready for workload deployment. 

1.  **Monitor the observability infrastructure itself:** Add monitoring to the central observability account so failures in cross-account collection, OAM links, or dashboard availability do not go unnoticed. Create [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) that watch for CloudWatch API throttling, OAM link failures, and unexpected drops in metric or log volume from source accounts. Use the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) to receive notifications about service events affecting CloudWatch in your monitoring account. Build runbooks for responding to observability infrastructure degradation so you do not lose visibility during a critical incident. 

1.  **Integrate with foundation operations:** Use central observability dashboards as the primary tools during incident response, operational reviews, and capacity planning. Provide role-based access to relevant dashboards and alerts for workload, foundation, and security teams without direct access to individual workload accounts. Build [runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) that reference central dashboards and metrics for common troubleshooting scenarios. Produce operational reports by using aggregated cross-account data to spot trends, measure service level objectives, and guide infrastructure improvement decisions. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND03-BP01 Define observability standards and policies](fnd03-bp01.md) 
+  [FND03-BP03 Establish centralized event monitoring and response](fnd03-bp03.md) 
+  [FND04-BP05 Establish service quota management](fnd04-bp05.md) 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 

 **Related documents:** 
+  [Amazon CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) 
+  [CloudWatch Observability Access Manager API Reference](https://docs.aws.amazon.com/OAM/latest/APIReference/Welcome.html) 
+  [Amazon CloudWatch native OpenTelemetry support](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html) 
+  [CloudWatch observability solutions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Monitoring-Solutions.html) 
+  [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html) 
+  [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) 
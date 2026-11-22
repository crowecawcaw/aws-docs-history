

# FND05-BP04 Configure standardized locations for logs, traces, and metrics

 Security teams use logs and findings to analyze events that might indicate unauthorized activity or unintentional changes. Operations teams use logs, distributed traces, and metrics to understand system behavior and detect and mitigate issues early. Capture logs, traces, and metrics in standardized locations to correlate data points across all three signal types and simplify tool integrations. 

 **Desired outcome:** 
+  You have a standardized approach to collect, analyze, and visualize log data, distributed traces, metrics, and security findings across workload accounts. 
+  Security and operations teams can efficiently correlate, analyze, and visualize security data across disparate systems to discover potential issues and identify anomalies. 
+  Security information and event management (SIEM) systems or other mechanisms are integrated to query and analyze log data for timely responses, tracking, and escalation of security events. 

 **Common anti-patterns:** 
+  Teams independently own, manage, and collect logs and metrics in a way that is inconsistent with the organization's logging strategy. 
+  Teams lack adequate access controls to restrict visibility and alteration of the data collected. 
+  Teams don't govern their security logs, findings, and metrics as part of their data classification policy. 
+  Teams neglect data sovereignty and localization requirements when configuring data collections. 

 **Benefits of establishing this best practice:** 
+  Standardized collection and querying of log data improves the quality and speed of insights derived from analysis. 
+  Automated lifecycle management for log data reduces storage costs and maintains compliance with retention requirements. 
+  Fine-grained access controls protect sensitive log information and confirm that teams have appropriate access based on their operational needs. 
+  Centralized logging supports integration with security and analytics tools to correlate events, visualize trends, and accelerate incident response. 
+  Unified observability across logs, traces, and metrics supports faster root cause analysis by correlating multiple data types in a single location. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Collecting activity data from distributed workloads for centralized analysis is challenging. Security teams use SIEM systems to collect data from these sources and perform correlation, analysis, and response workflows, but managing permissions for disparate data sources and operating ETL processes introduces overhead. 

 Aggregate all relevant sources of security log data into a dedicated [Log Archive](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) account, as described in [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/). Include workload security data and AWS service logs ([AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [AWS WAF](https://aws.amazon.com/waf/), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), and [Amazon Route 53](https://aws.amazon.com/route53/)). Capturing data in a separate account with cross-account permissions helps prevent log tampering by users with broad access in the workload account, provides a single integration point for additional tools, and simplifies data retention and lifecycle management. Evaluate data sovereignty, compliance scope, and other regulations to determine whether multiple storage locations and retention periods are required. 

 [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) is the standardized analytics-ready location for your security logs and findings. It consolidates operational, security, and compliance data in one place across multiple AWS accounts and Regions, supports [Open Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf) and OpenTelemetry formats, and is accessible from [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), [Amazon Athena](https://aws.amazon.com/athena/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), and third-party Iceberg-compatible tools without data duplication. Use [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to copy log data from your organization into a central account and Region, and aggregate common security sources such as CloudTrail, Route 53 Resolver query logs, [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), compute and workload logs from [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html), [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html), and findings from AWS Security Hub CSPM, [Amazon GuardDuty](https://aws.amazon.com/guardduty/), and [Amazon Inspector](https://aws.amazon.com/inspector/) into the same store. Pair the unified data store with [Amazon S3](https://aws.amazon.com/s3/) for long-term retention of raw logs and low-cost archival. 

 Deploy security analytics tools that operate in AWS into a [Security Tooling](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/) account separate from your Log Archive account. This separation implements defense in depth, protecting the integrity and availability of logs and log management independently from the tools that access them. Services like [Amazon Athena](https://aws.amazon.com/athena/) run on-demand queries across multiple data sources, [AWS Quick](https://aws.amazon.com/quick/) provides visualization, and AI-powered solutions can translate findings into human-readable summaries and support natural language interaction. 

 Apply the same centralization and standardization principles to distributed traces and metrics. [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) and [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) capture end-to-end request flows across distributed systems, so you can understand request dependencies and pinpoint latency or error sources across microservices. Correlate traces with the CloudTrail and application logs in your Log Archive account so investigators can move from a suspicious event to the exact user requests that triggered it. 

 Metrics provide counts, rates, and durations that make anomalies measurable. [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is the central metrics repository for AWS services and custom application metrics, and [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) aggregates metrics, logs, and traces from workload accounts into a monitoring account for unified dashboards and alarms. For long-term retention and downstream analytics, use [CloudWatch metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) to deliver metrics into Amazon S3 alongside your other observability data, so you can query and correlate logs, traces, and metrics together. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create the Log Archive and Security Tooling accounts:** Using [AWS Organizations](https://aws.amazon.com/organizations/), [create the Log Archive and Security Tooling accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) under a security organizational unit. If using [AWS Control Tower](https://aws.amazon.com/controltower/), these accounts are created automatically. See [AWS Control Tower account factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html). Follow [AWS SRA Logging Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) guidance. 

1.  **Evaluate data sovereignty and compliance requirements:** Determine whether your organization requires multiple log storage locations based on [data residency laws](https://aws.amazon.com/what-is/data-sovereignty/), regulatory scopes, or data classification policies. Workloads spanning multiple geographic regions with strict data localization requirements might need per-Region Log Archive accounts or Region-specific storage locations in a single account. Document retention requirements for different log types and sensitivity levels so they inform your storage and lifecycle configuration in later steps. 

1.  **Configure your standardized security data locations:** Use [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) as the destination for operational, security, and compliance telemetry, and [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to aggregate log data across your organization. Capture security data from AWS Regions that are [opted-in](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) for your accounts, even when not actively in use. Pair the unified data store with raw log storage in [Amazon S3](https://aws.amazon.com/s3/) for long-term retention and integration with third-party data products where required. 

1.  **Configure data retention requirements:** Establish appropriate lifecycles for each log source using [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) and [Log retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention). Typically, three to twelve months of logs are readily available, with retention up to seven years. Align these settings with your security requirements and regulatory mandates. 

1.  **Configure data source publication to your standardized locations:** Identify sources and configure them to publish to your standardized locations. Evaluate options that automatically export data in the desired format rather than requiring ETL. Use [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to replicate log groups from member accounts into your CloudWatch Unified Data Store, and [CloudWatch metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) to deliver metrics into the same data store. Include compute and workload logs from [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html), [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html) so investigators can correlate API activity with what happened inside the workloads. Configure findings from AWS Security Hub CSPM, GuardDuty, and Amazon Inspector to flow into CloudWatch alongside raw logs, and publish third-party sources via their OCSF- or OpenTelemetry-compatible exporters. 

1.  **Configure tools to access your standardized locations:** Configure tools like [Amazon Athena](https://aws.amazon.com/athena/), [AWS Quick](https://aws.amazon.com/quick/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), or third-party solutions with required access. Operate these tools out of the Security Tooling account with cross-account read access to the Log Archive account. Analysts can query the same OCSF- and OpenTelemetry-formatted data in the CloudWatch Unified Data Store from [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html), Athena, OpenSearch Service, and third-party Iceberg-compatible platforms without duplicating data. 

1.  **Centralize traces and metrics alongside logs:** Turn on [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) for application tracing, or deploy the [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) Collector for standardized telemetry that works across AWS and third-party backends. Configure [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html) so metrics, logs, and traces from workload accounts are visible in a central monitoring account. Use [CloudWatch metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) to deliver metrics into Amazon S3 for long-term retention and correlation with logs. 

1.  **Use logs for alerting:** Configure alerting using [Amazon GuardDuty](https://aws.amazon.com/guardduty/), [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/), and [AWS Config](https://aws.amazon.com/config/). Enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) alongside Security Hub CSPM. AWS [recommends enabling both services](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html) so Security Hub CSPM findings are routed to Security Hub CSPM automatically and correlated with findings from Amazon Inspector, Amazon Macie, and GuardDuty to generate exposure findings. Use custom alert generation engines for specific alerts relevant to your environment, and [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for custom event-driven alerting. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 
+  [FND05-BP07 Implement threat detection mechanisms](fnd05-bp07.md) 
+  [FND05-BP11 Establish encryption and key management standards](fnd05-bp11.md) 
+  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md) 

 **Related documents:** 
+  [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) 
+  [Logging and monitoring guide for application owners](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/introduction.html) 
+  [AWS SRA Logging Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) 
+  [AWS SRA Security Tooling Account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) 
+  [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) 
+  [Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) 
+  [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) 

 **Related examples:** 
+  [Aggregating, searching, and visualizing log data from distributed sources with Amazon Athena and Quick](https://aws.amazon.com/blogs/security/aggregating-searching-and-visualizing-log-data-from-distributed-sources-with-amazon-athena-and-amazon-quicksight/) 
+  [Simplifying Log Management using Amazon CloudWatch Logs Centralization](https://aws.amazon.com/blogs/mt/simplifying-log-management-using-amazon-cloudwatch-logs-centralization/) 

 **Related tools:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon CloudWatch Unified Data Store](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) 
+  [Open Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf) 
+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/) 

 **Related services:** 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 
+  [AWS Quick](https://aws.amazon.com/quick/) 
+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
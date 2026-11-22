

# SEC04-BP01 Configure service and application logging

 Capture access logs, network flow records, and configuration change events from every component in your workload. This evidence helps you detect threats and reconstruct incidents. 

 **Desired outcome:** 
+  Your workload emits logs from every component that supports them, across the infrastructure and application layers. 
+  You collect security-relevant events such as access, permission changes, network flows, and configuration changes in a consistent, queryable format. 
+  Your logs are centralized, retained according to defined policies, and protected by access controls that prevent unauthorized reading or modification. 
+  You mask or remove sensitive data before it reaches log storage. 
+  You can query and correlate logs quickly enough to support active incident response. 

 **Common anti-patterns:** 
+  Teams enable logging on some components but leave others silent, which creates blind spots during investigations. 
+  Logs are stored in fragmented formats and locations, which makes correlation across components slow or impossible. 
+  Organizations set no retention policy, so investigators lose historical data or storage costs grow without bound. 
+  Log stores lack access controls, so unauthorized parties can read or tamper with security evidence. 
+  Sensitive data such as credentials or personal information lands in logs unmasked. 

 **Benefits of establishing this best practice:** 
+  Detection and investigation are faster, because relevant events are captured and searchable in one place. 
+  Incident response is stronger, because responders can reconstruct a timeline from consistent logs. 
+  Risk of data exposure drops, because sensitive values are removed before storage. 
+  Compliance is more straightforward to demonstrate, because retention and access controls meet audit requirements. 
+  Evidence stays reliable, because access controls protect logs from tampering. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Workloads produce security-relevant signals in multiple places. For example, the control plane records API calls, the network layer records traffic flows, and the application layer records authentication and authorization events. Each layer answers a different investigative question, so unlogged layers create gaps at investigation time. Identify the components that matter for your threat model, and confirm each one produces logs. 

 Treat log stores as high-value assets. Unauthorized read access reveals how you monitor, while write or delete access lets an attacker erase evidence. Restrict read and write access to the smallest set of systems and people. Store logs in accounts separate from the ones that generate them, so an affected workload cannot destroy its own audit trail. Centralize logs into a single destination, which is easier to lock down and search than many scattered ones. 

 Attackers can also disable logging entirely. Someone with the right permissions can [stop a trail](https://aws-samples.github.io/threat-technique-catalog-for-aws/Techniques/T1562.008.html) or [delete a GuardDuty detector](https://aws-samples.github.io/threat-technique-catalog-for-aws/Techniques/T1562.A001.html). Treat a change to your logging or detection configuration as a security event. Set detection at the organization level with [GuardDuty organization management](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html). Enable [log file integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) on your trail. Alert on the API calls that disable any of these methods. 

 Applications often write request bodies, headers, or error payloads that contain credentials, tokens, or personal information. Once that data lands in a log store, it inherits the exposure of everyone who can read the store. Identify the sensitive fields your components emit and mask or drop them before they reach log storage. Scrubbing logs after the fact is unreliable. 

 Keep logs long enough to satisfy investigations and compliance obligations, but not so long that storage cost outweighs their value. Different log types justify different retention periods, and some regulations require a minimum. Set retention deliberately for each log type. 

 [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) records API activity, [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html) records resource configuration changes, and [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) record network traffic. Amazon CloudWatch consolidates operational, security, and compliance logs from across accounts and Regions with [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html). Its transformation pipelines can [normalize security data to OCSF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-parseToOCSF.html). For analysis, [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries data in log groups and the unified store; [Amazon Athena](https://aws.amazon.com/athena/) and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) query data in Amazon S3. To link events across sources, [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) correlates and enriches findings from GuardDuty, Inspector, and Security Hub CSPM into prioritized exposure findings with attack path context. A third-party SIEM can serve the same role. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable foundational logging:** Turn on the account-wide sources that apply to almost every workload. CloudTrail's event history holds only 90 days of management events, so create an [organization trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) that covers every account and Region and delivers a durable record for investigations and audit. Enable [AWS Config](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html) for configuration changes and [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) for network traffic. 

1.  **Enable service-specific logging:** For each AWS service in your workload, configure its native logs. Common sources include [Amazon GuardDuty finding export](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html), [AWS WAF web ACL traffic logging](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html), [AWS Network Firewall logging](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html), [Elastic Load Balancing access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html), [Amazon Route 53 Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html), [Amazon RDS logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html), [Amazon EKS control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html), and the [Amazon CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) for Amazon EC2 instances and on-premises servers. 

1.  **Instrument custom applications:** Add logging to your own application code to capture security-relevant events such as user access, permission changes, and modifications to key components. Emit these events in a consistent, structured format so they can be parsed and correlated with infrastructure logs. 

1.  **Mask sensitive data before ingestion:** Identify the fields your components emit that contain credentials, tokens, or personal information. Remove or mask those fields before events are written, and apply [CloudWatch Logs data protection policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) to detect and mask sensitive data that still reaches log groups. 

1.  **Centralize logs:** Aggregate logs from all workload components into a central destination. Use [cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to replicate logs into a single account, and [telemetry enablement rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/telemetry-enablement-rules.html) to turn logging on automatically as resources appear. Normalize security data to OCSF in the same pipeline so formats match across sources. Centralization gives you unified visibility and a single boundary to secure. 

1.  **Restrict access to logs:** Apply access controls so that only authorized systems and individuals can read or modify logs. Keep log storage separate from the accounts that generate the logs to protect the audit trail from a workload under unauthorized control. 

1.  **Set retention policies:** Define retention per log type based on security, audit, and compliance needs, balanced against storage cost. Confirm each retention setting meets any regulatory floor that applies to that data. 

1.  **Enable querying and correlation:** Select query mechanisms that fit where your logs live. Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) for CloudWatch log groups and the unified data store, and [Amazon Athena](https://aws.amazon.com/athena/) or [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) for data in Amazon S3. For cross-source investigation, [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) correlates findings from multiple AWS security services and presents them with exposure context and attack path visualization, or use a SIEM for the same purpose. 

1.  **Monitor and alert on anomalies:** Review logs for patterns that indicate security threats or unauthorized activity, and route findings to the teams that own the affected components. Establish this monitoring as an ongoing process rather than a one-time setup. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC04-BP02 Prepare metrics, alarms, and dashboards](sec04-bp02.md) 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [SEC10-BP02 Develop incident management plans](sec10-bp02.md) 

 **Related documents:** 
+  [Security Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) 
+  [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 

 **Related examples:** 
+  [How Amazon CloudWatch Logs data protection can help detect and protect sensitive log data](https://aws.amazon.com/blogs/mt/how-amazon-cloudwatch-logs-data-protection-can-help-detect-and-protect-sensitive-log-data/) 
+  [Logging strategies for security incident response](https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/) 
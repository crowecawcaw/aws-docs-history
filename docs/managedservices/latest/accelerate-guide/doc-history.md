

# Document history for AMS Accelerate User Guide
<a name="doc-history"></a>

The following table describes the important changes in each release of the *AMS Accelerate User Guide*. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Updated baseline monitoring alerts](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/monitoring-default-metrics.html) | Removed ALB instance RejectedConnectionCount, ALB target TargetConnectionErrorCount, NATGateways PacketsDropCount, and NATGateways ErrorPortAllocation alerts from the baseline monitoring table. | July 1, 2026 | 
| [Updated Alarm Manager documentation for control plane upgrade](#doc-history) | Updated Alarm Manager documentation to reflect the control plane migration completed in February 2026:+ [Accelerate Alarm Manager](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tag-alarms.html) - Removed regional limitation notice, added emphasis to configuration warning, and removed timing statement about changes taking effect<br />+ [Accelerate Configuration profile: monitoring](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-doc-format.html) - Removed contradictory statement about ConfigurationID<br />+ [Accelerate Configuration profile: pseudoparameter substitution](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-doc-sub.html) - Added pseudoparameters for new resource types and updated existing descriptions for EC2 instances and disks, Elasticsearch domains, and Elastic Load Balancing<br />+ [Accelerate alarm configuration examples](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-ex.html) - Removed path dimension from Linux disk alarm example as disk path parameter is no longer supported for Linux<br />+ Removed deprecated page "Viewing the number of resources monitored by Alarm Manager" as reporting functionality was deprecated with the control plane upgrade<br />+ [Resource inventory for Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-inventory.html) - Updated to reference new resource inventory file reflecting control plane architecture changes | March 31, 2026 | 
| [Updated Resouce Inventory for Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-inventory.html) | Added details regarding compliance control of AMS infrastructure. | March 27, 2026 | 
| [Updated Compute Optimizer recommendations boolean values](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-recommendations-co.html) | Updated all boolean parameter values from uppercase (True/False) to lowercase (true/false) for consistency with standard conventions. | March 24, 2026 | 
| [Updated AMS-STD-002 Point 6.11 for cross-account policies](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-stand-controls.html) | Clarified that cross-account policies with write access to third-party accounts can be configured with risk acceptance. | March 24, 2026 | 
| [Updated AWS Health monitoring notes](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/monitoring-default-metrics.html) | Clarified that notifications are sent only for AWS Health events that require action by AMS Operations. | March 24, 2026 | 
| [Added ONTAP volume capacity automatic remediation](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | Added AMSFSXONTAPVolumeCapacityUtilization alert to the automatic remediation table and added a new section describing ONTAP volume capacity remediation automation. | March 24, 2026 | 
| [Updated Resource Scheduler schedule periods field label](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/res-sched-periods.html) | Corrected the field label from "Schedules" to "Periods" in the add schedule procedure. | March 11, 2026 | 
| [Updated Alerts from baseline monitoring in AMS section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/monitoring-default-metrics.html) | Updated Alerts from baseline monitoring in AMS table with updated trigger condition for Amazon EC2 instance - all OSs. | January 22, 2026 | 
| [Updated Customer Security Risk Management process section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-csrm-process.html) | Updated Customer Security Risk Management process section with risk acceptance validity, review, and opt-out information. | January 15, 2026 | 
| [Updated Amazon RDS low storage event remediation automation section in AMS automatic remediation of alerts](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | Updated Amazon RDS low storage event remediation automation section with information for properties modified by remediations depending on a triggering event. | January 15, 2026 | 
| [Updated table for Operations On Demand section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ops-on-demand.html) | Updated the table for Operations On Demand section with updated content. | January 7, 2026 | 
| [Updated and added new content to Trusted Remediator in AMS section with information about Security Hub CSPM](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-sec-hub-recommendations.html) | Updated Trusted Remediator in AMS section with information about Security Hub CSPM and added a new page, Security Hub CSPM recommendations supported by Trusted Remediator. | December 11, 2025 | 
| [Updated supported Regions](#doc-history) | Added notes in the following sections for services not available in the Asia Pacific (Malaysia) Region:+ [Monitor with Amazon Macie](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-data-protect.html#acc-sec-data-protect-macie)<br />+ [Monitoring and incident management for Amazon EKS in AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mon-inc-mgmt-eks.html)<br />+ [SSM Agent automatic installation](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ssm-agent-auto-install.html)<br />+ [Accelerate Alarm Manager](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tag-alarms.html) | October 24, 2025 | 
| [Updated Log management — AWS CloudTrail section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-log-mgmt.html) | New information and note regarding AWS CloudTrail logging. | September 25, 2025 | 
| [Added 4 new Trusted Advisor cost optimization checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html) | Added the following cost optimization checks:+ c1z7kmr00n - Amazon EC2 cost optimization recommendations for instances<br />+ c1z7kmr02n - Amazon EBS cost optimization recommendations for volumes<br />+ c1z7kmr03n - Amazon RDS cost optimization recommendations for DB instances<br />+ c1z7kmr05n - AWS Lambda cost optimization recommendations for functions | September 22, 2025 | 
| [Updated deprecation note for Change Record service](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-change-record.html) | Updated deprecation note for Change Record service with alternate solutions. | September 11, 2025 | 
| [Updated Trusted Advisor security checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html#tr-supported-checks-security) | Updated the Supported preconfigured parameters and constraints for check Hs4Ma3G108 - CloudTrail trails should be integrated with Amazon CloudWatch Logs | September 5, 2025 | 
| [Updated Trusted Advisor security checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html#tr-supported-checks-security) | Updated Trusted Advisor security check to add version 2 of Hs4Ma3G184 - Application Load Balancers and Classic Load Balancers logging should be enabled | September 5, 2025 | 
| [Updated Trusted Advisor operational excellence checks supported by Trusted Remediator section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html) | Updated Trusted Advisor operational excellence checks supported by Trusted Remediator to add new supported check c1fd6b96l4 Amazon S3 Access Logs Enabled. | August 28, 2025 | 
| [Updated Trusted Remediator section to include new content for Compute Optimizer](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/trusted-remediator.html) | Updated Trusted Remediator section to include new content for supported AWS Compute Optimizer recommendations. | August 18, 2025 | 
| [TOC Glossary link removed](#doc-history) | [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html). | August 8, 2025 | 
| [TOC Glossary link removed](#doc-history) | [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html). | August 8, 2025 | 
| [New field in Patch Daily report](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/daily-patch-report.html) | Instance Tags: The tags associated with the Amazon EC2 instance ID. | August 8, 2025 | 
| [New Trusted Remediator checks](#doc-history) | [Trusted Advisor cost optimization checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html#tr-supported-checks-cost-op)   [Trusted Advisor security checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html#tr-supported-checks-security)   Hs4Ma3G120–AWSManagedServices-TerminateEC2InstanceStoppedForPeriodOfTime, Hs4Ma3G230–AWSManagedServices-TrustedRemediatorEnableBucketAccessLoggingV2, and c18d2gz150–AWSManagedServices-TerminateEC2InstanceStoppedForPeriodOfTime. | August 8, 2025 | 
| [Updating IAM standard in point 3.2](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-stand-controls.html) | Clarified language and removed mention of tagging. | July 25, 2025 | 
| [Updated Resource Tagger Configuration Profiles in Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-tools-profiles.html) | Added new AvailabilityZone filter in Resource Tagger Configuration Profiles in Accelerate. | July 25, 2025 | 
| [Updated Incident reports, service requests, and billing questions in Accelerate.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-supp-ex.html) | Replaced references to Plus and Premium service tiers with a link to service SLA. | July 25, 2025 | 
| [Updated Incident management in Accelerate.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-manage-incidents.html) | Updated information about operations centers. | July 25, 2025 | 
| [Updated AMS patterns page with correct links.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ams-patterns.html) | Fixed the SLA and SLO links. | July 25, 2025 | 
| [Update of alert opt-out options](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | Addition of a tag allows you to opt-out of an additional two alerts. | July 25, 2025 | 
| [New feature for backups](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-backup-ams-vaults.html) | Customize notifications on backup vaults with a new tag. | July 25, 2025 | 
| [Updated section for Supported configurations in Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html) | Updated Supported configurations for Supported operating systems and Supported End of Support (EOS) operating systems in Accelerate. | June 26, 2025 | 
| [Removed page Managing tags for patch management in Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-req.html) | Removed page Managing tags for patch management in Accelerate as this feature is deprecated. | June 19, 2025 | 
| [Patch management important security note for alternate patch repositories.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-patching.html) | Important security note and best practices for using alternate patch repositories in AMS Accelerate. | June 10, 2025 | 
| [AMS Accelerate change record deprecation.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-change-record.html) | The AMS Accelerate Change Record service is being deprecated effective July 1st, 2025. | May 27, 2025 | 
| [Supported operating systems updates.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) | AMS Accelerate supported operating systems are updated, some added, some removed. | May 22, 2025 | 
| [Note for Middle East (UAE) Region supported services.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#acc-supported-services) | Limited support for some services in Middle East (UAE) Region. | May 22, 2025 | 
| [Internal-only APIs.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/internal-apis.html) | Internal-only APIs that appear in some CloudWatch logs. | May 22, 2025 | 
| [Added missing log locations.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-log-mgmt.html#acc-lm-ec2) | Some missing Windows log locations were added. | May 22, 2025 | 
| [AMS Accelerate Trusted Remediator updates.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-configure-remediations.html) | How to use a new parameter, `preconfigured-parameters`, to customize Trusted Advisor checks in Trusted Remediator. | May 22, 2025 | 
| [AMS Accelerate Trusted Remediator FAQ and updates.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-faq.html) | Several updates to supported Trusted Advisor checks, Trusted Remediator FAQ (added "What resources does Trusted Remediator deploy to your accounts?"), and more. See also [Trusted Advisor checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html). | May 8, 2025 | 
| [AMS Accelerate Standard security controls update.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ams-sec-stand-controls.html) | Added "Security group sharing" controls. | May 8, 2025 | 
| [Accelerate monitoring alerts update.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/monitoring-default-metrics.html) | Additional alerts added, plus alert name added to Notes column. | April 28, 2025 | 
| [Accelerate resource inventory.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-inventory.html) | The resource inventory spreadsheet file (compressed) is updated. | April 24, 2025 | 
| [Accelerate log locations.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-log-mgmt.html#acc-lm-ec2) | Additional log locations added. | April 24, 2025 | 
| [Accelerate New roles and responsibilities (RACI) for Security Incident Response.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#acc-sd-responsibilities) | RACI for Security Incident Response. | March 27, 2025 | 
| [Accelerate New Amazon RDS auto-remediation alert.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | Alert ID:- 0224, triggers when the requested allocated storage reaches or exceeds the configured maximum storage threshold. | March 27, 2025 | 
| [Accelerate Onboarding role template update.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-onb-roles.html) | The AMS Accelerate onboarding role template has been updated to support AWS GovCloud regions. | March 25, 2025 | 
| [Accelerate New auto-remediations RDS alert.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | RDS-EVENT-0224 added. | March 17, 2025 | 
| [Accelerate New feature: Incident notifications.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/app-aware-inc-notifications.html) | You can use AppRegistry to create applications and customize the incident notifications for those applications. | March 13, 2025 | 
| [Accelerate Update to RDS alarm monitoring threshold.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/monitoring-default-metrics.html) | The RDS Average CPU Utilization alarm threshold has been changed from 75% to 90%. | February 20, 2025 | 
| [Accelerate Update to AMS automatic remediation of alerts table.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/auto-remediation.html) | The alert remediation table has been expanded with new content. | February 20, 2025 | 
| [Accelerate New feature: Retain Alarms.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-retain-alarm.html) | You can configure Alarm Manager to retain alarms in CloudWatch instead of automatic deletion. | February 20, 2025 | 
| [Updated Self-service reports with new data options for aggregated report viewing](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/self-service-reporting.html) | Added data options to include new **Field Name:** `Admin Account ID`, **Dataset Field Name:** `aws_admin_account_id`, and **Definition:** `Trusted AWS Organization account enabled by the customer` for the following Self-service reports:+ Patch report (daily)<br />+ Backup report (daily)<br />+ Incident report (weekly)<br />+ Resource Tagger dashboard<br />+ Security Config Rules dashboard | January 28, 2025 | 
| [Added additional AWS Trusted Advisor checks supported by Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html) | The following Trusted Advisor checks are now supported by Trusted Remediator:+ Cost Optimization  c1cj39rr6v - Amazon S3 Incomplete Multipart Upload Abort Configuration <br />+ Security  Hs4Ma3G199 - RDS DB instances should publish logs to CloudWatch Logs Hs4Ma3G326 - Amazon EMR block public access setting should be enabled Hs4Ma3G272 - Users should not have root access to SageMaker AI notebook instances Hs4Ma3G325 - EKS clusters should have audit logging enabled HHs4Ma3G118 - VPC default security groups should not allow inbound or outbound traffic Hs4Ma3G127 - API Gateway REST and WebSocket API execution logging should be enabled Hs4Ma3G124 - Amazon EC2 instances should use Instance Metadata Service Version 2 (IMDSv2) <br />+ Fault tolerance  c1qf5bt013 - Amazon RDS DB instances have storage auto scaling turned off 7qGXsKIUw - Classic Load Balancer Connection Draining c18d2gz106 - Amazon EBS Not Included in AWS Backup Plan c18d2gz107 - Amazon DynamoDB Table Not Included in AWS BackupPlan cc18d2gz117 - Amazon EFS Not Included in AWS BackupPlan c18d2gz105 - Network Load Balancer Cross Load Balancing c1qf5bt026 - Amazon RDS synchronous\_commit parameter is turned off c1qf5bt030 - Amazon RDS innodb\_flush\_log\_at\_trx\_commit parameter is not 1 c1qf5bt031 - Amazon RDS sync\_binlog parameter is turned off c1qf5bt036 - Amazon RDS innodb\_default\_row\_format parameter setting is unsafe c18d2gz144 - Amazon EC2 Detailed Monitoring Not Enabled <br />+ Operational Excellence  c18d2gz125 - Amazon API Gateway Not Logging Execution Logs c18d2gz168 - Elastic Load BalancingDeletion Protection Not Enabled for Load Balancers c1qf5bt012 - Amazon RDS Performance Insights is turned off <br />+ Performance  c1qf5bt021 - Amazon RDS innodb\_change\_buffering parameter using less than optimum value c1qf5bt025 - Amazon RDS autovacuum parameter is turned off c1qf5bt028 - Amazon RDS enable\_indexonlyscan parameter is turned off c1qf5bt029 - Amazon RDS enable\_indexscan parameter is turned off c1qf5bt032 - Amazon RDS innodb\_stats\_persistent parameter is turned off c1qf5bt037 - Amazon RDSgeneral\_logging parameter is turned on  | January 28, 2025 | 
| [Updated resource inventory spreadsheet](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-inventory.html) | Updated resource inventory spreadsheet. | January 23, 2025 | 
| [New AMS feature: Aggregated Self Service Reports](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/aggregated-reports.html) | Aggregated self-service reporting (SSR) provides you a view of existing self-service reports aggregated at the organization level, cross-account. | January 21, 2025 | 
| [New Accelerate patching feature: Patch Hooks](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-p-hooks.html) | Use this feature to configure "hooks" with SSM Command documents to run operating system level commands before or after patching. | January 16, 2025 | 
| [Update to How monitoring works section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-monitoring-works.html) | Added information on a new feature, configuring alert notifications by resource, or instance ID, rather than by incident. | January 8, 2025 | 
| [Update to Onboarding section of EKS Monitoring and Incident Management](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mon-inc-mgmt-eks-onboarding.html) | Updated the onboarding procedure note to clarify when alert signals are suspended and resumed. | December 19, 2024 | 
| [Member account log added to Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-logging.html#tr-logging-member-account) | You can use the Member accounts log to find the account ID, onboarded AWS Regions, and execution time of each member account. | December 19, 2024 | 
| [Prerequisites for SSM Agent use](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ssm-agent-auto-install.html) | Content on blocking outbound traffic is updated. | December 4, 2024 | 
| [Accelerate Monitoring and Incident Management for EKS is now supported in the Asia Pacific (Hong Kong) AWS Region](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-requirements.html) | Asia Pacific (Hong Kong) is now a supported by Accelerate Monitoring and Incident Management for EKS | November 21, 2024 | 
| [Updated Operations On Demand offerings table](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ops-on-demand.html) | The following operating systems are supported for in-place upgrades:+ Microsoft Windows 2016 to Microsoft Windows 2022 and above | November 11, 2024 | 
| [Accelerate Monitoring and Incident Management for EKS is now supported in the Africa (Cape Town) AWS Region.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-requirements.html) | Africa (Cape Town) is now a supported by Accelerate Monitoring and Incident Management for EKS | November 4, 2024 | 
| [Updated Operations On Demand offerings table](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ops-on-demand.html) | The following operating systems are supported for in-place upgrades:+ Microsoft Windows 2012 R2 to Microsoft Windows 2016 and above<br />+ Red Hat Enterprise Linux 7 to Red Hat Enterprise Linux 8<br />+ Red Hat Enterprise Linux 8 to Red Hat Enterprise Linux 9<br />+ Oracle Linux 7 to Oracle Linux 8 | November 1, 2024 | 
| [Updated Quick Start Template](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-quick-start.html) | Updated diagram, template parameters, and yaml template file. | October 28, 2024 | 
| [Trusted Advisor checks added to Trusted Remediator in AMS](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html) | The following Trusted Advisor checks are now available in Trusted Remediator:+ Z4AUBRNSmz - Unassociated Elastic IP Addresses<br />+ c18d2gz128 - Amazon ECR Repository Without Lifecycle Policy Configured<br />+ c18d2gz138 - DynamoDB Point-in-time Recovery<br />+ Hs4Ma3G323 - DynamoDBtables should have deletion protection enabled<br />+ Hs4Ma3G247 - Amazon EC2 Transit Gateway should not automatically accept VPC attachment requests<br />+ Hs4Ma3G308 - Amazon DocumentDB clusters should have deletion protection enabled<br />+ Hs4Ma3G299 - Neptune DB clusters should have deletion protection enabled<br />+ Hs4Ma3G306 - Amazon DocumentDB manual cluster snapshots should not be public<br />+ Hs4Ma3G109 - CloudTrail log file validation should be enabled<br />+ Hs4Ma3G217 - CodeBuild project environments should have a logging AWS Configuration4<br />+ Hs4Ma3G158 - SSM documents should not be public<br />+ Hs4Ma3G319 - Network Firewall firewalls should have deletion protection enabled | October 25, 2024 | 
| [Updated Supported configurations](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) | Updated supported Oracle Linux operating systems to 9.0-9.3, 8.0-8.9, 7.5-7.9. | October 24, 2024 | 
| [New section added to Offboard from AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-offboard.html) | Instructions on how to offboard with Alarm Manager and Resource Tagger dependencies added to **Offboard from AMS Accelerate**. | October 24, 2024 | 
| [Resource Tagger dashboard is now available.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/resource-tagger-dashboard.html) | The **Resource Tagger dashboard** is now available in **Self-service reporting**. | September 26, 2024 | 
| [You can now include multiple email addresses in tag-based alerts.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-monitoring-works.html#how-mon-works-alert-notes-tags) | Multiple email addresses are now supported in tag-based alerts. | September 20, 2024 | 
| [AMS Accelerate limits are now included in AMS patch management.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-p-maint-window.html) | AMS Accelerate limits are included in **Patch management** - **Create a patch maintenance window**. | August 30, 2024 | 
| [AMS Accelerate Account Discovery update](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-acct-disc.html) | A new section in Account Discovery has been added for Amazon EC2 Instance Evaluation. | August 29, 2024 | 
| [AMS Accelerate default patch baseline is now available for Ubuntu operating systems.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-patch-baseline.html#acc-patch-baseline-default) | AMS Accelerate default patch baseline is now available for Ubuntu operating systems. | August 22, 2024 | 
| [AMS Accelerate Account Discovery update](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-acct-disc.html) | Four new AWS API calls have been added to the AWS CloudTrail Evaluation section in the operational check table. | August 2, 2024 | 
| [Trusted Remediator now supports an additional check](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/tr-supported-checks.html) | Trusted Remediator now supports the security check Hs4Ma3G192 - RDS DB Instances should prohibit public access. | July 30, 2024 | 
| [AMS now supports Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-data-protect.html#acc-sec-data-protect-r53) | AMS now supports Amazon Route 53 Resolver DNS Firewall | July 30, 2024 | 
| [AMS Accelerate onboarding\_role\_minimal.zip now contains Terraform code](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-onb-roles.html) | AMS Accelerate onboarding\_role\_minimal.zip now contains Terraform code. | July 30, 2024 | 
| [Security Config Rules Dashboard](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/sec-config-dashboard.html) | The Security Config Rules Dashboard is now available in Self-Service reporting. | July 24, 2024 | 
| [AMS Accelerate now supports Oracle Linux 8.9, RHEL 8.10, and RHEL 9.4.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) | AMS Accelerate now supports Oracle Linux 8.9, RHEL 8.10, and RHEL 9.4. | July 5, 2024 | 
| [AMS Accelerate account discovery process updated.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-acct-disc.html) | The account discovery process used when onboarding AWS accounts to AMS Accelerate is updated. | July 1, 2024 | 
| [Trusted Remediator is now available.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/trusted-remediator) | Trusted Remediator, an AWS Managed Services solution that automates the remediation of AWS Trusted Advisor checks, is now available. | June 24, 2024 | 
| [Amazon Route 53 Resolver DNS firewall events in Security Incident Response.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/sir-detect.html) | AMS now monitors Amazon Route 53 Resolver DNS firewall events in Security Incident Response | June 21, 2024 | 
| [Updated supported operating systems](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) | AMS Accelerate now supports AlmaLinux 8.3-8.9, 9.0-9.2 (AlmaLinux is only supported with x86 architecture) | June 19, 2024 | 
| [Automatic instance profile limit now increases if the default is met.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/inst-auto-config-details-iam.html) | AMS now increases the default instance profile limit to 20 if the default limit of 10 is reached. | June 18, 2024 | 
| [AMS SSM Agent automatic installation feature now enabled by default.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ssm-agent-auto-install.html) | The AMS SSM Agent automatic installation feature is enabled by default for accounts onboarded after 6/03/2024. | June 7, 2024 | 
| [Security FAQ added to Security management.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/security-access-faq.html) | A Security FAQ is now available that covers common questions about the security best practices, controls, access models, and audit mechanisms used when an AMS operations engineer or automation accesses your accounts. | June 3, 2024 | 
| [Additional AWS Regions now supported by Monitoring and Incident Management for Amazon EKS.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-requirements.html) | Three additional AWS Regions are now supported by Monitoring and Incident Management for Amazon EKS. | May 23, 2024 | 
| [Service request patch notifications are now sent in advance of Patch Maintenance windows.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-patch-mon-remediate.html) | AMS Accelerate patching creates a new service request 4 days in advance of a Patch Maintenance window. You can use the service request to communicate with AMS for adjustments to the patch or to skip a patch. | May 3, 2024 | 
| [Alert thresholds added to the AMS Accelerate EKS monitoring baseline alerts table.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-baseline-eks-alerts) | Detailed alert thresholds are now available in the Baseline alerts table for Amazon EKS monitoring. | May 3, 2024 | 
| [Updated: Alarm Manager Configuration Profiles.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-doc-format) | Added notes about creating Anomaly Detection alarms with Alarm Manager. | April 25, 2024 | 
| [Additions to Resource Tagger configuration profiles.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-tools-profiles.html) | DynamoDB tables and Amazon S3 buckets are now available in Resource Tagger | April 25, 2024 | 
| [Added Planned Event Management (PEM) information section.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ams-pem.html) | Detailed information about the PEM service offering is now available in the *AMS Accelerate User Guide*. | April 25, 2024 | 
| [AMS supports Red Hat Enterpise Linux (RHEL) 9.x.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#supported-configs) | AMS supports Red Hat Enterprise Linux (RHEL) 9.x. | April 25, 2024 | 
| [AMS Accelerate supports reporting for all AWS Region configurations.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ams-reporting.html) | AMS Accelerate supports SSM Inventory Reporting for all AWS Region configurations. | April 25, 2024 | 
| [Updated: AWS managed policies.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/using-service-linked-roles.html#slr-updates) | Updated the AWSManagedServicesDeploymentToolkitPolicy with new ECR permissions. | April 4, 2024 | 
| [Updated: Resource Tagger Configuration Profiles section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-tools-profiles.html) | Added `AWS::EFS::FileSystem` to the **ResourceType** list. | March 21, 2024 | 
| [Updated: Incident reports and service requests in Accelerate section.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-billing-questions.html) | Changed the topic title to Incident reports, service requests, and billing questions in Accelerate. Added a new section, **Billing questions**. | March 21, 2024 | 
| [Updated: How service request management works section.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-sr-management-work.html) | Added clarification on how AMS handles service requests that contain a feature request or a bug. | March 21, 2024 | 
| [Updated: Create aws\_managedservices\_onboarding\_role role with CloudFormation section](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-onb-create-roles-with-cf.html) | Added commands to create the role from AWS CloudShell. | March 21, 2024 | 
| [Updated: (Optional) Quick Start template](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-quick-start.html#quick-start-download) | Added commands to download the template from AWS CloudShell. | March 21, 2024 | 
| [New resource types available for Alarm Manager configuration profiles.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-doc-format.html) | Added resource types for Amazon FSx, Amazon EFS, and Elasticsearch to Alarm Manager configuration profiles. | March 21, 2024 | 
| [Additional pseudoparameter substitutions available for configuration profile.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-config-doc-sub.html) | Added Amazon EFS and Amazon FSx pseudoparameter substitutions. | March 21, 2024 | 
| [Added new section to Features in the Service description topic.](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sd.html#features) | Added a new section, **Service request management** under **AMS Accelerate features**. | March 21, 2024 | 
| [New columns added to the self-service reporting Weekly Incident report](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/weekly-incident-report.html) | New columns were added to the Weekly Incident report so that you can filter for incidents based on quarter, month, week, or day that the incident was created or resolved. | March 11, 2024 | 

## Earlier updates
<a name="earlier-updates"></a>

The following table describes the important changes to the documentation of the AMS Accelerate guide prior to March 2024.




- **Improvements for AMS Accelerate CloudTrail trail onboarding **
  - **Description:** Improvements for AMS Accelerate CloudTrail trail onboarding:+ Collect all bucket policies in a single block<br />+ Remove the second AWS Organization ID in the policy statements<br />+ Clarify customer environment requirements<br />For more information, see [Review and update your configurations to enable AMS Accelerate to use your CloudTrail trail](acc-onb-trail-choices.md).
  - **Date:** February 23, 2024

- **Updated: Account onboarding process. **
  - **Description:** Restructured the **Account onboarding process** section to make the steps more clear. Also aded an optional Quick Start template for onboarding features.<br />See [(Optional) Quick Start template in Accelerate](acc-quick-start.md).
  - **Date:** February 22, 2024

- **Updated: Offboarding AMS Accelerate. **
  - **Description:** Updated the AMS Accelerate offboarding considerations section to indicate that the `ams-access-management ` CloudFormation stack and `ams-access-management` IAM role aren't deleted by the offboarding process.<br />See [AMS Accelerate offboarding effects](acc-offboard.md#acc-offboard-considerations).
  - **Date:** February 22, 2024

- **Updated: Configuration compliance in Accelerate. **
  - **Description:** Changed "Incident Report" to "Service Request" where applicable to avoid confusion on these terms.<br />See [Configuration compliance in Accelerate](acc-sec-compliance.md).
  - **Date:** February 22, 2024

- **Updated: Account discovery in Accelerate. **
  - **Description:** Reorganized **Account discovery in Accelerate** to better group prerequisites with the relevant section.<br />See [Step 1. Account discovery in Accelerate](acc-acct-disc.md).
  - **Date:** February 22, 2024

- **Renamed: AMS Patch reporting to AMS host management. **
  - **Description:** Renamed AMS Patch reporting to AMS host management and renamed the report, Patch Details report, to SSM Agent Coverage report.<br />See [AMS host management reports](ams-host-man.md).
  - **Date:** February 22, 2024

- **Updated Operations on Demand Catalog**
  - **Description:** Updated the Operations on Demand catalog of offerings table to remove references to "health" in `Amazon EKS cluster maintenance`.<br />See [Requesting AMS Operations On Demand](ops-on-demand.md#ops-on-demand-request).
  - **Date:** February 22, 2024

- **Updated AMS Event Router**
  - **Description:** Updated the `AMSCoreRule` in the AMS Event Router section.<br />See [Using Amazon EventBridge Managed Rules in AMS](how-event-router-works.md).
  - **Date:** February 22, 2024

- **Updated Supported Operating Systems. **
  - **Description:** Updated Supported Operating Systems to include SUSE Linux Enterprise Server 15 SP5.<br />See [Supported configurations](acc-sd.md#supported-configs).
  - **Date:** February 22, 2024

- **Updated EC2 volume usage remediation automation **
  - **Description:** Updated the EC2 volume usage remdiation automation section with correct capacity expansion schedule.<br />See [EC2 volume usage remediation automation](auto-remediation.md#auto-remediation-ec2-vol-use).
  - **Date:** February 22, 2024

- **Updated: Review and update your configurations to enable Accelerate to use your CloudTrail trail**
  - **Description:** Updated the AMS Accelerate Organization CloudTrail S3 bucket policy section. See [Review and update your configurations to enable AMS Accelerate to use your CloudTrail trail](acc-onb-trail-choices.md)
  - **Date:** February 15, 2024

- **Added new feature: SSM Agent auto installation **
  - **Description:** Added a new section for SSM Agent auto installation<br />See [SSM Agent automatic installation](ssm-agent-auto-install.md).
  - **Date:** January 26, 2024

- **Updated: Supported configurations **
  - **Description:** Added information regarding the supported versions of AWS Control Tower<br />See [Supported configurations](acc-sd.md#supported-configs).
  - **Date:** January 26, 2024

- **Updated: AMS Patch reporting. **
  - **Description:** Removed three sections from AMS Patch reporting:+ Patch Instance Details Summary report<br />+ Patch Details report<br />+ Instances that Missed Patches report<br />See [AMS host management reports](ams-host-man.md).
  - **Date:** December 22, 2023

- **Updated: Accelerate onboarding prerequisites. **
  - **Description:** Updated the support plans required to onboard AMS Accelerate.<br />See [Accelerate onboarding prerequisites](acc-gs-prereqs.md).
  - **Date:** December 15, 2023

- **Updated: Create a patch maintenace window. **
  - **Description:** Removed Default patch cycle sectio as this feature is deprecated.<br />See [Create a patch maintenance window in AMS](acc-p-maint-window.md).
  - **Date:** December 13, 2023

- **Updated: Notification settings in Accelerate. **
  - **Description:** Clarified what email is used for notifications.<br />See [Notification settings in Accelerate](acc-notifications.md) for more information.
  - **Date:** December 12, 2023

- **Updated: `AMSAccelerateCustomerAccessPolicies` template. **
  - **Description:** Updated the `AMSAccelerateCustomerAccessPolicies` template to correct a syntax error.<br />See [Permissions to use AMS features](acc-access-customer.md) for more information.
  - **Date:** December 12, 2023

- **Added: Change request security reviews **
  - **Description:** Added a new section **Change request security reviews** under **Security Management**.<br />See [Change request security reviews](acc-sec-change-request-review.md) for more information.
  - **Date:** December 11, 2023

- **Updated: resource\_inventory.xlsx **
  - **Description:** Updated the resource\_inventory.xlsx to include Security Analyst roles.<br />See [Resource inventory for Accelerate](acc-resource-inventory.md) for more information.
  - **Date:** November 17, 2023

- **Updated: ams-access-admin-operations role description **
  - **Description:** Updated **ams-access-admin-operations** description.<br />See [Why and when AMS accesses your account](access-justification.md) and [Authenticating with identities in AMS Accelerate](acc-sec-iam.md#acc-sec-iam-auth) for more information.
  - **Date:** November 17, 2023

- **Updated: AMS Accelerate offboarding considerations **
  - **Description:** Updated **Security** section to clarify what is available from Amazon GuardDuty and AWS Config rules after offboarding.<br />See [AMS Accelerate offboarding effects](acc-offboard.md#acc-offboard-considerations) for more information.
  - **Date:** November 17, 2023

- **Added: Monitoring and Incident Management for Amazon EKS**
  - **Description:** Monitoring and Incident Management for Amazon EKS monitors your Amazon EKS resources for failures, performance degradation, and security issues.<br />See [Monitoring and incident management for Amazon EKS in AMS Accelerate](acc-mon-inc-mgmt-eks.md) for more information.
  - **Date:** November 14, 2023

- **Updated: Tagging**
  - **Description:** Added information on customer-provided tagging.<br />See [Customer-provided tags in Accelerate](acc-tag-cust-provided.md) for more information.
  - **Date:** November 7, 2023

- **Updated: Resource Tagger Configuration Profiles**
  - **Description:** Added AWS::AutoScaling::AutoScalingGroup, AWS::EKS::Cluster, AWS::Elasticsearch::Domain, and AWS::FSx::FileSystem to the Filter section.<br />See [Resource Tagger Configuration Profiles in AMS Accelerate](acc-tag-tools-profiles.md) for more information.
  - **Date:** October 27, 2023

- **Updated: Service Description**
  - **Description:** Added Ubuntu 22.04 to Supported Operating Systems. See [Service description](acc-sd.md)
  - **Date:** September 29, 2023

- **Updated: AMS Accelerate Onboarding Prerequisites **
  - **Description:** Added a note to AMS Accelerate VPC endpoints to include CloudFormation template. See [Accelerate onboarding prerequisites](acc-gs-prereqs.md).
  - **Date:** September 29, 2023

- **Updated: Detect**
  - **Description:** Removed endpoint protection type from the AMS Accelerate security response. See [Detect](sir-detect.md). 
  - **Date:** September 29, 2023

- **Updated: Alerts from Baseline Monitoring in AMS**
  - **Description:** Added AWS Outposts to the Alerts from Baseline Monitoring table. See [Detect](sir-detect.md) monitoring-default-metrics.
  - **Date:** September 29, 2023

- **Updated: Create aws\_managedservices\_onboarding\_role role with CloudFormation**
  - **Description:** Updated screenshot for Specify Stack Details. See [Create `aws_managedservices_onboarding_role` with CloudFormation for Accelerate](acc-onb-create-roles-with-cf.md).
  - **Date:** September 29, 2023

- **Updated: Amazon EventBridge Managed Rules deployed by AMS Accelerate **
  - **Description:** Added new AMS Accelerate Amazon EventBridge Managed Rule **AMSCoreRule**.<br />Updated AMS Accelerate Amazon EventBridge Managed Rule **AMSAccessRolesRule** to add a new role.<br />See [Amazon EventBridge Managed Rules deployed by AMS](how-event-router-works.md#managed-rules-deployed) for more information. 
  - **Date:** September 19, 2023

- **Updated: Alarm Manager Configuration Profiles**
  - **Description:** Added AWS Outposts pseudoparameter substitution identifiers. See [Monitoring and event management in AMS Accelerate](acc-mon-event-mgmt.md). 
  - **Date:** September 11, 2023

- **Updated: Resource Tagger Configuration Profiles**
  - **Description:** Added AWS Outposts resource type. See [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md). 
  - **Date:** September 11, 2023

- **Updated: Supported services**
  - **Description:** Added Amazon Elastic File System to the **Services monitored by CloudWatch alarms** section.<br />See [Service description](acc-sd.md) for more information. 
  - **Date:** September 6, 2023

- **Updated: Patch monitoring and failure remediation**
  - **Description:** Added the following note to **Using Patch Orchestrator** section:<br />"Patch failure alerts aren't created for instances that have unsupported operating systems, or that are stopped during the maintenance window"<br />See [Understand patch management in AMS Accelerate](acc-patching.md) for more information. 
  - **Date:** September 6, 2023

- **Updated: Clarified Response to malware events runbook**
  - **Description:** Clarified Response to malware events runbook for Security Incident response. See [Security Incident Response in AMS](security-incident-response.md) for more information. 
  - **Date:** September 6, 2023

- **Updated: Connecting your Accelerate account with Transit Gateway**
  - **Description:** Clarified steps for Connecting a new Accelerate account VPC to the AMS Multi-Account Landing Zone network (creating a TGW VPC attachment): See [Connecting your Accelerate account withTransit Gateway](https://docs.aws.amazon.com/managedservices/latest/userguide/malz-accelerate-account.html#ams-add-acc-connect-tgw) for more information. 
  - **Date:** September 5, 2023

- **Updated: Alerts from baseline monitoring in AMS**
  - **Description:** Removed reference to two deprecated alarms AMSReadLatencyAlarm and AMSWriteLatencyAlarm. See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md) for more information. 
  - **Date:** September 5, 2023

- **Added: AMS Event Router**
  - **Description:** Added documentation for AMS Event Router See [Using Amazon EventBridge Managed Rules in AMS](how-event-router-works.md) for more information. 
  - **Date:** September 5, 2023

- **Updated: List of Alarm Manager pseudoparameters.**
  - **Description:** Updated the list of Alarm Manager pseudoparameters. EC2 instance name parameter was added to EC2 instance and EC2 disk alarm configurations. See [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md) for more information. 
  - **Date:** August 29, 2023

- **Added: AMS Access Offboarding**
  - **Description:** Added consideration when offboarding AMS Access. See [AMS Accelerate offboarding effects](acc-offboard.md#acc-offboard-considerations). 
  - **Date:** August 24, 2023

- **Added: AMS Security Incident Response**
  - **Description:** Added documentation for using AMS Security Incident Response. See [Security Incident Response in AMS](security-incident-response.md). 
  - **Date:** August 18, 2023

- **Updated: AMS Accelerate access roles**
  - **Description:** Corrected a typo in the role names. See [AWS Identity and Access Management in AMS Accelerate](acc-sec-iam.md). 
  - **Date:** August 10, 2023

- **Updated: Policy statements**
  - **Description:** Replaced hardcoded role names with wildcards. See [Review and update your configurations to enable AMS Accelerate to use your CloudTrail trail](acc-onb-trail-choices.md). 
  - **Date:** August 10, 2023

- **Updated: List of monitored services with EFS alerts.**
  - **Description:** Updated the list of monitoring services with new EFS alerts for AMS baseline monitoring. 4 new EFS alert types were added. See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md) for more information. 
  - **Date:** August 03, 2023

- **Updated: Accelerate resource inventory table**
  - **Description:** Removed ams-backup-config-rule-stack and related resources. See [Resource inventory for Accelerate](acc-resource-inventory.md). 
  - **Date:** July 18, 2023

- **Updated: AMS Accelerate access roles**
  - **Description:** Removed roles ams-backup-config-rule-st-amsBackupAlertConfigRule-<8-digit hash> and ams-backup-config-rule-st-amsBackupPlanConfigRuleH-<8-digit hash>. See [AWS Identity and Access Management in AMS Accelerate](acc-sec-iam.md). 
  - **Date:** July 18, 2023

- **Updated: List of monitored RDS alerts.**
  - **Description:** Updated the list of RDS alerts for AMS baseline monitoring. 9 new RDS alert types were added and 3 existing RDS alert types were removed. See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md) for more information. 
  - **Date:** June 19, 2023

- **New: AMS Accelerate access roles**
  - **Description:** Added new access roles for AMS Security. 
  - **Date:** June 16, 2023

- **New: AMS Accelerate CloudTrail log management can now use customer CloudTrail trails.**
  - **Description:** Updated Accelerate supported options for CloudTrail log management, including Accelerate deployed trail or integration with customer managed CloudTrail account or Organization trail. See [Review and update your configurations to enable AMS Accelerate to use your CloudTrail trail](acc-onb-trail-choices.md) for more information. 
  - **Date:** June 09, 2023

- **Updated: AMS Accelerate Config Rules Response Configuration Report.**
  - **Description:** Updated on-request reporting for AWS Config Rules Response Configuration Report. See Accelerate updates to on-request reporting. See [AMS Config Rules Response Configuration report](config-rules-response-configuration.md). 
  - **Date:** May 26, 2023

- **Updated: Service Billing Start Date policy.**
  - **Description:** Updated definitions of Billing Start Date in [AMS key terms](key-terms.md). 
  - **Date:** May 15, 2023

- **Updated: AWS managed policies.**
  - **Description:** Updated the AWSManagedServicesDeploymentToolkitPolicy with new CFN and ECR permissions, and scoped down existing actions with wildcards. See Accelerate updates to service-linked roles. See [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates). 
  - **Date:** May 09, 2023

- **Updated: Access role policy links.**
  - **Description:** The access roles can now be downloaded directly from Accelerate S3 bucket locations. <br />See [Why and when AMS accesses your account](access-justification.md) and [AWS Identity and Access Management in AMS Accelerate](acc-sec-iam.md).

- **Updated: Monthly Billing Self-Service Report.**
  - **Description:** Added note: The Monthly Billing reports are only available in a Management Payer account (AMS Advanced multi-account landing zone), but are available for all linked AMS Accelerate-managed accounts. <br />See [Billing report (monthly)](monthly-billing.md).
  - **Date:** April 13, 2023

- **Updated: List of Alerts.**
  - **Description:** Removed CloudTrail references. <br />See [Log management in AMS Accelerate](acc-log-mgmt.md).
  - **Date:** April 13, 2023

- **Updated: List of Alerts.**
  - **Description:** Added three new SSM agent alerts. <br />See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md).
  - **Date:** April 13, 2023

- **Updated: Accelerate Prerequisites.**
  - **Description:** Clarified that Accelerate requires one of four AWS Support plans be in place and excludes the Developer plan. <br />See [Accelerate onboarding prerequisites](acc-gs-prereqs.md).
  - **Date:** April 13, 2023

- **Updated: Accelerate service-linked role policy.**
  - **Description:** The Contacts Service policy zip file has been updated. <br />See [AWS managed policies for AMS Accelerate](security-iam-awsmanpol.md).
  - **Date:** April 13, 2023

- **Updated: AMS Resource Scheduler.**
  - **Description:** Incorrect role name, AWSManagedServices-DescribeScheduleOrPeriod, corrected to AWSManagedServices-DescribeScheduleOrPeriods. See [Cost optimization with AMS Resource Scheduler](acc-resource-scheduler.md).
  - **Date:** April 13, 2023

- **Updated: AWS managed policies.**
  - **Description:** Updated [Customized findings responses](custom-findings-responses.md) with instructions for updating custom reponses in single or multiple accounts.
  - **Date:** April 13, 2023

- **Updated: Resource Tagger**
  - **Description:** Added warnings about "specifying the name for your new configuration (SampleConfigurationBlock in the provided example) as you may inadvertently override the AMS-managed configuration with the same name". See [Resource Tagger use cases in AMS Accelerate](acc-rt-using.md).
  - **Date:** March 16, 2023

- **Updated: Patch RACI**
  - **Description:** Several updates and clarfications to the RACI for patching. See [Service description](acc-sd.md).
  - **Date:** March 16, 2023

- **Updated: Actions in deployment toolkit SLR JSON **
  - **Description:** Updated policy and actions. See: [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md).
  - **Date:** March 16, 2023

- **Updated: Auto remediation **
  - **Description:** Removed LVM support for EC2 volume automation. See: [AMS automatic remediation of alerts](auto-remediation.md).
  - **Date:** March 16, 2023

- **Updated: Accelerate Onboarding.**
  - **Description:** Clarified use of roles, espcially the minimal role [The template to create AMS roles](acc-onb-roles.md). 
  - **Date:** March 16, 2023

- **Updated: Self-service reporting.**
  - **Description:** Daily backup reports now support primary and secondary regions. Both are reported in the Resource Region field of [Backup report (daily)](daily-backup-report.md). 
  - **Date:** March 16, 2023

- **Updated: Patching guidance**
  - **Description:** Added a warning not to customize the default patching baselines, which are managed by AMS. Instead, create a new custom patching baseline. See: [Default patch baseline](acc-patch-baseline.md#acc-patch-baseline-default) and [Custom patch baseline with AMS Accelerate](acc-patch-baseline-custom.md).
  - **Date:** March 16, 2023

- **Updated Service Termination policy.**
  - **Description:** Updated definitions of Service Termination and Service Termination Date in [AMS key terms](key-terms.md). Termination notcies must be issued by the 20th day of the month prior to your last full month.
  - **Date:** March 16, 2023

- **Updated: AWS managed policies.**
  - **Description:** Clarified policy name: [Contacts service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-contacts-service). 
  - **Date:** Feb 16, 2023

- **New: AWS managed policies.**
  - **Description:** Added policy: [Contacts service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-contacts-service). 
  - **Date:** Feb 16, 2023

- **Updated: Configuration compliance.**
  - **Description:** Fixed a misspelled word in: [Configuration compliance in Accelerate](acc-sec-compliance.md). 
  - **Date:** Feb 16, 2023

- **New Content: Unsupported OSes**
  - **Description:** Added information on what services AMS provides for unsupported operating systems (OSes), see [Capabilities for unsupported operating systems in Accelerate](acc-unsupported-os.md).
  - **Date:** Feb 16, 2023

- **Updated: Create patch windows**
  - **Description:** Added a link for using CloudShell to [Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate](acc-p-maint-window-cli.md).
  - **Date:** Feb 16, 2023

- **Updated Content: Onboarding management resources**
  - **Description:** Updated the zipped JSON templates in [The template to create AMS roles](acc-onb-roles.md).
  - **Date:** Feb 16, 2023

- **New Content: Configuration Compliance**
  - **Description:** Added a new topic: [Customized findings responses](custom-findings-responses.md).
  - **Date:** Feb 16, 2023

- **New: AWS managed policies.**
  - **Description:** Added policy: [Amazon EventBridge rule service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-evb-rule). 
  - **Date:** Feb 07, 2023

- **Updated: AWS managed policies.**
  - **Description:** Updated the `AWSManagedServicesDeploymentToolkitPolicy` with new S3 permissions. See [Accelerate updates to service-linked roles](using-service-linked-roles.md#slr-updates). 
  - **Date:** Jan 30, 2023

- **New opt-in region: CPT.**
  - **Description:** AMS Accelerate is now available in the Capetown (CPT) opt-in region. To opt in, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html). 
  - **Date:** Jan 12, 2023

- **Updated: Service Description.**
  - **Description:** Added FSx services monitored by CloudWatch alarms to [Service description](acc-sd.md). 
  - **Date:** Jan 12, 2023

- **Updated: Monitoring default metrics.**
  - **Description:** Added 6 FSx alarms to [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md). 
  - **Date:** Jan 12, 2023

- **Updated: AMS patterns.**
  - **Description:** Added *Customize Cloudwatch Alarm Notifications* to [AMS patterns](ams-patterns.md). 
  - **Date:** Jan 12, 2023

- **Updated: Onboarding management resources.**
  - **Description:** Updated the table of templates, adding a row for `ams-onboarding-ssm-execution-role` in [The template to create AMS roles](acc-onb-roles.md). 
  - **Date:** Jan 12, 2023

- **Updated: Configuration compliance.**
  - **Description:** Additional details for requesting custom remediations (in the Important box) on [Configuration compliance in Accelerate](acc-sec-compliance.md). 
  - **Date:** Jan 12, 2023

- **Updated: Service-linked-role permissions.**
  - **Description:** Removed older or duplicated permissions. See [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md). 
  - **Date:** Dec 15, 2022

- **Updated: Patch management, maintenance windows.**
  - **Description:** Added guidance to console instructions, step 5, for creating a maintenance window. See [Create a maintenance window from the Systems Manager console for AMS Accelerate](acc-p-maint-window-console.md). 
  - **Date:** Dec 15, 2022

- **New: Patch management section.**
  - **Description:** Added a section for Patch Tuesday maintenance windows. See [Create a recurring "Patch Tuesday" maintenance window from the AMS console (recommended)](acc-p-maint-window-ams-console.md). 
  - **Date:** Dec 15, 2022

- **Updated: AMS Resource Scheduler.**
  - **Description:** Updated the CloudFormation stack name. See [Using resources with AMS Resource Scheduler](res-sched-design.md). 
  - **Date:** Dec 15, 2022

- **Updated: Tag your resources for backup.**
  - **Description:** Added guidance for using AMS Resource Tagger. See [Tag your resources to apply AMS backup plans](acc-backup-assign-plan-resources.md). 
  - **Date:** Dec 15, 2022

- **Updated: Select a backup plan.**
  - **Description:** Indicated which plans offer continuous backup. See [Select an AMS backup plan](acc-backup-select-plan.md). 
  - **Date:** Dec 15, 2022

- **Updated: AMS Resource Scheduler.**
  - **Description:** Updated the AWS CLI example for deleting a period or schedule. See [Working with periods and schedules in AWS Managed Services Resource Scheduler](res-sched-periods.md). 
  - **Date:** Dec 15, 2022

- **Updated: AWS managed policies.**
  - **Description:** Added the `AWSManagedServicesDeploymentToolkitPolicy`. See [AWS managed policies for AMS Accelerate](security-iam-awsmanpol.md). 
  - **Date:** Dec 15, 2022

- **New: Added section describing the AMS new service-linked role, AWSServiceRoleForManagedServices\_DetectiveControlsConfig.**
  - **Description:** Added GovCloud regions and permissions. See [Detective controls service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-deploy-detect-controls). 
  - **Date:** Dec 15, 2022

- **New: AWS-managed policy**
  - **Description:** Added section describing how the AWS-managed policy, AWSManagedServices\_AlarmManagerPermissionsBoundary, is used in the service-linked role policy, AWSManagedServices\_AlarmManager\_ServiceRolePolicy, to restrict permissions of IAM roles created by the service-linked role AWSServiceRoleForManagedServices\_AlarmManager. See [AWS managed policies for AMS Accelerate](security-iam-awsmanpol.md). 
  - **Date:** Dec 15, 2022

- **Updated: Operations on Demand.**
  - **Description:** Added offerings: *SQL Server on EC2 Operations* and *AMI Building and Vending*. See [Operations On Demand](ops-on-demand.md). 
  - **Date:** Nov 10, 2022

- **Updated: Monitoring and event management.**
  - **Description:** Updated explanation of service notifications and incident reports. See [How monitoring works](how-monitoring-works.md). 
  - **Date:** Nov 10, 2022

- **Updated: Service-linked role regions**
  - **Description:** Added GovCloud regions and permissions. See [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md). 
  - **Date:** Nov 10, 2022

- **New: Service-linked role.**
  - **Description:** Added new role: `AWSServiceRoleForAMSDetectiveControls`.<br />See [Detective controls service-linked role for AMS Accelerate](using-service-linked-roles.md#slr-deploy-detect-controls). 
  - **Date:** Nov 10, 2022

- **Updated: Access management.**
  - **Description:** Updated subsections with improved instructions. See [Access management in AMS Accelerate](acc-access.md). 
  - **Date:** Nov 10, 2022

- **Updated: Service description.**
  - **Description:** Updated *AMS Patterns* in the RACI matrix. See [Service description](acc-sd.md). 
  - **Date:** Nov 10, 2022

- **Updated: AMS patterns.**
  - **Description:** Customers are responsible for pattern deployments. See [AMS patterns](ams-patterns.md). 
  - **Date:** Nov 10, 2022

- **Updated: Offboarding.**
  - **Description:** Added details of what happens to specific Backup and Monitoring resources during offboarding. See [Offboard from AMS Accelerate](acc-offboard.md). 
  - **Date:** Nov 10, 2022

- **Updated: Patch management..**
  - **Description:** Updated and shortened guidance regarding IAM policies. See [Creating an IAM role for on-demand patching of AMS Accelerate](acc-p-user-access.md). 
  - **Date:** Nov 10, 2022

- **New: links to architecture diagrams.**
  - **Description:** Added links to [ AMS Reference Architecture Diagrams](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf) to various topics. For example, see [Monitoring and event management in AMS Accelerate](acc-mon-event-mgmt.md). 
  - **Date:** Nov 10, 2022

- **New: Operations on Demand offering**
  - **Description:** Added "Landing Zone Accelerator Operations". See [Operations On Demand](ops-on-demand.md).
  - **Date:** Oct 13, 2022

- **Update: Monitoring management. Alerts generate incident reports, not service requests**
  - **Description:** [How monitoring works](how-monitoring-works.md).
  - **Date:** Oct 13, 2022

- **New: Creating a patch maintenance window with an Accelerate-custom CFN template**
  - **Description:** CloudFormation patch window configuration templates. See [Create a patch maintenance window in AMS](acc-p-maint-window.md).
  - **Date:** Sept 15, 2022

- **Updated: Offboarding**
  - **Description:** Emphasized that backup plans in Accelerate no longer work after offboarding. See [Offboard from AMS Accelerate](acc-offboard.md).
  - **Date:** Sept 15, 2022

- **Updated: CloudWatch configuration change details**
  - **Description:** Corrected a mistake in the Windows and Linux examples. See [CloudWatch configuration change details](inst-auto-config-details-cw.md).
  - **Date:** Sept 15, 2022

- **Updated: Using AMS Resource Scheduler**
  - **Description:** Added guidance about Cost Allocation Tags. See [Cost estimator in AMS Resource Scheduler](resource-scheduler-cost-est.md).
  - **Date:** September 15, 2022

- **Updated: AMS Config Rule Library**
  - **Description:** Added two `ams-eks-` config rules to the Table of Rules. See [AMS Config Rule library](acc-sec-compliance.md#acc-sec-compliance-rules).
  - **Date:** September 15, 2022

- **Updated: Backup Management**
  - **Description:** Removed the misleading label PITR (point-in-time-recovery) from backup plan titles and descriptions. See [Select an AMS backup plan](acc-backup-select-plan.md).
  - **Date:** September 15, 2022

- **Updated: Accelerate Service Description**
  - **Description:** Updated descriptions of config rules and canaries. See [Service description](acc-sd.md).
  - **Date:** September 15, 2022

- **Updated: Service Description, Supported Configurations**
  - **Description:** Removed end-of-service date for Windows 2008 R2. Accelerate does not support Windows 2008. See [Supported configurations](acc-sd.md#supported-configs).
  - **Date:** August 11, 2022

- **Updated: Service Description, Roles and Responsibilities**
  - **Description:** Updated the RACI table. Removed ELB access logs from the last row of the Networking section. We do not enable ELB access logs for Accelerate customers. See [Roles and responsibilities](acc-sd.md#acc-sd-responsibilities).
  - **Date:** August 11, 2022

- **Updated: Configuration Compliance**
  - **Description:** Corrected a typo in the Table of Rules, Frameworks column. NIST-CSF was incorrectly listed as NIST-CIS. See [Configuration compliance in Accelerate](acc-sec-compliance.md).
  - **Date:** August 11, 2022

- **New: Accelerate Offboarding**
  - **Description:** Considerations and process for offboarding. See [Offboarding AMS Accelerate](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/what-is-acc.html#acc-offboard).
  - **Date:** August 11, 2022

- **Updated: List of pre-installed SSM agents' operating systems**
  - **Description:** Added "Ubuntu Linux 18.04 and 20.04" to the list. See [Onboarding EC2 instances to Accelerate](acc-get-feature-ec2-onboarding.md).
  - **Date:** August 11, 2022

- **New: Resource Scheduler**
  - **Description:** Use AMS Resource Scheduler to cost optimize by stopping and starting resources only as needed. See [Cost optimization with AMS Resource Scheduler](acc-resource-scheduler.md).
  - **Date:** July 14, 2022

- **Updated: Service Description for Resource Scheduler**
  - **Description:** Several sections of the service description were updated for the new Resource Scheduler offering. See [Service description](acc-sd.md).
  - **Date:** July 14, 2022

- **New: AMS Patterns**
  - **Description:** AMS offers pattern templates, a generalized solution that solves for a family of use cases in the AMS managed environment. First pattern on offer: [AMS patterns](ams-patterns.md).
  - **Date:** July 14, 2022

- **New: Cost optimization note**
  - **Description:** Added a note explaining how costs can increase with resource usage. See [Resource inventory for Accelerate](acc-resource-inventory.md).
  - **Date:** July 14, 2022

- **Updated: AMS Config Rules**
  - **Description:** Reorganized the tables in the [AMS Config Rule library](acc-sec-compliance.md#acc-sec-compliance-rules). The HTML table has fewer columns, to make it easier to read at a glance. The downloadable spreadsheet has additional columns to allow sorting and filtering. 
  - **Date:** July 14, 2022

- **Updated: Access Management**
  - **Description:** Updated the sample CloudFormation template in [Permissions to use AMS features](acc-access-customer.md). The `AMSAccelerateAdminAccess` policy now includes the `AmsResourceSchedulerPassRolePolicy` and `IAMReadOnlyPolicy` policies.
  - **Date:** July 14, 2022

- **Updated: Self-Service Reporting**
  - **Description:** Added instructions for encrypting AWS Glue metadata with KMS keys. See box labeled Important on [Self-service reports](self-service-reporting.md).
  - **Date:** July 14, 2022

- **Updated: AMS baseline monitoring**
  - **Description:** Added DeleteRecoveryPoint backup alert. [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md)
  - **Date:** July 14, 2022

- **Updated: Supported operating systems**
  - **Description:** Added End of Support date for Amazon Linux 2. [Service description](acc-sd.md)
  - **Date:** July 14, 2022

- **Updated: AMS Reporting**
  - **Description:** Added note about Opt-in Regions. [Reports and options](ams-reporting.md)
  - **Date:** July 14, 2022

- **Resource Scheduler**
  - **Description:** Added information about onboarding and using AMS Resource Scheduler to assist in cost optimization by scheduling resource stop and start times. Also, updated the Accelerate service description to include mention of Resource Scheduler. Additionally, updated the Amazon Linux 2 supported end of support date to 2024. See [Cost optimization with AMS Resource Scheduler](acc-resource-scheduler.md) and [Service description](acc-sd.md)
  - **Date:** June 30, 2022

- **New alarm**
  - **Description:** Added a AWS Backup alarm. [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md)
  - **Date:** June 21, 2022

- **New content**
  - **Description:** Added the service-linked role content. [Using service-linked roles for AMS Accelerate](using-service-linked-roles.md) / **Date:** June 16, 2022
  - **Description:** AWS Network Firewall Operations added to Operations on Demand (OOD) catalog of offerings. [Operations On Demand](ops-on-demand.md) / **Date:** June 16, 2022
  - **Description:** Added problem management feature description. [Service description](acc-sd.md) / **Date:** June 16, 2022
  - **Description:** Added note about the set of config rules that does not support in particular opt-in regions. [Configuration compliance in Accelerate](acc-sec-compliance.md) / **Date:** June 16, 2022

- **Updated content**
  - **Description:** Configuration compliance. "AMS Config Rule library" -> "Table of rules", was updated and removed to ZIP only. [Configuration compliance in Accelerate](acc-sec-compliance.md) / **Date:** June 16, 2022
  - **Description:** Removed escalation emails. [Escalation path](acc-escalation-path.md) / **Date:** June 16, 2022
  - **Description:** Moved topic list to below opening paragraphs. [What is AMS Accelerate?](what-is-acc.md) / **Date:** June 16, 2022
  - **Description:** Updated the auto remeditation content. [AMS automatic remediation of alerts](auto-remediation.md) / **Date:** June 16, 2022

- **Updated content: Service Description**
  - **Description:** Added EKS to the list of services monitored by AMS Config Rules in [Supported services](acc-sd.md#acc-supported-services).<br />Updated monitoring description in RACI table in [Roles and responsibilities](acc-sd.md#acc-sd-responsibilities).
  - **Date:** May 12, 2022

- **Updated content: Configuration Compliance**
  - **Description:** Added EKS-related config rules. See [Configuration compliance in Accelerate](acc-sec-compliance.md).
  - **Date:** May 12, 2022

- **Updated content: Getting Started, Account Discovery**
  - **Description:** Added a newer version of the AwsAccountDiscoveryCli script (in the *Account Discovery Changelog zip file*) in [Step 1. Account discovery in Accelerate](acc-acct-disc.md).
  - **Date:** May 12, 2022

- **Updated content: Monitoring, default metrics**
  - **Description:** Updated trigger conditions for ALB-related metrics. See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md). 
  - **Date:** May 12, 2022

- **Updated content: Patching onboarding**
  - **Description:** Added an explicit patching prerequisite: you need to opt-in to EBS. See [Onboarding patching in Accelerate](acc-get-feature-patching-onboarding.md). 
  - **Date:** May 12, 2022

- **Updated content: Accelerate resource inventory table**
  - **Description:** Changed ams-detective-controls-config-rules-cdk rules, added rules for ams-detective-controls-recorder-cdk and ams-detective-controls-infrastructure-cdk. See [Resource inventory for Accelerate](acc-resource-inventory.md). 
  - **Date:** April 14, 2022

- **Updated content: Configuration Compliance**
  - **Description:**  Introduction to industry standards, config rules, and types of responses. Emphasizes that customers do not choose individual config rules or responses. [Configuration compliance in Accelerate](acc-sec-compliance.md). 
  - **Date:** April 14, 2022

- **Updated content: Service Description**
  - **Description:** Moved the existing Scope of Changes section under Roles and Responsibilities. See [Roles and responsibilities](acc-sd.md#acc-sd-responsibilities). 
  - **Date:** April 14, 2022

- **Updated content: Tagging and Monitoring**
  - **Description:** Added `AWS::Synthetics:Canary` to lists of allowed Resource Types for tagging and monitoring. See [Resource Tagger Configuration Profiles in AMS Accelerate](acc-tag-tools-profiles.md) and [Accelerate Configuration profile: pseudoparameter substitution](acc-mem-config-doc-sub.md). 
  - **Date:** April 14, 2022

- **Updated content: Accelerate Prerequisites**
  - **Description:** Added SSM-required bucket permissions to [Amazon EC2 Systems Manager in Accelerate](acc-gs-prereqs.md#acc-gs-prereqs-sysman). 
  - **Date:** April 14, 2022

- **New content: Patching and Monitoring**
  - **Description:** Added sample code to use Cloudformation to deploy tagging and monitoring configurations. See [Deploying a configuration profile with CloudFormation for Accelerate](acc-tag-cf-ex-deploy-config.md) and [Using CloudFormation to deploy Accelerate configuration changes](acc-mem-deploy-change-cfn.md). 
  - **Date:** March 10, 2022

- **Updated content: Patch maintenance console**
  - **Description:** Reordered steps in [Create a maintenance window from the Systems Manager console for AMS Accelerate](acc-p-maint-window-console.md) to match the console interface. 
  - **Date:** March 10, 2022

- **Updated content: Patch maintenance CLI**
  - **Description:** Updated CLI parameters (schedule, duration, and cutoff) for [Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate](acc-p-maint-window-cli.md)
  - **Date:** March 10, 2022

- **New content: Auto Instance Config**
  - **Description:** Added definition of `AMSInstanceProfileBasePolicy` to [IAM permissions change details](inst-auto-config-details-iam.md)
  - **Date:** March 10, 2022

- **New content: Onboarding**
  - **Description:** Added a sample Linux command to [Outbound internet connectivity in Accelerate](acc-gs-prereqs.md#acc-gs-prereqs-ob) 
  - **Date:** March 10, 2022

- **New content: Onboarding**
  - **Description:**  Added a least-privilege option to [The template to create AMS roles](acc-onb-roles.md). 
  - **Date:** March 10, 2022

- **Updated content: Accelerate escalation instructions**
  - **Description:** Added guidance, links, and email contacts to [Escalation path](acc-escalation-path.md)
  - **Date:** March 10, 2022

- **Updated content: Supported Configurations**
  - **Description:** AMS expects to end support for RHEL 6 and CentOs on March 14, 2023. See [Supported configurations](acc-sd.md#supported-configs) 
  - **Date:** March 10, 2022

- **Updated content: Resources table**
  - **Description:** Added **AMS access** IAM roles to [Resource inventory for Accelerate](acc-resource-inventory.md) resources table
  - **Date:** March 10, 2022

- **Updated content: Onboarding and Backup**
  - **Description:** Added instructions for opting in to AWS Backup to [Onboarding AWS Backup in Accelerate](acc-get-feature-backup-onboarding.md) and [Continuity management in AMS Accelerate](acc-backup.md) 
  - **Date:** March 10, 2022

- **Updated content: Access Management**
  - **Description:** Removed Advanced-specific instructions from Accelerate guidance [How and when to use the root user account in AMS](how-when-to-use-root.md).
  - **Date:** March 10, 2022

- **Updated content: Supported Configurations**
  - **Description:**  AMS now supports Oracle Linux 8.3 and Ubuntu 18.04 and 20.04. See [Supported configurations](acc-sd.md#supported-configs). 
  - **Date:** February 28, 2022

- **Updated content: Service Level Agreement**
  - **Description:** Updated the downloadable Service Level Agreement in [Supported services](acc-sd.md#acc-supported-services).
  - **Date:** February 28, 2022

- **Updated content: Access Management**
  - **Description:** Updated [How AMS accesses your account](acc-access-operator.md) with FAQs for AMS operator console roles and a warning not to modify or delete them.
  - **Date:** February 28, 2022

- **Updated content: Alarm Manager**
  - **Description:** Updated [Accelerate Configuration profile: monitoring](acc-mem-config-doc-format.md). Alarm Manager is no longer limited to single-metric alarms.
  - **Date:** February 28, 2022

- **Updated content: Getting Started**
  - **Description:** Updated [Step 2. Onboarding management resources in Accelerate](acc-get-mgmt-resource-onboard.md). Added an IAM role with minimal access for onboarding resources.
  - **Date:** February 28, 2022

- **New content: Scope of Changes in Service Description**
  - **Description:** Added a new section,[Scope of changes performed by AMS Accelerate](acc-sd.md#acc-scope-changes) that emphasizes boundaries and actions that AMS Accelerate does not perform.
  - **Date:** February 10, 2022

- **Updated content: Getting Started**
  - **Description:** New onboarding process starts with setting up default features and configurations before customizing. Subsections contain feature-specific goals and related links. See [Getting Started with AMS Accelerate](getting-started-acc.md).
  - **Date:** February 10, 2022

- **Updated content: AMS Backup Management.**
  - **Description:** Shortened and reorganized the [Continuity management in AMS Accelerate](acc-backup.md) chapter for readability.
  - **Date:** February 10, 2022

- **Updated content: Tagging**
  - **Description:** Added a Tagging Tools section to accommodate code samples for CloudFormation and other tools. See [Tagging in AMS Accelerate](acc-tagging.md).
  - **Date:** February 10, 2022

- **Updated content: Baseline Monitoring**
  - **Description:** Improved trigger condition for RedShift cluster alarm reduces false alarms during maintenance. See [Alerts from baseline monitoring in AMS](monitoring-default-metrics.md).
  - **Date:** February 10, 2022

- **Updated content: Patching**
  - **Description:** Updated sample CLI command to register a maintenance window. See [Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate](acc-p-maint-window-cli.md).
  - **Date:** February 10, 2022

- **Updated content: AWS Config Rules Inventory.**
  - **Description:** Removed deprecated config rule `ams-nist-cis-ec2-security-group-attached-to-eni` from the AWS Config Rules Inventory table. See [Table of Rules](acc-sec-compliance.md#acc-sec-config-rules-inventory).
  - **Date:** January 27, 2022

- **New content: Creating patch maintenance windows.**
  - **Description:** Added a link to the [ SSM tutorial](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-create.html) and sample commands for creating patch maintenance windows from the command line. See [Create a maintenance window with the Systems Manager command line interface (CLI) for AMS Accelerate](acc-p-maint-window-cli.md).
  - **Date:** January 27, 2022

- **New content: Resource Tagger recognizes new Auto Scaling Groups (ASG) resource type.**
  - **Description:** Added Auto Scaling Groups to the resource types filterable with Resource Tagger configuration profiles. See [Syntax and structure](acc-tag-tools-profiles.md#acc-rt-config-doc-format).
  - **Date:** January 13, 2022

- **New content: Additional backup plans and vaults.**
  - **Description:** Added new backup plans and vaults to mitigate high-risk scenarios including ransomware attacks. See [View backups in AMS vaults](acc-backup-ams-vaults.md) and [View backups in AMS vaults](acc-backup-ams-vaults.md).
  - **Date:** January 13, 2022


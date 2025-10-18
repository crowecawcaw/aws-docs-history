# Monitor across accounts and
 Regions

To enable unified monitoring across accounts, CloudWatch offers the following features:


* **[CloudWatch
 cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md")**– facilitate
 observability within a single Region with the Observability Access Manager (OAM)
 service. You can link accounts and easily view metrics, logs, traces, and other
 telemetry between accounts. This helps you to unify observability in central
 monitoring accounts that view telemetry shared from source accounts, and operate on
 this shared telemetry as if it were native to the monitoring account.
* **[Cross-account
 cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md")**– delivers a console
 experience that allows you to view dashboards, metrics, and alarms consoles of other
 accounts across Regions by toggling between accounts. After you set up the necessary
 permissions, you use an account selector integrated into the alarms, dashboards, and
 metrics consoles to view metrics, dashboards, and alarms in other accounts without
 having to log in and out of the accounts. By enabling this feature, you can also set
 up dashboards that contain cross-account cross-Region metrics for centralized
 visibility within an account.
* **[Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html")**–
 collects copies of log data from multiple member accounts into one data repository
 using cross-account and cross-region centralization rules. You define the rules that
 automatically replicate log data from multiple accounts and AWS Regions into a
 centralized account within your organization. This capability streamlines log
 consolidation for improved centralized monitoring, analysis, and compliance across
 your entire AWSinfrastructure.
These three features are complementary to each other and can be used independently or
 together. See the following table for a comparison of the features. We recommend that you
 use CloudWatch cross-account observability for the richest cross-account observability and
 discovery experience within a Region for your metrics, logs, and traces. 



|  | **[CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md")** | **[Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md")** | **[Cross-account cross-Region log centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html")** |
| --- | --- | --- | --- |
| **What is it?** | Unified access to underlying telemetry and other observability resources across multiple accounts. After this is configured, observability resources are seamlessly viewable between accounts, eliminating the need for role assumptions. The central monitoring account gains direct access to the telemetry data and resources from source accounts, streamlining the monitoring and observability process. | A designated monitoring account assume a **CrossAccountSharingRole** defined in source accounts from the CloudWatch console. By assuming this role, the monitoring account can invoke operations such as dashboard viewing on behalf of source accounts, directly from its console.  | Amazon CloudWatch Logs data centralization capability streamlines log consolidation for improved centralized monitoring, analysis, and compliance across your entire AWS infrastructure.  |
| **How does it work?** | A monitoring account, using the Observability Access Monitoring service, creates a *sink* and attaches a sink policy to it. The sink policy defines which resources they would like to view and which source accounts should share them. Then source accounts can create a link to the monitoring account sink, establishing what they actually want to share. After the link is created, the specified resources are visible in the monitoring account. | A source account initiates the configuration by setting up a **CrossAccountSharingRole**, allowing a monitoring account to run operations in the source account. Then, a monitoring account enables the cross-account cross-Region selector in the console by specifying the source account ID. This enables the monitoring account to be able to switch into the source account. When switching, the CloudWatch console checks for the existence of a service-linked role that allows CloudWatch to assume the **CrossAccountSharingRole** that was created in the source account. | Amazon CloudWatch Logs data centralization works with AWS Organizations to copy log data from multiple member accounts into one data repository using cross-account and cross-region centralization rules. You define the rules that automatically replicate log data from multiple accounts and AWS Regions into a centralized account within your organization.  |
| **What telemetry is supported?** | <br>• Metrics <br>• Traces <br>• Logs | <br>• Metrics <br>• Traces | <br>• Logs |
| **What functionality is supported?** | <br>• Dashboarding <br>• Alarms <br>• Metrics Insights <br>• Outlier Detection <br>• CloudWatch Logs insights <br>• Application Insights <br>• Other functionalities. For more details see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md"). | <br>• Console switching between accounts and Regions in metrics, alarms, and traces consoles. <br>• Custom dashboards with metrics and alarms from other accounts and Regions For more details, see [Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md"). | CloudWatch Logs InsightsSubscription filtersMetric filters |
| **How many accounts can I use it with?** | A monitoring account can see resources from as many as 100,000 source accounts at the same time. A source account can share their resources with as many as five different monitoring accounts. | By using the cross-account cross-Region selector in the console, a monitoring account can switch to one other account at a time but there is no limit on the number of accounts that can be linked. When defining cross-account dashboards and alarms, many source accounts can be referenced. | Works with AWS Organizations supported number of accounts |
| **Does it move telemetry data?** | No. Resources are shared between accounts with the exception of copied traces. | No. An IAM policy is configured to allow embedded account switching for cross-account cross-Region resource visibility. | Yes |
| **How much does it cost?** | No extra charges for shared logs and metrics, and the first trace copy is free. For more information about pricing, see [Amazon CloudWatch pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing"). | No additional charges for cross-account or cross-Region actions. | You can centralize one copy of logs for free. Additional copies are charged at $0.05/GB of logs centralized (the backup region feature is considered an additional copy). For information about storage cost pricing in the destination account and other value-added experiences see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). |
| **Does it support observability across Regions?** | No | Yes | Yes, you can centralize data across Regions. |
| **Does it support programmatic access?** | Yes. the AWS CLI, AWS Cloud Development Kit (AWS CDK), and APIs are supported. | No | Yes |
| **Does it support programmatic setup?** | Yes | Yes | Yes |
| **Does it support AWS Organizations?** | Yes | Yes | Yes. AWS Organizations is required to use this feature. | ###### Topics <br>• [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md") <br>• [Cross-account cross-Region CloudWatch console](Cross-Account-Cross-Region.md "Cross-Account-Cross-Region.md")

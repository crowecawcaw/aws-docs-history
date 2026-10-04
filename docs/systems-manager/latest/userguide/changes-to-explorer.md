

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Changes to AWS Systems Manager Explorer
<a name="changes-to-explorer"></a>

Where you view operational data (OpsData) in AWS Systems Manager is changing. Starting December 31, 2026, the Explorer dashboard is no longer part of the Systems Manager console. You continue to view the same OpsData in the console of the AWS service or Systems Manager tool that produces it.

Only the dashboard changes. None of your OpsData is deleted, and how Systems Manager collects it stays the same. Explorer displays data that Systems Manager tools and other AWS services collect and store, so that data remains where it is today. Your resource data syncs continue to aggregate OpsData across your AWS accounts and AWS Regions, and every Systems Manager API operation that Explorer uses, including `GetOpsSummary`, continues to be supported in the AWS CLI and the AWS SDKs.

Use the following sections to find where each of your Explorer views is available, and to review answers to common questions about this change.

## Where to find each of your Explorer views
<a name="changes-to-explorer-views"></a>

Explorer has multiple widgets that provide operational data. The following table shows where the data in each widget is available. Some alternatives require setup before they display data for multiple AWS accounts and AWS Regions.



| Explorer widget or view | Where to find this data | What you need to know | 
| --- | --- | --- | 
| **Managed instances**, **Instance count**, **Instances by AMI** | Systems Manager console, **Review node insights** and **Explore nodes** pages | These pages aggregate node details for your organization or account. For more information, see [Reviewing node insights](review-node-insights.md) and [Exploring nodes](view-aggregated-node-details.md).<br />These pages require the Systems Manager unified console. To learn more about the AWS Regions where the unified console is available, see [Supported AWS Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html#regions). In other Regions, use Fleet Manager or the Systems Manager API to list your managed nodes. | 
| **Total noncompliant nodes** (patching) | Patch Manager console, **Dashboard** tab | Patch Manager presents this data differently than Explorer does. Instead of the timeline that the Explorer widget displays, the **Dashboard** tab shows counts of compliant and noncompliant managed nodes, and a patch compliance report for the past 7 days. For more information, see [Viewing patch Dashboard summaries](patch-manager-view-dashboard-summaries.md). | 
| **Noncompliant associations** (desired state compliance) | Systems Manager console, **Compliance** page, and State Manager console | For more information, see [AWS Systems Manager Compliance](systems-manager-compliance.md) and [AWS Systems Manager State Manager](systems-manager-state.md). If you use Quick Setup to create associations, you can also review status for each configuration in the Quick Setup console. For more information, see [AWS Systems Manager Quick Setup](systems-manager-quick-setup.md). | 
| **AWS Trusted Advisor** | AWS Trusted Advisor console | You must have a Business or Enterprise Support plan. The AWS Trusted Advisor console shows checks for the current account. To review checks across an organization, turn on the organizational view and generate a report. For more information, see [Organizational view for Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/organizational-view.html). | 
| **AWS Config compliance** | AWS Config console | To review compliance for multiple accounts and Regions, create an aggregator in AWS Config. For more information, see [Creating an aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregated-create.html). | 
| **AWS Security Hub CSPM findings** | AWS Security Hub CSPM console | To review findings for multiple accounts and Regions, turn on central configuration in Security Hub CSPM. For more information, see [Starting central configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/start-central-configuration.html). | 
| **AWS Compute Optimizer** | AWS Compute Optimizer console | Opt in for your account or your organization. Compute Optimizer aggregates findings for under-provisioned resources, and lists over-provisioned resources per resource type rather than as a single aggregated view. For more information, see [Opting in your account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html). | 
| **Support Center cases** | AWS Support Support Center | Support Center shows active cases and case history for the current account. It doesn't provide a view of cases across multiple accounts. To build one, see [Create a comprehensive view of AWS support cases with Amazon QuickSight](https://aws.amazon.com/blogs/business-intelligence/create-a-comprehensive-view-of-aws-support-cases-with-amazon-quicksight/). | 
| **Open OpsItem summary**, **OpsItems by status**, **OpsItems by severity**, **OpsItems over time** | OpsCenter console | The OpsCenter console provides information about your OpsItems. For more information, see [AWS Systems Manager OpsCenter](OpsCenter.md). | 
| **Export OpsData to Amazon S3 bucket** | Systems Manager Automation console, or the AWS CLI | Explorer uses the AWS-ExportOpsDataToS3 runbook to export OpsData. You can continue to run this runbook directly from the Automation console or the AWS CLI. For more information, see [AWS-ExportOpsDataToS3](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-exportopsdatatos3.html). | 

The aggregated counts that Explorer widgets display are returned by the [GetOpsSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html) API operation. You can call `GetOpsSummary` with the AWS CLI, an AWS SDK, or the Systems Manager API to build your own reports, including for the accounts and Regions covered by a resource data sync.

You can also build your own visualization of this data. For an example that combines an Explorer resource data sync, the AWS-ExportOpsDataToS3 runbook, and Amazon Quick Sight to chart Support cases across the accounts in an organization, see [Create a comprehensive view of AWS support cases with Amazon QuickSight](https://aws.amazon.com/blogs/business-intelligence/create-a-comprehensive-view-of-aws-support-cases-with-amazon-quicksight/).

Resource data syncs that you already created continue to aggregate OpsData for your accounts and Regions. Resource data sync management in the console will move to OpsCenter. You can manage them with the Systems Manager API by using the [CreateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateResourceDataSync.html), [ListResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceDataSync.html), [UpdateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateResourceDataSync.html), and [DeleteResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourceDataSync.html) API operations.

## Frequently asked questions
<a name="changes-to-explorer-faq"></a>

**Is my OpsData deleted when Explorer is discontinued?**  
No. Explorer displays data that other AWS services and Systems Manager tools collect and store. That data remains in those services, and remains available through their consoles and APIs.

**Are any API operations being removed?**  
No. This change affects the console experience only. The API operations that Explorer uses, including `GetOpsSummary` and the resource data sync operations, continue to be available.

**Do I need to delete or re-create my resource data syncs?**  
No. Your existing resource data syncs continue to work, and you can manage them with the Systems Manager API.

**Can I still view data for multiple accounts and Regions?**  
In most cases, yes, but the setup and the level of aggregation depend on the service. Review the **What you need to know** column in [Where to find each of your Explorer views](#changes-to-explorer-views) for the data sources you use.

If you have additional questions, contact us through the [AWS Support Center](https://console.aws.amazon.com/support).
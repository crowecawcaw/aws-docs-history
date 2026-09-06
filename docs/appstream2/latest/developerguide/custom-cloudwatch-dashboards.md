

# Create custom CloudWatch dashboards using CloudFormation templates
<a name="custom-cloudwatch-dashboards"></a>

AWS provides CloudFormation templates that you can use to create custom CloudWatch dashboards for WorkSpaces Applications. Choose from the following CloudFormation template options to create custom dashboards for your WorkSpaces Applications workloads in the CloudFormation console.

**Considerations before getting started**  
Consider the following before you get started with custom CloudWatch dashboards:
+ Create your dashboards in the same AWS Region as the deployed WorkSpaces you want to monitor.
+ You can also create custom dashboards using the CloudWatch console.
+ A cost might be associated with custom CloudWatch dashboards. For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Prerequisites**  
Before you begin, ensure you have access to the AWS Management Console and appropriate permissions to create CloudFormation stacks and CloudWatch dashboards.

**Procedure**  
This procedure covers three CloudFormation templates for monitoring WorkSpaces Applications fleets: the Fleet Dashboard for fleet-level health metrics with drill-down capabilities, the User Dashboard for individual user session experience troubleshooting, and the Fleet Performance Alerts template for automated email notifications when performance thresholds are breached.

**Fleet Dashboard Template**  
The Fleet Dashboard gives administrators a drill-down view of a specific fleet's health. A Fleet dropdown at the top auto-populates with all fleets in the account, shows metrics for each fleet and instances associated to that fleet.

**Steps to create:**

1. [Open the Create Stack page in the CloudFormation console.](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=WorkSpacesApps-FleetDashboard&templateURL=https://cfn-templates-global-prod-iad.s3.us-east-1.amazonaws.com/cfn-templates/ws_apps_fleet_dashboard.yaml) This link opens the page with the Amazon S3 bucket location of the custom CloudWatch dashboard template pre-populated.

1. Review the default selections on the **Create stack** page, and choose **Next**.

1. On the **Specify stack details** page, do the following:

   1. In the **Stack name** field, use the default name or enter a custom name for your stack.

   1. In the **DashboardName** field, use the default name or enter a custom name for your dashboard.

   1. Choose **Next**.

1. On the **Configure stack options** page, review the default selections, and choose **Next**.

1. On the **Review** page, scroll down to the **Transforms** section and select the acknowledgement checkboxes to confirm that CloudFormation might create IAM resources.

1. Choose **Submit** to create the stack and the custom CloudWatch dashboard.

1. After the stack creation is complete, open the CloudWatch console to view your newly created custom dashboard.

   1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

   1. In the left navigation bar, choose **Dashboards**.

   1. Under **Custom Dashboards**, choose the dashboard with the dashboard name you entered earlier in this procedure.

**User Dashboard Template**  
The User Dashboard allows administrators to troubleshoot individual user experience. A UserId dropdown at the top auto-populates with all user IDs from CloudWatch metrics, shows metrics for each User.

**Steps to create:**

1. [Open the Create Stack page in the CloudFormation console.](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=WorkSpacesApps-UserDashboard&templateURL=https://cfn-templates-global-prod-iad.s3.us-east-1.amazonaws.com/cfn-templates/ws_apps_user_dashboard.yaml) This link opens the page with the Amazon S3 bucket location of the custom CloudWatch dashboard template pre-populated.

1. Review the default selections on the **Create stack** page, and choose **Next**.

1. On the **Specify stack details** page, do the following:

   1. In the **Stack name** field, use the default name or enter a custom name for your stack.

   1. In the **DashboardName** field, use the default name or enter a custom name for your dashboard.

   1. Choose **Next**.

1. On the **Configure stack options** page, review the default selections, and choose **Next**.

1. On the **Review** page, scroll down to the **Transforms** section and select the acknowledgement checkboxes to confirm that CloudFormation might create IAM resources.

1. Choose **Submit** to create the stack and the custom CloudWatch dashboard.

1. After the stack creation is complete, open the CloudWatch console to view your newly created custom dashboard.

   1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

   1. In the left navigation bar, choose **Dashboards**.

   1. Under **Custom Dashboards**, choose the dashboard with the dashboard name you entered earlier in this procedure.

**Fleet Performance Alerts Template**  
This template creates 6 CloudWatch alarms for a specific fleet and an Amazon SNS topic that sends email notifications when alarms trigger or recover. After deployment, the administrator will receive a confirmation email from Amazon SNS — they must confirm the subscription to start receiving alerts.

**Steps to create:**

1. [Open the Create Stack page in the CloudFormation console.](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=WorkSpacesApps-FleetAlarms&templateURL=https://cfn-templates-global-prod-iad.s3.us-east-1.amazonaws.com/cfn-templates/ws_apps_fleet_level_alarms_template.yaml) This link opens the page with the Amazon S3 bucket location of the custom CloudWatch dashboard template pre-populated.

1. Review the default selections on the **Create stack** page, and choose **Next**.

1. On the **Specify stack details** page, do the following:

   1. In the **Stack name** field, use the default name or enter a custom name for your stack.

   1. In the **FleetName** field, enter the Fleet name that you want alerting for.

   1. In the **NotificationEmail** field, enter an email address through which you want to get notified.

   1. Choose **Next**.

1. On the **Configure stack options** page, review the default selections, and choose **Next**.

1. On the **Review** page, scroll down to the **Transforms** section and select the acknowledgement checkboxes to confirm that CloudFormation might create IAM resources.

1. Choose **Submit** to create the stack and the custom CloudWatch dashboard.

1. After the stack creation is complete, open the CloudWatch console to view your newly created custom dashboard.

   1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

   1. In the left navigation bar, choose **Dashboards**.

   1. Under **Custom Dashboards**, choose the dashboard with the dashboard name you entered earlier in this procedure.

**Next steps**  
After creating your dashboard, you can customize it further by adding or removing widgets, adjusting time ranges, and configuring alarms as needed.
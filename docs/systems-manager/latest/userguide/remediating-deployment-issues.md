

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Diagnosing and remediating failed deployments
<a name="remediating-deployment-issues"></a>

Systems Manager can diagnose and then help you remediate the following types of failed deployments:
+ Core setup for organization member accounts
+ Core setup for delegated administrator account
+ Core setup for your account

Use the following procedure to attempt to remediate these types of issues.

**To diagnose and remediate failed deployments**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Diagnose and remediate**.

1. Choose the **Deployment issues** tab.

1. In the **Failed deployments** section, review the list of findings for failed deployments.

1. In the **Setup step** column, choose the name of a finding to review additional details about the issue. For example: **Core setup for organization member accounts**.

1. In the detail page for that failed deployment, you can view a list of accounts and how many Regions in each have experienced deployment failures. 

1. Select an account ID to view information about the reason for failures in that account.

1. In the **Failed Regions** area, examine the information provided for **Status reason**. This information can indicate a reason for the failed deployment, which might provide insight into configuration changes that need to be made. 

1. If you want to retry the deployment without making configuration changes, choose **Redeploy**.
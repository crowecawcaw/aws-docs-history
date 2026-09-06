

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Implement change controls for Automation
<a name="automation-change-calendar-integration"></a>

By default, Automation lets you use runbooks without date and time constraints. By integrating Automation with Change Calendar, you can implement change controls to all automations in your AWS account. With this setting, AWS Identity and Access Management (IAM) principals in your account can only run automations during allowed time periods. To learn more about working with Change Calendar, see [Working with Change Calendar](systems-manager-change-calendar-working.md).

**To turn on change controls (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**.

1. Choose the **Preferences** tab, and then choose **Edit**.

1. Select the check box next to **Turn on Change Calendar integration**.

1. In the **Choose a change calendar** dropdown list, choose the change calendar that you want Automation to follow.

1. Choose **Save**.
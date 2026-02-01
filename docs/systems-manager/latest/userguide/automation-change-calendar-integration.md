• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Implement change controls

for Automation

By default, Automation allows you to use runbooks without date and time
constraints. By integrating Automation with Change Calendar, you can implement change
controls to all automations in your AWS account. With this setting, AWS Identity and Access Management
(IAM) principals in your account can only run automations during the time periods
allowed by your change calendar. To learn more about working with Change Calendar, see
[Working with Change Calendar](systems-manager-change-calendar-working.md "systems-manager-change-calendar-working.md").

###### To turn on change controls (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Automation**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Turn on Change Calendar
   integration**.
5. In the **Choose a change calendar** dropdown list, choose
   the change calendar that you want Automation to follow.
6. Choose **Save**.

• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Sharing a change calendar

You can share a calendar in Change Calendar, a tool in AWS Systems Manager, with other
AWS accounts by using the AWS Systems Manager console. When you share a calendar, the
calendar is read-only to users in the shared account. Maintenance windows, State Manager
associations, and automations aren't shared.

###### To share a change calendar

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Change Calendar**.
3. In the list of calendars, choose the name of the calendar that you want to
   share.
4. On the calendar's details page, choose the **Sharing**
   tab.
5. Choose **Actions, Share**.
6. In **Share calendar**, for **Account
   ID**, enter the ID number of a valid AWS account, and then
   choose **Share**.

Users of the shared account can read the change calendar, but they can't
make changes.

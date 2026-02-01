• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Deregister

an Explorer delegated administrator

Use the following procedure to deregister an Explorer delegated administrator.
A delegated administrator account can only be deregistered by the AWS Organizations
management account. When a delegated administrator account is deregistered, the
system deletes all AWS Organizations resource data syncs created by the delegated
administrator.

###### To deregister an Explorer delegated administrator

1. Log into your AWS Organizations management account.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. In the navigation pane, choose **Explorer**.
4. Choose **Settings**.
5. In the **Delegated administrator for Explorer**
   section, choose **Deregister**. The system displays a
   warning.
6. Enter the account ID and choose **Remove**.
   The account no longer has access to the AWS Organizations resource data sync API
   operations. The system deletes all AWS Organizations resource data syncs created by the
   account.

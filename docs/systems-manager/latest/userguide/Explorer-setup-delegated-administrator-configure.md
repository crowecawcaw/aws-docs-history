• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Configure

an Explorer delegated administrator

Use the following procedure to register an Explorer delegated
administrator.

###### To register an Explorer delegated administrator

1. Log into your AWS Organizations management account.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. In the navigation pane, choose **Explorer**.
4. Choose **Settings**.
5. In the **Delegated administrator for Explorer**
   section, verify that you have configured the required service-linked
   role and service access options. If necessary, choose the
   **Create role** and **Enable
   access** buttons to configure these options.
6. For **Account ID**, enter the AWS account ID. This
   account must be a member account in AWS Organizations.
7. Choose **Register delegated administrator**.
   The delegated administrator now has access to the **Include all
   accounts from my AWS Organizations configuration** and **Select
   organization units in AWS Organizations** options on the **Create
   resource data sync** page.

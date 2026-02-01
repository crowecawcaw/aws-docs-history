• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Register a delegated

administrator for Quick Setup

Use the following procedure to register a delegated administrator for
Quick Setup.

###### To register a Quick Setup delegated administrator

1. Log into your AWS Organizations management account.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. In the navigation pane, choose **Quick Setup**.
4. Choose **Settings**.
5. In the **Delegated administrator for Quick Setup** section,
   verify that you have configured the required service-linked role and service
   access options. If necessary, choose the **Create role**
   and **Enable access** buttons to configure these
   options.
6. For **Account ID**, enter the AWS account ID. This
   account must be a member account in AWS Organizations.
7. Choose **Register delegated administrator**.

• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Specify maximum session

duration

Session Manager, a tool in AWS Systems Manager, allows you to specify the maximum duration of a
session before it ends. By default, sessions do not have a maximum duration. The
value you specify for maximum session duration must be between 1 and 1,440
minutes.

###### To specify maximum session duration (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Enable maximum session
   duration**.
5. Specify the maximum duration of session before it ends in the
   **minutes** field under **Maximum session
   duration**.
6. Choose **Save**.

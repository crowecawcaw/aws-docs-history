• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Logging session data using

Amazon CloudWatch Logs (console)

With Amazon CloudWatch Logs, you can monitor, store, and access log files from various
AWS services. You can send session log data to a CloudWatch Logs log group for debugging and
troubleshooting purposes. The default option is for log data to be sent with
encryption using your KMS key, but you can send the data to your log group with or
without encryption.

Follow these steps to configure AWS Systems Manager Session Manager to send session log data to a
CloudWatch Logs log group at the end of your sessions.

###### Note

You can also use the AWS CLI to specify or change the CloudWatch Logs log group that
session data is sent to. For information, see [Update Session Manager
preferences (command line)](getting-started-configure-preferences-cli.md "getting-started-configure-preferences-cli.md").

###### To log session data using Amazon CloudWatch Logs (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Enable** under
   **CloudWatch logging**.
5. Choose the **Upload session logs** option.
6. (Recommended) Select the check box next to **Allow only encrypted
   CloudWatch log groups**. With this option turned on, log data
   is encrypted using the server-side encryption key specified for the log
   group. If you don't want to encrypt the log data that is sent to CloudWatch Logs,
   clear the check box. You must also clear the check box if encryption isn't
   allowed on the log group.
7. For **CloudWatch logs**, to specify the existing CloudWatch Logs log
   group in your AWS account to upload session logs to, select one of the
   following:
   - **Choose a log group from the list**: Select a
     log group that has already been created in your account to store
     session log data.
   - **Enter a log group name in the text box**: Enter
     the name of a log group that has already been created in your
     account to store session log data.

8. Choose **Save**.
   For more information about working with CloudWatch Logs, see the
   _[Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md")_.

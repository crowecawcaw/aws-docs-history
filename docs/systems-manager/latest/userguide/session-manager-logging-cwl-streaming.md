• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Streaming session data using

Amazon CloudWatch Logs (console)

You can send a continual stream of session data logs to Amazon CloudWatch Logs. Essential
details, such as the commands a user has run in a session, the ID of the user who
ran the commands, and timestamps for when the session data is streamed to CloudWatch Logs, are
included when streaming session data. When streaming session data, the logs are
JSON-formatted to help you integrate with your existing logging solutions. Streaming
session data isn't supported for interactive commands.

###### Note

To stream session data from Windows Server managed nodes, you must have
PowerShell 5.1 or later installed. By default, Windows Server 2016
and later have the required PowerShell version installed.
However, Windows Server 2012 and 2012 R2 don't have the required
PowerShell version installed by default. If you haven't
already updated PowerShell on your Windows Server 2012 or 2012 R2
managed nodes, you can do so using Run Command. For information about updating
PowerShell using Run Command, see [Updating PowerShell using
Run Command](run-command-tutorial-update-software.md#rc-console-pwshexample "run-command-tutorial-update-software.md#rc-console-pwshexample").

###### Important

If you have the **PowerShell Transcription** policy setting
configured on your Windows Server managed nodes, you won't be able to stream session
data.

###### To stream session data using Amazon CloudWatch Logs (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Enable** under
   **CloudWatch logging**.
5. Choose the **Stream session logs** option.
6. (Recommended) Select the check box next to **Allow only encrypted
   CloudWatch log groups**. With this option turned on, log data
   is encrypted using the server-side encryption key specified for the log
   group. If you don't want to encrypt the log data that is sent to CloudWatch Logs,
   clear the check box. You must also clear the check box if encryption isn't
   allowed on the log group.
7. For **CloudWatch logs**, to specify the existing CloudWatch Logs log
   group in your AWS account to upload session logs to, select one of the
   following:
   - Enter the name of a log group in the text box that has already
     been created in your account to store session log data.
   - **Browse log groups**: Select a log group that
     has already been created in your account to store session log
     data.

8. Choose **Save**.

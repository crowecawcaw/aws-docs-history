• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Working with Session Manager

You can use the AWS Systems Manager console, the Amazon Elastic Compute Cloud (Amazon EC2) console, or the AWS Command Line Interface
(AWS CLI) to start sessions that connect you to the managed nodes your system
administrator has granted you access to using AWS Identity and Access Management (IAM) policies. Depending on
your permissions, you can also view information about sessions, resume inactive sessions
that haven't timed out, and end sessions. After a session is established, it is not
affected by IAM role session duration. For information about limiting session duration
with Session Manager, see [Specify an idle session timeout
value](session-preferences-timeout.md "session-preferences-timeout.md") and [Specify maximum session
duration](session-preferences-max-timeout.md "session-preferences-max-timeout.md").

For more information about sessions, see [What is a session?](session-manager.md#what-is-a-session "session-manager.md#what-is-a-session")

###### Topics

- [Install the Session Manager plugin
  for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md")
- [Start a
  session](session-manager-working-with-sessions-start.md "session-manager-working-with-sessions-start.md")
- [End a session](session-manager-working-with-sessions-end.md "session-manager-working-with-sessions-end.md")
- [View session
  history](session-manager-working-with-view-history.md "session-manager-working-with-view-history.md")

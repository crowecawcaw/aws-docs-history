• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Enabling and disabling session logging

Session logging records information about current and completed sessions in the Systems Manager
console. You can also log details about commands run during sessions in your
AWS account. Session logging enables you to do the following:

- Create and store session logs for archival purposes.
- Generate a report showing details of every connection made to your managed
  nodes using Session Manager over the past 30 days.
- Generate notifications for session logging in your AWS account, such as
  Amazon Simple Notification Service (Amazon SNS) notifications.
- Automatically initiate another action on an AWS resource as the result of
  actions performed during a session, such as running an AWS Lambda function,
  starting an AWS CodePipeline pipeline, or running an AWS Systems Manager Run Command
  document.

###### Important

Note the following requirements and limitations for Session Manager:

- Session Manager logs the commands you enter and their output during a session
  depending on your session preferences. To prevent sensitive data, such as
  passwords, from being viewed in your session logs we recommend using the
  following commands when entering sensitive data during a session.

Linux & macOS

```
stty -echo; read passwd; stty echo;
```

Windows

```
$Passwd = Read-Host -AsSecureString
```

- If you're using Windows Server 2012 or earlier, the data in your logs might not
  be formatted optimally. We recommend using Windows Server 2012 R2 and later for
  optimal log formats.
- If you're using Linux or macOS managed nodes, ensure that
  the screen utility is installed. If it isn't,
  your log data might be truncated. On Amazon Linux 2, AL2023 and Ubuntu Server, the
  screen utility is installed by default. To
  install screen manually, depending on your
  version of Linux, run either `sudo yum install
screen` or `sudo apt-get install screen`.
- Logging isn't available for Session Manager sessions that connect through port forwarding or
  SSH. This is because SSH encrypts all session data within the secure TLS connection established between the AWS CLI
  and Session Manager endpoints, and Session Manager only serves as a tunnel for
  SSH connections.
  For more information about the permissions required to use Amazon S3 or Amazon CloudWatch Logs for
  logging session data, see [Creating an IAM
  role with permissions for Session Manager and Amazon S3 and CloudWatch Logs (console)](getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging "getting-started-create-iam-instance-profile.md#create-iam-instance-profile-ssn-logging").

Refer to the following topics for more information about logging options for
Session Manager.

###### Topics

- [Streaming session data using
  Amazon CloudWatch Logs (console)](session-manager-logging-cwl-streaming.md "session-manager-logging-cwl-streaming.md")
- [Logging session data using Amazon S3
  (console)](session-manager-logging-s3.md "session-manager-logging-s3.md")
- [Logging session data using
  Amazon CloudWatch Logs (console)](session-manager-logging-cloudwatch-logs.md "session-manager-logging-cloudwatch-logs.md")
- [Configuring session logging to
  disk](session-manager-logging-disk.md "session-manager-logging-disk.md")
- [Adjusting how long the
  Session Manager temporary log file is stored on disk](session-manager-logging-disk-retention.md "session-manager-logging-disk-retention.md")
- [Disabling Session Manager
  logging in CloudWatch Logs and Amazon S3](session-manager-enable-and-disable-logging.md "session-manager-enable-and-disable-logging.md")

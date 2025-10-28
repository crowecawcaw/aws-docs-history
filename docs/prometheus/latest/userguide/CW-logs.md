# Monitor Amazon Managed Service for Prometheus events with CloudWatch Logs

Amazon Managed Service for Prometheus logs Alert Manager and Ruler error and warning events in log groups in
Amazon CloudWatch Logs. For more information about Alert Manager and Rulers, see [Alert Manager](AMP-alert-manager.md "AMP-alert-manager.md") topic in this guide. You can publish the workspace logs data
to log streams in CloudWatch Logs. You can configure the logs that you wish to monitor in the
Amazon Managed Service for Prometheus console or by using the AWS CLI. You can view or query these logs in the CloudWatch
console. For more information about viewing CloudWatch Logs log streams in the console, see [Working with log groups and log streams in CloudWatch](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the CloudWatch user
guide.

The CloudWatch free tier allows up to 5Gb of logs to be published in CloudWatch Logs. The logs that
exceed the free tier allowance will be charged based on the [CloudWatch pricing plan](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Configuring CloudWatch Logs](#CW-logs-config "#CW-logs-config")

## Configuring CloudWatch Logs

Amazon Managed Service for Prometheus logs Alert Manager and Ruler error and warning events in log groups in
Amazon CloudWatch Logs.

You can set CloudWatch Logs logging configuration in Amazon Managed Service for Prometheus console or in the AWS CLI by
calling the `create-logging-configuration` API request.

**Prerequisites**

Before calling `create-logging-configuration`, attach the following
policy or equivalent permissions to the ID or role you will use to configure
CloudWatch Logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups",
 "aps:CreateLoggingConfiguration",
 "aps:UpdateLoggingConfiguration",
 "aps:DescribeLoggingConfiguration",
 "aps:DeleteLoggingConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

**To configure CloudWatch Logs**

You can configure logging in Amazon Managed Service for Prometheus using either the AWS console or the
AWS CLI.

Console
To configure logging in Amazon Managed Service for Prometheus console

1. Navigate to the **Logs** tab in your
   workspace details panel.
2. Choose **Manage logs** on the upper right
   side of the **Logs** panel.
3. Choose **all** in the **Log
   level** dropdown list.
4. Choose the log group that you want to publish your logs to in
   the **Log Group** dropdown list.

You can also create a new log group in CloudWatch console. 5. Choose **Save changes**.

AWS CLI
You can set logging configuration using the AWS CLI.

To configure logging using the AWS CLI

- Using the AWS CLI, run the following command.

```
aws amp create-logging-configuration --workspace-id `my_workspace_ID`
                                --log-group-arn `my-log-group-arn`
```

### Limitations

- **Not all events logged**

Amazon Managed Service for Prometheus only logs events that are at the `warning` or
`error` level.

- **Policy size limits**

CloudWatch Logs resource policies are limited to 5120 characters. When CloudWatch Logs
detect that a policy approaches this size limit, it automatically
enables log groups that start with `/aws/vendedlogs/`.

When you create an alert rule with logging enabled, Amazon Managed Service for Prometheus must
update your CloudWatch Logs resource policy with the log group you specify. To
avoid reaching the CloudWatch Logs resource policy size limit, prefix your CloudWatch Logs
log group names with `/aws/vendedlogs/`. When you create a
log group in the Amazon Managed Service for Prometheus console, the log group names are prefixed with
`/aws/vendedlogs/`. For more information, see [Enabling Logging from Certain AWS Services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the CloudWatch Logs
User Guide.

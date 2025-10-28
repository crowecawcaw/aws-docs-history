**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Sending protection pack (web ACL) traffic logs to a Amazon CloudWatch Logs log group

This topic provides information for sending your protection pack (web ACL) traffic logs to a CloudWatch Logs
log group.

###### Note

You are charged for logging in addition to the charges for using
AWS WAF. For information, see [Pricing for logging protection pack (web ACL) traffic information](logging-pricing.md "logging-pricing.md").

To send logs to Amazon CloudWatch Logs, you create a CloudWatch Logs log group. When you enable logging
in AWS WAF, you provide the log group ARN. After you enable logging for your
protection pack (web ACL), AWS WAF delivers logs to the CloudWatch Logs log group in log streams.

When you use CloudWatch Logs, you can explore the logs for your protection pack (web ACL) in the AWS WAF
console. In your protection pack (web ACL) page, select the tab **Logging insights**.
This option is in addition to the logging insights that are provided for CloudWatch Logs
through the CloudWatch console.

Configure the log group for AWS WAF protection pack (web ACL) logs in the same Region as the
protection pack (web ACL) and using the same account as you use to manage the protection pack (web ACL). For information
about configuring a CloudWatch Logs log group, see [Working with Log
Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

## Quotas for CloudWatch Logs log groups

CloudWatch Logs has a default maximum quota for throughput, shared across all log groups within a region, which you can request to increase.
If your logging requirements are too high for the current throughput setting, you'll see throttling metrics for `PutLogEvents` for your account. To view the limit in the Service Quotas console and request an increase, see the [CloudWatch Logs PutLogEvents quota](https://console.aws.amazon.com/servicequotas/home/services/logs/quotas/L-7E1FAE88 "https://console.aws.amazon.com/servicequotas/home/services/logs/quotas/L-7E1FAE88").

## Log group naming

Your log group names must start with `aws-waf-logs-` and can end
with any suffix you like, for example,
`aws-waf-logs-testLogGroup2`.

The resulting ARN format is as follows:

```
arn:aws:logs:`Region`:`account-id`:log-group:aws-waf-logs-`log-group-suffix`
```

The log streams have the following naming format:

```
`Region`_`web-acl-name`_`log-stream-number`
```

The following shows an example log stream for protection pack (web ACL) `TestWebACL` in
Region `us-east-1`.

```
us-east-1_TestWebACL_0
```

## Permissions required to publish logs to

CloudWatch Logs

Configuring protection pack (web ACL) traffic logging for a CloudWatch Logs log group requires the
permissions settings described in this section. The permissions are set for you when you use
one of the AWS WAF full access managed policies,
`AWSWAFConsoleFullAccess` or `AWSWAFFullAccess`. If
you want to manage finer-grained access to your logging and AWS WAF resources, you
can set the permissions yourself. For information about managing permissions,
see [Access
management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
_IAM User Guide_. For information about the AWS WAF
managed policies, see [AWS managed policies for AWS WAF](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

These permissions allow you to change the protection pack (web ACL) logging configuration, to
configure log delivery for CloudWatch Logs, and to retrieve information about your log
group. These permissions must be attached to the user that you use to manage
AWS WAF.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "wafv2:PutLoggingConfiguration",
 "wafv2:DeleteLoggingConfiguration"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "LoggingConfigurationAPI"
 },
 {
 "Sid": "WebACLLoggingCWL",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

When actions are permitted on all AWS resources, it's indicated in the policy
with a `"Resource"` setting of `"*"`. This means that the
actions are permitted on all AWS resources _that each action
supports_. For example, the action
`wafv2:PutLoggingConfiguration` is supported only for `wafv2` logging configuration resources.

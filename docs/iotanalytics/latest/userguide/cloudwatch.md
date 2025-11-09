End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Monitoring with Amazon CloudWatch Logs

AWS IoT Analytics supports logging with Amazon CloudWatch. You can enable and configure Amazon CloudWatch logging for
AWS IoT Analytics by using the [`PutLoggingOptions`
API operation](../APIReference/API_PutLoggingOptions.md "../APIReference/API_PutLoggingOptions.md"). This section describes how you can use `PutLoggingOptions`
with AWS Identity and Access Management (IAM) to configure and enable Amazon CloudWatch logging for AWS IoT Analytics.

For more information about CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md"). For more information
about AWS IAM, see the [AWS Identity and Access Management User
Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

###### Note

Before you enable AWS IoT Analytics logging, make sure you understand the CloudWatch Logs access permissions.
Users with access to CloudWatch Logs can see your debugging information. For more information, see [Authentication and access control for
Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").

## Create an IAM role to enable logging

To create an IAM role to enable logging for Amazon CloudWatch

1. Use the [AWS IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") or the
   following AWS IAM CLI command, [CreateRole](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md"), to create a new IAM role with a trust relationship policy (trust
   policy). The trust policy grants an entity, such as Amazon CloudWatch, permission to assume the
   role.

```
aws iam create-role --role-name exampleRoleName --assume-role-policy-document
       exampleTrustPolicy.json
```

The
`exampleTrustPolicy.json` file contains the following content.

###### Note

This example includes a global condition context key to protect against the confused
deputy security problem. Replace `123456789012` with your AWS account ID and `aws-region` with the AWS region of your AWS resources. For more information, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

You use the ARN of this role later when you call the AWS IoT Analytics `PutLoggingOptions`
command. 2. Use AWS IAM [PutRolePolicy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md") to
attach a permissions policy (a `role policy`) to the role you created in Step

1.

`aws iam put-role-policy --role-name exampleRoleName --policy-name examplePolicyName
 --policy-document exampleRolePolicy.json`

The exampleRolePolicy.json file contains the following content.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream"
 ],
 "Resource": [
 "arn:aws:logs:*:*:*"
 ]
 }
 ]
}`

```

3. To give AWS IoT Analytics permission to put logging events to Amazon CloudWatch, use the Amazon CloudWatch command
   [PutResourcePolicy](../../../cli/latest/reference/logs/put-resource-policy.md "../../../cli/latest/reference/logs/put-resource-policy.md").

###### Note

To help prevent the confused deputy security problem, we recommend that you specify
`aws:SourceArn` in your resource policy. This restricts access to allow only
those requests that come from a specified account. For more information about the confused
deputy problem, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

`aws logs put-resource-policy --policy-in-json
 exampleResourcePolicy.json`

The `exampleResourcePolicy.json` file contains the following resource policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "iotanalytics.amazonaws.com"
 },
 "Action": "logs:PutLogEvents",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:iotanalytics:`us-east-1`:`123456789012`:*/*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

## Configure and enable logging

Use the `PutLoggingOptions` command to configure and enable Amazon CloudWatch logging for
AWS IoT Analytics. The `roleArn` in the `loggingOptions` field should be the ARN of
the role you created in the previous section. You can also use the
`DecribeLoggingOptions` command to check your logging options settings.

### PutLoggingOptions

Sets or updates the AWS IoT Analytics logging options. If you update the value of any
`loggingOptions` field, it takes up to one minute for the change to take effect.
Also, if you change the policy attached to the role you specified in the `roleArn`
field (for example, to correct a
policy
that isn't valid), it can take up to five minutes for that change to take effect. For more
information, see [`PutLoggingOptions`](../APIReference/API_PutLoggingOptions.md "../APIReference/API_PutLoggingOptions.md").

### DescribeLoggingOptions

Retrieves the current settings of the AWS IoT Analytics logging options. For more information, see
[`DescribeLoggingOptions`](../APIReference/API_DescribeLoggingOptions.md "../APIReference/API_DescribeLoggingOptions.md")

### Namespace, metrics, and dimensions

AWS IoT Analytics puts the following metrics into the Amazon CloudWatch repository:

| Namespace        |
| ---------------- |
| AWS/IoTAnalytics |

| Metric                           | Description                                                           |
| -------------------------------- | --------------------------------------------------------------------- |
| ActionExecution                  | The number of actions<br>executed.                                    |
| ActionExecutionThrottled         | The number of actions that are throttled.                             |
| ActivityExecutionError           | The number of errors generated while executing the pipeline activity. |
| IncomingMessages                 | The number of messages coming into the channel.                       |
| PipelineConcurrentExecutionCount | The number of pipeline activities, which have executed concurrently.  |

| Dimension            | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| ActionType           | The type of action that is being monitored.                |
| ChannelName          | The name of the channel that is being monitored.           |
| DatasetName          | The name of the dataset that is being monitored.           |
| DatastoreName        | The name of the data store that is being monitored.        |
| PipelineActivityName | The name of the pipeline activity that is being monitored. |
| PipelineActivityType | The type of the pipeline activity that is being monitored. |
| PipelineName         | The name of the pipeline that is being monitored.          |

# `AWSSupport-EnableVPCFlowLogs`

**Description**

The `AWSSupport-EnableVPCFlowLogs` runbook creates Amazon Virtual Private Cloud (Amazon VPC)
Flow Logs for subnets, network interfaces, and VPCs in your AWS account. If you
create a flow log for a subnet or VPC, each elastic network interface in that subnet
or Amazon VPC is monitored. Flow log data is published to the Amazon CloudWatch Logs log group or the
Amazon Simple Storage Service (Amazon S3) bucket you specify. For more information about flow logs, see [VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon VPC User Guide_ .

###### Important

Data ingestion and archival charges for vended logs apply when you publish
flow logs to CloudWatch Logs or to Amazon S3. For more information, see [Flow Logs
pricing](../../../vpc/latest/userguide/flow-logs.md#flow-logs-pricing "../../../vpc/latest/userguide/flow-logs.md#flow-logs-pricing")

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-EnableVPCFlowLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-EnableVPCFlowLogs")

###### Note

When selecting `s3` as the log destination, ensure that the bucket policy allows the log delivery service access to the bucket. For more information see [Amazon S3 bucket permissions for flow logs](../../../vpc/latest/userguide/flow-logs-s3.md#flow-logs-s3-permissions "../../../vpc/latest/userguide/flow-logs-s3.md#flow-logs-s3-permissions")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- DeliverLogsPermissionArn

Type: String

Description: (Optional) The ARN for the IAM role that permits Amazon Elastic Compute Cloud
(Amazon EC2) to publish flow logs to the CloudWatch Logs log group in your account. If you
specify `s3` for the `LogDestinationType` parameter,
do not provide a value for this parameter. For more information, see [Publish flow logs to
CloudWatch Logs](../../../vpc/latest/userguide/flow-logs-cwl.md "../../../vpc/latest/userguide/flow-logs-cwl.md") in the _Amazon VPC User Guide_ .

- LogDestinationARN

Type: String

Description: (Optional) The ARN of the resource to which the flow log
data is published. If `cloud-watch-logs` is specified for the
`LogDestinationType` parameter, provide the ARN of the CloudWatch Logs
log group you want to publish flow log data to. Alternatively, use
`LogGroupName` instead. If `s3` is specified for
the `LogDestinationType` parameter, you must specify the ARN of
the Amazon S3 bucket you want to publish flow log data to for this parameter. You
can also specify a folder in the bucket.

###### Important

When choosing `s3` as the `LogDestinationType` you should ensure that the bucket selected follows [Amazon S3 Bucket security best practices](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md"), and that you follow the data privacy laws for your organisation and geographic region.

- LogDestinationType

Type: String

Valid values: cloud-watch-logs | s3

Description: (Required) Determines where flow log data is published. If
you specify `LogDestinationType` as `s3` , do not
specify `DeliverLogsPermissionArn` or `LogGroupName` .

- LogFormat

Type: String

Description: (Optional) The fields to include in the flow log, and the
order in which they should appear in the record. For a list of available
fields, see [Flow
log records](../../../vpc/latest/userguide/flow-logs.md#flow-log-records "../../../vpc/latest/userguide/flow-logs.md#flow-log-records") in the _Amazon VPC User Guide_ . If
you do not provide a value for this parameter, the flow log is created using
the default format. If you specify this parameter, you must specify at least
one field.

- LogGroupName

Type: String

Description: (Optional) The name of the CloudWatch Logs log group where flow log
data is published. If you specify `s3` for the
`LogDestinationType` parameter, do not provide a value for
this parameter.

- ResourceIds

Type: StringList

Description: (Required) A comma-separated list of the IDs for the subnets,
elastic network interfaces, or VPC for which you want to create a flow
log.

- TrafficType

Type: String

Valid values: ACCEPT | REJECT | ALL

Description: (Required) The type of traffic to log. You can log traffic
that the resource accepts or rejects, or all traffic.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ec2:CreateFlowLogs`
- `ec2:DeleteFlowLogs`
- `ec2:DescribeFlowLogs`
- `iam:AttachRolePolicy`
- `iam:CreateRole`
- `iam:CreatePolicy`
- `iam:DeletePolicy`
- `iam:DeleteRole`
- `iam:DeleteRolePolicy`
- `iam:GetPolicy`
- `iam:GetRole`
- `iam:TagRole`
- `iam:PassRole`
- `iam:PutRolePolicy`
- `iam:UpdateRole`
- `logs:CreateLogDelivery`
- `logs:CreateLogGroup`
- `logs:DeleteLogDelivery`
- `logs:DeleteLogGroup`
- `logs:DescribeLogGroups`
- `logs:DescribeLogStreams`
- `s3:GetBucketLocation`
- `s3:GetBucketAcl`
- `s3:GetBucketPublicAccessBlock`
- `s3:GetBucketPolicyStatus`
- `s3:GetBucketAcl`
- `s3:ListBucket`
- `s3:PutObject`
  Sample Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SSMExecutionPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm:StartAutomationExecution",
 "ssm:GetAutomationExecution"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EC2FlowLogsPermissions",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateFlowLogs",
 "ec2:DeleteFlowLogs",
 "ec2:DescribeFlowLogs"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:`instance`/`resource-id`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:`subnet`/`resource-id`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:`vpc`/`resource-id`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:`transit-gateway`/`resource-id`",
 "arn:aws:ec2:`us-east-1`:`111122223333`:`transit-gateway-attachment`/`resource-id`"
 ]
 },
 {
 "Sid": "IAMCreateRolePermissions",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:DeletePolicy",
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:GetPolicy",
 "iam:GetRole",
 "iam:TagRole",
 "iam:PassRole",
 "iam:PutRolePolicy",
 "iam:UpdateRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`role-name`",
 "arn:aws:iam::`111122223333`:role/AWSSupportCreateFlowLogsRole"
 ]
 },
 {
 "Sid": "CloudWatchLogsPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:DeleteLogDelivery",
 "logs:DeleteLogGroup",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`log-group-name`",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`log-group-name`:*"
 ]
 },
 {
 "Sid": "S3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetAccountPublicAccessBlock",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketAcl",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

**Document Steps**

- `aws:branch` - Branches based on the value specified for the
  `LogDestinationType` parameter.
- `aws:executeScript` - Checks if the target Amazon Simple Storage Service (Amazon S3) potentially grants
  **read** or **write** `public` access to its objects.
- `aws:executeScript` - Creates a log group if no value is
  specified for the `LogDestinationARN` parameter, and
  `cloud-watch-logs` is specified for the
  `LogDestinationType` parameter.
- `aws:executeScript` - Creates flow logs based on the values
  specified in the runbook parameters.

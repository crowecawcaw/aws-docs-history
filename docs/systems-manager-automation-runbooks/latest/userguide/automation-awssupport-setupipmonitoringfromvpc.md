# `AWSSupport-SetupIPMonitoringFromVPC`

**Description**

`AWSSupport-SetupIPMonitoringFromVPC` creates an Amazon Elastic Compute Cloud (Amazon EC2)
instance in the specified subnet and monitors selected target IPs (IPv4 or IPv6) by
continuously running ping, MTR, traceroute and tracetcp tests. The results are
stored in Amazon CloudWatch Logs logs, and metric filters are applied to quickly visualize
latency and packet loss statistics in a CloudWatch dashboard.

**Additional Information**

The CloudWatch Logs data can be used for network troubleshooting and analysis of
pattern/trends. Additionally, you can configure CloudWatch alarms with Amazon SNS notifications
when packet loss and/or latency reach a threshold. The data can also be used when
opening a case with AWS Support, to help isolate an issue quickly and reduce time to
resolution when investigating a network issue.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-SetupIPMonitoringFromVPC "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-SetupIPMonitoringFromVPC")

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

- CloudWatchLogGroupNamePrefix

Type: String

Default: `/AWSSupport-SetupIPMonitoringFromVPC`

Description: (Optional) Prefix used for each CloudWatch log group created for
the test results.

- CloudWatchLogGroupRetentionInDays

Type: String

Valid values: 1 | 3 | 5 | 7 | 14 | 30 | 60 | 90 | 120 | 150 | 180 | 365 |
400 | 545 | 731 | 1827 | 3653

Default: 7

Description: (Optional) Number of days you want to keep the network
monitoring results for.

- InstanceType

Type: String

Valid values: t2.micro | t2.small | t2.medium | t2.large | t3.micro |
t3.small | t3.medium | t3.large | t4g.micro | t4g.small | t4g.medium |
t4g.large

Default: t3.micro

Description: (Optional) The EC2 instance type for the EC2Rescue instance.
Recommended size: t3.micro.

- SubnetId

Type: String

Description: (Required) The subnet ID for the monitor instance. Be aware
that if you specify a private subnet, then you must make sure there is
Internet access to allow the monitor instance to setup the test (meaning,
install the CloudWatch Logs agent, interact with Systems Manager and CloudWatch).

- TargetIPs

Type: String

Description: (Required) Comma separated list of IPv4s and/or IPv6s to
monitor. No spaces allowed. Maximum size is 255 characters. Be aware that if
you provide an invalid IP, then the automation will fail and rollback the
test setup.

- TestInstanceSecurityGroupId

Type: String

Description: (Optional) The security group ID for the test instance. If
not specified, the automation creates one during the instance creation. Make
sure the security group allows outbound access to the monitoring IPs.

- TestInstanceProfileName

Type: String

Description: (Optional) The name of an existing IAM instance profile for
the test instance. If not specified, the automation creates one during the
instance creation. The role must have the following permissions:
`logs:CreateLogStream`, `logs:DescribeLogGroups`,
`logs:DescribeLogStreams`, and `logs:PutLogEvents`
and the AWS Managed Policy
`AmazonSSMManagedInstanceCore`.

- TestInterval

Type: String

Description: (Optional) The number of minutes between test intervals. The
default value is `1` minute and the maximum is `10`
minutes.

- RetainDashboardAndLogsOnDeletion

Type: String

Description: (Optional) Specify `False` to delete the Amazon
CloudWatch dashboard and Logs when deleting the AWS AWS CloudFormation stack. The
default value is `True`. By default, the dashboard and logs are
retained and will need to be manually deleted when they are no longer
needed.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

###### Warning

It is recommended to pass `TestInstanceProfileName` parameter or
ensure security guardrails in place to prevent misuse of mutable IAM
permissions.

It is recommended that the user who runs the automation have the **AmazonSSMAutomationRole** IAM managed policy attached. In
addition, the user must have the following policy attached to their user account,
group, or role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iam:CreateRole",
 "iam:CreateInstanceProfile",
 "iam:GetRole",
 "iam:GetInstanceProfile",
 "iam:DetachRolePolicy",
 "iam:AttachRolePolicy",
 "iam:PassRole",
 "iam:AddRoleToInstanceProfile",
 "iam:GetRolePolicy",
 "iam:RemoveRoleFromInstanceProfile",
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:DeleteInstanceProfile",
 "iam:PutRolePolicy",
 "iam:TagRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/SetupIPMonitoringFromVPC*",
 "arn:aws:iam::`111122223333`:instance-profile/SetupIPMonitoringFromVPC*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:CreateChangeSet",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackEvents",
 "cloudwatch:PutDashboard",
 "cloudwatch:DeleteDashboards",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:CreateSecurityGroup",
 "ec2:CreateLaunchTemplate",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeImages",
 "ec2:DescribeSubnets",
 "ec2:DescribeInstanceTypes",
 "ec2:DescribeVpcs",
 "ec2:DeleteLaunchTemplate",
 "ec2:DeleteSecurityGroup",
 "ec2:RunInstances",
 "ec2:TerminateInstances",
 "ec2:DescribeInstanceStatus",
 "ec2:CreateTags",
 "ec2:AssignIpv6Addresses",
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeLaunchTemplates",
 "ec2:RevokeSecurityGroupEgress",
 "logs:CreateLogGroup",
 "logs:DeleteLogGroup",
 "logs:PutMetricFilter",
 "logs:PutRetentionPolicy",
 "logs:TagResource",
 "ssm:DescribeInstanceInformation",
 "ssm:GetParameter",
 "ssm:GetParameters",
 "ssm:SendCommand",
 "ssm:ListCommands",
 "ssm:ListCommandInvocations"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

If the `TestInstanceProfileName` parameter is provided, the following
IAM permissions are not required to execute the runbook:

- iam:CreateRole
- iam:CreateInstanceProfile
- iam:DetachRolePolicy
- iam:AttachRolePolicy
- iam:AddRoleToInstanceProfile
- iam:RemoveRoleFromInstanceProfile
- iam:DeleteRole
- iam:DeleteRolePolicy
- iam:DeleteInstanceProfile

**Document Steps**

1. **`aws:executeAwsApi`** - describe the provided subnet to get the VPC ID and IPv6 CIDR block association state.
2. **`aws:executeScript`** - validate the provided target IPs are syntactically correct IPv4 and/or IPv6 addresses, get the architecture of the selected instance type, and verify the subnet has an IPv6 pool association if any target IP is IPv6.
3. **`aws:createStack`** - create an AWS CloudFormation stack that provisions the test Amazon EC2 instance, IAM instance profile (if not provided), security group (if not provided), CloudWatch log groups, and CloudWatch dashboard.

(Cleanup) If the step fails:

**`aws:executeScript`** - describe the CloudFormation stack events to identify the failure reason.

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 4. **`aws:waitForAwsResourceProperty`** - wait for the CloudFormation stack to complete creation.

(Cleanup) If the step fails:

**`aws:executeScript`** - describe the CloudFormation stack events to identify the failure reason.

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 5. **`aws:executeScript`** - describe the CloudFormation stack resources to get the test instance ID, security group ID, IAM role, instance profile, and dashboard name.

(Cleanup) If the step fails:

**`aws:executeScript`** - describe the CloudFormation stack events to identify the failure reason.

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 6. **`aws:waitForAwsResourceProperty`** - wait for the test instance to become a managed instance.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 7. **`aws:runCommand`** - install the CloudWatch agent on the test instance.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 8. **`aws:runCommand`** - define the network test scripts (MTR, ping, tracepath, and traceroute) for each of the provided IPs.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 9. **`aws:runCommand`** - start the network tests and schedule subsequent executions using cronjobs that run every TestInterval minutes.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 10. **`aws:runCommand`** - configure the CloudWatch agent to push test results from `/home/ec2-user/logs/` to CloudWatch Logs.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 11. **`aws:runCommand`** - configure log rotation for the test results in `/home/ec2-user/logs/`. 12. **`aws:executeScript`** - set the retention policy for all CloudWatch log groups created by the CloudFormation stack. 13. **`aws:executeScript`** - create CloudWatch log group metric filters for ping latency and ping packet loss.

(Cleanup) If the step fails:

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 14. **`aws:executeScript`** - update the CloudWatch dashboard to include widgets for ping latency and ping packet loss statistics.

(Cleanup) If the step fails:

**`aws:executeAwsApi`** - delete the CloudWatch dashboard, if it exists.

**`aws:deleteStack`** - delete the CloudFormation stack and all associated resources. 15. **`aws:branch`** - evaluate the SleepTime parameter. If set to `0`, the automation ends without deleting the stack. 16. **`aws:sleep`** - wait for the specified SleepTime duration before deleting the CloudFormation stack. 17. **`aws:deleteStack`** - delete the CloudFormation stack. Based on the RetainDashboardAndLogsOnDeletion parameter, the CloudWatch dashboard and log groups are either retained or deleted.

(Cleanup) If the stack deletion fails:

**`aws:executeScript`** - describe the CloudFormation stack events to identify the deletion failure reason.

**Outputs**

updateCloudWatchDashboard.StackUrl - the URL of the CloudFormation stack.

updateCloudWatchDashboard.DashboardUrl - the URL of the CloudWatch dashboard.

updateCloudWatchDashboard.DashboardName - the name of the CloudWatch dashboard.

updateCloudWatchDashboard.LogGroups - the list of CloudWatch log groups created.

describeStackResources.HelperInstanceId - the test instance ID.

describeStackResources.StackName - the CloudFormation stack name.

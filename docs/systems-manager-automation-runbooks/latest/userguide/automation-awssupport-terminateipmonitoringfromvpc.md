# `AWSSupport-TerminateIPMonitoringFromVPC`

**Description**

`AWSSupport-TerminateIPMonitoringFromVPC` terminates an IP monitoring
test previously started by `AWSSupport-SetupIPMonitoringFromVPC` . Data
related to the specified test ID will be deleted.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TerminateIPMonitoringFromVPC "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TerminateIPMonitoringFromVPC")

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

- AutomationExecutionId

Type: String

Description: (Required) The automation execution ID from when you
previously ran the `AWSSupport-SetupIPMonitoringFromVPC` runbook.
All resources associated with this execution ID are deleted.

- InstanceId

Type: String

Description: (Required) The instance ID for the monitor instance.

- SubnetId

Type: String

Description: (Required) The subnet ID for the monitor instance.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

It is recommended that the user who runs the automation have the **AmazonSSMAutomationRole** IAM managed policy attached. In
addition, the user must have the following policy attached to their user, group, or
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iam:DetachRolePolicy",
 "iam:RemoveRoleFromInstanceProfile",
 "iam:DeleteRole",
 "iam:DeleteInstanceProfile",
 "iam:DeleteRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/AWSSupport/SetupIPMonitoringFromVPC_*",
 "arn:aws:iam::`111122223333`:instance-profile/AWSSupport/SetupIPMonitoringFromVPC_*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "iam:DetachRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::aws:policy/service-role/AmazonSSMManagedInstanceCore"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "cloudwatch:DeleteDashboards"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "ec2:DescribeTags",
 "ec2:DescribeInstances",
 "ec2:DescribeSecurityGroups",
 "ec2:DeleteSecurityGroup",
 "ec2:TerminateInstances",
 "ec2:DescribeInstanceStatus"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

**Document Steps**

1. `aws:assertAwsResourceProperty` - check AutomationExecutionId and
   InstanceId are related to the same test.
2. `aws:assertAwsResourceProperty` - check SubnetId and InstanceId
   are related to the same test.
3. `aws:executeAwsApi` - retrieve the test security group.
4. `aws:executeAwsApi` - delete the CloudWatch dashboard.
5. `aws:changeInstanceState` - terminate the test instance.
6. `aws:executeAwsApi` - remove the IAM instance profile from the
   role.
7. `aws:executeAwsApi` - delete the IAM instance profile created by
   the automation.
8. `aws:executeAwsApi` - delete the CloudWatch inline policy from the role
   created by the automation.
9. `aws:executeAwsApi` - detach the **AmazonSSMManagedInstanceCore** managed policy from the role
   created by the automation.
10. `aws:executeAwsApi` - delete the IAM role created by the
    automation.
11. `aws:executeAwsApi` - delete the security group created by the
    automation, if it exists.

**Outputs**

None

# `AWS-DeleteImage`

**Description**

Delete an Amazon Machine Image (AMI) and all associated snapshots.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeleteImage "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeleteImage")

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

- ImageId

Type: String

Description: (Required) The ID of the AMI.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:DeleteSnapshot",
 "Resource": "arn:aws:ec2:*:*:snapshot/*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DescribeImages",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:DeregisterImage",
 "Resource": "*"
 }
 ]
}`

```

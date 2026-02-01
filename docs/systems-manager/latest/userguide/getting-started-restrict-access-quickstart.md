• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Sample IAM

policies for Session Manager

Use the samples in this section to help you create AWS Identity and Access Management (IAM) policies
that provide the most commonly needed permissions for Session Manager access.

###### Note

You can also use an AWS KMS key policy to control which IAM entities
(users or roles) and AWS accounts are given access to your KMS key. For
information, see [Overview of
Managing Access to Your AWS KMS Resources](../../../kms/latest/developerguide/control-access-overview.md "../../../kms/latest/developerguide/control-access-overview.md") and [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

###### Topics

- [Quickstart end user
  policies for Session Manager](#restrict-access-quickstart-end-user "#restrict-access-quickstart-end-user")
- [Quickstart administrator
  policy for Session Manager](#restrict-access-quickstart-admin "#restrict-access-quickstart-admin")

## Quickstart end user

policies for Session Manager

Use the following examples to create IAM end user policies for Session Manager.

You can create a policy that allows users to start sessions from only the
Session Manager console and AWS Command Line Interface (AWS CLI), from only the Amazon Elastic Compute Cloud (Amazon EC2)
console, or from all three.

These policies provide end users the ability to start a session to a
particular managed node and the ability to end only their own sessions.
Refer to [Additional sample
IAM policies for Session Manager](getting-started-restrict-access-examples.md "getting-started-restrict-access-examples.md") for examples
of customizations you might want to make to the policy.

In the following sample policies, replace each `example
 resource placeholder` with your own information.

Choose from the following tabs to view the sample policy
for the range of session access you want to provide.

Session Manager and Fleet Manager
Use this sample policy to give users the ability to start and
resume sessions from only the Session Manager and Fleet Manager consoles.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-02573cafcfEXAMPLE`",
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 },
 {
 "Effect": "Allow",
 "Action": ["ssmmessages:OpenDataChannel"],
 "Resource": ["arn:aws:ssm:*:*:session/${aws:userid}-*"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssm:GetConnectionStatus",
 "ssm:DescribeInstanceProperties",
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-name`"
 }
 ]
}`

```

Amazon EC2
Use this sample policy to give users the ability to start and
resume sessions from only the Amazon EC2 console. This policy doesn't
provide all the permissions needed to start sessions from the
Session Manager console and the AWS CLI.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-02573cafcfEXAMPLE`",
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 },
 {
 "Effect": "Allow",
 "Action": ["ssmmessages:OpenDataChannel"],
 "Resource": ["arn:aws:ssm:*:*:session/${aws:userid}-*"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetConnectionStatus",
 "ssm:DescribeInstanceInformation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:username}-*"
 ]
 }
 ]
}`

```

AWS CLI
Use this sample policy to give users the ability to start and
resume sessions from the AWS CLI.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-02573cafcfEXAMPLE`",
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 },
 {
 "Effect": "Allow",
 "Action": ["ssmmessages:OpenDataChannel"],
 "Resource": ["arn:aws:ssm:*:*:session/${aws:userid}-*"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-name`"
 }
 ]
}`

```

###### Note

`SSM-SessionManagerRunShell` is the default name of
the SSM document that Session Manager creates to store your session
configuration preferences. You can create a custom Session document and
specify it in this policy instead. You can also specify the
AWS-provided document `AWS-StartSSHSession` for users who
are starting sessions using SSH. For information about configuration
steps needed to support sessions using SSH, see [(Optional) Allow and control permissions for SSH connections through Session Manager](session-manager-getting-started-enable-ssh-connections.md "session-manager-getting-started-enable-ssh-connections.md").

The `kms:GenerateDataKey` permission enables the creation
of a data encryption key that will be used to encrypt session data. If
you will use AWS Key Management Service (AWS KMS) encryption for your session data, replace
`key-name` with the Amazon Resource Name
(ARN) of the KMS key you want to use, in the format
`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-12345EXAMPLE`.
If you won't use KMS key encryption for your session data, remove the
following content from the policy.

```
{
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "`key-name`"
        }
```

For information about using AWS KMS for encrypting session data, see
[Turn on KMS key
encryption of session data (console)](session-preferences-enable-encryption.md "session-preferences-enable-encryption.md").

The permission for [SendCommand](../APIReference/API_SendCommand.md "../APIReference/API_SendCommand.md") is needed for cases where a user
attempts to start a session from the Amazon EC2 console, but the SSM Agent
must be updated to the minimum required version for Session Manager first.
Run Command is used to send a command to the instance to update the
agent.

## Quickstart administrator

policy for Session Manager

Use the following examples to create IAM administrator policies for
Session Manager.

These policies provide administrators the ability to start a session to
managed nodes that are tagged with
`Key=Finance,Value=WebServers`, permission to create, update, and
delete preferences, and permission to end only their own sessions. Refer to
[Additional sample
IAM policies for Session Manager](getting-started-restrict-access-examples.md "getting-started-restrict-access-examples.md") for examples
of customizations you might want to make to the policy.

You can create a policy that allows administrators to perform these tasks
from only the Session Manager console and AWS CLI, from only the Amazon EC2 console, or
from all three.

In the following sample policies, replace each `example
 resource placeholder` with your own information.

Choose from the following tabs to view the sample policy
for the access scenario you want to support.

Session Manager and CLI
Use this sample policy to give administrators the ability to
perform session-related tasks from only the Session Manager console and
the AWS CLI. This policy doesn't provide all the permissions
needed to perform session-related tasks from the Amazon EC2
console.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/Finance": [
 "WebServers"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssm:GetConnectionStatus",
 "ssm:DescribeInstanceProperties",
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:CreateDocument",
 "ssm:UpdateDocument",
 "ssm:GetDocument",
 "ssm:StartSession"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 }
 ]
}`

```

Amazon EC2
Use this sample policy to give administrators the ability to
perform session-related tasks from only the Amazon EC2 console. This
policy doesn't provide all the permissions needed to perform
session-related tasks from the Session Manager console and the
AWS CLI.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/`tag-key`": [
 "`tag-value`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 },
 {
 "Effect": "Allow",
 "Action": ["ssmmessages:OpenDataChannel"],
 "Resource": ["arn:aws:ssm:*:*:session/${aws:userid}-*"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetConnectionStatus",
 "ssm:DescribeInstanceInformation"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 }
 ]
}`

```

Session Manager, CLI, and Amazon EC2
Use this sample policy to give administrators the ability to
perform session-related tasks from the Session Manager console, the
AWS CLI, and the Amazon EC2 console.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/`tag-key`": [
 "`tag-value`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": ["ssmmessages:OpenDataChannel"],
 "Resource": ["arn:aws:ssm:*:*:session/${aws:userid}-*"]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssm:GetConnectionStatus",
 "ssm:DescribeInstanceInformation",
 "ssm:DescribeInstanceProperties",
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:CreateDocument",
 "ssm:UpdateDocument",
 "ssm:GetDocument",
 "ssm:StartSession"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:TerminateSession",
 "ssm:ResumeSession"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:session/${aws:userid}-*"
 ]
 }
 ]
}`

```

###### Note

The permission for [SendCommand](../APIReference/API_SendCommand.md "../APIReference/API_SendCommand.md") is needed for cases where a user
attempts to start a session from the Amazon EC2 console, but a command must
be sent to update SSM Agent first.

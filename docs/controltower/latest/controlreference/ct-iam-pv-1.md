# [CT.IAM.PV.1] Disallow modification of an AWS IAM role that AWS Control Tower utilizes to manage AWS Backup resources

This control limits modification of the AWS IAM role (aws-controltower-BackupRole) that AWS Control Tower utilizes for management of AWS Backup resources.

This is a preventive control with elective guidance. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Identity and Access Management (IAM)

###### Control metadata

- **Control objective:** Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control group:**
- **Resource types:** `AWS::IAM::Role`

###### Usage considerations

- AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.
  The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CTIAMPV1",
 "Effect": "Deny",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:DeleteRolePermissionsBoundary",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:PutRolePermissionsBoundary",
 "iam:PutRolePolicy",
 "iam:UpdateAssumeRolePolicy",
 "iam:UpdateRole"
 ],
 "Resource": "arn:*:iam::*:role/aws-controltower-BackupRole",
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:*:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
 }`

```

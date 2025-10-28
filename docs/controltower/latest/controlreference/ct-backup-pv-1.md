# [CT.BACKUP.PV.1] Disallow modification of a tag that AWS Control Tower applies to AWS Backup resources

This control limits changes to tags that AWS Control Tower applies to AWS Backup resources.

This is a preventive control with elective guidance. By default, this control is not enabled. Although you can see the control in the console, you can enable it only by activating AWS Backup capabilities for your landing zone.

**AWS service:** AWS Backup

###### Control metadata

- **Control objective:** Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control group:**
- **Resource types:** `Multiple`

###### Usage considerations

- AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.
- If you apply a tag with the key `aws-control-tower` to an AWS Backup resource created independently of AWS Control Tower, the resource becomes subject to this SCP.
  The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CTBACKUPPV1",
 "Effect": "Deny",
 "Action": [
 "backup:TagResource",
 "backup:UntagResource"
 ],
 "Resource": "*",
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:*:iam::*:role/AWSControlTowerExecution"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "aws-control-tower"
 }
 }
 }
 ]
 }`

```

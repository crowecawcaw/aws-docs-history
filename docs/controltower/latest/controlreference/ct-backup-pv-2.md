# [CT.BACKUP.PV.2] Disallow modification of an AWS Backup report plan that AWS Control Tower manages

This control limits changes to the AWS Backup report plan that AWS Control Tower manages.

This is a preventive control with elective guidance. By default, this control is not enabled. Although you can see the control in the console, you can enable it only by activating AWS Backup capabilities for your landing zone.

**AWS service:** AWS Backup

###### Control metadata

- **Control objective:** Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control group:**
- **Resource types:** `AWS::Backup::ReportPlan`

###### Usage considerations

- AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.
  The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CTBACKUPPV2",
 "Effect": "Deny",
 "Action": [
 "backup:CreateReportPlan",
 "backup:DeleteReportPlan",
 "backup:UpdateReportPlan"
 ],
 "Resource": "arn:*:backup:*:*:report-plan:aws_controltower_*",
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": [
 "arn:*:iam::*:role/AWSControlTowerExecution"
 ]
 }
 }
 }
 ]
 }`

```

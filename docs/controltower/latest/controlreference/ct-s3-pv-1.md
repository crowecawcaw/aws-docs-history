# [CT.S3.PV.1] Disallow modification of an Amazon S3 bucket that stores AWS Backup reports for AWS Control Tower

This control limits modification of the Amazon S3 buckets that AWS Control Tower utilizes as a destination for storing AWS Backup reports.

This is a preventive control with elective guidance. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control group:**
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- AWS Backup resources managed by AWS Control Tower should be modified using the AWS Control Tower API or console. API read actions for AWS Backup, such as `ListBackupPlans` and `GetBackupVaultAccessPolicy`, can be utilized directly.
  The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CTS3PV1",
 "Effect": "Deny",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucket",
 "s3:DeleteBucketPolicy",
 "s3:DeleteBucketWebsite",
 "s3:PutAccelerateConfiguration",
 "s3:PutBucketAcl",
 "s3:PutBucketCORS",
 "s3:PutBucketLogging",
 "s3:PutBucketObjectLockConfiguration",
 "s3:PutBucketOwnershipControls",
 "s3:PutBucketPolicy",
 "s3:PutBucketPublicAccessBlock",
 "s3:PutBucketVersioning",
 "s3:PutBucketWebsite",
 "s3:PutEncryptionConfiguration",
 "s3:PutLifecycleConfiguration",
 "s3:PutReplicationConfiguration"
 ],
 "Resource": "arn:*:s3:::aws-controltower-backup-reports-*",
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

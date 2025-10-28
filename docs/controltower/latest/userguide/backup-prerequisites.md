# Prerequisites

Before you can set up AWS Backup for your AWS Control Tower resources, you must have an existing
AWS Organizations organization. If you've already set up your AWS Control Tower landing zone, that serves as
your existing organization.

You must allocate or create two other AWS accounts that are not enrolled in
AWS Control Tower. These accounts become the _central backup account_ and the
_backup administrator account_. Name these accounts with those
names.

Also, you must select or create a multi-Region AWS Key Management Service (KMS) key, specifically for
AWS Backup.

###### Defining your prerequisites

- **The central backup account**—The central
  backup account stores your AWS Control Tower backup vault and your backups. This vault is
  created in all AWS Regions that AWS Control Tower governs, within this account.
  Cross-account copies are stored in this account, in case an account is
  compromised and requires data restoration.
- **The backup administrator account**—The
  backup administrator account is the delegated administrator account for the
  AWS Backup service in AWS Control Tower. It stores the Backup Audit Manager (BAM) report
  plans. This account aggregates all backup monitoring data, such as restore jobs
  and copy jobs. The data is stored in an Amazon S3 bucket. For more information, see
  [Creating
  report plans using the AWS Backup console](../../../aws-backup/latest/devguide/create-report-plan-console.md "../../../aws-backup/latest/devguide/create-report-plan-console.md") in the _AWS Backup
  Developer Guide_.
- **Policy requirement for the multi-Region AWS KMS
  key**

Your AWS KMS key requires a key policy.
Consider a key policy similar to this
one, which restricts access to principals (users and roles) who have
permissions associated with your organization's management account:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "KMS key policy",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "Allow use of the KMS key for organization",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey*",
 "kms:Encrypt",
 "kms:ReEncrypt*",
 "kms:GetKeyPolicy",
 "kms:CreateGrant",
 "kms:ListGrants",
 "kms:RevokeGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`ORGANIZATION-ID`"
 }
 }
 }
 ]
}`

```

This example policy gives all accounts in your organization access to their encrypted backup data. Use [AWS global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") and [AWS KMS condition keys](../../../kms/latest/developerguide/policy-conditions.md "../../../kms/latest/developerguide/policy-conditions.md") to refine the permissions, depending on which principals require access to your backups.

###### Note

Your multi-region AWS KMS key must be replicated for every AWS Region that you
plan to govern with AWS Control Tower.

# Setting up prerequisites for entity lists and IP address

lists

GuardDuty uses entity lists and IP address lists to customize threat detection in your AWS
environment. Entity lists (recommended) support both IP addresses and domain names, while IP address
lists support only IP addresses. Before you begin creating these lists, you must
add the required permissions for the type of list that you want to use.

## Prerequisites for entity

lists

When you add entity lists, GuardDuty reads your trusted and threat intelligence lists
from S3 buckets. The role you use to create entity lists must have
the `s3:GetObject` permission for the S3 buckets contains these lists.

###### Note

In a multi-account environment, only the GuardDuty administrator account can manage lists, which automatically
apply to member accounts.

If you don't already have the `s3:GetObject` permission
for the S3 bucket location, then use the following example policy
and replace `amzn-s3-demo-bucket` with your S3 bucket
location.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`[object-key]`"
 }
 ]
}`

```

## Prerequisites for IP

address lists

Various IAM identities require special permissions to work with trusted IP
lists and threat lists in GuardDuty. An identity with the attached [AmazonGuardDutyFullAccess_v2 (recommended)](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2 "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGuardDutyFullAccess-v2")
managed policy can only rename and deactivate uploaded trusted IP lists and
threat lists.

To grant various identities full access to working with trusted IP lists and
threat lists (in addition to renaming and deactivating, this includes adding,
activating, deleting, and updating the location or name of the lists), make sure
that the following actions are present in the permissions policy attached to a
user, group, or role:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:PutRolePolicy",
        "iam:DeleteRolePolicy"
    ],
    "Resource": "arn:aws:iam::`555555555555`:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty"
}
```

###### Important

These actions are not included in the
`AmazonGuardDutyFullAccess` managed policy.

### Using SSE-KMS encryption with entity lists

and IP lists

GuardDuty supports SSE-AES256 and SSE-KMS encryption for your lists. SSE-C is
not supported. For more information about encryption types for S3, see
[Protecting data
using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md").

Regardless of whether you use entity lists or IP lists, if you use
SSE-KMS, then add the following statement to your AWS KMS key policy.
Replace `123456789012` with your own
account ID.

```
{
    "Sid": "AllowGuardDutyServiceRole",
    "Effect": "Allow",
    "Principal": {
    "AWS": "arn:aws:iam::`123456789012`:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty"
    },
    "Action": "kms:Decrypt*",
    "Resource": "*"
}
```

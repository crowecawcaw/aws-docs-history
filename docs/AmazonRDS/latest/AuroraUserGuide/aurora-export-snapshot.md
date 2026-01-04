# Setting up access to an Amazon S3 bucket

You identify the Amazon S3 bucket, then you give the snapshot permission to access it.

###### Topics

- [Identifying the Amazon S3 bucket for export](#aurora-export-snapshot.SetupBucket "#aurora-export-snapshot.SetupBucket")
- [Providing access to an Amazon S3 bucket using an
  IAM role](#aurora-export-snapshot.SetupIAMRole "#aurora-export-snapshot.SetupIAMRole")
- [Using a cross-account Amazon S3 bucket](#aurora-export-snapshot.Setup.XAcctBucket "#aurora-export-snapshot.Setup.XAcctBucket")
- [Using a cross-account AWS KMS key](#aurora-export-snapshot.CMK "#aurora-export-snapshot.CMK")

## Identifying the Amazon S3 bucket for export

Identify the Amazon S3 bucket to export the DB snapshot to. Use an existing S3 bucket or create
a new S3 bucket.

###### Note

The S3 bucket to export to must be in the same AWS Region as the snapshot.

For more information about working with Amazon S3 buckets, see the following in the _Amazon Simple Storage Service User Guide_:

- [How do I view the
  properties for an S3 bucket?](../../../AmazonS3/latest/user-guide/view-bucket-properties.md "../../../AmazonS3/latest/user-guide/view-bucket-properties.md")
- [How do I enable
  default encryption for an Amazon S3 bucket?](../../../AmazonS3/latest/user-guide/default-bucket-encryption.md "../../../AmazonS3/latest/user-guide/default-bucket-encryption.md")
- [How do I create an S3
  bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md")

## Providing access to an Amazon S3 bucket using an

IAM role

Before you export DB snapshot data to Amazon S3, give the snapshot export tasks write-access
permission to the Amazon S3 bucket.

To grant this permission, create an IAM policy that provides access to the bucket, then
create an IAM role and attach the policy to the role. Later, you can assign the
IAM role to your snapshot export task.

###### Important

If you plan to use the AWS Management Console to export your snapshot, you can choose to create the IAM policy and the role
automatically when you export the snapshot. For instructions, see [Creating snapshot export tasks](aurora-export-snapshot.md "aurora-export-snapshot.md").

###### To give DB snapshot tasks access to Amazon S3

1. Create an IAM policy. This policy provides the bucket and object permissions that allow your snapshot export task to access
   Amazon S3.

In the policy, include the following required actions to allow the transfer of files from Amazon Aurora to an S3 bucket:

    * `s3:PutObject*`
    * `s3:GetObject*`
    * `s3:ListBucket`
    * `s3:DeleteObject*`
    * `s3:GetBucketLocation`

In the policy, include the following resources to identify the S3 bucket and objects in the bucket. The following list of
resources shows the Amazon Resource Name (ARN) format for accessing Amazon S3.

    * `arn:aws:s3:::`amzn-s3-demo-bucket``
    * `arn:aws:s3:::`amzn-s3-demo-bucket`/*`

For more information on creating an IAM policy for Amazon Aurora, see
[Creating and using an IAM policy for
IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md"). See also [Tutorial:
Create and attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the
_IAM User Guide_.

The following AWS CLI command creates an IAM policy named `ExportPolicy` with
these options. It grants access to a bucket named
`amzn-s3-demo-bucket`.

###### Note

After you create the policy, note the ARN of the policy. You need the ARN for a
subsequent step when you attach the policy to an IAM role.

```
aws iam create-policy  --policy-name ExportPolicy --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExportPolicy",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject*",
                "s3:ListBucket",
                "s3:GetObject*",
                "s3:DeleteObject*",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}'
```

2. Create an IAM role, so that Aurora can assume this IAM role on your behalf to access
   your Amazon S3 buckets. For more information, see [Creating a
   role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the
   _IAM User Guide_.

The following example shows using the AWS CLI command to create a role named `rds-s3-export-role`.

```
aws iam create-role  --role-name rds-s3-export-role  --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "export.rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole"
       }
     ]
   }'
```

3. Attach the IAM policy that you created to the IAM role that you created.

The following AWS CLI command attaches the policy created earlier to the role named
`rds-s3-export-role`. Replace `your-policy-arn`
with the policy ARN that you noted in an earlier step.

```
aws iam attach-role-policy  --policy-arn `your-policy-arn`  --role-name rds-s3-export-role
```

## Using a cross-account Amazon S3 bucket

You can use Amazon S3 buckets across AWS accounts. To use a cross-account bucket, add a bucket policy to allow access to the
IAM role that you're using for the S3 exports. For more information, see [Example 2: Bucket owner granting
cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md").

- Attach a bucket policy to your bucket, as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/Admin"
 },
 "Action": [
 "s3:PutObject*",
 "s3:ListBucket",
 "s3:GetObject*",
 "s3:DeleteObject*",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 ]
 }
 ]
}`

```

## Using a cross-account AWS KMS key

You can use a cross-account AWS KMS key to encrypt Amazon S3 exports. First, you add a key policy to the local account, then
you add IAM policies in the external account. For more information, see [Allowing users in other accounts to use a
KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md").

###### To use a cross-account KMS key

1. Add a key policy to the local account.

The following example gives `ExampleRole` and `ExampleUser` in the external account
444455556666 permissions in the local account 123456789012.

```
{
    "Sid": "Allow an external account to use this KMS key",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::444455556666:role/ExampleRole",
            "arn:aws:iam::444455556666:user/ExampleUser"
        ]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:RetireGrant"
    ],
    "Resource": "*"
}
```

2. Add IAM policies to the external account.

The following example IAM policy allows the principal to use the KMS key in account 123456789012 for
cryptographic operations. To give this permission to `ExampleRole` and `ExampleUser` in
account 444455556666, [attach the policy](../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_managed-using.md#attach-managed-policy-console") to them in that account.

```
{
    "Sid": "Allow use of KMS key in account 123456789012",
    "Effect": "Allow",
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:RetireGrant"
    ],
    "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

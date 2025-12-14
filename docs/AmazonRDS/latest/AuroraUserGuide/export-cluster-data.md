# Setting up access to an Amazon S3 bucket

You identify the Amazon S3 bucket, then you give the DB cluster export task permission to access it.

###### Topics

- [Identifying the Amazon S3 bucket for export](#export-cluster-data.SetupBucket "#export-cluster-data.SetupBucket")
- [Providing access to an Amazon S3 bucket using an IAM role](#export-cluster-data.SetupIAMRole "#export-cluster-data.SetupIAMRole")
- [Using a cross-account Amazon S3 bucket](#export-cluster-data.Setup.XAcctBucket "#export-cluster-data.Setup.XAcctBucket")

## Identifying the Amazon S3 bucket for export

Identify the Amazon S3 bucket to export the DB cluster data to. Use an existing S3 bucket or create a new S3 bucket.

###### Note

The S3 bucket must be in the same AWS Region as the DB cluster.

For more information about working with Amazon S3 buckets, see the following in the
_Amazon Simple Storage Service User Guide_:

- [How do I view the
  properties for an S3 bucket?](../../../AmazonS3/latest/user-guide/view-bucket-properties.md "../../../AmazonS3/latest/user-guide/view-bucket-properties.md")
- [How do I enable
  default encryption for an Amazon S3 bucket?](../../../AmazonS3/latest/user-guide/default-bucket-encryption.md "../../../AmazonS3/latest/user-guide/default-bucket-encryption.md")
- [How do I create an S3
  bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md")

## Providing access to an Amazon S3 bucket using an IAM role

Before you export DB cluster data to Amazon S3, give the export tasks write-access permission to the Amazon S3 bucket.

To grant this permission, create an IAM policy that provides access to the bucket, then create an IAM role and attach
the policy to the role. Later, you can assign the IAM role to your DB cluster export task.

###### Important

If you plan to use the AWS Management Console to export your DB cluster, you can choose to create the IAM policy and the role
automatically when you export the DB cluster. For instructions, see [Creating DB cluster export tasks](export-cluster-data.md "export-cluster-data.md").

###### To give tasks access to Amazon S3

1. Create an IAM policy. This policy provides the bucket and object permissions that allow your DB cluster export
   task to access Amazon S3.

In the policy, include the following required actions to allow the transfer of files from Amazon Aurora to an S3
bucket:

    * `s3:PutObject*`
    * `s3:GetObject*`
    * `s3:ListBucket`
    * `s3:DeleteObject*`
    * `s3:GetBucketLocation`

In the policy, include the following resources to identify the S3 bucket and objects in the bucket. The following
list of resources shows the Amazon Resource Name (ARN) format for accessing Amazon S3.

    * `arn:aws:s3:::`amzn-s3-demo-bucket``
    * `arn:aws:s3:::`amzn-s3-demo-bucket`/*`

For more information about creating an IAM policy for Amazon Aurora, see [Creating and using an IAM policy for
IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md"). See also [Tutorial: Create and attach your
first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the _IAM User Guide_.

The following AWS CLI command creates an IAM policy named `ExportPolicy` with these options. It grants
access to a bucket named `amzn-s3-demo-bucket`.

###### Note

After you create the policy, note the ARN of the policy. You need the ARN for a subsequent step when you
attach the policy to an IAM role.

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

2. Create an IAM role, so that Aurora can assume this IAM role on your behalf to access your Amazon S3 buckets. For
   more information, see [Creating
   a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

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

The following AWS CLI command attaches the policy created earlier to the role named `rds-s3-export-role`.
Replace `your-policy-arn` with the policy ARN that you noted in an earlier
step.

```
aws iam attach-role-policy  --policy-arn `your-policy-arn`  --role-name rds-s3-export-role
```

## Using a cross-account Amazon S3 bucket

You can use S3 buckets across AWS accounts. For more information, see [Using a cross-account Amazon S3 bucket](aurora-export-snapshot.md#aurora-export-snapshot.Setup.XAcctBucket "aurora-export-snapshot.md#aurora-export-snapshot.Setup.XAcctBucket").

# Step 2: Set up Amazon Rekognition Custom Labels console permissions

To use the Amazon Rekognition console you need add to have appropriate permissions. If you want to
store your training files in a bucket other than the
[console bucket](su-create-console-bucket.md "su-create-console-bucket.md"), you need additional permissions.

###### Topics

- [Allowing console access](#su-console-access "#su-console-access")
- [Accessing external Amazon S3 Buckets](#su-external-buckets "#su-external-buckets")
- [Assigning permissions](#su-assign-permissions "#su-assign-permissions")

## Allowing console access

To use the Amazon Rekognition Custom Labels console, you need the following IAM policy that covers
Amazon S3, SageMaker AI Ground Truth, and Amazon Rekognition Custom Labels. For information about assigning
permissions, see [Assigning permissions](#su-assign-permissions "#su-assign-permissions").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "s3Policies",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:CreateBucket",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectVersion",
 "s3:GetObjectTagging",
 "s3:GetBucketVersioning",
 "s3:GetObjectVersionTagging",
 "s3:PutBucketCORS",
 "s3:PutLifecycleConfiguration",
 "s3:PutBucketPolicy",
 "s3:PutObject",
 "s3:PutObjectTagging",
 "s3:PutBucketVersioning",
 "s3:PutObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::custom-labels-console-*"

 ]
 },
 {
 "Sid": "rekognitionPolicies",
 "Effect": "Allow",
 "Action": [
 "rekognition:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "groundTruthPolicies",
 "Effect": "Allow",
 "Action": [
 "groundtruthlabeling:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Accessing external Amazon S3 Buckets

When you first open the Amazon Rekognition Custom Labels console in a new AWS Region, Amazon Rekognition Custom Labels creates a bucket
(console bucket) that's used to store project files. Alternatively, you can use
your own Amazon S3 bucket (external bucket) to upload the images or manifest file to the console. To use
an external bucket, add the following policy
block to the preceding policy. Replace `amzn-s3-demo-bucket` with the name of the bucket.

```
        {
            "Sid": "s3ExternalBucketPolicies",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:GetObjectVersion",
                "s3:GetObjectTagging",
                "s3:ListBucket",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`*"
            ]
        }
```

## Assigning permissions

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

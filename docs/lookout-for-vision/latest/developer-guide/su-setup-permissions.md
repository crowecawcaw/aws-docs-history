End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Step 2: Set up permissions

To use Amazon Lookout for Vision, you needs access permissions to the Lookout for Vision console, AWS SDK operations,
and the Amazon S3 bucket that you use for model training.

###### Note

If you only use AWS SDK operations, you can use policies that are scoped to AWS SDK operations.
For more information, see [Set up SDK permissions](su-sdk-permissions.md "su-sdk-permissions.md").

###### Topics

- [Setting console access with AWS managed policies](#su-console-managed-policies "#su-console-managed-policies")
- [Setting Amazon S3 bucket permissions](#su-non-console-buckets "#su-non-console-buckets")
- [Assigning permissions](#su-assign-permissions "#su-assign-permissions")

## Setting console access with AWS managed policies

Use the following AWS managed policies to apply appropriate access permissions for the Amazon Lookout for Vision console
and SDK operations.

- [AmazonLookoutVisionConsoleFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess") — allows full access to the
  Amazon Lookout for Vision console and SDK operations. You need `AmazonLookoutVisionConsoleFullAccess` permissions to
  create the console bucket. For more information, see [Step 3: Create the console bucket](su-create-console-bucket.md "su-create-console-bucket.md").
- [AmazonLookoutVisionConsoleReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess")— allows read-only
  access to the Amazon Lookout for Vision console and SDK operations.

To assign permissions, see [Assigning permissions](#su-assign-permissions "#su-assign-permissions").

For information about AWS managed policies, see
[AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Setting Amazon S3 bucket permissions

Amazon Lookout for Vision uses an Amazon S3 bucket to store the following files:

- Dataset images — Images that are used to train a model. For more information,
  see [Creating your dataset](model-create-dataset.md "model-create-dataset.md").
- Amazon SageMaker AI Ground Truth format manifest files. For example,
  the manifest file output from SageMaker AI GroundTruth job.
  For more information, see [Creating a dataset using an Amazon SageMaker AI
  Ground Truth manifest file](create-dataset-ground-truth.md "create-dataset-ground-truth.md").
- The output from model training.

If you use the console, Lookout for Vision creates an Amazon S3 bucket (console bucket) to manage your projects.
The `LookoutVisionConsoleReadOnlyAccess` and
`LookoutVisionConsoleFullAccess` managed policies include Amazon S3 access permissions for the console bucket.

You can use the console bucket to store dataset images and SageMaker AI Ground Truth format manifest files. Alternatively,
You can use a different Amazon S3 bucket.
The bucket must be owned by your AWS account and
must be located in the AWS Region in which you are using Lookout for Vision.

To use a different bucket, add the following policy to the desired user or group.
Replace `amzn-s3-demo-bucket` with the name of the desired bucket. For information about adding IAM policies, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionS3BucketAccessPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 },
 {
 "Sid": "LookoutVisionS3ObjectAccessPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

To assign permissions, see [Assigning permissions](#su-assign-permissions "#su-assign-permissions").

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

End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Set up SDK permissions

To use Amazon Lookout for Vision
SDK operations, you need access permissions to the Lookout for Vision API and the Amazon S3 bucket used
for model training.

###### Topics

- [Granting SDK operation permissions](#su-sdk-managed-policies "#su-sdk-managed-policies")
- [Granting Amazon S3 Bucket permissions](#su-sdk-bucket-permissions "#su-sdk-bucket-permissions")
- [Assigning permissions](#su-sdk-assign-permissions "#su-sdk-assign-permissions")

## Granting SDK operation permissions

We recommend that you grant only the permissions required to perform a task
(least-privilege permissions). For example, to call [DetectAnomalies](../APIReference/API_DetectAnomalies.md "../APIReference/API_DetectAnomalies.md"), you need permission to perform
`lookoutvision:DetectAnomalies`. To find the permissions for an
operation, check the [API reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

When you are just starting out with an application, you might not know the
specific permissions you need, so you can start with broader permissions. AWS
managed policies provide permissions to help you get started.

- [AmazonLookoutVisionFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionFullAccess") — allows full access to
  Amazon Lookout for Vision SDK operations.
- [AmazonLookoutVisionReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess") — allows access to the read-only
  SDK operations.

The managed policies for the console also provide access permissions for SDK operations. For more information,
see [Step 2: Set up permissions](su-setup-permissions.md "su-setup-permissions.md").

For information about AWS managed policies, see
[AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

When you know the permissions that your application needs, reduce
permissions further by defining customer managed policies specific to your
use cases. For more information, see [Customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies").

###### Note

The getting started instructions require `s3:PutObject` permissions. For more information, see
[Step 1: Create the manifest file and upload images](getting-started.md#getting-started-prepare-files "getting-started.md#getting-started-prepare-files").

To assign permissions, see [Assigning permissions](#su-sdk-assign-permissions "#su-sdk-assign-permissions").

## Granting Amazon S3 Bucket permissions

To train a model, you need an Amazon S3 bucket with appropriate permissions to store
the images, manifest files and training output.
The bucket must be owned by your AWS account and must be located in the
AWS Region in which you are using Amazon Lookout for Vision.

The SDK-only managed policies (`AmazonLookoutVisionFullAccess` and `AmazonLookoutVisionReadOnlyAccess`)
don't include Amazon S3 bucket permissions and you need to apply the following permission policy to access the buckets you use,
including existing console buckets.

The console managed policies (`AmazonLookoutVisionConsoleFullAccess` and `AmazonLookoutVisionConsoleReadOnlyAccess`)
include access permissions to the console bucket. If you are accessing
the console bucket with SDK operations and have console managed policy permissions, you don't need
to use the following policy. For more information,
see [Step 2: Set up permissions](su-setup-permissions.md "su-setup-permissions.md").

### Deciding task permissions

Use the following information to decide which permissions are needed for the tasks you
want to do.

#### Creating a dataset

To create a dataset with [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md"), you need the following permissions.

- `s3:GetBucketLocation` — allows Lookout for Vision to validate that
  your bucket is in the same region in which you are using Lookout for Vision.
- `s3:GetObject` — Allows access to the manifest file specifed in the `DatasetSource`
  input parameter. If you want to specify an exact S3
  object version of the manifest file, you also need `s3:GetObjectVersion` on the manifest file.
  For more information,
  see [Using versioning in S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md").

#### Creating a model

To create a model with [CreateModel](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md"),
you need the following permissions.

- `s3:GetBucketLocation` — allows Lookout for Vision to validate that
  your bucket is in the same region in which you are using Lookout for Vision.
- `s3:GetObject` — allows access to the images specified in
  the project’s training and test datasets.
- `s3:PutObject` — allows permission to store training output
  in the specified bucket. You specify the output bucket location in the `OutputConfig`
  parameter. Optionally, you can scope permissions down to only object keys specified in the
  `Prefix` field of the `S3Location` input field. For more information, see
  [OutputConfig](../APIReference/API_OutputConfig.md "../APIReference/API_OutputConfig.md").

#### Accessing images, manifest files, and training output

Amazon S3 bucket permissions aren't required to view Amazon Lookout for Vision operation responses. You do need
`s3:GetObject` permission if you want to access images, manifests files,
and training output referenced in operation responses. If you are accessing a versioned Amazon S3 object,
you need `s3:GetObjectVersion` permission.

### Setting Amazon S3 bucket policy

You can use the following policy to specify the Amazon S3 bucket permissions needed to
create a dataset (`CreateDataset`), create a model (`CreateModel`),
and access images, manifest files, and training output.
Change the value of `amzn-s3-demo-bucket` to the name of the bucket
that you want use.

You can adjust the policy to your needs. For more information, see
[Deciding task permissions](#su-sdk-permissions-tasks "#su-sdk-permissions-tasks").
Add the policy to the desired user. For more information, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionS3BucketAccess",
 "Effect": "Allow",
 "Action": "s3:GetBucketLocation",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Condition": {
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 },
 {
 "Sid": "LookoutVisionS3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "Bool": {
 "aws:ViaAWSService": "true"
 }
 }
 }
 ]
}`

```

To assign permissions, see [Assigning permissions](#su-sdk-assign-permissions "#su-sdk-assign-permissions").

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

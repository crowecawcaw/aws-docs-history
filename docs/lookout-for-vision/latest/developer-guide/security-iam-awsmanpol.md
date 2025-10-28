End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# AWS managed policies for Amazon Lookout for Vision

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AmazonLookoutVisionReadOnlyAccess

Use the `AmazonLookoutVisionReadOnlyAccess` policy to allow users
read-only access to Amazon Lookout for Vision (and its dependencies) with the following Amazon Lookout for Vision
actions (SDK operations). For example, you can use `DescribeModel` to get
information about an existing model.

- [DescribeDataset](../APIReference/API_DescribeDataset.md "../APIReference/API_DescribeDataset.md")
- [DescribeModel](../APIReference/API_DescribeModel.md "../APIReference/API_DescribeModel.md")
- [DescribeModelPackagingJob](../APIReference/API_DescribeModelPackagingJob.md "../APIReference/API_DescribeModelPackagingJob.md")
- [DescribeProject](../APIReference/API_DescribeProject.md "../APIReference/API_DescribeProject.md")
- [ListDatasetEntries](../APIReference/API_ListDatasetEntries.md "../APIReference/API_ListDatasetEntries.md")
- [ListModelPackagingJobs](../APIReference/API_ListModels.md "../APIReference/API_ListModels.md")
- [ListModels](../APIReference/API_ListModels.md "../APIReference/API_ListModels.md")
- [ListProjects](../APIReference/API_ListProjects.md "../APIReference/API_ListProjects.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")

To call read-only actions, users don't need Amazon S3 bucket permissions. However,
operation responses might include references to Amazon S3 buckets. For example, the
`source-ref` entry in the response from `ListDatasetEntries` is
a reference to an image in an Amazon S3 bucket. Add Amazon S3 bucket permissions if your users
need to access referenced buckets. For example, a user might want to download an image
referenced by a `source-ref` field. For more information, see [Granting Amazon S3 Bucket permissions](su-sdk-permissions.md#su-sdk-bucket-permissions "su-sdk-permissions.md#su-sdk-bucket-permissions").

You can attach the `AmazonLookoutVisionReadOnlyAccess` policy to your
IAM identities.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "lookoutvision:DescribeDataset",
 "lookoutvision:DescribeModel",
 "lookoutvision:DescribeProject",
 "lookoutvision:DescribeModelPackagingJob",
 "lookoutvision:ListDatasetEntries",
 "lookoutvision:ListModels",
 "lookoutvision:ListProjects",
 "lookoutvision:ListTagsForResource",
 "lookoutvision:ListModelPackagingJobs"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonLookoutVisionFullAccess

Use the `AmazonLookoutVisionFullAccess` policy to allow users full
access to Amazon Lookout for Vision (and its dependencies) with Amazon Lookout for Vision actions (SDK operations).
For example, you can train a model without having to use the Amazon Lookout for Vision console. For
more information, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

To create a dataset (`CreateDataset`) or create a model
(`CreateModel`), your users must have full access permissions to the Amazon S3
bucket that stores dataset images, Amazon SageMaker AI Ground Truth manifest files, and training
output. For more information, see [Step 2: Set up permissions](su-setup-permissions.md "su-setup-permissions.md").

You can also give permission to Amazon Lookout for Vision SDK actions by using the
`AmazonLookoutVisionConsoleFullAccess` policy.

You can attach the `AmazonLookoutVisionFullAccess` policy to your IAM identities.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionFullAccess",
 "Effect": "Allow",
 "Action": [
 "lookoutvision:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonLookoutVisionConsoleFullAccess

Use the `AmazonLookoutVisionFullAccess` policy to allow users full
access to the Amazon Lookout for Vision console, actions (SDK operations), and any dependencies that
the service has. For more information, see [Getting started with Amazon Lookout for Vision](getting-started.md "getting-started.md").

The `LookoutVisionConsoleFullAccess` policy includes permissions to
your Amazon Lookout for Vision console bucket. For information about the console bucket, see [Step 3: Create the console bucket](su-create-console-bucket.md "su-create-console-bucket.md"). To
store datasets, images, and Amazon SageMaker AI Ground Truth manifest files in a different Amazon S3
bucket, your users need additional permissions. For more information, see [Setting Amazon S3 bucket permissions](su-setup-permissions.md#su-non-console-buckets "su-setup-permissions.md#su-non-console-buckets").

You can attach the `AmazonLookoutVisionConsoleFullAccess` policy to your IAM identities.

###### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided:

- `LookoutVisionFullAccess` – Allows access to perform all Lookout for Vision
  actions.
- `LookoutVisionConsoleS3BucketSearchAccess` – Allows listing of all Amazon S3
  buckets owned by the caller. Lookout for Vision uses this action to identify the AWS
  Region-specific Lookout for Vision console bucket, if one exists in the caller’s
  account.
- `LookoutVisionConsoleS3BucketFirstUseSetupAccessPermissions` – Allows
  creating and configuring Amazon S3 buckets that match the Lookout for Vision console bucket name
  pattern. Lookout for Vision uses these actions to create and configure a Region-specific
  Lookout for Vision console bucket when it can't find one.
- `LookoutVisionConsoleS3BucketAccess` – Allows dependent Amazon S3 actions on
  buckets that match the Lookout for Vision console bucket name pattern. Lookout for Vision uses
  `s3:ListBucket` to search for image objects when creating a dataset
  from an Amazon S3 bucket and when starting a trial detection task. Lookout for Vision uses
  `s3:GetBucketLocation` and `s3:GetBucketVersioning` to
  validate the bucket's AWS Region, owner, and configuration as part of the
  following:

      + Creating a dataset
      + Training a model
      + Starting a trial detection task
      + Performing trial detection feedback

  `LookoutVisionConsoleS3ObjectAccess` – Allows reading and
  writing of Amazon S3 objects inside buckets that match the Lookout for Vision Console bucket name
  pattern. Lookout for Vision uses these actions to display images in console gallery views and
  to upload new images for use in datasets. Additionally, these permissions allow
  Lookout for Vision to write out metadata while creating a dataset, training a model, starting
  a trial detection task, and performing trial detection feedback.

- `LookoutVisionConsoleDatasetLabelingToolsAccess` – Allows dependent Amazon SageMaker AI
  GroundTruth labeling actions. Lookout for Vision uses these actions to scan S3 buckets for
  images, create GroundTruth manifest files, and to annotate trial detection task
  results with validation labels.
- `LookoutVisionConsoleDashboardAccess` - Allows reading of Amazon CloudWatch metrics. Lookout for Vision
  uses these actions to populate the dashboard graphs and anomalies-detected
  statistics.
- `LookoutVisionConsoleTagSelectorAccess` – Allows reading account-specific
  tag key and tag value suggestions. Lookout for Vision uses these permissions to provide
  recommendations for tag keys and tag values within the **Manage
  tags** console pages.
- `LookoutVisionConsoleKmsKeySelectorAccess` – Allows listing AWS Key Management Service (KMS)
  keys and aliases. Amazon Lookout for Vision uses this permission to populate the KMS keys in the
  suggested **Tags** selection on certain Lookout for Vision actions that
  support customer managed KMS keys for encryption.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionFullAccess",
 "Effect": "Allow",
 "Action": [
 "lookoutvision:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleS3BucketSearchAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleS3BucketFirstUseSetupAccess",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutBucketVersioning",
 "s3:PutLifecycleConfiguration",
 "s3:PutEncryptionConfiguration",
 "s3:PutBucketPublicAccessBlock"
 ],
 "Resource": "arn:aws:s3:::lookoutvision-*"
 },
 {
 "Sid": "LookoutVisionConsoleS3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetBucketAcl",
 "s3:GetBucketVersioning"
 ],
 "Resource": "arn:aws:s3:::lookoutvision-*"
 },
 {
 "Sid": "LookoutVisionConsoleS3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": "arn:aws:s3:::lookoutvision-*/*"
 },
 {
 "Sid": "LookoutVisionConsoleDatasetLabelingToolsAccess",
 "Effect": "Allow",
 "Action": [
 "groundtruthlabeling:RunGenerateManifestByCrawlingJob",
 "groundtruthlabeling:AssociatePatchToManifestJob",
 "groundtruthlabeling:DescribeConsoleJob"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleDashboardAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleTagSelectorAccess",
 "Effect": "Allow",
 "Action": [
 "tag:GetTagKeys",
 "tag:GetTagValues"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleKmsKeySelectorAccess",
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonLookoutVisionConsoleReadOnlyAccess

Use the `AmazonLookoutVisionConsoleReadOnlyAccess` policy to allow
users read-only access to the Amazon Lookout for Vision console, actions (SDK operations), and any
dependencies that the service has.

The `AmazonLookoutVisionConsoleReadOnlyAccess` policy includes Amazon S3
permissions for the Amazon Lookout for Vision console bucket. If your dataset images or Amazon SageMaker AI Ground
Truth manifest files are in a different Amazon S3 bucket, your users need additional
permissions. For more information, see [Setting Amazon S3 bucket permissions](su-setup-permissions.md#su-non-console-buckets "su-setup-permissions.md#su-non-console-buckets").

You can attach the `AmazonLookoutVisionConsoleReadOnlyAccess` policy to your IAM identities.

###### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided:

- `LookoutVisionReadOnlyAccess` – Allows access to perform read-only Lookout for Vision
  actions.
- `LookoutVisionConsoleS3BucketSearchAccess` – Allows listing of all S3
  buckets owned by the caller. Lookout for Vision uses this action to identify the AWS
  Region-specific Lookout for Vision console bucket, if there is one in the caller’s account.
- `LookoutVisionConsoleS3ObjectReadAccess` – Allows reading Amazon S3 objects and
  Amazon S3 object versions in Lookout for Vision console buckets. Lookout for Vision uses these actions to
  display the images in datasets, models, and trial detections.
- `LookoutVisionConsoleDashboardAccess` – Allows reading Amazon CloudWatch metrics.
  Lookout for Vision uses these actions to populate statistics for dashboard graphs and
  anomalies detected.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LookoutVisionReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "lookoutvision:DescribeDataset",
 "lookoutvision:DescribeModel",
 "lookoutvision:DescribeProject",
 "lookoutvision:DescribeTrialDetection",
 "lookoutvision:DescribeModelPackagingJob",
 "lookoutvision:ListDatasetEntries",
 "lookoutvision:ListModels",
 "lookoutvision:ListProjects",
 "lookoutvision:ListTagsForResource",
 "lookoutvision:ListTrialDetections",
 "lookoutvision:ListModelPackagingJobs"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleS3BucketSearchAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LookoutVisionConsoleS3ObjectReadAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::lookoutvision-*/*"
 },
 {
 "Sid": "LookoutVisionConsoleDashboardAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Lookout for Vision updates to AWS managed

policies

View details about updates to AWS managed policies for Lookout for Vision since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the Lookout for Vision Document history page.

| Change                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Date               |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Model packaging operations added            | Amazon Lookout for Vision added the following model packaging operations to the [AmazonLookoutVisionFullAccess](#security-iam-awsmanpol-AmazonLookoutVisionFullAccess "#security-iam-awsmanpol-AmazonLookoutVisionFullAccess") and [AmazonLookoutVisionConsoleFullAccess](#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess "#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess") policies: <br>• [DescribeModelPackagingJob](../APIReference/API_DescribeModelPackagingJob.md "../APIReference/API_DescribeModelPackagingJob.md") <br>• [ListModelPackagingJobs](../APIReference/API_ListModelPackagingJobs.md "../APIReference/API_ListModelPackagingJobs.md") <br>• [StartModelPackagingJob](../APIReference/API_StartModelPackagingJob.md "../APIReference/API_StartModelPackagingJob.md") Amazon Lookout for Vision added the following model packaging operations to the [AmazonLookoutVisionReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess") and [AmazonLookoutVisionConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess") policies: <br>• [DescribeModelPackagingJob](../APIReference/API_DescribeModelPackagingJob.md "../APIReference/API_DescribeModelPackagingJob.md") <br>• [ListModelPackagingJobs](../APIReference/API_ListModelPackagingJobs.md "../APIReference/API_ListModelPackagingJobs.md") | December 7th, 2021 |
| New policies added                          | Amazon Lookout for Vision added the following policies. <br>• [AmazonLookoutVisionReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutVisionReadOnlyAccess") <br>• [AmazonLookoutVisionFullAccess](#security-iam-awsmanpol-AmazonLookoutVisionFullAccess "#security-iam-awsmanpol-AmazonLookoutVisionFullAccess") <br>• [AmazonLookoutVisionConsoleFullAccess](#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess "#security-iam-awsmanpol-AmazonLookoutVisionConsoleFullAccess") <br>• [AmazonLookoutVisionConsoleReadOnlyAccess](#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess "#security-iam-awsmanpol-AmazonLookoutVisionConsoleReadOnlyAccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | May 11th, 2021     |
| Lookout for Vision started tracking changes | Amazon Lookout for Vision started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | March 1st, 2021    |

# Associating a dataset for use in AWS Clean Rooms ML

A _configured dataset association_ (dataset) is a
way to bring data stored in Amazon S3 into a collaboration for ML training or inference.
Unlike ML input channels, which use SQL queries on structured or tabular data,
datasets point directly to Amazon S3 objects such as images, documents, audio, video,
or other files.

As a data provider, you create datasets to share data with a collaboration. As a
model owner, you reference these datasets in training or inference jobs. When a job runs,
AWS Clean Rooms ML temporarily copies the data to service-managed storage for processing
and cleans up after the job completes. Your source data is never modified. Data in
service-managed storage is encrypted at rest. By default, Amazon S3 managed encryption
(SSE-S3) is used. For more information about encrypting data with a customer managed AWS KMS key, see
[Encryption for configured dataset associations](data-protection.md#encryption-cda "data-protection.md#encryption-cda").

After you associate a dataset, model owners can use it when [Creating a trained model in AWS Clean Rooms ML](create-trained-model.md "create-trained-model.md") or [Running inference on a trained model in AWS Clean Rooms ML](run-inference-jobs.md "run-inference-jobs.md").

###### Important

Datasets and ML input channels are mutually exclusive. A training or inference
job uses one or the other, not both.

###### Prerequisites

- An active collaboration membership with ML custom model capabilities
- Data stored in Amazon S3
- Your Amazon S3 bucket must be in the same AWS Region as the collaboration.
- An IAM role that grants AWS Clean Rooms and AWS Clean Rooms ML access to your data. For
  more information, see [IAM role for configured dataset associations](#cda-iam-role "#cda-iam-role").
- At least one configured model algorithm association in the collaboration
  (for the privacy configuration allowlist)
- (Optional) A customer managed AWS KMS key for encrypting data in
  service-managed storage

## Creating a configured dataset association

You can create a configured dataset association by using the AWS Clean Rooms console or
the API.

Console

###### To associate a dataset (console)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose your collaboration.
4. Choose the **ML models** tab.
5. In the **Datasets** section, choose
   **Associate dataset**.
6. Under **Details**, do the
   following:

   1. For **Name**, enter a name for
      your dataset (up to 100 characters).
   2. (Optional) For **Description**,
      enter a description (up to 255
      characters).

7. Under **Dataset**, enter the Amazon S3 URI for
   your data location (for example,
   `s3://bucket/prefix/`) or choose
   **Browse S3**.
8. Under **Privacy configuration**, for
   **Allowed models**, select one or more
   configured model algorithm associations that can use this
   dataset (maximum 10).
9. (Optional) Under **Encrypt at rest**,
   select the checkbox and specify an AWS KMS key to encrypt your
   data in service-managed storage. If you don't specify a key,
   Amazon S3 managed encryption (SSE-S3) is used.
10. Under **Service access**, choose one of
    the following:

    - **Create and use a new service
      role** – automatically creates a
      role with the necessary permissions
    - **Use an existing service
      role** – select from your
      existing roles

11. (Optional) If your source data in Amazon S3 is encrypted with a
    AWS KMS key, select **This dataset is encrypted with a
    KMS key** and specify the source AWS KMS key
    ARN.
12. (Optional) If you want to add tags, choose **Add
    new tag** and then enter the
    **Key** and **Value**
    pair.
13. Choose **Associate dataset**.

API
**To associate a dataset (API)**

Run the following AWS CLI command with your specific
parameters:

```
`aws cleanrooms create-configured-dataset-association \
 --membership-identifier `membership-id` \
 --name "`my-dataset`" \
 --description "`Dataset for ML training`" \
 --data-source '{
 "s3DataSource": {
 "s3Uri": "s3://`amzn-s3-demo-bucket`/`prefix`/"
 }
 }' \
 --role-arn "arn:aws:iam::`111122223333`:role/`CDAServiceRole`" \
 --privacy-configuration '{
 "configuredModelAlgorithmAssociationArns": [
 "arn:aws:cleanrooms-ml:`us-east-1`:`111122223333`:membership/`membership-id`/configured-model-algorithm-association/`association-id`"
 ]
 }' \
 --kms-key-arn "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"`
```

The `--kms-key-arn` and `--description`
parameters are optional. If you don't specify a AWS KMS key, Amazon S3
managed encryption (SSE-S3) is used.

On success, the API returns the ARN of the configured dataset
association.

## Viewing datasets

The information you can view about a dataset depends on whether you are the
dataset owner or another collaboration member.

- **As the dataset owner** – You can
  view full details including the Amazon S3 URI, role ARN, AWS KMS key, privacy
  configuration, and timestamps. Use the dataset detail page in the
  console or the `GetConfiguredDatasetAssociation` API
  operation.
- **As a collaboration member
  (non-owner)** – You can view the name, description,
  privacy configuration, and timestamps. You cannot view the Amazon S3 URI,
  role ARN, or AWS KMS key. Use the
  `GetCollaborationConfiguredDatasetAssociation` API
  operation or view the dataset in the console.

To list datasets, use
`ListConfiguredDatasetAssociations` (for your own membership) or
`ListCollaborationConfiguredDatasetAssociations` (for all
datasets in the collaboration).

## Editing a dataset

You can update the following properties of a configured dataset
association:

- Description
- Privacy configuration (allowed models)

You cannot update the name, Amazon S3 URI, role ARN, or AWS KMS key after creation.
To change these properties, delete the dataset and create a new one.

In the console, choose **Edit** from the dataset detail page.
With the API, use the `UpdateConfiguredDatasetAssociation`
operation.

## Deleting a dataset

In the console, choose **Delete** from the dataset detail
page and type `confirm` to confirm the deletion. With the
API, use the `DeleteConfiguredDatasetAssociation` operation.

###### Note

Deleting a dataset does not affect training or inference jobs that are
already in progress.

###### Note

You must delete all datasets in a membership before you can delete the
membership.

## IAM role for configured dataset associations

When you create a configured dataset association, you specify an IAM role
that grants AWS Clean Rooms ML permission to read your source data in Amazon S3 and copy it
to service-managed storage for processing. The console can automatically create
this role for you when you choose the **Create and use a new service
role** option, or you can create it manually.

### Trust policy

The trust policy allows the following service principals to assume the
role:

- `cleanrooms.amazonaws.com` – Validates the role
  at dataset creation time
- `cleanrooms-ml.amazonaws.com` – Accesses data
  during training and inference
- `batchoperations.s3.amazonaws.com` – Performs
  Amazon S3 Batch Operations to copy data to service-managed storage

The trust policy uses `aws:SourceAccount` and
`aws:SourceArn` conditions for confused deputy protection.

###### Note

In the following policy examples, replace all account ID and region
placeholders with the dataset owner's (data provider's) AWS account ID and
AWS Region.

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCleanRoomsAssumeWithCDP",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "cleanrooms.amazonaws.com",
 "cleanrooms-ml.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`ACCOUNT_ID`"
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:cleanrooms:`REGION`:`ACCOUNT_ID`:membership/`MEMBERSHIP_ID`/configureddatasetassociation/*"
 ]
 }
 }
 },
 {
 "Sid": "AllowS3BatchOperationsAssume",
 "Effect": "Allow",
 "Principal": {
 "Service": "batchoperations.s3.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`
```

### Permissions policy

The permissions policy grants the role access to read your source data,
write to service-managed storage, and manage Amazon S3 Batch Operations jobs.
The following is the base permissions policy without AWS KMS
permissions.

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`ACCOUNT_ID`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:PutInventoryConfiguration"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`ACCOUNT_ID`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::cleanrooms-cda-*",
 "arn:aws:s3:::cleanrooms-cda-*/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateJob",
 "s3:DescribeJob",
 "s3:UpdateJobStatus"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`ACCOUNT_ID`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "arn:aws:iam::`ACCOUNT_ID`:role/service-role/`ROLE_NAME`"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`ACCOUNT_ID`:role/service-role/`ROLE_NAME`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "s3.amazonaws.com"
 }
 }
 }
 ]
}`
```

The following table explains the purpose of each statement group in the
policy.

| Actions                                                      | Purpose                                                                                                   |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `s3:GetObject`,<br>`s3:GetObjectVersion`                     | Read objects from your source data bucket.                                                                |
| `s3:ListBucket`,<br>`s3:PutInventoryConfiguration`           | List objects and configure inventory on your source<br>bucket for batch processing.                       |
| `s3:GetObject`,<br>`s3:PutObject` (on<br>`cleanrooms-cda-*`) | Read and write data in service-managed Amazon S3 buckets<br>used for temporary storage during processing. |
| `s3:CreateJob`,<br>`s3:DescribeJob`,<br>`s3:UpdateJobStatus` | Create and manage Amazon S3 Batch Operations jobs that copy<br>data to service-managed storage.           |
| `iam:GetRole`                                                | Verify the role's own configuration.                                                                      |
| `iam:PassRole`                                               | Pass the role to Amazon S3 Batch Operations so it can<br>perform the copy job.                            |

### Optional AWS KMS permissions

If your source data or dataset uses AWS KMS encryption, add the
appropriate statements to the permissions policy. The AWS KMS statements you
need depend on your encryption configuration.

###### If your source data is encrypted with a customer managed AWS KMS key

Add the following statement to allow the role to decrypt your source
data:

```
`{
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`REGION`:`ACCOUNT_ID`:key/`SOURCE_KEY_ID`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`REGION`.amazonaws.com"
 }
 }
}`
```

###### If you specify a AWS KMS key for dataset encryption (CDA encryption key)

Add the following statement to allow the role to encrypt and decrypt data
in service-managed storage:

```
`{
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`REGION`:`ACCOUNT_ID`:key/`CDA_KEY_ID`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`REGION`.amazonaws.com"
 }
 }
}`
```

###### If both keys are the same key

If the source data encryption key and the CDA encryption key are the same
key, a single statement with both `kms:Decrypt` and
`kms:GenerateDataKey` on that key is sufficient.

###### Note

When you create a dataset in the console and choose **Create and
use a new service role**, the console automatically creates a role
with the required trust policy and permissions for your configuration.

## Privacy configuration for datasets

The privacy configuration controls which configured model algorithm
associations can use a dataset. Only algorithms on the allowlist can consume
the dataset during training or inference.

- You can specify a maximum of 10 configured model algorithm association
  ARNs per dataset.
- The allowlist is enforced at job creation time as a point-in-time
  check.
- You can update the allowlist at any time. Changes do not affect jobs
  that are already in progress.

## Limits for configured dataset associations

The following limits apply to configured dataset associations and their usage in
training and inference jobs:

| Limit                              | Value                                                  |
| ---------------------------------- | ------------------------------------------------------ |
| Maximum dataset size               | 25 TB                                                  |
| Maximum individual object size     | 5 GB                                                   |
| Maximum object size for inference  | 100 MB per object                                      |
| Maximum datasets per training job  | 20 (or 19 datasets and 1 incremental training channel) |
| Maximum datasets per inference job | 1                                                      |

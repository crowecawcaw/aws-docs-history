# Exporting mailbox content

Use the [StartMailboxExportJob](../APIReference/API_StartMailboxExportJob.md "../APIReference/API_StartMailboxExportJob.md") API action in the _Amazon WorkMail API Reference_
to export Amazon WorkMail mailbox content to an Amazon Simple Storage Service (Amazon S3) bucket. This action exports all email
messages and calendar items from the specified mailbox to a `.zip` file
in the Amazon S3 bucket, in MIME format. Other items, such as contacts and tasks, are not
exported.

The time it takes for the mailbox export job to finish is dependent on the size and number of items in the mailbox. Because the mailbox export job takes place over a period of time, it does not
represent a snapshot of the mailbox content at a single point in time. To see the status of an export job, use the
[DescribeMailboxExportJob](../APIReference/API_DescribeMailboxExportJob.md "../APIReference/API_DescribeMailboxExportJob.md") or
[ListMailboxExportJobs](../APIReference/API_ListMailboxExportJobs.md "../APIReference/API_ListMailboxExportJobs.md") API actions in the _Amazon WorkMail API Reference_.

When a mailbox export job is completed, the `.zip` file in the Amazon S3 bucket is encrypted using the symmetric AWS Key Management Service (AWS KMS) customer master key (CMK) that you provide.
Because AWS KMS encryption is integrated with Amazon S3, the decrypted data is visible to the user who downloads it, as long as the user has access to the AWS KMS CMK.

## Prerequisites

The following are prerequisites for exporting mailbox content:

- The ability to program.
- An Amazon WorkMail administrator account.
- An Amazon S3 bucket that does not allow public access. For more information, see [Using Amazon S3 block public access](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_ and the _[Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_.
- A symmetric AWS KMS CMK. For more information, see [Getting started](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in the _AWS Key Management Service Developer Guide_.
- An AWS Identity and Access Management (IAM) role with a policy that grants permission to write to the
  Amazon S3 bucket and encrypt the sent files with the AWS KMS CMK. For more information, see
  [How Amazon WorkMail works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

## IAM policy examples and role creation

The following example shows an IAM policy that grants permission to write to the Amazon S3 bucket and encrypt the sent files with the AWS KMS CMK. To use this example policy in the following
[Example: Exporting mailbox content](#example-export-mailbox "#example-export-mailbox") procedure, save the policy as a JSON file with file name `mailbox-export-policy.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:GetBucketPolicyStatus"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KEY-ID`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 },
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`amzn-s3-demo-bucket`/`S3-PREFIX`*"
 }
 }
 }
 ]
}`

```

The following example shows an IAM trust policy that is attached to the IAM role you create. To use this example policy in the following [Example: Exporting mailbox content](#example-export-mailbox "#example-export-mailbox") procedure,
save the policy as a JSON file with file name
`mailbox-export-trust-policy.json`.

You don’t have to use the `aws:SourceArn` and `aws:SourceAccount` conditions at the same time. For example, you can remove `aws:SourceArn`
from the policy if you need to use the same role to export messages from different Amazon WorkMail organizations under the same AWS account. For more information about condition keys, refer to the
[AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _AWS Identity and Access Management user guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "export.workmail.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:workmail:`us-east-1`:`111122223333`:organization/`m-a123b4c5de678fg9h0ij1k2lm234no56`"
 }
 }
 }
 ]
}`

```

You can use the AWS CLI to create the IAM role in your account by running the
following commands.

```
aws iam create-role --role-name `WorkmailMailboxExportRole` --assume-role-policy-document `file://mailbox-export-trust-policy.json` --region `us-east-1`
```

```
aws iam put-role-policy --role-name `WorkmailMailboxExportRole` --policy-name `MailboxExport` --policy-document `file://mailbox-export-policy.json`
```

For more information about the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

## Example: Exporting mailbox content

After you create the IAM role and policies in the preceding section,
complete the following steps to export your mailbox content. You must have your Amazon WorkMail
organization ID and user ID (entity ID), which you can access in the Amazon WorkMail console or by
using the Amazon WorkMail API.

###### Example: To export mailbox content

1. Use the AWS CLI to start the mailbox export job.

```
aws workmail start-mailbox-export-job --organization-id `m-a123b4c5de678fg9h0ij1k2lm234no56` --entity-id `S-1-1-11-1111111111-2222222222-3333333333-3333` --kms-key-arn arn:aws:kms:`us-east-1`:`111122223333`:key/`KEY-ID` --role-arn arn:aws:iam::`111122223333`:role/`WorkmailMailboxExportRole` --s3-bucket-name `amzn-s3-demo-bucket` --s3-prefix `S3-PREFIX`
```

2. Use the AWS CLI to monitor the state of the mailbox export jobs for your Amazon WorkMail organization.

```
aws workmail list-mailbox-export-jobs --organization-id `m-a123b4c5de678fg9h0ij1k2lm234no56`
```

Alternatively, use the job ID generated by the `start-mailbox-export-job` command to monitor the state of that mailbox export job only.

```
aws workmail describe-mailbox-export-job --organization-id `m-a123b4c5de678fg9h0ij1k2lm234no56` --job-id `JOB-ID`
```

When the mailbox export job state is **COMPLETED**, the exported mailbox items are available in a `.zip` file in the specified Amazon S3 bucket.

The following is an example of the output log from the exported mailbox:

```

{
  "totalNonExportableItems" : "13",
  "totalMessages" : "76",
  "sha384Hash" : "4de93a***96a1dd",
  "totalBytes" : "161892",
  "totalFolders" : "15",
  "startTime" : "168***380",
  "endTime" : "168***384"
}

```

###### Note

_totalNonExportableItems_ are unsupported items like notes and contacts.

## Considerations

The following considerations apply when exporting mailbox jobs for Amazon WorkMail:

- You can run up to 10 concurrent mailbox export jobs for a given Amazon WorkMail organization.
- You can run a mailbox export job for a given mailbox as often as once every 24 hours.
- The following resources must all be in the same AWS Region:
  - Amazon WorkMail organization
  - AWS KMS CMK
  - Amazon S3 bucket

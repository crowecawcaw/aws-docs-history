# Configuring replication for buckets in different

accounts

Live replication is the automatic, asynchronous copying of objects across buckets in the
same or different AWS Regions. Live replication copies newly created objects and object
updates from a source bucket to a destination bucket or buckets. For more information, see
[Replicating objects within and across Regions](replication.md "replication.md").

When you configure replication, you add replication rules to the source bucket.
Replication rules define which source bucket objects to replicate and the destination bucket
or buckets where the replicated objects are stored. You can create a rule to replicate all
the objects in a bucket or a subset of objects with a specific key name prefix, one or more
object tags, or both. A destination bucket can be in the same AWS account as the source
bucket, or it can be in a different account.

If you specify an object version ID to delete, Amazon S3 deletes that object version in the
source bucket. But it doesn't replicate the deletion in the destination bucket. In other
words, it doesn't delete the same object version from the destination bucket. This protects
data from malicious deletions.

When you add a replication rule to a bucket, the rule is enabled by default, so it starts
working as soon as you save it.

Setting up live replication when the source and destination buckets are owned by different
AWS accounts is similar to setting up replication when both buckets are owned by the same
account. However, there are several differences when you're configuring replication in a
cross-account scenario:

- The destination bucket owner must grant the source bucket owner permission to
  replicate objects in the destination bucket policy.
- If you're replicating objects that are encrypted with server-side encryption with
  AWS Key Management Service (AWS KMS) keys (SSE-KMS) in a cross-account scenario, the owner of the
  KMS key must grant the source bucket owner permission to use the KMS key. For
  more information, see [Granting additional
  permissions for cross-account scenarios](replication-config-for-kms-objects.md#replication-kms-cross-acct-scenario "replication-config-for-kms-objects.md#replication-kms-cross-acct-scenario").
- By default, replicated objects are owned by the source bucket owner. In a
  cross-account scenario, you might want to configure replication to change the
  ownership of the replicated objects to the owner of the destination bucket. For more
  information, see [Changing the replica owner](replication-change-owner.md "replication-change-owner.md").

###### To configure replication when the source and destination buckets are owned by

different AWS accounts

1. In this example, you create source and destination buckets in two different
   AWS accounts. You must have two credential profiles set for the AWS CLI. This
   example uses `acctA` and `acctB` for those profile names. For
   information about setting credential profiles and using named profiles, see [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide_.
2. Follow the step-by-step instructions in
   [Configuring replication for buckets in the same
   account](replication-walkthrough1.md "replication-walkthrough1.md") with the
   following changes:
   - For all AWS CLI commands related to source bucket activities (such as
     creating the source bucket, enabling versioning, and creating the IAM
     role), use the `acctA` profile. Use the `acctB`
     profile to create the destination bucket.
   - Make sure that the permissions policy for the IAM role specifies the
     source and destination buckets that you created for this example.

3. In the console, add the following bucket policy on the destination bucket to allow
   the owner of the source bucket to replicate objects. For instructions, see [Adding a bucket policy by using the Amazon S3 console](add-bucket-policy.md "add-bucket-policy.md"). Be sure to edit
   the policy by providing the AWS account ID of the source bucket owner, the IAM
   role name, and the destination bucket name.

###### Note

To use the following example, replace the `user input
 placeholders` with your own information. Replace
`amzn-s3-demo-destination-bucket` with your destination bucket
name. Replace
``source-bucket-account-ID`:role/service-role/`source-account-IAM-role``
in the IAM Amazon Resource Name (ARN) with the IAM role that you're using
for this replication configuration.

If you created the IAM service role manually, set the role path in the IAM
ARN as `role/service-role/`, as shown in the following policy
example. For more information, see [IAM
ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "",
 "Statement": [
 {
 "Sid": "Set-permissions-for-objects",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/`source-account-IAM-role`"
 },
 "Action": [
 "s3:ReplicateObject",
 "s3:ReplicateDelete"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 },
 {
 "Sid": "Set-permissions-on-bucket",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/`source-account-IAM-role`"
 },
 "Action": [
 "s3:GetBucketVersioning",
 "s3:PutBucketVersioning"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
 }
 ]
}`

```

4. (Optional) If you're replicating objects that are encrypted with SSE-KMS, the
   owner of the KMS key must grant the source bucket owner permission to use the
   KMS key. For more information, see [Granting additional
   permissions for cross-account scenarios](replication-config-for-kms-objects.md#replication-kms-cross-acct-scenario "replication-config-for-kms-objects.md#replication-kms-cross-acct-scenario").
5. (Optional) In replication, the owner of the source object owns the replica by
   default. When the source and destination buckets are owned by different
   AWS accounts, you can add optional configuration settings to change replica
   ownership to the AWS account that owns the destination buckets. This includes
   granting the `ObjectOwnerOverrideToBucketOwner` permission. For more
   information, see [Changing the replica owner](replication-change-owner.md "replication-change-owner.md").

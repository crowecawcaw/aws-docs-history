# Using an inventory report to copy

objects across AWS accounts

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
You can use S3 Batch Operations to create a **Copy** (`CopyObject`) job
to copy objects within the same account or to a different destination account.

You can use Amazon S3 Inventory to create an inventory report and use the report to create a
list (manifest) of objects to copy with S3 Batch Operations. For more information about using a CSV
manifest in the source or destination account, see [Using a CSV manifest to copy objects
across AWS accounts](specify-batchjob-manifest-xaccount-csv.md "specify-batchjob-manifest-xaccount-csv.md").

Amazon S3 Inventory generates inventories of the objects in a bucket. The resulting list is
published to an output file. The bucket that is inventoried is called the source bucket, and the
bucket where the inventory report file is stored is called the destination bucket.

The Amazon S3 Inventory report can be configured to be delivered to another AWS account.
Doing so allows S3 Batch Operations to read the inventory report when the job is created in the
destination account.

For more information about Amazon S3 Inventory source and destination buckets, see [Source and destination buckets](storage-inventory.md#storage-inventory-buckets "storage-inventory.md#storage-inventory-buckets").

The easiest way to set up an inventory is by using the Amazon S3 console, but you can also use
the Amazon S3 REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs.

The following console procedure contains the high-level steps for setting up permissions
for an S3 Batch Operations job. In this procedure, you copy objects from a source account to a
destination account, with the inventory report stored in the destination account.

###### To set up Amazon S3 Inventory for source and destination buckets owned by different

accounts

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. Decide on (or create) a destination manifest bucket to store the inventory report in.
   In this procedure, the _destination account_ is the account that owns
   both the destination manifest bucket and the bucket that the objects are copied to.
4. Configure an inventory report for a source bucket. For information about how to use
   the console to configure an inventory or how to encrypt an inventory list file, see [Configuring Amazon S3 Inventory](configure-inventory.md "configure-inventory.md").

When you configure the inventory report, you specify the destination bucket where you
want the list to be stored. The inventory report for the source bucket is published to the
destination bucket. In this procedure, the _source account_ is the
account that owns the source bucket.

Choose **CSV** for the output format.

When you enter information for the destination bucket, choose **Buckets in
another account**. Then enter the name of the destination manifest bucket.
Optionally, you can enter the account ID of the destination account.

After the inventory configuration is saved, the console displays a message similar to
the following:

**`Amazon S3 could not create a bucket policy on the destination bucket. Ask the
 destination bucket owner to add the following bucket policy to allow Amazon S3 to place data in
 that bucket.`**

The console then displays a bucket policy that you can use for the destination
bucket. 5. Copy the destination bucket policy that appears on the console. 6. In the destination account, add the copied bucket policy to the destination manifest
bucket where the inventory report is stored. 7. Create a role in the destination account that is based on the S3 Batch Operations trust
policy. For more information about this trust policy, see [Trust policy](batch-ops-iam-role-policies.md#batch-ops-iam-role-policies-trust "batch-ops-iam-role-policies.md#batch-ops-iam-role-policies-trust").

For more information about creating a role, see [Creating a role to delegate
permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

Enter a name for the role (the following example role uses the name
`BatchOperationsDestinationRoleCOPY`). Choose the
**S3** service, and then choose the **S3 Batch Operations**
use case, which applies the trust policy to the role.

Then choose **Create policy** to attach the following policy to the
role. To use this policy, replace the `user input
 placeholders` with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`AllowBatchOperationsDestinationObjectCOPY`",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectVersionAcl",
 "s3:PutObjectAcl",
 "s3:PutObjectVersionTagging",
 "s3:PutObjectTagging",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:GetObjectVersionAcl",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket/*",
 "arn:aws:s3:::amzn-s3-demo-source-bucket/*",
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 }
 ]
}`

```

The role uses the policy to grant `batchoperations.s3.amazonaws.com`
permission to read the manifest in the destination bucket. It also grants permissions to
`GET` objects, access control lists (ACLs), tags, and versions in the source
object bucket. And it grants permissions to `PUT` objects, ACLs, tags, and
versions into the destination object bucket. 8. In the source account, create a bucket policy for the source bucket that grants the
role that you created in the previous step permissions to `GET` objects, ACLs,
tags, and versions in the source bucket. This step allows S3 Batch Operations to get objects from
the source bucket through the trusted role.

The following is an example of the bucket policy for the source account. To use this
policy, replace the `user input placeholders` with
your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`AllowBatchOperationsSourceObjectCOPY`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`BatchOperationsDestinationRoleCOPY`"
 },
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:GetObjectVersionAcl",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
 }
 ]
}`

```

9. After the inventory report is available, create an S3 Batch Operations
   **Copy** (`CopyObject`) job in the destination account, and
   choose the inventory report from the destination manifest bucket. You need the ARN for the
   IAM role that you created in the destination account.

For general information about creating a job, see [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").

For information about creating a job by using the console, see [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").

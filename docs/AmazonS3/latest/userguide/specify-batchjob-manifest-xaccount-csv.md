# Using a CSV manifest to copy objects across AWS accounts

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
You can use S3 Batch Operations to create a **Copy** (`CopyObject`) job
to copy objects within the same account or to a different destination account.

You can use a CSV manifest that's stored in the source account to copy objects across
AWS accounts with S3 Batch Operations. To use an S3 Inventory report as a manifest, see [Using an inventory report to copy objects across AWS accounts](specify-batchjob-manifest-xaccount-inventory.md "specify-batchjob-manifest-xaccount-inventory.md").

For an example of the CSV format for manifest files, see [Creating a manifest file](batch-ops-create-job.md#create-manifest-file "batch-ops-create-job.md#create-manifest-file").

The following procedure shows how to set up permissions when using an S3 Batch Operations job
to copy objects from a source account to a destination account with a CSV manifest file that's
stored in the source account.

###### To use a CSV manifest to copy objects across AWS accounts

1. Create an AWS Identity and Access Management (IAM) role in the destination account that's based on the
   S3 Batch Operations trust policy. In this procedure, the _destination account_
   is the account that the objects are being copied to.

For more information about the trust policy, see [Trust policy](batch-ops-iam-role-policies.md#batch-ops-iam-role-policies-trust "batch-ops-iam-role-policies.md#batch-ops-iam-role-policies-trust").

For more information about creating a role, see [Creating a role to delegate
permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

If you create the role by using the console, enter a name for the role (the following
example role uses the name
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

Using the policy, the role grants `batchoperations.s3.amazonaws.com`
permission to read the manifest in the source manifest bucket. It grants permissions to
`GET` objects, access control lists (ACLs), tags, and versions in the source
object bucket. It also grants permissions to `PUT` objects, ACLs, tags, and
versions into the destination object bucket. 2. In the source account, create a bucket policy for the bucket that contains the
manifest to grant the role that you created in the previous step permissions to
`GET` objects and versions in the source manifest bucket.

This step allows S3 Batch Operations to read the manifest by using the trusted role. Apply
the bucket policy to the bucket that contains the manifest.

The following is an example of the bucket policy to apply to the source manifest
bucket. To use this policy, replace the `user input
 placeholders` with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowBatchOperationsSourceManifestRead",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:user/`ConsoleUserCreatingJob`",
 "arn:aws:iam::`111122223333`:role/`BatchOperationsDestinationRoleCOPY`"
 ]
 },
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 }
 ]
}`

```

This policy also grants permissions to allow a console user who is creating a job in
the destination account the same permissions in the source manifest bucket through the
same bucket policy. 3. In the source account, create a bucket policy for the source bucket that grants the
role that you created permissions to `GET` objects, ACLs, tags, and versions in
the source object bucket. S3 Batch Operations can then get objects from the source bucket through
the trusted role.

The following is an example of the bucket policy for the bucket that contains the
source objects. To use this policy, replace the `user input
 placeholders` with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowBatchOperationsSourceObjectCOPY",
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

4. Create an S3 Batch Operations job in the destination account. You need the Amazon Resource
   Name (ARN) for the role that you created in the destination account. For more information
   about creating a job, see [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").

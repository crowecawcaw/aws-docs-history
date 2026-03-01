# Granting permissions for Batch Operations

Before creating and running S3 Batch Operations jobs, you must grant required permissions. To
create an Amazon S3 Batch Operations job, the `s3:CreateJob` user permission is required. The
same entity that creates the job must also have the `iam:PassRole` permission to pass
the AWS Identity and Access Management (IAM) role that's specified for the job to Batch Operations.

The following sections provide information about creating an IAM role and attaching
policies. For general information about specifying IAM resources, see [IAM JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the
_IAM User Guide_.

###### Topics

- [Creating an S3 Batch Operations IAM role](#batch-ops-iam-role-policies-create "#batch-ops-iam-role-policies-create")
- [Attaching permissions policies](#batch-ops-iam-role-policies-perm "#batch-ops-iam-role-policies-perm")

## Creating an S3 Batch Operations IAM role

Amazon S3 must have permissions to perform S3 Batch Operations on your behalf. You grant these
permissions through an AWS Identity and Access Management (IAM) role. When you create an S3 Batch Operations job, you
specify the IAM role that you want the job to use. This can be an existing IAM role. Or,
if you use the Amazon S3 console to create the job, it can be an IAM role that Amazon S3 creates for
you.

If you choose to let Amazon S3 create the IAM role for you, it automatically creates and
attaches trust and permissions policies to the role. The trust policy allows the
S3 Batch Operations service principal (`batchoperations.s3.amazonaws.com`) to assume the
role. The permissions policy allows all the requisite actions for running the job, based on
the settings that you specify for the job. For example, if you configure a job to copy objects
from one bucket to another bucket in your AWS account, the permissions policy allows actions
such as `s3:GetObject` and `s3:PutObject`. You can review the trust and
permissions policies for the role before you submit the job. This option is available only if
you use the Amazon S3 console to create a job, and you configure the job to use an S3 generated
object list that uses filters or is based on a replication configuration. After you submit the
job, the IAM role persists in your account. You can then use it again for subsequent jobs
that perform the same operation, or delete it when the job finishes running.

If you prefer to create the IAM role manually, the policy examples in this section can
help you create the role. For more information about creating and configuring roles, see
[IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide_. For information about permissions for S3 API operations by S3
resource type, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For additional examples, see [Controlling permissions for Batch Operations using job tags](batch-ops-job-tags-examples.md "batch-ops-job-tags-examples.md") and
[Copying objects using S3 Batch Operations](batch-ops-examples-copy.md "batch-ops-examples-copy.md").

In your IAM policies, you can also use condition keys to filter access permissions for
S3 Batch Operations jobs. For more information and a complete list of Amazon S3 specific condition keys,
see [Actions, resources, and condition keys for Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md") in the _Service Authorization
Reference_.

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

The following video includes how to set up IAM permissions for
Batch Operations jobs using the Amazon S3 console.

### Trust policy

To allow the S3 Batch Operations service principal to assume the IAM role, attach the
following trust policy to the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"batchoperations.s3.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## Attaching permissions policies

Depending on the type of operations, you can attach one of the following policies.

Before you configure permissions, note the following:

- Regardless of the operation, Amazon S3 needs permissions to read your manifest object from
  your S3 bucket and optionally write a report to your bucket. Therefore, all of the
  following policies include these permissions.
- For Amazon S3 Inventory report manifests, S3 Batch Operations requires permission to read the
  manifest.json object and all associated CSV data files.
- Version-specific permissions such as `s3:GetObjectVersion` are only
  required when you are specifying the version ID of the objects.
- If you are running S3 Batch Operations on encrypted objects, the IAM role must also have
  access to the AWS KMS keys used to encrypt them.
- If you submit an inventory report manifest that's encrypted with AWS KMS, your IAM
  policy must include the permissions `"kms:Decrypt"` and
  `"kms:GenerateDataKey"` for the manifest.json object and all associated CSV
  data files.
- If the Batch Operations job generates a manifest in a bucket that has access control lists (ACLs)
  enabled and is in a different AWS account, you must grant the
  `s3:PutObjectAcl` permission in the IAM policy of the IAM role configured
  for the batch job. If you don't include this permission, the batch job fails with the
  error `Error occurred when preparing manifest: Failed to write
manifest`.

### Copy objects: PutObject

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectTagging"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 },
 {
 "Action": [
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:ListBucket"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Replace object tagging: PutObjectTagging

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObjectTagging",
 "s3:PutObjectVersionTagging"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Delete object tagging: DeleteObjectTagging

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObjectTagging",
 "s3:DeleteObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Replace access control list: PutObjectAcl

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObjectAcl",
 "s3:PutObjectVersionAcl"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Restore objects: RestoreObject

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:RestoreObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Apply Object Lock retention: PutObjectRetention

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetBucketObjectLockConfiguration",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObjectRetention",
 "s3:BypassGovernanceRetention"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Apply Object Lock legal hold: PutObjectLegalHold

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetBucketObjectLockConfiguration",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "s3:PutObjectLegalHold",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Replicate existing objects: InitiateReplication with an S3 generated manifest

Use this policy if you're using and storing an S3 generated manifest. For more
information about using Batch Operations to replicate existing objects, see [Replicating existing objects with Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Action":[
 "s3:InitiateReplication"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
 ]
 },
 {
 "Action":[
 "s3:GetReplicationConfiguration",
 "s3:PutInventoryConfiguration"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:s3:::amzn-s3-demo-source-bucket"
 ]
 },
 {
 "Action":[
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*",
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 }
 ]
}`

```

### Replicate existing objects: InitiateReplication with a user manifest

Use this policy if you're using a user supplied manifest. For more information about
using Batch Operations to replicate existing objects, see [Replicating existing objects with Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Action":[
 "s3:InitiateReplication"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
 ]
 },
 {
 "Action":[
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Effect":"Allow",
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-manifest-bucket`/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 ]
 }
 ]
}`

```

### Compute checksum: Allow `GetObject`, `GetObjectVersion`, `RestoreObject`, and `PutObject`

Use this policy if you're trying to use the **Compute checksum**
operation with S3 Batch Operations. Permissions for `GetObject`, `GetObjectVersion`, and
`RestoreObject` are required to obtain and read the bytes of stored data. Replace the user
input placeholders with your own information. For more information about **Compute checksum**,
see [Checking object integrity for data at rest in Amazon S3](checking-object-integrity-at-rest.md "checking-object-integrity-at-rest.md").

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:RestoreObject"
      ],
      "Resource": [
        "arn:aws:s3:::``amzn-s3-demo-bucket1``/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource": [
        "arn:aws:s3:::``amzn-s3-demo-bucket2``/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::``amzn-s3-demo-bucket3``/*"
      ]
    }
  ]
}

```

### Update object encryption

You must attach the following permissions policy to allow Batch Operations to read a manifest, update
the encryption type of your objects, and write a completion report. To use this permissions policy,
replace the `user input placeholders` with your own information.
For more information about using this operation and the permissions that you must attach to the role
used by your IAM principal, see [Update object encryption](batch-ops-update-encryption.md "batch-ops-update-encryption.md").

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Sid": "S3BatchOperationsUpdateEncryption",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:PutObject",
                "s3:UpdateObjectEncryption"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-target`"
                "arn:aws:s3:::`amzn-s3-demo-bucket-target`/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyForManifestFile",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-manifest`/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyForCompletionReport",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-completion-report`/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyManifestGeneration",
            "Effect": "Allow",
            "Action": [
                "s3:PutInventoryConfiguration"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-target`"
            ]
        }
        {
            "Sid": "AllowKMSOperationsForS3BatchOperations",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:Encrypt",
                "kms:ReEncrypt*"
            ],
            "Resource": [
                "arn:aws:kms:`us-east-1`:111122223333:key/`01234567-89ab-cdef-0123-456789abcdef`"
            ]
        }
    ]
}
```

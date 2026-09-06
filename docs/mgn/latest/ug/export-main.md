NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Exporting your data inventory

The **Export** feature allows you to easily export your
inventory of servers, applications, and waves to a CSV file that is saved in your local disk
or an S3 bucket.

###### Note

The export feature is not supported for IPv6.

## Defining required permissions for export

In order to use the export feature, you will need to create a role with the following policies (or any extension of them):

**Managed policies:**

- AWSApplicationMigrationReadOnlyAccess

**Additional policies:**

```
{
  "Sid":  "AllowS3Access",
   "Effect":  "Allow",
   "Action": [
     "s3:GetObject"
  ],
   "Resource":  "arn:aws:s3:::amzn-s3-demo-bucket/*"
},
{
   "Sid": "AllowMgnStartExport",
   "Effect": "Allow",
   "Action": [
     "mgn:StartExport"
  ],
   "Resource": "*"
}
```

When starting an export on an Amazon S3 bucket source that is owned by another account,
ensure that the role or user has access to the Amazon S3 objects. When using the API, the Amazon S3
bucket owner parameter defaults to the current user’s account ID.

The following is an example of an Amazon S3 bucket policy in the target account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExampleStatement",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:user/Dave"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

###### Note

If the Amazon S3 objects are encrypted with SSE-KMS, ensure that the role or user initiating
the export has access to decrypt using the AWS KMS key. This feature does not support SSE-C
encrypted Amazon S3 objects.

## Required Amazon S3 bucket permissions

Before you create an export job, you must create the destination S3 bucket to export to.
AWS Transform MGN doesn't create the S3 bucket for you. The S3 bucket that you specify can't be
publicly accessible, and can't be configured as a [Requester Pays](../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md "../../../AmazonS3/latest/userguide/RequesterPaysBuckets.md") bucket. After you create the S3 bucket, confirm that the bucket
has the required permissions policy to allow AWS Transform MGN to write the export files to
it.

## Export parameters

The exported file includes the same parameters as the imported file. For the full list
of parameters and their descriptions, see [Import parameters](import-parameters.md "import-parameters.md").

In addition, the exported file includes the following view-only parameters. These
parameters are exported for informational purposes only, and are ignored if they are present
in an imported file:

|                                  |                                                         |
| -------------------------------- | ------------------------------------------------------- |
| **Parameter**                    | **Description**                                         |
| **mgn:server:lifecycle-state**   | The server's lifecycle state.                           |
| **mgn:server:replication-state** | The state of the replication.                           |
| **mgn:server:replication-type**  | The type of the replication (agent-based or agentless). |

###### Note

If the bucket you're exporting to is encrypted with customer managed keys (KMS), that KMS
key's policies must give MGN permission to use it. This permission is given through
the user or role that initiates the export job.

If you choose to encrypt your export using a key protected by AWS Key Management Service (AWS KMS),
the key must be in the same Region as the destination S3 bucket.

# Granting access for Gremlin Amazon S3 export feature

**Required IAM policies**

1. **Neptune query read access**

```
{
  "Sid": "NeptuneQueryRead",
  "Effect": "Allow",
  "Action": ["neptune-db:Read*"],
  "Resource": "arn:aws:neptune-db:us-east-1:123456789012:cluster-ABCD12/*"
}
```

**Why it's needed:** This permission allows reading data from
Neptune databases, which is necessary to execute the Gremlin queries that will be exported. The
previous example allows read queries. For a read/write query, write/delete permissions are required. 2. **Amazon S3 export permissions**

```
{
  "Sid": "NeptuneS3Export",
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket",
    "s3:PutObject",
    "s3:AbortMultipartUpload",
    "s3:GetBucketPublicAccessBlock"
  ],
  "Resource": "arn:aws:s3:::`neptune-export-bucket`/*"
}
```

**Why each permission is needed:**

    * `s3:ListBucket`: Required to verify bucket existence and list contents.
    * `s3:PutObject`: Required to write the exported data to Amazon S3.
    * `s3:AbortMultipartUpload`: Required to clean up incomplete multipart uploads
     if the export fails.
    * `s3:GetBucketPublicAccessBlock`: Required as a security measure to verify that
     the bucket is not public before exporting data.

3. **AWS KMS permissios** - optional. Only required if using custom
   AWS KMS encryption.

```
{
  "Sid": "NeptuneS3ExportKMS",
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey",
    "kms:DescribeKey"
  ],
  "Resource": "arn:aws:kms:`<REGION>`:`<AWS_ACCOUNT_ID>`:key/mrk-48971c37"
    "Condition": {
    "StringEquals": {
      "kms:ViaService": [
        "s3.`<REGION>`.amazonaws.com",
        "rds.`<REGION>`.amazonaws.com"
      ]
    }
  }
}
```

**Why each permission is needed:**

    * `kms:Decrypt`: Required to decrypt the AWS KMS key for data encryption.
    * `kms:GenerateDataKey`: Required to generate data keys for encrypting the exported data.
    * `kms:DescribeKey`: Required to verify and retrieve information about the AWS KMS key.
    * `kms:ViaService`: Increases security by enforcing that the key is not usable by this
     role for any other AWS service.

###### Important prerequisites

- **IAM authentication:** Must be enabled on the Neptune cluster to enforce
  these permissions.
- **VPC endpoint:**
  - A Gateway-type VPC endpoint for Amazon S3 is required to allow Neptune to communicate with Amazon S3.
  - To use custom AWS KMS encryption in the query, an Interface-type VPC endpoint for AWS KMS is required
    to allow Neptune to communicate with AWS KMS.

- **Amazon S3 bucket configuration:**
  - Must not be public.
  - Should have a lifecycle rule to clean up incomplete multipart uploads.
  - Will automatically encrypt new objects.

These permissions and prerequisites ensure secure and reliable export of Gremlin query results while maintaining
proper access controls and data protection measures.

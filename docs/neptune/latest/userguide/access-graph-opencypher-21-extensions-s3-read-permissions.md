

# Managing permissions for neptune.read()
<a name="access-graph-opencypher-21-extensions-s3-read-permissions"></a>

## Required IAM Policies
<a name="access-graph-opencypher-21-extensions-s3-read-permissions-iam"></a>

To execute openCypher queries that use `neptune.read()`, you must have the appropriate permissions to access data in your Neptune database. Read-only queries require the `ReadDataViaQuery` action. Queries that modify data require `WriteDataViaQuery` for insertions or `DeleteDataViaQuery` for deletions. The example below grants all three actions on the specified cluster.

Additionally, you need permissions to access the S3 bucket containing your data files. The NeptuneS3Access policy statement grants the required S3 permissions:
+ **`s3:ListBucket`**: Required to verify bucket existence and list contents.
+ **`s3:GetObject`**: Required to access the specified object so its content can be read for integration into openCypher queries.

If your S3 bucket uses server-side encryption with AWS KMS, you must also grant KMS permissions. The NeptuneS3KMSAccess policy statement allows Neptune to decrypt data and generate data keys when accessing encrypted S3 objects. The condition restricts KMS operations to requests originating from S3 and RDS services in your region.
+ **`kms:Decrypt`**: Required to perform decryption of the encrypted object so its data can be read by Neptune.
+ **`kms:GenerateDataKey`**: Also required by the S3 API used to retrieve objects to be read.

```
{
  "Sid": "NeptuneQueryAccess",
  "Effect": "Allow",
  "Action": [
      "neptune-db:ReadDataViaQuery",
      "neptune-db:WriteDataViaQuery",
      "neptune-db:DeleteDataViaQuery"
  ],
  "Resource": "arn:aws:neptune-db:<REGION>:<AWS_ACCOUNT_ID>:<CLUSTER_RESOURCE_ID>/*"
},
{
  "Sid": "NeptuneS3Access",
  "Effect": "Allow",
  "Action": [
      "s3:ListBucket",
      "s3:GetObject"
  ],
  "Resource": [
      "arn:aws:s3:::neptune-read-bucket",
      "arn:aws:s3:::neptune-read-bucket/*"
  ]
},
{
  "Sid": "NeptuneS3KMSAccess",
  "Effect": "Allow",
  "Action": [
      "kms:Decrypt",
      "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:<REGION>:<AWS_ACCOUNT_ID>:key/<KEY_ID>",
  "Condition": {
      "StringEquals": {
        "kms:ViaService": [
            "s3.<REGION>.amazonaws.com",
            "rds.<REGION>.amazonaws.com"
        ]
      }
  }
}
```

## Important prerequisites
<a name="access-graph-opencypher-21-extensions-s3-read-permissions-prerequisites"></a>

These permissions and prerequisites ensure secure and reliable integration of S3 data into openCypher queries, while maintaining proper access controls and data protection measures.
+ **IAM authentication**: This feature is only supported for Neptune clusters with IAM authentication enabled. See [Securing your Amazon Neptune database](security.md) for detailed instructions on how to create and connect to IAM authentication-enabled clusters.
+ **VPC endpoint**:
  + A Gateway-type VPC endpoint for Amazon S3 is required to allow Neptune to communicate with Amazon S3.
  + To use custom AWS KMS encryption in the query, an Interface-type VPC endpoint for AWS KMS is required to allow Neptune to communicate with AWS KMS.
  + For detailed instructions for how to configure this endpoint, see [Creating the Amazon S3 VPC Endpoint](bulk-load-tutorial-IAM.md).
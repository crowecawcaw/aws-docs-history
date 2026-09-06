

# Service execution role
<a name="msk-data-delivery-iceberg-iam-service-role"></a>

A Channel assumes a service execution role to deliver data. The role needs a trust policy plus a permission policy that matches your destination type. The following policies are the authoritative reference for the required permissions.

## Trust policy
<a name="msk-data-delivery-iceberg-iam-trust-policy"></a>

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "kafka.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "ACCOUNT_ID"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:kafka:REGION:ACCOUNT_ID:channel/*"
                }
            }
        }
    ]
}
```

**Note**  
Use the `aws:SourceArn` and `aws:SourceAccount` conditions to prevent confused deputy attacks.

## Permission policy — streaming tables for Apache Iceberg
<a name="msk-data-delivery-iceberg-iam-policy"></a>

The following single policy contains every statement the service role may need. Keep the statements that apply to your setup (see [When you need each statement](#msk-data-delivery-iceberg-iam-when-needed)) and remove the rest.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3TablesActions",
            "Effect": "Allow",
            "Action": [
                "s3tables:GetTable",
                "s3tables:GetTableMetadataLocation",
                "s3tables:UpdateTableMetadataLocation",
                "s3tables:CreateTable",
                "s3tables:PutTableData",
                "s3tables:CreateNamespace",
                "s3tables:GetTableData",
                "s3tables:GetTableBucket",
                "s3tables:TagResource",
                "s3tables:PutTableRecordExpirationConfiguration",
                "s3tables:PutTableEncryption"
            ],
            "Resource": [
                "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/BUCKET_NAME",
                "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/BUCKET_NAME/table/*"
            ]
        },
        {
            "Sid": "AllowCreateTableWithTag",
            "Effect": "Allow",
            "Action": "s3tables:CreateTable",
            "Resource": [
                "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/BUCKET_NAME/table/*",
                "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/BUCKET_NAME"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/TableName": "TABLE_NAME"
                }
            }
        },
        {
            "Sid": "AllowPutTableDataWithTag",
            "Effect": "Allow",
            "Action": "s3tables:PutTableData",
            "Resource": "arn:aws:s3tables:REGION:ACCOUNT_ID:bucket/BUCKET_NAME/table/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/TableName": "TABLE_NAME"
                }
            }
        },
        {
            "Sid": "DLQBucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation",
                "s3:PutObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::DLQ_BUCKET",
                "arn:aws:s3:::DLQ_BUCKET/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "DLQ_ACCOUNT_ID"
                }
            }
        },
        {
            "Sid": "GlueSchemaRegistryAccess",
            "Effect": "Allow",
            "Action": [
                "glue:GetSchemaVersion"
            ],
            "Resource": [
                "arn:aws:glue:REGION:ACCOUNT_ID:schema/*",
                "arn:aws:glue:REGION:ACCOUNT_ID:registry/*"
            ]
        },
        {
            "Sid": "KMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": [
                "arn:aws:kms:REGION:ACCOUNT_ID:key/KEY_ID"
            ]
        }
    ]
}
```

## When you need each statement
<a name="msk-data-delivery-iceberg-iam-when-needed"></a>

The following explains when each statement in the preceding policy is required.
+ **`AllowS3TablesActions` (required)** — grants the core S3 Tables actions, scoped by the S3 Table ARN. `s3tables:PutTableEncryption` is required only when you provide your own customer-managed KMS key (you can remove it otherwise).
+ **`AllowCreateTableWithTag` / `AllowPutTableDataWithTag` (optional)** — use these only if you want tag-based access control instead of ARN scoping for table creation and data writes. They restrict `s3tables:CreateTable` and `s3tables:PutTableData` to resources carrying a matching `TableName` tag. Replace `TABLE_NAME` with your table name; omit these statements if you scope solely by ARN.
+ Table ARNs are UUID-based and only exist after the Channel creates the table, so scope to the bucket ARN plus `.../bucket/BUCKET_NAME/table/*` (sample table ARN: `arn:aws:s3tables:us-east-1:123456789012:bucket/my-bucket/table/49d6653e-244e-40a0-b0a0-c975c404127d`).
+ **`DLQBucketAccess` (required)** — the Channel writes the identifiers of unprocessable records to the DLQ bucket. Replace `DLQ_ACCOUNT_ID` with the ID of the account that owns the DLQ bucket; the `aws:ResourceAccount` condition restricts access to a bucket in that account.
+ **`GlueSchemaRegistryAccess` (required)** — grants `glue:GetSchemaVersion` so the Channel can resolve the schema for the topic data from the Glue Schema Registry. Required for both the `JSON` and `JSON_SCHEMA_GSR` input formats.
+ **`KMSAccess` (optional)** — required only when you provide your own customer-managed KMS key.

## Cross-account S3 Table bucket access
<a name="msk-data-delivery-iceberg-iam-cross-account"></a>

If your S3 Table bucket is in a different AWS account from your Amazon MSK cluster and the Channel service role, the bucket owner must grant access to the service role by attaching a table bucket policy (a resource-based policy) on the S3 Table bucket. Scope the policy to the Channel service-role principal and the S3 Tables actions the role needs (see the preceding Iceberg permission policy).

For details and policy examples, see [Managing table bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html) and [Resource-based policies for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-resource-based-policies.html) in the *Amazon S3 User Guide*.

## Additional permissions
<a name="msk-data-delivery-iceberg-iam-additional"></a>
+ **Amazon CloudWatch Logs (optional):** add `logs:CreateLogStream` and `logs:PutLogEvents` on the log group (see [Logging](msk-data-delivery-iceberg-logging.md)).
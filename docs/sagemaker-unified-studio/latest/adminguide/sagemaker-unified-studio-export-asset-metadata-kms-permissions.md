# KMS

permissions for exporting asset metadata in Amazon SageMaker Unified Studio

###### Topics

- [Granting
  the Amazon SageMaker Catalog export service principal and S3 Tables maintenance
  service principal permissions to your KMS key](#export-asset-metadata-kms-permissions-service-principal "#export-asset-metadata-kms-permissions-service-principal")
- [IAM permissions required for the principal for exporting](#export-asset-metadata-kms-permissions-service-principal-exporting "#export-asset-metadata-kms-permissions-service-principal-exporting")

## Granting

the Amazon SageMaker Catalog export service principal and S3 Tables maintenance
service principal permissions to your KMS key

All data in S3 tables are encrypted with SSE-S3 encryption by default. You can
choose to encrypt your data with AWS Key Management Service (AWS KMS) keys
(SSE-KMS). If you choose to encrypt your data with KMS keys, you must have
additional permissions.

For Amazon SageMaker Catalog, these permissions are required so that your data can
be encrypted when exporting the data into the S3 tables. Note that the KMS key used
for export feature can be same or different than the one used for Amazon SageMaker
Catalog domain. To read more about how Amazon SageMaker Catalog domain data
encryption works at rest, see [Data encryption at rest for Amazon DataZone](../../../datazone/latest/userguide/encryption-rest-datazone.md "../../../datazone/latest/userguide/encryption-rest-datazone.md").

To allow Amazon SageMaker Catalog access on SSE-KMS encrypted tables, you can use
the following example key policy. The policy allows
`maintenance.s3tables.amazonaws.com` service principal to use a
specific KMS key for encrypting and decrypting tables in a specific table bucket. To
use the policy, replace the user input placeholders with your own
information:

To read more about the S3 maintenance service principal, see [Permissions required for S3 Tables SSE-KMS encryption](../../../AmazonS3/latest/userguide/s3-tables-kms-permissions.md "../../../AmazonS3/latest/userguide/s3-tables-kms-permissions.md").

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnableSystemTablesKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "systemtables.sagemaker-catalog.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/key-id",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "EnableKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:us-east-1:111122223333:key/key-id",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "<table-or-table-bucket-arn>/*"
                }
            }
        }
    ]
}

```

## IAM permissions required for the principal for exporting

When your Amazon SageMaker Catalog domain is encrypted using AWS Key Management
Service (AWS KMS) keys, you need to grant permissions to the principals that will
allow them to enable [exporting](sagemaker-unified-studio-export-asset-metadata-kms-permissions.md "sagemaker-unified-studio-export-asset-metadata-kms-permissions.md") the asset metadata. The policy below grants the IAM principal
access to decrypt a specific Amazon SageMaker Catalog domain.

To read more about how Amazon SageMaker Catalog domain data encryption works at
rest, see [Data encryption at rest for Amazon DataZone](../../../datazone/latest/userguide/encryption-rest-datazone.md "../../../datazone/latest/userguide/encryption-rest-datazone.md").

```

{
    "Version": "2012-10-17",
    "Statement": [

        {
            "Sid": "Allow access to principal to manage an Amazon SageMaker catalog domain with the given domain id",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/ExampleRole"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:region:111122223333:key/key_ID",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:datazone:domainId": "dzd_sampleid"
                }
            }
        }
    ]
}

```

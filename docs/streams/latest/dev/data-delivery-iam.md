# IAM permissions for data delivery

Use this topic to learn about the IAM permissions required to create and manage delivery
resources in Amazon Kinesis Data Streams, as well as the service execution role that data delivery assumes
to deliver data to your destination.

## Lifecycle management permissions

To create, update, delete, describe, and list delivery resources, the calling
IAM principal must have the following permissions:

Delivery lifecycle permissions| Action | Resource | Description |
| --- | --- | --- |
| `kinesis:CreateChannel` | Stream ARN (`arn:aws:kinesis:`region`:`account-id`:stream/`stream-name``) | Create a delivery on a Kinesis Data Streams stream. |
| `kinesis:AssociateStreamsWithChannel` | Stream ARN (`arn:aws:kinesis:`region`:`account-id`:stream/`stream-name``) | Associate a stream with a delivery. This is a virtual action that the<br>calling principal must be granted to create a delivery that reads from<br>the specified stream. It is authorized in addition to<br>`kinesis:CreateChannel`. |
| `kinesis:UpdateChannel` | Channel ARN (`arn:aws:kinesis:`region`:`account-id`:channel/`channel-id``) | Update an existing delivery configuration. |
| `kinesis:DeleteChannel` | Channel ARN | Delete an existing delivery. |
| `kinesis:DescribeChannel` | Channel ARN | Retrieve details of a delivery. |
| `kinesis:ListChannels` | Account level (`arn:aws:kinesis:`region`:`account-id`:stream/*`) | List all deliveries in the account. |

## Service execution role

Data delivery assumes an IAM service execution role to deliver data to your
destination. You must create this role and attach both a trust policy and a
permission policy.

### Trust policy

The trust policy allows the Kinesis Data Streams service to assume the role. Include condition
keys to prevent the confused deputy problem.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "kinesis.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "<account-id>"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:kinesis:<region>:<account-id>:channel/*"
                }
            }
        }
    ]
}
```

### Permission policy for streaming tables on Apache Iceberg

When delivering to streaming tables on Apache Iceberg, the service execution role
requires the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3TablesAccess",
            "Effect": "Allow",
            "Action": [
                "s3tables:GetTable",
                "s3tables:GetTableBucket",
                "s3tables:GetTableMetadataLocation",
                "s3tables:UpdateTableMetadataLocation",
                "s3tables:CreateTable",
                "s3tables:CreateNamespace",
                "s3tables:PutTableData",
                "s3tables:GetTableData",
                "s3tables:TagResource",
                "s3tables:PutTableRecordExpirationConfiguration",
                "s3tables:PutTableEncryption"
            ],
            "Resource": [
                "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>",
                "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>/table/*"
            ]
        },
        {
            "Sid": "AllowCreateTableWithTag",
            "Effect": "Allow",
            "Action": "s3tables:CreateTable",
            "Resource": [
                "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>/table/*",
                "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/TableName": "<table-name>"
                }
            }
        },
        {
            "Sid": "AllowPutTableDataWithTag",
            "Effect": "Allow",
            "Action": "s3tables:PutTableData",
            "Resource": "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>/table/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/TableName": "<table-name>"
                }
            }
        },
        {
            "Sid": "DLQBucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::<dlq-bucket-name>",
                "arn:aws:s3:::<dlq-bucket-name>/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "<dlq-account-id>"
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
                "arn:aws:glue:<region>:<account-id>:registry/<registry-name>",
                "arn:aws:glue:<region>:<account-id>:schema/<registry-name>/<schema-name>"
            ]
        },
        {
            "Sid": "KMSForCreateTimeValidation",
            "Effect": "Allow",
            "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<key-id>"],
            "Condition": {
                "StringEqualsIfExists": {
                    "kms:ViaService": "kinesis.<region>.amazonaws.com"
                }
            }
        },
        {
            "Sid": "KMSForS3TablesEncryption",
            "Effect": "Allow",
            "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<key-id>"],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.<region>.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": [
                        "arn:aws:s3tables:<region>:<account-id>:bucket/<table-bucket-name>/*",
                        "arn:aws:s3:::<dlq-bucket-name>/*"
                    ]
                }
            }
        },
        {
            "Sid": "KMSForCreateTable",
            "Effect": "Allow",
            "Action": ["kms:DescribeKey"],
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<key-id>"],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3tables.<region>.amazonaws.com"
                }
            }
        },
        {
            "Sid": "KMSForDecryptSourceStreamRecords",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<stream-key-id>"],
            "Condition": {
                "StringEqualsIfExists": {
                    "kms:ViaService": "kinesis.<region>.amazonaws.com"
                },
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesis:arn": "arn:aws:kinesis:<region>:<account-id>:stream/<stream-name>"
                }
            }
        }
    ]
}
```

- `s3tables:PutTableEncryption` is required only when you encrypt
  the destination table with a customer managed AWS KMS key. Without it,
  `CreateTable` succeeds but table encryption fails and the table
  is never created.
- `s3tables:TagResource` is required because the service tags the
  tables it creates.
- The `AllowCreateTableWithTag` and
  `AllowPutTableDataWithTag` statements are optional. Include them
  only if you want tag-based access control instead of scoping solely by table
  ARN. They restrict `s3tables:CreateTable` and
  `s3tables:PutTableData` to resources carrying a matching
  `TableName` tag. Omit them if you scope by ARN.
- Only `glue:GetSchemaVersion` is required for the Glue Schema
  Registry. It is required for both the `JSON` and
  `GSR_JSON` input formats.
- The `KMSForCreateTimeValidation` statement lets Amazon Kinesis Data Streams
  validate your AWS KMS key when you create the delivery. It is required only
  when your destination table or source stream uses a customer managed AWS KMS
  key.
- The `KMSForS3TablesEncryption` statement grants the AWS KMS
  operations used to encrypt delivered table data at rest. It is required only
  when your table bucket uses a customer managed key.
- The `KMSForCreateTable` statement lets Amazon Kinesis Data Streams read the key
  configuration when it creates the destination table. It is required only
  when the table bucket uses a customer managed key.
- The `KMSForDecryptSourceStreamRecords` statement lets the role
  decrypt records read from the source stream. It is required only when your
  Kinesis Data Streams stream is encrypted with a customer managed key.

### Permission policy for general purpose Amazon S3 buckets

When delivering to general purpose Amazon S3 buckets, the service execution role
requires the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeliveryBucketList",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::<delivery-bucket-name>",
                "arn:aws:s3:::<delivery-bucket-name>/*"
            ]
        },
        {
            "Sid": "DeliveryBucketWrite",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:CreateMultipartUpload",
                "s3:UploadPart",
                "s3:CompleteMultipartUpload",
                "s3:ListMultipartUploads",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::<delivery-bucket-name>/*"
            ]
        },
        {
            "Sid": "DLQBucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::<dlq-bucket-name>",
                "arn:aws:s3:::<dlq-bucket-name>/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "<dlq-account-id>"
                }
            }
        },
        {
            "Sid": "KMSForCreateTimeValidation",
            "Effect": "Allow",
            "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<key-id>"],
            "Condition": {
                "StringEqualsIfExists": {
                    "kms:ViaService": "kinesis.<region>.amazonaws.com"
                }
            }
        },
        {
            "Sid": "KMSForS3BucketEncryption",
            "Effect": "Allow",
            "Action": ["kms:Decrypt", "kms:GenerateDataKey"],
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<key-id>"],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.<region>.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": [
                        "arn:aws:s3:::<delivery-bucket-name>/*",
                        "arn:aws:s3:::<dlq-bucket-name>/*"
                    ]
                }
            }
        },
        {
            "Sid": "KMSForDecryptSourceStreamRecords",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": ["arn:aws:kms:<region>:<account-id>:key/<stream-key-id>"],
            "Condition": {
                "StringEqualsIfExists": {
                    "kms:ViaService": "kinesis.<region>.amazonaws.com"
                },
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesis:arn": "arn:aws:kinesis:<region>:<account-id>:stream/<stream-name>"
                }
            }
        }
    ]
}
```

- The `KMSForCreateTimeValidation` statement lets Amazon Kinesis Data Streams
  validate your AWS KMS key when you create the delivery. It is required only
  when your destination bucket or source stream uses a customer managed AWS KMS
  key.
- The `KMSForS3BucketEncryption` statement grants the AWS KMS
  operations that Amazon S3 uses to encrypt delivered objects at rest. It is
  required only when your destination bucket or dead-letter queue bucket uses
  SSE-KMS with a customer managed key. The
  `kms:EncryptionContext:aws:s3:arn` values shown use the object
  ARN, which applies when S3 Bucket Keys are disabled. If you enable S3 Bucket
  Keys on the destination bucket or the dead-letter queue bucket, Amazon S3 uses the
  bucket ARN as the encryption context instead of the object ARN, so you must
  change the corresponding value to that bucket ARN (for example,
  `arn:aws:s3:::`delivery-bucket-name`` or
 `arn:aws:s3:::`dlq-bucket-name``).
  For more information, see
  [Configuring
  an S3 Bucket Key](../../../AmazonS3/latest/userguide/configuring-bucket-key.md "../../../AmazonS3/latest/userguide/configuring-bucket-key.md") in the _Amazon S3 User Guide_.
- The `KMSForDecryptSourceStreamRecords` statement lets the role
  decrypt records read from the source stream. It is required only when your
  Kinesis Data Streams stream is encrypted with a customer managed key.

###### Important

If you restrict the `s3:PutObject` resource to a specific prefix
(for example, `arn:aws:s3:::my-bucket/data*`), the object keys
generated by your output key template must start with that same prefix.
A mismatch between the IAM resource prefix and the output key template
results in access denied errors and no data being delivered.

For example, if your policy grants `s3:PutObject` on
`arn:aws:s3:::my-bucket/data*`, your output key template must
begin with `data/`, such as
`data/!{yyyy}/!{MM}/!{dd}/!{HH}/`. To avoid this, either scope the
resource to the entire bucket (`arn:aws:s3:::my-bucket/*`) or
ensure the prefixes match exactly.

### Optional CloudWatch Logs permissions

If you enable CloudWatch Logs for your delivery, add the following permissions to
the service execution role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:<region>:<account-id>:log-group:<log-group-name>:*"
        }
    ]
}
```

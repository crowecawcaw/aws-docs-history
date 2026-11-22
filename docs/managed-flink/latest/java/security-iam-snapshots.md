

# Identity and access management for enhanced snapshots

The permissions on this page apply only to enhanced snapshots in Amazon Managed Service for Apache Flink. If you do not use enhanced snapshots, you do not need these permissions. For more information about enhanced snapshots, see [How enhanced snapshots work](snapshots-how-it-works.md).

Enhanced snapshots use the following IAM identities:
+ **The caller**: The IAM principal that calls the enhanced snapshot API actions. You give the caller permissions with identity-based policies.
+ **The import or export role**: The IAM role that Managed Service for Apache Flink assumes to read from or write to your Amazon S3 bucket. For more information, see [IAM role for import and export](#security-iam-snapshots-transfer-role).
+ **The service execution role**: The IAM role of the application. This role needs no new permissions for enhanced snapshots.

## Policy actions for enhanced snapshots
<a name="security-iam-snapshots-actions"></a>

Enhanced snapshots add the policy actions in the following table. Two of these actions are permissions only, with no API action of the same name.


| Action | Resource | Description | 
| --- | --- | --- | 
| [`kinesisanalytics:CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) | Application ARN | Create an enhanced snapshot of a running application. | 
| [`kinesisanalytics:DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) | Snapshot ARN | Describe an enhanced snapshot. | 
| [`kinesisanalytics:ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) | "\*" | List the enhanced snapshots in the account and Region. | 
| [`kinesisanalytics:DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) | Snapshot ARN | Delete an enhanced snapshot. | 
| [`kinesisanalytics:DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) | Snapshot ARN | Describe one operation on an enhanced snapshot. | 
| [`kinesisanalytics:ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) | Snapshot ARN | List the operations on an enhanced snapshot. | 
| [`kinesisanalytics:ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) | Snapshot ARN of the new enhanced snapshot | Import an Apache Flink savepoint from Amazon S3 as a new enhanced snapshot. The caller also needs iam:PassRole on the IAM role that Managed Service for Apache Flink assumes to read the savepoint from Amazon S3. | 
| [`kinesisanalytics:ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) | Snapshot ARN | Export an enhanced snapshot to Amazon S3. The caller also needs iam:PassRole on the IAM role that Managed Service for Apache Flink assumes to write the enhanced snapshot to Amazon S3. | 
| kinesisanalytics:CreateSystemSnapshot (permission only) | Application ARN | Lets an application lifecycle API create a system snapshot. For the APIs that check this action, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions). | 
| kinesisanalytics:RestoreFromSnapshot (permission only) | Snapshot ARN | Lets an application lifecycle API, such as StartApplication, UpdateApplication, or RollbackApplication, restore from an enhanced snapshot. For the APIs and application statuses that check this action, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions). | 

Managed Service for Apache Flink checks `kinesisanalytics:ListSnapshots` on the resource `"*"`. This rule applies also when the request sets `SourceApplicationName`.

The [`TagResource`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_TagResource.html), [`UntagResource`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UntagResource.html), and [`ListTagsForResource`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListTagsForResource.html) actions accept a snapshot ARN. The legacy application snapshot APIs, such as [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html), use the same IAM policy actions as before.

## Policy resources for enhanced snapshots
<a name="security-iam-snapshots-resources"></a>

An enhanced snapshot is a separate IAM resource with the resource type `snapshot`. The snapshot ARN has the following format. The ARN contains the snapshot name and no suffix.

```
"Resource" : "arn:{{partition}}:kinesisanalytics:{{Region}}:{{account}}:snapshot/{{snapshot-name}}"
```

To control a group of enhanced snapshots, use a wildcard after a name prefix. The following example matches every enhanced snapshot whose name starts with `MyApplication-`.

```
"Resource" : "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-*"
```

In enhanced snapshot mode, system snapshot names start with `SYSTEMSNAPSHOT-`. The pattern `snapshot/SYSTEMSNAPSHOT-*` matches the enhanced system snapshots of every application in the account and Region.

`kinesisanalytics:CreateSnapshot` and `kinesisanalytics:CreateSystemSnapshot` control who creates enhanced snapshots and system snapshots. `kinesisanalytics:RestoreFromSnapshot` treats both kinds the same way. The `Resource` element of a `RestoreFromSnapshot` statement decides which of them a caller can restore from.

Application snapshots (legacy) are not IAM resources. To control the legacy application snapshot APIs, use the application ARN.

## Policy condition keys for enhanced snapshots
<a name="security-iam-snapshots-condition-keys"></a>

Enhanced snapshots add no service-specific condition keys. To control enhanced snapshot actions by tag, use the global condition keys `aws:ResourceTag`, `aws:RequestTag`, and `aws:TagKeys`. For more information, see [Attribute-based access control for enhanced snapshots](#security-iam-snapshots-abac).

When Managed Service for Apache Flink assumes an import or export role, it sets `aws:SourceAccount` and `aws:SourceArn`. The value of `aws:SourceArn` is the ARN of the enhanced snapshot that you import or export. For a trust policy that uses these keys, see [Trust policy](#security-iam-snapshots-transfer-role-trust).

## Attribute-based access control for enhanced snapshots
<a name="security-iam-snapshots-abac"></a>

Enhanced snapshots support tags. You can add tags when you create an enhanced snapshot with `CreateSnapshot`. You can also add tags to an existing enhanced snapshot with `TagResource` and the snapshot ARN.

The following rules apply to tags on enhanced snapshots:
+ **Tag on create**: A `CreateSnapshot` request with `Tags` needs `kinesisanalytics:CreateSnapshot` on the application ARN. It also needs `kinesisanalytics:TagResource` on the ARN of the new enhanced snapshot. If IAM denies either action, the request returns `AccessDeniedException`. Managed Service for Apache Flink does not create the enhanced snapshot.

  An `ImportSnapshot` request with `Tags` needs `kinesisanalytics:ImportSnapshot` and `kinesisanalytics:TagResource` on the ARN of the new enhanced snapshot. If IAM denies either action, the request returns `AccessDeniedException`.
+ **Request tags**: For a `CreateSnapshot` or `ImportSnapshot` request with `Tags`, Managed Service for Apache Flink sets `aws:RequestTag/{{key-name}}` and `aws:TagKeys`. You can use these keys on `kinesisanalytics:CreateSnapshot`, `kinesisanalytics:ImportSnapshot`, and `kinesisanalytics:TagResource`.
+ **Resource tags**: Actions on a snapshot ARN evaluate `aws:ResourceTag/{{key-name}}` against the tags of the enhanced snapshot. These actions include `RestoreFromSnapshot`, `DescribeSnapshot`, `DeleteSnapshot`, and `ExportSnapshot`.
+ **System snapshots**: `kinesisanalytics:CreateSystemSnapshot` evaluates `aws:ResourceTag` against the tags of the application. Managed Service for Apache Flink does not set `aws:RequestTag` or `aws:TagKeys` for this action. A system snapshot inherits the tags that the application has when Managed Service for Apache Flink creates the system snapshot. For more information, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots).

For tag limits and an example request, see [Create an enhanced snapshot](snapshots-manage.md#snapshots-manage-create-a-snapshot). For a policy that requires a tag on new enhanced snapshots, see [Control tags on new snapshots](#security_iam_id-based-policy-examples-require-snapshot-tags).

## IAM role for import and export
<a name="security-iam-snapshots-transfer-role"></a>

`ImportSnapshot` and `ExportSnapshot` use a separate IAM role that you supply in the request. You pass the role in `ImportRoleArn` or `ExportRoleArn`. Managed Service for Apache Flink assumes this role to read from or write to your Amazon S3 bucket.

The role needs the trust policy and one of the four permissions policies. The following list links to each policy:
+ [Trust policy](#security-iam-snapshots-transfer-role-trust)
+ [Import permissions policy](#security-iam-snapshots-transfer-role-import)
+ [Import KMS permissions policy](#security-iam-snapshots-transfer-role-import-kms)
+ [Export permissions policy](#security-iam-snapshots-transfer-role-export)
+ [Export KMS permissions policy](#security-iam-snapshots-transfer-role-export-kms)

The console can create this role for you.

In each example policy, replace the account ID, Region, snapshot name, bucket, prefix, and key ID with your own values.

For an import, use the ARN of the new enhanced snapshot in `aws:SourceArn` and in the `kms:EncryptionContext:aws:kinesisanalytics:arn` condition. For an export, use the ARN of the enhanced snapshot that you export.

Each Amazon S3 statement and each AWS KMS statement has an `aws:ResourceAccount` condition. The condition value is the ID of the account that owns the bucket or the key. Import and export work only within one account. The examples use your account ID.

Each permissions policy allows `s3:ListBucket` and `s3:GetBucketLocation` on the bucket. Before the transfer, Managed Service for Apache Flink uses these permissions to check that the bucket exists and to check the bucket owner. Managed Service for Apache Flink also uses them to get the Region of the bucket.

The policies with a customer managed key use the following AWS KMS conditions:
+ `kms:ViaService` uses the Regional form `s3.{{region}}.amazonaws.com`.
+ `kms:EncryptionContext:aws:s3:arn` uses `StringLike` and a value that ends with `*`. This value matches the bucket ARN when Amazon S3 Bucket Keys is on. The value also matches the object ARN when Amazon S3 Bucket Keys is off.

### Trust policy
<a name="security-iam-snapshots-transfer-role-trust"></a>

The trust policy lets the Managed Service for Apache Flink service principal `kinesisanalytics.amazonaws.com` assume the role. The `aws:SourceAccount` and `aws:SourceArn` conditions limit the role to your account and one enhanced snapshot. The example uses `ArnEquals` with the full snapshot ARN of one enhanced snapshot.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AssumeForSnapshotTransfer",
            "Effect": "Allow",
            "Principal": {
                "Service": "kinesisanalytics.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
                }
            }
        }
    ]
}
```

### Import permissions policy
<a name="security-iam-snapshots-transfer-role-import"></a>

Use this policy when the source objects use Amazon S3 managed keys (SSE-S3) and not a customer managed key. The role reads the savepoint objects under the source prefix.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadSnapshotSource",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectAttributes"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/imports/my-app/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

### Import KMS permissions policy
<a name="security-iam-snapshots-transfer-role-import-kms"></a>

Use this policy when a customer managed key encrypts the source objects. This policy adds permissions on the source key to the import permissions policy. Two statements allow access to the source key:
+ `ReadEncryptedSnapshotSourceViaS3`: Allows `kms:Decrypt` for the decrypt request that Amazon S3 makes for the role. The conditions require `kms:ViaService` and the Amazon S3 encryption context.
+ `ValidateSnapshotSourceKeyAccess`: Allows `kms:Decrypt` and `kms:GenerateDataKey` for the permission check that Managed Service for Apache Flink makes directly on the key. The encryption context of this check is the snapshot ARN.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ReadSnapshotSource",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectAttributes"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/imports/my-app/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "ReadEncryptedSnapshotSourceViaS3",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com",
                    "aws:ResourceAccount": "111122223333"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-bucket*"
                }
            }
        },
        {
            "Sid": "ValidateSnapshotSourceKeyAccess",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
                    "aws:ResourceAccount": "111122223333"
                },
                "StringEqualsIfExists": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotSourceKey",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com",
                    "aws:ResourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

### Export permissions policy
<a name="security-iam-snapshots-transfer-role-export"></a>

Use this policy when the default encryption of the destination bucket uses Amazon S3 managed keys (SSE-S3) and not a customer managed key. The role writes and reads objects under the destination prefix. The role also manages multipart uploads. The role does not need `s3:DeleteObject`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WriteSnapshotDestination",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/exports/my-app/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "ListDestinationMultipartUploads",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

### Export KMS permissions policy
<a name="security-iam-snapshots-transfer-role-export-kms"></a>

Use this policy when a customer managed key encrypts the exported objects. This policy adds permissions on the destination key to the export permissions policy. Two statements allow `kms:GenerateDataKey` and `kms:Decrypt` on the destination key:
+ `WriteEncryptedSnapshotDestinationViaS3`: Allows the key requests that Amazon S3 makes for the role. The conditions require `kms:ViaService`, the Amazon S3 encryption context, and the snapshot ARN in the Managed Service for Apache Flink encryption context.
+ `ValidateSnapshotDestinationKeyAccess`: Allows the permission check that Managed Service for Apache Flink makes directly on the key. The encryption context of this check is the snapshot ARN.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WriteSnapshotDestination",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/exports/my-app/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "ListDestinationMultipartUploads",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "WriteEncryptedSnapshotDestinationViaS3",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com",
                    "aws:ResourceAccount": "111122223333",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::amzn-s3-demo-bucket*"
                }
            }
        },
        {
            "Sid": "ValidateSnapshotDestinationKeyAccess",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
                    "aws:ResourceAccount": "111122223333"
                },
                "StringEqualsIfExists": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com"
                }
            }
        },
        {
            "Sid": "DescribeSnapshotDestinationKey",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": [
                "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "s3.aa-example-1.amazonaws.com",
                    "aws:ResourceAccount": "111122223333"
                }
            }
        }
    ]
}
```

## Service execution role
<a name="security-iam-snapshots-service-execution-role"></a>

Enhanced snapshots need no new permissions in the service execution role. Managed Service for Apache Flink checks the enhanced snapshot actions on the principal that calls each API. For more information, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

## Identity-based policy examples for enhanced snapshots
<a name="security-iam-snapshots-examples"></a>

The following identity-based policies give a caller permissions for enhanced snapshots.

### Manage enhanced snapshots
<a name="security_iam_id-based-policy-examples-manage-snapshots"></a>

The following policy lets a caller create enhanced snapshots of `MyApplication`. The policy also lets the caller describe and delete those enhanced snapshots, and track their operations. The policy assumes that each enhanced snapshot name starts with `MyApplication-`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateSnapshots",
      "Effect": "Allow",
      "Action": "kinesisanalytics:CreateSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
    },
    {
      "Sid": "ManageSnapshots",
      "Effect": "Allow",
      "Action": [
        "kinesisanalytics:DescribeSnapshot",
        "kinesisanalytics:DeleteSnapshot",
        "kinesisanalytics:DescribeSnapshotOperation",
        "kinesisanalytics:ListSnapshotOperations"
      ],
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-*"
    },
    {
      "Sid": "ListSnapshots",
      "Effect": "Allow",
      "Action": "kinesisanalytics:ListSnapshots",
      "Resource": "*"
    }
  ]
}
```

To add tags in the `CreateSnapshot` request, also allow `kinesisanalytics:TagResource` on the snapshot ARN. If a customer managed key encrypts the application, the caller also needs `kms:Decrypt` and `kms:GenerateDataKey` on that key. For more information, see [Create an enhanced snapshot](snapshots-manage.md#snapshots-manage-create-a-snapshot).

### Control tags on new snapshots
<a name="security_iam_id-based-policy-examples-require-snapshot-tags"></a>

The following policy lets a caller create enhanced snapshots of `MyApplication` only with an `Environment` tag. The `Deny` statement rejects a `CreateSnapshot` request without that tag. Its `Null` condition is true only when the request has no `Environment` tag, so a request with the tag is not denied. The `TagResource` statement allows the tag only with the values `dev` or `prod`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateSnapshots",
      "Effect": "Allow",
      "Action": "kinesisanalytics:CreateSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
    },
    {
      "Sid": "DenyCreateWithoutEnvironmentTag",
      "Effect": "Deny",
      "Action": "kinesisanalytics:CreateSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication",
      "Condition": {
        "Null": { "aws:RequestTag/Environment": "true" }
      }
    },
    {
      "Sid": "TagNewSnapshots",
      "Effect": "Allow",
      "Action": "kinesisanalytics:TagResource",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-*",
      "Condition": {
        "StringEquals": { "aws:RequestTag/Environment": [ "dev", "prod" ] }
      }
    }
  ]
}
```

The `Deny` statement does not affect system snapshots, because Managed Service for Apache Flink checks `CreateSystemSnapshot` for them, not `CreateSnapshot`.

### Restore from specific snapshots
<a name="security_iam_id-based-policy-examples-restore-snapshot"></a>

The following policy lets a caller start or update `MyApplication` from the enhanced snapshot `MyApplication-snapshot-1`. The request sets `ApplicationRestoreType` to `RESTORE_FROM_CUSTOM_SNAPSHOT` and `SnapshotArn` to the snapshot ARN.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "StartAndUpdateApplication",
      "Effect": "Allow",
      "Action": [
        "kinesisanalytics:StartApplication",
        "kinesisanalytics:UpdateApplication",
        "kinesisanalytics:CreateSystemSnapshot"
      ],
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
    },
    {
      "Sid": "RestoreFromOneSnapshot",
      "Effect": "Allow",
      "Action": "kinesisanalytics:RestoreFromSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
    }
  ]
}
```

The following rules apply to this policy:
+ `kinesisanalytics:CreateSystemSnapshot` is necessary only if `SnapshotsEnabled` is `true` for the application.
+ For `RESTORE_FROM_LATEST_SNAPSHOT`, Managed Service for Apache Flink checks `RestoreFromSnapshot` on the snapshot that it selects, which can be a system snapshot or one that you created. To cover both, allow `snapshot/SYSTEMSNAPSHOT-*` and `snapshot/MyApplication-*`, or scope the statement with a tag condition.

  If `SnapshotsEnabled` is `true`, `UpdateApplication` and the VPC and CloudWatch logging option requests do not check `RestoreFromSnapshot` for `RESTORE_FROM_LATEST_SNAPSHOT`. The snapshot that the application restores from is the system snapshot that the request creates, which does not exist yet when Managed Service for Apache Flink checks permissions.
+ If a customer managed key encrypts the enhanced snapshot, the caller also needs `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on that key.

For the restore procedure, see [Restore from a specific snapshot](snapshots-restore.md#snapshots-restore-restore-by-snapshot-arn).

### Import and export enhanced snapshots
<a name="security_iam_id-based-policy-examples-import-export-snapshots"></a>

The following policy lets a caller import a savepoint as the enhanced snapshot `MyApplication-snapshot-imported`. The policy also lets the caller export the enhanced snapshot `MyApplication-snapshot-1`. The `TagResource` statement lets the caller add tags in the `ImportSnapshot` request. The `iam:PassRole` statement lets the caller pass the import role and the export role to Managed Service for Apache Flink.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ImportSnapshot",
      "Effect": "Allow",
      "Action": "kinesisanalytics:ImportSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported"
    },
    {
      "Sid": "TagImportedSnapshot",
      "Effect": "Allow",
      "Action": "kinesisanalytics:TagResource",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported"
    },
    {
      "Sid": "ExportSnapshot",
      "Effect": "Allow",
      "Action": "kinesisanalytics:ExportSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
    },
    {
      "Sid": "PassImportExportRoles",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": [
        "arn:aws:iam::111122223333:role/MSFSnapshotImportRole",
        "arn:aws:iam::111122223333:role/MSFSnapshotExportRole"
      ],
      "Condition": {
        "StringEquals": { "iam:PassedToService": "kinesisanalytics.amazonaws.com" }
      }
    }
  ]
}
```

The import role and the export role need their own trust policy and permissions policy. For these role policies, see [IAM role for import and export](#security-iam-snapshots-transfer-role).

### Key policies for import and export
<a name="security_iam_id-based-policy-examples-import-export-key-policies"></a>

Managed Service for Apache Flink also needs a key policy on the key of the enhanced snapshot. The following key policy allows the caller role `Operator` to import the enhanced snapshot `MyApplication-snapshot-imported`. The key is the key in `DestinationEncryptionConfiguration`. The `DescribeKey` statements are for a later restore or export of the imported enhanced snapshot.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOperatorToDescribeKey",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/Operator" },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "kinesisanalytics.aa-example-1.amazonaws.com" }
      }
    },
    {
      "Sid": "AllowOperatorToUseKeyForImportedSnapshot",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/Operator" },
      "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported",
          "kms:ViaService": "kinesisanalytics.aa-example-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowServiceToDescribeKeyForImportedSnapshot",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "kinesisanalytics.amazonaws.com",
          "infrastructure.kinesisanalytics.amazonaws.com"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported",
          "aws:SourceAccount": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowServiceToUseKeyForImportedSnapshot",
      "Effect": "Allow",
      "Principal": { "Service": "kinesisanalytics.amazonaws.com" },
      "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported"
        }
      }
    }
  ]
}
```

The following key policy allows the caller role `Operator` to export the enhanced snapshot `MyApplication-snapshot-1`. The application `MyApplication` created this enhanced snapshot, so the conditions use the application ARN. For an imported enhanced snapshot, use the snapshot ARN instead. Keep the application ARN in the key policy after you delete the application.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOperatorToDescribeKey",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/Operator" },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "kinesisanalytics.aa-example-1.amazonaws.com" }
      }
    },
    {
      "Sid": "AllowOperatorToReadSnapshotForExport",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::111122223333:role/Operator" },
      "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication",
          "kms:ViaService": "kinesisanalytics.aa-example-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowServiceToDescribeKeyForExport",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "kinesisanalytics.amazonaws.com",
          "infrastructure.kinesisanalytics.amazonaws.com"
        ]
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication",
          "aws:SourceAccount": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowServiceToGenerateDataKeyForExport",
      "Effect": "Allow",
      "Principal": { "Service": "kinesisanalytics.amazonaws.com" },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication",
          "aws:SourceAccount": "111122223333",
          "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
        }
      }
    },
    {
      "Sid": "AllowServiceToDecryptForExport",
      "Effect": "Allow",
      "Principal": { "Service": "kinesisanalytics.amazonaws.com" },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
        }
      }
    }
  ]
}
```

Add statements that allow key administrators to manage the key. For more information about these key policies, see [Key policy for enhanced snapshot import and export](manage-cmk-api.md#create-cmk-kms-key-policy-snapshot-transfer).
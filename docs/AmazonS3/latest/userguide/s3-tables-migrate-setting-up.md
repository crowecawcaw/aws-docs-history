

# Setting up table migration
<a name="s3-tables-migrate-setting-up"></a>

Before you migrate a table, make sure that you have the required resources and permissions. You can also choose how migration writes your destination table.

## Required resources
<a name="s3-tables-migrate-required-resources"></a>
+ **Source table** – An AWS Glue Data Catalog Apache Hive external table that stores its data as Apache Parquet in an Amazon S3 general purpose bucket.
+ **Destination table bucket** – The table bucket where the migration job creates the destination table. The namespace must already exist, and the destination table does not.
+ **Report bucket** – A general purpose bucket where the migration job writes the compatibility reports and the object migration report.
+ **Migration role** – An AWS Identity and Access Management (IAM) role that the migration job assumes to run the migration.

For account, Region, and source table requirements, see [Considerations and limitations](#s3-tables-migrate-considerations).

## Required permissions
<a name="s3-tables-migrate-required-permissions"></a>

The migration role must be able to read your source and write your destination table and reports. Grant the role the following permissions:
+ **Source table metadata** – `glue:GetTable`, `glue:GetPartitions`, and `glue:GetColumnStatisticsForPartition`.
+ **Source data** – `s3:ListBucket`, `s3:GetObject`, and `s3:GetObjectVersion` on the source bucket.
+ **Destination table** – `s3tables:CreateTable`, `s3tables:GetTable`, `s3tables:GetTableMetadataLocation`, `s3tables:UpdateTableMetadataLocation`, `s3tables:GetTableData`, `s3tables:PutTableData`, and `s3tables:PutTableMaintenanceConfiguration`. To set tags, encryption, or a storage class, also `s3tables:TagResource`, `s3tables:PutTableEncryption`, or `s3tables:PutTableStorageClass`.
+ **Reports** – `s3:PutObject` on the report bucket and prefixes.
+ **Encryption** – For SSE-KMS source objects, `kms:Decrypt` on the source key. For an SSE-KMS destination table, `kms:GenerateDataKey`, `kms:Decrypt`, and `kms:DescribeKey` on the destination key, which must also allow `maintenance.s3tables.amazonaws.com`. For an SSE-KMS report bucket, `kms:GenerateDataKey` on that key. For an example IAM policy with these AWS KMS permissions, see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md).

The role's trust policy must allow the S3 Tables migration service principal, `migration.s3tables.amazonaws.com`, to assume the role. The following example permissions policy grants the required permissions. The policy includes AWS KMS statements for SSE-KMS source objects, an SSE-KMS destination table, and an SSE-KMS report bucket. To use these examples, remove the statements for keys that you don't use and replace the placeholders with your own information.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadSourceTableMetadata",
      "Effect": "Allow",
      "Action": ["glue:GetTable", "glue:GetPartitions", "glue:GetColumnStatisticsForPartition"],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/{{example_database}}",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:table/{{example_database}}/{{example_source_table}}"
      ]
    },
    {
      "Sid": "ListSourceBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-source-bucket}}"
    },
    {
      "Sid": "ReadSourceObjects",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:GetObjectVersion"],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-source-bucket}}/{{example-table-location}}/*"
    },
    {
      "Sid": "WriteReports",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{migration-reports}}/*"
    },
    {
      "Sid": "CreateDestinationTable",
      "Effect": "Allow",
      "Action": [
        "s3tables:CreateTable",
        "s3tables:TagResource",
        "s3tables:PutTableEncryption",
        "s3tables:PutTableStorageClass"
      ],
      "Resource": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}"
    },
    {
      "Sid": "WriteDestinationTable",
      "Effect": "Allow",
      "Action": [
        "s3tables:GetTable",
        "s3tables:GetTableMetadataLocation",
        "s3tables:UpdateTableMetadataLocation",
        "s3tables:GetTableData",
        "s3tables:PutTableData",
        "s3tables:PutTableMaintenanceConfiguration"
      ],
      "Resource": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/*"
    },
    {
      "Sid": "DecryptSourceObjects",
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{source-key-id}}",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::{{amzn-s3-demo-source-bucket}}/{{example-table-location}}/*"
        }
      }
    },
    {
      "Sid": "EncryptDestinationTable",
      "Effect": "Allow",
      "Action": ["kms:GenerateDataKey", "kms:Decrypt", "kms:DescribeKey"],
      "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{destination-key-id}}",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}/table/*"
        }
      }
    },
    {
      "Sid": "EncryptReports",
      "Effect": "Allow",
      "Action": "kms:GenerateDataKey",
      "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{report-bucket-key-id}}",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{migration-reports}}/*"
        }
      }
    }
  ]
}
```

The following example trust policy allows the migration service principal to assume the role only for migrations into the specified table bucket.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "migration.s3tables.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{111122223333}}",
          "aws:SourceArn": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}"
        }
      }
    }
  ]
}
```

### Permissions for the identity that runs the migration
<a name="s3-tables-migrate-identity-permissions"></a>

The IAM identity that runs the migration needs the following permissions:
+ `s3tables:StartTableMigration` and `s3tables:ListTableMigrations` on the table bucket.
+ `s3tables:SyncTableMigration`, `s3tables:GetTableMigration`, `s3tables:UpdateTableMigration`, and `s3tables:CompleteTableMigration` on the destination table.
+ `iam:PassRole` on the migration role, with the condition `iam:PassedToService` set to `migration.s3tables.amazonaws.com`.
+ If the destination table uses SSE-KMS, `kms:DescribeKey` and `kms:GenerateDataKey` on the table's KMS key. The key must be an enabled customer managed key.

The migration role must be in the same AWS account as the identity that starts the migration.

## Destination and migration settings
<a name="s3-tables-migrate-compaction-settings"></a>

You set these settings and your migration policy when you start a migration, and every sync uses them. Settings that you don't specify use the defaults in the following table.


| Setting | Request parameter | Default | Supported values | 
| --- | --- | --- | --- | 
| Compression codec | destinationTable.properties.compressionCodec | zstd | zstd, snappy, gzip, uncompressed | 
| Dictionary encoding | destinationTable.properties.dictionaryEncoding | true | true, false | 
| Target file size | dataMigration.maintenanceSettings.icebergCompaction.targetFileSizeMB | 512 | 64–512 MB | 
| Compaction strategy | dataMigration.maintenanceSettings.icebergCompaction.strategy | binpack | binpack. After you complete the migration, you can choose another strategy in the table's maintenance configuration. | 
| Sort order | destinationTable.icebergSortOrder | None | Up to five columns. Requires a destination schema that you specify. | 
| Minimum snapshots to keep | dataMigration.maintenanceSettings.icebergSnapshotManagement.minSnapshotsToKeep | 3 | 3 or more | 
| Maximum snapshot age | dataMigration.maintenanceSettings.icebergSnapshotManagement.maxSnapshotAgeHours | 120 hours | 1 hour or more | 
| Iceberg version | destinationTable.properties.icebergFormatVersion | 2 | Versions 2 and 3 | 

## Considerations and limitations
<a name="s3-tables-migrate-considerations"></a>
+ Migration supports AWS Glue Data Catalog Apache Hive external tables that store data as Apache Parquet, either uncompressed or compressed with Snappy, gzip, Zstandard, Brotli, or LZ4. Other file formats (e.g. ORC, Avro, and JSON) and compression codecs (e.g. LZO) aren't supported.
+ Migration doesn't support transactional (ACID) Hive tables, tables already in an open table format, such as Apache Iceberg, tables that use a storage handler, or tables that skip header or footer lines.
+ Migration doesn't support AWS Glue tables that are also registered with AWS Lake Formation.
+ A sync fails an object that was overwritten since the previous start or sync, even if the new object has identical content, and even in a versioned bucket.
+ The source table, the destination table bucket, and the report bucket must be in the same AWS account and AWS Region. Cross-account and federated AWS Glue catalogs aren't supported.
+ Every partition must be stored under the table location registered in AWS Glue. If a partition is stored elsewhere, move its data under the table location and update its location in AWS Glue.
+ Partition columns of data type `binary`, `uniontype`, or a nested data type aren't supported. Tables that use Amazon Athena partition projection aren't supported until you register their partitions in AWS Glue, for example with `MSCK REPAIR TABLE`.
+ Migration doesn't support source objects encrypted with customer-provided keys (SSE-C).
+ Migration doesn't support objects that require a restore before access, such as S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, and the S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers. Restore or copy these objects first.
+ Migration doesn't copy AWS Glue table parameters, SerDe settings, column statistics, column comments, or the table description. It also doesn't migrate directory markers, empty objects, or objects whose name or folder starts with `_` or `.`, which Hive ignores.
+ Migration is available in the US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm) AWS Regions.
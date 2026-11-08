

# Use Athena system tables
<a name="athena-system-tables"></a>

With *system tables for Amazon Athena*, your usage data is automatically stored in tables that you can query for observability, cost analysis, auditing, and governance. Athena system tables are stored as fully managed [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/), using [Apache Iceberg](https://aws.amazon.com/what-is/apache-iceberg/) format, allowing you to query them with Athena, [DuckDB](https://duckdb.org), [Amazon Redshift](https://aws.amazon.com/redshift/), or any other engine that is compatible with Apache Iceberg. You can also use AI agent skills to get insights from your system table data by asking questions in natural language, without writing SQL. For more information, see [System table skills for AWS Agent Toolkit](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/system-table-skills) on the GitHub website.

When you enable this feature, it covers all workgroups in your account, including workgroups that you create after you enable it. As new system tables become available, they are included automatically. Athena manages the tables for you, including schema definition, partitioning, compaction, and snapshot maintenance, so there is no infrastructure to build or maintain. You control how long data is retained by configuring record expiration through S3 Tables.

This feature supports the following:
+ **Analyze usage without extract, transform, and load (ETL)**. Search, filter, aggregate, and join across your usage data directly, without building or maintaining custom pipelines.
+ **Meet compliance and audit requirements**. Keep usage data for as long as you need, whether that is months or years.
+ **Monitor your usage in one place**. See activity across all workgroups in your account and Region, identify high-usage workgroups, and spot patterns.
+ **Attribute usage by team or project**. Break down usage by team, workgroup, or time period to attribute usage accurately.
+ **Optimize workload performance**. Identify trends, regressions, and optimization opportunities across your workloads over time.

**Topics**
+ [How it works](#athena-system-tables-how-it-works)
+ [Supported system tables](#athena-system-tables-supported)
+ [Enabling system tables](#athena-system-tables-enabling)
+ [Security](#athena-system-tables-security)
+ [Data governance](#athena-system-tables-data-governance)
+ [Delivery and lifecycle behavior](#athena-system-tables-lifecycle)
+ [Best practices](#athena-system-tables-best-practices)
+ [Billing](#athena-system-tables-billing)
+ [Considerations and limitations](#athena-system-tables-considerations)
+ [query\_executions](athena-system-table-query-executions.md)

## How it works
<a name="athena-system-tables-how-it-works"></a>

After you enable system tables through the [Athena console](https://console.aws.amazon.com/athena/), the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), or SDK, Athena writes usage data from all workgroups in your account and Region to Apache Iceberg tables stored in S3 Tables. Data is delivered in batches at a fixed frequency.

System tables reside in your account, but Athena manages them, including the following:
+ Creating the S3 Tables bucket, namespace, and tables in your account.
+ Defining and evolving the table schemas.
+ Writing data in Apache Iceberg format.
+ Compacting data and maintaining snapshots, using the built-in S3 Tables compaction feature.

Because Athena manages system tables, you cannot insert, update, or delete individual rows. You control read access to the tables and manage data retention through S3 Tables record expiration.

Only completed activity is delivered. In-flight activity is not written. Once a row has been written to a system table, it will not be updated. The delivered data is immutable.

### Storage location
<a name="athena-system-tables-storage-location"></a>

Athena stores your system table data in an S3 Tables bucket named `aws-athena` in your account and Region. The data is organized as follows:

```
aws-athena/                          # S3 Tables bucket (one per account per Region)
  +-- metadata/                      # Namespace
      +-- query_executions/           # Table
```

You can query a system table using its fully qualified name, like this:

```
SELECT * FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
```

## Supported system tables
<a name="athena-system-tables-supported"></a>

The following system tables are available:
+ [query\_executions](athena-system-table-query-executions.md)

## Enabling system tables
<a name="athena-system-tables-enabling"></a>

Athena system tables are an opt-in feature managed at the account and Region level. When you enable system tables, Athena provisions an S3 Tables bucket and namespace in your account, and usage data is published for all your current and future resources.

### Using the console
<a name="athena-system-tables-enabling-console"></a>

**To enable system tables**

1. Open the Athena console.

1. In the left navigation pane, under **Administration**, choose **System tables**.

1. Choose **Configure**.

1. Turn on the **Enable system tables for all your current and future resources** toggle.

1. Review the list of tables and their coverage. All supported system tables are enabled with scope **All**.

1. (Optional) Expand **Data encryption** and choose an AWS KMS key to encrypt the usage data written to S3 Tables. If you do not choose a key, Athena uses Amazon S3 managed keys (SSE-S3). The key applies to every current and future S3 table and takes effect when Athena first writes data. For more information, see [Configuring encryption](#athena-system-tables-configuring-encryption).

1. Choose **Save**.

After you save, Athena begins writing usage data to S3 Tables. The system tables page shows a summary of tables enabled, their scope, coverage, and the KMS key (if configured).

To disable system tables, choose **Configure**, turn off the toggle, and choose **Save**. Disabling stops new data from being written to the system tables. The tables will remain, and existing data will still be queryable. To permanently delete system tables, also drop the tables using SQL or from the S3 Tables console.

When you disable system tables for an account, query metadata ingestion stops immediately. Queries that were submitted but not yet written to `query_executions` when you disable the feature might not be ingested, so recent executions can be missing from the table.

### Using the AWS CLI
<a name="athena-system-tables-enabling-cli"></a>

You manage system tables using the following APIs:


| API | Description | 
| --- | --- | 
| CreateSystemTableConfiguration | Enable system tables for your account. Provisions the S3 Tables bucket and starts publishing. | 
| UpdateSystemTableConfiguration | Update the configuration (for example, change the KMS key before the table is created). | 
| DeleteSystemTableConfiguration | Disable system tables. Stops publishing new data. The table and all previously published data are retained. | 
| GetSystemTableConfiguration | Return the current configuration for your account. | 
| ListSystemTableStatuses | List the physical system tables and whether they are enabled. | 

#### Enable system tables
<a name="athena-system-tables-enabling-cli-enable"></a>

```
aws athena create-system-table-configuration \
    --table-name ALL
```

To use a customer managed KMS key for encryption, specify the key ARN:

```
aws athena create-system-table-configuration \
    --table-name ALL \
    --kms-key-arn arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab
```

#### Check current configuration
<a name="athena-system-tables-enabling-cli-check"></a>

```
aws athena get-system-table-configuration \
    --table-name ALL
```

#### List system table statuses
<a name="athena-system-tables-enabling-cli-list"></a>

```
aws athena list-system-table-statuses
```

#### Disable system tables
<a name="athena-system-tables-enabling-cli-disable"></a>

```
aws athena delete-system-table-configuration \
    --table-name ALL
```

### Registering with AWS Glue Data Catalog
<a name="athena-system-tables-registering-glue"></a>

Before you can query system table data, the S3 Tables bucket must be integrated with [AWS Glue](https://aws.amazon.com/glue/) Data Catalog. This is a one-time step per account and Region. If you have already integrated S3 Tables with AWS Glue Data Catalog, no additional action is required.

For integration instructions, see [Integrating Amazon S3 Tables with AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/glue-federation-s3tables.html) in the *AWS Glue Developer Guide*.

### IAM permissions
<a name="athena-system-tables-iam-permissions"></a>

System tables use two kinds of permissions. Administrators who enable, update, and disable system tables need the permissions in [Permissions to manage system tables](#athena-system-tables-iam-admin). Users who only query system tables need the permissions in [Permissions to query system tables](#athena-system-tables-iam-reader). Both example policies follow the principle of least privilege. Replace `<REGION>`, `<ACCOUNT>`, and the other placeholders with your own values.

The system table resource ARN format is `arn:{partition}:athena:{region}:{account}:system-table/{tableName}`. For the configuration operations, the resource is `system-table/{tableName}`, where `{tableName}` is the value of the `TableName` parameter in the request. Currently, `ALL` is the only supported value. For `ListSystemTableStatuses`, the resource is `system-table/*`.

#### Permissions to manage system tables
<a name="athena-system-tables-iam-admin"></a>

The following policy allows a principal to enable, update, view, and disable system tables. When you enable system tables, Athena uses your credentials to create the `aws-athena` S3 Tables bucket and attach its bucket policy. For this reason, you need both `s3tables:CreateTableBucket` and `s3tables:PutTableBucketPolicy`. If you encrypt system tables with a customer managed key, you also need `kms:DescribeKey` on that key. Omit the `ValidateEncryptionKey` statement if you use the default Amazon S3 managed keys (SSE-S3). Omit the `TagSystemTableConfiguration` statement if you don't tag the configuration.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageSystemTableConfiguration",
      "Effect": "Allow",
      "Action": [
        "athena:CreateSystemTableConfiguration",
        "athena:UpdateSystemTableConfiguration",
        "athena:DeleteSystemTableConfiguration",
        "athena:GetSystemTableConfiguration"
      ],
      "Resource": "arn:aws:athena:<REGION>:<ACCOUNT>:system-table/<TABLE_NAME>"
    },
    {
      "Sid": "ListSystemTableStatuses",
      "Effect": "Allow",
      "Action": "athena:ListSystemTableStatuses",
      "Resource": "arn:aws:athena:<REGION>:<ACCOUNT>:system-table/*"
    },
    {
      "Sid": "TagSystemTableConfiguration",
      "Effect": "Allow",
      "Action": [
        "athena:TagResource",
        "athena:UntagResource",
        "athena:ListTagsForResource"
      ],
      "Resource": "arn:aws:athena:<REGION>:<ACCOUNT>:system-table/<TABLE_NAME>"
    },
    {
      "Sid": "CreateSystemTablesBucket",
      "Effect": "Allow",
      "Action": [
        "s3tables:CreateTableBucket",
        "s3tables:PutTableBucketPolicy"
      ],
      "Resource": "arn:aws:s3tables:<REGION>:<ACCOUNT>:bucket/aws-athena"
    },
    {
      "Sid": "ValidateEncryptionKey",
      "Effect": "Allow",
      "Action": "kms:DescribeKey",
      "Resource": "arn:aws:kms:<REGION>:<ACCOUNT>:key/<KEY_ID>"
    }
  ]
}
```

To register the S3 Tables bucket with AWS Glue Data Catalog, the administrator also needs `glue:CreateCatalog` and `glue:PassConnection`. For more information, see [Registering with AWS Glue Data Catalog](#athena-system-tables-registering-glue).

#### Permissions to query system tables
<a name="athena-system-tables-iam-reader"></a>

The following policy allows a principal to query system tables in one workgroup without granting any permission to change the configuration or the table data. The principal also needs permissions to write query results to the workgroup's query result location. If system tables are encrypted with a customer managed key, the principal needs `kms:Decrypt` and `kms:DescribeKey` on that key. Without them, the query fails with `TABLE_NOT_FOUND` rather than an access denied error. Omit the `DecryptSystemTables` statement if you use the default SSE-S3 encryption.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RunQueries",
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:StopQueryExecution"
      ],
      "Resource": "arn:aws:athena:<REGION>:<ACCOUNT>:workgroup/<WORKGROUP>"
    },
    {
      "Sid": "ReadSystemTablesCatalog",
      "Effect": "Allow",
      "Action": [
        "glue:GetCatalog",
        "glue:GetDatabase",
        "glue:GetDatabases",
        "glue:GetTable",
        "glue:GetTables",
        "glue:GetPartitions"
      ],
      "Resource": [
        "arn:aws:glue:<REGION>:<ACCOUNT>:catalog",
        "arn:aws:glue:<REGION>:<ACCOUNT>:catalog/s3tablescatalog",
        "arn:aws:glue:<REGION>:<ACCOUNT>:catalog/s3tablescatalog/*",
        "arn:aws:glue:<REGION>:<ACCOUNT>:database/*",
        "arn:aws:glue:<REGION>:<ACCOUNT>:table/*"
      ]
    },
    {
      "Sid": "ReadSystemTablesData",
      "Effect": "Allow",
      "Action": [
        "s3tables:GetTableBucket",
        "s3tables:ListNamespaces",
        "s3tables:GetNamespace",
        "s3tables:ListTables",
        "s3tables:GetTable",
        "s3tables:GetTableData",
        "s3tables:GetTableMetadataLocation"
      ],
      "Resource": [
        "arn:aws:s3tables:<REGION>:<ACCOUNT>:bucket/aws-athena",
        "arn:aws:s3tables:<REGION>:<ACCOUNT>:bucket/aws-athena/*"
      ]
    },
    {
      "Sid": "LakeFormationDataAccess",
      "Effect": "Allow",
      "Action": "lakeformation:GetDataAccess",
      "Resource": "*"
    },
    {
      "Sid": "DecryptSystemTables",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "arn:aws:kms:<REGION>:<ACCOUNT>:key/<KEY_ID>"
    }
  ]
}
```

`lakeformation:GetDataAccess` does not support resource-level permissions, so its resource must be `*`.

### Configuring encryption
<a name="athena-system-tables-configuring-encryption"></a>

By default, data in system tables is encrypted with Amazon S3 managed keys (SSE-S3). To use a customer managed AWS KMS key, specify the `KmsKeyArn` parameter when you call `CreateSystemTableConfiguration`.

The KMS key is immutable after the system table is created by the ingestion pipeline. If you need to change the key after the table exists, you must drop the table through the S3 Tables API (which permanently removes the data) and then call `CreateSystemTableConfiguration` again with the new key.

If you use a customer managed key, the key policy must grant both the Amazon Athena system tables service principal (`systemtables.athena.amazonaws.com`) and the S3 Tables maintenance service principal (`maintenance.s3tables.amazonaws.com`) access to the key. Add the following statements to your key policy, replacing `<REGION>`, `<ACCOUNT>`, and `<KEY_ID>` with your values.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnableAthenaSystemTableKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "systemtables.athena.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "arn:aws:kms:<REGION>:<ACCOUNT>:key/<KEY_ID>",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT>"
        }
      }
    },
    {
      "Sid": "EnableS3TableMaintenanceKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "maintenance.s3tables.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "arn:aws:kms:<REGION>:<ACCOUNT>:key/<KEY_ID>",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:<REGION>:<ACCOUNT>:bucket/aws-athena/*"
        }
      }
    }
  ]
}
```

## Security
<a name="athena-system-tables-security"></a>

System tables follow the AWS shared responsibility model. For encryption, see [Data protection in Athena](security-data-protection.md). For permissions, see [Configure access to system tables](security-iam-system-tables.md). For auditing, see [Log and monitor Athena](security-logging-monitoring.md). The Athena and S3 Tables endpoints use TLS to encrypt data in transit to and from system tables.

## Data governance
<a name="athena-system-tables-data-governance"></a>

You govern access to system table data. Athena does not apply read permissions on your behalf and does not mask data.
+ **Cataloging and discovery**. The AWS Glue Data Catalog integration provides a central place to discover system tables and apply fine-grained permissions.
+ **Access control**. After you register the S3 Tables bucket with AWS Glue Data Catalog, you can govern read access using IAM or [AWS Lake Formation](https://aws.amazon.com/lake-formation/). You can apply table-level, column-level, or row-level permissions.
+ **Sensitive data**. You might determine that your usage data contains sensitive information. For example, query text might include personally identifiable information (PII) or proprietary logic. Consider restricting access to sensitive columns using column-level permissions in Lake Formation, or limit access to specific principals.

## Delivery and lifecycle behavior
<a name="athena-system-tables-lifecycle"></a>
+ **Delivery frequency**. Data is delivered in batches at a fixed frequency.
+ **Exactly-once delivery**. Each record appears exactly once. Re-enabling the feature does not create duplicates.
+ **Enable, disable, re-enable**. While system tables are disabled (through the console or `DeleteSystemTableConfiguration`), no data is captured for that period. Re-enabling (through the console or `CreateSystemTableConfiguration`) resumes delivery going forward. The gap period is not backfilled.
+ **Disabling**. Disabling through the console or by calling `DeleteSystemTableConfiguration` stops publishing new data. The table and all previously delivered data are retained and remain queryable.
+ **Dropping the table**. You can drop the underlying table using a [`DROP TABLE`](https://docs.aws.amazon.com/athena/latest/ug/drop-table.html) statement in Athena or through the S3 Tables API. This permanently removes all previously delivered data. If system tables are still enabled, the table is recreated automatically on the next ingestion cycle, but the old data is not recovered. For more information, see [Deleting S3 tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html) in the *Amazon S3 User Guide*.

## Best practices
<a name="athena-system-tables-best-practices"></a>

1. **Restrict access to sensitive data.** Some system tables can contain sensitive information such as query text with personally identifiable information (PII). Use IAM or Lake Formation to restrict read access based on your governance requirements. For more information, see [Data governance](#athena-system-tables-data-governance).

1. **Configure encryption before the table is created.** If you want to use a customer managed AWS KMS key, specify it when you first enable the feature. The key cannot be changed after the table is created. For more information, see [Configuring encryption](#athena-system-tables-configuring-encryption).

1. **Set retention through S3 Tables.** Athena does not set a default retention period. Data is kept indefinitely until you configure expiration. Use the S3 Tables record expiration feature to set retention based on your compliance and cost requirements. For more information, see [Configuring record expiration for S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html) in the *Amazon S3 User Guide*. The minimum retention is 1 day with no upper limit.

1. **Use partition filters for better query performance.** Athena system tables are partitioned. Include filters on the partition column in your queries to benefit from partition pruning and reduce data scanned. To see the partition columns of a system table, use the [`DESCRIBE`](https://docs.aws.amazon.com/athena/latest/ug/describe-table.html) statement. For example, when you query the `query_executions` table, filter on `work_group_name`.

## Billing
<a name="athena-system-tables-billing"></a>
+ **Delivery is free.** Athena does not charge for writing usage data to S3 Tables.
+ **S3 Tables storage.** You pay standard S3 Tables storage and maintenance charges for the retained data. For more information, see [Amazon S3 Tables pricing](https://aws.amazon.com/s3/pricing/).
+ **Query costs.** You pay standard Athena query charges when querying system tables. Other engines, such as DuckDB, Amazon Redshift, and Amazon EMR, follow their own pricing.

## Considerations and limitations
<a name="athena-system-tables-considerations"></a>
+ Athena system tables are supported within a single AWS account and a single AWS Region. Cross-account and cross-Region consolidation is not supported.
+ Delivered data is immutable. You cannot insert, update, or delete individual rows.
+ No default retention is set. You must configure record expiration through S3 Tables to manage storage costs.
+ Querying system tables requires integrating the S3 Tables bucket with AWS Glue Data Catalog.
# Exporting asset metadata

In the current release of Amazon SageMaker Unified Studio, you can export asset metadata as an Apache Iceberg
table through Amazon S3 Tables. This allows data teams to query catalog inventory and answer
questions - like the following: How many assets were registered last month?, Which assets
are classified as confidential?, or Which assets lack business descriptions?, etc. using
standard SQL without building custom ETL infrastructure for reporting.

This capability automatically converts catalog asset metadata into a queryable table
accessible from Amazon Athena, Amazon SageMaker Unified Studio notebooks, AI agents, and other analytics and BI
tools. The exported table includes technical metadata (such as resource_id, resource_type),
business metadata (such as asset_name, business_description), ownership details, and
timestamps. Data is partitioned by snapshot_date for query performance and automatically
appears in Amazon SageMaker Unified Studio under the aws-sagemaker-catalog bucket.

###### Note

You can enable asset metadata export for only one domain per AWS account per Region.
To enable export for a different domain, complete the following steps:

1. Delete the export configuration for the currently enabled domain using
   the DeleteDataExportConfiguration operation.
2. Delete the asset S3 table under the aws-sagemaker-catalog S3 table bucket.
   We recommend backing up the S3 table before deletion.
3. Call the PutDataExportConfiguration API to enable export for the new
   domain.
   Also, encryption configuration for the exported asset table cannot be updated.

This capability is available in all AWS Regions where Amazon SageMaker Catalog is
supported at no additional charge. You pay only for underlying services including S3 Tables
storage and Amazon Athena queries. You can control storage costs by setting retention
policies on S3 tables to automatically remove records older than your specified period. For
more information, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html](../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md "../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md").

## Requirements

Before you export asset metadata from Amazon SageMaker Unified Studio, make sure that you meet the following requirements:

### IAM permissions

The IAM user or role that runs the export commands must have permissions to configure asset metadata export in Amazon DataZone and to create the Amazon S3 Tables resources used to store the exported metadata.

The following example IAM policy shows the required permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "datazone:GetDataExportConfiguration",
                "datazone:PutDataExportConfiguration"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3tables:CreateTableBucket",
                "s3tables:PutTableBucketPolicy"
            ],
             "Resource": "arn:aws:s3tables:<REGION>:<ACCOUNT_ID>:bucket/aws-sagemaker-catalog"
        }
    ]
}
```

These permissions allow you to retrieve and update the asset metadata export configuration. They also allow Amazon DataZone to create the Amazon SageMaker Catalog S3 table bucket and apply the required bucket policy on your behalf, enabling DataZone to write the exported metadata.

For KMS related permission requirements, see [KMS permissions for exporting asset metadata in Amazon SageMaker Unified
Studio](../adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md "../adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md").

## Start exporting asset

metadata

To get started, activate dataset export by invoking the
`PutDataExportConfiguration` API action. In response, the DataZone
service creates an S3 table bucket named aws-sagemaker-catalog with an asset_metadata
namespace and an empty asset table. It also schedules a daily job to export updated
asset data. Within 24 hours, you can access the asset table through the S3 Tables
console or the Data tab in Amazon SageMaker Unified Studio. You can query the data using Amazon Athena or
Studio notebooks, or connect external BI tools through the S3 Tables Iceberg REST
Catalog endpoint.

Asset metadata is exported once a day around midnight local time per AWS
region.

Enable data export:

```

aws datazone put-data-export-configuration  --domain-identifier dzd-440699i00ezy21 --region us-east-2 --enable-export

```

With KMS key encryption configuration:

```

aws datazone put-data-export-configuration --encryption-configuration kmsKeyArn=arn:aws:kms:us-east-2:651673343886:key/292fedfe-c9h6-40fa-961b-87393584195c,sseAlgorithm=aws:kms --enable-export --region us-east-2 --domain-identifier dzd-440699i00ezy21

```

For more information, see the [API
reference documentation](../../../datazone/latest/APIReference/API_PutDataExportConfiguration.md "../../../datazone/latest/APIReference/API_PutDataExportConfiguration.md").

## Asset table schema

The asset metadata is exported to the following table structure:

| Column name          | Data type          | Comment                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| snapshot_time        | timestamp          | Timestamp when this metadata snapshot was captured from AWS<br>Sagemaker. Partition key for temporal queries. Use for point-in-time<br>analysis and time-travel queries (e.g., "show catalog state 30 days<br>ago").                                                                                                                              |
| asset_id             | string             | Unique identifier assigned by AWS Sagemaker Catalog for this asset.<br>Primary key for asset lookups.                                                                                                                                                                                                                                             |
| resource_type_enum   | string             | Type of data resource cataloged. Values: GlueTable, RedshiftTable,<br>S3Collection etc. Used for filtering by resource category.                                                                                                                                                                                                                  |
| resource_id          | string             | Platform-native unique identifier for the resource. For AWS: ARN<br>format (e.g., arn:aws:glue:region:account:table/db/table). Use for<br>cross-referencing with source systems.                                                                                                                                                                  |
| account_id           | string             | Cloud account or organizational identifier. For AWS: 12-digit account<br>ID. Used for multi-account queries and cost allocation.                                                                                                                                                                                                                  |
| region               | string             | Geographic region or availability zone where resource is hosted. For<br>AWS: us-east-1, eu-west-1, etc. NULL for region-agnostic resources. Use<br>for regional analysis and compliance queries.                                                                                                                                                  |
| catalog              | string             | Top-level namespace identifier. Meaning varies by resource_type: For<br>GLUE_TABLE: AWS account ID. For REDSHIFT_TABLE: database name. For<br>S3_COLLECTION: AWS account ID. Use for catalog-level grouping.                                                                                                                                      |
| namespace            | string             | Mid-level namespace identifier. Meaning varies by resource_type: For<br>GLUE_TABLE: database name. For REDSHIFT_TABLE: schema name. For<br>S3_COLLECTION: bucket name. May contain multiple levels (e.g.,<br>database.schema).                                                                                                                    |
| asset_name           | string             | Business friendly name for this asset. Optional business identifier<br>that can differ from the technical resource_name. NULL if no custom name<br>was provided during asset registration. Examples: 'Customer Master<br>Dataset', 'Q4 Sales Report', 'Production Orders Table'. Use for<br>user-friendly display and business-oriented searches. |
| resource_name        | string             | Leaf-level resource identifier. For tables: table name. For S3:<br>prefix path. For views: view name. Use for resource-level<br>filtering.                                                                                                                                                                                                        |
| resource_description | string             | Technical description from source system. For Glue: table comment<br>field. For Redshift: table remarks. NULL if source system has no<br>description. Use for technical documentation searches.                                                                                                                                                   |
| business_description | string             | Business-friendly description provided to AWS Sagemaker Catalog.<br>Explains purpose, usage, and business context of the asset. NULL if not<br>provided by data owner. Use for business glossary and discovery<br>queries.                                                                                                                        |
| extended_metadata    | map<string,string> | Flexible key-value store for platform-specific attributes not covered<br>by standard columns. Examples: s3_location, compression_type,<br>column_count, partition_keys, namespace_name, cluster_name. Use for<br>advanced filtering and platform-specific queries. Schema varies by<br>platform and resource_type.                                |
| asset_created_time   | timestamp          | Timestamp when this asset was first created in AWS Sagemaker<br>Catalog.                                                                                                                                                                                                                                                                          |
| asset_updated_time   | timestamp          | Timestamp when this asset was last updated in AWS Sagemaker<br>Catalog.                                                                                                                                                                                                                                                                           |

## Querying asset tables

To query Amazon S3 tables using Amazon SageMaker Unified Studio or Amazon Athena you must first do the
following:

- Enable analytic services integration by following [https://docs.aws.amazon.com/lake-formation/latest/dg/enable-s3-tables-catalog-integration.html](../../../lake-formation/latest/dg/enable-s3-tables-catalog-integration.md "../../../lake-formation/latest/dg/enable-s3-tables-catalog-integration.md")
- Grant the query role permission in Lake Formation by following [https://docs.aws.amazon.com/lake-formation/latest/dg/granting-table-permissions.html](../../../lake-formation/latest/dg/granting-table-permissions.md "../../../lake-formation/latest/dg/granting-table-permissions.md")

Example CLI command:

```
aws lakeformation grant-permissions \
        —principal DataLakePrincipalIdentifier=arn:aws:iam::123456789012:role/datazone_usr_role_3guzb15tfpk015_agjdowt5f47xgp \
        --resource '{"Table": {"CatalogId": "123456789012:s3tablescatalog/aws-sagemaker-catalog", "DatabaseName": "asset_metadata", "Name": "asset"}}' \
        --permissions DESCRIBE SELECT —region us-east-2
```

### Assets registered in last one month

- Query with sample aggregates

```
SELECT
    DATE(asset_created_time) as date,
    resource_type_enum,
    COUNT(*) as count
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
    AND asset_created_time >= DATE_ADD('month', -1, CURRENT_DATE)
GROUP BY DATE(asset_created_time), resource_type_enum
ORDER BY date DESC;
```

- Plain query without aggregates and groupBy

```
SELECT *
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
    AND asset_created_time >= DATE_ADD('month', -1, CURRENT_DATE)
```

### Assets without business description or owningEntityId in them

```
SELECT
    asset_id,
    asset_name,
    resource_name,
    resource_type_enum,
    account_id,
    business_description,
    extended_metadata['owningEntityId'] as owner
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
    AND (business_description IS NULL
         OR extended_metadata['owningEntityId'] IS NULL);
```

### Query asset matching metadata form field values

```
SELECT *
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
    AND extended_metadata['<metadata-form-name>.<field-name>'] = '<field-value>';
```

### Asset distribution queries

- Get distributions by account

```
SELECT
    account_id,
    resource_type_enum,
    COUNT(*) as count
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
GROUP BY account_id, resource_type_enum
ORDER BY count DESC
```

- Get distribution by asset owner (projectIds)

```
SELECT
    extended_metadata['owningEntityId'] as owner,
    COUNT(*) as count
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE
    AND extended_metadata['owningEntityId'] IS NOT NULL
GROUP BY extended_metadata['owningEntityId']
ORDER BY count DESC;
```

### Time travel capabilities

The asset_metadata.asset table captures daily snapshots of asset metadata,
allowing us to view the state of data catalog at any point in time. Simply change
the date filter in our query to travel back to any previous snapshot

###### Note

Querying without a snapshot_time filter will read all historical snapshots,
resulting in duplicate records and slower performance. Always filter by the
desired date or current timestamp.

- View Current Assets snapshot

```
SELECT *
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = CURRENT_DATE;
```

- Travel to a Specific Date ex: Nov-26-2025

```
SELECT *
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = DATE('2025-11-26');
```

- Travel Back Relative to Today ex: travel back by 2 days

```
SELECT *
FROM asset_metadata.asset
WHERE DATE(snapshot_time) = date_add('day', -2, CURRENT_DATE);
```

### Common use cases

1. Track Metadata Improvements see which assets gained descriptions or
   ownership over time:

```
SELECT
    t.asset_id,
    t.resource_name,
    p.business_description as description_before,
    t.business_description as description_now
FROM asset_metadata.asset t
JOIN asset_metadata.asset p ON t.asset_id = p.asset_id
WHERE DATE(t.snapshot_time) = CURRENT_DATE
    AND DATE(p.snapshot_time) = CURRENT_DATE - INTERVAL '7' DAY
    AND p.business_description IS NULL
    AND t.business_description IS NOT NULL;
```

2. Monitor Asset Growth View how data catalog has grown over the last 30
   days:

```
SELECT
    DATE(snapshot_time) as date,
    COUNT(*) as total_assets
FROM asset_metadata.asset
WHERE DATE(snapshot_time) >= CURRENT_DATE - INTERVAL '30' DAY
GROUP BY DATE(snapshot_time)
ORDER BY date DESC;
```

3. Audit Historical Changes to investigate what an asset looked like at a
   specific point in time:

```
SELECT
    asset_id,
    resource_name,
    business_description,
    extended_metadata['owningEntityId'] as owner,
    snapshot_time
FROM asset_metadata.asset
WHERE asset_id = 'your-asset-id'
    AND DATE(snapshot_time) = DATE('2025-11-26');
```

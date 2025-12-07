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

In the current release, you can enable exporting asset metadata only for one domain
per AWS account per region. If you disable exporting asset metadata feature for a
domain where it's already enabled, you cannot enable this feature for another domain in
the same AWS account and region.

Also, encryption configuration for the exported asset table cannot be updated.

This capability is available in all AWS Regions where Amazon SageMaker Catalog is
supported at no additional charge. You pay only for underlying services including S3 Tables
storage and Amazon Athena queries. You can control storage costs by setting retention
policies on S3 tables to automatically remove records older than your specified period. For
more information, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-record-expiration.html](../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md "../../../AmazonS3/latest/userguide/s3-tables-record-expiration.md").

## Start exporting asset

metadata

To get started, activate dataset export by invoking the
`PutDataExportConfiguration` API action, then access the asset table
through S3 Tables or Amazon SageMaker Unified Studio's Data tab within 24 hours. Query using Amazon Athena,
Studio notebooks, or connect external BI tools through the S3 Tables Iceberg REST
Catalog endpoint.

Asset metadata is exported once a day around midnight local time per AWS
region.

For more information, see [KMS permissions for exporting asset metadata in Amazon SageMaker Unified
Studio](../adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md "../adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.md").

Enable data export:

```

aws datazone put-data-export-configuration  --domain-identifier dzd-440699i00ezy21 --region us-east-2 --enable-export

```

With KMS key encryption configuration:

```

aws datazone put-data-export-configuration --encryption-configuration kmsKeyArn=arn:aws:kms:us-east-2:651673343886:key/292fedfe-c9h6-40fa-961b-87393584195c,sseAlgorithm=aws:kms --enable-export --region us-east-2 --domain-identifier dzd-440699i00ezy21

```

For more information, see the [API
reference documentation](../../../datazone/latest/APIReference/Welcome.md "../../../datazone/latest/APIReference/Welcome.md").

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

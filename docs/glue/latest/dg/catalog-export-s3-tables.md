

# Export metadata to S3 Tables (preview)
<a name="catalog-export-s3-tables"></a>

**Note**  
Catalog metadata export is available as a preview feature. This feature is subject to change before general availability.

## Overview
<a name="catalog-export-overview"></a>

You can export your AWS Glue Data Catalog metadata into managed catalog system tables stored in Amazon S3 Tables. When you enable the S3 Tables export, your technical and business metadata is stored in read-only Apache Iceberg tables in the AWS managed `aws-catalog` table bucket, making them queryable using SQL with AWS analytics services like , Amazon Redshift, and Amazon EMR.

Within the `aws-catalog` table bucket, system tables reside in the following namespaces:
+ `glue` — contains `tables` and `table_columns`.
+ `catalog_metadata` — contains `glossaries`, `glossary_terms`, `associated_glossary_terms`, `attachments`, and `item_attachments`.

The following system tables are currently supported:


| System table | Contains | 
| --- | --- | 
| `tables` | Technical and business metadata for each table in the Data Catalog, such as its name, database, description, storage location, and format. | 
| `table_columns` | The columns of each catalog table, including each column's name, data type, description, and whether it is a partition key. | 
| `glossaries` | The business glossaries in your catalog, including each glossary's name, description, and status. | 
| `glossary_terms` | The terms defined in your glossaries, including each term's name, descriptions, parent glossary, and status. | 
| `associated_glossary_terms` | The associations between glossary terms and assets, including the asset identifier and glossary term identifier. | 
| `attachments` | Custom-form metadata attached at the asset level, including the form type and the attachment content. | 
| `item_attachments` | Custom-form metadata attached to items within an asset, such as individual columns, including the iterable form name, item name, form type, and attachment content. | 

For the full column-level schema of each table, see [Catalog system tables reference](#catalog-export-system-tables-reference).

## How catalog metadata export works
<a name="catalog-export-how-it-works"></a>

After you enable export, the Data Catalog performs a one-time backfill of your existing catalog metadata and then keeps the system tables up to date as you make changes. Newly written or updated metadata typically becomes visible in the system tables within about 5 minutes.

The system tables reside in the `glue` and `catalog_metadata` namespaces within the `aws-catalog` table bucket. A given system table appears the first time metadata of that kind exists in your catalog. For example, if you enable export and your catalog contains only tables and databases, you see only the table-related system tables. The glossary system tables appear after you create your first glossary.

## Enable catalog metadata export using the AWS CLI
<a name="catalog-export-enable"></a>

Catalog metadata export is an account-level setting. You enable or disable it with the AWS CLI.

### Prerequisites
<a name="catalog-export-prerequisites"></a>

The IAM identity you use must have permission to call the export configuration operations `glue:PutDataCatalogExportConfiguration` and `glue:GetDataCatalogExportConfiguration`, as well as `s3tables:CreateTable`. For more information about S3 Tables permissions, see [Creating tables in S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html) in the *Amazon Simple Storage Service User Guide*.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:PutDataCatalogExportConfiguration",
                "glue:GetDataCatalogExportConfiguration"
            ],
            "Resource": "*"
        }
    ]
}
```

All data in S3 Tables, including Data Catalog metadata, is encrypted with SSE-S3 encryption by default. You can choose to encrypt your catalog export with AWS KMS keys (SSE-KMS). If you choose to encrypt with AWS KMS keys, you must add additional permissions by taking the following steps:

1. Grant the Data Catalog export service principal and the S3 Tables maintenance service principal permissions to use your KMS key (key policy).

1. Grant the IAM principal that runs the export permissions to use the KMS key (identity policy).

#### Granting the Data Catalog export service principal and S3 Tables maintenance service principal permissions to your KMS key
<a name="export-kms-permissions-service-principal"></a>

To allow AWS Glue to export encrypted catalog metadata and to allow automatic table maintenance like compaction and unreferenced file removal on the exported tables, you must grant the following service principals access to your KMS key:
+ `systemtables.catalog.amazonaws.com` — exports encrypted catalog metadata to S3 Tables.
+ `maintenance.s3tables.amazonaws.com` — performs automatic table maintenance on the exported tables.

AWS Glue writes to the AWS managed table bucket named `aws-catalog`. The KMS key used for encrypting the S3 Tables export does not need to be the same as the one used to encrypt the Data Catalog at rest. AWS Glue supports only symmetric KMS keys. To grant these service principals access, you can use the following example key policy. In this policy, the `maintenance.s3tables.amazonaws.com` service principal is granted permission to use a specific KMS key for encrypting and decrypting tables in the `aws-catalog` table bucket. For more information about the S3 Tables maintenance service principal, see [Permission requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html) in the *Amazon Simple Storage Service User Guide*.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSystemTablesDescribeKey",
            "Effect": "Allow",
            "Principal": {
                "Service": "systemtables.catalog.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        },
        {
            "Sid": "AllowSystemTablesEncryptDecrypt",
            "Effect": "Allow",
            "Principal": {
                "Service": "systemtables.catalog.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:{{us-east-1}}:{{123456789012}}:bucket/aws-catalog/table/*",
                    "kms:ViaService": "s3.{{us-east-1}}.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowS3TablesMaintenanceEncryptDecrypt",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:{{us-east-1}}:{{123456789012}}:bucket/aws-catalog/*"
                }
            }
        }
    ]
}
```

#### IAM permissions required for the principal for exporting
<a name="export-kms-permissions-exporting"></a>

Grant the principals that run exports the following permissions. The following policy grants the IAM principal access to decrypt a specific AWS Glue Data Catalog, scoped with the `glue_catalog_id` encryption context (the value is your `catalogId`).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowDescribeKey",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        },
        {
            "Sid": "AllowExportOfGlueDataCatalogByCatalogId",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}",
                    "kms:EncryptionContext:glue_catalog_id": "{{123456789012}}"
                }
            }
        }
    ]
}
```

### To enable catalog metadata export
<a name="catalog-export-enable-procedure"></a>

1. Run the following command to enable export:

   ```
   aws glue put-data-catalog-export-configuration \
       --export-setting ENABLED
   ```

1. Confirm the configuration by running the following command:

   ```
   aws glue get-data-catalog-export-configuration
   ```

   Example response:

   ```
   {
       "ExportSetting": "ENABLED",
       "Status": "ENABLED",
       "S3TableBucketArn": "arn:aws:s3tables:us-east-1:111122223333:bucket/aws-catalog"
   }
   ```

   The `Status` field transitions from `ENABLING` to `ENABLED` as the initial backfill progresses.

### To disable catalog metadata export
<a name="catalog-export-disable-procedure"></a>

Run the following command:

```
aws glue put-data-catalog-export-configuration \
    --export-setting DISABLED
```

## Catalog system tables reference
<a name="catalog-export-system-tables-reference"></a>

All system tables reside in the `glue` or `catalog_metadata` namespaces within the `aws-catalog` table bucket. Every table includes the following system columns:


| Column | Type | Description | 
| --- | --- | --- | 
| `ingestion_time` | timestamp | Time the record was ingested into the system table (UTC). | 
| `schema_version` | string | Schema version identifier for the table. | 

### tables
<a name="catalog-export-ref-glue-tables"></a>

Contains one row per catalog table.


| Column | Type | Description | 
| --- | --- | --- | 
| `id` | string | Unique identifier for the table. | 
| `catalog_id` | string | Catalog identifier. | 
| `catalog_name` | string | Catalog name. | 
| `update_time` | timestamp | Last update timestamp. | 
| `created_time` | timestamp | Creation timestamp. | 
| `created_by_id` | string | Identifier of the principal that created the table. | 
| `created_by_type` | string | Type of the creating principal. | 
| `description` | string | Table description. | 
| `name` | string | Table name. | 
| `namespace` | string | Namespace of the table. | 
| `region_name` | string | AWS Region. | 
| `tags` | map<string, string> | Resource tags. | 
| `type` | string | Asset type. | 
| `updated_by_id` | string | Identifier of the principal that last updated the table. | 
| `updated_by_type` | string | Type of the updating principal. | 
| `database_name` | string | Database containing the table. | 
| `input_format` | string | Input format class. | 
| `lake_formation_registration` | string | AWS Lake Formation registration status. | 
| `output_format` | string | Output format class. | 
| `owner` | string | Table owner. | 
| `retention` | int | Retention period. | 
| `serde_library` | string | Serialization/deserialization library. | 
| `table_data_format` | string | Data format. | 
| `table_data_location` | string | Data location URI. | 
| `table_format` | string | Table format (for example, Iceberg, Hudi). | 
| `table_type` | string | Table type. | 

### table\_columns
<a name="catalog-export-ref-glue-table-columns"></a>

Contains one row per column in a catalog table.


| Column | Type | Description | 
| --- | --- | --- | 
| `id` | string | Composite identifier in the format `assetId#columnName`. | 
| `asset_id` | string | Identifier of the parent table. | 
| `column_name` | string | Column name. | 
| `description` | string | Column description. | 
| `type` | string | Column data type. | 
| `is_partition_key` | boolean | Whether the column is a partition key. | 

### attachments
<a name="catalog-export-ref-attachments"></a>

Contains asset-level custom-form attachments (one row per attachment on an asset).


| Column | Type | Description | 
| --- | --- | --- | 
| `asset_id` | string | Identifier of the parent asset. | 
| `attachment_name` | string | Attachment name. | 
| `form_type_id` | string | Registered form type of the content. | 
| `content_json` | string | Attachment content as a JSON-encoded string. | 

### item\_attachments
<a name="catalog-export-ref-item-attachments"></a>

Contains attachments on items within an iterable form, such as individual columns.


| Column | Type | Description | 
| --- | --- | --- | 
| `asset_id` | string | Identifier of the parent asset. | 
| `iterable_form_name` | string | Name of the iterable form (for example, columns). | 
| `item_name` | string | Name of the item (for example, the column name). | 
| `attachment_name` | string | Attachment name. | 
| `form_type_id` | string | Registered form type of the content. | 
| `content_json` | string | Attachment content as a JSON-encoded string. | 

### glossaries
<a name="catalog-export-ref-glossaries"></a>

Contains one row per glossary.


| Column | Type | Description | 
| --- | --- | --- | 
| `id` | string | Unique glossary identifier. | 
| `description` | string | Glossary description. | 
| `name` | string | Glossary name. | 
| `status` | string | Status (`ENABLED` or `DISABLED`). | 

### glossary\_terms
<a name="catalog-export-ref-glossary-terms"></a>

Contains one row per glossary term.


| Column | Type | Description | 
| --- | --- | --- | 
| `id` | string | Unique term identifier. | 
| `glossary_id` | string | Identifier of the parent glossary. | 
| `long_description` | string | Detailed term description. | 
| `name` | string | Term name. | 
| `short_description` | string | Brief term description. | 
| `status` | string | Status (`ENABLED` or `DISABLED`). | 

### associated\_glossary\_terms
<a name="catalog-export-ref-associated-glossary-terms"></a>

Contains one row per association between a glossary term and an asset.


| Column | Type | Description | 
| --- | --- | --- | 
| `asset_id` | string | Identifier of the asset the glossary term is associated with. | 
| `glossary_term_id` | string | Identifier of the glossary term associated with the asset. Joins to the `glossary_terms` table. | 

## Querying catalog system tables
<a name="catalog-export-querying"></a>

Before you can query catalog metadata exported to S3 Tables using AWS analytics services like or Amazon EMR, you must enable analytics integration on the AWS managed `aws-catalog` table bucket and configure AWS Lake Formation permissions.

### Prerequisites
<a name="catalog-export-querying-prerequisites"></a>
+ Catalog metadata export is enabled and the status is `ENABLED`.
+ Access to or other analytics services.
+ Waited 5 minutes after enabling export for data to be available.

### Integration overview
<a name="catalog-export-querying-integration"></a>

For detailed information about integrating S3 Tables with AWS analytics services, including prerequisites, IAM role configuration, and step-by-step procedures, see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) in the *Amazon Simple Storage Service User Guide*.

After you enable S3 Tables export and set up analytics integration, you can query your Data Catalog metadata using AWS analytics services such as , Amazon Redshift, and Amazon EMR. This enables you to perform metadata audits and analysis using standard SQL.

### Example queries
<a name="catalog-export-querying-examples"></a>

**List all catalog tables with their database and format**  


```
SELECT id, name, database_name, table_format
FROM aws_catalog.glue.tables;
```

**Find columns with descriptions for a specific table**  


```
SELECT column_name, type, description
FROM aws_catalog.glue.table_columns
WHERE asset_id = '{{table-id}}';
```

**Join glossary terms to their parent glossary**  


```
SELECT g.name AS glossary_name,
       t.name AS term_name,
       t.short_description
FROM aws_catalog.catalog_metadata.glossary_terms t
JOIN aws_catalog.catalog_metadata.glossaries g
    ON t.glossary_id = g.id
WHERE g.status = 'ENABLED';
```

**Find tables associated with a specific glossary term**  


```
SELECT t.name, t.database_name, gt.name AS term_name
FROM aws_catalog.glue.tables t
JOIN aws_catalog.catalog_metadata.associated_glossary_terms agt
    ON agt.asset_id = t.id
JOIN aws_catalog.catalog_metadata.glossary_terms gt
    ON gt.id = agt.glossary_term_id
WHERE gt.name = '{{term-name}}';
```

**Extract a field from a custom-form attachment**  


```
SELECT asset_id,
       attachment_name,
       json_extract_scalar(content_json, '$.owner') AS data_owner
FROM aws_catalog.catalog_metadata.attachments
WHERE form_type_id = '{{your-form-type-id}}';
```
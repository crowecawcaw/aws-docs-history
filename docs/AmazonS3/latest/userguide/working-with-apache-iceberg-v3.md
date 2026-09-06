

# Working with Apache Iceberg V3
<a name="working-with-apache-iceberg-v3"></a>

Apache Iceberg Version 3 (V3) is the latest version of the Apache Iceberg table format specification, introducing advanced capabilities for building petabyte-scale data lakes with improved performance and reduced operational overhead. V3 addresses common performance bottlenecks encountered with Version 2 (V2), particularly around batch updates and compliance deletes.

AWS provides support for deletion vectors, row lineage, and the variant data type as defined in the Apache Iceberg Version 3 (V3) specification. You can use these features with Apache Spark on [Amazon EMR](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-emr.html), [AWS Glue ETL](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.html), [Amazon SageMaker Unified Studio Notebooks](https://docs.aws.amazon.com/next-generation-sagemaker/), and Apache Iceberg tables in [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html), including [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/). The variant data type is specific to S3 Tables.

## Key Features in V3
<a name="key-features-v3"></a>

Deletion Vectors  
Replaces V2's positional delete files with an efficient binary format stored as Puffin files. This eliminates write amplification from random batch updates and GDPR compliance deletes, significantly reducing the overhead of maintaining fresh data. Organizations processing high-frequency updates will see immediate improvements in write performance and reduced storage costs from fewer small files.

Row-lineage  
Enables precise change tracking at the row level. Your downstream systems can process changes incrementally, speeding up data pipelines and reducing compute costs for change data capture (CDC) workflows. This built-in capability eliminates the need for custom change tracking implementations.

Variant data type  
With the variant data type, you can write semi-structured data like JSON directly in Iceberg tables without defining a fixed schema in advance. V3 compatible engines shred your semi-structured data into hidden columns as you write it, generating Parquet column statistics that query engines use for optimizations like file pruning. This reduces the data your analytical queries scan. S3 Tables provides ongoing table maintenance for variant columns, including compaction, so you can consolidate data from semi-structured sources into larger files that Iceberg engines can read efficiently.

## Version Compatibility
<a name="version-compatibility"></a>

V3 maintains backward compatibility with V2 tables. AWS services support both V2 and V3 tables simultaneously, allowing you to:
+ Run queries across both V2 and V3 tables
+ Upgrade existing V2 tables to V3 without data rewrites
+ Execute time travel queries that span V2 and V3 snapshots
+ Use schema evolution and hidden partitioning across table versions

**Important**  
V3 is a one-way upgrade. Once a table is upgraded from V2 to V3, it cannot be downgraded back to V2 through standard operations.

## Getting Started with V3
<a name="getting-started-v3"></a>

### Prerequisites
<a name="prerequisites"></a>

Before working with V3 tables, ensure you have:
+ An AWS account with appropriate IAM permissions
+ Access to one or more AWS analytics services (EMR, Glue, Amazon SageMaker Unified Studio Notebooks, or S3 Tables)
+ An S3 bucket for storing table data and metadata
+ A table bucket to get started with S3 Tables or a general purpose S3 bucket if you are building your own Iceberg infrastructure
+ AWS Glue catalog configured

### Creating V3 Tables
<a name="creating-v3-tables"></a>

#### Creating New V3 Tables
<a name="creating-new-v3-tables"></a>

To create a new Iceberg V3 table, set the format-version table property to 3.

**Using Spark SQL:**

```
CREATE TABLE IF NOT EXISTS myns.orders_v3 (  
    order_id bigint,  
    customer_id string,  
    order_date date,  
    total_amount decimal(10,2),  
    status string,  
    created_at timestamp  
)  
USING iceberg  
TBLPROPERTIES (  
    'format-version' = '3'  
)
```

#### Upgrading V2 Tables to V3
<a name="upgrading-v2-to-v3"></a>

You can upgrade existing V2 tables to V3 atomically without rewriting data.

**Using Spark SQL:**

```
ALTER TABLE myns.existing_table  
SET TBLPROPERTIES ('format-version' = '3')
```

**Important**  
V3 is a one-way upgrade. Once a table is upgraded from V2 to V3, it cannot be downgraded back to V2 through standard operations.

**What happens during upgrade:**
+ A new metadata snapshot is created atomically
+ Existing Parquet data files are reused
+ Row-lineage fields are added to the table metadata
+ The next compaction will remove old V2 delete files
+ New modifications will use V3's Deletion Vector files
+ The upgrade does not perform a historical backfill of row-lineage change tracking records

### Enabling Deletion Vectors
<a name="enabling-deletion-vectors"></a>

To take advantage of Deletion Vectors for updates, deletes, and merges, configure your write mode.

**Using Spark SQL:**

```
ALTER TABLE myns.orders_v3  
SET TBLPROPERTIES ('format-version' = '3',  
                   'write.delete.mode' = 'merge-on-read',  
                   'write.update.mode' = 'merge-on-read',  
                   'write.merge.mode' = 'merge-on-read'  
                  )
```

These settings ensure that update, delete, and merge operations create Deletion Vector files instead of rewriting entire data files.

### Leveraging Row-lineage for Change Tracking
<a name="leveraging-row-lineage"></a>

V3 automatically adds row-lineage metadata fields to track changes.

**Using Spark SQL:**

```
# Query with parameter value provided  
last_processed_sequence = 47  
  
SELECT   
    id,  
    data,  
    _row_id,  
    _last_updated_sequence_number  
FROM myns.orders_v3  
WHERE _last_updated_sequence_number > :last_processed_sequence
```

The \_row\_id field uniquely identifies each row, while \_last\_updated\_sequence\_number tracks when the row was last modified. Use these fields to:
+ Identify changed rows for incremental processing
+ Track data lineage for compliance
+ Optimize CDC pipelines
+ Reduce compute costs by processing only changes

### Using the variant data type
<a name="using-variant-data-type"></a>

**Important**  
The variant data type is available only in specific AWS Regions. For the full list of supported Regions, see [Availability](#availability).

With the variant data type, you can write semi-structured data like JSON directly in your Iceberg tables without defining a fixed schema in advance. You can write data faster while still getting efficient analytical query performance. Iceberg V3 compatible engines shred your semi-structured data into hidden columns as you write it. These hidden columns generate Parquet column statistics that query engines use for optimizations like file pruning.

**Creating a table with a variant column using Spark SQL:**

```
CREATE TABLE IF NOT EXISTS myns.events (
    event_id bigint,
    event_timestamp timestamp,
    source string,
    event_data VARIANT
)
USING iceberg
TBLPROPERTIES (
    'format-version' = '3'
)
```

**Inserting semi-structured data into the variant column:**

```
INSERT INTO myns.events VALUES (
    1,
    current_timestamp(),
    'web-app',
    PARSE_JSON('{"user_id": "u-1234", "action": "page_view", "page": "/products", "duration_ms": 350}')
);

INSERT INTO myns.events VALUES (
    2,
    current_timestamp(),
    'mobile-app',
    PARSE_JSON('{"user_id": "u-5678", "action": "purchase", "items": [{"sku": "A100", "qty": 2}], "total": 49.99}')
);
```

With S3 Tables, table maintenance for variant columns, including compaction, runs automatically. Compaction consolidates data from semi-structured sources from small files into larger files that Iceberg engines can read more efficiently, improving query performance over time.

## Best Practices for V3
<a name="best-practices-v3"></a>

### When to Use V3
<a name="when-to-use-v3"></a>

Consider upgrading to or starting with V3 when:
+ You perform frequent batch updates or deletes
+ You need to meet GDPR or compliance delete requirements
+ Your workloads involve high-frequency upserts
+ You require efficient CDC workflows
+ You want to reduce storage costs from small files
+ You need better change tracking capabilities

### Optimizing Write Performance
<a name="optimizing-write-performance"></a>
+ Enable Deletion Vectors for update-heavy workloads:

  ```
  SET TBLPROPERTIES (  
  'write.delete.mode' = 'merge-on-read',  
  'write.update.mode' = 'merge-on-read',  
  'write.merge.mode' = 'merge-on-read'  
  )
  ```
+ Configure appropriate file sizes:

  ```
  SET TBLPROPERTIES (  
  'write.target-file-size-bytes' = '536870912'  — 512 MB  
  )
  ```

### Optimizing Read Performance
<a name="optimizing-read-performance"></a>
+ Leverage row-lineage for incremental processing
+ Use time travel to access historical data without copying
+ Enable statistics collection for better query planning

## Migration Strategy
<a name="migration-strategy"></a>

When migrating from V2 to V3:
+ Test in non-production first - Validate upgrade process and performance
+ Upgrade during low-activity periods - Minimize impact on concurrent operations
+ Monitor initial performance - Track metrics after upgrade
+ Run compaction - Consolidate delete files after upgrade
+ Update documentation - Reflect V3 features in team documentation

## Compatibility Considerations
<a name="compatibility-considerations"></a>
+ Engine versions - Ensure all engines accessing the table support V3
+ Third-party tools - Verify V3 compatibility before upgrading
+ Backup strategy - Test snapshot-based recovery procedures
+ Monitoring - Update monitoring dashboards for V3-specific metrics

### Considerations for compaction
<a name="considerations-for-compaction"></a>

Compaction writes shredded variant Parquet files by default. Older readers that do not support shredding might fail to read compacted files. You can disable shredding by setting the table property `write.variant.shredding.enabled=false`.

## Troubleshooting
<a name="troubleshooting"></a>

### Common Issues
<a name="common-issues"></a>

Error: "format-version 3 is not supported"  
+ Check your query engine catalog for compatibility with Iceberg V3.
+ Ensure that you are using the latest AWS service versions.
+ Verify your engine version supports V3

  V3 support for Amazon AWS services is as follows:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.html)

  \*Partial Region availability

Performance degradation after upgrade  
+ Verify there are no compaction failures. See [Logging and monitoring for S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-monitoring-overview.html) for more details.
+ Check if Deletion Vectors are enabled. Ensure the following properties are set:

  ```
  SET TBLPROPERTIES (  
  'write.delete.mode' = 'merge-on-read',  
  'write.update.mode' = 'merge-on-read',  
  'write.merge.mode' = 'merge-on-read'  
  )
  ```
+ You can verify table properties with the following code:

  ```
  DESCRIBE FORMATTED myns.orders_v3
  ```
+ Review partition strategy. Over partitioning can lead to small files. Run the below query to get the average file size for your table:

  ```
  SELECT avg(file_size_in_bytes) as avg_file_size_bytes   
  FROM myns.orders_v3.files
  ```

Incompatibility with third-party tools  
+ Verify tool supports V3 specification
+ Consider maintaining V2 tables for unsupported tools
+ Contact tool vendor for V3 support timeline

### Getting Help
<a name="getting-help"></a>
+ AWS Support: Contact AWS Support for service-specific issues
+ Apache Iceberg Community: Iceberg Slack
+ AWS Documentation: AWS Analytics Documentation

## Pricing
<a name="pricing"></a>
+ Amazon EMR: [Compute and storage pricing](https://aws.amazon.com/emr/pricing/)
+ [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/)
+ AWS Glue: [Job run and Data Catalog pricing](https://aws.amazon.com/glue/pricing/)
+ S3 Tables: [Storage and request pricing](https://aws.amazon.com/s3/pricing/)

## Availability
<a name="availability"></a>

Apache Iceberg V3 support for deletion vectors and row lineage is available across all AWS Regions where Amazon EMR, AWS Glue Data Catalog, AWS Glue ETL, and S3 Tables operate.

The variant data type in S3 Tables is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and South America (São Paulo).

## Additional Resources
<a name="additional-resources"></a>
+ [Apache Iceberg V3 Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html)
+ [Migration Best Practices](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/)
+ [Getting Started Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html)
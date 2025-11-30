# Working with Apache Iceberg V3

Apache Iceberg Version 3 (V3) is the latest version of the Apache Iceberg table format
specification, introducing advanced capabilities for building petabyte-scale data lakes with
improved performance and reduced operational overhead. V3 addresses common performance
bottlenecks encountered with V2, particularly around batch updates and compliance
deletes.

AWS provides support for deletion vectors and row lineage as defined in the Apache
Iceberg Version 3 (V3) specification. These features are available with Apache Spark on
[Amazon EMR
7.12](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-emr.md "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-emr.md"), [AWS Glue
ETL](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.md "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.md"), [Amazon SageMaker Unified Studio Notebooks](../../../next-generation-sagemaker.md "../../../next-generation-sagemaker.md"), and Apache Iceberg tables in
[AWS Glue
Data Catalog](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md"), including [Amazon S3 Tables](https://aws.amazon.com/s3/features/tables/ "https://aws.amazon.com/s3/features/tables/").

## Key Features in V3

Deletion Vectors

Replaces V2's positional delete files with an efficient binary format
stored as Puffin files. This eliminates write amplification from random
batch updates and GDPR compliance deletes, significantly reducing the
overhead of maintaining fresh data. Organizations processing high-frequency
updates will see immediate improvements in write performance and reduced
storage costs from fewer small files.

Row-lineage

Enables precise change tracking at the row level. Your downstream systems
can process changes incrementally, speeding up data pipelines and reducing
compute costs for change data capture (CDC) workflows. This built-in
capability eliminates the need for custom change tracking
implementations.

## Version Compatibility

V3 maintains backward compatibility with V2 tables. AWS services support both V2 and
V3 tables simultaneously, allowing you to:

- Run queries across both V2 and V3 tables
- Upgrade existing V2 tables to V3 without data rewrites
- Execute time travel queries that span V2 and V3 snapshots
- Use schema evolution and hidden partitioning across table versions

###### Important

V3 is a one-way upgrade. Once a table is upgraded from V2 to V3, it cannot be
downgraded back to V2 through standard operations.

## Getting Started with V3

### Prerequisites

Before working with V3 tables, ensure you have:

- An AWS account with appropriate IAM permissions
- Access to one or more AWS analytics services (EMR, Glue, Amazon
  SageMaker Unified Studio Notebooks, or S3 Tables)
- An S3 bucket for storing table data and metadata
- A table bucket to get started with S3 Tables or a general purpose S3
  bucket if you are building your own Iceberg infrastructure
- AWS Glue catalog configured

### Creating V3 Tables

#### Creating New V3 Tables

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

You can upgrade existing V2 tables to V3 atomically without rewriting
data.

**Using Spark SQL:**

```

ALTER TABLE myns.existing_table
SET TBLPROPERTIES ('format-version' = '3')

```

###### Important

V3 is a one-way upgrade. Once a table is upgraded from V2 to V3, it cannot
be downgraded back to V2 through standard operations.

**What happens during upgrade:**

- A new metadata snapshot is created atomically
- Existing Parquet data files are reused
- Row-lineage fields are added to the table metadata
- The next compaction will remove old V2 delete files
- New modifications will use V3's Deletion Vector files
- The upgrade does not perform a historical backfill of row-lineage
  change tracking records

### Enabling Deletion Vectors

To take advantage of Deletion Vectors for updates, deletes, and merges, configure
your write mode.

**Using Spark SQL:**

```

ALTER TABLE myns.orders_v3
SET TBLPROPERTIES ('format-version' = '3',
                   'write.delete.mode' = 'merge-on-read',
                   'write.update.mode' = 'merge-on-read',
                   'write.merge.mode' = 'merge-on-read'
                  )

```

These settings ensure that update, delete, and merge operations create Deletion
Vector files instead of rewriting entire data files.

### Leveraging Row-lineage for Change Tracking

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

The \_row_id field uniquely identifies each row, while
\_last_updated_sequence_number tracks when the row was last modified. Use these
fields to:

- Identify changed rows for incremental processing
- Track data lineage for compliance
- Optimize CDC pipelines
- Reduce compute costs by processing only changes

## Best Practices for V3

### When to Use V3

Consider upgrading to or starting with V3 when:

- You perform frequent batch updates or deletes
- You need to meet GDPR or compliance delete requirements
- Your workloads involve high-frequency upserts
- You require efficient CDC workflows
- You want to reduce storage costs from small files
- You need better change tracking capabilities

### Optimizing Write Performance

- Enable Deletion Vectors for update-heavy workloads:

```

SET TBLPROPERTIES (
'write.delete.mode' = 'merge-on-read',
'write.update.mode' = 'merge-on-read',
'write.merge.mode' = 'merge-on-read'
)

```

- Configure appropriate file sizes:

```

SET TBLPROPERTIES (
'write.target-file-size-bytes' = '536870912'  — 512 MB
)

```

### Optimizing Read Performance

- Leverage row-lineage for incremental processing
- Use time travel to access historical data without copying
- Enable statistics collection for better query planning

## Migration Strategy

When migrating from V2 to V3:

- Test in non-production first - Validate upgrade process and performance
- Upgrade during low-activity periods - Minimize impact on concurrent
  operations
- Monitor initial performance - Track metrics after upgrade
- Run compaction - Consolidate delete files after upgrade
- Update documentation - Reflect V3 features in team documentation

## Compatibility Considerations

- Engine versions - Ensure all engines accessing the table support V3
- Third-party tools - Verify V3 compatibility before upgrading
- Backup strategy - Test snapshot-based recovery procedures
- Monitoring - Update monitoring dashboards for V3-specific metrics

## Troubleshooting

### Common Issues

Error: "format-version 3 is not supported"

- Verify your engine version supports V3

V3 support for Amazon AWS services is as follows:

| Service                                                  | V3 Support    |
| -------------------------------------------------------- | ------------- |
| EMR Spark                                                | Release 7.12+ |
| AWS Glue ETL                                             | Yes           |
| Amazon SageMaker Unified Studio<br>Notebooks             | Yes           |
| AWS Glue: Iceberg REST API, Table<br>Maintenance         | Yes           |
| Amazon S3 Tables: Iceberg REST API, Table<br>Maintenance | Yes           |
| Amazon Athena (Trino)                                    | No            |

- Check catalog compatibility
- Ensure latest AWS service versions

Performance degradation after upgrade

- Verify there are no compaction failures. See [Logging and monitoring for S3 Tables](s3-tables-monitoring-overview.md "s3-tables-monitoring-overview.md") for more
  details.
- Check if Deletion Vectors are enabled. Ensure the following
  properties are set:

```

SET TBLPROPERTIES (
'write.delete.mode' = 'merge-on-read',
'write.update.mode' = 'merge-on-read',
'write.merge.mode' = 'merge-on-read'
)

```

- You can verify table properties with the following
  code:

```

DESCRIBE FORMATTED myns.orders_v3

```

- Review partition strategy. Over partitioning can lead to small
  files. Run the below query to get the average file size for your
  table:

```

SELECT avg(file_size_in_bytes) as avg_file_size_bytes
FROM myns.orders_v3.files

```

Incompatibility with third-party tools

- Verify tool supports V3 specification
- Consider maintaining V2 tables for unsupported tools
- Contact tool vendor for V3 support timeline

### Getting Help

- AWS Support: Contact AWS Support for service-specific issues
- Apache Iceberg Community: Iceberg Slack
- AWS Documentation: AWS Analytics Documentation

## Pricing

- Amazon EMR: [Compute and storage pricing](https://aws.amazon.com/emr/pricing/ "https://aws.amazon.com/emr/pricing/")
- [Amazon
  SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/")
- AWS Glue: [Job run and Data Catalog pricing](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")
- S3 Tables: [Storage and request pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")

## Availability

Apache Iceberg V3 support is available across all AWS regions where Amazon EMR,
AWS Glue Data Catalog, AWS Glue ETL, and S3 Tables operate.

## Additional Resources

- [Apache Iceberg V3 Documentation](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.md "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.md")
- [Migration Best Practices](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/ "https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/")
- [Getting
  Started Guide](s3-tables-getting-started.md "s3-tables-getting-started.md")

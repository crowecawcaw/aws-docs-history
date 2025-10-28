# Data partitioning

## What is data partitioning?

Data partitioning is a technique that divides large datasets into smaller, more manageable segments called partitions.
In the context of AWS Glue Zero-ETL integrations, partitioning organizes your data in the target location based on specific
column values or transformations of those values.

### Benefits of data partitioning

Effective data partitioning provides several key benefits for analytics workloads:

- **Improved query performance:** Queries can skip irrelevant partitions (partition pruning),
  reducing the amount of data that needs to be scanned.
- **Reduced costs:** By scanning less data, you can lower compute and I/O costs for your analytics queries.
- **Better scalability:** Partitioning allows parallel processing of data segments, enabling more efficient
  scaling of analytics workloads.
- **Simplified data lifecycle management:** You can manage retention policies at the partition level,
  making it easier to archive or delete older data.

### Key partitioning concepts

Partition columns

Columns in your data that are used to determine how records are organized into partitions. Effective partition columns
should align with common query patterns and have appropriate cardinality.

Partition functions

Transformations applied to partition column values to create the actual partition boundaries. Examples include identity
(using the raw value) and time-based functions (year, month, day, hour).

Partition pruning

The process where the query engine identifies and skips partitions that don't contain relevant data for a query,
significantly improving performance.

Partition granularity

The level of detail at which data is partitioned. Finer granularity (more partitions) can improve query performance
but may increase metadata overhead. Coarser granularity (fewer partitions) reduces metadata overhead but may result
in scanning more data than necessary.

### Partitioning in AWS Glue Zero-ETL integrations

AWS Glue Zero-ETL integrations use Apache Iceberg table format, which provides advanced partitioning capabilities. When you create
a Zero-ETL integration, you can:

- Use default partitioning strategies optimized for your data source
- Define custom partitioning specifications tailored to your query patterns
- Apply transformations to partition columns (especially useful for timestamp-based partitioning)
- Combine multiple partition strategies for multi-level partitioning

Partitioning configurations are specified through the `CreateIntegrationTableProperty` API when setting up your
Zero-ETL integration. Once configured, AWS Glue automatically applies these partitioning strategies to organize your data
in the target location.

## Partition specification API reference

Use the following parameters in the CreateIntegrationTableProperties API to configure partitioning:

PartitionSpec

An array of partition specifications that defines how data is partitioned in the target location.

```
{
  "partitionSpec": [
    {
      "fieldName": "timestamp_col",
      "functionSpec": "month",
      "conversionSpec": "epoch_milli"
    },
    {
      "fieldName": "category",
      "functionSpec": "identity"
    }
  ]
}
```

FieldName

A UTF-8 string (1-128 bytes) specifying the column name to use for partitioning.

FunctionSpec

Specifies the partitioning function. Valid values:

- `identity` - Uses source values directly without transformation
- `year` - Extracts the year from timestamp values (e.g., 2023)
- `month` - Extracts the month from timestamp values (e.g., 2023-01)
- `day` - Extracts the day from timestamp values (e.g., 2023-01-15)
- `hour` - Extracts the hour from timestamp values (e.g., 2023-01-15-14)

###### Note

Time-based functions (`year`, `month`, `day`, `hour`) require the `ConversionSpec` parameter to specify the source timestamp format.

ConversionSpec

A UTF-8 string that specifies the timestamp format of the source data. Valid values are:

- `epoch_sec` - Unix epoch timestamp in seconds
- `epoch_milli` - Unix epoch timestamp in milliseconds
- `iso` - ISO 8601 formatted timestamp

## Partitioning strategies

### Default partitioning

When no partition columns are specified, AWS Glue Zero-ETL applies default partitioning strategies optimized for your data source:

- **Primary key-based partitioning:** For sources with primary keys (like DynamoDB tables),
  AWS Glue Zero-ETL automatically partitions data using the primary key with bucketing to prevent partition explosion.

Default partitioning is designed to work well for common query patterns without requiring manual configuration. However,
for specific query patterns or performance requirements, you may want to define custom partitioning strategies.

### User-defined partitioning strategies

AWS Glue Zero-ETL allows you to define custom partitioning strategies using the `PartitionSpec` parameter.
You can specify one or more partition columns and apply different partitioning functions to each column.

**Identity partitioning** uses the raw values from a column to create partitions. This strategy is useful for columns with
low to medium cardinality, such as category, region, or status fields.

###### Example Identity partitioning example

```
{
  "partitionSpec": [
    {
      "fieldName": "category",
      "functionSpec": "identity"
    }
  ]
}
```

This creates separate partitions for each unique value in the "category" column.

###### Warning

Avoid using identity partitioning with high-cardinality columns (like primary keys or timestamps) as it can lead to
partition explosion, which degrades performance and increases metadata overhead.

**Time-based partitioning** organizes data based on timestamp values at different granularities (year, month, day, or hour).
This strategy is ideal for time-series data and enables efficient time-range queries.

When using time-based partitioning, AWS Glue Zero-ETL can automatically convert various timestamp formats to a standardized
format before applying the partition function. This conversion is specified using the `ConversionSpec` parameter.

###### Example Time-based partitioning example

```
{
  "partitionSpec": [
    {
      "fieldName": "created_at",
      "functionSpec": "month",
      "conversionSpec": "epoch_milli"
    }
  ]
}
```

This partitions data by month based on the "created_at" column, which contains Unix epoch timestamps in milliseconds.

AWS Glue Zero-ETL supports the following time-based partition functions:

- **year:** Partitions data by year (e.g., 2023, 2024)
- **month:** Partitions data by month (e.g., 2023-01, 2023-02)
- **day:** Partitions data by day (e.g., 2023-01-01, 2023-01-02)
- **hour:** Partitions data by hour (e.g., 2023-01-01-01, 2023-01-01-02)

AWS Glue Zero-ETL supports the following timestamp formats through the `ConversionSpec` parameter:

- **epoch_sec:** Unix epoch timestamps in seconds
- **epoch_milli:** Unix epoch timestamps in milliseconds
- **iso:** ISO 8601 formatted timestamps

###### Note

The original column values remain unchanged in your source data. AWS Glue only transforms partition column values to
Timestamp Type in the target database table. The transformations only apply to the partitioning process.

**Multi-level partitioning** combines multiple partition strategies to create a hierarchical partitioning scheme.
This is useful for optimizing different types of queries against the same dataset.

###### Example Multi-level partitioning example

```
{
  "partitionSpec": [
    {
      "fieldName": "created_at",
      "functionSpec": "month",
      "conversionSpec": "iso"
    },
    {
      "fieldName": "region",
      "functionSpec": "identity"
    }
  ]
}
```

This creates a two-level partitioning scheme: first by month (from the "created_at" column), then by region.
This enables efficient queries that filter by date ranges, specific regions, or a combination of these dimensions.

When designing multi-level partitioning schemes, consider:

- Placing higher-selectivity columns first in the partition hierarchy
- Balancing partition granularity with the number of partitions
- Aligning the partitioning scheme with your most common query patterns

## Best practices

### Partition column selection

- Do not use high-cardinality columns with the `identity` partition function. Using high-cardinality columns with identity partitioning
  creates many small partitions, which can significantly degrade ingestion performance. High-cardinality columns may include:
  - Primary keys
  - Timestamp fields (such as `LastModifiedTimestamp`, `CreatedDate`)
  - System-generated timestamps

- Do not select multiple timestamp partitions on same column. For example:

```
"partitionSpec": [
      {"fieldName": "col1", "functionSpec": "year", "conversionSpec" : "epoch_milli"},
      {"fieldName": "col1", "functionSpec": "month", "conversionSpec" : "epoch_milli"},
      {"fieldName": "col1", "functionSpec": "day", "conversionSpec" : "epoch_milli"},
      {"fieldName": "col1", "functionSpec": "hour", "conversionSpec" : "epoch_milli"}
]
```

###

Partition FunctionSpec/ConversionSpec selection

- Specify the correct ConversionSpec (epoch_sec | epoch_milli | iso) that represents format of column values chosen for timestamp based
  partitioning when using timestamp-based partition functions. AWS Glue Zero-ETL uses this parameter to correctly transform source data into timestamp
  format before partitioning.
- Use appropriate granularity (year/month/day/hour) based on data volume.
- Consider timezone implications when using ISO timestamps. AWS Glue Zero-ETL populates all the record values of chosen timestamp column with UTC
  timezone.

## Error handling

### NEEDS_ATTENTION State

An integration enters the NEEDS_ATTENTION state when:

- Specified partition columns do not exist in the source
- Timestamp conversion fails for partition columns

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Timestream for InfluxDB as a Target

Amazon Timestream for InfluxDB is a managed time-series database service on AWS that uses open-source InfluxDB APIs for real-time applications. It offers easy setup, operation, and scaling, delivering queries with single-digit millisecond response times.

The first step for determining whether Timestream for InfluxDB is an appropriate migration target for your use-case is determining the cardinality of your Timestream for LiveAnalytics table. We have developed a [script](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md") that calculates table cardinality in Timestream for LiveAnalytics. This calculation serves two purposes:

1. Checks if the cardinality is under 10 million, which will help determine whether Timestream for InfluxDB can handle your use-case.
2. Helps you decide which [Timestream for InfluxDB Instance type](timestream-for-influxdb.md#timestream-for-influx-dbi-classtypes "timestream-for-influxdb.md#timestream-for-influx-dbi-classtypes") to use.
   [Cardinality](https://docs.influxdata.com/influxdb/v2/reference/glossary/#series-cardinality "https://docs.influxdata.com/influxdb/v2/reference/glossary/#series-cardinality") in InfluxDB is the number of unique [measurements](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#measurement "https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#measurement"), [tags](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#tag-set "https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#tag-set"), and [field key](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#field-set "https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#field-set") combinations in an InfluxDB [bucket](https://docs.influxdata.com/influxdb/v2/admin/buckets/ "https://docs.influxdata.com/influxdb/v2/admin/buckets/"). Refer to [Timestream for InfluxDB's documentation on cardinality management](timestream-for-influxdb.md#timestream-for-influx-getting-started-security-best-practices "timestream-for-influxdb.md#timestream-for-influx-getting-started-security-best-practices") to understand how exceeding recommended limits can degrade query performance and increase memory consumption. Benchmark your anticipated query patterns against representative data samples before finalizing your instance selection to ensure your queries remain performant post-migration. Pay attention to memory-intensive aggregation queries that might behave differently than in Timestream for LiveAnalytics. When migrating from Timestream for LiveAnalytics, carefully select your InfluxDB instance specifications based on your dataset's cardinality as this directly impacts performance and resource requirement. We recommend considering other destinations if your data cardinality is more than 10 million.

**Cardinality calculation script overview**

The cardinality calculation script calculates the cardinality of a Timestream for LiveAnalytics table. If the cardinality is under 10 million, the script recommends a Timestream for InfluxDB instance type. Using the default schema mapping, cardinality is calculated by computing the total unique combinations of dimensions and measure name. Choosing the right [line protocol tags](https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#elements-of-line-protocol "https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/#elements-of-line-protocol") (equivalent to dimensions in Timestream for LiveAnalytics) helps you automatically [index](https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/#tag-value "https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/#tag-value") your data and filter your data efficiently using tags. The script also provides the option to exclude specific dimensions when calculating cardinality. If applicable to your case that is, if you are not using certain dimensions for filtering data in SQL queries (specifically not using them as predicates) then you can exclude these dimensions from the cardinality calculation. Later, you can ingest them as fields (equivalent to measures in Timestream for LiveAnalytics) in the next steps of migration.

_Prerequisites and installation_

See the Prerequisites section and installation in the [cardinality script's README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md").

**Basic usage**

To determine the cardinality of a table, example_table, in the database example_database the script can be used in the following way:

###### Example

```
python3 cardinality.py \
    --table-name example_table \
    --database-name example_database
```

This produces the following output:

```
Cardinality of "example_database"."example_table": 160
Your recommended Timestream for InfluxDB type is: db.influx.medium
```

**Recommendations**

The script automatically scans the entire table to calculate cardinality while offering time filter options for optimal query execution. We suggest implementing time filters when your data involves consistent dimensions and when analyzing distinct dimension variations across the entire table yields similar results to analyzing specific time ranges. This approach ensures efficient and performant query execution.

For more information, see the [cardinality script's README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/cardinality/README.md").

# Security Lake queries for AWS source version 1 (OCSF 1.0.0-rc.2)

The following section provides guidance on querying data from Security Lake and includes some query examples for natively-supported AWS sources for AWS source version 1. These
queries are designed to retrieve data in a specific AWS Region. These examples use us-east-1 (US East (N. Virginia)). In addition, the example queries
use a `LIMIT 25` parameter, which returns up to 25 records. You can omit this parameter or adjust it based on your preferences.
For more examples, see the [Amazon Security Lake OCSF Queries GitHub directory](https://github.com/awslabs/aws-security-analytics-bootstrap/tree/main/AWSSecurityAnalyticsBootstrap/amazon_security_lake_queries "https://github.com/awslabs/aws-security-analytics-bootstrap/tree/main/AWSSecurityAnalyticsBootstrap/amazon_security_lake_queries").

The following queries include time-based filters using `eventDay`
to ensure your query is within the configured retention settings.
For more information, see [Querying data with retention settings](subscriber-query-examples.md#security-lake-retention-setting-query-data "subscriber-query-examples.md#security-lake-retention-setting-query-data").

For example,
if data older than 60 days has expired, your queries should include time
constraints to prevent accessing expired data. For a 60-day retention period,
include the following clause in your query:

```
...
WHERE eventDay BETWEEN cast(date_format(current_date - INTERVAL '59' day, '%Y%m%d') AS varchar)
                   AND cast(date_format(current_date, '%Y%m%d') AS varchar)
...
```

This clause uses 59 days (rather than 60) to avoid any data or time
overlap between Amazon S3 and Apache Iceberg.

## Log source table

When you query Security Lake data, you must include the name of the Lake Formation table in which the data resides.

```

SELECT *
   FROM amazon_security_lake_glue_db_`DB_Region`.amazon_security_lake_table_`DB_Region`_`SECURITY_LAKE_TABLE`
   WHERE eventDay BETWEEN cast(date_format(current_timestamp - INTERVAL '7' day, '%Y%m%d%H') as varchar) and cast(date_format(current_timestamp - INTERVAL '0' day, '%Y%m%d%H') as varchar)
   LIMIT `25`

```

Common values for the log source table include the following:

- `cloud_trail_mgmt_1_0` – AWS CloudTrail management events
- `lambda_execution_1_0` – CloudTrail data events for Lambda
- `s3_data_1_0` – CloudTrail data events for S3
- `route53_1_0` – Amazon Route 53 resolver query logs
- `sh_findings_1_0` – AWS Security Hub findings
- `vpc_flow_1_0` – Amazon Virtual Private Cloud (Amazon VPC) Flow Logs

**Example: All Security Hub findings in table `sh_findings_1_0` from us-east-1 Region**

```

SELECT *
   FROM amazon_security_lake_glue_db_`us_east_1`.amazon_security_lake_table_`us_east_1`_`sh_findings_1_0`
   WHERE eventDay BETWEEN cast(date_format(current_timestamp - INTERVAL '7' day, '%Y%m%d%H') as varchar) and cast(date_format(current_timestamp - INTERVAL '0' day, '%Y%m%d%H') as varchar)
   LIMIT `25`

```

## Database Region

When you query Security Lake data, you must include the name of the database Region from which you're querying the data.
For a complete list of database Regions where Security Lake is currently available, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md").

**Example: List AWS CloudTrail activity from source IP**

The following example lists all the CloudTrail activities from the source IP `192.0.2.1` that
were recorded after `20230301` (March 01, 2023),
in the table `cloud_trail_mgmt_1_0` from the `us-east-1`
`DB_Region`.

```

SELECT *
    FROM amazon_security_lake_glue_db_`us_east_1`.amazon_security_lake_table_`us_east_1`_`cloud_trail_mgmt_1_0`
    WHERE eventDay > '`20230301`' AND src_endpoint.ip = '`192.0.2.1`'
    ORDER BY time desc
    LIMIT `25`

```

## Partition date

By partitioning your data, you can restrict the amount of data scanned by each query, thereby improving performance and reducing cost. Security Lake
implements partitioning through `eventDay`, `region`, and `accountid` parameters. `eventDay` partitions use the
format `YYYYMMDD`.

This is an example query using the `eventDay` partition:

```

SELECT *
    FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_1_0
    WHERE eventDay > '`20230301`'
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time desc

```

Common values for `eventDay` include the following:

**Events occurring in the last 1 year**

`> cast(date_format(current_timestamp - INTERVAL '1' year, '%Y%m%d%H') as varchar)`

**Events occurring in the last 1 month**

`> cast(date_format(current_timestamp - INTERVAL '1' month, '%Y%m%d%H') as varchar)`

**Events occurring in the last 30 days**

`> cast(date_format(current_timestamp - INTERVAL '30' day, '%Y%m%d%H') as varchar)`

**Events occurring in the last 12 hours**

`> cast(date_format(current_timestamp - INTERVAL '12' hour, '%Y%m%d%H') as varchar)`

**Events occurring in the last 5 minutes**

`> cast(date_format(current_timestamp - INTERVAL '5' minute, '%Y%m%d%H') as varchar)`

**Events occurring between 7–14 days ago**

`BETWEEN cast(date_format(current_timestamp - INTERVAL '14' day, '%Y%m%d%H') as varchar) and cast(date_format(current_timestamp - INTERVAL '7' day, '%Y%m%d%H') as varchar)`

**Events occurring on or after a specific date**

`>= '20230301'`

**Example: List of all CloudTrail activity from source IP `192.0.2.1` on or after March 1, 2023 in table `cloud_trail_mgmt_1_0`**

```

SELECT *
    FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_1_0
    WHERE eventDay >= '`20230301`'
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time desc
    LIMIT 25

```

**Example: List of all CloudTrail activity from source IP `192.0.2.1` in the last 30 days in table `cloud_trail_mgmt_1_0`**

```

SELECT *
    FROM amazon_security_lake_glue_db_us_east_1.amazon_security_lake_table_us_east_1_cloud_trail_mgmt_1_0
    WHERE eventDay > cast(date_format(current_timestamp - INTERVAL '`30`' day, '%Y%m%d%H') as varchar)
    AND src_endpoint.ip = '192.0.2.1'
    ORDER BY time desc
    LIMIT 25

```

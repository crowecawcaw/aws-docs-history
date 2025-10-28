# Create a table for CloudFront logs in Athena using

manual partitioning with Parquet

###### To create a table for CloudFront standard log file fields using a Parquet format

1. Copy and paste the following example DDL statement into the Query Editor in
   the Athena console. The example statement uses the log file fields documented in
   the [Standard log file fields](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat") section of the _Amazon CloudFront
   Developer Guide_.

This query uses ParquetHiveSerDe with the following SerDe properties to read
Parquet fields correctly in Athena.

```
CREATE EXTERNAL TABLE `cf_logs_manual_partition_parquet`(
  `date` string,
  `time` string,
  `x_edge_location` string,
  `sc_bytes` string,
  `c_ip` string,
  `cs_method` string,
  `cs_host` string,
  `cs_uri_stem` string,
  `sc_status` string,
  `cs_referer` string,
  `cs_user_agent` string,
  `cs_uri_query` string,
  `cs_cookie` string,
  `x_edge_result_type` string,
  `x_edge_request_id` string,
  `x_host_header` string,
  `cs_protocol` string,
  `cs_bytes` string,
  `time_taken` string,
  `x_forwarded_for` string,
  `ssl_protocol` string,
  `ssl_cipher` string,
  `x_edge_response_result_type` string,
  `cs_protocol_version` string,
  `fle_status` string,
  `fle_encrypted_fields` string,
  `c_port` string,
  `time_to_first_byte` string,
  `x_edge_detailed_result_type` string,
  `sc_content_type` string,
  `sc_content_len` string,
  `sc_range_start` string,
  `sc_range_end` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/'
```

2. Run the query in Athena console. After the query completes, Athena registers the
   `cf_logs_manual_partition_parquet` table, making the data in it
   ready for you to issue queries.

## Example queries

The following query adds up the number of bytes served by CloudFront for January 19, 2025.

```
SELECT sum(cast("sc_bytes" as BIGINT)) as sc
FROM cf_logs_manual_partition_parquet
WHERE "date"='2025-01-19'
```

To eliminate duplicate rows (for example, duplicate empty rows) from the query
results, you can use the `SELECT DISTINCT` statement, as in the following
example.

```
SELECT DISTINCT * FROM cf_logs_manual_partition_parquet
```

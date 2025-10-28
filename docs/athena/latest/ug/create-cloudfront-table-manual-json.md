# Create a table for CloudFront logs in Athena using

manual partitioning with JSON

###### To create a table for CloudFront standard log file fields using a JSON format

1. Copy and paste the following example DDL statement into the Query Editor in
   the Athena console. The example statement uses the log file fields documented in
   the [Standard log file fields](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat") section of the _Amazon CloudFront
   Developer Guide_. Modify the `LOCATION` for the Amazon S3
   bucket that stores your logs.

This query uses OpenX JSON SerDe with the following SerDe properties to read JSON fields correctly in Athena.

```
CREATE EXTERNAL TABLE `cf_logs_manual_partition_json`(
  `date` string ,
  `time` string ,
  `x-edge-location` string ,
  `sc-bytes` string ,
  `c-ip` string ,
  `cs-method` string ,
  `cs(host)` string ,
  `cs-uri-stem` string ,
  `sc-status` string ,
  `cs(referer)` string ,
  `cs(user-agent)` string ,
  `cs-uri-query` string ,
  `cs(cookie)` string ,
  `x-edge-result-type` string ,
  `x-edge-request-id` string ,
  `x-host-header` string ,
  `cs-protocol` string ,
  `cs-bytes` string ,
  `time-taken` string ,
  `x-forwarded-for` string ,
  `ssl-protocol` string ,
  `ssl-cipher` string ,
  `x-edge-response-result-type` string ,
  `cs-protocol-version` string ,
  `fle-status` string ,
  `fle-encrypted-fields` string ,
  `c-port` string ,
  `time-to-first-byte` string ,
  `x-edge-detailed-result-type` string ,
  `sc-content-type` string ,
  `sc-content-len` string ,
  `sc-range-start` string ,
  `sc-range-end` string )
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'paths'='c-ip,c-port,cs(Cookie),cs(Host),cs(Referer),cs(User-Agent),cs-bytes,cs-method,cs-protocol,cs-protocol-version,cs-uri-query,cs-uri-stem,date,fle-encrypted-fields,fle-status,sc-bytes,sc-content-len,sc-content-type,sc-range-end,sc-range-start,sc-status,ssl-cipher,ssl-protocol,time,time-taken,time-to-first-byte,x-edge-detailed-result-type,x-edge-location,x-edge-request-id,x-edge-response-result-type,x-edge-result-type,x-forwarded-for,x-host-header')
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/'
```

2. Run the query in Athena console. After the query completes, Athena registers the
   `cf_logs_manual_partition_json` table, making the data in it ready for
   you to issue queries.

## Example queries

The following query adds up the number of bytes served by CloudFront for January 15, 2025.

```
SELECT sum(cast("sc-bytes" as BIGINT)) as sc
FROM cf_logs_manual_partition_json
WHERE "date"='2025-01-15'
```

To eliminate duplicate rows (for example, duplicate empty rows) from the query
results, you can use the `SELECT DISTINCT` statement, as in the following
example.

```
SELECT DISTINCT * FROM cf_logs_manual_partition_json
```

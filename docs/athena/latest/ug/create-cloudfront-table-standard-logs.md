# Create a table for CloudFront standard logs (legacy)

###### Note

The following procedure works for the Web distribution access logs in CloudFront. It
does not apply to streaming logs from RTMP distributions.

###### To create a table for CloudFront standard log file fields

1. Copy and paste the following example DDL statement into the Query Editor in
   the Athena console. The example statement uses the log file fields documented in
   the [Standard log file fields](../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/AccessLogs.md#BasicDistributionFileFormat") section of the _Amazon CloudFront
   Developer Guide_. Modify the `LOCATION` for the Amazon S3
   bucket that stores your logs. For information about using the Query Editor, see
   [Get started](getting-started.md "getting-started.md").

This query specifies `ROW FORMAT DELIMITED` and `FIELDS
 TERMINATED BY '\t'` to indicate that the fields are delimited by tab
characters. For `ROW FORMAT DELIMITED`, Athena uses the [LazySimpleSerDe](lazy-simple-serde.md "lazy-simple-serde.md") by default. The column
`date` is escaped using backticks (`) because it is a reserved
word in Athena. For information, see [Escape reserved keywords in queries](reserved-words.md "reserved-words.md").

```
CREATE EXTERNAL TABLE IF NOT EXISTS cloudfront_standard_logs (
  `date` DATE,
  time STRING,
  x_edge_location STRING,
  sc_bytes BIGINT,
  c_ip STRING,
  cs_method STRING,
  cs_host STRING,
  cs_uri_stem STRING,
  sc_status INT,
  cs_referrer STRING,
  cs_user_agent STRING,
  cs_uri_query STRING,
  cs_cookie STRING,
  x_edge_result_type STRING,
  x_edge_request_id STRING,
  x_host_header STRING,
  cs_protocol STRING,
  cs_bytes BIGINT,
  time_taken FLOAT,
  x_forwarded_for STRING,
  ssl_protocol STRING,
  ssl_cipher STRING,
  x_edge_response_result_type STRING,
  cs_protocol_version STRING,
  fle_status STRING,
  fle_encrypted_fields INT,
  c_port INT,
  time_to_first_byte FLOAT,
  x_edge_detailed_result_type STRING,
  sc_content_type STRING,
  sc_content_len BIGINT,
  sc_range_start BIGINT,
  sc_range_end BIGINT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LOCATION 's3://amzn-s3-demo-bucket/'
TBLPROPERTIES ( 'skip.header.line.count'='2' )

```

2. Run the query in Athena console. After the query completes, Athena registers the
   `cloudfront_standard_logs` table, making the data in it ready for
   you to issue queries.

## Example queries

The following query adds up the number of bytes served by CloudFront between June 9 and
June 11, 2018. Surround the date column name with double quotes because it is a
reserved word.

```
SELECT SUM(bytes) AS total_bytes
FROM cloudfront_standard_logs
WHERE "date" BETWEEN DATE '2018-06-09' AND DATE '2018-06-11'
LIMIT 100;
```

To eliminate duplicate rows (for example, duplicate empty rows) from the query
results, you can use the `SELECT DISTINCT` statement, as in the following
example.

```
SELECT DISTINCT *
FROM cloudfront_standard_logs
LIMIT 10;
```

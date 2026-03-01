# Create a table for CloudFront real-time logs

###### To create a table for CloudFront real-time log file fields

1. Copy and paste the following example DDL statement into the Query Editor in
   the Athena console. The example statement uses the log file fields documented in
   the [Real-time
   logs](../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md "../../../AmazonCloudFront/latest/DeveloperGuide/real-time-logs.md") section of the _Amazon CloudFront Developer
   Guide_. Modify the `LOCATION` for the Amazon S3 bucket that
   stores your logs. For information about using the Query Editor, see [Get started](getting-started.md "getting-started.md").

This query specifies `ROW FORMAT DELIMITED` and `FIELDS
 TERMINATED BY '\t'` to indicate that the fields are delimited by tab
characters. For `ROW FORMAT DELIMITED`, Athena uses the [LazySimpleSerDe](lazy-simple-serde.md "lazy-simple-serde.md") by default. The column
`timestamp` is escaped using backticks (`) because it is a
reserved word in Athena. For information, see [Escape reserved keywords in queries](reserved-words.md "reserved-words.md").

The follow example contains all of the available fields. You can comment out
or remove fields that you do not require.

```
CREATE EXTERNAL TABLE IF NOT EXISTS cloudfront_real_time_logs (
`timestamp` STRING,
c_ip STRING,
time_to_first_byte BIGINT,
sc_status BIGINT,
sc_bytes BIGINT,
cs_method STRING,
cs_protocol STRING,
cs_host STRING,
cs_uri_stem STRING,
cs_bytes BIGINT,
x_edge_location STRING,
x_edge_request_id STRING,
x_host_header STRING,
time_taken BIGINT,
cs_protocol_version STRING,
c_ip_version STRING,
cs_user_agent STRING,
cs_referer STRING,
cs_cookie STRING,
cs_uri_query STRING,
x_edge_response_result_type STRING,
x_forwarded_for STRING,
ssl_protocol STRING,
ssl_cipher STRING,
x_edge_result_type STRING,
fle_encrypted_fields STRING,
fle_status STRING,
sc_content_type STRING,
sc_content_len BIGINT,
sc_range_start STRING,
sc_range_end STRING,
c_port BIGINT,
x_edge_detailed_result_type STRING,
c_country STRING,
cs_accept_encoding STRING,
cs_accept STRING,
cache_behavior_path_pattern STRING,
cs_headers STRING,
cs_header_names STRING,
cs_headers_count BIGINT,
primary_distribution_id STRING,
primary_distribution_dns_name STRING,
origin_fbl STRING,
origin_lbl STRING,
asn STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LOCATION 's3://amzn-s3-demo-bucket/'
TBLPROPERTIES ( 'skip.header.line.count'='2' )

```

2. Run the query in Athena console. After the query completes, Athena registers the
   `cloudfront_real_time_logs` table, making the data in it ready
   for you to issue queries.

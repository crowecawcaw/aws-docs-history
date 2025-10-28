# Create a table for CloudFront logs in Athena using

partition projection with Parquet

The following example CREATE TABLE statement automatically uses partition projection
on CloudFront logs in Parquet, from a specified CloudFront distribution until present for a single
AWS Region. After you run the query successfully, you can query the table.

```
CREATE EXTERNAL TABLE ``cloudfront_logs_parquet_pp``(
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
PARTITIONED BY(
 distributionid string,
 year int,
 month int,
 day int,
 hour int )
ROW FORMAT SERDE
'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
's3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/CloudFront/'
TBLPROPERTIES (
'projection.distributionid.type'='enum',
'projection.distributionid.values'='E3OK0LPUNWWO3',
'projection.day.range'='01,31',
'projection.day.type'='integer',
'projection.day.digits'='2',
'projection.enabled'='true',
'projection.month.range'='01,12',
'projection.month.type'='integer',
'projection.month.digits'='2',
'projection.year.range'='2019,2025',
'projection.year.type'='integer',
'projection.hour.range'='01,12',
'projection.hour.type'='integer',
'projection.hour.digits'='2',
'storage.location.template'='s3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/CloudFront/${distributionid}/${year}/${month}/${day}/${hour}/')

```

Following are some considerations for the properties used in the previous
example.

- **Table name** – The table name
  `cloudfront_logs_pp` is
  replaceable. You can change it to any name that you prefer.
- **Location** – Modify
  `s3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/`
  to point to your Amazon S3 bucket.
- **Distribution IDs** – For
  `projection.distributionid.values`, you can specify multiple
  distribution IDs if you separate them with commas. For example,
  `<distributionID1>`,
  `<distributionID2>`.
- **Year range** – In `projection.year.range`,
  you can define the range of years based on your data. For example, you can
  adjust it to any period, such as _2025_,
  _2026_.

###### Note

Including empty partitions, such as those for future dates (example: 2025-2040), can impact query performance. However, partition projection is designed to effectively handle future dates. To maintain optimal performance, ensure that partitions are managed thoughtfully and avoid excessive empty partitions when possible.

- **Storage location template** – You must ensure to update
  the `storage.location.template` correctly based on the following CloudFront
  partitioning structure and S3 path.

| Parameter                         | Pattern                                                                                                        |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CloudFront partitioning structure | `AWSLogs/{`AWS_ACCOUNT_ID`}/CloudFront/{`DistributionId`}/folder2/{yyyy}/{MM}/{dd}/{HH}/folder3`               |
| S3 path                           | `s3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/CloudFront/E2Oxxxxxxxxxxx/folder2/2025/01/25/03/folder3/` | After you confirm that the CloudFront partitioning structure and S3 structure match the required patterns, update the `storage.location.template` as follows: ``'storage.location.template'='s3://`amzn-s3-demo-bucket`/AWSLogs/`account_id`/CloudFront/${`distributionid`}/folder2/${year}/${month}/${day}/${hour}/folder3/'`` ###### Note Proper configuration of the `storage.location.template` is crucial for ensuring correct data storage and retrieval. |

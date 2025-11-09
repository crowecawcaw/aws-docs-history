# Create a table for CloudFront logs in Athena using

partition projection with JSON

You can reduce query runtime and automate partition management with Athena partition
projection feature. Partition projection automatically adds new partitions as new data
is added. This removes the need for you to manually add partitions by using `ALTER
 TABLE ADD PARTITION`.

The following example CREATE TABLE statement automatically uses partition projection
on CloudFront logs from a specified CloudFront distribution until present for a single AWS Region.
After you run the query successfully, you can query the table.

```
CREATE EXTERNAL TABLE ``cloudfront_logs_pp``(
  `date` string,
  `time` string,
  `x-edge-location` string,
  `sc-bytes` string,
  `c-ip` string,
  `cs-method` string,
  `cs(host)` string,
  `cs-uri-stem` string,
  `sc-status` string,
  `cs(referer)` string,
  `cs(user-agent)` string,
  `cs-uri-query` string,
  `cs(cookie)` string,
  `x-edge-result-type` string,
  `x-edge-request-id` string,
  `x-host-header` string,
  `cs-protocol` string,
  `cs-bytes` string,
  `time-taken` string,
  `x-forwarded-for` string,
  `ssl-protocol` string,
  `ssl-cipher` string,
  `x-edge-response-result-type` string,
  `cs-protocol-version` string,
  `fle-status` string,
  `fle-encrypted-fields` string,
  `c-port` string,
  `time-to-first-byte` string,
  `x-edge-detailed-result-type` string,
  `sc-content-type` string,
  `sc-content-len` string,
  `sc-range-start` string,
  `sc-range-end` string)
  PARTITIONED BY(
         distributionid string,
         year int,
         month int,
         day int,
         hour int )
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'paths'='c-ip,c-port,cs(Cookie),cs(Host),cs(Referer),cs(User-Agent),cs-bytes,cs-method,cs-protocol,cs-protocol-version,cs-uri-query,cs-uri-stem,date,fle-encrypted-fields,fle-status,sc-bytes,sc-content-len,sc-content-type,sc-range-end,sc-range-start,sc-status,ssl-cipher,ssl-protocol,time,time-taken,time-to-first-byte,x-edge-detailed-result-type,x-edge-location,x-edge-request-id,x-edge-response-result-type,x-edge-result-type,x-forwarded-for,x-host-header')
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/CloudFront/'
TBLPROPERTIES (
  'projection.distributionid.type'='enum',
  'projection.distributionid.values'='E2Oxxxxxxxxxxx',
  'projection.day.range'='01,31',
  'projection.day.type'='integer',
  'projection.day.digits'='2',
  'projection.enabled'='true',
  'projection.month.range'='01,12',
  'projection.month.type'='integer',
  'projection.month.digits'='2',
  'projection.year.range'='2025,2026',
  'projection.year.type'='integer',
  'projection.hour.range'='00,23',
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
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| CloudFront partitioning structure | `AWSLogs/{`AWS_ACCOUNT_ID`}/CloudFront/{`DistributionId`}/folder2/{yyyy}/{MM}/{dd}/{HH}/folder3`               |
| S3 path                           | `s3://`amzn-s3-demo-bucket`/AWSLogs/`AWS_ACCOUNT_ID`/CloudFront/E2Oxxxxxxxxxxx/folder2/2025/01/25/03/folder3/` |

After you confirm that the CloudFront partitioning structure and S3 structure match
the required patterns, update the `storage.location.template` as
follows:

```
'storage.location.template'='s3://`amzn-s3-demo-bucket`/AWSLogs/`account_id`/CloudFront/${`distributionid`}/folder2/${year}/${month}/${day}/${hour}/folder3/'
```

###### Note

Proper configuration of the `storage.location.template` is
crucial for ensuring correct data storage and retrieval.

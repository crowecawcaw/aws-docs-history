# Create tables for flow logs in Apache Parquet format

The following procedure creates an Amazon VPC table for Amazon VPC flow logs in Apache Parquet
format.

###### To create an Athena table for Amazon VPC flow logs in Parquet format

1. Enter a DDL statement like the following into the Athena console query editor,
   following the guidelines in the [Considerations and limitations](vpc-flow-logs.md#vpc-flow-logs-common-considerations "vpc-flow-logs.md#vpc-flow-logs-common-considerations") section. The sample
   statement creates a table that has the columns for Amazon VPC flow logs versions 2
   through 5 as documented in [Flow log records](../../../vpc/latest/userguide/flow-logs.md#flow-log-records "../../../vpc/latest/userguide/flow-logs.md#flow-log-records")
   in Parquet format, Hive partitioned hourly. If you do not have hourly
   partitions, remove `hour` from the `PARTITIONED BY`
   clause.

```
CREATE EXTERNAL TABLE IF NOT EXISTS vpc_flow_logs_parquet (
  version int,
  account_id string,
  interface_id string,
  srcaddr string,
  dstaddr string,
  srcport int,
  dstport int,
  protocol bigint,
  packets bigint,
  bytes bigint,
  start bigint,
  `end` bigint,
  action string,
  log_status string,
  vpc_id string,
  subnet_id string,
  instance_id string,
  tcp_flags int,
  type string,
  pkt_srcaddr string,
  pkt_dstaddr string,
  region string,
  az_id string,
  sublocation_type string,
  sublocation_id string,
  pkt_src_aws_service string,
  pkt_dst_aws_service string,
  flow_direction string,
  traffic_path int
)
PARTITIONED BY (
  `aws-account-id` string,
  `aws-service` string,
  `aws-region` string,
  `year` string,
  `month` string,
  `day` string,
  `hour` string
)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`prefix`/AWSLogs/'
TBLPROPERTIES (
  'EXTERNAL'='true',
  'skip.header.line.count'='1'
  )
```

2. Modify the sample `LOCATION
's3://amzn-s3-demo-bucket/`prefix`/AWSLogs/'`
   to point to the Amazon S3 path that contains your log data.
3. Run the query in Athena console.
4. If your data is in Hive-compatible format, run the following command in the
   Athena console to update and load the Hive partitions in the metastore. After the
   query completes, you can query the data in the
   `vpc_flow_logs_parquet` table.

```
MSCK REPAIR TABLE vpc_flow_logs_parquet
```

If you are not using Hive compatible data, run [ALTER TABLE ADD PARTITION](alter-table-add-partition.md "alter-table-add-partition.md") to load the partitions.
For more information about using Athena to query Amazon VPC flow logs in Parquet format, see
the post [Optimize performance and reduce costs for network analytics with VPC Flow Logs in
Apache Parquet format](https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/ "https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/") in the _AWS Big Data
Blog_.

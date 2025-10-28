# Copy on write (CoW)

create table examples

If you have Hudi tables already created in AWS Glue, you can query them directly in
Athena. When you create partitioned Hudi tables in Athena, you must run `ALTER TABLE
 ADD PARTITION` to load the Hudi data before you can query it.

## Nonpartitioned CoW

table

The following example creates a nonpartitioned CoW table in Athena.

```
CREATE EXTERNAL TABLE `non_partition_cow`(
  `_hoodie_commit_time` string,
  `_hoodie_commit_seqno` string,
  `_hoodie_record_key` string,
  `_hoodie_partition_path` string,
  `_hoodie_file_name` string,
  `event_id` string,
  `event_time` string,
  `event_name` string,
  `event_guests` int,
  `event_type` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hudi.hadoop.HoodieParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`folder`/non_partition_cow/'
```

## Partitioned CoW table

The following example creates a partitioned CoW table in Athena.

```
CREATE EXTERNAL TABLE `partition_cow`(
  `_hoodie_commit_time` string,
  `_hoodie_commit_seqno` string,
  `_hoodie_record_key` string,
  `_hoodie_partition_path` string,
  `_hoodie_file_name` string,
  `event_id` string,
  `event_time` string,
  `event_name` string,
  `event_guests` int)
PARTITIONED BY (
  `event_type` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hudi.hadoop.HoodieParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`folder`/partition_cow/'
```

The following `ALTER TABLE ADD PARTITION` example adds two partitions
to the example `partition_cow` table.

```
ALTER TABLE partition_cow ADD
  PARTITION (event_type = 'one') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_cow/one/'
  PARTITION (event_type = 'two') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_cow/two/'
```

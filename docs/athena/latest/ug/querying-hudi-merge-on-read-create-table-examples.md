# Merge on read (MoR) create table examples

Hudi creates two tables in the metastore for MoR: a table for snapshot queries, and a
table for read optimized queries. Both tables are queryable. In Hudi versions prior to
0.5.1, the table for read optimized queries had the name that you specified when you
created the table. Starting in Hudi version 0.5.1, the table name is suffixed with
`_ro` by default. The name of the table for snapshot queries is the name
that you specified appended with `_rt`.

## Nonpartitioned merge on read (MoR) table

The following example creates a nonpartitioned MoR table in Athena for read
optimized queries. Note that read optimized queries use the input format
`HoodieParquetInputFormat`.

```
CREATE EXTERNAL TABLE `nonpartition_mor`(
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
  'org.apache.hudi.hadoop.**HoodieParquetInputFormat**'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`folder`/nonpartition_mor/'
```

The following example creates a nonpartitioned MoR table in Athena for snapshot
queries. For snapshot queries, use the input format
`HoodieParquetRealtimeInputFormat`.

```
CREATE EXTERNAL TABLE `nonpartition_mor_rt`(
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
  'org.apache.hudi.hadoop.realtime.**HoodieParquetRealtimeInputFormat**'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`folder`/nonpartition_mor/'
```

## Partitioned merge on read (MoR) table

The following example creates a partitioned MoR table in Athena for read optimized
queries.

```
CREATE EXTERNAL TABLE `partition_mor`(
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
  's3://amzn-s3-demo-bucket/`folder`/partition_mor/'
```

The following `ALTER TABLE ADD PARTITION` example adds two partitions
to the example `partition_mor` table.

```
ALTER TABLE partition_mor ADD
  PARTITION (event_type = 'one') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_mor/one/'
  PARTITION (event_type = 'two') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_mor/two/'
```

The following example creates a partitioned MoR table in Athena for snapshot
queries.

```
CREATE EXTERNAL TABLE `partition_mor_rt`(
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
  'org.apache.hudi.hadoop.realtime.HoodieParquetRealtimeInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/`folder`/partition_mor/'
```

Similarly, the following `ALTER TABLE ADD PARTITION` example adds two
partitions to the example `partition_mor_rt` table.

```
ALTER TABLE partition_mor_rt ADD
  PARTITION (event_type = 'one') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_mor/one/'
  PARTITION (event_type = 'two') LOCATION 's3://amzn-s3-demo-bucket/`folder`/partition_mor/two/'
```

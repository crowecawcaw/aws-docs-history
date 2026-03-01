# Create and query a partitioned table based on Amazon EMR logs

These examples use the same log location to create an Athena table, but the table is
partitioned, and a partition is then created for each log location. For more
information, see [Partition your data](partitions.md "partitions.md").

The following query creates the partitioned table named
`mypartitionedemrlogs`:

```
CREATE EXTERNAL TABLE ``mypartitionedemrlogs``(
  `data` string COMMENT 'from deserializer')
 partitioned by (logtype string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`'
```

The following query statements then create table partitions based on sub-directories
for different log types that Amazon EMR creates in Amazon S3:

```
ALTER TABLE mypartitionedemrlogs ADD
     PARTITION (logtype='containers')
     LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`/containers/'
```

```
ALTER TABLE mypartitionedemrlogs ADD
     PARTITION (logtype='hadoop-mapreduce')
     LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`/hadoop-mapreduce/'
```

```
ALTER TABLE mypartitionedemrlogs ADD
     PARTITION (logtype='hadoop-state-pusher')
     LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`/hadoop-state-pusher/'
```

```
ALTER TABLE mypartitionedemrlogs ADD
     PARTITION (logtype='node')
     LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`/node/'
```

```
ALTER TABLE mypartitionedemrlogs ADD
     PARTITION (logtype='steps')
     LOCATION 's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`/steps/'
```

After you create the partitions, you can run a `SHOW PARTITIONS` query on
the table to confirm:

```
SHOW PARTITIONS mypartitionedemrlogs;
```

## Example queries

The following examples demonstrate queries for specific log entries use the table and
partitions created by the examples above.

###### Example– Querying application application_1561661818238_0002 logs in the containers partition for ERROR or WARN

```
SELECT data,
        "$PATH"
FROM "default"."mypartitionedemrlogs"
WHERE logtype='containers'
        AND regexp_like("$PATH",'application_1561661818238_0002')
        AND regexp_like(data, 'ERROR|WARN') limit 100;
```

###### Example– Querying the hadoop-Mapreduce partition for job job_1561661818238_0004 and failed reduces

```
SELECT data,
        "$PATH"
FROM "default"."mypartitionedemrlogs"
WHERE logtype='hadoop-mapreduce'
        AND regexp_like(data,'job_1561661818238_0004|Failed Reduces') limit 100;
```

###### Example– Querying Hive logs in the node partition for query ID 056e0609-33e1-4611-956c-7a31b42d2663

```
SELECT data,
        "$PATH"
FROM "default"."mypartitionedemrlogs"
WHERE logtype='node'
        AND regexp_like("$PATH",'hive')
        AND regexp_like(data,'056e0609-33e1-4611-956c-7a31b42d2663') limit 100;
```

###### Example– Querying resourcemanager logs in the node partition for application 1567660019320_0001_01_000001

```
SELECT data,
        "$PATH"
FROM "default"."mypartitionedemrlogs"
WHERE logtype='node'
        AND regexp_like(data,'resourcemanager')
        AND regexp_like(data,'1567660019320_0001_01_000001') limit 100
```

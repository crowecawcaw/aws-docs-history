# Create and query a basic table based on Amazon EMR log

files

The following example creates a basic table, `myemrlogs`, based on log
files saved to
`s3://aws-logs-`123456789012`-`us-west-2`/elasticmapreduce/`j-2ABCDE34F5GH6`/elasticmapreduce/`.
The Amazon S3 location used in the examples below reflects the pattern of the default log
location for an EMR cluster created by Amazon Web Services account
`123456789012` in Region
`us-west-2`. If you use a custom location, the pattern is
s3://amzn-s3-demo-bucket/`ClusterID`.

For information about creating a partitioned table to potentially improve query
performance and reduce data transfer, see [Create and query a partitioned table
based on Amazon EMR logs](emr-create-table-partitioned.md "emr-create-table-partitioned.md").

```
CREATE EXTERNAL TABLE ``myemrlogs``(
  `data` string COMMENT 'from deserializer')
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://aws-logs-`123456789012`-us-west-2/elasticmapreduce/`j-2ABCDE34F5GH6`'
```

## Example queries

The following example queries can be run on the `myemrlogs` table created
by the previous example.

###### Example – Query step logs for occurrences of ERROR, WARN, INFO, EXCEPTION, FATAL,

or DEBUG

```
SELECT data,
        "$PATH"
FROM "default"."myemrlogs"
WHERE regexp_like("$PATH",'s-86URH188Z6B1')
        AND regexp_like(data, 'ERROR|WARN|INFO|EXCEPTION|FATAL|DEBUG') limit 100;
```

###### Example – Query a specific instance log, i-00b3c0a839ece0a9c, for ERROR, WARN,

INFO, EXCEPTION, FATAL, or DEBUG

```
SELECT "data",
        "$PATH" AS filepath
FROM "default"."myemrlogs"
WHERE regexp_like("$PATH",'i-00b3c0a839ece0a9c')
        AND regexp_like("$PATH",'state')
        AND regexp_like(data, 'ERROR|WARN|INFO|EXCEPTION|FATAL|DEBUG') limit 100;
```

###### Example – Query presto application logs for ERROR, WARN, INFO, EXCEPTION, FATAL,

or DEBUG

```
SELECT "data",
        "$PATH" AS filepath
FROM "default"."myemrlogs"
WHERE regexp_like("$PATH",'presto')
        AND regexp_like(data, 'ERROR|WARN|INFO|EXCEPTION|FATAL|DEBUG') limit 100;
```

###### Example – Query Namenode application logs for ERROR, WARN, INFO, EXCEPTION,

FATAL, or DEBUG

```
SELECT "data",
        "$PATH" AS filepath
FROM "default"."myemrlogs"
WHERE regexp_like("$PATH",'namenode')
        AND regexp_like(data, 'ERROR|WARN|INFO|EXCEPTION|FATAL|DEBUG') limit 100;
```

###### Example – Query all logs by date and hour for ERROR, WARN, INFO, EXCEPTION,

FATAL, or DEBUG

```
SELECT distinct("$PATH") AS filepath
FROM "default"."myemrlogs"
WHERE regexp_like("$PATH",'2019-07-23-10')
        AND regexp_like(data, 'ERROR|WARN|INFO|EXCEPTION|FATAL|DEBUG') limit 100;
```

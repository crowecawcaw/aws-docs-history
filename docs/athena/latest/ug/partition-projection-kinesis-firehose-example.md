# Amazon Data Firehose example

When you use Firehose to deliver data to Amazon S3, the default configuration writes objects with
keys that look like the following example:

```
s3://amzn-s3-demo-bucket/prefix/yyyy/MM/dd/HH/file.extension
```

To create an Athena table that finds the partitions automatically at query time, instead of
having to add them to the AWS Glue Data Catalog as new data arrives, you can use partition
projection.

The following `CREATE TABLE` example uses the default Firehose
configuration.

```

CREATE EXTERNAL TABLE my_ingested_data (
 ...
)
...
PARTITIONED BY (
 datehour STRING
)
LOCATION "s3://amzn-s3-demo-bucket/`prefix`/"
TBLPROPERTIES (
 "projection.enabled" = "true",
 "projection.datehour.type" = "date",
 "projection.datehour.format" = "yyyy/MM/dd/HH",
 "projection.datehour.range" = "2021/01/01/00,NOW",
 "projection.datehour.interval" = "1",
 "projection.datehour.interval.unit" = "HOURS",
 "storage.location.template" = "s3://amzn-s3-demo-bucket/`prefix`/${datehour}/"
)
```

The `TBLPROPERTIES` clause in the `CREATE TABLE` statement tells
Athena the following:

- Use partition projection when querying the table
- The partition key `datehour` is of type `date` (which
  includes an optional time)
- How the dates are formatted
- The range of date times. Note that the values must be separated by a comma, not a
  hyphen.
- Where to find the data on Amazon S3.
  When you query the table, Athena calculates the values for `datehour` and uses
  the storage location template to generate a list of partition locations.

###### Topics

- [How
  to use the date type](partition-projection-kinesis-firehose-example-using-the-date-type.md "partition-projection-kinesis-firehose-example-using-the-date-type.md")
- [How to choose partition keys](partition-projection-kinesis-firehose-example-choosing-partition-keys.md "partition-projection-kinesis-firehose-example-choosing-partition-keys.md")
- [How to use custom prefixes and dynamic partitioning](partition-projection-kinesis-firehose-example-using-custom-prefixes-and-dynamic-partitioning.md "partition-projection-kinesis-firehose-example-using-custom-prefixes-and-dynamic-partitioning.md")

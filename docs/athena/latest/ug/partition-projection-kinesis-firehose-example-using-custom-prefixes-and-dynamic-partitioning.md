# How to use custom prefixes and dynamic partitioning

Firehose can be configured with [custom prefixes](../../../firehose/latest/dev/s3-prefixes.md "../../../firehose/latest/dev/s3-prefixes.md") and [dynamic
partitioning](../../../firehose/latest/dev/dynamic-partitioning.md "../../../firehose/latest/dev/dynamic-partitioning.md"). Using these features, you can configure the Amazon S3 keys and set
up partitioning schemes that better support your use case. You can also use partition
projection with these partitioning schemes and configure them accordingly.

For example, you could use the custom prefix feature to get Amazon S3 keys that have ISO
formatted dates instead of the default `yyyy/MM/dd/HH` scheme.

You can also combine custom prefixes with dynamic partitioning to extract a property
like `customer_id` from Firehose messages, as in the following example.

```
prefix/!{timestamp:yyyy}-!{timestamp:MM}-!{timestamp:dd}/!{partitionKeyFromQuery:customer_id}/
```

With that Amazon S3 prefix, the Firehose delivery stream would write objects to keys such as
`s3://amzn-s3-demo-bucket/prefix/2021-11-01/customer-1234/file.extension`.
For a property like `customer_id`, where the values may not be known in
advance, you can use the partition projection type `injected` and use a
`CREATE TABLE` statement like the following:

```
CREATE EXTERNAL TABLE my_ingested_data3 (
 ...
)
...
PARTITIONED BY (
 day STRING,
 customer_id STRING
)
LOCATION "s3://amzn-s3-demo-bucket/`prefix`/"
TBLPROPERTIES (
 "projection.enabled" = "true",
 "projection.day.type" = "date",
 "projection.day.format" = "yyyy-MM-dd",
 "projection.day.range" = "2021-01-01,NOW",
 "projection.day.interval" = "1",
 "projection.day.interval.unit" = "DAYS",
 "projection.customer_id.type" = "injected",
 "storage.location.template" = "s3://amzn-s3-demo-bucket/`prefix`/${day}/${customer_id}/"
)
```

When you query a table that has a partition key of type `injected`, your
query must include a value for that partition key. A query for the
`my_ingested_data3` table might look like this:

```
SELECT *
FROM my_ingested_data3
WHERE day BETWEEN '2021-11-01' AND '2021-11-30'
AND customer_id = 'customer-1234'
```

## Use the DATE type for the day partition key

Because the values for the `day` partition key are ISO formatted, you
can also use the `DATE` type for the day partition key instead of
`STRING`, as in the following example:

```
PARTITIONED BY (day DATE, customer_id STRING)
```

When you query, this strategy allows you to use date functions on the partition
key without parsing or casting, as in the following example:

```
SELECT *
FROM my_ingested_data3
WHERE day > CURRENT_DATE - INTERVAL '7' DAY
AND customer_id = 'customer-1234'
```

###### Note

Specifying a partition key of the `DATE` type assumes that you have
used the [custom prefix](../../../firehose/latest/dev/s3-prefixes.md "../../../firehose/latest/dev/s3-prefixes.md") feature to create Amazon S3 keys that have ISO formatted
dates. If you are using the default Firehose format of `yyyy/MM/dd/HH`,
you must specify the partition key as type `string` even though the
corresponding table property is of type `date`, as in the following
example:

```
PARTITIONED BY (
  `mydate` string)
TBLPROPERTIES (
  'projection.enabled'='true',
   ...
  'projection.mydate.type'='date',
  'storage.location.template'='s3://amzn-s3-demo-bucket/prefix/${mydate}')
```

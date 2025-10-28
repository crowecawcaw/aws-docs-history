# How to choose partition keys

You can specify how partition projection maps the partition locations to partition
keys. In the `CREATE TABLE`
example in the
previous section, the date and hour were combined into one partition
key called datehour, but other schemes are possible. For example, you could also
configure a table with separate partition keys for the year, month, day, and
hour.

However, splitting dates into year, month, and day means that the `date`
partition projection type can't be used. An alternative is to separate the date from the
hour to still leverage the `date` partition projection type, but make queries
that specify hour ranges easier to read.

With that in mind, the following `CREATE TABLE` example separates the date
from the hour.
Because `date` is a reserved word in SQL, the example uses `day`
as the name for the partition key that represents the date.

```

CREATE EXTERNAL TABLE my_ingested_data2 (
 ...
)
...
PARTITIONED BY (
 day STRING,
 hour INT
)
LOCATION "s3://amzn-s3-demo-bucket/`prefix`/"
TBLPROPERTIES (
 "projection.enabled" = "true",
 "projection.day.type" = "date",
 "projection.day.format" = "yyyy/MM/dd",
 "projection.day.range" = "2021/01/01,NOW",
 "projection.day.interval" = "1",
 "projection.day.interval.unit" = "DAYS",
 "projection.hour.type" = "integer",
 "projection.hour.range" = "0,23",
 "projection.hour.digits" = "2",
 "storage.location.template" = "s3://amzn-s3-demo-bucket/`prefix`/${day}/${hour}/"
)
```

In the example `CREATE TABLE` statement, the hour is a separate partition
key, configured as an integer. The configuration for the hour partition key specifies
the range 0 to 23, and that the hour should be formatted with two digits when Athena
generates the partition locations.

A query for the `my_ingested_data2` table might look like this:

```
SELECT *
FROM my_ingested_data2
WHERE day = '2021/11/09'
AND hour > 3
```

## Understand partition key and partition projection data types

Note that `datehour` key in the first `CREATE TABLE` example
is configured as `date` in the partition projection configuration, but
the type of the partition key is `string`. The same is true for
`day` in the second example. The types in the partition projection
configuration only tell Athena how to format the values when it generates the
partition locations. The types that you specify do not change the type of the
partition key — in queries, `datehour` and `day` are of
type `string`.

When a query includes a condition like `day = '2021/11/09'`, Athena
parses the string on the right side of the expression using the date format
specified in the partition projection configuration. After Athena verifies that the
date is within the configured range, it uses the date format again to insert the
date as a string into the storage location template.

Similarly, for a query condition like `day > '2021/11/09'`, Athena
parses the right side and generates a list of all matching dates within the
configured range. It then uses the date format to insert each date into the storage
location template to create the list of partition locations.

Writing the same condition as `day > '2021-11-09'` or `day >
 DATE '2021-11-09'` does not work. In the first case, the date format does
not match (note the hyphens instead of the forward slashes), and in the second case,
the data types do not match.

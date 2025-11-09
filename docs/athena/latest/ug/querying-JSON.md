# Query JSON data

Amazon Athena lets you query JSON-encoded data, extract data from nested JSON, search for
values, and find length and size of JSON arrays. To learn the basics of querying JSON data
in Athena, consider the following sample planet data:

```
{name:"Mercury",distanceFromSun:0.39,orbitalPeriod:0.24,dayLength:58.65}
{name:"Venus",distanceFromSun:0.72,orbitalPeriod:0.62,dayLength:243.02}
{name:"Earth",distanceFromSun:1.00,orbitalPeriod:1.00,dayLength:1.00}
{name:"Mars",distanceFromSun:1.52,orbitalPeriod:1.88,dayLength:1.03}
```

Notice how each record (essentially, each row in the table) is on a separate line. To
query this JSON data, you can use a `CREATE TABLE` statement like the
following:

```
CREATE EXTERNAL TABLE `planets_json`(
  `name` string,
  `distancefromsun` double,
  `orbitalperiod` double,
  `daylength` double)
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
LOCATION
  's3://amzn-s3-demo-bucket/json/'
```

To query the data, use a simple `SELECT` statement like the following
example.

```
SELECT * FROM planets_json
```

The query results look like the following.

| #   | name    | distancefromsun | orbitalperiod | daylength |
| --- | ------- | --------------- | ------------- | --------- |
| 1   | Mercury | 0.39            | 0.24          | 58.65     |
| 2   | Venus   | 0.72            | 0.62          | 243.02    |
| 3   | Earth   | 1.0             | 1.0           | 1.0       |
| 4   | Mars    | 1.52            | 1.88          | 1.03      |

Notice how the `CREATE TABLE` statement uses the [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md"), which requires each JSON
record to be on a separate line. If the JSON is in pretty print format, or if all records
are on a single line, the data will not be read correctly.

To query JSON data that is in pretty print format, you can use the [Amazon Ion Hive SerDe](ion-serde.md "ion-serde.md") instead of the OpenX JSON SerDe.
Consider the previous data stored in pretty print format:

```
{
  name:"Mercury",
  distanceFromSun:0.39,
  orbitalPeriod:0.24,
  dayLength:58.65
}
{
  name:"Venus",
  distanceFromSun:0.72,
  orbitalPeriod:0.62,
  dayLength:243.02
}
{
  name:"Earth",
  distanceFromSun:1.00,
  orbitalPeriod:1.00,
  dayLength:1.00
}
{
  name:"Mars",
  distanceFromSun:1.52,
  orbitalPeriod:1.88,
  dayLength:1.03
}
```

To query this data without reformatting, you can use a `CREATE TABLE` statement
like the following. Notice that, instead of specifying the OpenX JSON SerDe, the statement
specifies `STORED AS ION`.

```
CREATE EXTERNAL TABLE `planets_ion`(
  `name` string,
  `distancefromsun` DECIMAL(10, 2),
  `orbitalperiod` DECIMAL(10, 2),
  `daylength` DECIMAL(10, 2))
STORED AS ION
LOCATION
  's3://amzn-s3-demo-bucket/json-ion/'
```

The query `SELECT * FROM planets_ion` produces the same results as before. For
more information about creating tables in this way using the Amazon Ion Hive SerDe, see
[Create Amazon Ion tables](ion-serde-using-create-table.md "ion-serde-using-create-table.md").

The preceding example JSON data does not contain complex data types such as nested arrays
or structs. For more information about querying nested JSON data, see [Example: deserializing nested JSON](openx-json-serde.md#nested-json-serde-example "openx-json-serde.md#nested-json-serde-example").

###### Topics

- [Best practices for reading JSON data](parsing-json-data.md "parsing-json-data.md")
- [Extract JSON data from strings](extracting-data-from-JSON.md "extracting-data-from-JSON.md")
- [Search for values in JSON arrays](searching-for-values.md "searching-for-values.md")
- [Get the length and size of JSON arrays](length-and-size.md "length-and-size.md")
- [Troubleshoot JSON queries](json-troubleshooting.md "json-troubleshooting.md")

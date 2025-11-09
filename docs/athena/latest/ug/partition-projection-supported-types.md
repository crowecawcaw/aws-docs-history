# Supported types for partition

projection

A table can have any combination of `enum`, `integer`,
`date,` or `injected` partition column types.

## Enum type

Use the `enum` type for partition columns whose values are members of
an enumerated set (for example, airport codes or AWS Regions).

Define the partition properties in the table as follows:

| Property name                    | Example values          | Description                                                                                                                                                                                         |
| -------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `projection.`columnName`.type`   | `enum`                  | Required. The projection type to use for column<br>`columnName`. The value must be<br>`enum` (case insensitive) to signal the use of the<br>enum type. Leading and trailing white space is allowed. |
| `projection.`columnName`.values` | `A,B,C,D,E,F,G,Unknown` | Required. A comma-separated list of enumerated partition values<br>for column `columnName`. Any white space is<br>considered part of an enum value.                                                 |

###### Note

As a best practice we recommend limiting the use of `enum` based
partition projections to a few dozen or less. Although there is no specific
limit for `enum` projections, the total size of your table's metadata
cannot exceed the AWS Glue limit of about 1 MB when gzip compressed. Note that this
limit is shared across key parts of your table like column names, location,
storage format, and others. If you find yourself using more than a few dozen
unique IDs in your `enum` projection, consider an alternative
approach such as bucketing into a smaller number of unique values in a surrogate
field. By trading off cardinality, you can control the number of unique values
in your `enum` field.

## Integer type

Use the integer type for partition columns whose possible values are interpretable
as integers within a defined range. Projected integer columns are currently limited
to the range of a Java signed long (-263 to
263-1 inclusive).

| Property name                      | Example values                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `projection.`columnName`.type`     | `integer`                             | Required. The projection type to use for column<br>`columnName`. The value must be<br>`integer` (case insensitive) to signal the use of the<br>integer type. Leading and trailing white space is allowed.                                                                                                                                                                                                                                                                                |
| `projection.`columnName`.range`    | `0,10`<br>`-1,8675309`<br>`0001,9999` | Required. A two-element comma-separated list that provides the<br>minimum and maximum range values to be returned by queries on the<br>column `columnName`. Note that the values<br>must be separated by a comma, not a hyphen. These values are<br>inclusive, can be negative, and can have leading zeroes. Leading and<br>trailing white space is allowed.                                                                                                                             |
| `projection.`columnName`.interval` | `1`<br>`5`                            | Optional. A positive integer that specifies the interval between<br>successive partition values for the column<br>`columnName`. For example, a<br>`range` value of "1,3" with an `interval`<br>value of "1" produces the values 1, 2, and 3. The same<br>`range` value with an `interval` value of<br>"2" produces the values 1 and 3, skipping 2. Leading and trailing<br>white space is allowed. The default is 1.                                                                     |
| `projection.`columnName`.digits`   | `1`<br>`5`                            | Optional. A positive integer that specifies the number of digits<br>to include in the partition value's final representation for column<br>`columnName`. For example, a<br>`range` value of "1,3" that has a `digits`<br>value of "1" produces the values 1, 2, and 3. The same<br>`range` value with a `digits` value of "2"<br>produces the values 01, 02, and 03. Leading and trailing white space<br>is allowed. The default is no static number of digits and no leading<br>zeroes. |

## Date type

Use the date type for partition columns whose values are interpretable as dates
(with optional times) within a defined range.

###### Important

Projected date columns are generated in Coordinated Universal Time (UTC) at
query execution time.

| Property name                           | Example values                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------ | ----- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `projection.`columnName`.type`          | `date`                                                                                    | Required. The projection type to use for column<br>`columnName`. The value must be<br>`date` (case insensitive) to signal the use of the<br>date type. Leading and trailing white space is allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `projection.`columnName`.range`         | `201701,201812`<br>`01-01-2010,12-31-2018`<br>`NOW-3YEARS,NOW`<br>`201801,NOW+1MONTH`     | Required. A two-element, comma-separated list which provides<br>the minimum and maximum `range` values for the column<br>`columnName`. These values are<br>inclusive and can use any format compatible with the Java<br>`java.time.*` date types. Both the minimum and<br>maximum values must use the same format. The format specified in<br>the `.format` property must be the format used for<br>these values.<br>This column can also contain relative date strings, formatted<br>in this regular expression pattern:<br>`\s*NOW\s*(([\+\-])\s*([0-9]+)\s*(YEARS?                                                                                                                                                                   | MONTHS? | WEEKS? | DAYS? | HOURS? | MINUTES? | SECONDS?)\s\*)?`<br>White spaces are allowed, but in date literals are considered<br>part of the date strings themselves. |
| `projection.`columnName`.format`        | `yyyyMM`<br>`dd-MM-yyyy`<br>`dd-MM-yyyy-HH-mm-ss`                                         | Required. A date format string based on the Java date format<br>[DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html "https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html"). Can be any supported<br>`Java.time.*` type.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `projection.`columnName`.interval`      | `1`<br>`5`                                                                                | A positive integer that specifies the interval between<br>successive partition values for column<br>`columnName`. For example, a<br>`range` value of `2017-01,2018-12`<br>with an `interval` value of `1` and an<br>`interval.unit` value of `MONTHS`<br>produces the values 2017-01, 2017-02, 2017-03, and so on. The<br>same `range` value with an `interval`<br>value of `2` and an `interval.unit` value<br>of `MONTHS` produces the values 2017-01, 2017-03,<br>2017-05, and so on. Leading and trailing white space is<br>allowed.<br>When the provided dates are at single-day or single-month<br>precision, the `interval` is optional and defaults to<br>1 day or 1 month, respectively. Otherwise, `interval`<br>is required. |
| `projection.`columnName`.interval.unit` | `YEARS`<br>`MONTHS`<br>`WEEKS`<br>`DAYS`<br>`HOURS`<br>`MINUTES`<br>`SECONDS`<br>`MILLIS` | A time unit word that represents the serialized form of a<br>[ChronoUnit](https://docs.oracle.com/javase/8/docs/api/java/time/temporal/ChronoUnit.html "https://docs.oracle.com/javase/8/docs/api/java/time/temporal/ChronoUnit.html"). Possible values are `YEARS`,<br>`MONTHS`, `WEEKS`, `DAYS`,<br>`HOURS`, `MINUTES`,<br>`SECONDS`, or `MILLIS`. These values<br>are case insensitive.<br>When the provided dates are at single-day or single-month<br>precision, the `interval.unit` is optional and<br>defaults to 1 day or 1 month, respectively. Otherwise, the<br>`interval.unit` is required.                                                                                                                                 |

###### Example – Partitioning by month

The following example table configuration partitions data by month from 2015
to the present.

```
'projection.month.type'='date',
'projection.month.format'='yyyy-MM',
'projection.month.interval'='1',
'projection.month.interval.unit'='MONTHS',
'projection.month.range'='2015-01,NOW',
...
```

## Injected type

Use the injected type for partition columns with possible values that cannot be
procedurally generated within some logical range but that are provided in a query's
`WHERE` clause as a single value.

It is important to keep in mind the following points:

- Queries on injected columns fail if a filter expression is not provided
  for each injected column.
- Queries with multiple values for a filter expression on an injected column
  succeed only if the values are disjunct.
- Only columns of `string` type are supported.
- When you use the `WHERE IN` clause with an injected partition
  column, there is a limit of 1,000 values that you can specify in the
  `IN` list. To query a dataset with more than 1,000 partitions
  for an injected column, split the query into multiple smaller queries, each
  with up to 1,000 values in the `WHERE IN` clause, and then
  aggregate the results.

| Property name                  | Value      | Description                                                                                                                                                                                                                |
| ------------------------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `projection.`columnName`.type` | `injected` | Required. The projection type to use for the column<br>`columnName`. Only the<br>`string` type is supported. The value specified must<br>be `injected` (case insensitive). Leading and trailing<br>white space is allowed. |

For more information, see [When to use the
injected projection type](partition-projection-dynamic-id-partitioning.md#partition-projection-injection "partition-projection-dynamic-id-partitioning.md#partition-projection-injection").

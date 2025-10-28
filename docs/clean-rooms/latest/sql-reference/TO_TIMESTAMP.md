# TO_TIMESTAMP function

TO_TIMESTAMP converts a TIMESTAMP string to TIMESTAMPTZ.

## Syntax

```
to_timestamp (*timestamp*)
```

```
to_timestamp (*timestamp*, *format*)
```

## Arguments

_timestamp_

A timestamp string or a data type that can be cast into a timestamp
string.

_format_

A string literal that matches Spark's datetime patterns. For valid datetime patterns,
see [Datetime
Patterns for Formatting and Parsing](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html").

## Return type

TIMESTAMP

## Examples

The following example demonstrates using the TO_TIMESTAMP function to convert a
TIMESTAMP string to a TIMESTAMP.

```
`select current_timestamp() as timestamp, to_timestamp( current_timestamp(), 'YYYY-MM-DD HH24:MI:SS') as second;`

`timestamp | second
-------------------------- ----------------------
2021-04-05 19:27:53.281812 | 2021-04-05 19:27:53+00`
```

It's possible to pass TO_TIMESTAMP part of a date. The remaining date parts are set
to default values. The time is included in the output:

```
`SELECT TO_TIMESTAMP('2017','YYYY');`

`to_timestamp
--------------------------
2017-01-01 00:00:00+00`
```

The following SQL statement converts the string '2011-12-18 24:38:15' to a TIMESTAMP.
The result is a TIMESTAMP that falls on the next day because the number of hours is more
than 24 hours:

```
`select to_timestamp('2011-12-18 24:38:15', 'YYYY-MM-DD HH24:MI:SS');`

`to_timestamp
----------------------
2011-12-19 00:38:15+00`
```

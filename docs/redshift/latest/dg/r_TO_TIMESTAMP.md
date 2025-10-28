Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TO_TIMESTAMP function

TO_TIMESTAMP converts a TIMESTAMP string to TIMESTAMPTZ. For a list of additional date and time functions for Amazon Redshift,
see [Date and time functions](Date_functions_header.md "Date_functions_header.md").

## Syntax

```
to_timestamp(*timestamp*, *format*)
```

```
to_timestamp (*timestamp*, *format*, *is\_strict*)
```

## Arguments

_timestamp_

A string that represents a timestamp value in the format specified by
_format_. If this argument is left as empty, the timestamp value defaults to `0001-01-01 00:00:00`.

_format_

A string literal that defines the format of the _timestamp_ value. Formats that
include a time zone (`TZ`, `tz`, or
`OF`) are not supported as input. For valid timestamp
formats, see [Datetime format strings](r_FORMAT_strings.md "r_FORMAT_strings.md").

_is_strict_

An optional Boolean value that specifies whether an error is returned if an input timestamp value is out of range.
When _is_strict_ is set to TRUE, an error is returned if there is an out of range value.
When _is_strict_ is set to FALSE, which is the default, then overflow values are accepted.

## Return type

TIMESTAMPTZ

## Examples

The following example demonstrates using the TO_TIMESTAMP function to convert a
TIMESTAMP string to a TIMESTAMPTZ.

```
`select sysdate, to_timestamp(sysdate, 'YYYY-MM-DD HH24:MI:SS') as second;`

`timestamp | second
-------------------------- ----------------------
2021-04-05 19:27:53.281812 | 2021-04-05 19:27:53+00`
```

It's possible to pass TO_TIMESTAMP part of a date. The remaining date parts are set to default values. The time is included in the output:

```
`SELECT TO_TIMESTAMP('2017','YYYY');`

`to_timestamp
--------------------------
2017-01-01 00:00:00+00`
```

The following SQL statement converts the string '2011-12-18 24:38:15' to a TIMESTAMPTZ. The result is a
TIMESTAMPTZ that falls on the next day because the number of hours is more than 24 hours:

```
`SELECT TO_TIMESTAMP('2011-12-18 24:38:15', 'YYYY-MM-DD HH24:MI:SS');`

`to_timestamp
----------------------
2011-12-19 00:38:15+00`
```

The following SQL statement converts the string '2011-12-18 24:38:15' to a TIMESTAMPTZ. The result
is an error because the time value in the timestamp is more than 24 hours:

```
`SELECT TO_TIMESTAMP('2011-12-18 24:38:15', 'YYYY-MM-DD HH24:MI:SS', TRUE);`

`ERROR: date/time field time value out of range: 24:38:15.0`
```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# TRUNC function

Truncates a `TIMESTAMP` and returns a `DATE`.

This function can also truncate a number. For more information, see [TRUNC function](r_TRUNC.md "r_TRUNC.md").

## Syntax

```
TRUNC(*timestamp*)
```

## Arguments

_timestamp_

A column of data type `TIMESTAMP` or an expression that
implicitly evaluates to a `TIMESTAMP` type.

To return a timestamp value with `00:00:00` as the time, cast the
function result to a `TIMESTAMP`.

## Return type

DATE

## Examples

The following example returns the date portion from the result of the SYSDATE
function (which returns a timestamp).

```
`SELECT SYSDATE;`

`+----------------------------+
| timestamp |
+----------------------------+
| 2011-07-21 10:32:38.248109 |
+----------------------------+`

`SELECT TRUNC(SYSDATE);`

`+------------+
| trunc |
+------------+
| 2011-07-21 |
+------------+`
```

The following example applies the TRUNC function to a `TIMESTAMP` column. The return
type is a date.

```
`SELECT TRUNC(starttime) FROM event
ORDER BY eventid LIMIT 1;`

`+------------+
| trunc |
+------------+
| 2008-01-25 |
+------------+`
```

The following example returns a timestamp value with `00:00:00` as the time by casting the TRUNC function result to a `TIMESTAMP`.

```
`SELECT CAST((TRUNC(SYSDATE)) AS TIMESTAMP);`

`+---------------------+
| trunc |
+---------------------+
| 2011-07-21 00:00:00 |
+---------------------+`
```

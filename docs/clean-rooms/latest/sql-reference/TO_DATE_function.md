# TO_DATE function

TO_DATE converts a date represented by a character string to a DATE data type.

## Syntax

```
TO_DATE (*date\_str*)
```

```
TO_DATE (*date\_str*, *format*)
```

## Arguments

_date_str_

A date string or a data type that can be cast into a date string.

_format_

A string literal that matches Spark's datetime patterns. For valid datetime
patterns, see [Datetime Patterns for Formatting and Parsing](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html").

## Return type

TO_DATE returns a DATE, depending on the _format_ value.

If the conversion to _format_ fails, then an error is returned.

## Examples

The following SQL statement converts the date `02 Oct 2001` into a date
data type.

```
`select to_date('02 Oct 2001', 'dd MMM yyyy');`
`to_date
------------
2001-10-02
(1 row)`
```

The following SQL statement converts the string `20010631` to a
date.

```
select to_date('20010631', 'yyyyMMdd');
```

The following SQL statement converts the string `20010631` to a date:

```
`to_date('20010631', 'YYYYMMDD', TRUE);`
```

The result is a null value because there are only 30 days in June.

```
`to_date
------------
NULL`
```

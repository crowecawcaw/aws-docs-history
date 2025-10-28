# TO_DATE function

TO_DATE converts a date represented by a character string to a DATE data type.

## Syntax

```
TO_DATE (*date\_str*, *format*)
```

```
TO_DATE(*date\_str*, *format*, *is\_strict*)
```

## Arguments

_string_

A date string.

_format_

A string literal that matches Redshift's datetime patterns.

_is_strict_

Will return an error if the date overflows.

## Return type

TO_DATE returns a DATE, depending on the _format_ value.

If the conversion to _format_ fails, then an error is returned.

## Examples

The following SQL statement converts the date `02 Oct 2001` into a date
data type.

```
`select to_date('02 Oct 2001', 'DD Mon YYYY');`
`to_date
------------
2001-10-02
(1 row)`
```

The following SQL statement converts the string `20010631` to a
date.

```
select to_date('20010631', 'YYYYMMDD', FALSE);
```

The result is July 1, 2001, because there are only 30 days in June.

```
`to_date
------------
2001-07-01`

```

The following SQL statement converts the string `20010631` to a date:

```
`to_date('20010631', 'YYYYMMDD', TRUE);`
```

The result is an error because there are only 30 days in June.

```
`ERROR: date/time field date value out of range: 2001-6-31`
```

Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TO_DATE function

TO_DATE converts a date represented by a character string to a DATE data type.

###### Note

TO_DATE doesn't support format strings with Q (Quarter number).

## Syntax

```
TO_DATE(*string*, *format*)
```

```
TO_DATE(*string*, *format*, *is\_strict*)
```

## Arguments

_string_

A string to be converted.

_format_

A string literal that defines the format of the input _string_,
in terms of its date parts. For a list of valid day, month, and year formats, see [Datetime format strings](r_FORMAT_strings.md "r_FORMAT_strings.md").

_is_strict_

An optional Boolean value that specifies whether an error is returned if
an input date value is out of range. When _is_strict_ is
set to `TRUE`, an error is returned if there is an out of range
value. When _is_strict_ is set to `FALSE`,
which is the default, then overflow values are accepted.

## Return type

TO_DATE returns a DATE, depending on the _format_ value.

If the conversion to _format_ fails, then an error is returned.

## Examples

The following SQL statement converts the date `02 Oct 2001` into a
date data type.

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

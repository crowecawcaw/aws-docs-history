Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# TO\_DATE function

TO\_DATE converts a date represented by a character string to a DATE data type.

###### Note

TO\_DATE doesn't support format strings with Q (Quarter number).

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

_is\_strict_

An optional Boolean value that specifies whether an error is returned if
an input date value is out of range. When _is\_strict_ is
set to `TRUE`, an error is returned if there is an out of range
value. When _is\_strict_ is set to `FALSE`,
which is the default, then overflow values are accepted.

## Return type

TO\_DATE returns a DATE, depending on the _format_ value.

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

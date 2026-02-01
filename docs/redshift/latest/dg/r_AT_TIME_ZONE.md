Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AT TIME ZONE function

AT TIME ZONE specifies which time zone to use with a TIMESTAMP or TIMESTAMPTZ
expression.

## Syntax

```
AT TIME ZONE '*timezone*'
```

## Arguments

_timezone_

The `TIMEZONE` for the return value. The time zone can be
specified as a time zone name (such as `'Africa/Kampala'`
or `'Singapore'`) or as a time zone abbreviation (such as
`'UTC'` or `'PDT'`).

To view a list of supported time zone names, run the following command.

```
select pg_timezone_names();
```

To view a list of
supported time zone abbreviations, run the following command.

```
select pg_timezone_abbrevs();
```

For more
information and examples, see [Time zone usage notes](CONVERT_TIMEZONE.md#CONVERT_TIMEZONE-usage-notes "CONVERT_TIMEZONE.md#CONVERT_TIMEZONE-usage-notes").

## Return type

TIMESTAMPTZ when used with a TIMESTAMP expression. TIMESTAMP when used with a
TIMESTAMPTZ expression.

## Examples

The following example converts a timestamp value without time zone and interprets it
as MST time (UTC+7 in POSIX). The example returns a value of data type TIMESTAMPTZ for the UTC timezone. If you configure your default timezone to a timezone other than UTC, you might see a different result.

```
`SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'MST';`

`timezone
------------------------
2001-02-17 03:38:40+00`
```

The following example takes an input timestamp with a time zone value where the
specified time zone is EST (UTC+5 in POSIX) and converts it to MST (UTC+7 in POSIX). The example returns a value of data type TIMESTAMP.

```
`SELECT TIMESTAMPTZ '2001-02-16 20:38:40-05' AT TIME ZONE 'MST';`

`timezone
------------------------
2001-02-16 18:38:40`
```

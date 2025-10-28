Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMEZONE function

TIMEZONE returns a timestamp for the specified time zone and timestamp value.

For information and examples about how to set time zone, see [timezone](r_timezone_config.md "r_timezone_config.md").

For information and examples about how to convert time zone, see [CONVERT_TIMEZONE](CONVERT_TIMEZONE.md "CONVERT_TIMEZONE.md").

## Syntax

```
TIMEZONE('*timezone*', { *timestamp* | *timestamptz* })
```

## Arguments

_timezone_

The time zone for the return value. The time zone can be specified as a time
zone name (such as `'Africa/Kampala'` or
`'Singapore'`) or as a time zone abbreviation (such as
`'UTC'` or `'PDT'`). To view a
list of supported time zone names, run the following command.

```
select pg_timezone_names();
```

To view a list of
supported time zone abbreviations, run the following command.

```
select pg_timezone_abbrevs();
```

Note that Amazon Redshift uses the [IANA Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones") as the authoritative source of time zone
specification. For more information and examples, see [Time zone usage notes](CONVERT_TIMEZONE.md#CONVERT_TIMEZONE-usage-notes "CONVERT_TIMEZONE.md#CONVERT_TIMEZONE-usage-notes").

_timestamp_ | _timestamptz_

An expression that results in a TIMESTAMP or TIMESTAMPTZ type, or a value
that can implicitly be coerced to a timestamp or a timestamp with time
zone.

## Return type

TIMESTAMPTZ when used with a TIMESTAMP expression.

TIMESTAMP when used with a TIMESTAMPTZ expression.

## Examples

The following returns a timestamp for the UTC time zone using the timestamp
`2008-06-17 09:44:54` from the PST timezone.

```
`SELECT TIMEZONE('PST', '2008-06-17 09:44:54');`

`timezone
-----------------------
2008-06-17 17:44:54+00`
```

The following returns a timestamp for the PST time zone using the timestamp with UTC
time zone `2008-06-17 09:44:54+00`.

```
`SELECT TIMEZONE('PST', timestamptz('2008-06-17 09:44:54+00'));`

`timezone
-----------------------
2008-06-17 01:44:54`
```

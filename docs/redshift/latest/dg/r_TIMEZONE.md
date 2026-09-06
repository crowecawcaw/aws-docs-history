

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TIMEZONE function
<a name="r_TIMEZONE"></a>

TIMEZONE returns a timestamp for the specified time zone and timestamp value.

For information and examples about how to set time zone, see [timezone](r_timezone_config.md).

For information and examples about how to convert time zone, see [CONVERT\_TIMEZONE](CONVERT_TIMEZONE.md).

## Syntax
<a name="r_TIMEZONE-syntax"></a>

```
TIMEZONE('timezone', { timestamp | timestamptz })
```

## Arguments
<a name="r_TIMEZONE-arguments"></a>

*timezone*  
The time zone for the return value. The time zone can be specified as a time zone name (such as **'Africa/Kampala'** or **'Singapore'**) or as a time zone abbreviation (such as **'UTC'** or **'PDT'**). To view a list of supported time zone names, run the following command.   

```
select pg_timezone_names();
```
 To view a list of supported time zone abbreviations, run the following command.   

```
select pg_timezone_abbrevs();
```
Note that Amazon Redshift uses the [IANA Time Zone Database](https://www.iana.org/time-zones) as the authoritative source of time zone specification. For more information and examples, see [Time zone usage notes](CONVERT_TIMEZONE.md#CONVERT_TIMEZONE-usage-notes).

*timestamp* \| *timestamptz*  
An expression that results in a TIMESTAMP or TIMESTAMPTZ type, or a value that can implicitly be coerced to a timestamp or a timestamp with time zone.

## Return type
<a name="r_TIMEZONE-return-type"></a>

TIMESTAMPTZ when used with a TIMESTAMP expression. 

TIMESTAMP when used with a TIMESTAMPTZ expression. 

## Examples
<a name="r_TIMEZONE-examples"></a>

The following returns a timestamp for the UTC time zone using the timestamp `2008-06-17 09:44:54` from the PST timezone.

```
SELECT TIMEZONE('PST', '2008-06-17 09:44:54');

timezone
-----------------------
2008-06-17 17:44:54+00
```

The following returns a timestamp for the PST time zone using the timestamp with UTC time zone `2008-06-17 09:44:54+00`.

```
SELECT TIMEZONE('PST', timestamptz('2008-06-17 09:44:54+00'));

timezone
-----------------------
2008-06-17 01:44:54
```
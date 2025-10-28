Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CONVERT_TIMEZONE function

CONVERT_TIMEZONE converts a timestamp from one time zone to another. The function automatically adjusts for daylight saving time.

## Syntax

```
CONVERT_TIMEZONE( ['*source\_timezone*',] '*target\_timezone*', '*timestamp*')
```

## Arguments

_source_timezone_

(Optional) The time zone of the current timestamp. The default is UTC. For
more information, see [Time zone usage notes](#CONVERT_TIMEZONE-usage-notes "#CONVERT_TIMEZONE-usage-notes").

_target_timezone_

The time zone for the new timestamp. For more information, see [Time zone usage notes](#CONVERT_TIMEZONE-usage-notes "#CONVERT_TIMEZONE-usage-notes").

_timestamp_

A timestamp column or an expression that implicitly converts to a timestamp.

## Return type

TIMESTAMP

## Time zone usage notes

_source_timezone_ or _target_timezone_
can be specified as a time zone name (such as 'Africa/Kampala' or 'Singapore') or as a
time zone abbreviation (such as 'UTC' or 'PDT'). You don't have to convert time zone names to names or abbreviations
to abbreviations. For example, you can choose a timestamp from the source time zone name 'Singapore' and
convert it to a timestamp in the time zone abbreviation 'PDT'.

###### Note

The results of using a time zone name or a time zone abbreviation can be different due to local seasonal time, such as daylight saving time.

### Using a time zone name

To view a current and complete list of time zone names, run the following command.

```
select pg_timezone_names();
```

Each row contains a comma-separated string with the time zone name, abbreviation, UTC offset, and indicator if the time zone observes daylight saving time (`t` or `f`).
For example, the following snippet shows two resulting rows.
The first row is the time zone `Antarctica/South Pole`, abbreviation `NZDT`, with `13:00:00` offset from UTC, and `f` to indicate it doesn't observe daylight saving time.
The second row is the time zone `Europe/Paris`, abbreviation `CET`, with `01:00:00` offset from UTC, and `f` to indicate it observes daylight saving time.

```
pg_timezone_names
------------------
(Antarctica/South_Pole,NZDT,13:00:00,t)
(Europe/Paris,CET,01:00:00,f)

```

Run the SQL statement to obtain the entire list and find a time zone name.
Approximately 600 rows are returned.
Even though some of the returned time zone names are capitalized initialisms or
acronyms (for example; GB, PRC, ROK), the CONVERT_TIMEZONE function treats them as time
zone names, not time zone abbreviations.

If you specify a time zone using a time zone name, CONVERT_TIMEZONE automatically
adjusts for daylight saving time (DST), or any other local seasonal protocol, such as
Summer Time, Standard Time, or Winter Time, that is in force for that time zone
during the date and time specified by '_timestamp_'. For example,
'Europe/London' represents UTC in the winter and adds one hour in the summer. Note
that Amazon Redshift uses the [IANA Time
Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones") as the authoritative source of time zone specification.

### Using a time zone abbreviation

To view a current and complete list of
time zone abbreviations, run the following command.

```
select pg_timezone_abbrevs();
```

The results contain a comma-separated string with the time zone abbreviation, UTC offset, and indicator if the time zone observes daylight saving time (`t` or `f`).
For example, the following snippet shows two resulting rows.
The first row contains the abbreviation for Pacific Daylight Time `PDT`, with a `-07:00:00` offset from UTC, and `t` to indicate it observes daylight saving time.
The second row contains the abbreviation for Pacific Standard Time `PST`, with a `-08:00:00` offset from UTC, and `f` to indicate it doesn't observe daylight saving time.

```
pg_timezone_abbrevs
--------------------
(PDT,-07:00:00,t)
(PST,-08:00:00,f)

```

Run the SQL statement to obtain the entire list and find an abbreviation based on its offset and daylight saving time indicator.
Approximately 200 rows are returned.

Time zone abbreviations represent a fixed offset from UTC. If you specify a time
zone using a time zone abbreviation, CONVERT_TIMEZONE uses the fixed offset from UTC
and doesn't adjust for any local seasonal protocol.

### Using POSIX-style format

A POSIX-style time zone
specification is in the form _STDoffset_ or
_STDoffsetDST_, where _STD_ is a time zone
abbreviation, _offset_ is the numeric offset in hours west from UTC,
and _DST_ is an optional daylight saving zone abbreviation. Daylight
saving time is assumed to be one hour ahead of the given offset.

POSIX-style time zone formats use positive offsets west of Greenwich, in contrast to
the ISO-8601 convention, which uses positive offsets east of Greenwich.

The following are examples of POSIX-style time zones:

- PST8
- PST8PDT
- EST5
- EST5EDT

###### Note

Amazon Redshift doesn't validate POSIX-style time zone specifications, so it is
possible to set the time zone to an invalid value. For example, the following command
doesn't return an error, even though it sets the time zone to an invalid
value.

```
set timezone to ‘xxx36’;
```

## Examples

Many of the examples use the TICKIT sample data set. For more information, see [Sample database](c_sampledb.md "c_sampledb.md").

The following example converts the timestamp value from the
default UTC time zone to PST.

```
`select convert_timezone('PST', '2008-08-21 07:23:54');`

 convert_timezone
------------------------
2008-08-20 23:23:54
```

The following example converts the timestamp value in the LISTTIME column from the
default UTC time zone to PST. Though the timestamp is within the daylight time period,
it's converted to standard time because the target time zone is specified as an
abbreviation (PST).

```
`select listtime, convert_timezone('PST', listtime) from listing
where listid = 16;`

     listtime       |   convert_timezone
--------------------+-------------------
2008-08-24 09:36:12     2008-08-24 01:36:12
```

The following example converts a timestamp LISTTIME column from the default UTC time
zone to US/Pacific time zone. The target time zone uses a time zone name, and the timestamp is within the daylight time period, so the function returns the daylight
time.

```
`select listtime, convert_timezone('US/Pacific', listtime) from listing
where listid = 16;`

     listtime       |   convert_timezone
--------------------+---------------------
2008-08-24 09:36:12 | 2008-08-24 02:36:12
```

The following example converts a timestamp string from EST to
PST:

```
`select convert_timezone('EST', 'PST', '20080305 12:25:29');`

 convert_timezone
-------------------
2008-03-05 09:25:29
```

The following example converts a timestamp to US Eastern Standard Time because the
target time zone uses a time zone name (America/New_York) and the timestamp is within
the standard time
period.

```
`select convert_timezone('America/New_York', '2013-02-01 08:00:00');`

 convert_timezone
---------------------
2013-02-01 03:00:00
(1 row)
```

The following example converts the timestamp to US Eastern Daylight Time because the
target time zone uses a time zone name (America/New_York) and the timestamp is within
the daylight time
period.

```
`select convert_timezone('America/New_York', '2013-06-01 08:00:00');`

 convert_timezone
---------------------
2013-06-01 04:00:00
(1 row)

```

The following example demonstrates the use of offsets.

```
`SELECT CONVERT_TIMEZONE('GMT','NEWZONE +2','2014-05-17 12:00:00') as newzone_plus_2,
CONVERT_TIMEZONE('GMT','NEWZONE-2:15','2014-05-17 12:00:00') as newzone_minus_2_15,
CONVERT_TIMEZONE('GMT','America/Los_Angeles+2','2014-05-17 12:00:00') as la_plus_2,
CONVERT_TIMEZONE('GMT','GMT+2','2014-05-17 12:00:00') as gmt_plus_2;`

   newzone_plus_2    | newzone_minus_2_15  |      la_plus_2      |     gmt_plus_2
---------------------+---------------------+---------------------+---------------------
2014-05-17 10:00:00 | 2014-05-17 14:15:00 | 2014-05-17 10:00:00 | 2014-05-17 10:00:00
(1 row)
```

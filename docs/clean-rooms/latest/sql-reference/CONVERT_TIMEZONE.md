# CONVERT_TIMEZONE function

CONVERT_TIMEZONE converts a timestamp from one time zone to another. The function
automatically adjusts for daylight saving time.

## Syntax

```
CONVERT_TIMEZONE ( ['*source\_timezone*',] '*target\_timezone*', '*timestamp*')
```

## Arguments

_source_timezone_

(Optional) The time zone of the current timestamp. The default is UTC.

_target_timezone_

The time zone for the new timestamp.

_timestamp_

A timestamp column or an expression that implicitly converts to a
timestamp.

## Return type

TIMESTAMP

## Examples

The following example converts the timestamp value from the default UTC time zone to
PST.

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
zone to US/Pacific time zone. The target time zone uses a time zone name, and the
timestamp is within the daylight time period, so the function returns the daylight
time.

```
`select listtime, convert_timezone('US/Pacific', listtime) from listing
where listid = 16;`

     listtime       |   convert_timezone
--------------------+---------------------
2008-08-24 09:36:12 | 2008-08-24 02:36:12
```

The following example converts a timestamp string from EST to PST:

```
`select convert_timezone('EST', 'PST', '20080305 12:25:29');`

 convert_timezone
-------------------
2008-03-05 09:25:29
```

The following example converts a timestamp to US Eastern Standard Time because the
target time zone uses a time zone name (America/New_York) and the timestamp is within
the standard time period.

```
`select convert_timezone('America/New_York', '2013-02-01 08:00:00');`

 convert_timezone
---------------------
2013-02-01 03:00:00
(1 row)
```

The following example converts the timestamp to US Eastern Daylight Time because the
target time zone uses a time zone name (America/New_York) and the timestamp is within
the daylight time period.

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

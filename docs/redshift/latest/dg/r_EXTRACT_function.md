Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# EXTRACT function

The EXTRACT function returns a date or time part from a TIMESTAMP, TIMESTAMPTZ, TIME, TIMETZ, INTERVAL YEAR TO MONTH, or INTERVAL DAY TO SECOND value.
Examples include a day, month, year, hour, minute, second, millisecond, or microsecond from a timestamp.

## Syntax

```
EXTRACT(*datepart* FROM *source*)
```

## Arguments

_datepart_

The subfield of a date or time to extract, such as a day, month, year, hour, minute, second, millisecond, or microsecond.
For possible values, see [Date parts for date or timestamp
functions](r_Dateparts_for_datetime_functions.md "r_Dateparts_for_datetime_functions.md").

_source_

A column or expression that evaluates to a data type of TIMESTAMP, TIMESTAMPTZ, TIME, TIMETZ, INTERVAL YEAR TO MONTH, or INTERVAL DAY TO SECOND.

## Return type

INTEGER if the _source_ value evaluates to data type TIMESTAMP, TIME, TIMETZ, INTERVAL YEAR TO MONTH, or INTERVAL DAY TO SECOND.

DOUBLE PRECISION if the _source_ value evaluates to data type TIMESTAMPTZ.

## Examples with TIMESTAMP

The following example determines the week numbers for sales in which the price paid
was $10,000 or more. This example uses the TICKIT data. For more information, see
[Sample database](c_sampledb.md "c_sampledb.md").

```
select salesid, extract(week from saletime) as weeknum
from sales
where pricepaid > 9999
order by 2;

salesid | weeknum
--------+---------
 159073 |       6
 160318 |       8
 161723 |      26

```

The following example returns the minute value from a literal timestamp value.

```
select extract(minute from timestamp '2009-09-09 12:08:43');

date_part
-----------
8

```

The following example returns the millisecond value from a literal timestamp value.

```
select extract(ms from timestamp '2009-09-09 12:08:43.101');

date_part
-----------
101

```

## Examples with TIMESTAMPTZ

The following example returns the year value from a literal timestamptz value.

```
select extract(year from timestamptz '1.12.1997 07:37:16.00 PST');

date_part
-----------
1997

```

## Examples with TIME

The following example table TIME_TEST has a column TIME_VAL (type TIME) with three
values inserted.

```
select time_val from time_test;

time_val
---------------------
20:00:00
00:00:00.5550
00:58:00
```

The following example extracts the minutes from each time_val.

```
select extract(minute from time_val) as minutes from time_test;

minutes
-----------
         0
         0
         58
```

The following example extracts the hours from each time_val.

```
select extract(hour from time_val) as hours from time_test;

hours
-----------
         20
         0
         0
```

The following example extracts milliseconds from a literal value.

```
select extract(ms from time '18:25:33.123456');

 date_part
-----------
     123
```

## Examples with TIMETZ

The following example table TIMETZ_TEST has a column TIMETZ_VAL (type TIMETZ) with
three values inserted.

```
select timetz_val from timetz_test;

timetz_val
------------------
04:00:00+00
00:00:00.5550+00
05:58:00+00
```

The following example extracts the hours from each timetz_val.

```
select extract(hour from timetz_val) as hours from time_test;

hours
-----------
         4
         0
         5
```

The following example extracts milliseconds from a literal value. Literals aren't
converted to UTC before the extraction is processed.

```
select extract(ms from timetz '18:25:33.123456 EST');

 date_part
-----------
     123
```

The following example returns the timezone offset hour from UTC from a literal timetz value.

```
select extract(timezone_hour from timetz '1.12.1997 07:37:16.00 PDT');

date_part
-----------
-7

```

## Examples with INTERVAL YEAR TO MONTH and INTERVAL DAY TO SECOND

The following example extracts the day part of `1` from the INTERVAL DAY TO SECOND that defines 36 hours, which is 1 day 12 hours.

```
`select EXTRACT('days' from INTERVAL '36 hours' DAY TO SECOND)`
 `date_part
------------------
 1`
```

The following example extracts the month part of `3` from the YEAR TO MONTH that defines 15 months, which is 1 year 3 months.

```
`select EXTRACT('month' from INTERVAL '15 months' YEAR TO MONTH)`
 `date_part
------------------
 3`
```

The following example extracts the month part of `6` from 30 months which is 2 years 6 months.

```
`select EXTRACT('month' from INTERVAL '30' MONTH)`
 `date_part
------------------
 6`
```

The following example extracts the hour part of `2` from 50 hours which is 2 days 2 hours.

```
`select EXTRACT('hours' from INTERVAL '50' HOUR)`
 `date_part
------------------
 2`
```

The following example extracts the minute part of `11` from 1 hour 11 minutes 11.123 seconds.

```
`select EXTRACT('minute' from INTERVAL '70 minutes 70.123 seconds' MINUTE TO SECOND)`
 `date_part
------------------
 11`
```

The following example extracts the seconds part of `1.11` from 1 day 1 hour 1 minute 1.11 seconds.

```
`select EXTRACT('seconds' from INTERVAL '1 day 1:1:1.11' DAY TO SECOND)`
 `date_part
------------------
 1.11`
```

The following example extracts the total number of hours in an INTERVAL. Each part is extracted and added to a total.

```
`select EXTRACT('days' from INTERVAL '50' HOUR) * 24 + EXTRACT('hours' from INTERVAL '50' HOUR)`
 `?column?
------------------
 50`
```

The following example extracts the total number of seconds in an INTERVAL. Each part is extracted and added to a total.

```
`select EXTRACT('days' from INTERVAL '1 day 1:1:1.11' DAY TO SECOND) * 86400 +
 EXTRACT('hours' from INTERVAL '1 day 1:1:1.11' DAY TO SECOND) * 3600 +
 EXTRACT('minutes' from INTERVAL '1 day 1:1:1.11' DAY TO SECOND) * 60 +
 EXTRACT('seconds' from INTERVAL '1 day 1:1:1.11' DAY TO SECOND)`
 `?column?
------------------
 90061.11`
```

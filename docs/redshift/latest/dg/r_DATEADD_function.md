Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DATEADD function

Increments a DATE, TIME, TIMETZ, or TIMESTAMP value by a specified interval.

## Syntax

```
DATEADD( *datepart*, *interval*, {*date*|*time*|*timetz*|*timestamp*} )
```

## Arguments

_datepart_

The date part (year, month, day, or hour, for example) that the function
operates on. For more information, see [Date parts for date or timestamp
functions](r_Dateparts_for_datetime_functions.md "r_Dateparts_for_datetime_functions.md").

_interval_

An integer that specified the interval (number of days, for example) to
add to the target expression. A negative integer subtracts the interval.

_date_|_time_|_timetz_|_timestamp_

A DATE, TIME, TIMETZ, or TIMESTAMP column or an expression that implicitly converts to a
DATE, TIME, TIMETZ, or TIMESTAMP. The DATE, TIME, TIMETZ, or TIMESTAMP expression must contain the
specified date part.

## Return type

TIMESTAMP or TIME or TIMETZ depending on the input data type.

## Examples with a DATE column

The following example adds 30 days to each date in November that exists in the DATE
table.

```
select dateadd(day,30,caldate) as novplus30
from date
where month='NOV'
order by dateid;

novplus30
---------------------
2008-12-01 00:00:00
2008-12-02 00:00:00
2008-12-03 00:00:00
...
(30 rows)
```

The following example adds 18 months to a literal date value.

```
select dateadd(month,18,'2008-02-28');

date_add
---------------------
2009-08-28 00:00:00
(1 row)
```

The
default column name for a DATEADD function is DATE_ADD. The default timestamp for a
date value is `00:00:00`.

The following example adds 30 minutes to a date value that doesn't specify a
timestamp.

```
select dateadd(m,30,'2008-02-28');

date_add
---------------------
2008-02-28 00:30:00
(1 row)
```

You can name date parts in full or abbreviate them. In this case, _m_
stands for minutes, not months.

## Examples with a TIME column

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

The following example adds 5 minutes to each TIME_VAL in the TIME_TEST table.

```
select dateadd(minute,5,time_val) as minplus5 from time_test;

minplus5
---------------
20:05:00
00:05:00.5550
01:03:00
```

The following example adds 8 hours to a literal time value.

```
select dateadd(hour, 8, time '13:24:55');

date_add
---------------
21:24:55
```

The following example shows when a time goes over 24:00:00 or under 00:00:00.

```
select dateadd(hour, 12, time '13:24:55');

date_add
---------------
01:24:55
```

## Examples with a TIMETZ column

The output values in these examples are in UTC which is the default timezone.

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

The following example adds 5 minutes to each TIMETZ_VAL in TIMETZ_TEST table.

```
select dateadd(minute,5,timetz_val) as minplus5_tz from timetz_test;

minplus5_tz
---------------
04:05:00+00
00:05:00.5550+00
06:03:00+00
```

The following example adds 2 hours to a literal timetz value.

```
select dateadd(hour, 2, timetz '13:24:55 PST');

date_add
---------------
23:24:55+00
```

## Examples with a TIMESTAMP column

The output values in these examples are in UTC which is the default timezone.

The following example table TIMESTAMP_TEST has a column TIMESTAMP_VAL (type TIMESTAMP) with
three values inserted.

```
SELECT timestamp_val FROM timestamp_test;

timestamp_val
------------------
1988-05-15 10:23:31
2021-03-18 17:20:41
2023-06-02 18:11:12
```

The following example adds 20 years only
to the TIMESTAMP_VAL values in TIMESTAMP_TEST from before the year 2000.

```
SELECT dateadd(year,20,timestamp_val)
FROM timestamp_test
WHERE timestamp_val < to_timestamp('2000-01-01 00:00:00', 'YYYY-MM-DD HH:MI:SS');

date_add
---------------
2008-05-15 10:23:31
```

The following example adds 5 seconds to a literal timestamp value written without
a seconds indicator.

```
SELECT dateadd(second, 5, timestamp '2001-06-06');

date_add
---------------
2001-06-06 00:00:05
```

## Usage notes

The DATEADD(month, ...) and ADD_MONTHS functions handle dates that fall at the ends
of months differently:

- ADD_MONTHS: If the date you are adding to is the last day of the month, the
  result is always the last day of the result month, regardless of the length of the
  month. For example, April 30 + 1 month is May 31.

```
select add_months('2008-04-30',1);

add_months
---------------------
2008-05-31 00:00:00
(1 row)
```

- DATEADD: If there are fewer days in the date you are adding to than in the
  result month, the result is the corresponding day of the result month, not the
  last day of that month. For example, April 30 + 1 month is May 30.

```
select dateadd(month,1,'2008-04-30');

date_add
---------------------
2008-05-30 00:00:00
(1 row)
```

The DATEADD function handles the leap year date 02-29 differently when using
dateadd(month, 12,…) or dateadd(year, 1, …).

```
select dateadd(month,12,'2016-02-29');

date_add
---------------------
2017-02-28 00:00:00

select dateadd(year, 1, '2016-02-29');

date_add
---------------------
2017-03-01 00:00:00
```

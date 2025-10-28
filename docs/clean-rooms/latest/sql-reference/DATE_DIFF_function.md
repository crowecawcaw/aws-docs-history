# DATE_DIFF function

DATE_DIFF returns the difference between the date parts of two date or time expressions.

## Syntax

```
date_diff(endDate, startDate)
```

## Arguments

_endDate_

A DATE expression.

_startDate_

A DATE expression.

## Return type

BIGINT

## Examples with a DATE column

The following example finds the difference, in number of weeks, between two literal
date values.

```
select date_diff(week,'2009-01-01','2009-12-31') as numweeks;

numweeks
----------
52
(1 row)
```

The following example finds the difference, in hours, between two literal date
values. When you don't provide the time value for a date, it defaults to
00:00:00.

```
select date_diff(hour, '2023-01-01', '2023-01-03 05:04:03');

date_diff
----------
53
(1 row)
```

The following example finds the difference, in days, between two literal TIMESTAMETZ
values.

```
`Select date_diff(days, 'Jun 1,2008 09:59:59 EST', 'Jul 4,2008 09:59:59 EST')`
 `date_diff
----------
33`
```

The following example finds the difference, in days, between two dates in the same
row of a table.

```
select * from date_table;

start_date |   end_date
-----------+-----------
2009-01-01 | 2009-03-23
2023-01-04 | 2024-05-04
(2 rows)

select date_diff(day, start_date, end_date) as duration from date_table;

duration
---------
      81
     486
(2 rows)
```

The following example finds the difference, in number of quarters, between a literal
value in the past and today's date. This example assumes that the current date is
June 5, 2008. You can name date parts in full or abbreviate them. The default column
name for the DATE_DIFF function is DATE_DIFF.

```
select date_diff(qtr, '1998-07-01', current_date);

date_diff
-----------
40
(1 row)
```

The following example joins the SALES and LISTING tables to calculate how many days
after they were listed any tickets were sold for listings 1000 through 1005. The longest
wait for sales of these listings was 15 days, and the shortest was less than one day (0
days).

```
select priceperticket,
date_diff(day, listtime, saletime) as wait
from sales, listing where sales.listid = listing.listid
and sales.listid between 1000 and 1005
order by wait desc, priceperticket desc;

priceperticket | wait
---------------+------
 96.00         |   15
 123.00        |   11
 131.00        |    9
 123.00        |    6
 129.00        |    4
 96.00         |    4
 96.00         |    0
(7 rows)
```

This example calculates the average number of hours sellers waited for all ticket
sales.

```
select avg(date_diff(hours, listtime, saletime)) as avgwait
from sales, listing
where sales.listid = listing.listid;

avgwait
---------
465
(1 row)
```

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

The following example finds the difference in number of hours between the TIME_VAL
column and a time literal.

```
select date_diff(hour, time_val, time '15:24:45') from time_test;

 date_diff
-----------
        -5
        15
        15
```

The following example finds the difference in number of minutes between two literal
time values.

```
select date_diff(minute, time '20:00:00', time '21:00:00') as nummins;

nummins
----------
60
```

## Examples with a TIMETZ

column

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

The following example finds the differences in number of hours, between a TIMETZ
literal and timetz_val.

```
select date_diff(hours, timetz '20:00:00 PST', timetz_val) as numhours from timetz_test;

numhours
----------
0
-4
1
```

The following example finds the difference in number of hours, between two literal
TIMETZ values.

```
select date_diff(hours, timetz '20:00:00 PST', timetz '00:58:00 EST') as numhours;

numhours
----------
1
```

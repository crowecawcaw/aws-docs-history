Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# MONTHS_BETWEEN function

MONTHS_BETWEEN determines the number of months between two dates.

If the first date is later than the second date, the result is positive; otherwise, the
result is negative.

If either argument is null, the result is NULL.

## Syntax

```
MONTHS_BETWEEN( *date1*, *date2* )
```

## Arguments

_date1_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

_date2_

A column of data type `DATE` or an expression that implicitly
evaluates to a `DATE` type.

## Return type

FLOAT8

The whole number portion of the result is based on the difference between the year
and month values of the dates. The fractional portion of the result is calculated from
the day and timestamp values of the dates and assumes a 31-day month.

If _date1_ and _date2_ both contain the same
date within a month (for example, 1/15/14 and 2/15/14) or the last day of the month (for
example, 8/31/14 and 9/30/14), then the result is a whole number based on the year and
month values of the dates, regardless of whether the timestamp portion matches, if
present.

## Examples

The following example returns the months between 1/18/1969 and 3/18/1969.

```
`select months_between('1969-01-18', '1969-03-18')
as months;`

`months
----------
-2`
```

The following example returns the months between 1/18/1969 and 1/18/1969.

```
`select months_between('1969-01-18', '1969-01-18')
as months;`

`months
----------
0`
```

The following example returns the months between the first and last showings of an event.

```
`select eventname,
min(starttime) as first_show,
max(starttime) as last_show,
months_between(max(starttime),min(starttime)) as month_diff
from event
group by eventname
order by eventname
limit 5;`

`eventname first_show last_show month_diff
---------------------------------------------------------------------------
.38 Special 2008-01-21 19:30:00.0 2008-12-25 15:00:00.0 11.12
3 Doors Down 2008-01-03 15:00:00.0 2008-12-01 19:30:00.0 10.94
70s Soul Jam 2008-01-16 19:30:00.0 2008-12-07 14:00:00.0 10.7
A Bronx Tale 2008-01-21 19:00:00.0 2008-12-15 15:00:00.0 10.8
A Catered Affair 2008-01-08 19:30:00.0 2008-12-19 19:00:00.0 11.35`
```

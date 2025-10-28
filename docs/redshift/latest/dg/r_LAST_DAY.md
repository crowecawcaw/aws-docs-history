Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# LAST_DAY function

LAST_DAY returns the date of the last day of the month that contains
_date_. The return type is always DATE, regardless of the data type
of the _date_ argument.

For more information about retrieving specific date parts, see [DATE_TRUNC function](r_DATE_TRUNC.md "r_DATE_TRUNC.md").

## Syntax

```
LAST_DAY( { *date* | *timestamp* } )
```

## Arguments

_date_ | _timestamp_

A column of data type `DATE` or `TIMESTAMP` or an expression that implicitly
evaluates to a `DATE` or `TIMESTAMP` type.

## Return type

DATE

## Examples

The following example returns the date of the last day in the current month.

```
`select last_day(sysdate);`

 `last_day
------------
 2014-01-31`
```

The following example returns the number of tickets sold for each of the last 7 days
of the month. The values in the SALETIME column are timestamps.

```
`select datediff(day, saletime, last_day(saletime)) as "Days Remaining", sum(qtysold)
from sales
where datediff(day, saletime, last_day(saletime)) < 7
group by 1
order by 1;`

`days remaining | sum
---------------+-------
 0 | 10140
 1 | 11187
 2 | 11515
 3 | 11217
 4 | 11446
 5 | 11708
 6 | 10988
(7 rows)`
```

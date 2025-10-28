Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ADD_MONTHS function

ADD_MONTHS adds the specified number of months to a date or timestamp value or
expression. The [DATEADD](r_DATEADD_function.md "r_DATEADD_function.md") function provides similar functionality.

## Syntax

```
ADD_MONTHS( {*date* | *timestamp*}, *integer*)
```

## Arguments

_date_ | _timestamp_

A column of data type `DATE` or `TIMESTAMP` or an
expression that implicitly evaluates to a `DATE` or
`TIMESTAMP` type. If the date is the last day of the month, or if
the resulting month is shorter, the function returns the last day of the month
in the result. For other dates, the result contains the same day number as the
date expression.

_integer_

A value of data type `INTEGER`. Use a negative number to subtract months
from dates.

## Return type

TIMESTAMP

## Examples

The following query uses the ADD_MONTHS function inside a TRUNC function. The TRUNC
function removes the time of day from the result of ADD_MONTHS. The ADD_MONTHS function
adds 12 months to each value from the CALDATE column. The values in the CALDATE column
are dates.

```
`select distinct trunc(add_months(caldate, 12)) as calplus12,
trunc(caldate) as cal
from date
order by 1 asc;`

 `calplus12 | cal
------------+------------
 2009-01-01 | 2008-01-01
 2009-01-02 | 2008-01-02
 2009-01-03 | 2008-01-03
...
(365 rows)`
```

The following example uses the ADD_MONTHS function to add 1 month to a _timestamp_.

```
`select add_months('2008-01-01 05:07:30', 1);`

`add_months
---------------------
2008-02-01 05:07:30`
```

The following examples demonstrate the behavior when the ADD_MONTHS function operates
on dates with months that have different numbers of days. This example shows how the
function handles adding 1 month to March 31 and adding 1 month to April 30. April has 30
days, so adding 1 month to March 31 results in April 30. May has 31 days, so adding 1
month to April 30 results in May 31.

```
`select add_months('2008-03-31',1);`

`add_months
---------------------
2008-04-30 00:00:00`

`select add_months('2008-04-30',1);`

`add_months
---------------------
2008-05-31 00:00:00`
```

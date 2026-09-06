

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# LAST\_DAY function
<a name="r_LAST_DAY"></a>

LAST\_DAY returns the date of the last day of the month that contains *date*. The return type is always DATE, regardless of the data type of the *date* argument.

For more information about retrieving specific date parts, see [DATE\_TRUNC function](r_DATE_TRUNC.md).

## Syntax
<a name="r_LAST_DAY-synopsis"></a>

```
LAST_DAY( { date | timestamp } )
```

## Arguments
<a name="r_LAST_DAY-arguments"></a>

*date* \| *timestamp*

A column of data type `DATE` or `TIMESTAMP` or an expression that implicitly evaluates to a `DATE` or `TIMESTAMP` type.

## Return type
<a name="r_LAST_DAY-return-type"></a>

DATE

## Examples
<a name="r_LAST_DAY-examples"></a>

The following example returns the date of the last day in the current month.

```
select last_day(sysdate);

  last_day
------------
 2014-01-31
```

The following example returns the number of tickets sold for each of the last 7 days of the month. The values in the SALETIME column are timestamps.

```
select datediff(day, saletime, last_day(saletime)) as "Days Remaining", sum(qtysold)
from sales
where datediff(day, saletime, last_day(saletime)) < 7
group by 1
order by 1;

days remaining |  sum
---------------+-------
             0 | 10140
             1 | 11187
             2 | 11515
             3 | 11217
             4 | 11446
             5 | 11708
             6 | 10988
(7 rows)
```
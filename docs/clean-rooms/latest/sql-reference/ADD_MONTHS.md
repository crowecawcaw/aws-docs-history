

# ADD\_MONTHS function

ADD\_MONTHS adds the specified number of months to a date or timestamp value or expression. The [DATE\_ADD](DATE_ADD_function.md) function provides similar functionality. 

## Syntax
<a name="ADD_MONTHS-synopsis"></a>

```
ADD_MONTHS( {date | timestamp}, integer)
```

## Arguments
<a name="ADD_MONTHS-arguments"></a>

 *date* \| *timestamp*   
A date or timestamp column or an expression that implicitly converts to a date or timestamp. If the date is the last day of the month, or if the resulting month is shorter, the function returns the last day of the month in the result. For other dates, the result contains the same day number as the date expression. 

 *integer*   
A positive or negative integer. Use a negative number to subtract months from dates. 

## Return type
<a name="ADD_MONTHS-return-type"></a>

TIMESTAMP

## Example
<a name="ADD_MONTHS-example"></a>

The following query adds 12 months to each value from the CALDATE column.

```
SELECT DISTINCT ADD_MONTHS(caldate, 12) AS calplus12,
    caldate AS cal
FROM date
ORDER BY 1 ASC;

 calplus12  |    cal
------------+------------
 2009-01-01 | 2008-01-01
 2009-01-02 | 2008-01-02
 2009-01-03 | 2008-01-03
...
(365 rows)
```

The following examples demonstrate the behavior when the ADD\_MONTHS function operates on dates with months that have different numbers of days. 

```
select add_months('2008-03-31',1);

add_months
---------------------
2008-04-30 00:00:00
(1 row)

select add_months('2008-04-30',1);

add_months
---------------------
2008-05-31 00:00:00
(1 row)
```
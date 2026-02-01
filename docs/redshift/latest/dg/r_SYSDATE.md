Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYSDATE function

SYSDATE returns the current date and time in the current session time zone (UTC by
default).

###### Note

SYSDATE returns the start date and time for the current transaction, not for the
start of the current statement.

## Syntax

```
SYSDATE
```

This function requires no arguments.

## Return type

TIMESTAMP

## Examples

The following example uses the SYSDATE function to return the full timestamp for the
current date.

```
`select sysdate;`

`timestamp
----------------------------
2008-12-04 16:10:43.976353`
```

The following example uses the SYSDATE function inside the TRUNC function to return
the current date without the time.

```
`select trunc(sysdate);`

`trunc
------------
2008-12-04`
```

The following query returns sales information for dates that fall between the date
when the query is issued and whatever date is 120 days earlier.

```
`select salesid, pricepaid, trunc(saletime) as saletime, trunc(sysdate) as now
from sales
where saletime between trunc(sysdate)-120 and trunc(sysdate)
order by saletime asc;`

 `salesid | pricepaid | saletime | now
---------+-----------+------------+------------
91535 | 670.00 | 2008-08-07 | 2008-12-05
91635 | 365.00 | 2008-08-07 | 2008-12-05
91901 | 1002.00 | 2008-08-07 | 2008-12-05
...`
```

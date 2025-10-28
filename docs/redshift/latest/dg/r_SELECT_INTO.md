Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SELECT INTO

Selects rows defined by any query and inserts them into a new table. You can specify
whether to create a temporary or a persistent table.

## Syntax

```
[ WITH *with\_subquery* [, ...] ]
SELECT
[ TOP *number* | [ ALL | DISTINCT ]
* | *expression* [ AS *output\_name* ] [, ...] ]
[ EXCLUDE *column\_list* ]
INTO [ TEMPORARY | TEMP ] [ TABLE ] *new\_table*
[ FROM *table\_reference* [, ...] ]
[ WHERE *condition* ]
[ [ START WITH *expression* ] CONNECT BY *expression* ]
[ GROUP BY ALL | *expression* [, ...] ]
[ HAVING *condition* ]
[ QUALIFY *condition* ]
[ { UNION | ALL | INTERSECT | EXCEPT | MINUS } *query* ]
[ ORDER BY *expression* [ ASC | DESC ] ]
[ LIMIT { *number* | ALL } ]
[ OFFSET *start* ]
```

For details about the parameters of this command, see [SELECT](r_SELECT_synopsis.md "r_SELECT_synopsis.md").

## Examples

Select all of the rows from the EVENT table and create a NEWEVENT table:

```
select * into newevent from event;

```

Select the result of an aggregate query into a temporary table called PROFITS:

```
select username, lastname, sum(pricepaid-commission) as profit
into temp table profits
from sales, users
where sales.sellerid=users.userid
group by 1, 2
order by 3 desc;

```

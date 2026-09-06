

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SELECT INTO
<a name="r_SELECT_INTO"></a>

Selects rows defined by any query and inserts them into a new table. You can specify whether to create a temporary or a persistent table. 

## Syntax
<a name="r_SELECT_INTO-synopsis"></a>

```
[ WITH with_subquery [, ...] ]
SELECT
[ TOP number | [ ALL | DISTINCT ]
* | expression [ AS output_name ] [, ...] ]
[ EXCLUDE column_list ]
INTO [ TEMPORARY | TEMP ] [ TABLE ] new_table
[ FROM table_reference [, ...] ]
[ WHERE condition ]
[ [ START WITH expression ] CONNECT BY expression ]
[ GROUP BY ALL | expression [, ...] ]
[ HAVING condition ]
[ QUALIFY condition ]
[ { UNION | ALL | INTERSECT | EXCEPT | MINUS } query ]
[ ORDER BY expression [ ASC | DESC ] ]
[ LIMIT { number | ALL } ]
[ OFFSET start ]
```

 For details about the parameters of this command, see [SELECT](r_SELECT_synopsis.md). 

## Examples
<a name="r_SELECT_INTO-examples"></a>

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
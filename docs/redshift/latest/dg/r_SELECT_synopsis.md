Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SELECT

Returns rows from tables, views, and user-defined functions.

###### Note

The maximum size for a single SQL statement is 16 MB.

## Syntax

```
[ WITH *with\_subquery* [, ...] ]
SELECT
[ TOP *number* | [ ALL | DISTINCT ]
* | *expression* [ AS *output\_name* ] [, ...] ]
[ EXCLUDE *column\_list* ]
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

###### Topics

- [WITH clause](r_WITH_clause.md "r_WITH_clause.md")
- [SELECT list](r_SELECT_list.md "r_SELECT_list.md")
- [EXCLUDE column_list](r_EXCLUDE_list.md "r_EXCLUDE_list.md")
- [FROM clause](r_FROM_clause30.md "r_FROM_clause30.md")
- [WHERE clause](r_WHERE_clause.md "r_WHERE_clause.md")
- [GROUP BY clause](r_GROUP_BY_clause.md "r_GROUP_BY_clause.md")
- [HAVING clause](r_HAVING_clause.md "r_HAVING_clause.md")
- [QUALIFY clause](r_QUALIFY_clause.md "r_QUALIFY_clause.md")
- [UNION, INTERSECT, and EXCEPT](r_UNION.md "r_UNION.md")
- [ORDER BY clause](r_ORDER_BY_clause.md "r_ORDER_BY_clause.md")
- [CONNECT BY clause](r_CONNECT_BY_clause.md "r_CONNECT_BY_clause.md")
- [Subquery examples](r_Subquery_examples.md "r_Subquery_examples.md")
- [Correlated subqueries](r_correlated_subqueries.md "r_correlated_subqueries.md")

# Query Delta Lake tables with SQL

To query a Delta Lake table, use standard SQL `SELECT` syntax:

```
[ WITH with_query [, ...] ]SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition ]
[ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]
[ OFFSET count [ ROW | ROWS ] ]
[ LIMIT [ count | ALL ] ]
```

For more information about `SELECT` syntax, see [SELECT](select.md "select.md") in the Athena documentation.

The Delta Lake format stores the minimum and maximum values per column of each data
file. Athena makes use of this information to enable file skipping on predicates to
eliminate unnecessary files from consideration.

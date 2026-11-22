

# SELECT

The SELECT command returns rows from tables and user-defined functions.

**Unique output column names**

The output column names of a query must be unique. If two columns have the same name, for example when you join tables that share a column name, give one of them an alias with `AS`. Otherwise, the query returns an error that begins with `Duplicate column(s) [{{column_name}}] found in the query output schema`.

The following example joins the `impressions` and `purchases` tables, which both have a `user_id` column. It gives the second `user_id` column an alias so that the output column names are unique:

```
SELECT i.user_id,
    p.user_id AS purchase_user_id
FROM impressions i
    JOIN purchases p
        ON i.user_id = p.user_id
```

The following SELECT SQL commands, clauses, and set operators are supported in AWS Clean Rooms Spark SQL:

**Topics**
+ [SELECT list](sql-function-select-list-spark.md)
+ [WITH clause](WITH_clause.md)
+ [FROM clause](FROM_clause30.md)
+ [JOIN clause](join-clause.md)
+ [WHERE clause](WHERE_clause.md)
+ [VALUES clause](VALUES.md)
+ [GROUP BY clause](GROUP_BY_clause.md)
+ [HAVING clause](HAVING_clause.md)
+ [Set operators](UNION.md)
+ [ORDER BY clause](ORDER_BY_clause.md)
+ [Subquery examples](Subquery_examples.md)
+ [Correlated subqueries](correlated_subqueries.md)

The syntax, arguments, and some examples come from the [Apache Spark SQL Reference](https://spark.apache.org/docs/latest/api/sql/).
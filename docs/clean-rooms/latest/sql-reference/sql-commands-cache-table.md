# CACHE TABLE

The CACHE TABLE command caches an existing table's data or creates and caches a new table
containing query results.

###### Note

The cached data persists for the entire query.

The syntax, arguments, and some examples come from the [Apache Spark SQL Reference](https://spark.apache.org/docs/latest/api/sql/ "https://spark.apache.org/docs/latest/api/sql/").

## Syntax

The CACHE TABLE command supports three syntax patterns:

With AS (without parentheses): Creates and caches a new table based on the query results.

```
CACHE TABLE `cache_table_identifier` AS `query`;
```

With AS and parentheses: Functions similarly to the first syntax but uses parentheses to
explicitly group the query.

```
CACHE TABLE `cache_table_identifier` AS ( `query` );
```

Without AS: Caches an existing table, using the SELECT statement to filter which rows to
cache.

```
CACHE TABLE `cache_table_identifier` `query`;
```

Where:

- All statements should end with a semicolon (;)
- `query` is typically a SELECT statement
- Parentheses around the query are optional with AS
- The AS keyword is optional

## Parameters

_cache_table_identifier_

The name for the cached table. Can include an optional database name qualifier.

_AS_

A keyword used when creating and caching a new table from query results.

_query_

A SELECT statement or other query that defines the data to be cached.

## Examples

In the following examples, the cached table persists for the entire query. After caching,
subsequent queries that reference `cache_table_identifier` will read
from the cached version rather than recomputing or reading from
`sourceTable`. This can improve query performance for frequently
accessed data.

### Create and cache a filtered table from query

results

The first example demonstrates how to create and cache a new table from query results. This
command uses the `AS` keyword without parentheses around the `SELECT`
statement. It creates a new table named '`cache_table_identifier`' containing only
the rows from '`sourceTable`' where the status is '`active'`. It runs the
query, stores the results in the new table, and caches the new table's contents. The original
'`sourceTable`' remains unchanged, and subsequent queries must reference
'`cache_table_identifier`' to use the cached data.

```
CACHE TABLE `cache_table_identifier` AS
    SELECT * FROM `sourceTable`
    WHERE status = 'active';

```

### Cache query results with parenthesized SELECT

statements

The second example demonstrates how to cache the results of a query as a new table with a
specified name (`cache_table_identifier`), using parentheses around the
`SELECT` statement. This command creates a new table named
'`cache_table_identifier`' containing only the rows from '`sourceTable`'
where the status is '`active'`. It runs the query, stores the results in the new
table, and caches the new table's contents. The original '`sourceTable`' remains
unchanged. Subsequent queries must reference '`cache_table_identifier`' to use the
cached data.

```
CACHE TABLE `cache_table_identifier` AS (
    SELECT * FROM `sourceTable`
    WHERE status = 'active'
);

```

### Cache an existing table with filter conditions

The third example demonstrates how to cache an existing table using a different syntax.
This syntax, which omits the '`AS`' keyword and parentheses, typically caches the
specified rows from an existing table named '`cache_table_identifier`' rather than
creating a new table. The `SELECT` statement acts as a filter to determine which rows
to cache.

###### Note

The exact behavior of this syntax varies across database systems. Always verify the
correct syntax for your specific AWS service.

```
CACHE TABLE `cache_table_identifier`
SELECT * FROM `sourceTable`
WHERE status = 'active';

```

# SELECT

Use a SELECT statement to query data.

Syntax

```
**select\_statement** ::=  SELECT  [ JSON ] ( select_clause | '*' )
                      FROM table_name
                      [ WHERE 'where_clause' ]
                      [ ORDER BY 'ordering_clause' ]
                      [ LIMIT (integer | bind_marker) ]
                      [ ALLOW FILTERING ]
**select\_clause**    ::=  selector [ AS identifier ] ( ',' selector [ AS identifier ] )
**selector**         ::=  column_name
                      | term
                      | CAST '(' selector AS cql_type ')'
                      | function_name '(' [ selector ( ',' selector )* ] ')'
**where\_clause**     ::=  relation ( AND relation )*
**relation**         ::=  column_name operator term
                      TOKEN
**operator**         ::=  '=' | '<' | '>' | '<=' | '>=' | IN | CONTAINS | CONTAINS KEY
**ordering\_clause**  ::=  column_name [ ASC | DESC ] ( ',' column_name [ ASC | DESC ] )*


```

Examples

```
SELECT name, id, manager_id FROM "myGSGKeyspace".employees_tbl ;

SELECT JSON name, id, manager_id FROM "myGSGKeyspace".employees_tbl ;
```

For a table that maps JSON-encoded data types to Amazon Keyspaces data types, see [JSON encoding of Amazon Keyspaces data types](cql.md#cql.data-types.JSON "cql.md#cql.data-types.JSON").

Using the `IN` keyword

The `IN` keyword specifies equality for one or more values. It can be
applied to the partition key and the clustering column. Results are returned in the order the
keys are presented in the `SELECT`
statement.

Examples

```
SELECT * from `mykeyspace.mytable` WHERE primary.key1 IN (1,2) and clustering.key1 = 2;
SELECT * from `mykeyspace.mytable` WHERE primary.key1 IN (1,2) and clustering.key1 <= 2;
SELECT * from `mykeyspace.mytable` WHERE primary.key1 = 1 and clustering.key1 IN (1, 2);
SELECT * from `mykeyspace.mytable` WHERE primary.key1 <= 2 and clustering.key1 IN (1, 2) ALLOW FILTERING;
```

For more information about the `IN` keyword and how Amazon Keyspaces processes the
statement, see [Use the IN operator with the SELECT statement in a query in Amazon Keyspaces](in.md "in.md").

Ordering results

The `ORDER BY` clause specifies the sort order of the returned results.
It takes as arguments a list of column names along with the sort order for each
column. You can only specify clustering columns in ordering clauses. Non-clustering
columns are not allowed. The sort order options are `ASC` for ascending
and `DESC` for descending sort order. If the sort order is omitted, the
default ordering of the clustering column is used. For possible sort orders, see
[Order results with ORDER BY in Amazon Keyspaces](ordering-results.md "ordering-results.md").

Example

```
SELECT name, id, division, manager_id FROM "myGSGKeyspace".employees_tbl WHERE id = '012-34-5678' ORDER BY division;
```

When using `ORDER BY` with the `IN` keyword, results are ordered within a page.
Full re-ordering with disabled pagination is
not supported.

TOKEN

You can apply the `TOKEN` function to the `PARTITION KEY`
column in `SELECT` and `WHERE` clauses. With the `TOKEN` function, Amazon Keyspaces returns rows
based on the mapped token value of the `PARTITION_KEY` rather than on the
value of the `PARTITION KEY`.

`TOKEN` relations are not supported with the `IN` keyword.

Examples

```
SELECT TOKEN(id) from `my_table`;

SELECT TOKEN(id) from `my_table` WHERE TOKEN(id) > 100 and TOKEN(id) < 10000;
```

TTL function

You can use the `TTL` function with the `SELECT` statement to retrieve the
expiration time in seconds that is stored for a column. If no `TTL` value is set, the function returns `null`.

Example

```
SELECT TTL(`my_column`) from `my_table`;
```

The `TTL` function can’t be used on multi-cell columns such as collections.

WRITETIME function

You can use the `WRITETIME` function with the `SELECT`
statement to retrieve the timestamp that is stored as metadata for the value of a
column only if the table uses client-side timestamps. For more information, see
[Client-side timestamps in Amazon Keyspaces](client-side-timestamps.md "client-side-timestamps.md").

```
SELECT WRITETIME(`my_column`) from `my_table`;
```

The `WRITETIME` function can’t be used on multi-cell columns such as collections.

###### Note

For compatibility with established Cassandra driver behavior, tag-based authorization policies
are not enforced when you perform operations on system tables by using Cassandra
Query Language (CQL) API calls through Cassandra drivers and developer tools.
For more information, see [Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags").

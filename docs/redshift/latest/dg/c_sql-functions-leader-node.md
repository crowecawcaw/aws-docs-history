Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SQL functions supported on the leader

node

Some Amazon Redshift queries are distributed and run on the compute nodes, and other queries
run exclusively on the leader node.

The leader node distributes SQL to the compute nodes whenever a query references
user-created tables or system tables (tables with an STL or STV prefix and system views
with an SVL or SVV prefix). A query that references only catalog tables (tables with a
PG prefix, such as PG_TABLE_DEF, which reside on the leader node) or that does not
reference any tables, runs exclusively on the leader node.

Some Amazon Redshift SQL functions are supported only on the leader node and are not
supported on the compute nodes. A query that uses a leader-node function must run
exclusively on the leader node, not on the compute nodes, or it will return an
error.

The documentation for each function that must run exclusively on the leader node
includes a note stating that the function will return an error if it references
user-defined tables or Amazon Redshift system tables. See [Leader node–only
functions](c_SQL_functions_leader_node_only.md "c_SQL_functions_leader_node_only.md") for a list of functions that run
exclusively on the leader node.

## Examples

The following examples use the sample TICKIT database. For more information on the
sample database, go to [Sample database](c_sampledb.md "c_sampledb.md").

**CURRENT_SCHEMA**

The CURRENT_SCHEMA function is a leader-node only function. In this example, the
query does not reference a table, so it runs exclusively on the leader node.

```
`select current_schema();`

`current_schema
---------------
public`
```

In the next example, the query references a system catalog table, so it runs
exclusively on the leader node.

```
`select * from pg_table_def
where schemaname = current_schema() limit 1;`

 `schemaname | tablename | column | type | encoding | distkey | sortkey | notnull
------------+-----------+--------+----------+----------+---------+---------+---------
 public | category | catid | smallint | none | t | 1 | t`
```

In the next example, the query references an Amazon Redshift system table that resides on
the compute nodes, so it returns an error.

```
`select current_schema(), userid from users;`

`INFO: Function "current_schema()" not supported.
ERROR: Specified types or functions (one per INFO message) not supported on Amazon Redshift tables.`
```

**SUBSTR**

SUBSTR is also a leader-node only function. In the following example, the query
runs exclusive on the leader node because it does not reference a table.

````
`SELECT SUBSTR('amazon', 5);`

`+--------+
| substr | +--------+
| on | +--------+` ``` In the following example, the query references a table that resides on the compute nodes. This results in an error. ``` `SELECT SUBSTR(catdesc, 1) FROM category LIMIT 1;` `ERROR: SUBSTR() function is not supported (Hint: use SUBSTRING instead)` ``` To successfully run the previous query, use [SUBSTRING](r_SUBSTRING.md "r_SUBSTRING.md"). ``` `SELECT SUBSTRING(catdesc, 1) FROM category LIMIT 1;` `+---------------------------------+
| substring | +---------------------------------+
| National Basketball Association | +---------------------------------+` ``` **FACTORIAL()** FACTORIAL() is a leader-node only function. In the following example, the query runs exclusive on the leader node because it does not reference a table. ``` `SELECT FACTORIAL(5);` `factorial ------------- 120` ``` In the following example, the query references a table that resides on the compute nodes. This results in an error when run using query editor v2. ``` `create table t(a int); insert into t values (5); select factorial(a) from t;` `ERROR: Specified types or functions (one per INFO message) not supported on Redshift tables. Info: Function "factorial(bigint)" not supported.` ```
````

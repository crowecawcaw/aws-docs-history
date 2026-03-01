# Use federated passthrough queries

In Athena, you can run queries on federated data sources using the query language of the
data source itself and push the full query down to the data source for execution. These
queries are called _passthrough queries_. To run passthrough queries,
you use a table function in your Athena query. You include the passthrough query to run on
the data source in one of the arguments to the table function. Pass through queries return a
table that you can analyze using Athena SQL.

## Supported connectors

The following Athena data source connectors support passthrough queries.

- [Azure Data Lake Storage](connectors-adls-gen2.md "connectors-adls-gen2.md")
- [Azure Synapse](connectors-azure-synapse.md "connectors-azure-synapse.md")
- [Cloudera Hive](connectors-cloudera-hive.md "connectors-cloudera-hive.md")
- [Cloudera Impala](connectors-cloudera-impala.md "connectors-cloudera-impala.md")
- [CloudWatch](connectors-cloudwatch.md "connectors-cloudwatch.md")
- [Db2](connectors-ibm-db2.md "connectors-ibm-db2.md")
- [Db2 iSeries](connectors-ibm-db2-as400.md "connectors-ibm-db2-as400.md")
- [DocumentDB](connectors-docdb.md "connectors-docdb.md")
- [DynamoDB](connectors-dynamodb.md "connectors-dynamodb.md")
- [HBase](connectors-hbase.md "connectors-hbase.md")
- [Google BigQuery](connectors-bigquery.md "connectors-bigquery.md")
- [Hortonworks](connectors-hortonworks.md "connectors-hortonworks.md")
- [MySQL](connectors-mysql.md "connectors-mysql.md")
- [Neptune](connectors-neptune.md "connectors-neptune.md")
- [OpenSearch](connectors-opensearch.md "connectors-opensearch.md")
- [Oracle](connectors-oracle.md "connectors-oracle.md")
- [PostgreSQL](connectors-postgresql.md "connectors-postgresql.md")
- [Redshift](connectors-redshift.md "connectors-redshift.md")
- [SAP HANA](connectors-sap-hana.md "connectors-sap-hana.md")
- [Snowflake](connectors-snowflake.md "connectors-snowflake.md")
- [SQL Server](connectors-microsoft-sql-server.md "connectors-microsoft-sql-server.md")
- [Teradata](connectors-teradata.md "connectors-teradata.md")
- [Timestream](connectors-timestream.md "connectors-timestream.md")
- [Vertica](connectors-vertica.md "connectors-vertica.md")

## Considerations and limitations

When using passthrough queries in Athena, consider the following points:

- Query passthrough is supported only for Athena `SELECT` statements
  or read operations.
- Query performance can vary depending on the configuration of the data
  source.
- Query passthrough does not support Lake Formation fine-grained access control.
- Passthrough queries are not supported on data sources that are [registered as a Glue Data
  Catalog](register-connection-as-gdc.md "register-connection-as-gdc.md").

## Syntax

The general Athena query passthrough syntax is as follows.

```
SELECT * FROM TABLE(catalog.system.`function_name`(`arg1` => '`arg1Value`'[, `arg2` => '`arg2Value`', ...]))
```

Note the following:

- **catalog** – The target Athena federated
  connector name or data catalog name.
- **system** – The namespace that contains
  the function. All Athena connector implementations use this namespace.
- **function_name** – The name of the
  function that pushes the passthrough query down to the data source. This is
  often called `query`. The combination
  `catalog.system.function_name` is the full resolution path for
  the function.
- **arg1, arg2, and so on** – Function
  arguments. The user must pass these to the function. In most cases, this is the
  query string that is passed down to the data source.

For most data sources, the first and only argument is `query` followed by
the arrow operator `=>` and the query string.

```
SELECT * FROM TABLE(catalog.system.query(query => 'query string'))
```

For simplicity, you can omit the optional named argument `query` and the
arrow operator `=>`.

```
SELECT * FROM TABLE(catalog.system.query('query string'))
```

You can further simplify the query by removing the `catalog` name if the
query is run within the context of the target catalog.

```
SELECT * FROM TABLE(system.query('query string'))
```

If the data source requires more than the query string, use named arguments in the
order expected by the data source. For example, the expression
``arg1` =>
'`arg1Value`'`contains the first argument and its
 value. The name`arg1` is specific to the data source and can
differ from connector to connector.

```
SELECT * FROM TABLE(
        system.query(
            `arg1` => '`arg1Value`',
            `arg2` => '`arg2Value`',
            `arg3` => '`arg3Value`'
        ));
```

The above can also be simplified by omitting the argument names. However, you must
follow the order of the method's signature. See each connector's documentation for more
information about the function's signature.

```
SELECT * FROM TABLE(catalog.system.query('arg1Value', 'arg2Value', 'arg3Value'))
```

You can run multiple passthrough queries across different Athena connectors by
utilizing the full function resolution path, as in the following example.

```
SELECT c_customer_sk
    FROM TABLE (postgresql.system.query('select * from customer limit 10'))
UNION
SELECT c_customer_sk
    FROM TABLE(dynamodb.system.query('select * from customer')) LIMIT 10
```

You can use passthrough queries as part of a federated view. The same limitations
apply. For more information, see [Query federated views](running-federated-queries.md#running-federated-queries-federated-views "running-federated-queries.md#running-federated-queries-federated-views").

```
CREATE VIEW catalog.database.ViewName AS
    SELECT * FROM TABLE (
        catalog.system.query('query')
    )
```

For information about the exact syntax to use with a particular connector, see the
individual connector documentation.

### Quotation mark usage

Argument values, including the query string that you pass, must be enclosed in
single quotes, as in the following example.

```
SELECT * FROM TABLE(system.query(query => 'SELECT * FROM testdb.persons LIMIT 10'))
```

When the query string is surrounded by double quotes, the query fails. The
following query fails with the error message **`COLUMN_NOT_FOUND: line 1:43:
 Column 'select * from testdb.persons limit 10' cannot be
 resolved`**.

```
SELECT * FROM TABLE(system.query(query => "SELECT * FROM testdb.persons LIMIT 10"))
```

To escape a single quote, add a single quote to the original (for example,
`terry's_group` to `terry''s_group`).

## Examples

The following example query pushes down a query to a data source. The query selects
all columns in the `customer` table, limiting the results to 10.

```
SELECT * FROM TABLE(
        catalog.system.query(
            query => 'SELECT * FROM customer LIMIT 10;'
        ))
```

The following statement runs the same query, but eliminates the optional named
argument `query` and the arrow operator `=>`.

```
SELECT * FROM TABLE(
        catalog.system.query(
            'SELECT * FROM customer LIMIT 10;'
        ))
```

This can also be encapsulated within a federated view for ease of reuse. When used
with a view, you must use the full function resolution path.

```
CREATE VIEW AwsDataCatalog.default.example_view AS
    SELECT * FROM TABLE (
        catalog.system.query('SELECT * FROM customer LIMIT 10;')
    )
```

## Opt out of query passthrough

To disable passthrough queries, add a Lambda environment variable named
`enable_query_passthrough` and set it to `false`.

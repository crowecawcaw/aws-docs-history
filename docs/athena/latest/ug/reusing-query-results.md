# Reuse query results in Athena

When you re-run a query in Athena, you can optionally choose to reuse the last stored query
result. This option can increase performance and reduce costs in terms of the number of
bytes scanned. Reusing query results is useful if, for example, you know that the results
will not change within a given time frame. You can specify a maximum age for reusing query
results. Athena uses the stored result as long as it is not older than the age that you
specify. For more information, see [Reduce cost and improve query performance with Amazon Athena](https://aws.amazon.com/blogs/big-data/reduce-cost-and-improve-query-performance-with-amazon-athena-query-result-reuse/ "https://aws.amazon.com/blogs/big-data/reduce-cost-and-improve-query-performance-with-amazon-athena-query-result-reuse/") in the _AWS
Big Data Blog_.

## Key features

When you enable result reuse for a query, Athena looks for a previous execution of the query within the same workgroup.
If Athena finds a match, it bypasses execution and returns the query result from the previous, matching execution.
You can enable query result reuse on a per query basis.

Athena reuses the last query result when all of the following conditions are true:

- Query strings match as determined by Athena.
- Database and catalog names match.
- The previous result has not expired.
- Query result configuration matches the query result configuration from the previous execution.
- You have access to all tables referenced in the query.
- You have access to the S3 file location where the previous result is stored.

If any of these conditions are not met, Athena runs the query without using the cached results.

## Considerations

and limitations

When using the query result reuse feature, keep in mind the following points:

- Athena reuses query results only within the same workgroup.
- The reuse query results feature respects workgroup configurations. If you
  override the result configuration for a query, the feature is disabled.
- Only queries that produce result sets on Amazon S3 are supported. Statements other than `SELECT` and `EXECUTE` are not supported.
- Apache Hive, Apache Hudi, Apache Iceberg, and Linux Foundation Delta Lake
  tables registered with AWS Glue are supported. External Hive metastores are not
  supported.
- Queries that reference federated catalogs or an external Hive metastore are
  not supported.
- Query result reuse is not supported for Lake Formation governed tables.
- Query result reuse is not supported when the Amazon S3 location of the table source
  is registered as a data location in Lake Formation.
- Tables with row and column permissions are not supported.
- Tables that have fine grained access control (for example, column or row
  filtering) are not supported.
- Any query that references an unsupported table is not eligible for query
  result reuse.
- Athena requires that you have Amazon S3 read permissions for the previously
  generated output file to be reused.
- The reuse query results feature assumes that content of previous result has
  not been modified. Athena does not check the integrity of a previous result
  before using it.
- If the query results from the previous execution have been deleted or moved to
  different location in Amazon S3, the subsequent execution of the same query will not
  reuse the query results.
- Potentially stale results can be returned. Athena does not check for changes in
  source data until the maximum reuse age that you specify has been
  reached.
- If multiple results are available for reuse, Athena uses the latest
  result.
- Queries that use non-deterministic operators or functions like
  `rand()` or `shuffle()` do not use cached results. For
  example, `LIMIT` without `ORDER BY` is non-deterministic
  and not cached, but `LIMIT` with `ORDER BY` is
  deterministic and is cached.
- To use the query result reuse feature with JDBC, the minimum required driver
  version is 2.0.34.1000. For ODBC, the minimum required driver version is
  1.1.19.1002. For driver download information, see [Connect to Amazon Athena with ODBC and JDBC
  drivers](athena-bi-tools-jdbc-odbc.md "athena-bi-tools-jdbc-odbc.md").
- Query result reuse is not supported for queries that use more than one data
  catalog.
- Query result reuse is not supported for queries that include more than 20
  tables.
- For query strings under 100 KB in size, differences in comments and white space are ignored,
  and `INNER JOIN` and `JOIN` are treated as equivalents for the purposes of reusing results.
  Query strings larger than 100 KB must be an exact match to reuse results.
- A query result is considered to be expired if it is older than the maximum age specified, or older than the default of
  60 minutes if a maximum age has not been specified. The maximum age for reusing query results can be specified in minutes,
  hours, or days. The maximum age specifiable is the equivalent of 7 days regardless of the time unit used.
- [Managed query results](managed-results.md "managed-results.md") is not supported.

## How to reuse query results in the

Athena console

To use the feature, enable the **Reuse query results** option in the
Athena query editor.

![Enable Reuse query results in the Athena query editor.](images/reusing-query-results-1.png)

###### To configure the reuse query results feature

1. In the Athena query editor, under the **Reuse query results**
   option, choose the edit icon next to **up to 60 minutes
   ago**.
2. In the **Edit reuse time** dialog box, from the box on the
   right, choose a time unit (minutes, hours, or days).
3. In the box on the left, enter or choose the number of time units that you want
   to specify. The maximum time you can enter is the equivalent of seven days
   regardless of the time unit chosen.

![Configuring the maximum age for reusing query results.](images/reusing-query-results-2.png) 4. Choose **Confirm**.

A banner confirms your configuration change, and the **Reuse query
results** option displays your new setting.

# Create a table from query results (CTAS)

A `CREATE TABLE AS SELECT` (CTAS) query creates a new table in Athena from the
results of a `SELECT` statement from another query. Athena stores data files
created by the CTAS statement in a specified location in Amazon S3. For syntax, see [CREATE TABLE AS](create-table-as.md "create-table-as.md").

`CREATE TABLE AS` combines a `CREATE TABLE` DDL statement with a
`SELECT` DML statement and therefore technically contains both DDL and DML.
However, note that for Service Quotas purposes, CTAS queries in Athena are treated as DML.
For information about Service Quotas in Athena, see [Service Quotas](service-limits.md "service-limits.md").

Use CTAS queries to:

- Create tables from query results in one step, without repeatedly querying raw data
  sets. This makes it easier to work with raw data sets.
- Transform query results and migrate tables into other table formats such as Apache
  Iceberg. This improves query performance and reduces query costs in Athena. For
  information, see [Create Iceberg tables](querying-iceberg-creating-tables.md "querying-iceberg-creating-tables.md").
- Transform query results into storage formats such as Parquet and ORC. This
  improves query performance and reduces query costs in Athena. For information, see
  [Use columnar storage formats](columnar-storage.md "columnar-storage.md").
- Create copies of existing tables that contain only the data you need.

###### Topics

- [Considerations and limitations for CTAS
  queries](ctas-considerations-limitations.md "ctas-considerations-limitations.md")
- [Create CTAS queries](ctas-console.md "ctas-console.md")
- [CTAS examples](ctas-examples.md "ctas-examples.md")
- [Use CTAS and INSERT INTO for ETL](ctas-insert-into-etl.md "ctas-insert-into-etl.md")
- [Work around the 100 partition limit](ctas-insert-into.md "ctas-insert-into.md")

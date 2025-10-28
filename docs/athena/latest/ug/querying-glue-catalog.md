# Query the AWS Glue Data Catalog

Because AWS Glue Data Catalog is used by many AWS services as their central metadata repository,
you might want to query Data Catalog metadata. To do so, you can use SQL queries in Athena. You
can use Athena to query AWS Glue catalog metadata like databases, tables, partitions, and
columns.

To obtain AWS Glue Catalog metadata, you query the `information_schema` database
on the Athena backend. The example queries in this topic show how to use Athena to query AWS Glue
Catalog metadata for common use cases.

## Considerations and

limitations

- Instead of querying the `information_schema` database, it is
  possible to use individual Apache Hive [DDL commands](ddl-reference.md "ddl-reference.md") to extract metadata
  information for specific databases, tables, views, partitions, and columns from
  Athena. However, the output is in a non-tabular format.
- Querying `information_schema` is most performant if you have a
  small to moderate amount of AWS Glue metadata. If you have a large amount of
  metadata, errors can occur.
- You cannot use `CREATE VIEW` to create a view on the
  `information_schema` database.

###### Topics

- [List databases and searching a specified database](querying-glue-catalog-querying-available-databases-including-rdbms.md "querying-glue-catalog-querying-available-databases-including-rdbms.md")
- [List tables in a specified
  database and searching for a table by name](querying-glue-catalog-listing-tables.md "querying-glue-catalog-listing-tables.md")
- [List partitions for a
  specific table](querying-glue-catalog-listing-partitions.md "querying-glue-catalog-listing-partitions.md")
- [List or search columns for
  a specified table or view](querying-glue-catalog-listing-columns.md "querying-glue-catalog-listing-columns.md")
- [List the columns
  that specific tables have in common](querying-glue-catalog-listing-columns-in-common.md "querying-glue-catalog-listing-columns-in-common.md")
- [List all
  columns for all tables](querying-glue-catalog-listing-all-columns-for-all-tables.md "querying-glue-catalog-listing-all-columns-for-all-tables.md")

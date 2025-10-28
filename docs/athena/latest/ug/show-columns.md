# SHOW COLUMNS

Shows only the column names for a single specified table, Athena view, or Data Catalog view. To
obtain more detailed information for Athena views, query the AWS Glue Data Catalog instead. For
information and examples, see the following sections of the [Query the AWS Glue Data Catalog](querying-glue-catalog.md "querying-glue-catalog.md") topic:

- To view column metadata such as data type, see [List or search columns for
  a specified table or view](querying-glue-catalog-listing-columns.md "querying-glue-catalog-listing-columns.md").
- To view all columns for all tables in a specific database in
  `AwsDataCatalog`, see [List or search columns for
  a specified table or view](querying-glue-catalog-listing-columns.md "querying-glue-catalog-listing-columns.md").
- To view all columns for all tables in all databases in
  `AwsDataCatalog`, see [List all
  columns for all tables](querying-glue-catalog-listing-all-columns-for-all-tables.md "querying-glue-catalog-listing-all-columns-for-all-tables.md").
- To view the columns that specific tables in a database have in common, see [List the columns
  that specific tables have in common](querying-glue-catalog-listing-columns-in-common.md "querying-glue-catalog-listing-columns-in-common.md").
  For Data Catalog views, the output of the statement is controlled by Lake Formation access control and
  shows only the columns that the caller has access to.

## Synopsis

```
SHOW COLUMNS {FROM|IN} `database_name`.`table_or_view_name`
```

```
SHOW COLUMNS {FROM|IN} `table_or_view_name` [{FROM|IN} `database_name`]
```

The `FROM` and `IN` keywords can be used interchangeably. If
`table_or_view_name` or
`database_name` has special characters like hyphens,
surround the name with back quotes (for example, ``my-database`.`my-table``).
Do not surround the `table_or_view_name` or
`database_name` with single or double quotes. Currently,
the use of `LIKE` and pattern matching expressions is not supported.

## Examples

The following equivalent examples show the columns from the `orders` table
in the `customers` database. The first two examples assume that
`customers` is the current database.

```
SHOW COLUMNS FROM orders
```

```
SHOW COLUMNS IN orders
```

```
SHOW COLUMNS FROM customers.orders
```

```
SHOW COLUMNS IN customers.orders
```

```
SHOW COLUMNS FROM orders FROM customers
```

```
SHOW COLUMNS IN orders IN customers
```

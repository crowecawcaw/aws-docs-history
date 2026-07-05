Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Use the Amazon Redshift driver metadata API for applications and tools

For applications and tools that connect to Amazon Redshift, such as a business
intelligence tool or query editor, we recommend that
you use the driver metadata API provided by the Amazon Redshift
[JDBC 2.x](jdbc20-install.md "jdbc20-install.md"),
[ODBC 2.x](odbc20-install.md "odbc20-install.md"), or
[Python](python-redshift-driver.md "python-redshift-driver.md")
drivers to discover metadata about your data warehouse objects,
including databases, schemas, tables, columns, and data types. As alternatives, you
can use Amazon Redshift `SHOW` commands.

Use the driver metadata API for the following benefits:

- **Specification-compliant**. The JDBC and
  ODBC drivers implement standard metadata interfaces (`DatabaseMetaData`
  in JDBC, `SQLTables` and `SQLColumns` in ODBC). Since
  Python's DB-API (PEP 249) does not define a metadata API specification,
  the Amazon Redshift Python driver follows the JDBC DatabaseMetaData specification,
  providing equivalent methods such as `get_tables()`,
  `get_columns()`, and `get_schemas()`. These APIs follow
  well-defined specifications, so your integration code is portable. As
  Amazon Redshift evolves its internal system tables, your application
  doesn't need to change.
- **Performance-optimized**. The driver
  metadata API is optimized to return metadata efficiently. AWS continues to
  invest in driver metadata API performance.
- **Forward-compatible**. Amazon Redshift
  adheres to the JDBC, ODBC, and Python connector specifications. When you
  code against these standard APIs, your application is protected from changes
  to the underlying system catalog structure.

## Example: Using JDBC DatabaseMetaData.getTables() to retrieve table metadata

```
DatabaseMetaData dbmd = connection.getMetaData();

// getTables(catalog, schemaPattern, tableNamePattern, types)
//   catalog:          "test" — filters to the database named "test"
//   schemaPattern:    "test_pattern" — filters schemas matching this pattern (supports SQL wildcards % and _)
//   tableNamePattern: null — no filter, returns all table names
//   types:            {"TABLE", "EXTERNAL TABLE"} — only return regular tables and external tables
ResultSet rs = dbmd.getTables("test", "test_pattern", null, new String[] {"TABLE", "EXTERNAL TABLE"});
```

## Example: Using Python cursor.get\_columns() to retrieve column metadata

```
cursor: redshift_connector.Cursor = conn.cursor()

# get_columns(catalog, schema_pattern, table_name_pattern, column_name_pattern)
#   catalog:             'test' — filters to the database named "test"
#   schema_pattern:      'test_pattern' — filters schemas matching this pattern (supports SQL wildcards % and _)
#   table_name_pattern:  'testabc' — filters to the table named "testabc"
#   column_name_pattern: '%' — wildcard, returns all columns in the matching table
result: tuple = cursor.get_columns('test', 'test_pattern', 'testabc', '%')
```

## Example: Using ODBC SQLPrimaryKeys() to retrieve primary key metadata

```
// SQLPrimaryKeys(hstmt, catalog, catalog_len, schema, schema_len, table, table_len)
//   catalog: "test"         — filters to the database named "test"
//   schema:  "test_schema"  — filters to the schema named "test_schema"
//   table:   "test_table"   — retrieves primary key columns for this table
// Note: Unlike getTables/getColumns, SQLPrimaryKeys does NOT support wildcard patterns.
retcode = SQLPrimaryKeys(hstmt, (SQLCHAR *)"test", SQL_NTS, (SQLCHAR *)"test_schema", SQL_NTS, (SQLCHAR *)"test_table", SQL_NTS);

while (SQL_SUCCEEDED(retcode = SQLFetch(hstmt))) {
    for (i = 1; i <= columns; i++) {
        retcode = SQLGetData(hstmt, i, SQL_C_CHAR, buf, sizeof(buf), &indicator);
    }
}
```

## Example: Using ODBC SQLTables() to list databases and schemas

The ODBC API does not provide separate functions for listing catalogs or
schemas. Instead, you use special calling conventions of
`SQLTables()` to retrieve this information.

**To list all databases (catalogs)**

Call `SQLTables()` with `CatalogName` set to
`SQL_ALL_CATALOGS`. Set `SchemaName` and
`TableName` to empty strings. The result set returns valid values
only in the `TABLE_CAT` column. All other columns contain
NULLs.

```
// List all catalogs (databases) available on the data source.
retcode = SQLTables(hstmt,
    (SQLCHAR *)SQL_ALL_CATALOGS, SQL_NTS, // CatalogName = "%" (SQL_ALL_CATALOGS)
    (SQLCHAR *)"", 0,                     // SchemaName = "" (empty string)
    (SQLCHAR *)"", 0,                     // TableName  = "" (empty string)
    NULL, 0);                             // TableType  = NULL (not filtered)
```

**To list all schemas**

Call `SQLTables()` with `SchemaName` set to
`SQL_ALL_SCHEMAS`. Set `CatalogName` and
`TableName` to empty strings.

```
// List all schemas available on the data source.
retcode = SQLTables(hstmt,
    (SQLCHAR *)"", 0,                     // CatalogName = "" (empty string)
    (SQLCHAR *)SQL_ALL_SCHEMAS, SQL_NTS,  // SchemaName = "%" (SQL_ALL_SCHEMAS)
    (SQLCHAR *)"", 0,                     // TableName  = "" (empty string)
    NULL, 0);                             // TableType  = NULL (not filtered)
```

###### Note

The ODBC specification defines only `TABLE_SCHEM` as valid
for schema enumeration. Amazon Redshift also populates `TABLE_CAT`
because it supports cross-database metadata discovery, and each schema is
scoped to a specific database.

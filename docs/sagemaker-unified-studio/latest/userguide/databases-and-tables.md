# Catalogs, databases, and tables

If your `Connection` is of the `LAKEHOUSE` or
`IAM` type, you can retrieve catalogs, databases, and tables
within a project.

## Catalogs

If your Connection is of the `LAKEHOUSE` or `IAM` type, you can retrieve a list of catalogs, or a single catalog by providing its id.

```

conn_catalogs: List[Catalog] = proj.connection().catalogs
my_default_catalog: Catalog = proj.connection().catalog()
my_catalog: Catalog = proj.connection().catalog("1234567890:catalog1/sub_catalog")
proj.connection("<lakehouse_connection_name>").catalogs

```

Each `Catalog` object has several properties that can provide information about the catalog.

```

my_catalog.name
my_catalog.id
my_catalog.type
my_catalog.spark_catalog_name
my_catalog.resource_arn

```

## Databases

You can retrieve a list of databases or a single database within a catalog
by providing its name.

```

my_catalog: Catalog
catalog_dbs: List[Database] = my_catalog.databases
my_db: Database = my_catalog.database("my_db")

```

Each `Database` object has several properties that can provide
information about the database.

```

my_db.name
my_db.catalog_id
my_db.location_uri
my_db.project_id
my_db.domain_id

```

## Tables

You can also retrieve a list of tables or a specific table within a
`Database`.

```

my_db_tables: List[Table] = my_db.tables
my_table: Table = my_db.table("my_table")

```

Each `Table` object has several properties that can provide
information about the table.

```

my_table.name
my_table.database_name
my_table.catalog_id
my_table.location

```

You can also retrieve a list of the columns within a table.
`Column` contains the column name and the data type of the
column.

```

my_table_columns: List[Column] = my_table.columns
col_0: Column = my_table_columns[0]
col_0.name
col_0.type

```

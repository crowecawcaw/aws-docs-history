

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Connecting to consumer databases in Amazon Redshift
<a name="database-direct-connect"></a>

With a direct connection to a datashare database, you can directly connect to a database created from a datashare in the same way as you can connect to any other type of Amazon Redshift database. For example, you can connect to a database created from a datashare using JDBC or ODBC drivers, the Amazon Redshift query editor v2, or any other tool that can connect to an Amazon Redshift database. For more information, see [Connecting to an Amazon Redshift data warehouse using SQL client tools](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-to-cluster.html).

## Accessing shared data
<a name="database-shared-data"></a>

When you connect to a database created from a datashare, you can query the shared objects using two-part notation (`{{schema_name}}.{{table_name}}`). If the table can be found in the consumer database search path, you can also use one-part notation (`{{table_name}}`). 

If you want to perform cross-database queries, you can use three-part notation (`{{consumer_database_name}}.{{schema_name}}.{{table_name}}`). These queries can reference shared objects from other consumer database on the cluster, or local objects from local databases. They can also reference both local databases and data shared from other clusters within the same query.

**Note**  
A database that is created from a datashare doesn't have a local catalog. Therefore, any queries that access local catalog tables, such as `pg_class`, return an empty result.

## Accessing metadata for shared objects
<a name="database-metadata-shared"></a>

To help cluster administrators discover shared objects in the consumer database, Amazon Redshift provides a set of metadata views and SHOW commands that list the metadata for these objects. When you connect to a consumer database, these metadata views and commands don't support cross-database metadata discovery. They only return metadata for the shared objects in the datashare that are associated with the connected database.

Use SHOW SCHEMAS to view a list of the shared schemas in the datashare associated with the connected database. For more information, see [SHOW SCHEMAS](r_SHOW_SCHEMAS.md).

Use SHOW TABLES to view a list of the tables in a shared schema from the datashare associated with the connected database. For more information, see [SHOW TABLES](r_SHOW_TABLES.md).

Use SHOW COLUMNS to view a list of the columns from a shared table in the datashare associated with the connected database. For more information, see [SHOW COLUMNS](r_SHOW_COLUMNS.md).

Use SVV\_ALL\_SCHEMAS to view a list of the shared schemas in the datashare associated with the connected database. For more information, see [SVV\_ALL\_SCHEMAS](r_SVV_ALL_SCHEMAS.md).

Use SVV\_ALL\_TABLES to view a list of the shared tables in the datashare associated with the connected database. For more information, see [SVV\_ALL\_TABLES](r_SVV_ALL_TABLES.md).

Use SVV\_ALL\_COLUMNS to view a list of the shared columns in the datashare associated with the connected database. For more information, see [SVV\_ALL\_COLUMNS](r_SVV_ALL_COLUMNS.md).

## Integrating Amazon Redshift data sharing with business intelligence tools
<a name="database-integration"></a>

To integrate data sharing with business intelligence (BI) tools, we recommend that you use the Amazon Redshift JDBC or ODBC drivers. Amazon Redshift JDBC and ODBC drivers support the `GetCatalogs` API operation in the drivers. This operation returns a list of all databases, including those created from datashares. 

The drivers also support downstream operations, such as `GetSchemas` and GetTables, that return data from all the databases that `GetCatalogs` returns. The drivers provide this support even when you don't explicitly specify the catalog in the call. For more information on JDBC or ODBC drivers, see [Configuring connections](https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html) in the *Amazon Redshift Management Guide*.

The Amazon Redshift query editor v2 includes consumer databases in its connection switching interface. However, most tools exclude these databases and only include local cluster databases as connectable databases.

**Note**  
A new system database named `sys:internal` was added for internal maintenance. Some tools include this system database as a connectable database. However, you can't connect to it or run queries against its objects.


# Understand federated table name qualifiers
<a name="tables-qualifiers"></a>

Athena uses the following terms to refer to hierarchies of data objects:
+ **Data source** – a group of databases
+ **Database** – a group of tables
+ **Table** – data organized as a group of rows or columns

Sometimes these objects are also referred to with alternate but equivalent names such as the following:
+ A data source is sometimes referred to as a catalog.
+ A database is sometimes referred to as a schema.

## Terms in federated data sources
<a name="tables-qualifiers-terms-in-federated-data-sources"></a>

When you query federated data sources, note that the underlying data source might not use the same terminology as Athena. Keep this distinction in mind when you write your federated queries. The following sections describe how data object terms in Athena correspond to those in federated data sources.

### Amazon Redshift
<a name="tables-qualifiers-redshift"></a>

An Amazon Redshift *database* is a group of Redshift *schemas* that contains a group of Redshift *tables*.



| Athena | Redshift | 
| --- | --- | 
| Redshift data source | A Redshift connector Lambda function configured to point to a Redshift database. | 
| data\_source.database.table | database.schema.table | 

Example query

```
SELECT * FROM 
{{Athena_Redshift_connector_data_source}}.{{Redshift_schema_name}}.{{Redshift_table_name}}
```

For more information about this connector, see [Amazon Athena Redshift connector](connectors-redshift.md).

### Cloudera Hive
<a name="tables-qualifiers-cloudera-hive"></a>

An Cloudera Hive *server* or *cluster* is a group of Cloudera Hive *databases* that contains a group of Cloudera Hive *tables*.



| Athena | Hive | 
| --- | --- | 
| Cloudera Hive data source | Cloudera Hive connector Lambda function configured to point to a Cloudera Hive server. | 
| data\_source.database.table | server.database.table | 

Example query

```
SELECT * FROM 
{{Athena_Cloudera_Hive_connector_data_source}}.{{Cloudera_Hive_database_name}}.{{Cloudera_Hive_table_name}}
```

For more information about this connector, see [Amazon Athena Cloudera Hive connector](connectors-cloudera-hive.md).

### Cloudera Impala
<a name="tables-qualifiers-cloudera-impala"></a>

An Impala *server* or *cluster* is a group of Impala *databases* that contains a group of Impala *tables*.



| Athena | Impala | 
| --- | --- | 
| Impala data source | Impala connector Lambda function configured to point to an Impala server. | 
| data\_source.database.table | server.database.table | 

Example query

```
SELECT * FROM 
{{Athena_Impala_connector_data_source}}.{{Impala_database_name}}.{{Impala_table_name}}
```

For more information about this connector, see [Amazon Athena Cloudera Impala connector](connectors-cloudera-impala.md).

### MySQL
<a name="tables-qualifiers-mysql"></a>

A MySQL *server* is a group of MySQL *databases* that contains a group of MySQL *tables*.



| Athena | MySQL | 
| --- | --- | 
| MySQL data source | MySQL connector Lambda function configured to point to a MySQL server. | 
| data\_source.database.table | server.database.table | 

Example query

```
SELECT * FROM 
{{Athena_MySQL_connector_data source}}.{{MySQL_database_name}}.{{MySQL_table_name}}
```

For more information about this connector, see [Amazon Athena MySQL connector](connectors-mysql.md).

### Oracle
<a name="tables-qualifiers-oracle"></a>

An Oracle *server* (or *database*) is a group of Oracle *schemas* that contains a group of Oracle *tables*.



| Athena | Oracle | 
| --- | --- | 
| Oracle data source | Oracle connector Lambda function configured to point to an Oracle server. | 
| data\_source.database.table | server.schema.table | 

Example query

```
SELECT * FROM 
{{Athena_Oracle_connector_data_source}}.{{Oracle_schema_name}}.{{Oracle_table_name}}
```

For more information about this connector, see [Amazon Athena Oracle connector](connectors-oracle.md).

### Postgres
<a name="tables-qualifiers-postgres"></a>

A Postgres *server* (or *cluster*) is a group of Postgres *databases*. A Postgres *database* is a group of Postgres *schemas* that contains a group of Postgres *tables*.



| Athena | Postgres | 
| --- | --- | 
| Postgres data source | Postgres connector Lambda function configured to point to a Postgres server and database. | 
| data\_source.database.table | server.database.schema.table | 

Example query

```
SELECT * FROM 
{{Athena_Postgres_connector_data_source}}.{{Postgres_schema_name}}.{{Postgres_table_name}}
```

For more information about this connector, see [Amazon Athena PostgreSQL connector](connectors-postgresql.md).
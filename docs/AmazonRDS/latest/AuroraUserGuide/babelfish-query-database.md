# Getting information from the Babelfish

system catalog

You can obtain information about the database objects that are stored in your
Babelfish cluster by querying many of the same system views as used in SQL
Server. Each new release of Babelfish adds support for more system views. For a
list of available views currently available, see the [SQL Server system catalog views](#system-catalog-table "#system-catalog-table") table.

These system views provide information from the system catalog
(`sys.schemas`). In the case of Babelfish, these views contain
both SQL Server and PostgreSQL system schemas. To query Babelfish for system
catalog information, you can use the TDS port or the PostgreSQL port, as shown in the
following examples.

- Query the T-SQL port using `sqlcmd` or
  another SQL Server client.

```
`1>` SELECT * FROM sys.schemas
`2>` GO
```

This query returns SQL Server and Aurora PostgreSQL system schemas, as shown in
the following.

```
name
---------------------------------------------------------
demographic_dbo
public
sys
master_dbo
tempdb_dbo
...
```

- Query the PostgreSQL port using `psql` or
  `pgAdmin`. This example uses the `psql`
  list schemas metacommand (`\dn`):

```
`babelfish_db=>` \dn
```

The query returns the same result set as that returned by `sqlcmd`
on the T-SQL port.

```
        List of schemas
             Name
------------------------------

 demographic_dbo

 public
 sys
 master_dbo
 tempdb_dbo
...

```

## SQL Server system

catalogs available in Babelfish

In the following table you can find the SQL Server views currently implemented in
Babelfish. For more information about the system catalogs in SQL Server, see
[System Catalog Views (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/catalog-views-transact-sql?view=sql-server-ver16") in Microsoft documentation.

| View name                             | Description or Babelfish limitation (if any)                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sys.all_columns`                     | All columns in all tables and views                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sys.all_objects`                     | All objects in all schemas                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `sys.all_sql_modules`                 | The union of `sys.sql_modules` and<br>`sys.system_sql_modules`                                                                                                                                                                                                                                                                                                                                                                              |
| `sys.all_views`                       | All views in all schemas                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `sys.columns`                         | All columns in user-defined tables and views                                                                                                                                                                                                                                                                                                                                                                                                |
| `sys.configurations`                  | Babelfish support limited to a single read-only<br>configuration.                                                                                                                                                                                                                                                                                                                                                                           |
| `sys.data_spaces`                     | Contains a row for each data space. This can be a<br>filegroup, partition scheme, or FILESTREAM data<br>filegroup.                                                                                                                                                                                                                                                                                                                          |
| `sys.database_files`                  | A per-database view that contains one row for each file of<br>a database as stored in the database itself.                                                                                                                                                                                                                                                                                                                                  |
| `sys.database_mirroring`              | For information, see [sys.database_mirroring](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-mirroring-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-mirroring-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                              |
| `sys.database_principals`             | For information, see [sys.database_principals](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-principals-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-principals-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                           |
| `sys.database_role_members`           | For information, see [sys.database_role_members](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-role-members-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-database-role-members-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                     |
| `sys.databases`                       | All databases in all schemas                                                                                                                                                                                                                                                                                                                                                                                                                |
| `sys.dm_exec_connections`             | For information, see [sys.dm_exec_connections](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-exec-connections-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-exec-connections-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                     |
| `sys.dm_exec_sessions`                | For information, see [sys.dm_exec_sessions](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-exec-sessions-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-exec-sessions-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                              |
| `sys.dm_hadr_database_replica_states` | For information, see [sys.dm_hadr_database_replica_states](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-hadr-database-replica-states-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-hadr-database-replica-states-transact-sql?view=sql-server-ver16") in Microsoft<br>Transact-SQL documentation. |
| `sys.dm_os_host_info`                 | For information, see [sys.dm_os_host_info](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-host-info-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-host-info-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                 |
| `sys.endpoints`                       | For information, see [sys.endpoints](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-endpoints-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-endpoints-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                                         |
| `sys.indexes`                         | For information, see [sys.indexes](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-indexes-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-indexes-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                                               |
| `sys.languages`                       | For information, see [sys.languages](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-fulltext-languages-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-fulltext-languages-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                       |
| `sys.schemas`                         | All schemas                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sys.server_principals`               | All logins and roles                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `sys.sql_modules`                     | For information, see [sys.sql_modules](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-sql-modules-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-sql-modules-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                                   |
| `sys.sysconfigures`                   | Babelfish support limited to a single read-only<br>configuration.                                                                                                                                                                                                                                                                                                                                                                           |
| `sys.syscurconfigs`                   | Babelfish support limited to a single read-only<br>configuration.                                                                                                                                                                                                                                                                                                                                                                           |
| `sys.sysprocesses`                    | For information, see [sys.sysprocesses](https://docs.microsoft.com/en-us/sql/relational-databases/system-compatibility-views/sys-sysprocesses-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-compatibility-views/sys-sysprocesses-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                    |
| `sys.system_sql_modules`              | For information, see [sys.system_sql_modules](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-system-sql-modules-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-system-sql-modules-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                              |
| `sys.table_types`                     | For information, see [sys.table_types](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-table-types-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-table-types-transact-sql?view=sql-server-ver16") in Microsoft Transact-SQL<br>documentation.                                                                                   |
| `sys.tables`                          | All tables in a schema                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `sys.xml_schema_collections`          | For information, see [sys.xml_schema_collections](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-xml-schema-collections-transact-sql?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-xml-schema-collections-transact-sql?view=sql-server-ver16") in Microsoft<br>Transact-SQL documentation.                                                  |

PostgreSQL implements system catalogs that are similar to the SQL Server object
catalog views. For a complete list of system catalogs, see [System
Catalogs](https://www.postgresql.org/docs/current/catalogs.html "https://www.postgresql.org/docs/current/catalogs.html") in the PostgreSQL documentation.

## DDL exports supported by Babelfish

From Babelfish 2.4.0 and 3.1.0 versions, Babelfish supports DDL exports using
various tools. For example, you can use this functionality from SQL Server Management Studio
(SSMS) to generate the data definition scripts for various objects in a Babelfish for Aurora PostgreSQL
database. You can then use the generated DDL commands in this script to create the same
objects in another Babelfish for Aurora PostgreSQL or SQL Server database.

Babelfish supports DDL exports for the following objects in the specified
versions.

| List of objects          | 2.4.0 | 3.1.0 |
| ------------------------ | ----- | ----- |
| User tables              | Yes   | Yes   |
| Primary keys             | Yes   | Yes   |
| Foreign keys             | Yes   | Yes   |
| Unique constraints       | Yes   | Yes   |
| Indexes                  | Yes   | Yes   |
| Check constraints        | Yes   | Yes   |
| Views                    | Yes   | Yes   |
| Stored procedures        | Yes   | Yes   |
| User-defined functions   | Yes   | Yes   |
| Table-valued functions   | Yes   | Yes   |
| Triggers                 | Yes   | Yes   |
| User Defined Datatypes   | No    | No    |
| User Defined Table Types | No    | No    |
| Users                    | No    | No    |
| Logins                   | No    | No    |
| Sequences                | No    | No    |
| Roles                    | No    | No    |

### Limitations with the exported DDLs

- Use escape hatches before recreating the objects with
  the exported DDLs – Babelfish doesn't support
  all the commands in the exported DDL script. Use escape hatches to avoid errors
  caused when recreating the objects from the DDL commands in Babelfish.
  For more information on escape hatches, see [Managing Babelfish error handling with escape hatches](babelfish-strict.md "babelfish-strict.md")
- Objects containing CHECK constraints with explicit
  COLLATE clauses – The scripts with these objects generated
  from a SQL Server database have different but equivalent collations as in the
  Babelfish database. For example, a few collations, such as
  sql_latin1_general_cp1_cs_as, sql_latin1_general_cp1251_cs_as, and
  latin1_general_cs_as are generated as latin1_general_cs_as, which is the closest
  Windows collation.

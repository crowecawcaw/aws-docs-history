# Required permissions

When you connect to a Amazon Quick Sight data source that requires a user name, the user name must
have `SELECT` permissions on some system tables. These permissions allow Amazon Quick Sight
to do things such as discover table schemas and estimate table size.

The following table identifies the tables that the account must have `SELECT`
permissions for, depending on the type of database you are connecting to. These requirements
apply for all database instances you connect to, regardless of their environment. In other
words, they apply whether your database instances are on-premises, in Amazon RDS, in Amazon EC2, or
elsewhere.

| Instance type        | Tables                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Aurora        | `INFORMATION_SCHEMA.STATISTICS` `INFORMATION_SCHEMA.TABLES`                                                  |
| Amazon Redshift      | `pg_stats` `pg_class` `pg_namespace`                                                                         |
| MariaDB              | `INFORMATION_SCHEMA.STATISTICS` `INFORMATION_SCHEMA.TABLES`                                                  |
| Microsoft SQL Server | `DBCC SHOW_STATISTICS` `sp_statistics`                                                                       |
| MySQL                | `INFORMATION_SCHEMA.STATISTICS` INFORMATION_SCHEMA.TABLES                                                    |
| **Oracle**           | DBA_TAB_COLS ALL_TABLES dba_segments all_segments user_segments                                              |
| PostgreSQL           | `pg_stats` `pg_class` `pg_namespace`                                                                         |
| ServiceNow           | `sys_dictionary (column metadata)` `sys_db_object (table metadata)` `sys_glide_object (field type metadata)` | ###### Note If you are using MySQL or PostgreSQL, verify that you are connecting from an allowed host or IP address. For more detail, see [Database configuration requirements for self-administered instances](configure-access.md#database-configuration-requirements "configure-access.md#database-configuration-requirements"). |

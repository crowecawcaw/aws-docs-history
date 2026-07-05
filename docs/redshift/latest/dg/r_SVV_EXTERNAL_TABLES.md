Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_EXTERNAL\_TABLES

Use SVV\_EXTERNAL\_TABLES to view details for external tables; for more information, see
[CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").
Use SVV\_EXTERNAL\_TABLES also for cross-database queries to view metadata on all tables
on unconnected databases that users have access to.

SVV\_EXTERNAL\_TABLES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW TABLES](r_SHOW_TABLES.md "r_SHOW_TABLES.md") command for table discovery. SHOW TABLES works consistently across
local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name              | Data type | Description                                                                                                                  |
| ------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| redshift\_database\_name | text      | The name of the local Amazon Redshift database.                                                                              |
| schemaname               | text      | The name of the Amazon Redshift external schema for the<br>external table.                                                   |
| tablename                | text      | The name of the external table.                                                                                              |
| tabletype                | text      | The type of table. Some values are TABLE, VIEW,<br>MATERIALIZED VIEW, or " " empty string that represents no<br>information. |
| location                 | text      | The location of the table.                                                                                                   |
| input\_format            | text      | The input format                                                                                                             |
| output\_format           | text      | The output format.                                                                                                           |
| serialization\_lib       | text      | The serialization library.                                                                                                   |
| serde\_parameters        | text      | SerDe parameters.                                                                                                            |
| compressed               | integer   | A value that indicates whether the table is<br>compressed; `1` indicates compressed,<br>`0` indicates not compressed.        |
| parameters               | text      | Table properties.                                                                                                            |

## Example

The following example shows details svv\_external\_tables with a predicate on the
external schema used by a federated query.

```
select schemaname, tablename from svv_external_tables where schemaname = 'apg_tpch';
schemaname  | tablename
------------+-----------
apg_tpch    | customer
apg_tpch    | lineitem
apg_tpch    | nation
apg_tpch    | orders
apg_tpch    | part
apg_tpch    | partsupp
apg_tpch    | region
apg_tpch    | supplier
(8 rows)

```

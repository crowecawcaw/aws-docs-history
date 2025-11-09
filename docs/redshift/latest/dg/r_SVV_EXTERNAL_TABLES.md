Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_EXTERNAL_TABLES

Use SVV_EXTERNAL_TABLES to view details for external tables; for more information, see
[CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").
Use SVV_EXTERNAL_TABLES also for cross-database queries to view metadata on all tables
on unconnected databases that users have access to.

SVV_EXTERNAL_TABLES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type | Description                                                                                                                  |
| ---------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| redshift_database_name | text      | The name of the local Amazon Redshift database.                                                                              |
| schemaname             | text      | The name of the Amazon Redshift external schema for the<br>external table.                                                   |
| tablename              | text      | The name of the external table.                                                                                              |
| tabletype              | text      | The type of table. Some values are TABLE, VIEW,<br>MATERIALIZED VIEW, or " " empty string that represents no<br>information. |
| location               | text      | The location of the table.                                                                                                   |
| input_format           | text      | The input format                                                                                                             |
| output_format          | text      | The output format.                                                                                                           |
| serialization_lib      | text      | The serialization library.                                                                                                   |
| serde_parameters       | text      | SerDe parameters.                                                                                                            |
| compressed             | integer   | A value that indicates whether the table is<br>compressed; `1` indicates compressed,<br>`0` indicates not compressed.        |
| parameters             | text      | Table properties.                                                                                                            |

## Example

The following example shows details svv_external_tables with a predicate on the
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

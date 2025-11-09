Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_EXTERNAL_SCHEMAS

Use SVV_EXTERNAL_SCHEMAS to view information about external schemas. For more
information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

SVV_EXTERNAL_SCHEMAS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name  | Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| esoid        | oid       | External schema ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| eskind       | smallint  | The type of the external catalog for the external<br>schema: 1 indicates a data catalog, 2 indicates a Hive metastore, 3<br>indicates a federated query to Aurora PostgreSQL or Amazon RDS PostgreSQL,<br>4 indicates a schema for a local Amazon Redshift database, 5 indicates a schema for a remote Amazon Redshift database,<br>6 indicates a schema for a system table, 8 indicates a schema for remote MySQL databases, 9 indicates a schema for an Amazon Kinesis data stream,<br>and 10 indicates an Amazon Managed Streaming for Apache Kafka data stream. |
| schemaname   | name      | External schema name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| esowner      | integer   | User ID of the external schema owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| databasename | text      | External database name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| esoptions    | text      | External schema options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Example

The following example shows details for external schemas.

```
select * from svv_external_schemas;

esoid  | eskind | schemaname | esowner | databasename | esoptions
-------+--------+------------+---------+--------------+-------------------------------------------------------------
100133 |      1 | spectrum   |     100 | redshift     | {"IAM_ROLE":"arn:aws:iam::123456789012:role/mySpectrumRole"}

```

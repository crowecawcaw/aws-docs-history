Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_REDSHIFT\_DATABASES

Use SVV\_ REDSHIFT\_DATABASES to view a list of all the databases that a user has access
to. This includes the databases on the cluster and the databases created from datashares provided by remote clusters.

SVV\_REDSHIFT\_DATABASES is visible to all users by default. To control access to your database's metadata,
enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view
permissions for object metadata by users and roles. For more information, see
[Metadata security](t_metadata_security.md "t_metadata_security.md").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW DATABASES](r_SHOW_DATABASES.md "r_SHOW_DATABASES.md") command for database discovery. SHOW DATABASES works consistently across
local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name                | Data type    | Description                                                                                            |
| -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| database\_name             | varchar(128) | The name of the database.                                                                              |
| database\_owner            | integer      | The database owner user ID.                                                                            |
| database\_type             | varchar(32)  | The type of database. Possible types are local or<br>shared databases.                                 |
| database\_acl              | varchar(128) | This information is for internal use only.                                                             |
| database\_options          | varchar(128) | The properties of the database.                                                                        |
| database\_isolation\_level | varchar(128) | The isolation level of the database. Possible values include: `Snapshot Isolation` and `Serializable`. |

## Sample query

The following example returns the output for SVV\_REDSHIFT\_DATABASES.

```
`select database_name, database_owner, database_type, database_options, database_isolation_level
from svv_redshift_databases;`
`database_name | database_owner | database_type | database_options | database_isolation_level
--------------+----------------+---------------+------------------+------------------
 dev | 1 | local | NULL | Serializable`
```

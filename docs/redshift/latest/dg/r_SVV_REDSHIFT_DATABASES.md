Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_REDSHIFT_DATABASES

Use SVV\_ REDSHIFT_DATABASES to view a list of all the databases that a user has access
to. This includes the databases on the cluster and the databases created from datashares provided by remote clusters.

SVV_REDSHIFT_DATABASES is visible to all users by default. To control access to your database's metadata,
enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view
permissions for object metadata by users and roles. For more information, see
[Metadata security](t_metadata_security.md "t_metadata_security.md").

## Table columns

| Column name              | Data type    | Description                                                                                            |
| ------------------------ | ------------ | ------------------------------------------------------------------------------------------------------ |
| database_name            | varchar(128) | The name of the database.                                                                              |
| database_owner           | integer      | The database owner user ID.                                                                            |
| database_type            | varchar(32)  | The type of database. Possible types are local or<br>shared databases.                                 |
| database_acl             | varchar(128) | This information is for internal use only.                                                             |
| database_options         | varchar(128) | The properties of the database.                                                                        |
| database_isolation_level | varchar(128) | The isolation level of the database. Possible values include: `Snapshot Isolation` and `Serializable`. |

## Sample query

The following example returns the output for SVV_REDSHIFT_DATABASES.

```
`select database_name, database_owner, database_type, database_options, database_isolation_level
from svv_redshift_databases;`
`database_name | database_owner | database_type | database_options | database_isolation_level
--------------+----------------+---------------+------------------+------------------
 dev | 1 | local | NULL | Serializable`
```

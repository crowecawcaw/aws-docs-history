

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_COLUMN\_PRIVILEGES
<a name="r_SVV_COLUMN_PRIVILEGES"></a>

Use SVV\_COLUMN\_PRIVILEGES to view the column permissions that are explicitly granted to users, roles, and groups in the current database.

SVV\_COLUMN\_PRIVILEGES is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW COLUMN GRANTS](r_SHOW_COLUMN_GRANTS.md) command for permission discovery. SHOW COLUMN GRANTS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_COLUMN_PRIVILEGES-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| namespace\_name | text | The name of the namespace where a specified relation exists. | 
| relation\_name | text | The name of the relation. | 
| column\_name | text | The name of the column. | 
| privilege\_type | text | The type of the permission. Possible values are SELECT or UPDATE. | 
| identity\_id | integer | The ID of the identity. Possible values are user ID, role ID, or group ID. | 
| identity\_name | text | The name of the identity. | 
| identity\_type | text | The type of the identity. Possible values are user, role, group or public. | 

## Sample query
<a name="r_SVV_COLUMN_PRIVILEGES-sample-query"></a>

The following example displays the result of the SVV\_COLUMN\_PRIVILEGES.

```
SELECT namespace_name,relation_name,COLUMN_NAME,privilege_type,identity_name,identity_type
FROM svv_column_privileges WHERE relation_name = 'lineitem';

 namespace_name | relation_name | column_name | privilege_type | identity_name | identity_type
----------------+---------------+-------------+----------------+---------------+----------------
    public      |   lineitem    | l_orderkey  |     SELECT     |    reguser    |     user
    public      |   lineitem    | l_orderkey  |     SELECT     |     role1     |     role
    public      |   lineitem    | l_partkey   |     SELECT     |    reguser    |     user
    public      |   lineitem    | l_partkey   |     SELECT     |     role1     |     role
```
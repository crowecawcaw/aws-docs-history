

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ROLES
<a name="r_SVV_ROLES"></a>

Use SVV\_ROLES to view role information.

This table is visible to all users.

## Table columns
<a name="r_SVV_ROLES-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| role\_id | integer | The role ID. | 
| role\_name | text | The name of the role. | 
| role\_owner | text | The name of the role owner. | 
| external\_id | text | The unique identifier of the role in the third-party identity provider. | 

## Sample query
<a name="r_SVV_ROLES-sample-query"></a>

The following example returns the output of SVV\_ROLES.

```
SELECT role_name,role_owner FROM svv_roles WHERE role_name IN ('role1', 'role2');

 role_name | role_owner
-----------+------------
   role1   | superuser
   role2   | superuser
```
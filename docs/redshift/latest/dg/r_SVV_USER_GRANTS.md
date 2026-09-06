

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_USER\_GRANTS
<a name="r_SVV_USER_GRANTS"></a>

Use SVV\_USER\_GRANTS to view the list of users that are explicitly granted roles in the cluster.

SVV\_USER\_GRANTS is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see roles that are explicitly granted to them.

## Table columns
<a name="sub-r_SVV_USER_GRANTS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The user ID for the user.  | 
| user\_name | text | The name of the user. | 
| role\_id | integer | The role ID for the granted role. | 
| role\_name | text | The role name for the granted role. | 
| admin\_option | boolean | A value that indicates whether the user can grant the role to other users and roles. | 

## Sample queries
<a name="r_SVV_USER_GRANTS-sample-queries"></a>

The following queries grant roles to users and show the list of users that are explicitly granted roles.

```
GRANT ROLE role1 TO reguser;
GRANT ROLE role2 TO reguser;
GRANT ROLE role1 TO superuser;
GRANT ROLE role2 TO superuser;

SELECT user_name,role_name,admin_option FROM svv_user_grants;

 user_name | role_name | admin_option
-----------+-----------+--------------
 superuser |  role1    | False
 reguser   |  role1    | False
 superuser |  role2    | False
  reguser  |  role2    | False
```


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_DATASHARE\_PRIVILEGES
<a name="r_SVV_DATASHARE_PRIVILEGES"></a>

Use SVV\_DATASHARE\_PRIVILEGES to view the datashare permissions that are explicitly granted to users, roles, and groups in your Amazon Redshift cluster.

SVV\_DATASHARE\_PRIVILEGES is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

## Table columns
<a name="r_SVV_DATASHARE_PRIVILEGES-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| datashare\_name | text | The name of the datashare. | 
| privilege\_type | text | The type of the permission. Possible values are ALTER or SHARE. | 
| identity\_id | integer | The ID of the identity. Possible values are user ID, role ID, or group ID. | 
| identity\_name | text | The name of the identity. | 
| identity\_type | text | The type of the identity. Possible values are user, role, group, or public. | 
| admin\_option | boolean | A value that indicates whether the user can grant the permission to other users and roles. It is always false for the role and group identity type. | 

## Sample query
<a name="r_SVV_DATASHARE_PRIVILEGES-sample-query"></a>

The following example displays the result of the SVV\_DATASHARE\_PRIVILEGES.

```
SELECT datashare_name,privilege_type,identity_name,identity_type,admin_option FROM svv_datashare_privileges
WHERE datashare_name = 'demo_share';

 datashare_name | privilege_type |  identity_name | identity_type | admin_option
----------------+----------------+----------------+---------------+--------------
   demo_share   |     ALTER      |    superuser   |     user      |   False
   demo_share   |     ALTER      |    reguser     |     user      |   False
```
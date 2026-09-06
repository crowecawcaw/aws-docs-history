

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ROLE\_GRANTS
<a name="r_SVV_ROLE_GRANTS"></a>

Use SVV\_ROLE\_GRANTS to view a list of roles that are explicitly granted roles in the cluster.

SVV\_ROLE\_GRANTS is visible to the following users:
+ Superusers
+ Users with the ACCESS SYSTEM TABLE permission

Other users can only see identities they have access to or own.

## Table columns
<a name="r_SVV_ROLE_GRANTS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| role\_id | integer | The ID of the role. | 
| role\_name | text | The name of the role. | 
| granted\_role\_id | integer | The ID for the granted role. | 
| granted\_role\_name | text | The name for the granted role. | 

## Sample query
<a name="r_SVV_ROLE_GRANTS-sample-query"></a>

The following example returns the output of SVV\_ROLE\_GRANTS.

```
GRANT ROLE role1 TO ROLE role2;
GRANT ROLE role2 TO ROLE role3;

SELECT role_name, granted_role_name FROM svv_role_grants;

 role_name |  granted_role_name
-----------+--------------------
   role2   |      role1
   role3   |      role2
(2 rows)
```


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DETACH MASKING POLICY
<a name="r_DETACH_MASKING_POLICY"></a>

Detaches an already attached dynamic data masking policy from a column. For more information on dynamic data masking, see [Dynamic data masking](t_ddm.md).

Superusers and users or roles that have the sys:secadmin role can detach a masking policy.

## Syntax
<a name="r_DETACH_MASKING_POLICY-synopsis"></a>

```
DETACH MASKING POLICY
{
  policy_name ON table_name
  | database_name.policy_name ON database_name.schema_name.table_name
}
( output_column_names )
FROM { user_name | ROLE role_name | PUBLIC };
```

## Parameters
<a name="r_DETACH_MASKING_POLICY-parameters"></a>

 *policy\_name*   
The name of the masking policy to detach.

database\_name  
The name of the database where the policy and the relation are created. The policy and the relation needs to be on the same database. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

schema\_name  
The name of the schema the relation belongs to.

 *table\_name*   
The name of the table to detach the masking policy from.

*output\_column\_names*   
The names of the columns to which the masking policy was attached.

*user\_name*   
The name of the user to whom the masking policy was attached.  
You can only set one of user\_name, role\_name, and PUBLIC in a single DETACH MASKING POLICY statement.

*role\_name*   
The name of the role to which the masking policy was attached.  
You can only set one of user\_name, role\_name, and PUBLIC in a single DETACH MASKING POLICY statement.

*PUBLIC*   
Shows that the policy was attached to all users in the table.  
You can only set one of user\_name, role\_name, and PUBLIC in a single DETACH MASKING POLICY statement.

For the usage of DETACH MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).
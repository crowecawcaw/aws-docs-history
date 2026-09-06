

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DROP MASKING POLICY
<a name="r_DROP_MASKING_POLICY"></a>

Drops a dynamic data masking policy from all databases. You can't drop a masking policy that's still attached to one or more tables. For more information on dynamic data masking, see [Dynamic data masking](t_ddm.md).

Superusers and users or roles that have the sys:secadmin role can drop a masking policy.

## Syntax
<a name="r_DROP_MASKING_POLICY-synopsis"></a>

```
DROP MASKING POLICY { policy_name | database_name.policy_name };
```

## Parameters
<a name="r_DROP_MASKING_POLICY-parameters"></a>

 *policy\_name*   
The name of the masking policy to drop.

database\_name  
The name of the database from where the policy to be dropped. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

For the usage of DROP MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).
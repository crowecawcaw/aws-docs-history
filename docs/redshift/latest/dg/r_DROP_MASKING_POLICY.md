Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP MASKING POLICY

Drops a dynamic data masking policy from all databases. You can't drop a masking policy
that's still attached to one or more tables. For more information on dynamic data masking,
see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can drop a masking
policy.

## Syntax

```
DROP MASKING POLICY { policy_name | database_name.policy_name };
```

## Parameters

_policy_name_

The name of the masking policy to drop.

database_name

The name of the database from where the policy to be dropped. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

For the usage of DROP MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

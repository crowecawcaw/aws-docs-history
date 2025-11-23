Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DETACH MASKING POLICY

Detaches an already attached dynamic data masking policy from a column. For more
information on dynamic data masking, see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can detach a masking
policy.

## Syntax

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

_policy_name_

The name of the masking policy to detach.

database_name

The name of the database where the policy and the relation are created. The policy and the relation needs to be on the same database. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

schema_name

The name of the schema the relation belongs to.

_table_name_

The name of the table to detach the masking policy from.

_output_column_names_

The names of the columns to which the masking policy was attached.

_user_name_

The name of the user to whom the masking policy was attached.

You can only set one of user_name, role_name, and PUBLIC in a single DETACH
MASKING POLICY statement.

_role_name_

The name of the role to which the masking policy was attached.

You can only set one of user_name, role_name, and PUBLIC in a single DETACH
MASKING POLICY statement.

_PUBLIC_

Shows that the policy was attached to all users in the table.

You can only set one of user_name, role_name, and PUBLIC in a single DETACH
MASKING POLICY statement.

For the usage of DETACH MASKING POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

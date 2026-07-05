Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# DETACH RLS POLICY

Detach a row-level security policy on a table from one or more users or
roles.

Superusers and users or roles that have the `sys:secadmin` role can detach a
policy.

## Syntax

```
DETACH RLS POLICY
{
  policy_name ON [TABLE] table_name [, ...]
  | database_name.policy_name ON [TABLE] database_name.schema_name.table_name [, ...]
}
FROM { user_name | ROLE role_name | PUBLIC } [, ...];


```

## Parameters

_policy\_name_

The name of the policy.

database\_name

The name of the database where the policy and the relation are created. The policy and the relation needs to be on the same database. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

schema\_name

The name of the schema the relation belongs to.

table\_name

The relation that the row-level security policy is attached to.

FROM { _user\_name_ | ROLE _role\_name_
| PUBLIC} [, ...]

Specifies whether the policy is detached from one or more specified users or
roles.

For the usage of DETACH RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

## Usage notes

When working with the DETACH RLS POLICY statement, observe the following:

- You can detach a policy from a relation, user, role, or public.

## Examples

The following example detaches a policy on a table from a role.

```
DETACH RLS POLICY policy_concerts ON tickit_category_redshift FROM ROLE analyst, ROLE dbadmin;
```

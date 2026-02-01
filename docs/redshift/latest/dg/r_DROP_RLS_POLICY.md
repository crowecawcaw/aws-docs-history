Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP RLS POLICY

Drops a row-level security policy for all tables in all
databases.

Superusers and users or roles that have the sys:secadmin role can drop a policy.

## Syntax

```
DROP RLS POLICY [ IF EXISTS ]
{ policy_name | database_name.policy_name }
[ CASCADE | RESTRICT ]
```

## Parameters

_IF EXISTS_

A clause that indicates if the specified policy already exists.

_policy_name_

The name of the policy.

database_name

The name of the database from where the policy to be dropped. The database can be the connected database or a database that supports Amazon Redshift federated permissions.

_CASCADE_

A clause that indicates to automatically detach the policy from all attached
tables before dropping the policy.

_RESTRICT_

A clause that indicates not to drop the policy when it is attached to some
tables. This is the default.

For the usage of DROP RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

## Examples

The following example drops the row-level security policy.

```
DROP RLS POLICY policy_concerts;
```

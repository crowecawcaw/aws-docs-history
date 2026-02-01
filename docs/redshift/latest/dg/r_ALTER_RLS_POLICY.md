Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER RLS POLICY

Alter an existing row-level security policy on a table.

Superusers and users or roles that have the `sys:secadmin` role can alter a
policy.

## Syntax

```
ALTER RLS POLICY
{ policy_name | database_name.policy_name }
USING ( using_predicate_exp );
```

## Parameters

_policy_name_

The name of the policy.

database_name

The name of the database from where the policy is created. The database can be
the connected database or a database that supports Amazon Redshift federated permissions.

USING ( _using_predicate_exp_ )

Specifies a filter that is applied to the WHERE clause of the query.
Amazon Redshift applies a policy predicate before the query-level user predicates. For
example, `current_user = ‘joe’ and price > 10` limits Joe
to see only records with the price greater than $10.

The expression has access to the variables declared in the WITH clause of
the CREATE RLS POLICY statement that was used to create the policy with name
policy_name.

For the usage of ALTER RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

## Examples

The following example alters a RLS policy.

```
-- First create an RLS policy that limits access to rows where catgroup is 'concerts'.
CREATE RLS POLICY policy_concerts
WITH (catgroup VARCHAR(10))
USING (catgroup = 'concerts');

-- Then, alter the RLS policy to only show rows where catgroup is 'piano concerts'.
ALTER RLS POLICY policy_concerts
USING (catgroup = 'piano concerts');
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE RLS POLICY

Creates a new row-level security policy to provide granular access to database
objects.

Superusers and users or roles that have the sys:secadmin role can create a
policy.

## Syntax

```
CREATE RLS POLICY { policy_name | database_name.policy_name }
[ WITH (column_name data_type [, ...]) [ [AS] relation_alias ] ]
USING ( using_predicate_exp )

```

## Parameters

_policy_name_

The name of the policy.

database_name

The database name of where the policy will be created. Policy can be created on the connected database or on a database that supports Amazon Redshift federated permissions.

WITH (_column_name data_type [, ...]_)

Specifies the _column_name_ and
_data_type_ referenced to the columns of tables to which
the policy is attached.

You can omit the WITH clause only when the RLS policy doesn't reference
any columns of tables to which the policy is attached.

AS _relation_alias_

Specifies an optional alias for the table that the RLS policy will be
attached to.

USING ( _using_predicate_exp_ )

Specifies a filter that is applied to the WHERE clause of the query.
Amazon Redshift applies a policy predicate before the query-level user predicates. For
example, `current_user = ‘joe’ and price > 10` limits Joe
to see only records with the price greater than $10.

For the usage of CREATE RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [Managing access control with Amazon Redshift federated permissions](federated-permissions-managing-access.md "federated-permissions-managing-access.md").

## Usage notes

When working with the CREATE RLS POLICY statement, observe the following:

- Amazon Redshift supports filters that can be part of a WHERE clause of a query.
- All policies being attached to a table must have been created with the same
  table alias.
- You must use the GRANT and REVOKE statements to explicitly grant and revoke SELECT permissions to RLS policies that reference lookup tables. A lookup table is a table object used inside a policy definition. For more information, see [GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").
- Amazon Redshift row-level security doesn't support the following object types
  inside a policy definition: catalog tables, cross-database relations, external
  tables, regular views, late-binding views, tables with RLS policies turned on, and
  temporary tables.

## Examples

The following example creates an RLS policy called policy_concerts.
This policy applies to a VARCHAR(10) column called catgroup and
and sets the USING filter to only return rows where the value of catgroup is
`'Concerts'`.

```
CREATE RLS POLICY policy_concerts
WITH (catgroup VARCHAR(10))
USING (catgroup = 'Concerts');
```

For an end-to-end example of using RLS policies, see
[Row-level security end-to-end example](t_rls-example.md "t_rls-example.md").

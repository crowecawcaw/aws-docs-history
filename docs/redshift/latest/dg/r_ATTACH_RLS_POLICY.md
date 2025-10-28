Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ATTACH RLS POLICY

Attach a row-level security policy on a table to one or more users or
roles.

Superusers and users or roles that have the `sys:secadmin` role can attach a
policy.

## Syntax

```
ATTACH RLS POLICY *policy\_name* ON [TABLE] *table\_name* [, ...]
TO { *user\_name* | ROLE *role\_name* | PUBLIC } [, ...]
```

## Parameters

_policy_name_

The name of the policy.

ON [TABLE] _table_name_ [, ...]

The relation that the row-level security policy is attached to.

TO { _user_name_ | ROLE _role_name_ |
PUBLIC} [, ...]

Specifies whether the policy is attached to one or more specified users or
roles.

## Usage notes

When working with the ATTACH RLS POLICY statement, observe the following:

- The table being attached should have all the columns listed in the WITH clause
  of the policy creation statement.
- Amazon Redshift RLS supports attaching RLS policies to the following objects:
  - Tables
  - Views
  - Late-binding views
  - Materialized views

- Amazon Redshift RLS doesn't support attaching RLS policies to the following
  objects:
  - Catalog tables
  - Cross-database relations
  - External tables
  - Temporary tables
  - Policy lookup tables
  - Materialized view base tables

- RLS policies that are attached to superusers or to users with the
  `sys:secadmin` permission are ignored.

## Examples

The following example attaches an RLS policy to the specified table and role combinations.
The RLS policy applies to any users with the role of `analyst` or `dbadmin` when they
access the tickit_category_redshift table.

```
ATTACH RLS POLICY policy_concerts ON tickit_category_redshift TO ROLE analyst, ROLE dbadmin;
```

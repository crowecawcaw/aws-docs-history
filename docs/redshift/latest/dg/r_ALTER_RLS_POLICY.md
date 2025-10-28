Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER RLS POLICY

Alter an existing row-level security policy on a table.

Superusers and users or roles that have the `sys:secadmin` role can alter a
policy.

## Syntax

```
ALTER RLS POLICY *policy\_name*
USING ( *using\_predicate\_exp* );
```

## Parameters

_policy_name_

The name of the policy.

USING ( _using_predicate_exp_ )

Specifies a filter that is applied to the WHERE clause of the query.
Amazon Redshift applies a policy predicate before the query-level user predicates. For
example, `current_user = ‘joe’ and price > 10` limits Joe
to see only records with the price greater than $10.

The expression has access to the variables declared in the WITH clause of
the CREATE RLS POLICY statement that was used to create the policy with name
policy_name.

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

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP RLS POLICY

Drops a row-level security policy for all tables in all
databases.

Superusers and users or roles that have the sys:secadmin role can drop a policy.

## Syntax

```
DROP RLS POLICY [ IF EXISTS ] *policy\_name* [ CASCADE | RESTRICT ]
```

## Parameters

_IF EXISTS_

A clause that indicates if the specified policy already exists.

_policy_name_

The name of the policy.

_CASCADE_

A clause that indicates to automatically detach the policy from all attached
tables before dropping the policy.

_RESTRICT_

A clause that indicates not to drop the policy when it is attached to some
tables. This is the default.

## Examples

The following example drops the row-level security policy.

```
DROP RLS POLICY policy_concerts;
```

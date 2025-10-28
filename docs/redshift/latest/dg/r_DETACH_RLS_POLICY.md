Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DETACH RLS POLICY

Detach a row-level security policy on a table from one or more users or
roles.

Superusers and users or roles that have the `sys:secadmin` role can detach a
policy.

## Syntax

```
DETACH RLS POLICY *policy\_name* ON [TABLE] *table\_name* [, ...]
FROM { *user\_name* | ROLE *role\_name* | PUBLIC } [, ...]
```

## Parameters

_policy_name_

The name of the policy.

ON [TABLE] _table_name_ [, ...]

The table or view that the row-level security policy is detached
from.

FROM { _user_name_ | ROLE _role_name_
| PUBLIC} [, ...] Specifies whether the policy is detached from one or more specified users or roles. ## Usage notes When working with the DETACH RLS POLICY statement, observe the following: <br>• You can detach a policy from a relation, user, role, or public. ## Examples The following example detaches a policy on a table from a role. `DETACH RLS POLICY policy_concerts ON tickit_category_redshift FROM ROLE analyst, ROLE dbadmin;`

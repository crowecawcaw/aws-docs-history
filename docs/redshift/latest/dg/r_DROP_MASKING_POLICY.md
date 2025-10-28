Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP MASKING POLICY

Drops a dynamic data masking policy from all databases. You can't drop a masking policy
that's still attached to one or more tables. For more information on dynamic data masking,
see [Dynamic data masking](t_ddm.md "t_ddm.md").

Superusers and users or roles that have the sys:secadmin role can drop a masking
policy.

## Syntax

```
DROP MASKING POLICY *policy\_name*;
```

## Parameters

_policy_name_

The name of the masking policy to drop.

Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HAS_ASSUMEROLE_PRIVILEGE

Returns Boolean `true` (`t`) if the specified user has the
specified IAM role with the privilege to run the specified command. The function
returns `false` (`f`) if the user doesn't have the specified IAM
role with the privilege to run the specified command. For more information about
privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

## Syntax

```
has_assumerole_privilege( [ *user*, ] *iam\_role\_arn*, *cmd\_type*)
```

## Arguments

_user_

The name of the user to check for IAM role privileges. The default is
to check the current user. Superusers and users can use this function.
However, users can only view their own privileges.

_iam_role_arn_

The IAM role that has been granted the command privileges.

_cmd_type_

The command for which access has been granted. Valid values are the
following:

- COPY
- UNLOAD
- EXTERNAL FUNCTION
- CREATE MODEL

## Return type

BOOLEAN

## Example

The following query confirms that the user `reg_user1` has the
privilege for the `Redshift-S3-Read` role to run the COPY command.

```
select has_assumerole_privilege('reg_user1', 'arn:aws:iam::123456789012:role/Redshift-S3-Read', 'copy');

```

```
has_assumerole_privilege
------------------------
true
(1 row)
```

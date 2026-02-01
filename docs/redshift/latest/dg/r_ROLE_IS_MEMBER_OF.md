Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ROLE_IS_MEMBER_OF

Returns true if the role is a member of another role. Superusers can check the
membership of all roles. Regular users who have the ACCESS SYSTEM TABLE permission can
check all users' membership. Otherwise, regular users can only check roles to which they
have access. Amazon Redshift errors out if the provided roles don't exist or the current
user doesn't have access to the role.

## Syntax

```
role_is_member_of( *role\_name*,  *granted\_role\_name*)
```

## Arguments

_role_name_

The name of the role.

_granted_role_name_

The name of the granted role.

## Return type

Returns a BOOLEAN.

## Example

The following query confirms that the role isn't a member of role1 nor role2.

```
SELECT role_is_member_of('role1', 'role2');

 role_is_member_of
-------------------
             False
```

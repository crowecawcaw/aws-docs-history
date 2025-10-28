Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# USER_IS_MEMBER_OF

###### Important

Starting February 16, 2026, Amazon Redshift will no longer support the usage of
`user_is_member_of` and related functions that access consumer user, role, or
group information through datasharing.

Returns true if the user is a member of a role or group. Superusers can check the
membership of all users. Regular users who are members of the sys:secadmin or
sys:superuser role can check all users' membership. Otherwise, regular users can
only check themselves. Amazon Redshift sends an error if the provided identities don't
exist or the current user doesn't have access to the role.

## Syntax

```
user_is_member_of( *user\_name*,  *role\_name* | *group\_name*)
```

## Arguments

_user_name_

The name of the user.

_role_name_

The name of the role.

_group_name_

The name of the group.

## Return type

Returns a BOOLEAN.

## Example

The following query confirms that the user isn't a member of role1.

```
SELECT user_is_member_of('reguser', 'role1');

 user_is_member_of
-------------------
           False
```

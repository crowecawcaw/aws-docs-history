Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# USER\_IS\_MEMBER\_OF

###### Important

Starting February 16, 2026, Amazon Redshift will no longer support the usage of
`user_is_member_of` and related functions that access consumer user, role, or
group information through datasharing.

Returns true if the user is a member of a role or group. Superusers can check the
membership of all users. Regular users who are members of the sys:secadmin or
sys:superuser role can check all users' membership. Otherwise, regular users can
only check themselves. Amazon Redshift sends an error if the provided identities don't
exist or the current user doesn't have access to the role.

**Data sharing consideration**

When a consumer cluster queries a shared object that references this function,
such as a view, RLS policy, or DDM policy, the function evaluates using the consumer
cluster's security context. The consumer's local users, roles, and group memberships
determine the result, not those defined on the producer cluster. If you intend to
enforce the same permissions context that is implemented on the producer, ensure that
the corresponding role names, group names, and user memberships exist on the consumer
cluster and match those on the producer.

## Syntax

```
user_is_member_of( *user\_name*,  *role\_name* | *group\_name*)
```

## Arguments

_user\_name_

The name of the user.

_role\_name_

The name of the role.

_group\_name_

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

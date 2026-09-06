

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ROLE\_IS\_MEMBER\_OF
<a name="r_ROLE_IS_MEMBER_OF"></a>

Returns true if the role is a member of another role. Superusers can check the membership of all roles. Regular users who have the ACCESS SYSTEM TABLE permission can check all users' membership. Otherwise, regular users can only check roles to which they have access. Amazon Redshift errors out if the provided roles don't exist or the current user doesn't have access to the role.

**Data sharing consideration**

When a consumer cluster queries a shared object that references this function, such as a view, RLS policy, or DDM policy, the function evaluates using the consumer cluster's security context. The consumer's local users, roles, and group memberships determine the result, not those defined on the producer cluster. If you intend to enforce the same permissions context that is implemented on the producer, make sure that the corresponding role names, group names, and user memberships exist on the consumer cluster and match those on the producer.

## Syntax
<a name="r_ROLE_IS_MEMBER_OF-synopsis"></a>

```
role_is_member_of( role_name,  granted_role_name)
```

## Arguments
<a name="r_ROLE_IS_MEMBER_OF-arguments"></a>

 *role\_name*   
The name of the role.

 *granted\_role\_name*   
The name of the granted role.

## Return type
<a name="r_ROLE_IS_MEMBER_OF-return-type"></a>

Returns a BOOLEAN.

## Example
<a name="r_ROLE_IS_MEMBER_OF-example"></a>

The following query confirms that the role isn't a member of role1 nor role2.

```
SELECT role_is_member_of('role1', 'role2');

 role_is_member_of
-------------------
             False
```
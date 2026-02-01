Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Role assignment

Superusers and regular users with the CREATE ROLE permissions can use the CREATE ROLE
statement to create roles. Superusers and role administrators can use the GRANT ROLE
statement to grant a role to others. They can use the REVOKE ROLE statement to revoke a
role from others, and the DROP ROLE statement to drop roles. Role administrators include role owners and users who have been granted the role with the ADMIN OPTION permission.

Only superusers or role administrators can grant and revoke roles. You can grant or
revoke one or more roles to or from one or more roles or users. Use the WITH ADMIN
OPTION option in the GRANT ROLE statement to provide the administration options for all
the granted roles to all the grantees.

Amazon Redshift supports different combinations of role assignments, such as granting
multiple roles or having multiple grantees. The WITH ADMIN OPTION only applies to users
and not to roles. Similarly, use the WITH ADMIN OPTION option in the REVOKE ROLE
statement to remove the role and the administrative authorization from the grantee. When
used with the ADMIN OPTION, only the administrative authorization is revoked from the
role.

The following example revokes the administrative authorization of the
`sample_role2` role from `user2`.

```
REVOKE ADMIN OPTION FOR sample_role2 FROM user2;
```

For more information about how to create roles and manage role assignments, see [Managing roles in RBAC](r_roles-managing.md "r_roles-managing.md").

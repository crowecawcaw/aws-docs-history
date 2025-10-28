After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing user access in Amazon FinSpace

Amazon FinSpace administrators or superusers can use the following topics to manage user
access.

**Superuser**

A superuser has all the permissions in FinSpace. The first superuser for your FinSpace
environment is created from the AWS console. The superuser can then create other
superusers and application users from the FinSpace web application.

**Application user**

An application user does not have any permissions when their account is created. They
are assigned permissions by adding them to a permission group.

**Permission group**

Permission groups contain users. Permissions to perform any action in FinSpace are
assigned to permission groups, not directly to the user. A user can be a member of
multiple permission groups. A permission group cannot be a member of another permission
group.

**Permissions**

Permissions are assigned to permission groups and not to users. The are two kinds of
permissions in FinSpace - application permissions and dataset permissions. Application
permissions are assigned to a permission group when creating or editing it (for example,
create datasets). Dataset permissions are assigned on a per dataset basis when
associating a permission group to a dataset (for example, read a view in a
dataset).

######

Topics

- [Managing user access with email and
  password](managing-user-email-pwd.md "managing-user-email-pwd.md")
- [Managing user access with SSO](managing-user-sso.md "managing-user-sso.md")
- [Managing user permissions with permission
  groups](managing-user-permissions.md "managing-user-permissions.md")
- [Temporary credentials in Amazon FinSpace](temporary-credentials.md "temporary-credentials.md")

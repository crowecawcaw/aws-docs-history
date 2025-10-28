Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE ROLE

Creates a new custom role that is a collection of permissions. For a list of Amazon Redshift
system-defined roles, see [Amazon Redshift system-defined roles](r_roles-default.md "r_roles-default.md").
Query [SVV_ROLES](r_SVV_ROLES.md "r_SVV_ROLES.md") to view the currently created roles
in your cluster or workgroup.

There is a quota of the number of roles that can be created. For more information, see
[Quotas and limits in Amazon Redshift](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md") in the _Amazon Redshift Management Guide_.

## Required permissions

Following are the required privileges for CREATE ROLE.

- Superuser
- Users with the CREATE ROLE privilege

## Syntax

```
CREATE ROLE *role\_name*
[ EXTERNALID *external\_id* ]
```

## Parameters

_role_name_

The name of the role. The role name must be unique and can't be the
same as any user names. A role name can't be a reserved word.

A superuser or regular user with the CREATE ROLE privilege can create roles.
A user that is not a superuser but that has been granted USAGE to the role WITH
GRANT OPTION and ALTER privilege can grant this role to anyone.

EXTERNALID _external_id_

The identifier for the role, which is associated with an identity provider.
For more information, see [Native
identity provider (IdP) federation for Amazon Redshift](../mgmt/redshift-iam-access-control-native-idp.md "../mgmt/redshift-iam-access-control-native-idp.md").

## Examples

The following example creates a role `sample_role1`.

```
CREATE ROLE sample_role1;
```

The following example creates a role `sample_role1`, with an external ID
that is associated with an identity provider.

```
CREATE ROLE sample_role1 EXTERNALID "ABC123";
```

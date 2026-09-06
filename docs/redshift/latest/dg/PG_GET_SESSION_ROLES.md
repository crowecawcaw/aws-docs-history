

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PG\_GET\_SESSION\_ROLES
<a name="PG_GET_SESSION_ROLES"></a>

Returns session roles of the currently logged in user. Session roles of a user are the groups defined by an identity provider (IdP) for the logged in user. For example, an identity provider (IdP) such as [Microsoft Azure Active Directory (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/) verifies the identity of the user and provides any external groups the user is part of during the user login process. These external groups are transformed into Amazon Redshift roles and are available during the current session. These roles are called session roles. An administrator can grant privileges to a session role similar to other Amazon Redshift roles. For information about using roles, see [Role-based access control (RBAC)](t_Roles.md). For information about managing identities with an identity provider (IdP), see [Native identity provider (IdP) federation for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-native-idp.html) in the *Amazon Redshift Management Guide*.

To view the roles defined in the Amazon Redshift catalog, query the system view [SVV\_ROLES](r_SVV_ROLES.md).

## Syntax
<a name="PG_GET_LATE_BINDING_VIEW_COLS-synopsis"></a>

```
pg_get_session_roles()
```

## Return type
<a name="PG_GET_SESSION_ROLES-return-type"></a>

A set of rows that consists of two values. The first value has two parts separated by a colon(:) that contains an `idp-namespace:role-name`. The `idp-namespace` is the namespace of the identity provider (IdP). The `role-name` is the name of the external group in the identity provider (IdP). The second value contains a `role-id` which is the role identifier.

## Usage notes
<a name="PG_GET_SESSION_ROLES-usage-notes"></a>

The `PG_GET_SESSION_ROLES` function returns one row for each returned session role.

## Examples
<a name="PG_GET_SESSION_ROLES-example"></a>

The following example returns one row for each role from the Azure Active Directory IdP. The returned columns are cast to `sess_roles` with columns `name` and `roleid`. Each `name` consists of the Azure Active Directory namespace and a group name in Azure Active Directory.

```
SELECT * FROM pg_get_session_roles() AS sess_roles(name name, roleid integer);

name                  roleid
--------------------------------
my_aad:test_group_1   106204
my_aad:test_group_2   106205
my_aad:test_group_3   106206
my_aad:test_group_4   106207
my_aad:test_group_5   106208
```

The following example returns one row for each IAM group that the currently logged in IAM user is a member of. The returned columns are cast to `sess_roles` with columns `name` and `roleid`. Each `name` consists of the IAM namespace and IAM group name.

```
SELECT * FROM pg_get_session_roles() AS sess_roles(name name, roleid integer);

name                  roleid
--------------------------------
IAM:myGroup           110332
```
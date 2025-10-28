Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER ROLE

Renames a role or changes the owner. For a list of Amazon Redshift system-defined roles, see
[Amazon Redshift system-defined roles](r_roles-default.md "r_roles-default.md").

## Required permissions

Following are the required permissions for ALTER ROLE:

- Superuser
- Users with the ALTER ROLE permissions

## Syntax

```
ALTER ROLE role [ WITH ]
  { { RENAME TO role } | { OWNER TO *user\_name* } }[, ...]
  [ EXTERNALID TO *external\_id* ]
```

## Parameters

_role_

The name of the role to be altered.

RENAME TO

A new name for the role.

OWNER TO _user_name_

A new owner for the role.

EXTERNALID TO _external_id_

A new external ID for the role, which is associated with an identity
provider. For more information, see [Native
identity provider (IdP) federation for Amazon Redshift](../mgmt/redshift-iam-access-control-native-idp.md "../mgmt/redshift-iam-access-control-native-idp.md").

## Examples

The following example changes the name of a role from `sample_role1` to
`sample_role2`.

```
ALTER ROLE sample_role1 RENAME TO sample_role2;
```

The following example changes the owner of the role.

```
ALTER ROLE sample_role1 WITH OWNER TO user1
```

The syntax of the ALTER ROLE is similar to ALTER PROCEDURE following.

```
ALTER PROCEDURE first_quarter_revenue(bigint, numeric) RENAME TO quarterly_revenue;
```

The following example changes the owner of a procedure to
`etl_user`.

```
ALTER PROCEDURE quarterly_revenue(bigint, numeric) OWNER TO etl_user;
```

The following example updates a role `sample_role1` with a new external ID
that is associated with an identity provider.

```
ALTER ROLE sample_role1 EXTERNALID TO "XYZ456";
```

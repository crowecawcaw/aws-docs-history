Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP ROLE

Removes a role from a database. Only the role owner who either created the role, a user
with the WITH ADMIN option, or a superuser can drop a role.

You can't drop a role that is granted to a user or another role that is dependent
on this role.

## Required privileges

Following are the required privileges for DROP ROLE:

- Superuser
- Role owner who is either the user that created the role or a user that has been
  granted the role with the WITH ADMIN OPTION privilege.

## Syntax

```
DROP ROLE *role\_name* [ FORCE | RESTRICT ]
```

## Parameters

_role_name_

The name of the role.

[ FORCE | RESTRICT ]

The default setting is RESTRICT. Amazon Redshift throws an error when you try to
drop a role that has inherited another role. Use FORCE to remove all role
assignments, if any exists.

## Examples

The following example drops the role `sample_role`.

```
DROP ROLE sample_role FORCE;
```

The following example attempts to drop the role sample_role1 that has been granted to
a user with the default RESTRICT option.

```
CREATE ROLE sample_role1;
GRANT ROLE sample_role1 TO user1;
DROP ROLE sample_role1;
ERROR:  cannot drop this role since it has been granted on a user
```

To successfully drop the sample_role1 that has been granted to a user, use the FORCE
option.

```
DROP ROLE sample_role1 FORCE;
```

The following example attempts to drop the role sample_role2 that has another role
dependent on it with the default RESTRICT option.

```
CREATE ROLE sample_role1;
CREATE ROLE sample_role2;
GRANT ROLE sample_role1 TO sample_role2;
DROP ROLE sample_role2;
ERROR:  cannot drop this role since it depends on another role

```

To successfully drop the sample_role2 that has another role dependent on it, use the
FORCE option.

```
DROP ROLE sample_role2 FORCE;
```

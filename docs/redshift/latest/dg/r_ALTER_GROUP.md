Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ALTER GROUP

Changes a user group. Use this command to add users to the group, drop users from the
group, or rename the group.

## Syntax

```
ALTER GROUP *group\_name*
{
ADD USER *username* [, ... ] |
DROP USER *username* [, ... ] |
RENAME TO *new\_name*
}
```

## Parameters

_group\_name_

Name of the user group to modify.

ADD

Adds a user to a user group.

DROP

Removes a user from a user group.

_username_

Name of the user to add to the group or drop from the group.

RENAME TO

Renames the user group. Group names beginning with two underscores are
reserved for Amazon Redshift internal use. For more information about valid names, see
[Names and identifiers](r_names.md "r_names.md").

_new\_name_

New name of the user group.

## Examples

The following example adds a user named DWUSER to the ADMIN\_GROUP group.

```
ALTER GROUP admin_group
ADD USER dwuser;
```

The following example renames the group ADMIN\_GROUP to ADMINISTRATORS.

```
ALTER GROUP admin_group
RENAME TO administrators;
```

The following example adds two users to the group ADMIN\_GROUP.

```
ALTER GROUP admin_group
ADD USER u1, u2;
```

The following example drops two users from the group ADMIN\_GROUP.

```
ALTER GROUP admin_group
DROP USER u1, u2;
```

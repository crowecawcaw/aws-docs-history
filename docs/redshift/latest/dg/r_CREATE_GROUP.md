Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE GROUP

Defines a new user group. Only a superuser can create a group.

## Syntax

```
CREATE GROUP *group\_name*
[ [ WITH ] [ USER *username* ] [, ...] ]
```

## Parameters

_group_name_

Name of the new user group. Group names beginning with two underscores are
reserved for Amazon Redshift internal use. For more information about valid names, see
[Names and identifiers](r_names.md "r_names.md").

WITH

Optional syntax to indicate additional parameters for CREATE GROUP.

USER

Add one or more users to the group.

_username_

Name of the user to add to the group.

## Examples

The following example creates a user group named ADMIN_GROUP with a two users, ADMIN1
and ADMIN2.

```
create group admin_group with user admin1, admin2;
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HAS_SCHEMA_PRIVILEGE

Returns `true` if the user has the specified privilege for the specified
schema. For more information about privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

## Syntax

###### Note

This is a leader-node function. This function returns an error if it references
a user-created table, an STL or STV system table, or an SVV or SVL system
view.

```
has_schema_privilege( [ *user*, ] *schema*, *privilege*)
```

## Arguments

_user_

The name of the user to check for schema privileges. The default is to
check the current user.

_schema_

The schema associated with the privilege.

_privilege_

The privilege to check. Valid values are the following:

- CREATE
- USAGE
- ALTER
- DROP

## Return type

Returns a CHAR or VARCHAR string.

## Example

The following query confirms that the GUEST user has the CREATE privilege on the
PUBLIC schema:

```
select has_schema_privilege('guest', 'public', 'create');

has_schema_privilege
----------------------
true
(1 row)
```

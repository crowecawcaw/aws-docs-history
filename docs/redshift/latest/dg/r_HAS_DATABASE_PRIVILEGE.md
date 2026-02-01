Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HAS_DATABASE_PRIVILEGE

Returns `true` if the user has the specified privilege for the specified
database. For more information about privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

## Syntax

###### Note

This is a leader-node function. This function returns an error if it references
a user-created table, an STL or STV system table, or an SVV or SVL system
view.

```
has_database_privilege( [ *user*, ] *database*, *privilege*)
```

## Arguments

_user_

The name of the user to check for database privileges. The default is to
check the current user.

_database_

The database associated with the privilege.

_privilege_

The privilege to check. Valid values are the following:

- CREATE
- TEMPORARY
- TEMP

## Return type

Returns a CHAR or VARCHAR string.

## Example

The following query confirms that the GUEST user has the TEMP privilege on the
TICKIT database.

```
select has_database_privilege('guest', 'tickit', 'temp');

has_database_privilege
------------------------
true
(1 row)
```

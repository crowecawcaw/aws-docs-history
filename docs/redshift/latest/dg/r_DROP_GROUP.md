Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP GROUP

Deletes a user group. This command isn't reversible. This command doesn't
delete the individual users in a group.

See DROP USER to delete an individual user.

## Syntax

```
DROP GROUP *name*
```

## Parameter

_name_

Name of the user group to delete.

## Example

The following example deletes the `guests` user group:

```
DROP GROUP guests;
```

You can't drop a group if the group has any privileges on an object. If you
attempt to drop such a group, you will receive the following error.

```
ERROR: group "guests" can't be dropped because the group has a privilege on some object
```

If the group has privileges for an object, you must revoke the privileges before
dropping the group. To find the objects that the `guests` group has
privileges for, use the following example. For more information about the metadata view
used in the example, see [SVV_RELATION_PRIVILEGES](r_SVV_RELATION_PRIVILEGES.md "r_SVV_RELATION_PRIVILEGES.md").

```
`SELECT DISTINCT namespace_name, relation_name, identity_name, identity_type
FROM svv_relation_privileges
WHERE identity_type='group' AND identity_name='guests';`

`+----------------+---------------+---------------+---------------+
| namespace_name | relation_name | identity_name | identity_type |
+----------------+---------------+---------------+---------------+
| public | table1 | guests | group |
+----------------+---------------+---------------+---------------+
| public | table2 | guests | group |
+----------------+---------------+---------------+---------------+`
```

The following example revokes all privileges on all tables in the `public`
schema from the `guests` user group, and then drops the group.

```
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM GROUP guests;
DROP GROUP guests;
```

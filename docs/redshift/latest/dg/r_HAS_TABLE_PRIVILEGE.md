Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# HAS_TABLE_PRIVILEGE

Returns `true` if the user has the specified privilege for the specified
table and returns `false` otherwise.

## Syntax

###### Note

This is a leader-node function. This function returns an error if it references
a user-created table, an STL or STV system table, or an SVV or SVL system view.
For more information about privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

```
has_table_privilege( [ *user*, ] *table*, *privilege*)
```

## Arguments

_user_

The name of the user to check for table privileges. The default is to
check the current user.

_table_

Table associated with the privilege.

_privilege_

Privilege to check. Valid values are the following:

- SELECT
- INSERT
- UPDATE
- DELETE
- DROP
- REFERENCES

## Return type

BOOLEAN

## Examples

The following query finds that the GUEST user doesn't have SELECT privilege
on the LISTING table.

```
`select has_table_privilege('guest', 'listing', 'select');`

`has_table_privilege
---------------------
false`
```

The following query lists table privileges, including select, insert, update, and
delete, using output from the pg_tables and pg_user catalog tables. This is a sample
only. You might have to specify a schema name and table names from your database. For more information, see
[Querying the catalog tables](c_join_PG.md "c_join_PG.md").

```
`SELECT
 tablename
 ,usename
 ,HAS_TABLE_PRIVILEGE(users.usename, tablename, 'select') AS sel
 ,HAS_TABLE_PRIVILEGE(users.usename, tablename, 'insert') AS ins
 ,HAS_TABLE_PRIVILEGE(users.usename, tablename, 'update') AS upd
 ,HAS_TABLE_PRIVILEGE(users.usename, tablename, 'delete') AS del
FROM
(SELECT * from pg_tables
WHERE schemaname = 'public' and tablename in ('event','listing')) as tables
,(SELECT * FROM pg_user) AS users;`

`tablename | usename | sel | ins | upd | del
----------+-----------+--------+-------+-------+-------
event | john | true | true | true | true
event | sally | false | false | false | false
event | elsa | false | false | false | false
listing | john | true | true | true | true
listing | sally | false | false | false | false
listing | elsa | false | false | false | false`
```

The previous query also contains a cross join. For more information, see [JOIN examples](r_Join_examples.md "r_Join_examples.md"). To query tables that are not in the `public` schema, remove the `schemaname` condition from the WHERE clause and use the following example prior to your query.

```
`SET SEARCH_PATH to '`schema_name`';`
```

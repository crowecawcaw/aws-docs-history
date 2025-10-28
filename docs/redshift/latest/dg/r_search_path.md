Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# search_path

## Values (default in bold)

**'$user', public,** _schema_names_

A comma-separated list of existing schema names. If **'$user'** is present, then the schema having the same name as
`SESSION_USER` is substituted, otherwise it is ignored.

## Description

Specifies the order in which schemas are searched when an object (such as a table or
a function) is referenced by a simple name with no schema component:

- Search paths aren't supported with external schemas and external tables.
  External tables must be explicitly qualified by an external schema. Datashares
  behave as external data and are therefore not supported as search paths.
- When objects are created without a specific target schema, they are placed in
  the first schema listed in the search path. If the search path is empty, the
  system returns an error.
- When objects with identical names exist in different schemas, the one found
  first in the search path is used.
- An object that isn't in any of the schemas in the search path can only be
  referenced by specifying its containing schema with a qualified (dotted) name.
- The system catalog schema, pg_catalog, is always searched. If it is mentioned
  in the path, it is searched in the specified order. If not, it is searched before
  any of the path items.
- The current session's temporary-table schema, pg_temp_nnn, is always searched
  if it exists. It can be explicitly listed in the path by using the alias pg_temp.
  If it is not listed in the path, it is searched first (even before pg_catalog).
  However, the temporary schema is only searched for relation names (tables, views).
  It is not searched for function names.

## Example

The following example creates the schema ENTERPRISE and sets the search_path to the
new schema.

```
create schema enterprise;
set search_path to enterprise;
show search_path;

 search_path
-------------
 enterprise
(1 row)
```

The following example adds the schema ENTERPRISE to the default search_path.

```
set search_path to '$user', public, enterprise;
show search_path;

         search_path
-----------------------------
 "$user", public, enterprise
(1 row)
```

The following example adds the table FRONTIER to the schema ENTERPRISE.

```
create table enterprise.frontier (c1 int);
```

When the table PUBLIC.FRONTIER is created in the same database, and the user does not
specify the schema name in a query, PUBLIC.FRONTIER takes precedence over
ENTERPRISE.FRONTIER.

```
create table public.frontier(c1 int);
insert into enterprise.frontier values(1);
select * from frontier;

frontier
----
(0 rows)

select * from enterprise.frontier;

c1
----
1
(1 row)
```

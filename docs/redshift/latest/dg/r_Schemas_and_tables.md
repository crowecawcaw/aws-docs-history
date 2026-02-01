Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Schemas

A database contains one or more named schemas. Each schema in a database contains tables
and other kinds of named objects. By default, a database has a single schema, which is
named PUBLIC. You can use schemas to group database objects under a common name. Schemas
are similar to file system directories, except that schemas cannot be nested.

Identical database object names can be used in different schemas in the same database
without conflict. For example, both MY_SCHEMA and YOUR_SCHEMA can contain a table named
MYTABLE. Users with the necessary permissions can access objects across multiple schemas in
a database.

By default, an object is created within the first schema in the search path of the
database. For information, see [Search path](#c_Search_path "#c_Search_path") later in this section.

Schemas can help with organization and concurrency issues in a multiuser environment in
the following ways:

- To let many developers work in the same database without interfering with each
  other.
- To organize database objects into logical groups to make them more
  manageable.
- To give applications the ability to put their objects into separate schemas so
  that their names will not collide with the names of objects used by other
  applications.

## Search path

The search path is defined in the search_path parameter with a comma-separated list
of schema names. The search path specifies the order in which schemas are searched when
an object, such as a table or function, is referenced by a simple name that does not
include a schema qualifier.

If an object is created without specifying a target schema, the object is added to
the first schema that is listed in search path. When objects with identical names exist
in different schemas, an object name that does not specify a schema will refer to the
first schema in the search path that contains an object with that name.

To change the default schema for the current session, use the [SET](r_SET.md "r_SET.md") command.

For more information, see the [search_path](r_search_path.md "r_search_path.md") description in the Configuration Reference.

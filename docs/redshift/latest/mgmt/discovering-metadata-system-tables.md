Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Querying system tables

If neither the driver metadata API nor `SHOW` commands meet your
needs, you can query PostgreSQL catalog tables (`pg_*`), the information
schema (`information_schema`), or Amazon Redshift system views such as
`SVV_TABLE_INFO` directly.

This approach is useful for ad hoc exploration, debugging, or administrative tasks
that you run from interactive SQL queries, for example in Amazon Redshift query editor v2
or `psql`. However, system catalog structures can change across Amazon Redshift
releases. We don't recommend that you rely on direct system table queries as
the metadata interface for production application integrations.

When you query system tables, follow these practices:

- **Specify database, schema, and table**.
  For best performance, include the database name, schema name, and
  table name in your query filters. Narrowing the scope reduces the amount of
  metadata that Amazon Redshift needs to scan and return.
- **Use equality or LIKE filters**. Use
  equality (`=`) or `LIKE` predicates in your
  `WHERE` clause to narrow results. Avoid unfiltered queries
  against large catalog views. They can be slow on clusters with many
  objects.
- **Avoid functions in filter predicates**.
  Don't use functions such as `LOWER()` or string
  concatenation in your `WHERE` clause when you filter system table
  queries. These prevent efficient metadata lookups and can significantly
  degrade query performance.

## Example Anti-pattern vs. Recommended Queries

```
-- Avoid:
SELECT * FROM svv_all_columns;

-- Recommended:
SELECT * FROM svv_all_columns WHERE database_name = 'dev' and schema_name = 'public' AND table_name = 'sales';
```

```
-- Avoid:
SELECT * FROM svv_all_columns WHERE LOWER(schema_name) = 'public';

-- Recommended:
SELECT * FROM svv_all_columns WHERE schema_name = 'public' AND table_name LIKE 'sales%';
```

```
-- Avoid:
SELECT * FROM svv_all_columns WHERE database_name || '.' || schema_name || '.' || table_name = 'dev.public.sales';

-- Recommended:
SELECT * FROM svv_all_columns WHERE database_name = 'dev' and schema_name = 'public' AND table_name = 'sales';
```

```
-- Avoid:
SELECT * FROM svv_all_columns WHERE CONCAT(database_name, '.', schema_name) = 'dev.public';

-- Recommended:
SELECT * FROM svv_all_columns WHERE database_name = 'dev' and schema_name = 'public';
```

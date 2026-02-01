Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using RLS policies in SQL statements

When using RLS policies in SQL statements, Amazon Redshift applies the following
rules:

- Amazon Redshift applies RLS policies to the SELECT, UPDATE, and DELETE statements by default.
- For SELECT and UNLOAD, Amazon Redshift filters rows according to your defined policy.
- For UPDATE, Amazon Redshift updates only the rows that are visible to you. If a policy restricts a subset of the rows in a table, then you can't update them.
- For DELETE, you can delete only the rows that are visible to you. If a policy restricts a
  subset of the rows in a table, then you can't delete them. For TRUNCATE, you
  can still truncate the table.
- For CREATE TABLE LIKE, tables created with the LIKE options won't inherit permission
  settings from the source table. Similarly, the target table won't inherit the
  RLS policies from source table.

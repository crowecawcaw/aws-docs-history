Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Limitations

This topic describes limitations for cross-database queries in Amazon Redshift.

When you work with the cross-database query feature in Amazon Redshift, be aware of the
limitations following:

- You can't query views that are created on other databases that refer to
  objects of yet another database.
- You can't write to external schemas to database objects on any other unconnected
  databases.
- You can only create late-binding and materialized views on objects of other
  databases in the cluster. You can't create regular views on objects of other
  databases in the cluster.
- Amazon Redshift doesn't support tables with column-level privileges for
  cross-database queries.
- Running cross-database queries on tables with interleaved sort keys isn't
  supported.

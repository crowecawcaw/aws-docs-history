

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Limitations
<a name="cross-database_limitation"></a>

This topic describes limitations for cross-database queries in Amazon Redshift.

When you work with the cross-database query feature in Amazon Redshift, be aware of the limitations following:
+ You can't query views that are created on other databases that refer to objects of yet another database.
+ You can't write to external schemas to database objects on any other unconnected databases.
+ You can only create late-binding and materialized views on objects of other databases in the cluster. You can't create regular views on objects of other databases in the cluster.
+ Amazon Redshift doesn't support tables with column-level privileges for cross-database queries.
+  Running cross-database queries on tables with interleaved sort keys isn't supported. 
Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Schedule around maintenance

windows

If a scheduled maintenance occurs while a query is running, the query is terminated
and rolled back and you need to restart it. Schedule long-running operations, such as
large data loads or VACUUM operation, to avoid maintenance windows. You can also
minimize the risk, and make restarts easier when they are needed, by performing data
loads in smaller increments and managing the size of your VACUUM operations. For more
information, see [Load data in
sequential blocks](c_best-practices-load-data-in-sequential-blocks.md "c_best-practices-load-data-in-sequential-blocks.md") and [Vacuuming tables](t_Reclaiming_storage_space202.md "t_Reclaiming_storage_space202.md").

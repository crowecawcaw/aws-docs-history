Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Automatic table optimization

Automatic table optimization is a self-tuning capability that automatically optimizes the
design of tables by applying sort and distribution keys without the need for administrator
intervention. By using automation to tune the design of tables, you can get started and get
the fastest performance without investing time to manually tune and implement table
optimizations.

Automatic table optimization continuously observes how queries interact with tables. It
uses advanced artificial intelligence methods to choose sort and distribution keys to
optimize performance for the cluster's workload. If Amazon Redshift determines that applying a key
improves cluster performance, tables are automatically altered within hours from the time
the cluster was created, with minimal impact to queries.

To take advantage of this automation, an Amazon Redshift administrator creates a new table, or alters an existing table to enable it to use automatic optimization.
Existing tables with a distribution style or sort key of `AUTO` are already enabled for automation.
When you run queries against those tables,
Amazon Redshift determines if a sort key or distribution key will improve performance.
If so, then Amazon Redshift automatically modifies the table without requiring administrator intervention.
If a minimum number of queries are run, optimizations are applied within hours of the cluster being launched.

If Amazon Redshift determines that a distribution key improves the performance of queries, tables where
distribution style is `AUTO` can have their distribution style changed to
`KEY`.

###### Topics

- [Enabling, disabling, and monitoring automatic table optimization](c_ato-enabling-disabling-monitoring.md "c_ato-enabling-disabling-monitoring.md")
- [Managing workload exclusions from Autonomics](t_Manage_workload_exclusion.md "t_Manage_workload_exclusion.md")
- [Column compression to reduce the size of stored data](t_Compressing_data_on_disk.md "t_Compressing_data_on_disk.md")
- [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md")
- [Sort keys](t_Sorting_data.md "t_Sorting_data.md")
- [Table constraints](t_Defining_constraints.md "t_Defining_constraints.md")

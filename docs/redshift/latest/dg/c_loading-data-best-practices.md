Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift best practices for loading

data

Loading very large datasets can take a long time and consume a lot of computing
resources. How your data is loaded can also affect query performance. This section presents
best practices for loading data efficiently using COPY commands, bulk inserts, and staging
tables.

###### Topics

- [Learn how to load data with a tutorial](c_best-practices-loading-take-loading-data-tutorial.md "c_best-practices-loading-take-loading-data-tutorial.md")
- [Use a COPY command to load data](c_best-practices-use-copy.md "c_best-practices-use-copy.md")
- [Use a single COPY command to load
  from multiple files](c_best-practices-single-copy-command.md "c_best-practices-single-copy-command.md")
- [Loading data files](c_best-practices-use-multiple-files.md "c_best-practices-use-multiple-files.md")
- [Compressing your data files](c_best-practices-compress-data-files.md "c_best-practices-compress-data-files.md")
- [Verify data files before and
  after a load](c_best-practices-verifying-data-files.md "c_best-practices-verifying-data-files.md")
- [Use a multi-row insert](c_best-practices-multi-row-inserts.md "c_best-practices-multi-row-inserts.md")
- [Use a bulk insert](c_best-practices-bulk-inserts.md "c_best-practices-bulk-inserts.md")
- [Load data in sort key order](c_best-practices-sort-key-order.md "c_best-practices-sort-key-order.md")
- [Load data in
  sequential blocks](c_best-practices-load-data-in-sequential-blocks.md "c_best-practices-load-data-in-sequential-blocks.md")
- [Use time-series tables](c_best-practices-time-series-tables.md "c_best-practices-time-series-tables.md")
- [Schedule around maintenance
  windows](c_best-practices-avoid-maintenance.md "c_best-practices-avoid-maintenance.md")

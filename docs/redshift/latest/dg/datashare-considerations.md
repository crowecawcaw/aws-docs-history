Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for data sharing in

Amazon Redshift

With Amazon Redshift _data sharing_, you can securely share
access to live data across Amazon Redshift clusters, workgroups, AWS accounts, and AWS Regions
without manually moving or copying the data. Previously, objects in datashares were read
only in all circumstances. Writing to an object in a datashare is a new feature. Objects
in datashares are only write-enabled when a producer specifically grants write
privileges like INSERT or CREATE on objects to the datashare. Additionally, for
cross-account sharing, a producer has to authorize the datashare for writes and the
consumer has to associate specific clusters and workgroups for writes.

This section covers considerations when working with Amazon Redshift data sharing.

###### Topics

- [General considerations for data
  sharing in Amazon Redshift](considerations-datashare-general.md "considerations-datashare-general.md")
- [Considerations for data sharing
  reads and writes in Amazon Redshift](considerations-datashare-reads-writes.md "considerations-datashare-reads-writes.md")
- [Considerations for data sharing with
  data lake tables in Amazon Redshift](considerations-datashare-datalake.md "considerations-datashare-datalake.md")
- [Considerations for data sharing with AWS Lake Formation in
  Amazon Redshift](lake-formation-considerations.md "lake-formation-considerations.md")
- [Considerations for data sharing with AWS Data Exchange in
  Amazon Redshift](adx-considerations.md "adx-considerations.md")
- [Permissions you can grant to datashares](permissions-datashares.md "permissions-datashares.md")
- [Supported SQL statements for
  data sharing writes on consumers](multi-warehouse-writes-sql-statements.md "multi-warehouse-writes-sql-statements.md")
- [Unsupported SQL
  statements for data sharing writes on consumers](multi-warehouse-writes-sql-statements-unsupported.md "multi-warehouse-writes-sql-statements-unsupported.md")

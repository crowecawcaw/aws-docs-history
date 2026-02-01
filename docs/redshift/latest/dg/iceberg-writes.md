Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Writing to Apache Iceberg tables

With Amazon Redshift, you can create and write to Apache Iceberg tables stored in
Amazon S3 and Amazon S3 table buckets. Writing Iceberg data directly from Amazon Redshift
streamlines your data management by eliminating extra tools. Iceberg tables must be
registered with AWS Glue Data Catalog.

You can use lakehouse architecture with Apache Iceberg tables while simultaneously taking
advantage of Amazon Redshift's powerful SQL analytics across both warehouses and lakes. You
also gain immediate access to advanced Amazon Redshift features like materialized views on
your Iceberg tables, significantly enhancing your analytical capabilities without adding
complexity.

Iceberg writes is supported on both Amazon Redshift provisioned clusters and Amazon Redshift Serverless
instances.

###### Topics

- [SQL commands](iceberg-writes-sql-syntax.md "iceberg-writes-sql-syntax.md")
- [Transaction semantics](iceberg-writes-transaction-semantics.md "iceberg-writes-transaction-semantics.md")
- [Best practices](iceberg-writes-best-practices.md "iceberg-writes-best-practices.md")

Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift Spectrum

This section describes how to use Redshift Spectrum to efficiently read data from Amazon S3.

Using Amazon Redshift Spectrum, you can efficiently query and retrieve structured and semi-structured
data from files in Amazon S3 without having to load the data into Amazon Redshift tables. Redshift Spectrum
queries employ massive parallelism to run very fast against large datasets. Much of the
processing occurs in the Redshift Spectrum layer, and most of the data remains in Amazon S3.
Multiple clusters can concurrently query the same dataset in Amazon S3 without the need to make
copies of the data for each cluster.

###### Topics

- [Amazon Redshift Spectrum overview](c-spectrum-overview.md "c-spectrum-overview.md")
- [Getting started with Amazon Redshift
  Spectrum](c-getting-started-using-spectrum.md "c-getting-started-using-spectrum.md")
- [IAM policies for Amazon Redshift Spectrum](c-spectrum-iam-policies.md "c-spectrum-iam-policies.md")
- [Redshift Spectrum and AWS Lake Formation](spectrum-lake-formation.md "spectrum-lake-formation.md")
- [Data files for queries in Amazon Redshift
  Spectrum](c-spectrum-data-files.md "c-spectrum-data-files.md")
- [External schemas in Amazon Redshift
  Spectrum](c-spectrum-external-schemas.md "c-spectrum-external-schemas.md")
- [External tables for Redshift Spectrum](c-spectrum-external-tables.md "c-spectrum-external-tables.md")
- [Using Apache Iceberg tables with Amazon Redshift](querying-iceberg.md "querying-iceberg.md")
- [Amazon Redshift Spectrum query
  performance](c-spectrum-external-performance.md "c-spectrum-external-performance.md")
- [Data handling options](t_setting-data-handling-options.md "t_setting-data-handling-options.md")
- [Example: Performing correlated subqueries in Redshift Spectrum](c_performing-correlated-subqueries-spectrum.md "c_performing-correlated-subqueries-spectrum.md")
- [Metrics in Amazon Redshift Spectrum](c-spectrum-metrics.md "c-spectrum-metrics.md")
- [Query troubleshooting in Amazon Redshift
  Spectrum](c-spectrum-troubleshooting.md "c-spectrum-troubleshooting.md")
- [Tutorial: Querying nested data with Amazon Redshift
  Spectrum](tutorial-query-nested-data.md "tutorial-query-nested-data.md")

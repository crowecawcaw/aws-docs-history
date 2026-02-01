Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data into a database

You can use query editor v2 to load data into a database in an Amazon Redshift cluster or workgroup.
This section covers how to load sample data, data from S3, and data from a local file setup
and workflow.

## Sample data

The query editor v2 comes with sample data and notebooks available to be loaded into a sample database and corresponding schema.

To load sample data, choose the
![External](images/external.png)
icon associated with the sample data you want to load. The query editor v2
then loads the data into a schema in database `sample_data_dev` and creates a
folder of saved notebooks.

The following sample datasets are available.

**tickit**

Most of the examples in the Amazon Redshift documentation use sample data
called `tickit`. This data consists of seven tables: two fact
tables and five dimensions. When you load this data, the schema
`tickit` is updated with sample data. For more information
about the `tickit` data, see [Sample database](../dg/c_sampledb.md "../dg/c_sampledb.md") in the
_Amazon Redshift Database Developer Guide_.

**tpch**

This data is used for a decision support benchmark. When you load this
data, the schema `tpch` is updated with sample data. For more
information about the `tpch` data, see [TPC-H](http://www.tpc.org/tpch/ "http://www.tpc.org/tpch/").

**tpcds**

This data is used for a decision support benchmark. When you load this
data, the schema `tpcds` is updated with sample data. For more
information about the `tpcds` data, see [TPC-DS](http://www.tpc.org/tpcds/ "http://www.tpc.org/tpcds/").

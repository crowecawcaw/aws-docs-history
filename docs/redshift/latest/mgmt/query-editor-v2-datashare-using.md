Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Datashares

You can create a datashare so that users on another cluster can query the data. The
cluster containing the data that you want to share is called the
_producer_ cluster. You create a datashare on the producer
cluster for the database objects that you want to share. You can share schemas, tables,
views, and SQL user-defined functions (UDFs). The cluster that you want to share the
data to is called the _consumer_ cluster. On the consumer cluster,
you create a database from the datashare. Then, users on the consumer cluster can query
the data. For more information, see [Getting started with data
sharing](../dg/getting-started-datasharing.md "../dg/getting-started-datasharing.md") in the _Amazon Redshift Database Developer Guide_.

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying data on remote database managers

You can join data from an Amazon RDS database and an Amazon Aurora database with
data in your Amazon Redshift database using a federated query. You can use Amazon Redshift to query
operational data directly (without moving it), apply transformations, and insert data into
your Redshift tables. Some of the computation for federated queries is distributed to the
remote data sources.

To run federated queries, Amazon Redshift first makes a connection to the remote data
source. Amazon Redshift then retrieves metadata about the tables in the remote data source, issues
queries, and then retrieves the result rows. Amazon Redshift then distributes the result rows to
Amazon Redshift compute nodes for further processing.

For information about setting up your environment for federated queries, see one
of the following topics in the _Amazon Redshift Database Developer Guide_:

- [Getting started with using federated queries to PostgreSQL](../dg/getting-started-federated.md "../dg/getting-started-federated.md")
- [Getting started with using federated queries to MySQL](../dg/getting-started-federated-mysql.md "../dg/getting-started-federated-mysql.md")

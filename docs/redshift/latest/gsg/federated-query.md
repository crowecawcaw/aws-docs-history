

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Querying data on remote database managers
<a name="federated-query"></a>

You can join data from an Amazon RDS database and an Amazon Aurora database with data in your Amazon Redshift database using a federated query. You can use Amazon Redshift to query operational data directly (without moving it), apply transformations, and insert data into your Redshift tables. Some of the computation for federated queries is distributed to the remote data sources.

To run federated queries, Amazon Redshift first makes a connection to the remote data source. Amazon Redshift then retrieves metadata about the tables in the remote data source, issues queries, and then retrieves the result rows. Amazon Redshift then distributes the result rows to Amazon Redshift compute nodes for further processing. 

For information about setting up your environment for federated queries, see one of the following topics in the *Amazon Redshift Database Developer Guide*:
+ [Getting started with using federated queries to PostgreSQL](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-federated.html)
+ [Getting started with using federated queries to MySQL ](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-federated-mysql.html)


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Load data
<a name="cm-dev-t-load-sample-data"></a>

Many of the examples in this guide use the TICKIT sample dataset. You can download the file [tickitdb.zip](samples/tickitdb.zip), which contains individual sample data files. You can then upload the sample data to your own Amazon S3 bucket.

To load the sample data for your database, first create the tables. Then use the COPY command to load the tables with sample data that is stored in an Amazon S3 bucket. For steps to create tables and load sample data, see [Step 4: Load data from Amazon S3 to Amazon Redshift](new-user.md#rs-gsg-create-sample-db).
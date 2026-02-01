Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Load data

Many of the examples in this guide use the TICKIT sample dataset. You can download the file [tickitdb.zip](samples/tickitdb.md "samples/tickitdb.md"), which
contains individual sample data files. You can then upload the sample data to your own Amazon S3 bucket.

To load the sample data for your database, first create the tables. Then use the COPY
command to load the tables with sample data that is stored in an Amazon S3 bucket. For steps
to create tables and load sample data, see [Step 4: Load data from Amazon S3 to Amazon Redshift](new-user.md#rs-gsg-create-sample-db "new-user.md#rs-gsg-create-sample-db").

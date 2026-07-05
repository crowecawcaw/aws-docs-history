Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Use a COPY command to load data

The COPY command loads data in parallel from Amazon S3, Amazon EMR, Amazon DynamoDB, or multiple data
sources on remote hosts. COPY loads large amounts of data much more efficiently than
using INSERT statements, and stores the data more effectively as well.

For more information about using the COPY command, see [Loading data from Amazon S3](t_Loading-data-from-S3.md "t_Loading-data-from-S3.md") and [Loading data from an Amazon DynamoDB table](t_Loading-data-from-dynamodb.md "t_Loading-data-from-dynamodb.md").

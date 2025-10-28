Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using Amazon Redshift with other

services

This section describes how you can use other services as sources and destinations for Amazon Redshift data.

Amazon Redshift integrates with other AWS services to enable you to move, transform, and load
your data quickly and reliably, using data security features.

S3
Amazon Simple Storage Service (Amazon S3) is a web service that stores data in the cloud. Amazon Redshift leverages
parallel processing to read and load data from multiple data files stored in Amazon S3
buckets. For more information, see [Loading data from Amazon S3](t_Loading-data-from-S3.md "t_Loading-data-from-S3.md").

You can also use parallel processing to export data from your Amazon Redshift data
warehouse to multiple data files on Amazon S3. For more information, see [Unloading data in Amazon Redshift](c_unloading_data.md "c_unloading_data.md").

DynamoDB
Amazon DynamoDB is a fully managed NoSQL database service. You can use the COPY command
to load an Amazon Redshift table with data from a single Amazon DynamoDB table. For more
information, see [Loading data from an Amazon DynamoDB
table](t_Loading-data-from-dynamodb.md "t_Loading-data-from-dynamodb.md").

SSH
You can use the COPY command in Amazon Redshift to load data from one or more remote hosts,
such as Amazon EMR clusters, Amazon EC2 instances, or other computers. COPY connects to the
remote hosts using SSH and runs commands on the remote hosts to generate data.
Amazon Redshift supports multiple simultaneous connections. The COPY command reads and
loads the output from multiple host sources in parallel. For more information, see
[Loading data from remote hosts](loading-data-from-remote-hosts.md "loading-data-from-remote-hosts.md").

AWS DMS
You can migrate data to Amazon Redshift using AWS Database Migration Service. AWS DMS can migrate your data to and
from most widely used commercial and open-source databases such as Oracle,
PostgreSQL, Microsoft SQL Server, Amazon Redshift, Aurora DB cluster, DynamoDB, Amazon S3, MariaDB, and MySQL. For
more information, see [Using an
Amazon Redshift database as a target for AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md").

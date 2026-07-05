Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Data sources

You can load data from text files in an Amazon S3 bucket, in an Amazon EMR cluster, or on a
remote host that your cluster can access using an SSH connection. You can also load data
directly from a DynamoDB table.

The maximum size of a single input row from any source is 4 MB.

To export data from a table to a set of files in an Amazon S3, use the [UNLOAD](r_UNLOAD.md "r_UNLOAD.md") command.

######

- [COPY from Amazon S3](copy-parameters-data-source-s3.md "copy-parameters-data-source-s3.md")
- [COPY from Amazon EMR](copy-parameters-data-source-emr.md "copy-parameters-data-source-emr.md")
- [COPY from remote host (SSH)](copy-parameters-data-source-ssh.md "copy-parameters-data-source-ssh.md")
- [COPY from Amazon DynamoDB](copy-parameters-data-source-dynamodb.md "copy-parameters-data-source-dynamodb.md")

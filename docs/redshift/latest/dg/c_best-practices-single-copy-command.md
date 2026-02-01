Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Use a single COPY command to load

from multiple files

Amazon Redshift can automatically load in parallel from multiple compressed data files.
You can specify the files to be loaded by using an Amazon S3 object prefix or by using a manifest file.

However, if you use multiple concurrent COPY commands to load one table from multiple files,
Amazon Redshift is forced to perform a serialized load. This type of load is much slower and
requires a VACUUM process at the end if the table has a sort column defined. For more
information about using COPY to load data in parallel, see [Loading data from Amazon S3](t_Loading-data-from-S3.md "t_Loading-data-from-S3.md").

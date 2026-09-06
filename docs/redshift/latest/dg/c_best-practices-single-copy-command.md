

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Use a single COPY command to load from multiple files
<a name="c_best-practices-single-copy-command"></a>

Amazon Redshift can automatically load in parallel from multiple compressed data files. You can specify the files to be loaded by using an Amazon S3 object prefix or by using a manifest file.

However, if you use multiple concurrent COPY commands to load one table from multiple files, Amazon Redshift is forced to perform a serialized load. This type of load is much slower and requires a VACUUM process at the end if the table has a sort column defined. For more information about using COPY to load data in parallel, see [Loading data from Amazon S3](t_Loading-data-from-S3.md).
Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Load data is incorrect

Your COPY operation can load incorrect data in the following ways. We suggest the
following troubleshooting approaches.

###### Wrong files are loaded

Using an object prefix to specify data files can cause unwanted files to be read.
Instead, use a manifest file to specify exactly which files to load. For more
information, see the [copy_from_s3_manifest_file](copy-parameters-data-source-s3.md#copy-manifest-file "copy-parameters-data-source-s3.md#copy-manifest-file") option for the COPY command
and [Example: COPY from Amazon S3 using a manifest](r_COPY_command_examples.md#copy-command-examples-manifest "r_COPY_command_examples.md#copy-command-examples-manifest") in the COPY examples.

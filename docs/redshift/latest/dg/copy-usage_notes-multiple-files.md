Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Errors when reading multiple

files

The COPY command is atomic and transactional. In other words, even when the COPY
command reads data from multiple files, the entire process is treated as a single
transaction. If COPY encounters an error reading a file, it automatically retries until
the process times out (see [statement_timeout](r_statement_timeout.md "r_statement_timeout.md")) or if data can't be download from Amazon S3 for a
prolonged period of time (between 15 and 30 minutes), ensuring that each file is loaded
only once. If the COPY command fails, the entire transaction is canceled and all changes
are rolled back. For more information about handling load errors, see [Troubleshooting data loads](t_Troubleshooting_load_errors.md "t_Troubleshooting_load_errors.md").

After a COPY command is successfully initiated, it doesn't fail if the session
terminates, for example when the client disconnects. However, if the COPY command is
within a BEGIN … END transaction block that doesn't complete because the session
terminates, the entire transaction, including the COPY, is rolled back. For more
information about transactions, see [BEGIN](r_BEGIN.md "r_BEGIN.md").

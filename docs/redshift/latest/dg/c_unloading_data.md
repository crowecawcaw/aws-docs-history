Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unloading data in Amazon Redshift

To unload data from database tables to a set of files in an Amazon S3 bucket, you can
use the [UNLOAD](r_UNLOAD.md "r_UNLOAD.md") command with a SELECT
statement. You can unload text data in either delimited format or fixed-width format,
regardless of the data format that was used to load it. You can also specify whether to
create compressed GZIP files.

You can limit the access users have to your Amazon S3 bucket by using temporary security
credentials.

###### Topics

- [Unloading data to Amazon S3](t_Unloading_tables.md "t_Unloading_tables.md")
- [Unloading encrypted data files](t_unloading_encrypted_files.md "t_unloading_encrypted_files.md")
- [Unloading data in delimited or
  fixed-width format](t_unloading_fixed_width_data.md "t_unloading_fixed_width_data.md")
- [Reloading unloaded data](t_Reloading_unload_files.md "t_Reloading_unload_files.md")

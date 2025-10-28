Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data from Amazon S3

The COPY command leverages the Amazon Redshift massively parallel processing (MPP)

architecture to read and load data in parallel from a file or multiple files in an Amazon S3
bucket. You can take maximum advantage of parallel processing by splitting your data
into multiple files, in cases where the files are compressed. (There are exceptions to this rule. These are detailed
in [Loading data files](c_best-practices-use-multiple-files.md "c_best-practices-use-multiple-files.md").) You can also take maximum
advantage of parallel processing by setting distribution keys on your tables. For more
information about distribution keys, see [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md").

Data is loaded into the target table, one line per row. The fields in
the data file are matched to table columns in order, left to right. Fields in the data
files can be fixed-width or character delimited; the default delimiter is a pipe (|). By
default, all the table columns are loaded, but you can optionally define a
comma-separated list of columns. If a table column is not included in the column list
specified in the COPY command, it is loaded with a default value. For more information,
see [Loading default column values](c_loading_default_values.md "c_loading_default_values.md").

###### Topics

- [Loading data from compressed and uncompressed files](t_splitting-data-files.md "t_splitting-data-files.md")
- [Uploading files to Amazon S3 to use with COPY](t_uploading-data-to-S3.md "t_uploading-data-to-S3.md")
- [Using the COPY command to load from
  Amazon S3](t_loading-tables-from-s3.md "t_loading-tables-from-s3.md")

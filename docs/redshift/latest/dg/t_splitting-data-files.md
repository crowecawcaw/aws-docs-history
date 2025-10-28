Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data from compressed and uncompressed files

When you load compressed data, we recommend that you split the data for each
table into multiple files. When you load uncompressed, delimited data, the COPY command uses massively
parallel processing (MPP) and scan
ranges to load data from large files in an Amazon S3 bucket.

## Loading data from multiple compressed files

In cases where you have compressed data, we recommend that you split the data for each
table into multiple files. The COPY command can load data from multiple files in
parallel. You can load multiple files by specifying a common prefix, or
_prefix key_, for the set, or by explicitly listing the files
in a manifest file.

Split your data into files so that the number of files is a multiple of the
number of slices in your cluster. That way, Amazon Redshift can divide the data evenly
among the slices. The number of slices per node depends on the node size of the
cluster. For example, each dc2.large compute node has two slices, and each dc2.8xlarge
compute node has 16 slices. For more information about the number of slices that
each node size has, see [About
clusters and nodes](../mgmt/working-with-clusters.md#rs-about-clusters-and-nodes "../mgmt/working-with-clusters.md#rs-about-clusters-and-nodes") in the _Amazon Redshift Management Guide_.

The nodes all participate in running parallel queries, working on data that is
distributed as evenly as possible across the slices. If you have a cluster with
two dc2.large nodes, you might split your data into four files or some multiple of
four. Amazon Redshift doesn't take file size into account when dividing the
workload. Thus, you need to ensure that the files are roughly the same size, from
1 MB to 1 GB after compression.

To use object prefixes to identify the load files, name each file with a common
prefix. For example, you might split the `venue.txt` file might be
split into four files, as follows.

```
venue.txt.1
venue.txt.2
venue.txt.3
venue.txt.4
```

If you put multiple files in a folder in your bucket and specify the folder
name as the prefix, COPY loads all of the files in the folder. If you explicitly
list the files to be loaded by using a manifest file, the files can reside in
different buckets or folders.

For more information about manifest files, see [Example: COPY from Amazon S3 using a manifest](r_COPY_command_examples.md#copy-command-examples-manifest "r_COPY_command_examples.md#copy-command-examples-manifest").

## Loading data from uncompressed, delimited files

When you load uncompressed, delimited data, the COPY command uses the massively
parallel processing (MPP) architecture in Amazon Redshift. Amazon Redshift automatically uses slices working in parallel
to load ranges of data from a large file in an Amazon S3 bucket. The file must be delimited for parallel loading to occur. For
example, pipe delimited. Automatic, parallel data loading with the COPY command is also
available for CSV files. You can also take advantage of parallel processing by
setting distribution keys on your tables. For more information about distribution
keys, see [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md").

Automatic, parallel data loading isn't supported when the COPY query includes any of
the following keywords: ESCAPE, REMOVEQUOTES, and FIXEDWIDTH.

Data from the file or files is loaded into the target table, one line per row.
The fields in the data file are matched to table columns in order, left to right.
Fields in the data files can be fixed-width or character delimited; the default
delimiter is a pipe (|). By default, all the table columns are loaded, but you can
optionally define a comma-separated list of columns. If a table column isn't
included in the column list specified in the COPY command, it's loaded with a
default value. For more information, see [Loading default column values](c_loading_default_values.md "c_loading_default_values.md").

Follow this general process to load data from Amazon S3, when your data is uncompressed and delimited:

1. Upload your files to Amazon S3.
2. Run a COPY command to load the table.
3. Verify that the data was loaded correctly.

For examples of COPY commands, see [COPY examples](r_COPY_command_examples.md "r_COPY_command_examples.md"). For information about data loaded into Amazon Redshift, check the [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md") and [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md") system tables.

For more information about nodes and the slices contained in each, see [About
clusters and nodes](../mgmt/working-with-clusters.md#rs-about-clusters-and-nodes "../mgmt/working-with-clusters.md#rs-about-clusters-and-nodes") in the _Amazon Redshift Management Guide_.

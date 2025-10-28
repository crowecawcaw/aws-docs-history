Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Load takes too long

Your load operation can take too long for the following reasons. We suggest the
following troubleshooting approaches.

###### COPY loads data from a single file

Split your load data into multiple files. When you load all the data from a single
large file, Amazon Redshift is forced to perform a serialized load, which is much slower.
The number of files should be a multiple of the number of slices in your cluster, and
the files should be about equal size, between 1 MB and 1 GB after compression. For
more information, see [Amazon Redshift best practices for designing
queries](c_designing-queries-best-practices.md "c_designing-queries-best-practices.md").

###### Load operation uses multiple COPY commands

If you use multiple concurrent COPY commands to load one table from multiple
files, Amazon Redshift is forced to perform a serialized load, which is much slower. In this
case, use a single COPY command.

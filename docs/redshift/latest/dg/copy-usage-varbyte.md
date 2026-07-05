Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Loading a column of the VARBYTE data type

You can load data from a file in CSV, Parquet, and ORC format.
For CSV, the data is loaded from a file in hexadecimal representation of the VARBYTE data.
You can't load VARBYTE data with the `FIXEDWIDTH` option.
The `ADDQUOTES` or `REMOVEQUOTES` option of COPY is not supported.
A VARBYTE column can't be used as a partition column.

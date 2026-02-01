Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading a column of the VARBYTE data

type

You can load data from a file in CSV, Parquet, and ORC format.
For CSV, the data is loaded from a file in hexadecimal representation of the VARBYTE data.
You can't load VARBYTE data with the `FIXEDWIDTH` option.
The `ADDQUOTES` or `REMOVEQUOTES` option of COPY is not supported.
A VARBYTE column can't be used as a partition column.

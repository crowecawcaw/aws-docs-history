Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading multibyte data from Amazon S3

If your data includes non-ASCII multibyte characters (such as Chinese or
Cyrillic characters), you must load the data to VARCHAR columns. The VARCHAR data
type supports four-byte UTF-8 characters, but the CHAR data type only accepts
single-byte ASCII characters. You cannot load five-byte or longer characters into
Amazon Redshift tables. For more information about CHAR and VARCHAR, see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

To check which encoding an input file uses, use the Linux _`file`_ command:

```
$ file ordersdata.txt
ordersdata.txt: ASCII English text
$ file uni_ordersdata.dat
uni_ordersdata.dat: UTF-8 Unicode text
```

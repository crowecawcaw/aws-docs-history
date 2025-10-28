Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading multibyte data from Amazon S3

If your data includes non-ASCII multibyte characters (such as Chinese or Cyrillic
characters), you must load the data to VARCHAR columns. The VARCHAR data type supports
four-byte UTF-8 characters, but the CHAR data type only accepts single-byte ASCII
characters. You can't load five-byte or longer characters into Amazon Redshift tables. For
more information, see [Multibyte
characters](c_Supported_data_types.md#c_Supported_data_types-multi-byte-characters "c_Supported_data_types.md#c_Supported_data_types-multi-byte-characters").

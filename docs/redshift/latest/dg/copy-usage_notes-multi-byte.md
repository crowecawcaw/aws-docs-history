

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Loading multibyte data from Amazon S3
<a name="copy-usage_notes-multi-byte"></a>

If your data includes non-ASCII multibyte characters (such as Chinese or Cyrillic characters), you must load the data to VARCHAR columns. The VARCHAR data type supports four-byte UTF-8 characters, but the CHAR data type only accepts single-byte ASCII characters. You can't load five-byte or longer characters into Amazon Redshift tables. For more information, see [Multibyte characters](c_Supported_data_types.md#c_Supported_data_types-multi-byte-characters). 
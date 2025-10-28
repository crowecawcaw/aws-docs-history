Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading semi-structured data into Amazon Redshift

Use the SUPER data type to parse and query hierarchical and generic data in Amazon Redshift.
Amazon Redshift introduces the [JSON_PARSE function](JSON_PARSE.md "JSON_PARSE.md") to parse data in JSON format and
convert it into the SUPER representation. Amazon Redshift also supports loading SUPER columns
using the COPY command. The supported file formats are JSON, Avro, text, comma-separated
value (CSV) format, Parquet, and ORC.

You can use JSON_PARSE to insert and update JSON data into SUPER columns, or
use COPY to load JSON data into Amazon Redshift from outside sources such as from Amazon S3 buckets.

###### Topics

- [Using JSON_PARSE to insert data into SUPER columns](parse_json.md "parse_json.md")
- [Using COPY to load data into SUPER columns](copy_json.md "copy_json.md")

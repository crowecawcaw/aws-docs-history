Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Loading semi-structured data into Amazon Redshift

Use the SUPER data type to parse and query hierarchical and generic data in Amazon Redshift.
Amazon Redshift introduces the [JSON\_PARSE function](JSON_PARSE.md "JSON_PARSE.md") to parse data in JSON format and
convert it into the SUPER representation. Amazon Redshift also supports loading SUPER columns
using the COPY command. The supported file formats are JSON, Avro, text, comma-separated
value (CSV) format, Parquet, and ORC.

You can use JSON\_PARSE to insert and update JSON data into SUPER columns, or
use COPY to load JSON data into Amazon Redshift from outside sources such as from Amazon S3 buckets.

###### Topics

- [Using JSON\_PARSE to insert data into SUPER columns](parse_json.md "parse_json.md")
- [Using COPY to load data into SUPER columns](copy_json.md "copy_json.md")

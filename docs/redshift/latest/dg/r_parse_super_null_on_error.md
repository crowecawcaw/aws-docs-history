Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# parse_super_null_on_error

## Values (default in bold)

**off**, on

## Description

Specifies that when Amazon Redshift tries to parse a nonexistent member of an object or
element of an array, Amazon Redshift returns a NULL value if your query is run in the strict
mode.

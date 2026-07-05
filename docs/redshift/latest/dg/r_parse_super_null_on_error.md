Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# parse\_super\_null\_on\_error

## Values (default in bold)

**off**, on

## Description

Specifies that when Amazon Redshift tries to parse a nonexistent member of an object or
element of an array, Amazon Redshift returns a NULL value if your query is run in the strict
mode.

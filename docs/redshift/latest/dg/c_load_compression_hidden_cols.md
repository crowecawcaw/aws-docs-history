Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Optimizing storage for narrow

tables

If you have a table with very few columns but a very large number of rows, the three
hidden metadata identity columns (INSERT_XID, DELETE_XID, ROW_ID) will consume a
disproportionate amount of the disk space for the table.

In order to optimize compression of the hidden columns, load the table in a single
COPY transaction where possible. If you load the table with multiple separate COPY
commands, the INSERT_XID column will not compress well. You must perform a vacuum
operation if you use multiple COPY commands, but it will not improve compression of
INSERT_XID.

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Use the smallest possible column

size

Don't make it a practice to use the maximum column size for convenience.

Instead, consider the largest values you are likely to store in your columns and size them
accordingly.

For instance, a CHAR column for storing U.S. state and territory abbreviations used by the post office only needs to be CHAR(2).

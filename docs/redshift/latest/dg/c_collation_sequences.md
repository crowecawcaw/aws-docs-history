Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Collation sequences

Amazon Redshift doesn’t support locale-specific or user-defined collation sequences. In
general, the results of any predicate in any context could be affected by the lack of
locale-specific rules for sorting and comparing data values. For example, ORDER BY
expressions and functions such as MIN, MAX, and RANK return results based on binary
UTF8 ordering of the data that does not take locale-specific characters into
account.

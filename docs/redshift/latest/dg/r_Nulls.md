Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Nulls

If a column in a row is missing, unknown, or not applicable, it is a null value or
is said to contain null. Nulls can appear in fields of any data type that are not
restricted by primary key or NOT NULL constraints. A null is not equivalent to the
value zero or to an empty string.

Any arithmetic expression containing a null always evaluates to a null. All
operators return a null when given a null argument or operand.

To test for nulls, use the comparison conditions IS NULL and IS NOT NULL. Because
null represents a lack of data, a null is not equal or unequal to any value or to
another null.

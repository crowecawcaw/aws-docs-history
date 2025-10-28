Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# spectrum_enable_pseudo_columns

## Values (default in bold)

**true**, false

## Description

You can
disable the creation of pseudocolumns for a session by setting the
`spectrum_enable_pseudo_columns` configuration parameter to
`false`.

## Example

The following command disables the creation of pseudocolumns for a session.

```
set spectrum_enable_pseudo_columns to false;

```

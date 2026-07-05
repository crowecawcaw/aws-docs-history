Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# spectrum\_enable\_pseudo\_columns

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

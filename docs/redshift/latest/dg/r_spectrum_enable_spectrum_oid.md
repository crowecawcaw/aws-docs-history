Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# enable\_spectrum\_oid

## Values (default in bold)

**true**, false

## Description

You can also disable only the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

## Example

The following command disables the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

```
set enable_spectrum_oid to false;
```

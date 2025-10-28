Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# enable_spectrum_oid

## Values (default in bold)

**true**, false

## Description

You can also disable only the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

## Example

The following command disables the `$spectrum_oid` pseudocolumn by setting the `enable_spectrum_oid` configuration parameter to `false`.

```
set enable_spectrum_oid to false;
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# enable_vacuum_boost

## Values (default in bold)

**false**, true

## Description

Specifies whether to enable the vacuum boost option for all VACUUM commands run in a
session. If `enable_vacuum_boost` is `true`, Amazon Redshift runs all VACUUM
commands in the session with the BOOST option. If `enable_vacuum_boost` is
`false`, Amazon Redshift doesn't run with the BOOST option by default.
For more information about the BOOST option, see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

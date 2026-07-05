Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# enable\_vacuum\_boost

## Values (default in bold)

**false**, true

## Description

Specifies whether to enable the vacuum boost option for all VACUUM commands run in a
session. If `enable_vacuum_boost` is `true`, Amazon Redshift runs all VACUUM
commands in the session with the BOOST option. If `enable_vacuum_boost` is
`false`, Amazon Redshift doesn't run with the BOOST option by default.
For more information about the BOOST option, see [VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

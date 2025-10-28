Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift RSQL environment

variables

Amazon Redshift RSQL can use environment variables to select default parameter values.

## RSPASSWORD

###### Important

We don't recommend using this environment variable for security reasons,
as some operating systems allow non-administrative users to see process
environment variables.

Sets the password for Amazon Redshift RSQL to use when connecting to Amazon Redshift. This
environment variable requires Amazon Redshift RSQL 1.0.4 and above.

RSQL prioritizes RSPASSWORD if one is set. If RSPASSWORD is not set and
you're connecting using a DSN, RSQL takes the password from the DSN file's
parameters. Finally, if RSPASSWORD is not set and you're not using a DSN, RSQL
provides a password prompt after attempting to connect.

The following is an example of setting an RSPASSWORD:

```
export RSPASSWORD=TestPassw0rd
```

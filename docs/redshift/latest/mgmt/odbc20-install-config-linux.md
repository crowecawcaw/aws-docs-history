Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an Amazon Redshift ODBC driver on

Linux

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift
data warehouse. For each computer where you install the driver, there are the following
minimum requirements:

- Root access on the machine.
- One of the following distributions:
  - Red Hat® Enterprise Linux® (RHEL) 8 or later
  - CentOS 8 or later.

- 150 MB of available disk space.
- unixODBC 2.2.14 or later.
- glibc 2.26 or later.

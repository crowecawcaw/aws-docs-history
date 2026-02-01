Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an Amazon Redshift ODBC driver on Apple macOS

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift
data warehouse. For each computer where you install the driver, these are the following
minimum requirements:

- Root access on the machine.
- Apple macOS System Requirements:
  - A 64-bit version of Apple macOS version 11.7 or higher (such as Apple macOS Big Sur, Monterey, Ventura or later) is required. The Redshift ODBC driver only supports 64-bit client applications.
  - 150 MB of available disk space.
  - The driver supports applications built with iODBC 3.52.9+ or unixODBC 2.3.7+.

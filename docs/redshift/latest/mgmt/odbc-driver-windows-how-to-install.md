Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Downloading and installing the Amazon Redshift ODBC

driver

Use the following procedure to download the Amazon Redshift ODBC drivers for
Windows operating systems. Only use a driver other than these if you're
running a third-party application that is certified for use with Amazon Redshift
and that requires a specific driver.

###### To install the ODBC driver

1. Download one of the following, depending on the system
   architecture of your SQL client tool or application:
   - [64-bit ODBC driver version 1.6.1](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC64-1.6.1.1000.msi "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC64-1.6.1.1000.msi")

   The name for this driver is Amazon Redshift (x64).
   - [32-bit ODBC driver version 1.4.52](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.52.1000/AmazonRedshiftODBC32-1.4.52.1000.msi "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.52.1000/AmazonRedshiftODBC32-1.4.52.1000.msi")

   The name for this driver is Amazon Redshift (x86). The 32-bit
   ODBC drivers are discontinued. Further updates will not be
   released, except for urgent security patches.

###### Note

Download the MSI package that corresponds to the system
architecture of your SQL client tool or application. For
example, if your SQL client tool is 64-bit, install the 64-bit
driver.

Then download and review the [Amazon Redshift ODBC and JDBC driver license agreement](https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf"). 2. Double-click the .msi file, and then follow the steps in the
wizard to install the driver.

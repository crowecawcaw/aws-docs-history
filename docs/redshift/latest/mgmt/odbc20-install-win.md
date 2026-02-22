Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Downloading and installing the Amazon Redshift ODBC driver

Use the following procedure to download and install the Amazon Redshift ODBC driver for
Windows operating systems. Only use a different driver if you're running a
third-party application that is certified for use with Amazon Redshift, and that
application requires that specific driver.

To download and install the ODBC driver:

1. Download the following driver: [64-bit ODBC driver version 2.1.13.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.1.13.0/AmazonRedshiftODBC64-2.1.13.0.msi "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.1.13.0/AmazonRedshiftODBC64-2.1.13.0.msi")

The name for this driver is **Amazon Redshift ODBC Driver
(x64)**. 2. Review the [Amazon Redshift ODBC driver version 2.x license](https://github.com/aws/amazon-redshift-odbc-driver/blob/master/LICENSE "https://github.com/aws/amazon-redshift-odbc-driver/blob/master/LICENSE"). 3. Double-click the .msi file, then follow the steps in the wizard to install
the driver.

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Downloading and installing the Amazon Redshift ODBC driver

Use the steps in this section to download and install the Amazon Redshift ODBC
driver on a supported version of macOS X. The installation process installs
the driver files in the following directories:

- `/opt/amazon/redshift/lib/universal`
- `/opt/amazon/redshift/ErrorMessages`
- `/opt/amazon/redshift/Setup`

###### To install the Amazon Redshift

ODBC driver on macOS X

1. If your macOS X system uses Intel architecture, download the [macOS X Intel driver version 1.5.20](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.5.20.1024/AmazonRedshiftODBC-1.5.20.1024.x86_64.dmg "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.5.20.1024/AmazonRedshiftODBC-1.5.20.1024.x86_64.dmg").
   If your system uses ARM architecture, download the [macOS X ARM driver version 1.5.20](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.5.20.1024/AmazonRedshiftODBC-1.5.20.1024.arm64.dmg "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.5.20.1024/AmazonRedshiftODBC-1.5.20.1024.arm64.dmg").
   In both cases, the name for this driver is Amazon Redshift ODBC driver.

Then download and review the [Amazon Redshift ODBC and JDBC driver license agreement](https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf"). 2. Double-click **AmazonRedshiftODBC.dmg** to mount
the disk image. 3. Double-click **AmazonRedshiftODBC.pkg** to run
the installer. 4. Follow the steps in the installer to complete the driver
installation process. To perform the installation, agree to the
terms of the license agreement.

###### Important

When you have finished installing the driver, configure it for use on
your system. For more information on driver configuration, see [Use an ODBC driver manager to
configure the driver](odbc-driver-configure-mac.md "odbc-driver-configure-mac.md").

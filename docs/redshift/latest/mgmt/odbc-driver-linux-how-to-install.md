Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Downloading and installing the Amazon Redshift ODBC driver

Use the steps in this section to download and install the Amazon Redshift ODBC
drivers on a supported Linux distribution. The installation process installs
the driver files in the following directories:

- `/opt/amazon/redshiftodbc/lib/64` (for the 64-bit
  driver)
- `/opt/amazon/redshiftodbc/ErrorMessages`
- `/opt/amazon/redshiftodbc/Setup`
- `/opt/amazon/redshiftodbc/lib/32` (for the 32-bit
  driver)

###### To install the Amazon Redshift

ODBC driver

1.  Download one of the following, depending on the system
    architecture of your SQL client tool or application:

        * [64-bit RPM driver version 1.6.1](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC-64-bit-1.6.1.1000-1.x86_64.rpm "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC-64-bit-1.6.1.1000-1.x86_64.rpm")
        * [64-bit Debian driver version 1.6.1](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC-64-bit-1.6.1.1000-1.x86_64.deb "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/AmazonRedshiftODBC-64-bit-1.6.1.1000-1.x86_64.deb")
        * [32-bit driver version 1.4.52](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.52.1000/AmazonRedshiftODBC-32-bit-1.4.52.1000-1.i686.rpm "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.52.1000/AmazonRedshiftODBC-32-bit-1.4.52.1000-1.i686.rpm")

    The name for each of these drivers is Amazon Redshift ODBC driver. The
    32-bit ODBC drivers are discontinued. Further updates will not be
    released, except for urgent security patches.

###### Note

Download the package that corresponds to the system
architecture of your SQL client tool or application. For
example, if your client tool is 64-bit, install a 64-bit
driver.

Then download and review the [Amazon Redshift ODBC and JDBC driver license agreement](https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf"). 2. Go to the location where you downloaded the package, and then run
one of the following commands. Use the command that corresponds to
your Linux distribution.

    * On RHEL and CentOS operating
     systems, run the following command.



    ```
    yum -nogpgcheck localinstall `RPMFileName`
    ```

    Replace
     ``RPMFileName`` with
     the RPM package file name. For example, the following
     command demonstrates installing the 64-bit driver.



    ```
    yum -nogpgcheck localinstall AmazonRedshiftODBC-64-bit-1.x.xx.xxxx-x.x86_64.rpm
    ```
    * On SLES, run the following command.



    ```
    zypper install `RPMFileName`
    ```

    Replace
     ``RPMFileName`` with
     the RPM package file name. For example, the following
     command demonstrates installing the 64-bit driver.



    ```
    zypper install AmazonRedshiftODBC-1.x.x.xxxx-x.x86_64.rpm
    ```
    * On Debian, run the following command.



    ```
    sudo apt install ./`DEBFileName.deb`
    ```

    Replace
     ``DEBFileName.deb``
     with the Debian package file name. For example, the
     following command demonstrates installing the 64-bit
     driver.



    ```
    sudo apt install ./AmazonRedshiftODBC-1.x.x.xxxx-x.x86_64.deb
    ```

###### Important

When you have finished installing the drivers, configure them for use
on your system. For more information on driver configuration, see [Using an ODBC driver manager to
configure the driver](odbc-driver-configure-linux.md "odbc-driver-configure-linux.md").

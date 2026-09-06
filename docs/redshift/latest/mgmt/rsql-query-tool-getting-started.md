

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Getting started with Amazon Redshift RSQL
<a name="rsql-query-tool-getting-started"></a>

Install Amazon Redshift RSQL on a computer with a Linux, macOS, or Microsoft Windows operating system.

## Download RSQL
<a name="rsql-query-tool-download"></a>
+ Linux 64-bit RPM: [RSQL Version 1.1.2](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.2/AmazonRedshiftRsql-1.1.2.rhel.x86_64.rpm) 
  + Linux Artifact Signature Key: [Key](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.2/AmazonRedshiftRsql-1.1.2-certificate.pem) 
  + Linux Artifact Signed Hash: [Hash](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.2/AmazonRedshiftRsql-1.1.2-signature.bin) 
+ Mac OS 64-bit PKG: [RSQL Version 1.1.2](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.2/AmazonRedshiftRsql-1.1.2.universal.pkg) 
+ Windows 64-bit MSI: [RSQL Version 1.1.2](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.2/AmazonRedshiftRsql-1.1.2.x86_64.msi) 

See the change log and downloads for previous versions at [Amazon Redshift RSQL change log](rsql-query-tool-changelog.md).

## Install RSQL for Linux
<a name="rsql-query-tool-linux-install"></a>

Follow the steps below to install RSQL for Linux.

1. Install the driver manager with the following command:

   ```
   sudo yum install unixODBC
   ```

1. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC driver](odbc20-install-linux.md).

1. Copy the ini file to your home directory:

   ```
   cp /opt/amazon/redshiftodbcx64/odbc.ini ~/.odbc.ini
   ```

1. Set the environment variables to point to the location of the file:

   ```
   export ODBCINI=~/.odbc.ini
   export ODBCSYSINI=/opt/amazon/redshiftodbcx64/
   export AMAZONREDSHIFTODBCINI=/opt/amazon/redshiftodbcx64/amazon.redshiftodbc.ini
   ```

1. You can now install RSQL by running the following command.

   ```
   sudo rpm -i AmazonRedshiftRsql-<version>.rhel.x86_64.rpm
   ```

## Install RSQL for Mac
<a name="rsql-query-tool-mac-install"></a>

Follow the steps below to install RSQL for Mac OSX.

1. Install the driver manager with the following command:

   ```
   brew install unixodbc --build-from-source
   ```

1. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC driver](odbc-driver-mac-how-to-install.md).

1. Copy the ini file to your home directory:

   ```
   cp /opt/amazon/redshift/Setup/odbc.ini ~/.odbc.ini
   ```

1. Set the environment variables to point to the location of the file:

   ```
   export ODBCINI=~/.odbc.ini
   export ODBCSYSINI=/opt/amazon/redshift/Setup
   export AMAZONREDSHIFTODBCINI=/opt/amazon/redshift/lib/amazon.redshiftodbc.ini
   ```

1. Set `DYLD_LIBRARY_PATH` to location of your libodbc.dylib if its not in `/usr/local/lib`.

   ```
   export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/usr/local/lib
   ```

1. Double-click the pkg file to run the installer.

1. Follow the steps in the installer to complete the installation. Agree to the terms of the license agreement.

## Install RSQL for Windows
<a name="rsql-query-tool-windows-install"></a>

Follow the steps below to install RSQL for Windows.

1. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC driver](odbc-driver-windows-how-to-install.md).

1. Double-click the RSQL download file to run the installer, then follow the prompts to complete the installation.
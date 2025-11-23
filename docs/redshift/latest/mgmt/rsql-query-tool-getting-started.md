Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with Amazon Redshift

RSQL

Install Amazon Redshift RSQL on a computer with a Linux, macOS, or Microsoft Windows
operating system.

## Download RSQL

- Linux 64-bit RPM: [RSQL Version 1.1.1](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.rhel.x86_64.rpm "https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.rhel.x86_64.rpm")
  - Linux Artifact Signature Key: [Key](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1-certificate.pem "https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1-certificate.pem")
  - Linux Artifact Signed Hash: [Hash](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1-signature.bin "https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1-signature.bin")

- Mac OS 64-bit PKG: [RSQL Version 1.1.1](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.universal.pkg "https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.universal.pkg")
- Windows 64-bit MSI: [RSQL Version 1.1.1](https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.x86_64.msi "https://s3.amazonaws.com/redshift-downloads/amazon-redshift-rsql/1.1.1/AmazonRedshiftRsql-1.1.1.x86_64.msi")

See the change log and downloads for previous versions at [Amazon Redshift RSQL change log](rsql-query-tool-changelog.md "rsql-query-tool-changelog.md").

## Install RSQL for

Linux

Follow the steps below to install RSQL for Linux.

1. Install the driver manager with the following command:

```
sudo yum install unixODBC
```

2. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC driver](odbc20-install-linux.md "odbc20-install-linux.md").
3. Copy the ini file to your home directory:

```
cp /opt/amazon/redshiftodbcx64/odbc.ini ~/.odbc.ini
```

4. Set the environment variables to point to the location of the
   file:

```
export ODBCINI=~/.odbc.ini
export ODBCSYSINI=/opt/amazon/redshiftodbcx64/
export AMAZONREDSHIFTODBCINI=/opt/amazon/redshiftodbcx64/amazon.redshiftodbc.ini
```

5. You can now install RSQL by running the following command.

```
sudo rpm -i AmazonRedshiftRsql-<version>.rhel.x86_64.rpm
```

## Install RSQL for Mac

Follow the steps below to install RSQL for Mac OSX.

1. Install the driver manager with the following command:

```
brew install unixodbc --build-from-source
```

2. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC driver](odbc-driver-mac-how-to-install.md "odbc-driver-mac-how-to-install.md").
3. Copy the ini file to your home directory:

```
cp /opt/amazon/redshift/Setup/odbc.ini ~/.odbc.ini
```

4. Set the environment variables to point to the location of the
   file:

```
export ODBCINI=~/.odbc.ini
export ODBCSYSINI=/opt/amazon/redshift/Setup
export AMAZONREDSHIFTODBCINI=/opt/amazon/redshift/lib/amazon.redshiftodbc.ini
```

5. Set `DYLD_LIBRARY_PATH` to location of your
   libodbc.dylib if its not in `/usr/local/lib`.

```
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/usr/local/lib
```

6. Double-click the pkg file to run the installer.
7. Follow the steps in the installer to complete the installation.
   Agree to the terms of the license agreement.

## Install RSQL for

Windows

Follow the steps below to install RSQL for Windows.

1. Install the ODBC driver: [Downloading and installing the Amazon Redshift ODBC
   driver](odbc-driver-windows-how-to-install.md "odbc-driver-windows-how-to-install.md").
2. Double-click the RSQL download file to run the installer, then follow the
   prompts to complete the installation.

Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an ODBC driver manager to

configure the driver

On Linux operating systems, you use an ODBC driver manager to
configure the ODBC connection settings. ODBC driver managers use configuration
files to define and configure ODBC data sources and drivers. The ODBC driver
manager that you use depends on the operating system that you use. For Linux, it's unixODBC driver manager.

For more information about the supported ODBC driver managers to configure the
Amazon Redshift ODBC drivers, see [Using an Amazon Redshift ODBC driver on
Linux](install-odbc-driver-linux.md "install-odbc-driver-linux.md") for Linux operating systems.
Also, see "Specifying ODBC Driver Managers on Non- Windows Machines" in the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

Three files are required for configuring the Amazon Redshift ODBC driver:
`amazon.redshiftodbc.ini`, `odbc.ini`, and
`odbcinst.ini`.

If you installed to the default location, the
`amazon.redshiftodbc.ini` configuration file is located in one of
the following directories:

- `/opt/amazon/redshiftodbc/lib/64` (for the 64-bit driver on
  Linux operating systems)
- `/opt/amazon/redshiftodbc/lib/32` (for the 32-bit driver on
  Linux operating systems)
  Additionally, under `/opt/amazon/redshiftodbc/Setup` on Linux, there are sample `odbc.ini`
  and `odbcinst.ini` files. You can use these files as examples for
  configuring the Amazon Redshift ODBC driver and the data source name (DSN).

We don't recommend using the Amazon Redshift ODBC driver installation directory
for the configuration files. The sample files in the `Setup`
directory are for example purposes only. If you reinstall the Amazon Redshift ODBC
driver at a later time, or upgrade to a newer version, the installation
directory is overwritten. You then lose any changes that you might have made to
those files.

To avoid this, copy the `amazon.redshiftodbc.ini` file to a
directory other than the installation directory. If you copy this file to the
user's home directory, add a period (.) to the beginning of the file name
to make it a hidden file.

For the `odbc.ini` and `odbcinst.ini` files, either use
the configuration files in the user's home directory or create new
versions in another directory. By default, your Linux operating system
should have an `odbc.ini` file and an `odbcinst.ini`
file in the user's home directory (`/home/$USER` or
`~/`.). These default files are hidden files, which is
indicated by the dot (.) in front of each file name. These files display
only when you use the `-a` flag to list the directory
contents.

Whichever option you choose for the `odbc.ini` and
`odbcinst.ini` files, modify the files to add driver and DSN
configuration information. If you create new files, you also need to set
environment variables to specify where these configuration files are located.

By default, ODBC driver managers are configured to use hidden versions of the
`odbc.ini` and `odbcinst.ini` configuration files
(named .`odbc.ini` and .`odbcinst.ini`) located in the
home directory. They also are configured to use the
`amazon.redshiftodbc.ini` file in the `/lib` subfolder
of the driver installation directory. If you store these configuration files
elsewhere, set the environment variables described following so that the driver
manager can locate the files. For more information, see "Specifying the
Locations of the Driver Configuration Files" in the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

## Creating a data source name on

Linux operating systems

When connecting to your data store using a data source name (DSN),
configure the `odbc.ini` file to define DSNs. Set the properties
in the `odbc.ini` file to create a DSN that specifies the
connection information for your data store.

For information about how to configure the `odbc.ini` file, see
"Creating a Data Source Name on a Non-Windows Machine" in the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf")

Use the following format on Linux operating systems.

```
[ODBC Data Sources]
`driver_name`=`dsn_name`

[`dsn_name`]
Driver=`path`/`driver_file`

Host=`cluster_endpoint`
Port=`port_number`
Database=`database_name`
locale=`locale`

```

The following example shows the configuration for odbc.ini with the 64-bit
ODBC driver on Linux operating systems.

```
[ODBC Data Sources]
Amazon_Redshift_x64=Amazon Redshift (x64)

[Amazon Redshift (x64)]
Driver=/opt/amazon/redshiftodbc/lib/64/libamazonredshiftodbc64.so
Host=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com
Port=5932
Database=dev
locale=en-US

```

The following example shows the configuration for odbc.ini with the 32-bit
ODBC driver on Linux operating systems.

```
[ODBC Data Sources]
Amazon_Redshift_x32=Amazon Redshift (x86)

[Amazon Redshift (x86)]
Driver=/opt/amazon/redshiftodbc/lib/32/libamazonredshiftodbc32.so
Host=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com
Port=5932
Database=dev
locale=en-US
```

## Configuring a connection

without a DSN on Linux operating systems

To connect to your data store through a connection that doesn't have
a DSN, define the driver in the `odbcinst.ini` file. Then provide
a DSN-less connection string in your application.

For information about how to configure the `odbcinst.ini` file
in this case, see "Configuring a DSN-less Connection on a Non-Windows
Machine" in the [Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

Use the following format on Linux operating systems.

```
[ODBC Drivers]
`driver_name`=Installed
...

[`driver_name`]
Description=`driver_description`
Driver=`path`/`driver_file`

...
```

The following example shows the `odbcinst.ini` configuration
for the 64-bit driver installed in the default directories on Linux
operating systems.

```
[ODBC Drivers]
Amazon Redshift (x64)=Installed

[Amazon Redshift (x64)]
Description=Amazon Redshift ODBC Driver (64-bit)
Driver=/opt/amazon/redshiftodbc/lib/64/libamazonredshiftodbc64.so
```

The following example shows the `odbcinst.ini` configuration
for the 32-bit driver installed in the default directories on Linux
operating systems.

```
[ODBC Drivers]
Amazon Redshift (x86)=Installed

[Amazon Redshift (x86)]
Description=Amazon Redshift ODBC Driver (32-bit)
Driver=/opt/amazon/redshiftodbc/lib/32/libamazonredshiftodbc32.so
```

## Configuring

environment variables

Use the correct ODBC driver manager to load the correct driver. To do
this, set the library path environment variable. For more information, see
"Specifying ODBC Driver Managers on Non-Windows Machines" in the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

By default, ODBC driver managers are configured to use hidden versions of
the `odbc.ini` and `odbcinst.ini` configuration files
(named .`odbc.ini` and .`odbcinst.ini`) located in the
home directory. They also are configured to use the
`amazon.redshiftodbc.ini` file in the `/lib`
subfolder of the driver installation directory. If you store these
configuration files elsewhere, the environment variables so that the driver
manager can locate the files. For more information, see "Specifying the
Locations of the Driver Configuration Files" in _Amazon Redshift ODBC
Connector Installation and Configuration Guide_.

## Configuring connection

features

You can configure the following connection features for your ODBC
setting:

- Configure the ODBC driver to provide credentials and authenticate
  the connection to the Amazon Redshift database.
- Configure the ODBC driver to connect to a socket enabled with
  Secure Sockets Layer (SSL), if you are connecting to an Amazon Redshift
  server that has SSL enabled.
- Configure the ODBC driver to connect to Amazon Redshift through a proxy
  server.
- Configure the ODBC driver to use a query processing mode to
  prevent queries from consuming too much memory.
- Configure the ODBC driver to pass IAM authentication processes
  through a proxy server.
- Configure the ODBC driver to use TCP keepalives to prevent
  connections from timing out.

For information about these connection features, see the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

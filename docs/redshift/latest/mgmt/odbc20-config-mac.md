Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an ODBC driver manager to configure the ODBC driver

On Mac, you use an ODBC driver manager to configure the ODBC connection
settings. ODBC driver managers use configuration files to define and configure ODBC
data sources and drivers. The ODBC driver manager that you use depends on the
operating system that you use.

## Configuring the ODBC driver using

iODBC or unixODBC driver manager

The following files are required to configure the Amazon Redshift ODBC driver:

- `amazon.redshiftodbc.ini`
- `odbc.ini`
- `odbcinst.ini`

If you installed to the default location, the
`amazon.redshiftodbc.ini` configuration file is located in
`/opt/amazon/redshiftodbcx64`.

Additionally, under `/opt/amazon/redshiftodbcx64`, you can find
sample `odbc.ini` and `odbcinst.ini` files. You can use
these files as examples for configuring the Amazon Redshift ODBC driver and the data
source name (DSN). The sample files in the installed directory are for
example purposes only.

We don't recommend using the Amazon Redshift ODBC driver installation directory for
the configuration files. If you reinstall the Amazon Redshift ODBC driver at a later
time, or upgrade to a newer version, the installation directory is overwritten.
You will lose any changes that you might have made to files in the installation
directory.

To avoid this, copy the `odbc.ini`, `odbcinst.ini`
and `amazon.redshiftodbc.ini` files to a directory other than the
installation directory. If you copy these files to the user's home directory,
add a period (.) to the beginning of these file names to make it a hidden file.

Modify the files to add DSN configuration information.
When you create new files, you also need to set environment variables
to specify where these configuration files are located.

The following is an example of setting the environment variables:

```
export ODBCINI=/Library/ODBC/odbc.ini
export ODBCSYSINI=/Library/ODBC
export ODBCINSTINI=${ODBCSYSINI}/odbcinst.ini
```

For command-line applications: Add the export commands to your
shell startup file (e.g., `~/.bash_profile` or `~/.zshrc`).

For supported version of driver manager,
see [here](odbc20-install-config-mac.md "odbc20-install-config-mac.md")

### Configuring a connection using a data source

name (DSN) on Apple MacOS

When connecting to your data store using a data source name (DSN), configure
the `odbc.ini` file to define data source names (DSNs). Set the
properties in the `odbc.ini` file to create a DSN that specifies the
connection information for your Redshift data warehouse.

On Apple MacOS, use the following format:

```
[ODBC Data Sources]
driver_name=dsn_name

[dsn_name]
Driver=path/driver_file
Host=cluster_endpoint
Port=port_number
Database=database_name
locale=locale
```

The following example shows the configuration for `odbc.ini` with
the 64-bit ODBC driver on Apple MacOS.

```
[ODBC Data Sources]
Amazon_Redshift_x64=Amazon Redshift ODBC Driver (x64)

[Amazon_Redshift_x64]
Driver=/opt/amazon/redshiftodbcx64/librsodbc64.dylib
Host=examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com
Port=5932
Database=dev
locale=en-US
```

### Configuring a connection without a DSN on

Apple MacOS

To connect to your Redshift data warehouse through a connection that doesn't have a DSN,
define the driver in the `odbcinst.ini` file. Then provide a DSN-less
connection string in your application.

On Apple MacOS, use the following format:

```
[ODBC Drivers]
driver_name=Installed
...

[driver_name]
Description=driver_description
Driver=path/driver_file

...
```

The following example shows the configuration for `odbcinst.ini`
with the 64-bit ODBC driver on Apple MacOS.

```
[ODBC Drivers]
Amazon Redshift ODBC Driver (x64)=Installed

[Amazon Redshift ODBC Driver (x64)]
Description=Amazon Redshift ODBC Driver (64-bit)
Driver=/opt/amazon/redshiftodbcx64/librsodbc64.dylib
```

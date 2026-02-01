Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ODBC driver options

You can use configuration options to control the behavior of the Amazon Redshift ODBC
driver.

In Microsoft Windows, you typically set driver options when you configure a
data source name (DSN). You can also set driver options in the connection string
when you connect programmatically, or by adding or changing registry keys in
`HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBC.INI\`your_DSN``.
For more information about configuring a DSN, see [Using an Amazon Redshift ODBC driver on Microsoft Windows](install-odbc-driver-windows.md "install-odbc-driver-windows.md").

In macOS X, you set driver configuration options in your
`odbc.ini` and `amazon.redshiftodbc.ini` files, as
described in [Use an ODBC driver manager to
configure the driver](odbc-driver-configure-mac.md "odbc-driver-configure-mac.md"). Configuration options set
in an `amazon.redshiftodbc.ini` file apply to all connections. In
contrast, configuration options set in an `odbc.ini` file are
specific to a connection. Configuration options set in `odbc.ini`
take precedence over configuration options set in
`amazon.redshiftodbc.ini`.

For information about how to set up ODBC driver configuration options, see the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

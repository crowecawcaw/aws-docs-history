Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring a connection for ODBC driver version 2.x for

Amazon Redshift

###### Note

The ODBC driver version 2.x doesn’t have full parity with the ODBC driver 1.x.
We recommend that you confirm that the ODBC driver 2.x has all of the features
that you need when considering moving from version 1.x to 2.x.

You can use an ODBC connection to connect to your Amazon Redshift cluster from many third-party
SQL client tools and applications. If your client tool supports JDBC, you can choose to use
that type of connection rather than ODBC due to the ease of configuration that JDBC
provides. However, if your client tool doesn't support JDBC, you can follow the steps in
this section to set up an ODBC connection on your client computer or Amazon EC2 instance.

Amazon Redshift provides 64-bit ODBC drivers for Linux, Windows and Mac operating systems; the 32-bit
ODBC drivers are discontinued. Further updates to the
32-bit ODBC drivers will not be released, except for urgent security patches.

For the latest information about ODBC driver changes, see the [change
log](https://github.com/aws/amazon-redshift-odbc-driver/blob/master/CHANGELOG.md "https://github.com/aws/amazon-redshift-odbc-driver/blob/master/CHANGELOG.md").

###### Topics

- [Getting the ODBC URL](odbc20-getting-url.md "odbc20-getting-url.md")
- [Using an Amazon Redshift ODBC driver on Microsoft
  Windows](odbc20-install-config-win.md "odbc20-install-config-win.md")
- [Using an Amazon Redshift ODBC driver on
  Linux](odbc20-install-config-linux.md "odbc20-install-config-linux.md")
- [Using an Amazon Redshift ODBC driver on Apple macOS](odbc20-install-config-mac.md "odbc20-install-config-mac.md")
- [Authentication methods](odbc20-authentication-ssl.md "odbc20-authentication-ssl.md")
- [Data types conversions](odbc20-converting-data-types.md "odbc20-converting-data-types.md")
- [ODBC driver options](odbc20-configuration-options.md "odbc20-configuration-options.md")
- [Previous ODBC driver versions](odbc20-previous-versions.md "odbc20-previous-versions.md")

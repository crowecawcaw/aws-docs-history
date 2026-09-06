

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configuring an ODBC driver version 1.x connection
<a name="configure-odbc-connection"></a>

You can use an ODBC connection to connect to your Amazon Redshift cluster from many third-party SQL client tools and applications. To do this, set up the connection on your client computer or Amazon EC2 instance. If your client tool supports JDBC, you might choose to use that type of connection rather than ODBC due to the ease of configuration that JDBC provides. However, if your client tool doesn't support JDBC, follow the steps in this section to configure an ODBC connection. 

Amazon Redshift provides 64-bit ODBC drivers for Linux, Windows, and macOS operating systems. The 32-bit ODBC drivers are discontinued. Further updates will not be released, except for urgent security patches. 

For the latest information about ODBC driver functionality and prerequisites, see [Amazon Redshift ODBC driver release notes](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.3.1008/Release+Notes.pdf). 

For installation and configuration information for Amazon Redshift ODBC drivers, see the [Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.3.1008/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf). 

**Topics**
+ [Getting the ODBC URL](obtain-odbc-url.md)
+ [Using an Amazon Redshift ODBC driver on Microsoft Windows](install-odbc-driver-windows.md)
+ [Using an Amazon Redshift ODBC driver on Linux](install-odbc-driver-linux.md)
+ [Using an Amazon Redshift ODBC driver on macOS](install-odbc-driver-mac.md)
+ [ODBC driver options](configure-odbc-options.md)
+ [Previous ODBC driver versions](odbc-previous-versions.md)
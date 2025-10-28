Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring a connection for JDBC driver version 2.x for

Amazon Redshift

You can use a JDBC driver version 2.x connection to connect to your Amazon Redshift cluster from
many third-party SQL client tools. The Amazon Redshift JDBC connector provides an open source
solution. You can browse the source code, request enhancements, report issues, and provide
contributions.

For the latest information about JDBC driver changes, see the [change
log](https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/CHANGELOG.md "https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/CHANGELOG.md").

By default, the Amazon Redshift JDBC driver is configured to use TCP keepalives to prevent
connections from timing out. You can specify when the driver starts sending keepalive
packets or turn off the feature by setting the relevant properties in the connection URL.
For more information about the syntax of the connection URL, see [Building the connection URL](jdbc20-build-connection-url.md "jdbc20-build-connection-url.md").

| Property       | Description                                               |
| -------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TCPKeepAlive` | To turn off TCP keepalives, set this property to `FALSE`. | ###### Topics <br>• [Download the Amazon Redshift JDBC driver, version 2.1](jdbc20-download-driver.md "jdbc20-download-driver.md") <br>• [Installing the Amazon Redshift JDBC driver, version 2.2](jdbc20-install-driver.md "jdbc20-install-driver.md") <br>• [Getting the JDBC URL](jdbc20-obtain-url.md "jdbc20-obtain-url.md") <br>• [Building the connection URL](jdbc20-build-connection-url.md "jdbc20-build-connection-url.md") <br>• [Configuring a JDBC connection with Apache Maven](configure-jdbc20-connection-with-maven.md "configure-jdbc20-connection-with-maven.md") <br>• [Configuring authentication and SSL](jdbc20-configure-authentication-ssl.md "jdbc20-configure-authentication-ssl.md") <br>• [Configuring logging](jdbc20-configuring-logging.md "jdbc20-configuring-logging.md") <br>• [Data type conversions](jdbc20-data-type-mapping.md "jdbc20-data-type-mapping.md") <br>• [Using prepared statement support](jdbc20-prepared-statement-support.md "jdbc20-prepared-statement-support.md") <br>• [Differences between the 2.2 and 1.x versions of the JDBC driver](jdbc20-jdbc10-driver-differences.md "jdbc20-jdbc10-driver-differences.md") <br>• [Creating initialization (.ini) files for JDBC driver version 2.x](jdbc20-ini-file.md "jdbc20-ini-file.md") <br>• [Options for JDBC driver version 2.x configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md") <br>• [Previous versions of JDBC driver version 2.x](jdbc20-previous-driver-version-20.md "jdbc20-previous-driver-version-20.md") |



 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configuring a connection for JDBC driver version 2.x for Amazon Redshift
<a name="jdbc20-install"></a>

You can use a JDBC driver version 2.x connection to connect to your Amazon Redshift cluster from many third-party SQL client tools. The Amazon Redshift JDBC connector provides an open source solution. You can browse the source code, request enhancements, report issues, and provide contributions. 

For the latest information about JDBC driver changes, see the [change log](https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/CHANGELOG.md).

By default, the Amazon Redshift JDBC driver is configured to use TCP keepalives to prevent connections from timing out. You can specify when the driver starts sending keepalive packets or turn off the feature by setting the relevant properties in the connection URL. For more information about the syntax of the connection URL, see [Building the connection URL](jdbc20-build-connection-url.md).


| Property | Description | 
| --- | --- | 
| `TCPKeepAlive` | To turn off TCP keepalives, set this property to `FALSE`. | 

**Topics**
+ [Download the Amazon Redshift JDBC driver, version 2.x](jdbc20-download-driver.md)
+ [Installing the Amazon Redshift JDBC driver, version 2.x](jdbc20-install-driver.md)
+ [Getting the JDBC URL](jdbc20-obtain-url.md)
+ [Building the connection URL](jdbc20-build-connection-url.md)
+ [Configuring a JDBC connection with Apache Maven](configure-jdbc20-connection-with-maven.md)
+ [Configuring authentication and SSL](jdbc20-configure-authentication-ssl.md)
+ [Configuring logging](jdbc20-configuring-logging.md)
+ [Data type conversions](jdbc20-data-type-mapping.md)
+ [Using prepared statement support](jdbc20-prepared-statement-support.md)
+ [Differences between the 2.x and 1.x versions of the JDBC driver](jdbc20-jdbc10-driver-differences.md)
+ [Creating initialization (.ini) files for JDBC driver version 2.x](jdbc20-ini-file.md)
+ [Options for JDBC driver version 2.x configuration](jdbc20-configuration-options.md)
+ [Previous versions of JDBC driver version 2.x](jdbc20-previous-driver-version-20.md)
Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Download the Amazon Redshift JDBC driver, version

2.1

###### Note

The Amazon Redshift JDBC 2.x driver isn't designed to be thread-safe.
Two or more threads concurrently attempting to use the same connection can lead to
deadlocks, errors, incorrect results, or other unexpected behaviors.

If you do have a multi-threaded application, we recommend that you synchronize
access to the driver to avoid concurrent access.

Amazon Redshift offers drivers for tools that are compatible with the JDBC 4.2 API. The class
name for this driver is `com.amazon.redshift.Driver`.

For detailed information about how to install the JDBC driver, reference the JDBC
driver libraries, and register the driver class, see the following topics.

For each computer where you use the Amazon Redshift JDBC driver version 2.x, make sure that the
Java Runtime Environment (JRE) 8.0 is installed.

If you use the Amazon Redshift JDBC driver for database authentication, make sure that you have
AWS SDK for Java 1.11.118 or later in your Java class path. If you don't have AWS SDK for Java
installed, download the ZIP file with JDBC 4.2–compatible driver and driver dependent
libraries for the AWS SDK:

- [JDBC 4.2–compatible driver version 2.x and AWS SDK driver–dependent libraries](https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/2.2.4/redshift-jdbc42-2.2.4.zip "https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/2.2.4/redshift-jdbc42-2.2.4.zip")

This ZIP file contains the JDBC 4.2–compatible driver version 2.x and
AWS SDK for Java 1.x driver–dependent library files. Unzip the
dependent jar files to the same location as the JDBC driver. Only the JDBC
driver needs to be in CLASSPATH.

This ZIP file doesn't include the complete AWS SDK for Java 1.x.
However, it includes the AWS SDK for Java 1.x driver–dependent
libraries that are required for AWS Identity and Access Management (IAM) database
authentication.

Use this Amazon Redshift JDBC driver with the AWS SDK that is required for IAM
database authentication.

To install the complete AWS SDK for Java 1.x, see [AWS SDK for Java 1.x](../../../sdk-for-java/v1/developer-guide/welcome.md "../../../sdk-for-java/v1/developer-guide/welcome.md") in the _AWS SDK for Java Developer
Guide_.

- [JDBC 4.2–compatible driver version 2.x (without the AWS SDK)](https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/2.2.4/redshift-jdbc42-2.2.4.jar "https://s3.amazonaws.com/redshift-downloads/drivers/jdbc/2.2.4/redshift-jdbc42-2.2.4.jar")
  Review the JDBC driver version 2.x software license and change log file:

- [JDBC driver version 2.x license](https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/LICENSE "https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/LICENSE")
- [JDBC driver version 2.x change log](https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/CHANGELOG.md "https://github.com/aws/amazon-redshift-jdbc-driver/blob/master/CHANGELOG.md")
  JDBC drivers version 1.2.27.1051 and later support Amazon Redshift stored procedures. For more
  information, see [Creating stored procedures
  in Amazon Redshift](../dg/stored-procedure-overview.md "../dg/stored-procedure-overview.md") in the _Amazon Redshift Database Developer Guide_.

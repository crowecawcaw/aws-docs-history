# Athena JDBC 3.x driver

You can use the Athena JDBC driver to connect to Amazon Athena from many third-party SQL client
tools and from custom applications.

## System Requirements

- Java 8 (or higher) runtime environment
- At least 20 MB of available disk space

## Considerations and limitations

Following are some considerations and limitations for the Athena JDBC 3.x
driver.

- Logging – The 3.x driver uses [SLF4J](https://www.slf4j.org/manual.html "https://www.slf4j.org/manual.html"), which is an
  abstraction layer that enables the use of any one of several logging systems at
  runtime.
- Encryption – When using the Amazon S3 fetcher
  with the `CSE_KMS` encryption option, the Amazon S3 client can't decrypt
  results stored in an Amazon S3 bucket. If you require `CSE_KMS`
  encryption, you can continue to use the streaming fetcher. Support for
  `CSE_KMS` encryption with the Amazon S3 fetcher is planned.

## JDBC 3.x driver download

This section contains download and license information for the JDBC 3.x driver.

###### Important

When you use the JDBC 3.x driver, be sure to note the following
requirements:

- Open port 444 – Keep port 444, which
  Athena uses to stream query results, open to outbound traffic. When you use a
  PrivateLink endpoint to connect to Athena, ensure that the security group
  attached to the PrivateLink endpoint is open to inbound traffic on port 444.
- athena:GetQueryResultsStream policy
  – Add the `athena:GetQueryResultsStream` policy action to
  the IAM principals that use the JDBC driver. This policy action is not
  exposed directly with the API. It is used only with the ODBC and JDBC
  drivers as part of streaming results support. For an example policy, see
  [AWS managed policy: AWSQuicksightAthenaAccess](managed-policies.md#awsquicksightathenaaccess-managed-policy "managed-policies.md#awsquicksightathenaaccess-managed-policy").

To download the Amazon Athena 3.x JDBC driver, visit the following links.

### JDBC driver uber jar

The following download packages the driver and all its dependencies in the same
`.jar` file. This download is commonly used for third-party
SQL clients.

[3.7.0 uber jar](https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/athena-jdbc-3.7.0-with-dependencies.jar "https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/athena-jdbc-3.7.0-with-dependencies.jar")

### JDBC driver lean jar

The following download is a `.zip` file that contains the lean
`.jar` for the driver and separate `.jar`
files for the driver's dependencies. This download is commonly used for custom
applications that might have dependencies that conflict with the dependencies that
the driver uses. This download is useful if you want to choose which of the driver
dependencies to include with the lean jar, and which to exclude if your custom
application already contains one or more of them.

[3.7.0 lean jar](https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/athena-jdbc-3.7.0-lean-jar-and-separate-dependencies-jars.zip "https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/athena-jdbc-3.7.0-lean-jar-and-separate-dependencies-jars.zip")

### License

The following link contains the license agreement for the JDBC 3.x driver.

[License](https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/LICENSE.txt "https://downloads.athena.us-east-1.amazonaws.com/drivers/JDBC/3.7.0/LICENSE.txt")

## Trusted identity propagation with JDBC

You can now connect to Amazon Athena using JDBC drivers with single sign-on capabilities through AWS Identity and Access Management Identity Center.
When you access Athena from tools like PowerBI, Tableau, or DBeaver, your identity and
permissions automatically propagate to Athena through IAM Identity Center. For more
information, see [Use Trusted identity propagation with Amazon Athena drivers](using-trusted-identity-propagation.md "using-trusted-identity-propagation.md").

###### Topics

- [Get started with the JDBC 3.x driver](jdbc-v3-driver-getting-started.md "jdbc-v3-driver-getting-started.md")
- [Amazon Athena JDBC 3.x connection parameters](jdbc-v3-driver-connection-parameters.md "jdbc-v3-driver-connection-parameters.md")
- [Other JDBC 3.x configuration](jdbc-v3-driver-other-configuration.md "jdbc-v3-driver-other-configuration.md")
- [Amazon Athena JDBC 3.x release notes](jdbc-v3-driver-release-notes.md "jdbc-v3-driver-release-notes.md")
- [Previous versions of the Athena JDBC 3.x driver](jdbc-v3-driver-previous-versions.md "jdbc-v3-driver-previous-versions.md")

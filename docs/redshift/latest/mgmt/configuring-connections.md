Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring connections in Amazon Redshift

In the following section, learn how to configure JDBC, Python, and ODBC connections to
connect to your cluster from SQL client tools. This section describes how to set up
JDBC, Python, and ODBC connections. It also describes how to use Secure Sockets Layer
(SSL) and server certificates to encrypt communication between the client and server.

## JDBC, Python, and ODBC drivers for

Amazon Redshift

To work with data in your cluster, you must have JDBC, Python, or ODBC drivers for
connectivity from your client computer or instance. Code your applications to use
JDBC, Python, or ODBC data access API operations, and use SQL client tools that
support either JDBC, Python, or ODBC.

Amazon Redshift offers JDBC, Python, and ODBC drivers for download. These drivers are
supported by Support.

PostgreSQL drivers are not tested and not supported by the Amazon Redshift team. Use the
Amazon Redshift–specific drivers when connecting to an Amazon Redshift cluster. The Amazon Redshift drivers
have the following advantages:

- Support for IAM, SSO, and federated authentication.
- Support for new Amazon Redshift data types.
- Support for authentication profiles.
- Improved performance in conjunction with Amazon Redshift enhancements.

For more information about how to download the JDBC and ODBC drivers and
configure connections to your cluster, see [Configuring a connection for JDBC driver version 2.x for
Amazon Redshift](jdbc20-install.md "jdbc20-install.md"), [Amazon Redshift Python connector](python-redshift-driver.md "python-redshift-driver.md"), and [Configuring a connection for ODBC driver version 2.x for
Amazon Redshift](odbc20-install.md "odbc20-install.md").

For more information about managing IAM identities, including best practices for
IAM roles, see [Identity and access management in
Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

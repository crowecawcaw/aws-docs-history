Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Users

You can create and manage database users using the Amazon Redshift SQL commands CREATE USER and
ALTER USER. Or you can configure your SQL client with custom Amazon Redshift JDBC or ODBC drivers.
These manage the process of creating database users and temporary passwords as part of the
database logon process.

The drivers authenticate database users based on AWS Identity and Access Management (IAM) authentication. If you
already manage user identities outside of AWS, you can use a SAML 2.0-compliant identity
provider (IdP) to manage access to Amazon Redshift resources. You use an IAM role to configure your
IdP and AWS to permit your federated users to generate temporary database credentials and
log on to Amazon Redshift databases. For more information, see [Using IAM authentication to generate
database user credentials](../mgmt/generating-user-credentials.md "../mgmt/generating-user-credentials.md").

Amazon Redshift users can only be created and dropped by a database superuser. Users
are authenticated when they log on to Amazon Redshift. They can own databases and database objects
(for example, tables). They can also grant permissions on those objects to users, groups,
and schemas to control who has access to which object. Users with CREATE DATABASE rights
can create databases and grant permissions to those databases. Superusers have database
ownership permissions for all databases.

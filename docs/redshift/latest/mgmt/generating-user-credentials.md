Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using IAM authentication to

generate database user credentials

You can generate temporary database credentials based on permissions granted through an
AWS Identity and Access Management (IAM) permissions policy to manage the access that your users have to your Amazon Redshift
database.

Commonly, Amazon Redshift database users log in to the database by providing a database user name and
password. However, you don't have to maintain user names and passwords in your Amazon Redshift
database. As an alternative, you can configure your system to permit users to create user
credentials and log in to the database based on their IAM credentials.

Amazon Redshift provides the [GetClusterCredentials](../APIReference/API_GetClusterCredentials.md "../APIReference/API_GetClusterCredentials.md") API operation to generate temporary database user
credentials. You can configure your SQL client with Amazon Redshift JDBC or ODBC drivers that manage
the process of calling the `GetClusterCredentials` operation. They do so by
retrieving the database user credentials, and establishing a connection between your SQL
client and your Amazon Redshift database. You can also use your database application to
programmatically call the `GetClusterCredentials` operation, retrieve database
user credentials, and connect to the database.

If you already manage user identities outside AWS, you can use an identity provider
(IdP) compliant with Security Assertion Markup Language (SAML) 2.0 to manage access to Amazon Redshift
resources. You configure your IdP to permit your federated users access to an IAM role. With
that IAM role, you can generate temporary database credentials and log in to Amazon Redshift databases.

Your SQL client needs permission to call the `GetClusterCredentials` operation
for you. You manage those permissions by creating an IAM role and attaching an IAM
permissions policy that grants or restricts access to the `GetClusterCredentials`
operation and related actions. As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

The policy also grants or restricts access to specific resources, such as Amazon Redshift
clusters, databases, database user names, and user group names.

###### Note

We recommend using the Amazon Redshift JDBC or ODBC drivers to manage the process of calling the
`GetClusterCredentials` operation and logging on to the database. For
simplicity, we assume that you are using a SQL client with the JDBC or ODBC drivers
throughout this topic.

For specific details and examples of using the `GetClusterCredentials`
operation or the parallel `get-cluster-credentials` CLI command, see [GetClusterCredentials](../APIReference/API_GetClusterCredentials.md "../APIReference/API_GetClusterCredentials.md") and
[get-cluster-credentials](../../../cli/latest/reference/redshift/get-cluster-credentials.md "../../../cli/latest/reference/redshift/get-cluster-credentials.md").

To manage authentication and authorization centrally, Amazon Redshift supports database
authentication with IAM, enabling user authentication through enterprise federation. Instead
of creating a user, you can use existing identities from AWS Directory Service, your enterprise user
directory, or a web identity provider. These are known as federated users. AWS assigns a
role to a federated user when access is requested through an IdP.

To provide federated access to a user or client application in your organization to call
Amazon Redshift API operations, you can also use the JDBC or ODBC driver with SAML 2.0 support to
request authentication from your organization IdP. In this case, your organization's users
don't have direct access to Amazon Redshift.

For more information, see [Identity
Providers and Federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md") in the _IAM User Guide_.

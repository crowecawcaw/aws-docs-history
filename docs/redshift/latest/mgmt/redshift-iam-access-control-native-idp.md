Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Native identity provider (IdP)

federation for Amazon Redshift

Managing identities and permissions for Amazon Redshift is made easier with native identity provider
federation because it leverages your existing identity provider to simplify authentication and
managing permissions. It does this by making it possible to share identity metadata to
Redshift from your identity provider. For the first iteration of this feature, the supported
identity provider is [Microsoft Azure Active Directory (Azure AD)](https://azure.microsoft.com/en-us/services/active-directory/ "https://azure.microsoft.com/en-us/services/active-directory/").

To configure Amazon Redshift so it can authenticate identities from the third-party identity
provider, you register the identity provider with Amazon Redshift. Doing this enables Redshift to
authenticate users and roles defined by the identity provider. Thus you can avoid having to
perform granular identity management in both your third-party identity provider and in Amazon Redshift,
because identity information is shared.

For information about using session roles that are transferred from identity provider
(IdP) groups, see [PG_GET_SESSION_ROLES](../dg/PG_GET_SESSION_ROLES.md "../dg/PG_GET_SESSION_ROLES.md") in the
_Amazon Redshift Database Developer Guide_.

## Native identity provider

(IdP) federation

To complete the preliminary setup between the identity provider and Amazon Redshift, you perform a
couple of steps: First, you register Amazon Redshift as a third-party application with your identity
provider, requesting the necessary API permissions. Then you create users and groups in the
identity provider. Last, you register the identity provider with Amazon Redshift, using SQL statements,
which set authentication parameters that are unique to the identity provider. As part of
registering the identity provider with Redshift, you assign a namespace to make sure users
and roles are grouped correctly.

With the identity provider registered with Amazon Redshift, communication is set up between
Redshift and the identity provider. A client can then pass tokens and authenticate to
Redshift as an identity provider entity. Amazon Redshift uses the IdP group membership information to
map to Redshift roles. If the user doesn't previously exist in Redshift, the user is
created. Roles are created that map to identity provider groups, if they don't exist. The
Amazon Redshift administrator grants permission on the roles, and users can run queries and perform
other database tasks.

The following steps outline how native identity provider federation works, when a user
logs in:

1. When a user logs in using the native IdP option, from the client, the identity
   provider token is sent from the client to the driver.
2. The user is authenticated. If the user doesn't already exist in Amazon Redshift, a new user is
   created. Redshift maps the user's identity provider groups to Redshift roles.
3. Permissions are assigned, based on the user's Redshift roles. These are granted to
   users and roles by an administrator.
4. The user can query Redshift.

## Desktop client tools

For instructions on how to use native identity provider federation to connect to Amazon Redshift
with Power BI, see the blog post [Integrate Amazon Redshift native IdP federation with Microsoft Azure Active Directory (AD) and Power
BI](https://aws.amazon.com/blogs/big-data/integrate-amazon-redshift-native-idp-federation-with-microsoft-azure-ad-and-power-bi/ "https://aws.amazon.com/blogs/big-data/integrate-amazon-redshift-native-idp-federation-with-microsoft-azure-ad-and-power-bi/"). It describes a step-by-step implementation of the Amazon Redshift native IdP setup with
Azure AD. It details the steps to set up the client connection for either Power BI Desktop
or the Power BI service. The steps include application registration, configuring
permissions, and configuring credentials.

To learn how to integrate Amazon Redshift native IdP federation with Azure AD, using Power BI
Desktop and JDBC Client-SQL Workbench/J, watch the following video:

For instructions on how to use native identity provider federation to connect to Amazon Redshift
with a SQL client, specifically DBeaver or SQL Workbench/J, see the blog post [Integrate Amazon Redshift native IdP federation with Microsoft Azure AD using a SQL
client](https://aws.amazon.com/blogs/big-data/integrate-amazon-redshift-native-idp-federation-with-microsoft-azure-ad-using-a-sql-client/ "https://aws.amazon.com/blogs/big-data/integrate-amazon-redshift-native-idp-federation-with-microsoft-azure-ad-using-a-sql-client/").

## Limitations

These limitations apply:

- Amazon Redshift drivers support `BrowserIdcAuthPlugin` starting from the
  following versions:
  - Amazon Redshift JDBC driver v2.1.0.30
  - Amazon Redshift ODBC driver v2.1.3
  - Amazon Redshift Python driver v2.1.3

- Amazon Redshift drivers support `IdpTokenAuthPlugin` starting from the
  following versions:
  - Amazon Redshift JDBC driver v2.1.0.19
  - Amazon Redshift ODBC driver v2.0.0.9
  - Amazon Redshift Python driver v2.0.914

- **No support for enhanced VPC** – Enhanced VPC
  isn't supported when you configure Redshift trusted identity propagation with AWS
  IAM Identity Center. For more information about enhanced VPC, see [Enhanced VPC routing in
  Amazon Redshift](enhanced-vpc-routing.md "enhanced-vpc-routing.md").
- **AWS IAM Identity Center caching** – AWS IAM Identity Center caches session
  information. This might cause unpredictable access issues when you attempt to connect to
  your Redshift database via Redshift query editor v2. This is because the associated AWS IAM Identity Center
  session in query editor v2 remains valid, even in a case where the database user is signed out of
  the AWS console. The cache expires after one hour, which typically remediates any
  issues.

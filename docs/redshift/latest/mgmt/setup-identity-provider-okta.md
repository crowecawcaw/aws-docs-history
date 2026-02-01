Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Okta

You can use Okta as an identity provider (IdP) to access your Amazon Redshift cluster.
This tutorial shows you how you can use Okta as an identity provider (IdP) to
access your Amazon Redshift cluster.

## Step 1: Set up Okta and

your AWS account to trust each other

The following procedure describes how to set up a trust
relationship.

###### To set up Okta and your AWS account to trust each other

1. Create or use an existing Amazon Redshift cluster for your Okta users to
   connect to. To configure the connection, certain properties of this
   cluster are needed, such as the cluster identifier. For more
   information, see [Creating a Cluster](create-cluster.md "create-cluster.md").
2. Add Amazon Redshift as a new application on the Okta portal. For detailed
   steps, see the [Okta
   documentation](https://developer.okta.com/docs/ "https://developer.okta.com/docs/").
   - Choose **Add Application**.
   - Under **Add Application**, choose
     **Create New App**.
   - On the **Create a New Add Application
     Integration** page, for
     **Platform**, choose
     **Web**.
   - For **Sign on method**, choose
     **SAML v2.0**.
   - On the **General Settings** page, for
     **App name**, enter
     `your-redshift-saml-sso-name`.
     This is the name of your application.
   - On the **SAML Settings** page, for
     **Single sign on URL**, enter
     `your-redshift-local-host-url`.
     This is the local host and port that the SAML assertion
     redirects to, for example
     `http://localhost:7890/redshift/`.

3. Use the **Single sign on URL** value as the
   **Recipient URL** and **Destination
   URL**.
4. For **Signing**, choose **Sign
   Assertion**.
5. For **Audience URI (SP Entity ID)**, enter
   `urn:amazon:webservices` for the claims, as
   shown in the following table.
6. In the **Advanced Settings** section, for
   **SAML Issuer ID**, enter
   `your-Identity-Provider-Issuer-ID`,
   which you can find in the **View Setup
   Instructions** section.
7. In the **Attribute Statements** section, create
   the claims as shown in the following table.

| Claim name                                                 | Value                                                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **https://aws.amazon.com/SAML/Attributes/Role**            | arn:aws:iam::`123456789012`:role/`Okta`,arn:aws:iam::`123456789012`:saml-provider/`Okta` |
| **https://aws.amazon.com/SAML/Attributes/RoleSessionName** | user.email                                                                               |
| **https://redshift.amazon.com/SAML/Attributes/AutoCreate** | "true"                                                                                   |
| **https://redshift.amazon.com/SAML/Attributes/DbUser**     | user.email                                                                               |

8. In the **App Embed Link** section, find the URL
   that you can use as the login URL for the Browser SAML
   plugin.
9. Create an IAM SAML identity provider on the IAM console. The
   metadata document that you provide is the federation metadata XML
   file that you saved when you set up Okta. For detailed steps, see
   [Creating and Managing an IAM Identity Provider
   (Console)](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console") in the _IAM User Guide_.
10. Create an IAM role for SAML 2.0 federation on the IAM console. For
    detailed steps, see [Creating a Role for SAML](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create") in the
    _IAM User Guide_.
11. Create an IAM policy that you can attach to the IAM role that you
    created for SAML 2.0 federation on the IAM console. For detailed
    steps, see [Creating IAM Policies (Console)](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
    _IAM User Guide_. For an Azure AD example,
    see [Setting up JDBC or ODBC single
    sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

## Step 2: Set up JDBC or

ODBC for authentication to Okta

JDBC

###### To set up JDBC for authentication to Okta

- Configure your database client to connect to your
  cluster through JDBC using Okta single sign-on.

You can use any client that uses a JDBC driver to
connect using Okta single sign-on or use a language like
Java to connect using a script. For installation and
configuration information, see [Configuring a connection for JDBC driver version 2.x for
Amazon Redshift](jdbc20-install.md "jdbc20-install.md").

For example, you can use SQLWorkbench/J as the client.
When you configure SQLWorkbench/J, the URL of your
database uses the following format.

```
jdbc:redshift:iam://`cluster-identifier`:`us-west-1`/`dev`
```

If you use SQLWorkbench/J as the client, take the
following steps:

    1. Start SQL Workbench/J. In the **Select
     Connection Profile** page, add a
     **Profile Group**, for example
     `Okta`.
    2. For **Connection Profile**,
     enter
     ``your-connection-profile-name``,
     for example `Okta`.
    3. Choose **Manage Drivers**,
     and choose **Amazon Redshift**.
     Choose the **Open Folder** icon
     next to **Library**, then choose
     the appropriate JDBC .jar file.
    4. On the **Select Connection
     Profile** page, add information to the
     connection profile as follows:




    	+ For **User**, enter your
    	 Okta user name. This is the user name of the Okta
    	 account that you are using for single sign-on that
    	 has permission to the cluster that you are trying
    	 to authenticate using.
    	+ For **Password**, enter
    	 your Okta password.
    	+ For **Drivers**, choose
    	 **Amazon Redshift
    	 (com.amazon.redshift.jdbc.Driver)**.
    	+ For **URL**, enter
    	 `jdbc:redshift:iam://`your-cluster-identifier`:`your-cluster-region`/`your-database-name``.
    5. Choose **Extended
     Properties** and do one of the
     following:




    	+ For **login\_url**, enter
    	 ``your-okta-sso-login-url``.
    	 This value specifies to the URL to use single
    	 sign-on as the authentication to log in to Okta.
    	+ For Okta single sign-on, for
    	 **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.OktaCredentialsProvider`.
    	 This value specifies to the driver to use Okta
    	 single sign-on as the authentication method.
    	+ For Okta single sign-on with MFA, for
    	 **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.BrowserSamlCredentialsProvider`.
    	 This value specifies to the driver to use Okta
    	 single sign-on with MFA as the authentication
    	 method.

ODBC

###### To set up ODBC for authentication to Okta

- Configure your database client to connect to your
  cluster through ODBC using Okta single sign-on.

Amazon Redshift provides ODBC drivers for Linux, Windows, and
macOS operating systems. Before you install an ODBC
driver, determine whether your SQL client tool is 32-bit
or 64-bit. Install the ODBC driver that matches the
requirements of your SQL client tool.

On Windows, in the **Amazon Redshift ODBC
Driver DSN Setup** page, under
**Connection Settings**, enter the
following information:

    + For **Data Source Name**,
     enter
     ``your-DSN``.
     This specifies the data source name used as the
     ODBC profile name.
    + For **Auth type**, do one of
     the following:




    	- For Okta single sign-on configuration,
    	 choose `Identity Provider:
    	 Okta`. This is the authentication
    	 method that the ODBC driver uses to authenticate
    	 using Okta single sign-on.
    	- For Okta single sign-on with MFA
    	 configuration, choose `Identity
    	 Provider: Browser SAML`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate using Okta single sign-on with
    	 MFA.
    + For **Cluster ID**, enter
     ``your-cluster-identifier``.
    + For **Region**, enter
     ``your-cluster-region``.
    + For **Database**, enter
     ``your-database-name``.
    + For **User**, enter
     ``your-okta-username``.
     This is the user name for the Okta account that
     you are using for single sign-on that has
     permission to the cluster that you're trying to
     authenticate using. Use this only for
     **Auth type** is
     **Identity Provider:
     Okta**.
    + For **Password**, enter
     ``your-okta-password``.
     Use this only for **Auth type**
     is **Identity Provider: Okta**.

On macOS and Linux, edit the `odbc.ini`
file as follows:

###### Note

All entries are case-insensitive.

    + For **clusterid**, enter
     ``your-cluster-identifier``.
     This is the name of the created Amazon Redshift
     cluster.
    + For **region**, enter
     ``your-cluster-region``.
     This is the AWS Region of the created Amazon Redshift
     cluster.
    + For **database**, enter
     ``your-database-name``.
     This is the name of the database that you're
     trying to access on the Amazon Redshift cluster.
    + For **locale**, enter
     `en-us`. This is the language
     that error messages display in.
    + For **iam**, enter
     `1`. This value specifies to
     the driver to authenticate using IAM
     credentials.
    + For **plugin\_name**, do one
     of the following:




    	- For Okta single sign-on with MFA
    	 configuration, enter
    	 `BrowserSAML`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate to Okta single sign-on with MFA.
    	- For Okta single sign-on configuration, enter
    	 `Okta`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate using Okta single sign-on.
    + For **uid**, enter
     ``your-okta-username``.
     This is the user name of the Okta account you are
     using for single sign-on that has permission to
     the cluster you are trying to authenticate
     against. Use this only for
     **plugin\_name** is
     **Okta**.
    + For **pwd**, enter
     ``your-okta-password``.
     Use this only for **plugin\_name**
     is **Okta**.
    + For **login\_url**, enter
     ``your-login-url``.
     This is the Initiate single sign-on URL that
     returns the SAML Response. This applies only to
     the Browser SAML plugin.
    + For **idp\_response\_timeout**,
     enter
     ``the-number-of-seconds``.
     This is the specified period of time in seconds to
     wait for response from PingOne. This applies only
     to the Browser SAML plugin.
    + For **listen\_port**, enter
     ``your-listen-port``.
     This is the port that local server is listening
     to. The default is 7890. This applies only to the
     Browser SAML plugin.

On macOS and Linux, also edit the profile settings to
add the following exports.

```
export ODBCINI=/opt/amazon/redshift/Setup/odbc.ini
```

```
export ODBCINSTINI=/opt/amazon/redshift/Setup/odbcinst.ini
```

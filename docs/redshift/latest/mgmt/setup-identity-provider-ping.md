Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Ping Identity

You can use Ping Identity as an identity provider (IdP) to access your Amazon Redshift
cluster. This tutorial shows you how you can use Ping Identity as an identity
provider (IdP) to access your Amazon Redshift cluster.

## Step 1: Set up Ping

Identity and your AWS account to trust each other

The following procedure describes how to set up a trust relationship using
the PingOne portal.

###### To set up Ping Identity and your AWS account to trust each

other

1. Create or use an existing Amazon Redshift cluster for your Ping Identity
   users to connect to. To configure the connection, certain properties
   of this cluster are needed, such as the cluster identifier. For more
   information, see [Creating a Cluster](create-cluster.md "create-cluster.md").
2. Add Amazon Redshift as a new SAML application on the PingOne portal. For
   detailed steps, see the [Ping Identity documentation](https://docs.pingidentity.com/ "https://docs.pingidentity.com/").
   1. Go to **My Applications**.
   2. Under **Add Application**, choose
      **New SAML Application**.
   3. For **Application Name**, enter
      `Amazon Redshift`.
   4. For **Protocol Version**, choose
      **SAML v2.0**.
   5. For **Category**, choose
      `your-application-category`.
   6. For **Assertion Consumer Service (ACS)**,
      type
      `your-redshift-local-host-url`.
      This is the local host and port that the SAML assertion
      redirects to.
   7. For **Entity ID**, enter
      `urn:amazon:webservices`.
   8. For **Signing**, choose **Sign
      Assertion**.
   9. In the **SSO Attribute Mapping** section,
      create the claims as shown in the following table.

   | Application attribute                                      | Identity bridge attribute of literal<br>value                                                                                                                                                                                                                 |
   | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **https://aws.amazon.com/SAML/Attributes/Role**            | arn:aws:iam::`123456789012`:role/`Ping`,arn:aws:iam::`123456789012`:saml-provider/`PingProvider`                                                                                                                                                              |
   | **https://aws.amazon.com/SAML/Attributes/RoleSessionName** | email                                                                                                                                                                                                                                                         |
   | **https://redshift.amazon.com/SAML/Attributes/AutoCreate** | "true"                                                                                                                                                                                                                                                        |
   | https://redshift.amazon.com/SAML/Attributes/DbUser         | email                                                                                                                                                                                                                                                         |
   | https://redshift.amazon.com/SAML/Attributes/DbGroups       | The groups in the “DbGroups” attributes<br>contain the @directory prefix. To remove this, in<br>**Identity bridge**, enter<br>**memberOf**. In<br>**Function**, choose<br>**ExtractByRegularExpression**.<br>In **Expression**, enter<br>**(.\*)[\@](?:.*)**. |

3. For **Group Access**, set up the following group
   access, if needed:
   - **https://aws.amazon.com/SAML/Attributes/Role**
   - **https://aws.amazon.com/SAML/Attributes/RoleSessionName**
   - **https://redshift.amazon.com/SAML/Attributes/AutoCreate**
   - **https://redshift.amazon.com/SAML/Attributes/DbUser**

4. Review your setup and make changes, if necessary.
5. Use the **Initiate Single Sign-On (SSO) URL** as
   the login URL for the Browser SAML plugin.
6. Create an IAM SAML identity provider on the IAM console. The
   metadata document that you provide is the federation metadata XML
   file that you saved when you set up Ping Identity. For detailed
   steps, see [Creating and Managing an IAM Identity Provider
   (Console)](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console") in the
   _IAM User Guide_.
7. Create an IAM role for SAML 2.0 federation on the IAM console. For
   detailed steps, see [Creating a Role for SAML](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create") in the
   _IAM User Guide_.
8. Create an IAM policy that you can attach to the IAM role that you
   created for SAML 2.0 federation on the IAM console. For detailed
   steps, see [Creating IAM Policies (Console)](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
   _IAM User Guide_. For an Azure AD example,
   see [Setting up JDBC or ODBC single
   sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

## Step 2: Set up JDBC or

ODBC for authentication to Ping Identity

JDBC

###### To set up JDBC for authentication to Ping

Identity

- Configure your database client to connect to your
  cluster through JDBC using Ping Identity single sign-on.

You can use any client that uses a JDBC driver to
connect using Ping Identity single sign-on or use a
language like Java to connect using a script. For
installation and configuration information, see [Configuring a connection for JDBC driver version 2.x for
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
     `Ping`.
    2. For **Connection Profile**,
     enter
     ``your-connection-profile-name``,
     for example `Ping`.
    3. Choose **Manage Drivers**,
     and choose **Amazon Redshift**.
     Choose the **Open Folder** icon
     next to **Library**, then choose
     the appropriate JDBC .jar file.
    4. On the **Select Connection
     Profile** page, add information to the
     connection profile as follows:




    	+ For **User**, enter your
    	 PingOne user name. This is the user name of the
    	 PingOne account that you are using for single
    	 sign-on that has permission to the cluster that
    	 you are trying to authenticate using.
    	+ For **Password**, enter
    	 your PingOne password.
    	+ For **Drivers**, choose
    	 **Amazon Redshift
    	 (com.amazon.redshift.jdbc.Driver)**.
    	+ For **URL**, enter
    	 `jdbc:redshift:iam://`your-cluster-identifier`:`your-cluster-region`/`your-database-name``.
    5. Choose **Extended
     Properties** and do one of the
     following:




    	+ For **login\_url**, enter
    	 ``your-ping-sso-login-url``.
    	 This value specifies to the URL to use single
    	 sign-on as the authentication to log in.
    	+ For Ping Identity, for
    	 **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.PingCredentialsProvider`.
    	 This value specifies to the driver to use Ping
    	 Identity single sign-on as the authentication
    	 method.
    	+ For Ping Identity with single sign-on, for
    	 **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.BrowserSamlCredentialsProvider`.
    	 This value specifies to the driver to use Ping
    	 Identity PingOne with single sign-on as the
    	 authentication method.

ODBC

###### To set up ODBC for authentication to Ping

Identity

- Configure your database client to connect to your
  cluster through ODBC using Ping Identity PingOne single
  sign-on.

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




    	- For Ping Identity configuration, choose
    	 **Identity Provider: Ping
    	 Federate**. This is the authentication
    	 method that the ODBC driver uses to authenticate
    	 using Ping Identity single sign-on.
    	- For Ping Identity with single sign-on
    	 configuration, choose **Identity Provider:
    	 Browser SAML**. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate using Ping Identity with single
    	 sign-on.
    + For **Cluster ID**, enter
     ``your-cluster-identifier``.
    + For **Region**, enter
     ``your-cluster-region``.
    + For **Database**, enter
     ``your-database-name``.
    + For **User**, enter
     ``your-ping-username``.
     This is the user name for the PingOne account that
     you are using for single sign-on that has
     permission to the cluster that you're trying to
     authenticate using. Use this only for
     **Auth type** is
     **Identity Provider:
     PingFederate**.
    + For **Password**, enter
     ``your-ping-password``.
     Use this only for **Auth type**
     is **Identity Provider:
     PingFederate**.
    + For **Listen Port**, enter
     ``your-listen-port``.
     This is the port that local server is listening
     to. The default is 7890. This applies only to the
     Browser SAML plugin.
    + For **Response Timeout**,
     enter
     ``the-number-of-seconds``.
     This is the number of seconds to wait before
     timing out when the IdP server sends back a
     response. The minimum number of seconds must be
     10. If establishing the connection takes longer
     than this threshold, then the connection is
     aborted. This applies only to the Browser SAML
     plugin.
    + For **Login URL**, enter
     ``your-login-url``.
     This applies only to the Browser SAML
     plugin.

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




    	- For Ping Identity configuration, enter
    	 `BrowserSAML`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate to Ping Identity.
    	- For Ping Identity with single sign-on
    	 configuration, enter `Ping`.
    	 This is the authentication method that the ODBC
    	 driver uses to authenticate using Ping Identity
    	 with single sign-on.
    + For **uid**, enter
     ``your-ping-username``.
     This is the user name of the Microsoft Azure
     account you are using for single sign-on that has
     permission to the cluster you are trying to
     authenticate against. Use this only for
     **plugin\_name** is
     **Ping**.
    + For **pwd**, enter
     ``your-ping-password``.
     Use this only for **plugin\_name**
     is **Ping**.
    + For **login\_url**, enter
     ``your-login-url``.
     This is the Initiate single sign-on URL that
     returns the SAML Response. This applies only to
     the Browser SAML plugin.
    + For **idp\_response\_timeout**,
     enter
     ``the-number-of-seconds``.
     This is the specified period of time in seconds to
     wait for response from PingOne Identity. This
     applies only to the Browser SAML plugin.
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

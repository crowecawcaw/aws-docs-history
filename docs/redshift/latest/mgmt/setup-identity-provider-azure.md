Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Azure

You can use Microsoft Azure AD as an identity provider (IdP) to access your
Amazon Redshift cluster. This tutorial shows you how you can use Azure as an identity
provider (IdP) to access your Amazon Redshift cluster.

To learn how to federate Amazon Redshift access with Microsoft Azure AD
single sign-on, watch the following video.

## Step 1: Set up Azure

and your AWS account to trust each other

The following procedure describes how to set up a trust
relationship.

###### To set up Azure AD and your AWS account to trust each other

1. Create or use an existing Amazon Redshift cluster for your Azure AD users to
   connect to. To configure the connection, certain properties of this
   cluster are needed, such as the cluster identifier. For more
   information, see [Creating a Cluster](create-cluster.md "create-cluster.md").
2. Set up an Azure Active Directory, groups, users used for AWS on
   the Microsoft Azure portal.
3. Add Amazon Redshift as an enterprise application on the Microsoft Azure
   portal to use for single sign-on to the AWS Console and federated
   login to Amazon Redshift. Choose **Enterprise
   application**.
4. Choose **+New application**. The Add an
   application page appears.
5. Search for `AWS` in the search field.
6. Choose **Amazon Web Services (AWS)** and choose
   **Add**. This creates the AWS
   application.
7. Under **Manage**, choose **Single
   sign-on**.
8. Choose **SAML**. The Amazon Web Services (AWS) |
   SAML-based Sign-on page appears.
9. Choose **Yes** to proceed to the Set up Single
   Sign-On with SAML page. This page shows the list of pre-configured
   single sign-on related attributes.
10. For **Basic SAML Configuration**, choose the edit
    icon and choose **Save**.
11. When you are configuring for more than one application, provide an
    identifier value. For example, enter
    `https://signin.aws.amazon.com/saml#2`.
    Note that from the second application onwards, use this format with
    a # sign to specify a unique SPN value.
12. In the **User Attributes and Claims** section,
    choose the edit icon.

By default, the Unique User Identifier (UID), Role,
RoleSessionName, and SessionDuration claims are
pre-configured. 13. Choose **+ Add new claim** to add a claim for
database users.

For **Name**, enter
`DbUser`.

For **Namespace**, enter
`https://redshift.amazon.com/SAML/Attributes`.

For **Source**, choose
**Attribute**.

For **Source attribute**, choose
**user.userprincipalname**. Then, choose
**Save**. 14. Choose **+ Add new claim** to add a claim for
AutoCreate.

For **Name**, enter
`AutoCreate`.

For **Namespace**, enter
`https://redshift.amazon.com/SAML/Attributes`.

For **Source**, choose
**Attribute**.

For **Source attribute**, choose
**"true"**. Then, choose
**Save**.

Here, `123456789012` is your
AWS account, `AzureSSO` is
an IAM role you created, and
`AzureADProvider` is
the IAM provider.

| Claim name                                                 | Value                                                                                                   |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Unique user identifier (name ID)                           | user.userprincipalname                                                                                  |
| **https://aws.amazon.com/SAML/Attributes/SessionDuration** | "900"                                                                                                   |
| **https://aws.amazon.com/SAML/Attributes/Role**            | arn:aws:iam::`123456789012`:role/`AzureSSO`,arn:aws:iam::`123456789012`:saml-provider/`AzureADProvider` |
| **https://aws.amazon.com/SAML/Attributes/RoleSessionName** | user.userprincipalname                                                                                  |
| **https://redshift.amazon.com/SAML/Attributes/AutoCreate** | "true"                                                                                                  |
| **https://redshift.amazon.com/SAML/Attributes/DbGroups**   | user.assignedroles                                                                                      |
| **https://redshift.amazon.com/SAML/Attributes/DbUser**     | user.userprincipalname                                                                                  |

15. Under \*\*App Registration >
    `your-application-name`
    > Authentication**, add **Mobile And Desktop
    > Application\*\*. Specify the URL as
    > http://localhost/redshift/.
16. In the **SAML Signing Certificate** section,
    choose **Download** to download and save the
    federation metadata XML file for use when you create an IAM SAML
    identity provider. This file is used to create the single sign-on
    federated identity.
17. Create an IAM SAML identity provider on the IAM console. The
    metadata document that you provide is the federation metadata XML
    file that you saved when you set up Azure Enterprise Application.
    For detailed steps, see [Creating and Managing an IAM Identity Provider
    (Console)](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console") in the _IAM User Guide_.
18. Create an IAM role for SAML 2.0 federation on the IAM console. For
    detailed steps, see [Creating a Role for SAML](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create") in the
    _IAM User Guide_.
19. Create an IAM policy that you can attach to the IAM role that you created for SAML 2.0
    federation on the IAM console. For detailed steps, see [Creating IAM Policies (Console)](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
    _IAM User Guide_.

Modify the following policy (in JSON format) for your environment:

    * Substitute the AWS Region of your cluster for
     ``us-west-1``.
    * Substitute your AWS account for ``123456789012``.
    * Substitute your cluster identifier (or `*` for all clusters) for
     ``cluster-identifier``.
    * Substitute your database (or `*` for all databases) for
     ``dev``.
    * Substitute the unique identifier of your IAM role for
     ``AROAJ2UCCR6DPCEXAMPLE``.
    * Substitute your tenant or company email domain for
     ``example.com``.
    * Substitute the database group that you plan to assign the user to for
     ``my_dbgroup``.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "redshift:GetClusterCredentials",
            "Resource": [
                "arn:aws:redshift:`us-west-1`:`123456789012`:dbname:`cluster-identifier`/`dev`",
                "arn:aws:redshift:`us-west-1`:`123456789012`:dbuser:`cluster-identifier`/${redshift:DbUser}",
                "arn:aws:redshift:`us-west-1`:`123456789012`:cluster:`cluster-identifier`"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:userid": "`AROAJ2UCCR6DPCEXAMPLE`:${redshift:DbUser}@`example.com`"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "redshift:CreateClusterUser",
            "Resource": "arn:aws:redshift:`us-west-1`:`123456789012`:dbuser:`cluster-identifier`/${redshift:DbUser}"
        },
        {
            "Effect": "Allow",
            "Action": "redshift:JoinGroup",
            "Resource": "arn:aws:redshift:`us-west-1`:`123456789012`:dbgroup:`cluster-identifier`/`my_dbgroup`"
        },
        {
            "Effect": "Allow",
            "Action": [
                "redshift:DescribeClusters",
                "iam:ListRoles"
            ],
            "Resource": "*"
        }
    ]
}
```

This policy grants permissions as follows:

    * The first section grants permission to the `GetClusterCredentials` API operation to
     get temporary credentials for the specified cluster. In this
     example, the resource is
     ``cluster-identifier``
     with database ``dev``, in
     account ``123456789012``, and in
     AWS Region ``us-west-1``. The
     `${redshift:DbUser}` clause allows only users that
     match the `DbUser` value specified in Azure AD to
     connect.
    * The condition clause enforces that only certain users get temporary credentials. These are users under
     the role specified by the role unique ID
     ``AROAJ2UCCR6DPCEXAMPLE``
     in the IAM account identified by an email address in your
     company's email domain. For more information about unique IDs,
     see [Unique IDs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids") in the *IAM User Guide*.


    Your setup with your IdP (in this case, Azure AD) determines how the
     condition clause is written. If your employee's email is
     `johndoe@example.com`, first set
     `${redshift:DbUser}` to the super field that matches
     the employee's user name `johndoe`. Then, to make this condition work, set the AWS
     SAML `RoleSessionName` field to the super field that
     matches the employee’s email `johndoe@example.com`.
     When you take this approach, consider the following:




    	+ If you set `${redshift:DbUser}` to be the employee's email, then remove the
    	 `@example.com` in the example JSON to match
    	 the `RoleSessionName`.
    	+ If you set the `RoleSessionId` to be just the employee's user name, then
    	 remove the `@example.com` in the example to match
    	 the `RoleSessionName`.
    	+ In the example JSON, the `${redshift:DbUser}` and `RoleSessionName` are both
    	 set to the employee's email. This example JSON uses the
    	 Amazon Redshift database user name with `@example.com` to
    	 sign the user in to access the cluster.
    * The second section grants permission to create a `dbuser` name in the specified cluster.
     In this example JSON, it restricts creation to `${redshift:DbUser}`.
    * The third section grants permission to specify which `dbgroup` a user can join.
     In this example JSON, a user can join the `my_dbgroup` group in the specified cluster.
    * The fourth section grants permission to actions the user can do on all resources. In this
     example JSON, it allows users to call
     `redshift:DescribeClusters` to get cluster
     information such as the cluster endpoint, AWS Region, and port. It
     also allows users to call `iam:ListRoles` to check which
     roles a user can assume.

## Step 2: Set up JDBC or

ODBC for authentication to Azure

JDBC

###### To set up JDBC for authentication to Microsoft Azure

AD

- Configure your database client to connect to your
  cluster through JDBC using your Azure AD single sign-on.

You can use any client that uses a JDBC driver to
connect using Azure AD single sign-on or use a language
like Java to connect using a script. For installation
and configuration information, see [Configuring a connection for JDBC driver version 2.x for
Amazon Redshift](jdbc20-install.md "jdbc20-install.md").

For example, you can use SQLWorkbench/J as the client.
When you configure SQLWorkbench/J, the URL of your
database uses the following format.

```
jdbc:redshift:iam://`cluster-identifier`:`us-west-1`/`dev`
```

If you use SQLWorkbench/J as the client, take the
following steps:

    1. Start SQL Workbench/J. On the **Select
     Connection Profile** page, add a
     **Profile Group** called
     `AzureAuth`.
    2. For **Connection Profile**,
     enter `Azure`.
    3. Choose **Manage Drivers**,
     and choose **Amazon Redshift**.
     Choose the **Open Folder** icon
     next to **Library**, then choose
     the appropriate JDBC .jar file.
    4. On the **Select Connection
     Profile** page, add information to the
     connection profile as follows:




    	+ For **User**, enter your
    	 Microsoft Azure user name. This is the user name
    	 of the Microsoft Azure account that you are using
    	 for single sign-on that has permission to the
    	 cluster that you are trying to authenticate
    	 using.
    	+ For **Password**, enter
    	 your Microsoft Azure password.
    	+ For **Drivers**, choose
    	 **Amazon Redshift
    	 (com.amazon.redshift.jdbc.Driver)**.
    	+ For **URL**, enter
    	 `jdbc:redshift:iam://`your-cluster-identifier`:`your-cluster-region`/`your-database-name``.
    5. Choose **Extended
     Properties** to add additional
     information to the connection properties, as
     described following.



    For Azure AD single sign-on configuration,
     add additional information as follows:



    	+ For **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.AzureCredentialsProvider`.
    	 This value specifies to the driver to use Azure AD
    	 Single Sign-On as the authentication method.
    	+ For **idp\_tenant**, enter
    	 ``your-idp-tenant``.
    	 Used only for Microsoft Azure AD. This is the
    	 tenant name of your company configured on Azure
    	 AD. This value can either be the tenant name or
    	 the tenant unique ID with hyphens.
    	+ For **client\_secret**,
    	 enter
    	 ``your-azure-redshift-application-client-secret``.
    	 Used only for Microsoft Azure AD. This is your
    	 client secret of the Amazon Redshift application that you
    	 created when setting up your Azure Single Sign-On
    	 configuration. This is only applicable to the
    	 com.amazon.redshift.plugin.AzureCredentialsProvider
    	 plugin.
    	+ For **client\_id**, enter
    	 ``your-azure-redshift-application-client-id``.
    	 Used only for Microsoft Azure AD. This is the
    	 client ID (with hyphens) of the Amazon Redshift application
    	 that you created when setting up your Azure Single
    	 Sign-On configuration.

    For Azure AD single sign-on with MFA
     configuration, add additional information to the
     connection properties as follows:



    	+ For **plugin\_name**, enter
    	 `com.amazon.redshift.plugin.BrowserAzureCredentialsProvider`.
    	 This value specifies to the driver to use Azure AD
    	 single sign-on with MFA as the authentication
    	 method.
    	+ For **idp\_tenant**, enter
    	 ``your-idp-tenant``.
    	 Used only for Microsoft Azure AD. This is the
    	 tenant name of your company configured on Azure
    	 AD. This value can either be the tenant name or
    	 the tenant unique ID with hyphens.
    	+ For **client\_id**, enter
    	 ``your-azure-redshift-application-client-id``.
    	 This option is used only for Microsoft Azure AD.
    	 This is the client ID (with hyphens) of the Amazon Redshift
    	 application that you created when setting up your
    	 Azure AD single sign-on with MFA configuration.
    	+ For **listen\_port**, enter
    	 ``your-listen-port``.
    	 This is the port that local server is listening
    	 to. The default is 7890.
    	+ For
    	 **idp\_response\_timeout**, enter
    	 ``the-number-of-seconds``.
    	 This is the number of seconds to wait before
    	 timing out when the IdP server sends back a
    	 response. The minimum number of seconds must be
    	 10. If establishing the connection takes longer
    	 than this threshold, then the connection is
    	 aborted.

ODBC

###### To set up ODBC for authentication to Microsoft Azure

AD

- Configure your database client to connect to your
  cluster through ODBC using your Azure AD single sign-on.

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
    + For **Auth type** for Azure
     AD single sign-on configuration, choose
     `Identity Provider: Azure
     AD`. This is the authentication method
     that the ODBC driver uses to authenticate using
     Azure single sign-on.
    + For **Auth type** for Azure
     AD single sign-on with MFA configuration, choose
     `Identity Provider: Browser Azure
     AD`. This is the authentication method
     that the ODBC driver uses to authenticate using
     Azure single sign-on with MFA.
    + For **Cluster ID**, enter
     ``your-cluster-identifier``.
    + For **Region**, enter
     ``your-cluster-region``.
    + For **Database**, enter
     ``your-database-name``.
    + For **User**, enter
     ``your-azure-username``.
     This is the user name for the Microsoft Azure
     account that you are using for single sign-on that
     has permission to the cluster that you're trying
     to authenticate using. Use this only for
     **Auth Type** is
     **Identity Provider: Azure
     AD**.
    + For **Password**, enter
     ``your-azure-password``.
     Use this only for **Auth Type**
     is **Identity Provider: Azure
     AD**.
    + For **IdP Tenant**, enter
     ``your-idp-tenant``.
     This is the tenant name of your company configured
     on your IdP (Azure). This value can either be the
     tenant name or the tenant unique ID with
     hyphens.
    + For **Azure Client Secret**,
     enter
     ``your-azure-redshift-application-client-secret``.
     This is the client secret of the Amazon Redshift application
     that you created when setting up your Azure single
     sign-on configuration.
    + For **Azure Client ID**,
     enter
     ``your-azure-redshift-application-client-id``.
     This is the client ID (with hyphens) of the Amazon Redshift
     application that you created when setting up your
     Azure single sign-on configuration.
    + For **Listen Port**, enter
     ``your-listen-port``.
     This is the default listen port that local server
     is listening to. The default is 7890. This applies
     only to the Browser Azure AD plugin.
    + For **Response Timeout**,
     enter
     ``the-number-of-seconds``.
     This is the number of seconds to wait before
     timing out when the IdP server sends back a
     response. The minimum number of seconds must be
     10. If establishing the connection takes longer
     than this threshold, then the connection is
     aborted. This option applies only to the Browser
     Azure AD plugin.

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
    + For **plugin\_name** for Azure
     AD single sign-on configuration, enter
     `AzureAD`. This specifies to
     the driver to use Azure Single Sign-On as the
     authentication method.
    + For **plugin\_name** for Azure
     AD single sign-on with MFA configuration, enter
     `BrowserAzureAD`. This
     specifies to the driver to use Azure Single
     Sign-On with MFA as the authentication method.
    + For **uid**, enter
     ``your-azure-username``.
     This is the user name of the Microsoft Azure
     account you are using for single sign-on that has
     permission to the cluster you are trying to
     authenticate against. Use this only for
     **plugin\_name** is
     **AzureAD**.
    + For **pwd**, enter
     ``your-azure-password``.
     Use this only for **plugin\_name**
     is **AzureAD**.
    + For **idp\_tenant**, enter
     ``your-idp-tenant``.
     This is the tenant name of your company configured
     on your IdP (Azure). This value can either be the
     tenant name or the tenant unique ID with
     hyphens.
    + For **client\_secret**, enter
     ``your-azure-redshift-application-client-secret``.
     This is the client secret of the Amazon Redshift application
     that you created when setting up your Azure single
     sign-on configuration.
    + For **client\_id**, enter
     ``your-azure-redshift-application-client-id``.
     This is the client ID (with hyphens) of the Amazon Redshift
     application that you created when setting up your
     Azure single sign-on configuration.
    + For **listen\_port**, enter
     ``your-listen-port``.
     This is the port that local server is listening
     to. The default is 7890. This applies to the
     Browser Azure AD plugin.
    + For **idp\_response\_timeout**,
     enter
     ``the-number-of-seconds``.
     This is the specified period of time in seconds to
     wait for response from Azure. This option applies
     to the Browser Azure AD plugin.

On macOS and Linux, also edit the profile settings to
add the following exports.

```
export ODBCINI=/opt/amazon/redshift/Setup/odbc.ini
```

```
export ODBCINSTINI=/opt/amazon/redshift/Setup/odbcinst.ini
```

## Troubleshooting

To troubleshoot issues with the Browser Azure AD plugin, consider the following.

- To use the Browser Azure AD plugin, you must set the reply URL
  specified in the request to match the reply URL configured for your
  application. Navigate to the **Set up Single Sign-On with SAML**
  page on the Microsoft Azure portal. Then check the **Reply
  URL** is set to http://localhost/redshift/.
- If you get an IdP tenant error, verify that the **IdP
  Tenant** name matches the domain name you initially used to
  set up the Active Directory in Microsoft Azure.

On Windows, navigate to the **Connection Settings**
section of the **Amazon Redshift ODBC DSN Setup** page. Then
check the tenant name of your company configured on your IdP (Azure)
matches the domain name you initially used to set up the Active
Directory in Microsoft Azure.

On macOS and Linux, find the _odbc.ini_ file. Then
check the tenant name of your company configured on your IdP (Azure)
matches the domain name you initially used to set up the Active
Directory in Microsoft Azure.

- If you get an error that the reply URL specified in the request does
  not match the reply URLs configured for your application, verify that
  the **Redirect URIs** is the same as the reply
  URL.

Navigate to the **App registration** page of your
application on the Microsoft Azure portal. Then check the Redirect URIs
matches the reply URL.

- If you get the unexpected response: unauthorized error, verify that
  you completed the **Mobile and desktop applications**
  configuration.

Navigate to the **App registration** page of your
application on the Microsoft Azure portal. Then navigate to
**Authentication** and check that you configured
**Mobile and desktop applications** to use
http://localhost/redshift/ as the redirect URIs.

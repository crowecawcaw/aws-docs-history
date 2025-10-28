# Configure single sign-on using ODBC, SAML 2.0, and the Okta

Identity Provider

To connect to data sources, you can use Amazon Athena with identity providers (IdPs) like
PingOne, Okta, OneLogin, and others. Starting with Athena ODBC driver version 1.1.13 and
Athena JDBC driver version 2.0.25, a browser SAML plugin is included that you can configure
to work with any SAML 2.0 provider. This topic shows you how to configure the Amazon Athena ODBC
driver and the browser-based SAML plugin to add single sign-on (SSO) capability using the
Okta identity provider.

## Prerequisites

Completing the steps in this tutorial requires the following:

- Athena ODBC driver version 1.1.13 or later. Versions 1.1.13 and later include
  browser SAML support. For download links, see [Connecting to Amazon Athena with ODBC](connect-with-odbc.md "connect-with-odbc.md").
- An IAM Role that you want to use with SAML. For more information, see [Creating a role for SAML 2.0 federation](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md") in the _IAM User Guide_.
- An Okta account. For information, visit [okta.com](https://www.okta.com/ "https://www.okta.com/").

## Creating an app

integration in Okta

First, use the Okta dashboard to create and configure a SAML 2.0 app for single
sign-on to Athena.

###### To use the Okta dashboard to set up single sign-on for Athena

1. Login to the Okta admin page on `okta.com`.
2. In the navigation pane, choose **Applications**,
   **Applications**.
3. On the **Applications** page, choose **Create App
   Integration**.

![Choose Create App Integration.](images/okta-saml-sso-1.png) 4. In the **Create a new app integration** dialog box, for
**Sign-in method**, select **SAML 2.0**,
and then choose **Next**.

![Choose SAML 2.0](images/okta-saml-sso-2.png) 5. On the **Create SAML Integration** page, in the
**General Settings** section, enter a name for the
application. This tutorial uses the name **Athena SSO**.

![Enter a name for the Okta application.](images/okta-saml-sso-3.png) 6. Choose **Next**. 7. On the **Configure SAML** page, in the **SAML
Settings** section, enter the following values:

    * For **Single sign on URL**, enter
     `http://localhost:7890/athena`
    * For **Audience URI**, enter
     `urn:amazon:webservices`



    ![Enter SAML settings.](images/okta-saml-sso-4.png)

8. For **Attribute Statements (optional)**, enter the following
   two name/value pairs. These are required mapping attributes.
   - For **Name**, enter the following URL:

   `https://aws.amazon.com/SAML/Attributes/Role`

   For **Value**, enter the name of your IAM role. For
   information about the IAM role format, see [Configuring SAML assertions for the authentication response](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md")
   in the _IAM User Guide_.
   - For **Name**, enter the following URL:

   `https://aws.amazon.com/SAML/Attributes/RoleSessionName`

   For **Value**, enter
   `user.email`.

   ![Enter SAML attributes for Athena.](images/okta-saml-sso-5.png)

9. Choose **Next**, and then choose **Finish**.

When Okta creates the application, it also creates your login URL, which you
will retrieve next.

## Getting

the login URL from the Okta dashboard

Now that your application has been created, you can obtain its login URL and other
metadata from the Okta dashboard.

###### To get the login URL from the Okta dashboard

1. In the Okta navigation pane, choose **Applications**,
   **Applications**.
2. Choose the application for which you want to find the login URL (for example,
   **AthenaSSO**).
3. On the page for your application, choose **Sign On**.

![Choose Sign On.](images/okta-saml-sso-6.png) 4. Choose **View Setup Instructions**.

![Choose View Setup Instructions.](images/okta-saml-sso-7.png) 5. On the **How to Configure SAML 2.0 for Athena SSO** page, find
the URL for **Identity Provider Issuer**. Some places in the
Okta dashboard refer to this URL as the **SAML issuer
ID**.

![The value for Identity Provider Issuer.](images/okta-saml-sso-8.png) 6. Copy or store the value for **Identity Provider Single Sign-On
URL**.

In the next section, when you configure the ODBC connection, you will provide
this value as the **Login URL** connection parameter for the
browser SAML plugin.

## Configuring the browser SAML ODBC connection to Athena

Now you are ready to configure the browser SAML connection to Athena using the ODBC
Data Sources program in Windows.

###### To configure the browser SAML ODBC connection to Athena

1. In Windows, launch the **ODBC Data Sources** program.
2. In the **ODBC Data Source Administrator** program, choose
   **Add**.

![Choose Add.](images/okta-saml-sso-9.png) 3. Choose **Simba Athena ODBC Driver**, and then choose
**Finish**.

![Choose Simba Athena Driver](images/okta-saml-sso-10.png) 4. In the **Simba Athena ODBC Driver DSN Setup** dialog, enter
the values described.

![Enter the DSN setup values.](images/okta-saml-sso-11.png)

    * For **Data Source Name,** enter a name for your data
     source (for example, **Athena ODBC 64**).
    * For **Description**, enter a description for your
     data source.
    * For **AWS Region**, enter the AWS Region that you
     are using (for example, `us-west-1`).
    * For **S3 Output Location**, enter the Amazon S3 path where
     you want your output to be stored.

5. Choose **Authentication Options**.
6. In the **Authentication Options** dialog box, choose or enter
   the following values.

![Enter authentication options.](images/okta-saml-sso-12.png)

    * For **Authentication Type**, choose
     **BrowserSAML**.
    * For **Login URL**, enter the **Identity
     Provider Single Sign-On URL** that you obtained from the
     Okta dashboard.
    * For **Listen Port**, enter
     **7890**.
    * For **Timeout (sec)**, enter a connection timeout
     value in seconds.

7. Choose **OK** to close **Authentication
   Options**.
8. Choose **Test** to test the connection, or
   **OK** to finish.

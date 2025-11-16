Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Options for providing IAM

credentials

To provide IAM credentials for a JDBC or ODBC connection, choose one of the following
options.

- **AWS profile**

As an alternative to providing credentials values in the form of JDBC or ODBC
settings, you can put the values in a named profile. For more information, see
[Using a configuration profile](#using-configuration-profile "#using-configuration-profile").

- **IAM credentials**

Provide values for AccessKeyID, SecretAccessKey, and, optionally, SessionToken
in the form of JDBC or ODBC settings. SessionToken is required only for an IAM
role with temporary credentials. For more information, see [JDBC and ODBC options
for providing IAM credentials](#jdbc-options-for-providing-iam-credentials "#jdbc-options-for-providing-iam-credentials").

- **Identity provider federation**

When you use identity provider federation to enable users from an identity
provider to authenticate to Amazon Redshift, specify the name of a credential provider
plugin. For more information, see [Credentials provider
plugins](#using-credentials-provider-plugin "#using-credentials-provider-plugin").

The Amazon Redshift JDBC and ODBC drivers include plugins for the following SAML-based
identity federation credential providers:

    + Microsoft Active Identity Federation Services (AD FS)
    + PingOne
    + Okta
    + Microsoft Azure Active Directory (Azure AD)

You can provide the plugin name and related values in the form of JDBC or ODBC
settings or by using a profile. For more information, see [Options for JDBC driver version 2.x
configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md").
For more information, see [Step
5: Configure a JDBC or ODBC connection to use IAM credentials](generating-iam-credentials-steps.md#generating-iam-credentials-configure-jdbc-odbc "generating-iam-credentials-steps.md#generating-iam-credentials-configure-jdbc-odbc").

## Using a configuration profile

You can supply the IAM credentials options and `GetClusterCredentials`
options as settings in named profiles in your AWS configuration file. To provide
the profile name, use the Profile JDBC option. The configuration is stored in a file
named `config` or a file named `credentials` in a folder named
`.aws` in your home directory.

For a SAML-based credential provider plugin included with an Amazon Redshift JDBC or ODBC
driver, you can use the settings described just preceding in [Credentials provider
plugins](#using-credentials-provider-plugin "#using-credentials-provider-plugin"). If `plugin_name`
isn't used, the other options are ignored.

The following example shows the ~/.aws/credentials file with two profiles.

```
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[user2]
aws_access_key_id=AKIAI44QH8DHBEXAMPLE
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
session_token=AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQWLWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGd
QrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU
9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz
+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==

```

To use the credentials for the `user2` example, specify
`Profile=user2` in the JDBC URL.

For more information on using profiles, see [Configuration and credential file
settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide._

For more information on using profiles for the JDBC driver, see [Specifying profiles](jdbc20-configure-authentication-ssl.md#jdbc20-aws-credentials-profiles "jdbc20-configure-authentication-ssl.md#jdbc20-aws-credentials-profiles").

For more information on using profiles for the ODBC driver, see [Authentication methods](odbc20-authentication-ssl.md "odbc20-authentication-ssl.md").

## JDBC and ODBC options

for providing IAM credentials

The following table lists the JDBC and ODBC options for providing IAM
credentials.

| Option                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Iam`                                                | For use only in an ODBC connection string. Set to<br>1 to use IAM authentication.                                                                                                                                                                                                                                                                                                                                 |
| `AccessKeyID`<br>`SecretAccessKey`<br>`SessionToken` | The access key ID and secret access key for the<br>IAM role or user configured for IAM database authentication.<br>`SessionToken` is required only for an IAM role with<br>temporary credentials. SessionToken isn't used for a user. For more<br>information, see [Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md"). |
| `plugin_name`                                        | The fully qualified name of a class that<br>implements a credentials provider. The Amazon Redshift JDBC driver includes<br>SAML-based credential provider plugins. If you provide<br>`plugin_name`, you can also provide other related<br>options. For more information, see [Credentials provider<br>plugins](#using-credentials-provider-plugin "#using-credentials-provider-plugin").                          |
| `Profile`                                            | The name of a profile in an AWS credentials or<br>config file that contains values for the JDBC connection options.<br>For more information, see [Using a configuration profile](#using-configuration-profile "#using-configuration-profile").                                                                                                                                                                    |

## JDBC

and ODBC options for creating database user credentials

To use the Amazon Redshift JDBC or ODBC driver to create database user credentials, provide
the database user name as a JDBC or ODBC option. Optionally, you can have the driver
create a new database user if one doesn't exist, and you can specify a list of
database user groups the user joins at login.

If you use an identity provider (IdP), work with your IdP administrator to
determine the correct values for these options. Your IdP administrator can also
configure your IdP to provide these options, in which case you don't need to provide
them as JDBC or ODBC options. For more information, see [Step 2: Configure SAML
assertions for your IdP](generating-iam-credentials-steps.md#configuring-saml-assertions "generating-iam-credentials-steps.md#configuring-saml-assertions").

###### Note

If you use an IAM policy variable `${redshift:DbUser}`, as
described in [Resource
policies for GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources "redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources")
the value for `DbUser` is replaced with the value retrieved by the
API operation's request context. The Amazon Redshift drivers use the value for the
`DbUser` variable provided by the connection URL, rather than the
value supplied as a SAML attribute.

To help secure this configuration, we recommend that you use a condition in an
IAM policy to validate the `DbUser` value with the
`RoleSessionName`. You can find examples of how to set a
condition using an IAM policy in [Example 8: IAM policy for using
GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-examples-getclustercredentials "redshift-iam-access-control-identity-based.md#redshift-policy-examples-getclustercredentials").

The following table lists the options for creating database user credentials.

| Option     | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DbUser     | The name of a database user. If a user named DbUser exists in<br>the database, the temporary user credentials have the same<br>permissions as the existing user. If DbUser doesn't exist<br>in the database and AutoCreate is true, a new user named DbUser<br>is created. Optionally, disable the password for an existing<br>user. For more information, see [ALTER_USER](../dg/r_ALTER_USER.md "../dg/r_ALTER_USER.md") |
| AutoCreate | Specify `true` to create a database user with the<br>name specified for DbUser if one does not exist. The default is<br>false.                                                                                                                                                                                                                                                                                             |
| `DbGroups` | A comma-delimited list of the names of one or more<br>existing database groups the database user joins for the current<br>session. By default, the new user is added only to PUBLIC.                                                                                                                                                                                                                                       |

## Credentials provider

plugins

Amazon Redshift uses credentials provider plugins for single sign-on authentication.

To support single sign-on authentication, Amazon Redshift provides the Azure AD plugin for
Microsoft Azure Active Directory. For information on how to configure this plugin,
see [Setting up JDBC or ODBC single
sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

### Multi-factor authentication

To support multi-factor authentication (MFA), Amazon Redshift provides browser-based
plugins. Use the browser SAML plugin for Okta, PingOne, and the browser Azure AD
plugin for Microsoft Azure Active Directory.

With the browser SAML plugin, OAuth authentication flows like this:

![OAuth workflows for how the plugin, local server, web browser, and endpoint work together to authenticate a user with SAML authentication.](images/BrowserSAML_plugin.png)

1. A user tries to log in.
2. The plugin launches a local server to listen to incoming connections
   on the localhost.
3. The plugin launches a web browser to request a SAML response over
   HTTPS from the specified single sign-on login URL federated identity
   provider endpoint.
4. The web browser follows the link and prompts the user to enter
   credentials.
5. After the user authenticates and grants consent, the federated
   identity provider endpoint returns a SAML response over HTTPS to the URI
   indicated by `redirect_uri`.
6. The web browser moves the response message with the SAML response to
   the indicated `redirect_uri`.
7. The local server accepts the incoming connection and the plugin
   retrieves the SAML response and passes it to Amazon Redshift.

With the browser Azure AD plugin, SAML authentication flows like this:

![Azure workflows for how the plugin, local server, web browser, and endpoint work together to authenticate a user with SAML authentication.](images/BrowserAzure_plugin.png)

1. A user tries to log in.
2. The plugin launches a local server to listen to incoming connections
   on the localhost.
3. The plugin launches a web browser to request an authorization code
   from the Azure AD `oauth2/authorize` endpoint.
4. The web browser follows the generated link over HTTPS and prompts the
   user to enter credentials. The link is generated using configuration
   properties, such as tenant and client_id.
5. After the user authenticates and grants consent, the Azure AD
   `oauth2/authorize` endpoint returns and sends a response
   over HTTPS with the authorization code to the indicated
   `redirect_uri`.
6. The web browser moves the response message with the SAML response to
   the indicated `redirect_uri`.
7. The local server accepts the incoming connection and the plugin
   requests and retrieves the authorization code and sends a POST request
   to the Azure AD `oauth2/token` endpoint.
8. The Azure AD `oauth2/token` endpoint returns a response
   with an access token to the indicated `redirect_uri`.
9. The plugin retrieves the SAML response and passes it to Amazon Redshift.

See the following sections:

- Active Directory Federation Services (AD FS)

For more information, see [Setting up JDBC or ODBC single
sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

- PingOne (Ping)

Ping is supported only with the predetermined PingOne IdP Adapter
using Forms authentication.

For more information, see [Setting up JDBC or ODBC single
sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

- Okta

Okta is supported only for the Okta-supplied application used with the
AWS Management Console.

For more information, see [Setting up JDBC or ODBC single
sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

- Microsoft Azure Active Directory

For more information, see [Setting up JDBC or ODBC single
sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

### Plugin options

To use a SAML-based credentials provider plugin, specify the following options
using JDBC or ODBC options or in a named profile. If `plugin_name`
isn't specified, the other options are ignored.

| Option           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `plugin_name`    | For JDBC, the class name that implements a credentials<br>provider. Specify one of the following:<br>• For Active Directory Federation Services<br>`<br>com.amazon.redshift.plugin.AdfsCredentialsProvider<br>`<br>• For Okta<br>`<br>com.amazon.redshift.plugin.OktaCredentialsProvider<br>`<br>• For PingFederate<br>`<br>com.amazon.redshift.plugin.PingCredentialsProvider<br>`<br>• For Microsoft Azure Active Directory<br>`<br>com.amazon.redshift.plugin.AzureCredentialsProvider<br>`<br>• For SAML MFA<br>`<br>com.amazon.redshift.plugin.BrowserSamlCredentialsProvider<br>`<br>• For Microsoft Azure Active Directory single<br>sign-on with MFA<br>`<br>com.amazon.redshift.plugin.BrowserAzureCredentialsProvider<br>`<br>For ODBC, specify one of the<br>following:<br>• For Active Directory Federation Services:<br>`adfs`<br>• For Okta: `okta`<br>• For PingFederate: `ping`<br>• For Microsoft Azure Active Directory:<br>`azure`<br>• For SAML MFA: `browser saml`<br>• For Microsoft Azure Active Directory single<br>sign-on with MFA: `browser azure<br>ad` |
| `idp_host`       | The name of the corporate identity provider<br>host. This name should not include any slashes (‘/’). For an<br>Okta identity provider, the value for `idp_host`<br>should end with `.okta.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idp_port`       | The port used by the identity provider. The<br>default is 443. This port is ignored for Okta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `preferred_role` | A role Amazon Resource Name (ARN) from the<br>`AttributeValue` elements for the<br>`Role` attribute in the SAML assertion. To find<br>the appropriate value for the preferred role, work with your IdP<br>administrator. For more information, see [Step 2: Configure SAML<br>assertions for your IdP](generating-iam-credentials-steps.md#configuring-saml-assertions "generating-iam-credentials-steps.md#configuring-saml-assertions").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user`           | A corporate user name, including the domain<br>when applicable. For example, for Active Directory, the domain<br>name is required in the format<br>_domain\username_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| password         | The corporate user's password. We<br>recommend not using this option. Instead, use your SQL client to<br>supply the password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `app_id`         | An ID for an Okta application. Used only with<br>Okta. The value for `app_id` follows<br>`amazon_aws` in the Okta application embed link.<br>To get this value, work with your IdP administrator. The<br>following is an example of an application embed link:<br>`https://example.okta.com/home/amazon_aws/0oa2hylwrpM8UGehd1t7/272`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idp_tenant`     | A tenant used for Azure AD. Used only with<br>Azure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `client_id`      | A client ID for the Amazon Redshift enterprise<br>application in Azure AD. Used only with Azure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Integrating your application or tool with OAuth using a trusted token issuer
<a name="redshift-iam-access-control-idp-connect-oauth"></a>

 You can add functionality to client tools you create to connect to Redshift by means of the AWS IAM Identity Center connection. If you already configured Redshift integration to AWS IAM Identity Center, use the properties detailed in this section to set up a connection. 

## Authentication plugin for connecting to Redshift using AWS IAM Identity Center
<a name="redshift-iam-access-control-idp-connect-plugin"></a>

You can use AWS IAM Identity Center to connect to Amazon Redshift using the following driver plugins: 
+  `BrowserIdcAuthPlugin` – This plugin facilitates seamless single-sign-on integration with AWS IAM Identity Center. It creates a browser window for users to sign in with the user credentials defined in their corporate identity providers. 
+  `IdpTokenAuthPlugin` – This plugin should be used by applications that want to manage the authentication flow on their own, instead of letting the Amazon Redshift driver open a browser window for AWS IAM Identity Center authentication. It accepts an AWS IAM Identity Center vended Access token or an OpenID Connect (OIDC) JSON web token (JWT) from any web identity provider that’s connected with AWS IAM Identity Center, such as Okta, PingOne, and Microsoft Entra ID (Azure AD). The client application is responsible for generating this required access token/JWT. 

### Authenticating with `BrowserIdcAuthPlugin`
<a name="redshift-iam-access-control-idp-connect-plugin-browseridcauthplugin"></a>

Use the following plugin names to connect using `BrowserIdcAuthPlugin`, depending on your Amazon Redshift driver.


| Driver | Connection option key | Value | Notes | 
| --- | --- | --- | --- | 
| JDBC | `plugin_name` | com.amazon.redshift.plugin.BrowserIdcAuthPlugin | You must enter the fully-qualified class name of the plugin when you connect. | 
| ODBC | `plugin_name` | BrowserIdcAuthPlugin |  | 
| Python | `credentials_provider` | BrowserIdcAuthPlugin | There is no `plugin_name` option available for the Python driver. Instead, use `credentials_provider`. | 

The `BrowserIdcAuthPlugin` plugin has the following additional connection options:


| Option name | Required? | Description | Example | 
| --- | --- | --- | --- | 
| idc\_region | Required | The AWS Region where the AWS IAM Identity Center instance is located. | us-east-1 | 
| issuer\_url | Required | The AWS IAM Identity Center server's instance endpoint. You can find this value using the AWS IAM Identity Center console. | https://identitycenter.amazonaws.com/ssoins-g5j2k70sn4yc5nsc | 
| listen\_port | Optional | The port that the Amazon Redshift driver uses to receive the `auth_code` response from AWS IAM Identity Center through the browser redirect. | 7890 | 
| idc\_client\_display\_name | Optional | The name that the AWS IAM Identity Center client uses for the application in the AWS IAM Identity Center's single sign-on consent popup. | Amazon Redshift driver | 
| idp\_response\_timeout | Optional | The amount of time, in seconds, that the Redshift driver waits for the auth flow to complete. | 60 | 

You must enter these values in the connection properties of the tool you create and connect with. For more information, see the connection options documentation for each respective driver:
+ [Options for JDBC driver version 2.x configuration](jdbc20-configuration-options.md)
+ [ODBC driver options](odbc20-configuration-options.md)
+ [Configuration options for the Amazon Redshift Python connector](python-configuration-options.md)

### Authenticating with `IdpTokenAuthPlugin`
<a name="redshift-iam-access-control-idp-connect-plugin-idptokenauthplugin"></a>

Use the following plugin names to connect using `IdpTokenAuthPlugin`, depending on your Amazon Redshift driver.


| Driver | Connection option key | Value | Notes | 
| --- | --- | --- | --- | 
| JDBC | `plugin_name` | com.amazon.redshift.plugin.IdpTokenAuthPlugin | You must enter the fully-qualified class name of the plugin when you connect. | 
| ODBC | `plugin_name` | IdpTokenAuthPlugin |  | 
| Python | `credentials_provider` | IdpTokenAuthPlugin | There is no `plugin_name` option available for the Python driver. Instead, use `credentials_provider`. | 

The `IdpTokenAuthPlugin` plugin has the following additional connection options:


| Option name | Required? | Description | 
| --- | --- | --- | 
| token | Required | An AWS IAM Identity Center vended access token or an OpenID Connect (OIDC) JSON Web Token (JWT) provided by a web identity provider that's connected with AWS IAM Identity Center. Your application must generate this token by authenticating your application user with AWS IAM Identity Center or an identity provider connected with AWS IAM Identity Center. | 
| token\_type | Required | The type of token used for `IdpTokenAuthPlugin`. Possible values are the following: +   **ACCESS\_TOKEN** – Enter this if you use an AWS IAM Identity Center provided access token.  <br />+   **EXT\_JWT** – Enter this if you use an OpenID Connect (OIDC) JSON Web Token (JWT) provided by a web-based identity provider that's connected with AWS IAM Identity Center.   | 

You must enter these values in the connection properties of the tool you create and connect with. For more information, see the connection options documentation for each respective driver:
+ [Options for JDBC driver version 2.x configuration](jdbc20-configuration-options.md)
+ [ODBC driver options](odbc20-configuration-options.md)
+ [Configuration options for the Amazon Redshift Python connector](python-configuration-options.md)
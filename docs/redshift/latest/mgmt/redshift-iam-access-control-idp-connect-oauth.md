Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Integrating your application or

tool with OAuth using a trusted token issuer

You can add functionality to client tools you create to connect to Redshift by means
of the AWS IAM Identity Center connection. If you already configured Redshift integration to AWS
IAM Identity Center, use the properties detailed in this section to set up a connection.

## Authentication plugin for

connecting to Redshift using AWS IAM Identity Center

You can use AWS IAM Identity Center to connect to Amazon Redshift using the following driver plugins:

- `BrowserIdcAuthPlugin` – This plugin facilitates seamless
  single-sign-on integration with AWS IAM Identity Center. It creates a browser window for users to
  sign in with the user credentials defined in their corporate identity providers.
- `IdpTokenAuthPlugin` – This plugin should be used by applications
  that want to manage the authentication flow on their own, instead of letting the
  Amazon Redshift driver open a browser window for AWS IAM Identity Center authentication. It accepts an
  AWS IAM Identity Center vended Access token or an OpenID Connect (OIDC) JSON web token (JWT) from
  any web identity provider that’s connected with AWS IAM Identity Center, such as Okta, PingOne,
  and Microsoft Entra ID (Azure AD). The client application is responsible for
  generating this required access token/JWT.

### Authenticating with `BrowserIdcAuthPlugin`

Use the following plugin names to connect using `BrowserIdcAuthPlugin`,
depending on your Amazon Redshift driver.

| Driver | Connection option key  | Value                                           | Notes                                                                                                     |
| ------ | ---------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| JDBC   | `plugin_name`          | com.amazon.redshift.plugin.BrowserIdcAuthPlugin | You must enter the fully-qualified class name of the plugin when you<br>connect.                          |
| ODBC   | `plugin_name`          | BrowserIdcAuthPlugin                            |                                                                                                           |
| Python | `credentials_provider` | BrowserIdcAuthPlugin                            | There is no `plugin_name` option available for the Python<br>driver. Instead, use `credentials_provider`. |

The `BrowserIdcAuthPlugin` plugin has the following additional connection
options:

| Option name             | Required? | Description                                                                                                                                        | Example                                                      |
| ----------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| idc_region              | Required  | The AWS Region where the AWS IAM Identity Center instance is<br>located.                                                                           | us-east-1                                                    |
| issuer_url              | Required  | The AWS IAM Identity Center server's instance endpoint. You can find this value<br>using the AWS IAM Identity Center console.                      | https://identitycenter.amazonaws.com/ssoins-g5j2k70sn4yc5nsc |
| listen_port             | Optional  | The port that the Amazon Redshift driver uses to receive the<br>`auth_code` response from AWS IAM Identity Center through the browser<br>redirect. | 7890                                                         |
| idc_client_display_name | Optional  | The name that the AWS IAM Identity Center client uses for the application in the<br>AWS IAM Identity Center's single sign-on consent popup.        | Amazon Redshift driver                                       |
| idp_response_timeout    | Optional  | The amount of time, in seconds, that the Redshift driver waits for<br>the auth flow to complete.                                                   | 60                                                           |

You must enter these values in the connection properties of the tool you create and
connect with. For more information, see the connection options documentation for each
respective driver:

- [Options for JDBC driver version 2.x
  configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md")
- [ODBC driver options](odbc20-configuration-options.md "odbc20-configuration-options.md")
- [Configuration options for the Amazon Redshift
  Python connector](python-configuration-options.md "python-configuration-options.md")

### Authenticating with `IdpTokenAuthPlugin`

Use the following plugin names to connect using `IdpTokenAuthPlugin`,
depending on your Amazon Redshift driver.

| Driver | Connection option key  | Value                                         | Notes                                                                                                     |
| ------ | ---------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| JDBC   | `plugin_name`          | com.amazon.redshift.plugin.IdpTokenAuthPlugin | You must enter the fully-qualified class name of the plugin when you<br>connect.                          |
| ODBC   | `plugin_name`          | IdpTokenAuthPlugin                            |                                                                                                           |
| Python | `credentials_provider` | IdpTokenAuthPlugin                            | There is no `plugin_name` option available for the Python<br>driver. Instead, use `credentials_provider`. |

The `IdpTokenAuthPlugin` plugin has the following additional connection
options:

| Option name | Required? | Description                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| token       | Required  | An AWS IAM Identity Center vended access token or an OpenID Connect (OIDC) JSON<br>Web Token (JWT) provided by a web identity provider that's connected with<br>AWS IAM Identity Center. Your application must generate this token by authenticating your<br>application user with AWS IAM Identity Center or an identity provider connected with AWS<br>IAM Identity Center.   |
| token_type  | Required  | The type of token used for `IdpTokenAuthPlugin`. Possible<br>values are the following:<br>• **ACCESS_TOKEN** – Enter this if you<br>use an AWS IAM Identity Center provided access token.<br>• **EXT_JWT** – Enter this if you use an<br>OpenID Connect (OIDC) JSON Web Token (JWT) provided by a web-based<br>identity provider that's connected with AWS IAM Identity Center. |

You must enter these values in the connection properties of the tool you create and
connect with. For more information, see the connection options documentation for each
respective driver:

- [Options for JDBC driver version 2.x
  configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md")
- [ODBC driver options](odbc20-configuration-options.md "odbc20-configuration-options.md")
- [Configuration options for the Amazon Redshift
  Python connector](python-configuration-options.md "python-configuration-options.md")

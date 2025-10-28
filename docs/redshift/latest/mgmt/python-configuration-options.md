Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuration options for the Amazon Redshift

Python connector

Following, you can find descriptions for the options that you can specify for the
Amazon Redshift Python connector. The options below apply to the latest available connector
version unless specified otherwise.

## access_key_id

- Default value – None
- Data type – String

The access key for the IAM role or user configured for IAM database
authentication.

This parameter is optional.

## allow_db_user_override

- Default value – False
- Data type – Boolean

True

Specifies that the connector uses the `DbUser` value from
the Security Assertion Markup Language (SAML) assertion.

False

Specifies that the value in the `DbUser` connection
parameter is used.

This parameter is optional.

## app_name

- Default value – None
- Data type – String

The name of the identity provider (IdP) application used for authentication.

This parameter is optional.

## application_name

- Default value – None
- Data type – String

The name of the client application to pass to Amazon Redshift for audit purposes.
The application name that you provide appears in the 'application_name'
column of the [SYS_CONNECTION_LOG](../dg/SYS_CONNECTION_LOG.md "../dg/SYS_CONNECTION_LOG.md")
table. This helps track and
troubleshoot connection sources when debugging issues.

This parameter is optional.

## auth_profile

- Default value – None
- Data type – String

The name of an Amazon Redshift authentication profile having connection properties as
JSON. For more information about naming connection parameters, see the
`RedshiftProperty` class. The `RedshiftProperty` class
stores connection parameters provided by the end user and, if applicable, generated
during the IAM authentication process (for example, temporary IAM credentials). For
more information, see the [RedshiftProperty class](https://github.com/aws/amazon-redshift-python-driver/blob/master/redshift_connector/redshift_property.py#L9 "https://github.com/aws/amazon-redshift-python-driver/blob/master/redshift_connector/redshift_property.py#L9").

This parameter is optional.

## auto_create

- Default value – False
- Data type – Boolean

A value that indicates whether to create the user if the user doesn't exist.

This parameter is optional.

## client_id

- Default value – None
- Data type – String

The client ID from Azure IdP.

This parameter is optional.

## client_secret

- Default value – None
- Data type – String

The client secret from Azure IdP.

This parameter is optional.

## cluster_identifier

- Default value – None
- Data type – String

The cluster identifier of the Amazon Redshift cluster.

This parameter is optional.

## credentials_provider

- Default value – None
- Data type – String

The IdP that is used for authenticating with Amazon Redshift. Following are valid values:

- `AdfsCredentialsProvider`
- `AzureCredentialsProvider`
- `BrowserAzureCredentialsProvider`
- `BrowserAzureOAuth2CredentialsProvider`
- `BrowserIdcAuthPlugin` – An authorization plugin using
  AWS IAM Identity Center.
- `BrowserSamlCredentialsProvider`
- `IdpTokenAuthPlugin` – An authorization plugin that
  accepts an AWS IAM Identity Center token or OpenID Connect (OIDC) JSON-based identity
  tokens (JWT) from any web identity provider linked to the AWS
  IAM Identity Center.
- `PingCredentialsProvider`
- `OktaCredentialsProvider`

This parameter is optional.

## database

- Default value – None
- Data type – String

The name of the database to which you want to connect.

This parameter is required.

## database_metadata_current_db_only

- Default value – True
- Data type – Boolean

A value that indicates whether an application supports multidatabase datashare
catalogs. The default value of True indicates that the application doesn't
support multidatabase datashare catalogs for backward compatibility.

This parameter is optional.

## db_groups

- Default value – None
- Data type – String

A comma-separated list of existing database group names that the user indicated by
DbUser joins for the current session.

This parameter is optional.

## db_user

- Default value – None
- Data type – String

The user ID to use with Amazon Redshift.

This parameter is optional.

## endpoint_url

- Default value – None
- Data type – String

The Amazon Redshift endpoint URL. This option is only for AWS internal use.

This parameter is optional.

## group_federation

- Default value – False
- Data type – Boolean

This option specifies whether to use Amazon Redshift IDP groups.

This parameter is optional.

**true**

Use Amazon Redshift Identity Provider (IDP) groups.

**false**

Use STS API and GetClusterCredentials for user federation and specify
**db_groups** for the connection.

## host

- Default value – None
- Data type – String

The hostname of Amazon Redshift cluster.

This parameter is optional.

## iam

- Default value – False
- Data type – Boolean

IAM authentication is enabled.

This parameter is required.

## iam_disable_cache

- Default value – False
- Data type – Boolean

This option specifies whether the IAM credentials are cached. By default, the
IAM credentials are cached. This improves performance when requests to the API
gateway are throttled.

This parameter is optional.

## idc_client_display_name

- Default Value – Amazon Redshift Python
  connector
- Data Type – String

The display name to be used for the client that's using
BrowserIdcAuthPlugin.

This parameter is optional.

## idc_region

- Default Value – None
- Data Type – String

The AWS region where the AWS IAM Identity Center instance is located.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the credentials_provider configuration
option.

## idp_partition

- Default Value – None
- Data Type – String

The partition that your Idp (identity provider) is set up in.
A partition is a group of AWS Regions. For more information
on partitions, see
[partition](../../../glossary/latest/reference/glos-chap.md#partition "../../../glossary/latest/reference/glos-chap.md#partition")
in the _AWS Glossary_.

If this parameter is left blank, Amazon Redshift defaults to the AWS standard
partition, which includes all commercial AWS Regions.
Possible values are as follows:

- `us-gov` ‐ The IdP is set up in the AWS GovCloud (US) Regions.
- `cn` ‐ The IdP is set up in the China Regions.

This parameter is optional.

## idpPort

- Default value – 7890
- Data type – Integer

The listen port to which IdP sends the SAML assertion.

This parameter is required.

## idp_response_timeout

- Default value – 120
- Data type – Integer

The timeout for retrieving SAML assertion from IdP.

This parameter is required.

## idp_tenant

- Default value – None
- Data type – String

The IdP tenant.

This parameter is optional.

## issuer_url

- Default Value – None
- Data Type – String

Points to the AWS IAM Identity Center server's instance endpoint.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the credentials_provider configuration
option.

## listen_port

- Default value – 7890
- Data type – Integer

The port that the driver uses to receive the SAML response from the identity
provider or authorization code when using SAML, Azure AD, or AWS IAM Identity Center services
through a browser plugin.

This parameter is optional.

## login_url

- Default value – None
- Data type – String

The single sign-on Url for the IdP.

This parameter is optional.

## max_prepared_statements

- Default value – 1000
- Data type – Integer

The maximum number of prepared statements that will be cached per connection.
Setting this parameter to 0 disables the caching mechanism. Entering a negative
number for this parameter sets it to the default value.

This parameter is optional.

## numeric_to_float

- Default value – False
- Data type – Boolean

This option specifies if the connector converts numeric data type values from
decimal.Decimal to float. By default, the connector receives numeric data type
values as decimal.Decimal and does not convert them.

We don't recommend enabling numeric_to_float for use cases that require
precision, as results may be rounded.

For more information on decimal.Decimal and the tradeoffs between it and float,
see [decimal —
Decimal fixed point and floating point arithmetic](https://docs.python.org/3/library/decimal.html "https://docs.python.org/3/library/decimal.html") on the Python website.

This parameter is optional.

## partner_sp_id

- Default value – None
- Data type – String

The Partner SP ID used for authentication with Ping.

This parameter is optional.

## password

- Default value – None
- Data type – String

The password to use for authentication.

This parameter is optional.

## port

- Default value – 5439
- Data type – Integer

The port number of the Amazon Redshift cluster.

This parameter is required.

## preferred_role

- Default value – None
- Data type – String

The IAM role preferred for the current connection.

This parameter is optional.

## principal_arn

- Default value – None
- Data type – String

The Amazon Resource Name (ARN) of the user or IAM role for which you are
generating a policy. It's recommended that you attach a policy to a role and then
assign the role to your user, for access.

This parameter is optional.

## profile

- Default value – None
- Data type – String

The name of a profile in an AWS credentials file that contains AWS
credentials.

This parameter is optional.

## provider_name

- Default value – None
- Data type – String

The name of the Redshift Native Authentication Provider.

This parameter is optional.

## region

- Default value – None
- Data type – String

The AWS Region where the cluster is located.

This parameter is optional.

## role_arn

- Default value – None
- Data type – String

The Amazon Resource Name (ARN) of the role that the caller is assuming. This
parameter is used by the provider indicated by `JwtCredentialsProvider`.

For the `JwtCredentialsProvider` provider, this parameter is mandatory.
Otherwise, this parameter is optional.

## role_session_name

- Default value –
  jwt_redshift_session
- Data type – String

An identifier for the assumed role session. Typically, you pass the name or
identifier that is associated with the user who is using your application. The
temporary security credentials that your application uses are associated with that
user. This parameter is used by the provider indicated by
`JwtCredentialsProvider`.

This parameter is optional.

## scope

- Default value – None
- Data type – String

A space-separated list of scopes to which the user can consent. You specify this
parameter so that your application can get consent for APIs that you want to call.
You can specify this parameter when you specify
BrowserAzureOAuth2CredentialsProvider for the credentials_provider option.

This parameter is required for the BrowserAzureOAuth2CredentialsProvider
plug-in.

## secret_access_key_id

- Default value – None
- Data type – String

The secret access key for the IAM role or user configured for IAM database
authentication.

This parameter is optional.

## session_token

- Default value – None
- Data type – String

The access key for the IAM role or user configured for IAM database
authentication. This parameter is required if temporary AWS credentials are being
used.

This parameter is optional.

## serverless_acct_id

- Default value – None
- Data type – String

The Amazon Redshift Serverless account ID.

This parameter is optional.

## serverless_work_group

- Default value – None
- Data type – String

The Amazon Redshift Serverless workgroup name.

This parameter is optional.

## ssl

- Default value – True
- Data type – Boolean

Secure Sockets Layer (SSL) is enabled.

This parameter is required.

## ssl_insecure

- Default value – False
- Data type – Boolean

A value that specifies whether to disable the verification of the
IdP host's server SSL certificate. Setting this parameter to True
will disable the verification of the IdP host's server SSL certificate.
We recommend that you keep the default value of False in production
environments.

This parameter is optional.

## sslmode

- Default value – verify-ca
- Data type – String

The security of the connection to Amazon Redshift. You can specify either of the
following:

- verify-ca
- verify-full

This parameter is required.

## tcp_keepalive

- Default value – True
- Data type – Boolean

Whether to use TCP keepalives to keep connections from timing out. You can specify the following values:

- True: The driver will use TCP keepalives to keep connections from timing out.
- False: The driver won’t use TCP keepalives.

This parameter is optional.

## tcp_keepalive_count

- Default value – None
- Data type – Integer

The number of unacknowledged probes to send before considering
the connection inactive. For example, setting the value to 3 means
that the driver will send 3 unanswered keepalive packets before
determining that the connection is no longer active.

If this parameter is not specified, Amazon Redshift uses the
system's default value.

This parameter is optional.

## tcp_keepalive_interval

- Default value – None
- Data type – Integer

The interval, in seconds, between subsequent keepalive probes
if the driver doesn’t received acknowledgement for the probe
before it. If you specify this parameter, it must be a positive
integer.

If this parameter is not specified, Amazon Redshift
uses the system's default value.

This parameter is optional.

## tcp_keepalive_idle

- Default value – None
- Data type – Integer

The duration of inactivity, in seconds, after which the driver
sends the first keepalive probe. For example, setting the value to
120 means that the driver will wait for 2 minutes of inactivity before
sending the first keepalive packet. If you specify this parameter,
it must be a positive integer.

If this parameter is not specified, Amazon Redshift
uses the system's default value.

This parameter is optional.

## timeout

- Default value – None
- Data type – Integer

The number of seconds before the connection to the server times out.

This parameter is optional.

## token

- Default Value – None
- Data Type – String

An AWS IAM Identity Center provided access token or an OpenID Connect (OIDC) JSON Web Token
(JWT) provided by a web identity provider that's linked with AWS IAM Identity Center. Your
application must generate this token by authenticating the user of your application
with AWS IAM Identity Center or an identity provider linked with AWS IAM Identity Center.

This parameter works with `IdpTokenAuthPlugin`.

## token_type

- Default Value – None
- Data Type – String

The type of token that is being used in `IdpTokenAuthPlugin`.

You can specify the following values:

**ACCESS_TOKEN**

Enter this if you use an AWS IAM Identity Center provided access token.

**EXT_JWT**

Enter this if you use an OpenID Connect (OIDC) JSON Web Token (JWT)
provided by a web-based identity provider that's integrated with AWS
IAM Identity Center.

This parameter works with `IdpTokenAuthPlugin`.

## user

- Default value – None
- Data type – String

The user name to use for authentication.

This parameter is optional.

## web_identity_token

- Default value – None
- Data type – String

The OAuth 2.0 access token or OpenID Connect ID token that is provided by the
identity provider. Make sure that your application gets this token by authenticating
the user who is using your application with a web identity provider. The provider
indicated by `JwtCredentialsProvider` uses this parameter.

For the `JwtCredentialsProvider` provider, this parameter is mandatory.
Otherwise, this parameter is optional.

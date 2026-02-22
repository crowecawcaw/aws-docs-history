Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ODBC driver options

You can use driver configuration options to control the behavior of the Amazon Redshift ODBC
driver. Driver options are not case sensitive.

In Microsoft Windows, you typically set driver options when you configure a data
source name (DSN). You can also set driver options in the connection string when you
connect programmatically, or by adding or changing registry keys in
`HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBC.INI\`your_DSN``.

In Linux, you set driver configuration options in your `odbc.ini` and
`amazon.redshiftodbc.ini` files. Configuration options set in an
`amazon.redshiftodbc.ini` file apply to all connections. In contrast,
configuration options set in an `odbc.ini` file are specific to a connection.
Configuration options set in `odbc.ini` take precedence over configuration
options set in `amazon.redshiftodbc.ini`.

Following are descriptions for the options that you can specify for the Amazon Redshift ODBC
version 2.x driver:

## AccessKeyID

- Default Value – None
- Data Type – String

The IAM access key for the user or role. If you set this parameter, you must also
specify **SecretAccessKey**.

This parameter is optional.

## app_id

- Default Value – None
- Data Type – String

The Okta-provided unique ID associated with your Amazon Redshift application.

This parameter is optional.

## ApplicationName

- Default value – None
- Data type – String

The name of the client application to pass to Amazon Redshift for audit purposes.
The application name that you provide appears in the 'application_name'
column of the [SYS_CONNECTION_LOG](../dg/SYS_CONNECTION_LOG.md "../dg/SYS_CONNECTION_LOG.md")
table. This helps track and
troubleshoot connection sources when debugging issues.

This parameter is optional.

## app_name

- Default Value – None
- Data Type – String

The name of the Okta application that you use to authenticate the connection to
Amazon Redshift.

This parameter is optional.

## AuthProfile

- Default Value – None
- Data Type – String

The authentication profile used to manage the connection settings. If you set this
parameter, you must also set **AccessKeyID** and
**SecretAccessKey**.

This parameter is optional.

## AuthType

- Default Value – Standard
- Data Type – String

This option specifies the authentication mode that the driver uses when you
configure a DSN using the Amazon Redshift ODBC Driver DSN Setup dialog box:

- Standard: Standard authentication using your Amazon Redshift user name and password.
- AWS Profile: IAM authentication using a profile.
- AWS IAM Credentials: IAM authentication using IAM credentials.
- Identity Provider: AD FS: IAM authentication using Active Directory
  Federation Services (AD FS).
- Identity Provider: Auth Plugin: An authorization plugin that accepts an
  AWS IAM Identity Center token or OpenID Connect (OIDC) JSON-based identity tokens (JWT)
  from any web identity provider linked to AWS IAM Identity Center.
- Identity Provider: Azure AD: IAM authentication using an Azure AD
  portal.
- Identity Provider: JWT: IAM authentication using a JSON Web Token
  (JWT).
- Identity Provider: Okta: IAM authentication using Okta.
- Identity Provider: PingFederate: IAM authentication using PingFederate.

This option is available only when you configure a DSN using the Amazon Redshift ODBC
Driver DSN Setup dialog box in the Windows driver. When you configure a connection
using a connection string or a non-Windows machine, the driver automatically
determines whether to use Standard, AWS Profile, or AWS IAM Credentials
authentication based on your specified credentials. To use an identity provider, you
must set the **plugin_name** property.

This parameter is required.

## AutoCreate

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver creates a new user when the specified user
does not exist.

- 1 | TRUE: If the user specified by the **UID** does not
  exist, the driver creates a new user.
- 0 | FALSE: The driver does not create a new user. If the specified user
  does not exist, the authentication fails.

This parameter is optional.

## CaFile

- Default Value – None
- Data Type – String

The file path to the CA certificate file used for some forms of IAM
authentication.

This parameter is only available on Linux.

This parameter is optional.

## client_id

- Default Value – None
- Data Type – String

The client ID associated with your Amazon Redshift application in Azure AD.

This parameter is required if authenticating through the Azure AD service.

## client\_ secret

- Default Value – None
- Data Type – String

The secret key associated with your Amazon Redshift application in Azure AD.

This parameter is required if authenticating through the Azure AD service.

## ClusterId

- Default Value – None
- Data Type – String

The name of the Amazon Redshift cluster you want to connect to. It is used in IAM
authentication. The Cluster ID is not specified in the **Server**
parameter.

This parameter is optional.

## compression

- Default Value – off
- Data Type – String

The compression method used for wire protocol communication between the Amazon Redshift
server and the client or driver.

You can specify the following values:

- lz4: Sets the compression method used for wire protocol communication with
  Amazon Redshift to `lz4`.
- zstd: Sets the compression method used for wire protocol communication
  with Amazon Redshift to `zstd`.
- off: Doesn't use compression for wire protocol communication with
  Amazon Redshift.

This parameter is optional.

## Database

- Default Value – None
- Data Type – String

The name of the Amazon Redshift database that you want to access.

This parameter is required.

## DatabaseMetadataCurrentDbOnly

- Default Value – 1
- Data Type – Boolean

A boolean specifying whether the driver returns metadata from multiple databases
and clusters.

- 1 | TRUE: The driver only returns metadata from the current database.
- 0 | FALSE. The driver returns metadata across multiple Amazon Redshift databases
  and clusters.

This parameter is optional.

## dbgroups_filter

- Default Value – None
- Data Type – String

The regular expression you can specify to filter out DbGroups that are received
from the SAML response to Amazon Redshift when using Azure, Browser Azure, and Browser SAML
authentication types.

This parameter is optional.

## Driver

- Default Value – Amazon Redshift ODBC
  Driver (x64)
- Data Type – String

The name of the driver. The only supported value is **Amazon Redshift ODBC
Driver (x64)**.

This parameter is required if you do not set **DSN**.

## DSN

- Default Value – None
- Data Type – String

The name of the driver data source name. The application specifies the DSN in the
SQLDriverConnect API.

This parameter is required if you do not set **Driver.**.

## EndpointUrl

- Default Value – None
- Data Type – String

The overriding endpoint used to communicate with the Amazon Redshift Coral Service for
IAM authentication.

This parameter is optional.

## ForceLowercase

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver lowercases all DbGroups sent from the
identity provider to Amazon Redshift when using single sign-on authentication.

- 1 | TRUE: The driver lowercases all DbGroups that are sent from the
  identity provider.
- 0 | FALSE: The driver does not alter DbGroups.

This parameter is optional.

## group_federation

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the `getClusterCredentialsWithIAM` API is
used for obtaining temporary cluster credentials in provisioned clusters. This
option lets IAM users integrate with Redshift database roles in provisioned
clusters. Note that this option does not apply to Redshift Serverless namespaces.

- 1 | TRUE: The driver uses the `getClusterCredentialsWithIAM`
  API for obtaining temporary cluster credentials in provisioned clusters.
- 0 | FALSE: The driver uses the default `getClusterCredentials`
  API for obtaining temporary cluster credentials in provisioned clusters.

This parameter is optional.

## https_proxy_host

- Default Value – None
- Data Type – String

The host name or IP address of the proxy server through which you want to pass
IAM authentication processes.

This parameter is optional.

## https_proxy_password

- Default Value – None
- Data Type – String

The password that you use to access the proxy server. It’s used for IAM
authentication.

This parameter is optional.

## https_proxy_port

- Default Value – None
- Data Type – Integer

The number of the port that the proxy server uses to listen for client
connections. It’s used for IAM authentication.

This parameter is optional.

## https_proxy_username

- Default Value – None
- Data Type – String

The user name that you use to access the proxy server. It's used for IAM
authentication.

This parameter is optional.

## IAM

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver uses an IAM authentication method to
authenticate the connection.

- 1 | TRUE: The driver uses one of the IAM authentication methods (using
  an access key and secret key pair, or a profile, or a credentials service).
- 0 | FALSE. The driver uses standard authentication (using your database
  user name and password).

This parameter is optional.

## idc_client_display_name

- Default Value – Amazon Redshift ODBC
  driver
- Data Type – String

The display name to be used for the client that's using
BrowserIdcAuthPlugin.

This parameter is optional.

## idc_region

- Default Value – None
- Data Type – String

The AWS region where the AWS IAM Identity Center instance is located.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the plugin_name configuration
option.

## idp_host

- Default Value – None
- Data Type – String

The IdP (identity provider) host you are using to authenticate into
Amazon Redshift.

This parameter is optional.

## idp_port

- Default Value – None
- Data Type – Integer

The port for an IdP (identity provider) you are using to authenticate into
Amazon Redshift. Depending on the port you selected when creating, modifying or migrating
the cluster, allow access to the selected port.

This parameter is optional.

## idp_response_timeout

- Default Value – 120
- Data Type – Integer

The number of seconds that the driver waits for the SAML response from the
identity provider when using SAML or Azure AD services through a browser plugin.

This parameter is optional.

## idp_tenant

- Default Value – None
- Data Type – String

The Azure AD tenant ID associated with your Amazon Redshift application.

This parameter is required if authenticating through the Azure AD service.

## idp_partition

- Default Value – None
- Data Type – String

Specifies the cloud partition where your identity provider (IdP) is configured. This determines which IdP authentication endpoint the driver connects to.

If this parameter is left blank, the driver defaults to the commercial partition. Possible values are:

- `us-gov`: Use this value if your IdP is configured in Azure Government. For example, Azure AD Government uses the endpoint `login.microsoftonline.us`.
- `cn`: Use this value if your IdP is configured in the China cloud partition. For example, Azure AD China uses the endpoint `login.chinacloudapi.cn`.

This parameter is optional.

## idp_use_https_proxy

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver passes the authentication processes for
identity providers (IdP) through a proxy server.

- 1 | TRUE: The driver passes IdP authentication processes through a proxy
  server.
- 0 | FALSE. The driver does not pass IdP authentication processes through
  a proxy server.

This parameter is optional.

## InstanceProfile

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver uses the Amazon EC2 instance profile, when
configured to use a profile for authentication.

- 1 | TRUE: The driver uses the Amazon EC2 instance profile.
- 0 | FALSE. The driver uses the chained roles profile specified by the
  Profile Name option (**Profile**) instead.

This parameter is optional.

## issuer_url

- Default Value – None
- Data Type – String

Points to the AWS IAM Identity Center server's instance endpoint.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the plugin_name configuration
option.

## KeepAlive

- Default Value – 1
- Data Type – Boolean

A boolean specifying whether the driver uses TCP keepalives to prevent connections
from timing out.

- 1 | TRUE: The driver uses TCP keepalives to prevent connections from
  timing out.
- 0 | FALSE. The driver does not use TCP keepalives.

This parameter is optional.

## KeepAliveCount

- Default Value – 0
- Data Type – Integer

The number of TCP keepalive packets that can be lost before the connection is
considered broken. When this parameter is set to 0, the driver uses the system
default for this setting.

This parameter is optional.

## KeepAliveInterval

- Default Value – 0
- Data Type – Integer

The number of seconds between each TCP keepalive retransmission. When this
parameter is set to 0, the driver uses the system default for this setting.

This parameter is optional.

## KeepAliveTime

- Default Value – 0
- Data Type – Integer

The number of seconds of inactivity before the driver sends a TCP keepalive
packet. When this parameter is set to 0, the driver uses the system default for this
setting.

This parameter is optional.

## listen_port

- Default Value – 7890
- Data Type – Integer

The port that the driver uses to receive the SAML response from the identity
provider or authorization code when using SAML, Azure AD, or AWS IAM Identity Center services
through a browser plugin.

This parameter is optional.

## login_url

- Default Value – None
- Data Type – String

The URL for the resource on the identity provider's website when using the generic
Browser SAML plugin.

This parameter is required if authenticating with the SAML or Azure AD services
through a browser plugin.

## loginToRp

- Default Value –
  urn:amazon:webservices
- Data Type – String

The relying party trust that you want to use for the AD FS authentication
type.

This string is optional.

## LogLevel

- Default Value – 0
- Data Type – Integer

Use this property to enable or disable logging in the driver and to specify the
amount of detail included in log. files. We recommend you only enable logging long
enough to capture an issue, as logging decreases performance and can consume a large
quantity of disk space.

Set the property to one of the following values:

- 0: OFF. Disable all logging.
- 1: ERROR. Logs error events that might allow the driver to continue
  running but produce an error.
- 2: API_CALL. Logs ODBC API function calls with function argument values.
- 3: INFO. Logs general information that describes the progress of the
  driver.
- 4: MSG_PROTOCOL. Logs detailed information of the driver's message
  procotol.
- 5: DEBUG. Logs all driver activity
- 6: DEBUG_APPEND. Keep appending logs for all driver activities.

When logging is enabled, the driver produces the following log files at the
location you specify in the **LogPath** property:

- A `redshift_odbc.log.1` file that logs driver activity that
  takes place during handshake of a connection.
- A `redshift_odbc.log` file for all driver activities after a
  connection is made to the database.

This parameter is optional.

## LogPath

- Default Value – The OS-specific TEMP
  directory
- Data Type – String

The full path to the folder where the driver saves log files when
**LogLevel** is higher than 0.

This parameter is optional.

## Min_TLS

- Default Value – 1.2
- Data Type – String

The minimum version of TLS/SSL that the driver allows the data store to use for
encrypting connections. For example, if TLS 1.2 is specified, TLS 1.1 cannot be used
to encrypt connections.

Min_TLS accepts the following values:

- 1.0: The connection must use at least TLS 1.0.
- 1.1: The connection must use at least TLS 1.1.
- 1.2: The connection must use at least TLS 1.2.

This parameter is optional.

## partner_spid

- Default Value – None
- Data Type – String

The partner SPID (service provider ID) value to use when authenticating the
connection using the PingFederate service.

This parameter is optional.

## Password | PWS

- Default Value – None
- Data Type – String

The password corresponding to the database user name that you provided in the User
field (**UID** | **User** |
**LogonID**).

This parameter is optional.

## plugin_name

- Default Value – None
- Data Type – String

The credentials provider plugin name that you want to use for authentication.

The following values are supported:

- `ADFS`: Use Active Directory Federation Services for
  authentication.
- `AzureAD`: Use Microsoft Azure Active Directory (AD) Service for
  authentication.
- `BrowserAzureAD`: Use a browser plugin for the Microsoft Azure
  Active Directory (AD) Service for authentication.
- `BrowserIdcAuthPlugin` : An authorization plugin using AWS
  IAM Identity Center.
- `BrowserSAML`: Use a browser plugin for SAML services such as
  Okta or Ping for authentication.
- `IdpTokenAuthPlugin`: An authorization plugin that accepts an
  AWS IAM Identity Center token or OpenID Connect (OIDC) JSON-based identity tokens (JWT)
  from any web identity provider linked to AWS IAM Identity Center.
- `JWT`: Use a JSON Web Token (JWT) for authentication.
- `Ping`: Use the PingFederate service for authentication.
- `Okta`: Use the Okta service for authentication.

This parameter is optional.

## Port | PortNumber

- Default Value – 5439
- Data Type – Integer

The number of the TCP port that the Amazon Redshift server uses to listen for client
connections.

This parameter is optional.

## preferred_role

- Default Value – None
- Data Type – String

The role you want to assume during the connection to Amazon Redshift. It’s used for IAM
authentication.

This parameter is optional.

## Profile

- Default Value – None
- Data Type – String

The name of the user AWS profile used to authenticate into Amazon Redshift.

- If the Use Instance Profile parameter (the
  **InstanceProfile** property) is set to 1 | TRUE, that
  setting takes precedence and the driver uses the Amazon EC2 instance profile
  instead.
- The default location for the credentials file that contains profiles is
  `~/.aws/Credentials`. The
  `AWS_SHARED_CREDENTIALS_FILE` environment variable can be
  used to point to a different credentials file.

This parameter is optional.

## provider_name

- Default Value – None
- Data Type – String

The authentication provider created by the user using the CREATE IDENTITY PROVIDER
query. It’s used in native Amazon Redshift authentication.

This parameter is optional.

## ProxyHost

- Default Value – None
- Data Type – String

The host name or IP address of the proxy server that you want to connect
through.

This parameter is optional.

## ProxyPort

- Default Value – None
- Data Type – Integer

The number of the port that the proxy server uses to listen for client
connections.

This parameter is optional.

## ProxyPwd

- Default ValPrevious ODBC driver versionsue – None
- Data Type – String

The password that you use to access the proxy server.

This parameter is optional.

## ProxyUid

- Default Value – None
- Data Type – String

The user name that you use to access the proxy server.

This parameter is optional.

## ReadOnly

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver is in read-only mode.

- 1 | TRUE: The connection is in read-only mode, and cannot write to the
  data store.
- 0 | FALSE: The connection is not in read-only mode, and can write to the
  data store.

This parameter is optional.

## region

- Default Value – None
- Data Type – String

The AWS region that your cluster is in.

This parameter is optional.

## SecretAccessKey

- Default Value – None
- Data Type – String

The IAM secret key for the user or role. If you set this parameter, you must
also set **AccessKeyID**.

This parameter is optional.

## SessionToken

- Default Value – None
- Data Type – String

The temporary IAM session token associated with the IAM role that you are
using to authenticate.

This parameter is optional.

## Server | HostName | Host

- Default Value – None
- Data Type – String

The endpoint server to connect to.

This parameter is required.

## ssl_insecure

- Default Value – 0
- Data Type – Boolean

A boolean specifying whether the driver checks the authenticity of the IdP server
certificate.

- 1 | TRUE: The driver does not check the authenticity of the IdP server
  certificate.
- 0 | FALSE: The driver checks the authenticity of the IdP server
  certificate

This parameter is optional.

## SSLMode

- Default Value –
  `verify-ca`
- Data Type – String

The SSL certificate verification mode to use when connecting to Amazon Redshift. The
following values are possible:

- `verify-full`: Connect only using SSL, a trusted certificate
  authority, and a server name that matches the certificate.
- `verify-ca`: Connect only using SSL and a trusted certificate
  authority.
- `require`: Connect only using SSL.
- `prefer`: Connect using SSL if available. Otherwise, connect
  without using SSL.
- `allow`: By default, connect without using SSL. If the server
  requires SSL connections, then use SSL.
- `disable`: Connect without using SSL.

This parameter is optional.

## StsConnectionTimeout

- Default Value – 0
- Data Type – Integer

The maximum wait time for IAM connections, in seconds. If set to 0 or not
specified, the driver waits 60 seconds for each AWS STS call.

This parameter is optional.

## StsEndpointUrl

- Default Value – None
- Data Type – String

This option specifies the overriding endpoint used to communicate with the
AWS Security Token Service (AWS STS).

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

## UID | User | LogonID

- Default Value – None
- Data Type – String

The user name that you use to access the Amazon Redshift server.

This parameter is required if you use database authentication.

## web_identity_token

- Default Value – None
- Data Type – String

The OAUTH token that is provided by the identity provider. It’s used in the JWT
plugin.

This parameter is required if you set the **plugin_name**
parameter to BasicJwtCredentialsProvider.

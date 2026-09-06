

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configuration options for the Amazon Redshift Python connector
<a name="python-configuration-options"></a>

Following, you can find descriptions for the options that you can specify for the Amazon Redshift Python connector. The options below apply to the latest available connector version unless specified otherwise.

## access\_key\_id
<a name="python-access-key-id-option"></a>
+ **Default value** – None
+ **Data type** – String

The access key for the IAM role or user configured for IAM database authentication. 

This parameter is optional.

## allow\_db\_user\_override
<a name="python-allow-db-user-override-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

True  
Specifies that the connector uses the `DbUser` value from the Security Assertion Markup Language (SAML) assertion.

False  
Specifies that the value in the `DbUser` connection parameter is used.

This parameter is optional.

## app\_name
<a name="python-app-name-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of the identity provider (IdP) application used for authentication. 

This parameter is optional.

## application\_name
<a name="python-application_name-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of the client application to pass to Amazon Redshift for audit purposes. The application name that you provide appears in the 'application\_name' column of the [SYS\_CONNECTION\_LOG](https://docs.aws.amazon.com/redshift/latest/dg/SYS_CONNECTION_LOG.html) table. This helps track and troubleshoot connection sources when debugging issues.

This parameter is optional.

## auth\_profile
<a name="python-auth-profile-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of an Amazon Redshift authentication profile having connection properties as JSON. For more information about naming connection parameters, see the `RedshiftProperty` class. The `RedshiftProperty` class stores connection parameters provided by the end user and, if applicable, generated during the IAM authentication process (for example, temporary IAM credentials). For more information, see the [RedshiftProperty class](https://github.com/aws/amazon-redshift-python-driver/blob/master/redshift_connector/redshift_property.py#L9). 

This parameter is optional.

## auto\_create
<a name="python-auto-create-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

A value that indicates whether to create the user if the user doesn't exist. 

This parameter is optional.

## client\_id
<a name="python-client-id-option"></a>
+ **Default value** – None
+ **Data type** – String

The client ID from Azure IdP. 

This parameter is optional.

## client\_secret
<a name="python-client-secret-option"></a>
+ **Default value** – None
+ **Data type** – String

The client secret from Azure IdP. 

This parameter is optional.

## cluster\_identifier
<a name="python-cluster-identifier-option"></a>
+ **Default value** – None
+ **Data type** – String

The cluster identifier of the Amazon Redshift cluster. 

This parameter is optional.

## credentials\_provider
<a name="python-credential-provider-option"></a>
+ **Default value** – None
+ **Data type** – String

The IdP that is used for authenticating with Amazon Redshift. Following are valid values: 
+ `AdfsCredentialsProvider`
+ `AzureCredentialsProvider`
+ `BrowserAzureCredentialsProvider`
+ `BrowserAzureOAuth2CredentialsProvider`
+ `BrowserIdcAuthPlugin` – An authorization plugin using AWS IAM Identity Center.
+ `BrowserSamlCredentialsProvider`
+ `IdpTokenAuthPlugin` – An authorization plugin that accepts an AWS IAM Identity Center token or OpenID Connect (OIDC) JSON-based identity tokens (JWT) from any web identity provider linked to the AWS IAM Identity Center.
+ `PingCredentialsProvider`
+ `OktaCredentialsProvider`

This parameter is optional.

## database
<a name="python-database-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of the database to which you want to connect. 

This parameter is required.

## database\_metadata\_current\_db\_only
<a name="python-database-metadata-current-db-only-option"></a>
+ **Default value** – True
+ **Data type** – Boolean

A value that indicates whether an application supports multidatabase datashare catalogs. The default value of True indicates that the application doesn't support multidatabase datashare catalogs for backward compatibility. 

This parameter is optional.

## db\_groups
<a name="python-db-groups-option"></a>
+ **Default value** – None
+ **Data type** – String

A comma-separated list of existing database group names that the user indicated by DbUser joins for the current session. 

This parameter is optional.

## db\_user
<a name="python-db-user-option"></a>
+ **Default value** – None
+ **Data type** – String

The user ID to use with Amazon Redshift. 

This parameter is optional.

## enable\_table\_types
<a name="python-enable-table-types-option"></a>
+ **Default value** – True
+ **Data type** – Boolean

Specifies whether the connector recognizes detailed table type information from the data source in the results of the `get_tables` and `get_table_types` metadata methods. By default, the connector recognizes detailed table types.
+ True: The connector recognizes the following table types: TABLE, VIEW, SYSTEM TABLE, SYSTEM VIEW, EXTERNAL TABLE, and LOCAL TEMPORARY.
+ False: The connector normalizes the detailed table type information into the generic TABLE and VIEW table types.

This parameter is optional. It is available in connector versions 2.1.16 and later.

## endpoint\_url
<a name="python-endpoint-url-option"></a>
+ **Default value** – None
+ **Data type** – String

The Amazon Redshift endpoint URL. This option is only for AWS internal use. 

This parameter is optional.

## group\_federation
<a name="python-group-federation-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

This option specifies whether to use Amazon Redshift IDP groups.

This parameter is optional.

**true**  
Use Amazon Redshift Identity Provider (IDP) groups.

**false**  
Use STS API and GetClusterCredentials for user federation and specify **db\_groups** for the connection.

## host
<a name="python-host-option"></a>
+ **Default value** – None
+ **Data type** – String

The hostname of Amazon Redshift cluster. 

This parameter is optional.

## iam
<a name="python-iam-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

IAM authentication is enabled. 

This parameter is required.

## iam\_disable\_cache
<a name="python-iam-disable-cache-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

This option specifies whether the IAM credentials are cached. By default, the IAM credentials are cached. This improves performance when requests to the API gateway are throttled. 

This parameter is optional.

## idc\_client\_display\_name
<a name="python-idc_client_display_name-option"></a>
+ **Default Value** – Amazon Redshift Python connector
+ **Data Type** – String

The display name to be used for the client that's using BrowserIdcAuthPlugin.

This parameter is optional.

## idc\_region
<a name="python-idc_region"></a>
+ **Default Value** – None
+ **Data Type** – String

The AWS region where the AWS IAM Identity Center instance is located.

This parameter is required only when authenticating using `BrowserIdcAuthPlugin` in the credentials\_provider configuration option.

## idp\_partition
<a name="python-idp_partition-option"></a>
+ **Default Value** – None
+ **Data Type** – String

Specifies the cloud partition where your identity provider (IdP) is configured. This determines which IdP authentication endpoint the driver connects to.

If this parameter is left blank, the driver defaults to the commercial partition. Possible values are:
+  `us-gov`: Use this value if your IdP is configured in Azure Government. For example, Azure AD Government uses the endpoint `login.microsoftonline.us`.
+  `cn`: Use this value if your IdP is configured in the China cloud partition. For example, Azure AD China uses the endpoint `login.chinacloudapi.cn`. 

This parameter is optional.

## idpPort
<a name="python-idp-port-option"></a>
+ **Default value** – 7890
+ **Data type** – Integer

The listen port to which IdP sends the SAML assertion. 

This parameter is required.

## idp\_response\_timeout
<a name="python-idp-response-timeout-option"></a>
+ **Default value** – 120
+ **Data type** – Integer

The timeout for retrieving SAML assertion from IdP. 

This parameter is required.

## idp\_tenant
<a name="python-idp-tenant-option"></a>
+ **Default value** – None
+ **Data type** – String

The IdP tenant. 

This parameter is optional.

## issuer\_url
<a name="python-issuer_url"></a>
+ **Default Value** – None
+ **Data Type** – String

 Points to the AWS IAM Identity Center server's instance endpoint. 

This parameter is required only when authenticating using `BrowserIdcAuthPlugin` in the credentials\_provider configuration option.

## listen\_port
<a name="python-listen-port-option"></a>
+ **Default value** – 7890
+ **Data type** – Integer

The port that the driver uses to receive the SAML response from the identity provider or authorization code when using SAML, Azure AD, or AWS IAM Identity Center services through a browser plugin.

This parameter is optional.

## login\_url
<a name="python-login-url-option"></a>
+ **Default value** – None
+ **Data type** – String

The single sign-on Url for the IdP. 

This parameter is optional.

## max\_prepared\_statements
<a name="python-max-prepared-statements-option"></a>
+ **Default value** – 1000
+ **Data type** – Integer

The maximum number of prepared statements that will be cached per connection. Setting this parameter to 0 disables the caching mechanism. Entering a negative number for this parameter sets it to the default value. 

This parameter is optional.

## numeric\_to\_float
<a name="python-numeric-to-float-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

This option specifies if the connector converts numeric data type values from decimal.Decimal to float. By default, the connector receives numeric data type values as decimal.Decimal and does not convert them. 

We don't recommend enabling numeric\_to\_float for use cases that require precision, as results may be rounded. 

For more information on decimal.Decimal and the tradeoffs between it and float, see [decimal — Decimal fixed point and floating point arithmetic](https://docs.python.org/3/library/decimal.html) on the Python website. 

This parameter is optional.

## partner\_sp\_id
<a name="python-partner-sp-id-option"></a>
+ **Default value** – None
+ **Data type** – String

The Partner SP ID used for authentication with Ping. 

This parameter is optional.

## password
<a name="python-password-option"></a>
+ **Default value** – None
+ **Data type** – String

The password to use for authentication. 

This parameter is optional.

## port
<a name="python-port-option"></a>
+ **Default value** – 5439
+ **Data type** – Integer

The port number of the Amazon Redshift cluster. 

This parameter is required.

## preferred\_role
<a name="python-preferred-role-option"></a>
+ **Default value** – None
+ **Data type** – String

The IAM role preferred for the current connection. 

This parameter is optional.

## principal\_arn
<a name="python-principal-arn-option"></a>
+ **Default value** – None
+ **Data type** – String

The Amazon Resource Name (ARN) of the user or IAM role for which you are generating a policy. It's recommended that you attach a policy to a role and then assign the role to your user, for access. 

This parameter is optional.

## profile
<a name="python-profile-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of a profile in an AWS credentials file that contains AWS credentials. 

This parameter is optional.

## provider\_name
<a name="python-provider_name-option"></a>
+ **Default value** – None
+ **Data type** – String

The name of the Redshift Native Authentication Provider. 

This parameter is optional.

## region
<a name="python-region-option"></a>
+ **Default value** – None
+ **Data type** – String

The AWS Region where the cluster is located. 

This parameter is optional.

## role\_arn
<a name="python-role-arn-option"></a>
+ **Default value** – None
+ **Data type** – String

The Amazon Resource Name (ARN) of the role that the caller is assuming. This parameter is used by the provider indicated by `JwtCredentialsProvider`. 

For the `JwtCredentialsProvider` provider, this parameter is mandatory. Otherwise, this parameter is optional.

## role\_session\_name
<a name="python-role-session-name-option"></a>
+ **Default value** – jwt\_redshift\_session
+ **Data type** – String

An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. The temporary security credentials that your application uses are associated with that user. This parameter is used by the provider indicated by `JwtCredentialsProvider`. 

This parameter is optional.

## scope
<a name="python-scope-option"></a>
+ **Default value** – None
+ **Data type** – String

A space-separated list of scopes to which the user can consent. You specify this parameter so that your application can get consent for APIs that you want to call. You can specify this parameter when you specify BrowserAzureOAuth2CredentialsProvider for the credentials\_provider option.

This parameter is required for the BrowserAzureOAuth2CredentialsProvider plug-in.

## secret\_access\_key\_id
<a name="python-secret-access-key-id-option"></a>
+ **Default value** – None
+ **Data type** – String

The secret access key for the IAM role or user configured for IAM database authentication. 

This parameter is optional.

## session\_token
<a name="python-session-token-option"></a>
+ **Default value** – None
+ **Data type** – String

The access key for the IAM role or user configured for IAM database authentication. This parameter is required if temporary AWS credentials are being used. 

This parameter is optional.

## serverless\_acct\_id
<a name="python-serverless-acct-id-option"></a>
+ **Default value** – None
+ **Data type** – String

The Amazon Redshift Serverless account ID.

This parameter is optional.

## serverless\_work\_group
<a name="python-serverless-work-group-option"></a>
+ **Default value** – None
+ **Data type** – String

The Amazon Redshift Serverless workgroup name.

This parameter is optional.

## ssl
<a name="python-ssl-option"></a>
+ **Default value** – True
+ **Data type** – Boolean

Secure Sockets Layer (SSL) is enabled. 

This parameter is required.

## ssl\_insecure
<a name="python-ssl-insecure-option"></a>
+ **Default value** – False
+ **Data type** – Boolean

A value that specifies whether to disable the verification of the IdP host's server SSL certificate. Setting this parameter to True will disable the verification of the IdP host's server SSL certificate. We recommend that you keep the default value of False in production environments.

This parameter is optional.

## sslmode
<a name="python-sslmode-option"></a>
+ **Default value** – verify-ca
+ **Data type** – String

The security of the connection to Amazon Redshift. You can specify either of the following: 
+ verify-ca
+ verify-full

This parameter is required.

## tcp\_keepalive
<a name="python-tcp_keepalive-option"></a>
+ **Default value** – True
+ **Data type** – Boolean

Whether to use TCP keepalives to keep connections from timing out. You can specify the following values:
+ True: The driver will use TCP keepalives to keep connections from timing out.
+ False: The driver won’t use TCP keepalives.

This parameter is optional.

## tcp\_keepalive\_count
<a name="python-tcp_keepalive_count-option"></a>
+ **Default value** – None
+ **Data type** – Integer

The number of unacknowledged probes to send before considering the connection inactive. For example, setting the value to 3 means that the driver will send 3 unanswered keepalive packets before determining that the connection is no longer active.

If this parameter is not specified, Amazon Redshift uses the system's default value.

This parameter is optional.

## tcp\_keepalive\_interval
<a name="python-tcp_keepalive_interval-option"></a>
+ **Default value** – None
+ **Data type** – Integer

The interval, in seconds, between subsequent keepalive probes if the driver doesn’t received acknowledgement for the probe before it. If you specify this parameter, it must be a positive integer.

If this parameter is not specified, Amazon Redshift uses the system's default value.

This parameter is optional.

## tcp\_keepalive\_idle
<a name="python-tcp_keepalive_idle-option"></a>
+ **Default value** – None
+ **Data type** – Integer

The duration of inactivity, in seconds, after which the driver sends the first keepalive probe. For example, setting the value to 120 means that the driver will wait for 2 minutes of inactivity before sending the first keepalive packet. If you specify this parameter, it must be a positive integer. 

If this parameter is not specified, Amazon Redshift uses the system's default value.

This parameter is optional.

## timeout
<a name="python-timeout-option"></a>
+ **Default value** – None
+ **Data type** – Integer

The number of seconds before the connection to the server times out. 

This parameter is optional.

## token
<a name="python-token-option"></a>
+ **Default Value** – None
+ **Data Type** – String

An AWS IAM Identity Center provided access token or an OpenID Connect (OIDC) JSON Web Token (JWT) provided by a web identity provider that's linked with AWS IAM Identity Center. Your application must generate this token by authenticating the user of your application with AWS IAM Identity Center or an identity provider linked with AWS IAM Identity Center. 

This parameter works with `IdpTokenAuthPlugin`.

## token\_type
<a name="python-token_type-option"></a>
+ **Default Value** – None
+ **Data Type** – String

The type of token that is being used in `IdpTokenAuthPlugin`.

You can specify the following values:

**ACCESS\_TOKEN**  
Enter this if you use an AWS IAM Identity Center provided access token.

**EXT\_JWT**  
Enter this if you use an OpenID Connect (OIDC) JSON Web Token (JWT) provided by a web-based identity provider that's integrated with AWS IAM Identity Center.

This parameter works with `IdpTokenAuthPlugin`.

## user
<a name="python-user-option"></a>
+ **Default value** – None
+ **Data type** – String

The user name to use for authentication. 

This parameter is optional.

## web\_identity\_token
<a name="python-web-identity-token-option"></a>
+ **Default value** – None
+ **Data type** – String

The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Make sure that your application gets this token by authenticating the user who is using your application with a web identity provider. The provider indicated by `JwtCredentialsProvider` uses this parameter. 

For the `JwtCredentialsProvider` provider, this parameter is mandatory. Otherwise, this parameter is optional.
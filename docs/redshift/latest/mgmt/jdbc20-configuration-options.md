Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Options for JDBC driver version 2.x

configuration

Following, you can find descriptions for the options that you can specify for version
2.2 of the Amazon Redshift JDBC driver. Configuration options are not case sensitive.

You can set configuration properties using the connection URL. For more information,
see [Building the connection URL](jdbc20-build-connection-url.md "jdbc20-build-connection-url.md").

###### Topics

- [AccessKeyID](#jdbc20-accesskeyid-option "#jdbc20-accesskeyid-option")
- [AllowDBUserOverride](#jdbc20-allowdbuseroverride-option "#jdbc20-allowdbuseroverride-option")
- [App_ID](#jdbc20-app-id-option "#jdbc20-app-id-option")
- [App_Name](#jdbc20-app-name-option "#jdbc20-app-name-option")
- [ApplicationName](#jdbc20-applicationname-option "#jdbc20-applicationname-option")
- [AuthProfile](#jdbc20-authprofile-option "#jdbc20-authprofile-option")
- [AutoCreate](#jdbc20-autocreate-option "#jdbc20-autocreate-option")
- [Client_ID](#jdbc20-client_id-option "#jdbc20-client_id-option")
- [Client_Secret](#jdbc20-client_secret-option "#jdbc20-client_secret-option")
- [ClusterID](#jdbc20-clusterid-option "#jdbc20-clusterid-option")
- [Compression](#jdbc20-compression-option "#jdbc20-compression-option")
- [connectTimeout](#jdbc20-connecttimeout-option "#jdbc20-connecttimeout-option")
- [connectionTimezone](#jdbc20-connecttimezone-option "#jdbc20-connecttimezone-option")
- [databaseMetadataCurrentDbOnly](#jdbc20-databasemetadatacurrentdbonly-option "#jdbc20-databasemetadatacurrentdbonly-option")
- [DbUser](#jdbc20-dbuser-option "#jdbc20-dbuser-option")
- [DbGroups](#jdbc20-dbgroups-option "#jdbc20-dbgroups-option")
- [DBNAME](#jdbc20-dbname-option "#jdbc20-dbname-option")
- [defaultRowFetchSize](#jdbc20-defaultrowfetchsize-option "#jdbc20-defaultrowfetchsize-option")
- [DisableIsValidQuery](#jdbc20-disableisvalidquery-option "#jdbc20-disableisvalidquery-option")
- [enableFetchRingBuffer](#jdbc20-enablefetchringbuffer-option "#jdbc20-enablefetchringbuffer-option")
- [enableMultiSqlSupport](#jdbc20-enablemultisqlsupport-option "#jdbc20-enablemultisqlsupport-option")
- [fetchRingBufferSize](#jdbc20-fetchringbuffersize-option "#jdbc20-fetchringbuffersize-option")
- [ForceLowercase](#jdbc20-forcelowercase-option "#jdbc20-forcelowercase-option")
- [groupFederation](#jdbc20-groupFederation-option "#jdbc20-groupFederation-option")
- [HOST](#jdbc20-host-option "#jdbc20-host-option")
- [IAMDisableCache](#jdbc20-iamdisablecache-option "#jdbc20-iamdisablecache-option")
- [IAMDuration](#jdbc20-iamduration-option "#jdbc20-iamduration-option")
- [Idc_Client_Display_Name](#jdbc20-idc_client_display_name "#jdbc20-idc_client_display_name")
- [Idc_Region](#jdbc20-idc_region "#jdbc20-idc_region")
- [IdP_Host](#jdbc20-idp_host-option "#jdbc20-idp_host-option")
- [IdP_Partition](#jdbc20-idp_partition-option "#jdbc20-idp_partition-option")
- [IdP_Port](#jdbc20-idp_port-option "#jdbc20-idp_port-option")
- [IdP_Tenant](#jdbc20-idp_tenant-option "#jdbc20-idp_tenant-option")
- [IdP_Response_Timeout](#jdbc20-idp_response_timeout-option "#jdbc20-idp_response_timeout-option")
- [IniFile](#jdbc20-inifile-option "#jdbc20-inifile-option")
- [IniSection](#jdbc20-inisection-option "#jdbc20-inisection-option")
- [isServerless](#jdbc20-isserverless-option "#jdbc20-isserverless-option")
- [Issuer_Url](#jdbc20-issuer-url "#jdbc20-issuer-url")
- [Listen_Port](#jdbc20-listen-port "#jdbc20-listen-port")
- [Login_URL](#jdbc20-login_url-option "#jdbc20-login_url-option")
- [loginTimeout](#jdbc20-logintimeout-option "#jdbc20-logintimeout-option")
- [loginToRp](#jdbc20-logintorp-option "#jdbc20-logintorp-option")
- [LogLevel](#jdbc20-loglevel-option "#jdbc20-loglevel-option")
- [LogPath](#jdbc20-logpath-option "#jdbc20-logpath-option")
- [OverrideSchemaPatternType](#jdbc20-override-schema-pattern-type "#jdbc20-override-schema-pattern-type")
- [Partner_SPID](#jdbc20-partner_spid-option "#jdbc20-partner_spid-option")
- [Password](#jdbc20-password-option "#jdbc20-password-option")
- [Plugin_Name](#jdbc20-plugin_name-option "#jdbc20-plugin_name-option")
- [PORT](#jdbc20-port-option "#jdbc20-port-option")
- [Preferred_Role](#jdbc20-preferred_role-option "#jdbc20-preferred_role-option")
- [Profile](#jdbc20-profile-option "#jdbc20-profile-option")
- [PWD](#jdbc20-pwd-option "#jdbc20-pwd-option")
- [queryGroup](#jdbc20-querygroup-option "#jdbc20-querygroup-option")
- [readOnly](#jdbc20-readonly-option "#jdbc20-readonly-option")
- [Region](#jdbc20-region-option "#jdbc20-region-option")
- [reWriteBatchedInserts](#jdbc20-rewritebatchedinserts-option "#jdbc20-rewritebatchedinserts-option")
- [reWriteBatchedInsertsSize](#jdbc20-rewritebatchedinsertssize-option "#jdbc20-rewritebatchedinsertssize-option")
- [roleArn](#jdbc20-rolearn-option "#jdbc20-rolearn-option")
- [roleSessionName](#jdbc20-roleaessionname-option "#jdbc20-roleaessionname-option")
- [scope](#jdbc20-scope-option "#jdbc20-scope-option")
- [SecretAccessKey](#jdbc20-secretaccesskey-option "#jdbc20-secretaccesskey-option")
- [SessionToken](#jdbc20-sessiontoken-option "#jdbc20-sessiontoken-option")
- [serverlessAcctId](#jdbc20-serverlessacctid-option "#jdbc20-serverlessacctid-option")
- [serverlessWorkGroup](#jdbc20-serverlessworkgroup-option "#jdbc20-serverlessworkgroup-option")
- [socketFactory](#jdbc20-socketfactory-option "#jdbc20-socketfactory-option")
- [socketTimeout](#jdbc20-sockettimeout-option "#jdbc20-sockettimeout-option")
- [SSL](#jdbc20-ssl-option "#jdbc20-ssl-option")
- [SSL_Insecure](#jdbc20-ssl_insecure-option "#jdbc20-ssl_insecure-option")
- [SSLCert](#jdbc20-sslcert-option "#jdbc20-sslcert-option")
- [SSLFactory](#jdbc20-sslfactory-option "#jdbc20-sslfactory-option")
- [SSLKey](#jdbc20-sslkey-option "#jdbc20-sslkey-option")
- [SSLMode](#jdbc20-sslmode-option "#jdbc20-sslmode-option")
- [SSLPassword](#jdbc20-sslpassword-option "#jdbc20-sslpassword-option")
- [SSLRootCert](#jdbc20-sslrootcert-option "#jdbc20-sslrootcert-option")
- [StsEndpointUrl](#jdbc20-stsendpointurl-option "#jdbc20-stsendpointurl-option")
- [tcpKeepAlive](#jdbc20-tcpkeepalive-option "#jdbc20-tcpkeepalive-option")
- [token](#jdbc20-token-option "#jdbc20-token-option")
- [token_type](#jdbc20-token-type-option "#jdbc20-token-type-option")
- [UID](#jdbc20-uid-option "#jdbc20-uid-option")
- [User](#jdbc20-user-option "#jdbc20-user-option")
- [webIdentityToken](#jdbc20-webidentitytoken-option "#jdbc20-webidentitytoken-option")

## AccessKeyID

- Default Value – None
- Data Type – String

You can specify this parameter to enter the IAM access key for the user or role.
You can usually locate the key by looking at and existing string or user profile. If
you specify this parameter, you must also specify the `SecretAccessKey`
parameter. If passed in the JDBC URL, AccessKeyID must be URL encoded.

This parameter is optional.

## AllowDBUserOverride

- Default Value – 0
- Data Type – String

This option specifies whether the driver uses the `DbUser` value from
the SAML assertion or the value that is specified in the `DbUser`
connection property in the connection URL.

This parameter is optional.

**1**

The driver uses the `DbUser` value from the SAML
assertion.

If the SAML assertion doesn't specify a value for
`DBUser`, the driver uses the value specified in the
`DBUser` connection property. If the connection property
also doesn't specify a value, the driver uses the value specified
in the connection profile.

**0**

The driver uses the `DBUser` value specified in the
`DBUser` connection property.

If the `DBUser` connection property doesn't specify a
value, the driver uses the value specified in the connection profile. If
the connection profile also doesn't specify a value, the driver
uses the value from the SAML assertion.

## App_ID

- Default Value – None
- Data Type – String

The Okta-provided unique ID associated with your Amazon Redshift application.

This parameter is required if authenticating through the Okta service.

## App_Name

- Default Value – None
- Data Type – String

The name of the Okta application that you use to authenticate the connection to
Amazon Redshift.

This parameter is optional.

## ApplicationName

- Default Value – null
- Data Type – String

The name of the application to pass to Amazon Redshift for audit purposes.

This parameter is optional.

## AuthProfile

- Default Value – None
- Data Type – String

The name of the authentication profile to use for connecting to Amazon Redshift.

This parameter is optional.

## AutoCreate

- Default Value – false
- Data Type – Boolean

This option specifies whether the driver causes a new user to be created when the
specified user doesn't exist.

This parameter is optional.

**true**

If the user specified by either `DBUser` or unique ID (UID)
doesn't exist, a new user with that name is created.

**false**

The driver doesn't cause new users to be created. If the
specified user doesn't exist, the authentication fails.

## Client_ID

- Default Value – None
- Data Type – String

The client ID to use when authenticating the connection using the Azure AD
service.

This parameter is required if authenticating through the Azure AD service.

## Client_Secret

- Default Value – None
- Data Type – String

The Client Secret to use when authenticating the connection using the Azure AD
service.

This parameter is required if authenticating through the Azure AD service.

## ClusterID

- Default Value – None
- Data Type – String

The name of the Amazon Redshift cluster that you want to connect to. The driver attempts to
detect this parameter from the given host. If you're using a Network Load Balancer
(NLB) and connecting via IAM, the driver will fail to detect it, so you can set it
using this connection option.

This parameter is optional.

## Compression

- Default Value – off
- Data Type – String

The compression method used for wire protocol communication between the Amazon Redshift
server and the client or driver.

This parameter is optional.

You can specify the following values:

- **lz4**

Sets the compression method used for wire protocol communication with
Amazon Redshift to lz4.

- **off**

Doesn't use compression for wire protocol communication with
Amazon Redshift.

## connectTimeout

- Default Value – 10
- Data Type – Integer

The timeout value to use for socket connect operations. If the time required to
establish an Amazon Redshift connection exceeds this value, the connection is considered
unavailable. The timeout is specified in seconds. A value of 0 means that no timeout
is specified.

This parameter is optional.

## connectionTimezone

- Default Value – LOCAL
- Data Type – String

The session level timezone.

This parameter is optional.

You can specify the following values:

**LOCAL**

Configures the session level timezone to the LOCAL JVM
timezone.

**SERVER**

Configures the session level timezone to the timezone set for the user
on the Amazon Redshift server. You can configure session level timezones
for users with the following command:

```
ALTER USER
[...]
SET TIMEZONE TO [...];
```

## databaseMetadataCurrentDbOnly

- Default Value – true
- Data Type – Boolean

This option specifies whether the metadata API retrieves data from all accessible
databases or only from the connected database.

This parameter is optional.

You can specify the following values:

**true**

The application retrieves metadata from a single database.

**false**

The application retrieves metadata from all accessible
databases.

## DbUser

- Default Value – None
- Data Type – String

The user ID to use with your Amazon Redshift account. You can use an ID that doesn't
currently exist if you have enabled the AutoCreate property.

This parameter is optional.

## DbGroups

- Default Value – PUBLIC
- Data Type – String

A comma-separated list of existing database group names that `DBUser`
joins for the current session.

This parameter is optional.

## DBNAME

- Default Value – null
- Data Type – String

The name of the database to connect to. You can use this option to specify the
database name in the JDBC connection URL.

This parameter is required. You must specify the database name, either in the
connection URL or in the connection properties of the client application.

## defaultRowFetchSize

- Default Value – 0
- Data Type – Integer

This option specifies a default value for getFetchSize.

This parameter is optional.

You can specify the following values:

**0**

Fetch all rows in a single operation.

**Positive integer**

Number of rows to fetch from the database for each fetch iteration of
the ResultSet.

## DisableIsValidQuery

- Default Value – False
- Data Type – Boolean

This option specifies whether the driver submits a new database query when using
the Connection.isValid() method to determine whether the database connection is
active.

This parameter is optional.

**true**

The driver doesn't submit a query when using Connection.isValid()
to determine whether the database connection is active. This may cause
the driver to incorrectly identify the database connection as active if
the database server has shut down unexpectedly.

**false**

The driver submits a query when using Connection.isValid() to
determine whether the database connection is active.

## enableFetchRingBuffer

- Default Value – true
- Data Type – Boolean

This option specifies that the driver fetches rows using a ring buffer on a
separate thread. The fetchRingBufferSize parameter specifies the ring buffer size.

If a transaction detects a Statement containing multiple SQL commands separated by
semicolons, the fetch ring buffer for that transaction is set to false.
enableFetchRingBuffer's value doesn't change.

This parameter is optional.

## enableMultiSqlSupport

- Default Value – true
- Data Type – Boolean

This option specifies whether to process multiple SQL commands separated by
semicolons in a Statement.

This parameter is optional.

You can specify the following values:

**true**

The driver processes multiple SQL commands, separated by semicolons,
in a Statement object.

**false**

The driver returns an error for multiple SQL commands in a single
Statement.

## fetchRingBufferSize

- Default Value – 1G
- Data Type – String

This option specifies the size of the ring buffer used while fetching the result
set. You can specify a size in bytes, for example 1K for 1 KB, 5000 for 5,000 bytes,
1M for 1 MB, 1G for 1 GB, and so on. You can also specify a percentage of heap
memory. The driver stops fetching rows upon reaching the limit. Fetching resumes
when the application reads rows and frees space in the ring buffer.

This parameter is optional.

## ForceLowercase

- Default Value – false
- Data Type – Boolean

This option specifies whether the driver lowercases all database groups (DbGroups)
sent from the identity provider to Amazon Redshift when using single sign-on authentication.

This parameter is optional.

**true**

The driver lowercases all database groups that are sent from the
identity provider.

**false**

The driver doesn't alter database groups.

## groupFederation

- Default Value – false
- Data Type – Boolean

This option specifies whether to use Amazon Redshift IDP groups. This is supported by the
GetClusterCredentialsV2 API.

This parameter is optional.

**true**

Use Amazon Redshift Identity Provider (IDP) groups.

**false**

Use STS API and GetClusterCredentials for user federation and
explicitly specify DbGroups for the connection.

## HOST

- Default Value – null
- Data Type – String

The host name of the Amazon Redshift server to connect to. You can use this option to
specify the host name in the JDBC connection URL.

This parameter is required. You must specify the host name, either in the
connection URL or in the connection properties of the client application.

## IAMDisableCache

- Default Value – false
- Data Type – Boolean

This option specifies whether the IAM credentials are cached.

This parameter is optional.

**true**

The IAM credentials aren't cached.

**false**

The IAM credentials are cached. This improves performance when
requests to the API gateway are throttled, for instance.

## IAMDuration

- Default Value – 900
- Data Type – Integer

The length of time, in seconds, until the temporary IAM credentials expire.

- Minimum value – 900
- Maximum value – 3,600

This parameter is optional.

## Idc_Client_Display_Name

- Default Value – Amazon Redshift JDBC
  driver
- Data Type – String

The display name to be used for the client that's using
BrowserIdcAuthPlugin.

This parameter is optional.

## Idc_Region

- Default Value – None
- Data Type – String

The AWS region where the IAM Identity Center instance is located.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the plugin_name configuration
option.

## IdP_Host

- Default Value – None
- Data Type – String

The IdP (identity provider) host you are using to authenticate into Amazon Redshift. This can
be specified in either the connection string or in a profile.

This parameter is optional.

## IdP_Partition

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

## IdP_Port

- Default Value – None
- Data Type – String

The port used by an IdP (identity provider). You can specify the port in either
the connection string or in a profile. The default port is 5439. Depending on the
port you selected when creating, modifying or migrating the cluster, allow access to
the selected port.

This parameter is optional.

## IdP_Tenant

- Default Value – None
- Data Type – String

The Azure AD tenant ID for your Amazon Redshift application.

This parameter is required if authenticating through the Azure AD service.

## IdP_Response_Timeout

- Default Value – 120
- Data Type – Integer

The amount of time, in seconds, that the driver waits for the SAML response from
the identity provider when using the SAML or Azure AD services through a browser
plugin.

This parameter is optional.

## IniFile

- Default Value – None
- Data Type – String

The full path of the .ini file, including file name. For example:

```
IniFile="C:\tools\rsjdbc.ini"
```

For information about the .ini file, see [Creating initialization (.ini) files for JDBC driver
version 2.x](jdbc20-ini-file.md "jdbc20-ini-file.md").

This parameter is optional.

## IniSection

- Default Value – None
- Data Type – String

The name of a section in the .ini file containing the configuration options. For
information about the .ini file, see [Creating initialization (.ini) files for JDBC driver
version 2.x](jdbc20-ini-file.md "jdbc20-ini-file.md").

The following example specifies the [Prod] section of the .ini file:

```
IniSection="Prod"
```

This parameter is optional.

## isServerless

- Default Value – false
- Data Type – Boolean

This option specifies whether the Amazon Redshift endpoint host is a serverless instance.
The driver attempts to detect this parameter from the given host. If you're using a
Network Load Balancer (NLB), the driver will fail to detect it, so you can set it here.

This parameter is optional.

**true**

The Amazon Redshift endpoint host is a serverless instance.

**false**

The Amazon Redshift endpoint host is a provisioned cluster.

## Issuer_Url

- Default Value – None
- Data Type – String

Points to the AWS IAM Identity Center server's instance endpoint.

This parameter is required only when authenticating using
`BrowserIdcAuthPlugin` in the plugin_name configuration
option.

## Listen_Port

- Default Value – 7890
- Data Type – Integer

The port that the driver uses to receive the SAML response from the identity
provider or authorization code when using SAML, Azure AD, or AWS Identity Center
services through a browser plugin.

This parameter is optional.

## Login_URL

- Default Value – None
- Data Type – String

The URL for the resource on the identity provider's website when using the SAML or
Azure AD services through a browser plugin.

This parameter is required if authenticating with the SAML or Azure AD services
through a browser plugin.

## loginTimeout

- Default Value – 0
- Data Type – Integer

The number of seconds to wait before timing out when connecting and authenticating
to the server. If establishing the connection takes longer than this threshold, then
the connection is aborted.

When this property is set to 0, connections don't time out.

This parameter is optional.

## loginToRp

- Default Value –
  `urn:amazon:webservices`
- Data Type – String

The relying party trust that you want to use for the AD FS authentication type.

This parameter is optional.

## LogLevel

- Default Value – 0
- Data Type – Integer

Use this property to turn on or turn off logging in the driver and to specify the
amount of detail included in log files.

Enable logging only long enough to capture an issue. Logging decreases performance
and can consume a large quantity of disk space.

This parameter is optional.

Set the parameter to one of the following values:

**0**

Disable all logging.

**1**

Enable logging on the FATAL level, which logs very severe error events
that will lead the driver to abort.

**2**

Enable logging on the ERROR level, which logs error events that might
still allow the driver to continue running.

**3**

Enable logging on the WARNING level, which logs events that might
result in an error if action is not taken.

**4**

Enable logging on the INFO level, which logs general information that
describes the progress of the driver.

**5**

Enable logging on the DEBUG level, which logs detailed information
that is useful for debugging the driver.

**6**

Enable logging on the TRACE level, which logs all driver
activity.

When logging is enabled, the driver produces the following log files in the
location specified in the `LogPath` property:

- `redshift_jdbc.log` – File that logs driver
  activity that is not specific to a connection.
- `redshift_jdbc_connection_[Number].log` –
  File for each connection made to the database, where `[Number]`
  is a number that distinguishes each log file from the others. This file logs
  driver activity that is specific to the connection.

If the LogPath value is invalid, the driver sends the logged information to the
standard output stream, `System.out`.

## LogPath

- Default Value – The current working
  directory.
- Data Type – String

The full path to the folder where the driver saves log files when the DSILogLevel
property is enabled.

To be sure that the connection URL is compatible with all JDBC applications, we
recommend that you escape the backslashes (\) in your file path by typing another
backslash.

This parameter is optional.

## OverrideSchemaPatternType

- Default Value – null
- Data Type – Integer

This option specifies whether to override the type of query used in getTables
calls.

**0**

No Schema Universal Query

**1**

Local Schema Query

**2**

External Schema Query

This parameter is optional.

## Partner_SPID

- Default Value – None
- Data Type – String

The partner SPID (service provider ID) value to use when authenticating the
connection using the PingFederate service.

This parameter is optional.

## Password

- Default Value – None
- Data Type – String

When connecting using IAM authentication through an IDP, this is the password
for the IDP_Host server. When using standard authentication, this can be used for
the Amazon Redshift database password instead of PWD.

This parameter is optional.

## Plugin_Name

- Default Value – None
- Data Type – String

The fully qualified class name to implement a specific credentials provider
plugin.

This parameter is optional.

The following provider options are supported:

- `AdfsCredentialsProvider`
  – Active Directory Federation Service.
- `AzureCredentialsProvider`
  – Microsoft Azure Active Directory (AD) Service.
- `BasicJwtCredentialsProvider`
  – JSON Web Tokens (JWT) Service.
- `BasicSamlCredentialsProvider`
  – Security Assertion Markup Language (SAML) credentials which you can
  use with many SAML service providers.
- `BrowserAzureCredentialsProvider` – Browser
  Microsoft Azure Active Directory (AD) Service.
- `BrowserAzureOAuth2CredentialsProvider`
  – Browser Microsoft Azure Active Directory (AD) Service for
  Native Authentication.
- `BrowserIdcAuthPlugin`
  – An authorization plugin using AWS IAM Identity Center.
- `BrowserSamlCredentialsProvider`
  – Browser SAML for SAML services such as Okta, Ping, or ADFS.
- `IdpTokenAuthPlugin` – An
  authorization plugin that accepts an AWS IAM Identity Center token or OpenID Connect
  (OIDC) JSON-based identity tokens (JWT) from any web identity provider
  linked to AWS IAM Identity Center.
- `OktaCredentialsProvider`
  – Okta Service.
- `PingCredentialsProvider`
  – PingFederate Service.

## PORT

- Default Value – null
- Data Type – Integer

The port of the Amazon Redshift server to connect to. You can use this option to specify
the port in the JDBC connection URL.

This parameter is optional.

## Preferred_Role

- Default Value – None
- Data Type – String

The IAM role that you want to assume during the connection to Amazon Redshift.

This parameter is optional.

## Profile

- Default Value – None
- Data Type – String

The name of the profile to use for IAM authentication. This profile contains any
additional connection properties not specified in the connection string.

This parameter is optional.

## PWD

- Default Value – None
- Data Type – String

The password corresponding to the Amazon Redshift username that you provided using the
property UID.

This parameter is optional.

## queryGroup

- Default Value – null
- Data Type – String

This option assigns a query to a queue at runtime by assigning your query to the
appropriate query group. The query group is set for the session. All queries that
run on the connection belong to this query group.

This parameter is optional.

## readOnly

- Default Value – false
- Data Type – Boolean

This property specifies whether the driver is in read-only mode.

This parameter is optional.

**true**

The connection is in read-only mode and cannot write to the data
store.

**false**

The connection is not in read-only mode and can write to the data
store.

## Region

- Default Value – null
- Data Type – String

This option specifies the AWS Region where the cluster is located. If you
specify the StsEndPoint option, the Region option is ignored. The Redshift
`GetClusterCredentials` API operation also uses the Region option.

This parameter is optional.

## reWriteBatchedInserts

- Default Value – false
- Data Type – Boolean

This option enables optimization to rewrite and combine compatible INSERT
statements into batches.

This parameter is optional.

## reWriteBatchedInsertsSize

- Default Value – 128
- Data Type – Integer

This option enables optimization to rewrite and combine compatible INSERT
statements into batches. This value must increase exponentially by the power of 2.

This parameter is optional.

## roleArn

- Default Value – None
- Data Type – String

The Amazon Resource Name (ARN) of role. Make sure to specify this parameter when
you specify BasicJwtCredentialsProvider for the Plugin_Name option. You specify the
ARN in the following format:

`arn:`partition`:`service`:`region`:`account-id`:`resource-id``

This parameter is required if you specify BasicJwtCredentialsProvider for the
Plugin_Name option.

## roleSessionName

- Default Value –
  jwt_redshift_session
- Data Type – String

An identifier for the assumed role session. Typically, you pass the name or
identifier that is associated with the user of your application. The temporary
security credentials that your application uses are associated with that user. You
can specify this parameter when you specify BasicJwtCredentialsProvider for the
Plugin_Name option.

This parameter is optional.

## scope

- Default Value – None
- Data Type – String

A space-separated list of scopes to which the user can consent. You specify this
parameter so that your Microsoft Azure application can get consent for APIs that you
want to call. You can specify this parameter when you specify
BrowserAzureOAuth2CredentialsProvider for the Plugin_Name option.

This parameter is required for the BrowserAzureOAuth2CredentialsProvider
plug-in.

## SecretAccessKey

- Default Value – None
- Data Type – String

The IAM access key for the user or role. If this is specified, then AccessKeyID
must also be specified. If passed in the JDBC URL, SecretAccessKey must be URL
encoded.

This parameter is optional.

## SessionToken

- Default Value – None
- Data Type – String

The temporary IAM session token associated with the IAM role you are using to
authenticate. If passed in the JDBC URL, the temporary IAM session token must be URL
encoded.

This parameter is optional.

## serverlessAcctId

- Default Value – null
- Data Type – String

The Amazon Redshift Serverless account ID. The driver attempts to detect this parameter
from the given host. If you're using a Network Load Balancer (NLB), the driver will fail to detect
it, so you can set it here.

This parameter is optional.

## serverlessWorkGroup

- Default Value – null
- Data Type – String

The Amazon Redshift Serverless workgroup name. The driver attempts to detect this parameter
from the given host. If you're using a Network Load Balancer (NLB), the driver will fail to detect
it, so you can set it here.

This parameter is optional.

## socketFactory

- Default Value – null
- Data Type – String

This option specifies a socket factory for socket creation.

This parameter is optional.

## socketTimeout

- Default Value – 0
- Data Type – Integer

The number of seconds to wait during socket read operations before timing out. If
the operation takes longer than this threshold, then the connection is closed. When
this property is set to 0, the connection doesn't time out.

This parameter is optional.

## SSL

- Default Value – TRUE
- Data Type – String

Use this property to turn on or turn off SSL for the connection.

This parameter is optional.

You can specify the following values:

**TRUE**

The driver connects to the server through SSL.

**FALSE**

The driver connects to the server without using SSL. This option is
not supported with IAM authentication.

Alternatively, you can configure the AuthMech property.

## SSL_Insecure

- Default Value – true
- Data Type – String

This property indicates whether the IDP hosts server certificate should be
verified.

This parameter is optional.

You can specify the following values:

**true**

The driver doesn't check the authenticity of the IDP server
certificate.

**false**

The driver checks the authenticity of the IDP server
certificate.

## SSLCert

- Default Value – None
- Data Type – String

The full path of a .pem or .crt file containing additional trusted CA certificates
for verifying the Amazon Redshift server instance when using SSL.

This parameter is required if SSLKey is specified.

## SSLFactory

- Default Value – None
- Data Type – String

The SSL factory to use when connecting to the server through TLS/SSL without using
a server certificate.

## SSLKey

- Default Value – None
- Data Type – String

The full path of the .der file containing the PKCS8 key file for verifying the
certificates specified in SSLCert.

This parameter is required if SSLCert is specified.

## SSLMode

- Default Value – verify-ca
- Data Type – String

Use this property to specify how the driver validates certificates when TLS/SSL is
enabled.

This parameter is optional.

You can specify the following values:

**verify-ca**

The driver verifies that the certificate comes from a trusted
certificate authority (CA).

**verify-full**

The driver verifies that the certificate comes from a trusted CA and
that the host name in the certificate matches the host name specified in
the connection URL.

## SSLPassword

- Default Value – 0
- Data Type – String

The password for the encrypted key file specified in SSLKey.

This parameter is required if SSLKey is specified and the key file is
encrypted.

## SSLRootCert

- Default Value – None
- Data Type – String

The full path of a .pem or .crt file containing the root CA certificate for
verifying the Amazon Redshift Server instance when using SSL.

## StsEndpointUrl

- Default Value – null
- Data Type – String

You can specify an AWS Security Token Service (AWS STS) endpoint. If you specify this option, the
Region option is ignored. You can only specify a secure protocol (HTTPS) for this
endpoint.

## tcpKeepAlive

- Default Value – TRUE
- Data Type – String

Use this property to turn on or turn off TCP keepalives.

This parameter is optional.

You can specify the following values:

**TRUE**

The driver uses TCP keepalives to prevent connections from timing
out.

**FALSE**

The driver doesn't use TCP keepalives.

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

## UID

- Default Value – None
- Data Type – String

The database username that you use to access the database.

This parameter is required.

## User

- Default Value – None
- Data Type – String

When connecting using IAM authentication through an IDP, this is the username
for the idp_host server. When using standard authentication, this can be used for
the Amazon Redshift database username.

This parameter is optional.

## webIdentityToken

- Default Value – None
- Data Type – String

The OAuth 2.1 access token or OpenID Connect ID token that is provided by the
identity provider. Your application must get this token by authenticating the user
of your application with a web identity provider. Make sure to specify this
parameter when you specify BasicJwtCredentialsProvider for the Plugin_Name option.

This parameter is required if you specify BasicJwtCredentialsProvider for the
Plugin_Name option.

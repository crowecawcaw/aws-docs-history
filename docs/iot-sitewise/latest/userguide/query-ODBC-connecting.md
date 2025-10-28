# Connection string syntax and options for the ODBC driver

The syntax for specifying connection-string options for the ODBC driver is as follows:

```
Driver={AWS IoT SiteWise ODBC Driver};`(option)`=`(value)`;
```

Available options are as follows:

###### Driver connection options

- **`Driver`**   _(required)_   –  
  The driver being used with ODBC.

The default is AWS IoT SiteWise.

- **`DSN`**   –  
  The data source name (DSN) to use for configuring the connection.

The default is `NONE`.

- **`Auth`**   –  
  The authentication mode. This must be one of the following:

      + `AWS_PROFILE` – Use the default credential chain.
      + `IAM` – Use AWS IAM credentials.
      + `AAD` – Use the Azure Active Directory (AD) identity provider.
      + `OKTA` – Use the Okta identity provider.

  The default is `AWS_PROFILE`.

###### Endpoint configuration options

- **`EndpointOverride`**   –  
  The endpoint override for the AWS IoT SiteWise service. This is an advanced option that overrides
  the region. For example:

```
iotsitewise.us-east-1.amazonaws.com
```

- **`Region`**   –  
  The signing region for the AWS IoT SiteWise service endpoint.

The default is `us-east-1`.

###### Credentials provider option

- **`ProfileName`**   –  
  The profile name in the AWS config file.

The default is `NONE`.

###### AWS IAM authentication options

- **`UID`** or **`AccessKeyId`**   –  
  The AWS user access key id. If both `UID` and `AccessKeyId` are
  provided in the connection string, the `UID` value will be used unless it is empty.

The default is `NONE`.

- **`PWD`** or **`SecretKey`**   –  
  The AWS user secret access key. If both `PWD` and `SecretKey` are
  provided in the connection string, the `PWD` value with will be used unless it's empty.

The default is `NONE`.

- **`SessionToken`**   –  
  The temporary session token required to access a database with multi-factor
  authentication (MFA) enabled. Do not include a trailing `=` in the input.

The default is `NONE`.

###### SAML-based authentication options for Okta

- **`IdPHost`**   –  
  The hostname of the specified IdP.

The default is `NONE`.

- **`UID`** or **`IdPUserName`**   –  
  The user name for the specified IdP account. If both `UID` and
  `IdPUserName` are provided in the connection string, the `UID`
  value will be used unless it's empty.

The default is `NONE`.

- **`PWD`** or **`IdPPassword`**   –  
  The password for the specified IdP account. If both `PWD` and
  `IdPPassword` are provided in the connection string, the `PWD`
  value will be used unless it's empty.

The default is `NONE`.

- **`OktaApplicationID`**   –  
  The unique Okta-provided ID associated with the AWS IoT SiteWise application. A place
  to find the application ID (AppId) is in the `entityID` field
  provided in the application metadata. An example is:

```
entityID="http://www.okta.com//`(IdPAppID)`
```

The default is `NONE`.

- **`RoleARN`**   –  
  The Amazon Resource Name (ARN) of the role that the caller is assuming.

The default is `NONE`.

- **`IdPARN`**   –  
  The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.

The default is `NONE`.

###### SAML-based authentication options for Azure Active Directory

- **`UID`** or **`IdPUserName`**   –  
  The user name for the specified IdP account..

The default is `NONE`.

- **`PWD`** or **`IdPPassword`**   –  
  The password for the specified IdP account.

The default is `NONE`.

- **`AADApplicationID`**   –  
  The unique id of the registered application on Azure AD.

The default is `NONE`.

- **`AADClientSecret`**   –  
  The client secret associated with the registered application on Azure AD used to authorize fetching tokens.

The default is `NONE`.

- **`AADTenant`**   –  
  The Azure AD Tenant ID.

The default is `NONE`.

- **`RoleARN`**   –  
  The Amazon Resource Name (ARN) of the role that the caller is assuming.

The default is `NONE`.

- **`IdPARN`**   –  
  The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.

The default is `NONE`.

###### AWS SDK (advanced) Options

- **`RequestTimeout`**   –  
  The time in milliseconds that the AWS SDK waits for a query request
  before timing out. Any non-positive value disables the request timeout.

The default is `3000`.

- **`ConnectionTimeout`**   –  
  The time in milliseconds that the AWS SDK waits for data to be transferred
  over an open connection before timing out. A value of 0 disables the
  connection timeout. This value must not be negative.

The default is `1000`.

- **`MaxRetryCountClient`**   –  
  The maximum number of retry attempts for retryable errors with 5xx error
  codes in the SDK. The value must not be negative.

The default is `0`.

- **`MaxConnections`**   –  
  The maximum number of allowed concurrently open HTTP connections to the
  AWS IoT SiteWise service. The value must be positive.

The default is `25`.

###### ODBC driver logging Options

- **`LogLevel`**   –  
  The log level for driver logging. Must be one of:

      + **0**   (OFF).
      + **1**   (ERROR).
      + **2**   (WARNING).
      + **3**   (INFO).
      + **4**   (DEBUG).

  The default is `1` (ERROR).

**Warning:** personal information could be
logged by the driver when using the DEBUG logging mode.

- **`LogOutput`**   –  
  Folder in which to store the log file.

The default is:

    + **Windows:** `%USERPROFILE%`,
     or if not available, `%HOMEDRIVE%%HOMEPATH%`.
    + **macOS and Linux:** `$HOME`,
     or if not available, the field `pw_dir` from the function
     `getpwuid(getuid())` return value.

**SDK logging options**

The AWS SDK log level is separate from the AWS IoT SiteWise ODBC driver log level.
Setting one does not affect the other.

The SDK Log Level is set using the environment variable `SW_AWS_LOG_LEVEL`.
Valid values are:

- `OFF`
- `ERROR`
- `WARN`
- `INFO`
- `DEBUG`
- `TRACE`
- `FATAL`
  If `SW_AWS_LOG_LEVEL` is not set, the SDK log level is set to the default,
  which is `WARN`.

## Connecting through a proxy

The ODBC driver supports connecting to AWS IoT SiteWise through a proxy. To use this
feature, configure the following environment variables based on your proxy setting:

- **`SW_PROXY_HOST`**   –  
  the proxy host.
- **`SW_PROXY_PORT`**   –  
  The proxy port number.
- **`SW_PROXY_SCHEME`**   –  
  The proxy scheme, either `http` or `https`.
- **`SW_PROXY_USER`**   –  
  The user name for proxy authentication.
- **`SW_PROXY_PASSWORD`**   –  
  The user password for proxy authentication.
- **`SW_PROXY_SSL_CERT_PATH`**   –  
  The SSL Certificate file to use for connecting to an HTTPS proxy.
- **`SW_PROXY_SSL_CERT_TYPE`**   –  
  The type of the proxy client SSL certificate.
- **`SW_PROXY_SSL_KEY_PATH`**   –  
  The private key file to use for connecting to an HTTPS proxy.
- **`SW_PROXY_SSL_KEY_TYPE`**   –  
  The type of the private key file used to connect to an HTTPS proxy.
- **`SW_PROXY_SSL_KEY_PASSWORD`**   –  
  The passphrase to the private key file used to connect to an HTTPS proxy.

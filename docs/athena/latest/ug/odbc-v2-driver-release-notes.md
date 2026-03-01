# Amazon Athena ODBC 2.x release notes

These release notes provide details of enhancements, features, known issues, and workflow
changes in the Amazon Athena ODBC 2.x driver.

## 2.0.6.0

Released 2025-11-21

### Improvements

- Browser Trusted Identity Propagation authentication plugin
  – Added a new authentication plugin to support browser-based OpenID Connect (OIDC)
  authentication with trusted identity propagation. This plugin provides a seamless authentication experience by
  handling the complete OAuth 2.0 flow through your default browser, automatically fetching
  the JSON Web Token (JWT), and integrating with trusted identity propagation. The plugin is specifically designed
  for single-user desktop environments. For information on enabling and using trusted identity propagation, see
  [What is trusted identity propagation?](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").
- Enhanced logging framework – Significantly
  improved the driver's logging mechanism by:
  - Introducing more granular log levels beyond basic 0/1 options
  - Removing redundant log statements
  - Optimizing the logging framework to include diagnostically relevant information
  - Addressing performance issues that were causing operational delays
  - Reducing excessive log file generation when logging is enabled

### Fixes

- Result fetcher optimization – Fixed an issue
  where fetch size parameter limitations were incorrectly applied to both streaming and
  non-streaming result fetchers. The limitation is now correctly applied only to
  non-streaming result fetchers.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.5.1

Released 2025-10-13

### Fixes

The Amazon Athena ODBC v2.0.5.1 driver contains the following fixes to
browser-based authentication plugins.

- Implemented validation for login URL and schema checking.
- Improved browser launch mechanism on Linux to utilize system APIs, resulting in improved stability and security.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.5.0

Released 2025-09-10

### Improvements

- JWT Trusted Identity Provider (TIP) authentication
  plugin – Added a new authentication plugin to support
  JWT Trusted Identity Provider (TIP) integration with ODBC drivers. This
  authentication type allows you to use a JSON web token (JWT) obtained from
  an external identity provider as a connection parameter to authenticate with
  Athena. With TIP, identity context is added to an IAM role to identify the
  user requesting access to AWS resources. For information on enabling and
  using TIP, see [What is Trusted Identity Propagation?](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").
- Custom SSO admin endpoints support –
  Added support for custom SSO Admin endpoints in the ODBC driver. This
  enhancement allows you to specify your own endpoints for SSO services when
  running ODBC behind VPCs.
- AWS SDK version update – We have
  updated the AWS SDK version used in the driver to 2.32.16 and have updated
  the project dependencies for release 2.0.5.0.

## 2.0.4.0

Released 2025-06-17

The Amazon Athena ODBC v2.0.4.0 driver contains the following improvements and
fixes.

### Improvements

- **Result Fetcher** – The driver now
  automatically selects the method to download query results. This removes the
  need to manually configure the fetcher in most situations. For more
  information, see [Result fetcher](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-result-fetcher "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-result-fetcher").
- Curl Library has been updated to 8.12.1.

### Fixes

- Fixed proxy configuration for IAM profile when connecting to STS. The fix allows IAM Profile to be used for successful authentication.
- Read all additional configuration options for IAM profile with
  authentication plugins. This includes `UseProxyForIdP`,
  `SSL_Insecure`, `LakeformationEnabled`, and
  `LoginToRP` to resolve misconfigurations for the affected
  plugins.
- Fixed round function by allowing it to take in an optional 2nd parameter.
  It successfully processes queries containing the escape syntax.
- Fixed column size for `TIME WITH TIME ZONE` and `TIMESTAMP WITH TIME ZONE` data types. Values with timestamp and timezone data type will not get truncated.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.3.0

Released 2024-04-08

The Amazon Athena ODBC v2.0.3.0 driver contains the following improvements and
fixes.

### Improvements

- Added MFA support for the Okta authentication plugin on Linux and Mac
  platforms.
- Both the `athena-odbc.dll` library and the
  `AmazonAthenaODBC-2.x.x.x.msi` installer for Windows
  are now signed.
- Updated the CA certificate `cacert.pem` file that is
  installed with the driver.
- Improved the time required to list tables under Lambda catalogs. For
  `LAMBDA` catalog types, the ODBC driver can now submit a
  [SHOW TABLES](show-tables.md "show-tables.md") query to get a
  list of available tables. For more information, see [Use query to list tables](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-use-query-to-list-tables "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-use-query-to-list-tables").
- Introduced the `UseWCharForStringTypes` connection parameter to
  report string data types using `SQL_WCHAR` and
  `SQL_WVARCHAR`. For more information, see [Use WCHAR for string types](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-use-wchar-for-string-types "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-use-wchar-for-string-types").

### Fixes

- Fixed a registry corruption warning that occurred when the Get-OdbcDsn
  PowerShell tool was used.
- Updated the parsing logic to handle comments at the start of query
  strings.
- Date and timestamp data types now allow zero in the year field.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.2.2

Released 2024-02-13

The Amazon Athena ODBC v2.0.2.2 driver contains the following improvements and
fixes.

### Improvements

- Added two connection parameters, `StringColumnLength` and
  `ComplexTypeColumnLength`, that you can use to change the
  default column length for string and complex data types. For more
  information, see [String column length](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-string-column-length "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-string-column-length")
  and [Complex type column length](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-complex-type-column-length "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-complex-type-column-length").
- Support has been added for the Linux and macOS (Intel and ARM) operating
  systems. For more information, see [Linux](odbc-v2-driver-getting-started-linux.md "odbc-v2-driver-getting-started-linux.md") and [macOS](odbc-v2-driver-getting-started-macos.md "odbc-v2-driver-getting-started-macos.md").
- AWS-SDK-CPP has been updated to the 1.11.245 tag version.
- The curl library has been updated to the 8.6.0 version.

### Fixes

- Resolved an issue that cause incorrect values to be reported in result-set
  metadata for string-like data types in the precision column.

To download the ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.2.1

Released 2023-12-07

The Amazon Athena ODBC v2.0.2.1 driver contains the following improvements and
fixes.

### Improvements

- Improved ODBC driver thread safety for all interfaces.
- When logging is enabled, datetime values are now recorded with millisecond
  precision.
- During authentication with the [Browser SSO OIDC](odbc-v2-driver-browser-sso-oidc.md "odbc-v2-driver-browser-sso-oidc.md") plugin, the terminal
  now opens to display the device code to the user.

### Fixes

- Resolved a memory release issue that occurred when parsing results from
  the streaming API.
- Requests for the interfaces `SQLTablePrivileges()`,
  `SQLSpecialColumns()`, `SQLProcedureColumns()`,
  and `SQLProcedures()` now return empty result sets.

To download the ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.2.0

Released 2023-10-17

The Amazon Athena ODBC v2.0.2.0 driver contains the following improvements and
fixes.

### Improvements

- File cache feature added for the Browser Azure AD, Browser SSO OIDC, and
  Okta browser-based authentication plugins.

BI Tools like Power BI and browser-based plugins use multiple browser
windows. The new file cache connection parameter enables temporary
credentials to be cached and reused between the multiple processes opened by
BI applications.

- Applications can now query information about the result set after a
  statement is prepared.
- Default connection and request timeouts have been increased for use with
  slower client networks. For more information, see [Connection timeout](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-connection-timeout "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-connection-timeout") and
  [Request timeout](odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-request-timeout "odbc-v2-driver-advanced-options.md#odbc-v2-driver-advanced-options-request-timeout").
- Endpoint overrides have been added for SSO and SSO OIDC. For more
  information, see [Endpoint overrides](odbc-v2-driver-endpoint-overrides.md "odbc-v2-driver-endpoint-overrides.md").
- Added a connection parameter to pass a URI argument for an authentication
  request to Ping. You can use this parameter to bypass the Lake Formation
  single role limitation. For more information, see [Ping URI param](odbc-v2-driver-ping.md#odbc-v2-driver-ping-uri-param "odbc-v2-driver-ping.md#odbc-v2-driver-ping-uri-param").

### Fixes

- Fixed an integer overflow issue that occurred when using the row-based
  binding mechanism.
- Removed timeout from the list of required connection parameters for the
  Browser SSO OIDC authentication plugin.
- Added missing interfaces for `SQLStatistics()`,
  `SQLPrimaryKeys()`, `SQLForeignKeys()`, and
  `SQLColumnPrivileges()`, and added the ability to return
  empty result sets upon request.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download"). For connection information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

## 2.0.1.1

Released 2023-08-10

The Amazon Athena ODBC v2.0.1.1 driver contains the following improvements and
fixes.

### Improvements

- Added URI logging to the Okta authentication plugin.
- Added the preferred role parameter to the external credentials provider
  plugin.
- Adding handling for the profile prefix in the profile name of AWS
  configuration file.

### Fixes

- Corrected a AWS Region use issue that occurred when working with Lake Formation
  and AWS STS clients.
- Restored missing partition keys to the list of table columns.
- Added the missing `BrowserSSOOIDC` authentication type to the
  AWS profile.

To download the new ODBC v2 driver, see [ODBC 2.x driver download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download").

## 2.0.1.0

Released 2023-06-29

Amazon Athena releases the ODBC v2.0.1.0 driver.

Athena has released a new ODBC driver that improves the experience of connecting to,
querying, and visualizing data from compatible SQL development and business intelligence
applications. The latest version of the Athena ODBC driver supports the features of the
existing driver and is straightforward to upgrade. The new version includes support for
authenticating users through [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"). It also offers the option to read query results from Amazon S3, which
can make query results available to you sooner.

For more information, see [Amazon Athena ODBC 2.x](odbc-v2-driver.md "odbc-v2-driver.md").

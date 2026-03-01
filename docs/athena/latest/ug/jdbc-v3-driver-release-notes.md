# Amazon Athena JDBC 3.x release notes

These release notes provide details of improvements and fixes in the Amazon Athena JDBC 3.x
driver.

## 3.7.0

Released 2025-11-21

### Improvements

- Browser OIDC Trusted identity propagation authentication plugin –
  Added a new authentication plugin that enables seamless browser-based authentication
  with OpenID Connect (OIDC) identity providers. This plugin handles the complete OAuth 2.0
  flow through your default browser, automatically fetches the JSON Web Token (JWT), and
  integrates with trusted identity propagation. Designed specifically for single-user desktop environments,
  it provides a more streamlined authentication experience compared to manual JWT handling.
  For more information about trusted identity propagation, see [What is trusted identity propagation?](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").

### Fixes

- Enhanced timestamp precision support –
  The driver now fully supports millisecond and nanosecond precision in timestamp
  values returned from Athena queries through the `getTimestamp()` method.
- Improved complex type handling –
  Fixed issues with parsing nested data types (arrays, structs, and maps) in
  both `DatabaseMetaData#getColumns` and general metadata operations,
  ensuring accurate type information for complex data structures.
- Enhanced error logging –
  Improved logging for S3 metadata fetch failures, providing clearer error messages
  and better diagnostic information.

## 3.6.0

Released 2025-09-10

### Improvements

- JWT Trusted identity propagation authentication plugin –
  Added a new authentication plugin to support JWT trusted identity propagation integration with
  JDBC drivers. This authentication type allows you to use a JSON web token
  (JWT) obtained from an external identity provider as a connection parameter
  to authenticate with Athena. With trusted identity propagation, identity context is added to an
  IAM role to identify the user requesting access to AWS resources. For
  information on enabling and using trusted identity propagation, see [What is trusted identity propagation?](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").
- Custom SSO OIDC and SSO admin endpoints
  support – Added support for custom SSO OIDC and SSO
  Admin endpoints in the JDBC driver. This enhancement allows you to specify
  your own endpoints for SSO services when running JDBC behind VPCs.
- AWS SDK version update – We have
  updated the AWS SDK version used in the driver to 2.32.16 and have updated
  the project dependencies for release 3.6.0.

## 3.5.1

Released 2025-07-17

### Improvements

- Logging capabilities – Enhanced S3
  fetch logging by elevating log level to `INFO` and adding metrics
  for row counts, offsets, and object length. Implemented connection lifecycle
  tracking and optimized overall logging performance.
- Special characters handling –
  Improved handling of special characters for `LIKE` patterns in
  schema and catalog names.
- Connection state management – Improved connection state management to prevent potential errors by preventing API calls after connection closure and adding safety checks for query operations during shutdown.

### Fixes

- DDL query metadata – Fixed
  `NoSuchKeyFound` issue with DDL query metadata
  handling.

## 3.5.0

Released 2025-03-18

### Improvements

- **Result configuration parameters** –
  Added support for two new connection parameters
  `ExpectedBucketOwner` and `AclOption`. For more
  information, see [Result
  configuration parameters](jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-result-config "jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-result-config").
- **AWS SDK version** – The AWS SDK
  version used in the driver has been updated to 2.30.22.

## 3.4.0

Released 2025-02-18

### Improvements

- Result Fetcher – The driver now
  automatically selects the fastest method to download query results. This
  removes the need to manually configure the fetcher in most situations. For
  more information, see [Result fetching parameters](jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-result-fetching-parameters "jdbc-v3-driver-advanced-connection-parameters.md#jdbc-v3-driver-result-fetching-parameters").

### Fixes

- ResultSet – The driver now handles iterating over
  the result sets of DDL statements that don't produce result objects on S3.
  It also returns an empty `ResultSet` object instead of null when
  `GetQueryResultsStream` returns a completely empty
  page.
- ResultsStream – The result streaming
  has been optimized by removing unnecessary calls to count the number of rows
  in internal buffers.
- getTables – The
  `GetTables` call has been optimized by handling table types
  based on `ListTableMetadata` and `GetTableMetadata`
  responses.

## 3.3.0

Released 2024-10-30

### Improvements

- DataZone authentication – Added
  support for the DataZone authentication plugins `DataZoneIdC` and
  `DataZoneIAM`. For more information, see [DataZone IdC Credentials Provider](jdbc-v3-driver-datazone-idc.md "jdbc-v3-driver-datazone-idc.md") and [DataZone IAM Credentials Provider](jdbc-v3-driver-datazone-iamcp.md "jdbc-v3-driver-datazone-iamcp.md").
- Network timeout – The network
  timeout can now be set using the `NetworkTimeoutMillis`
  connection parameter. Previously it could be set only on the
  `Connection` object itself. For more information, see [Network timeout](jdbc-v3-driver-other-configuration.md#jdbc-v3-driver-network-timeout "jdbc-v3-driver-other-configuration.md#jdbc-v3-driver-network-timeout").

### Fixes

- S3 empty object handling – The
  driver now handles empty objects in the S3 fetcher instead of throwing an
  Amazon S3 **`Range Not Satisfiable`** exception.
- Logging – The driver no longer logs
  the message **`Items requested for query execution [...], but
subscription is cancelled`** after consuming query
  results.
- Empty parameter strings – The driver
  now handles empty strings present in a connection parameter as if the
  parameter were not present. This resolves issues that occurred when some BI
  tools inadvertently passed empty strings that caused unintended
  authentication attempts.

## 3.2.2

Released 2024-07-29

### Improvements

- Data type mapping – Improved the
  compliance with the JDBC spec by changing how the driver maps the
  `tinyint`, `smallint`, `row`, and
  `struct` data types to Java objects.
- AWS SDK version update – The AWS
  SDK version used in the driver has been updated to 2.26.23.

### Fixes

- Comments – Fixed an issue with line
  comments at the end of a statement.
- Database listing – Fixed an issue in
  which listing databases could enter an infinite loop when the last page
  returned by the paginated `ListDatabases` API was empty.

## 3.2.1

Released 2024-07-03

### Improvements

- JWT credentials provider – Added
  support for user-specified session durations. For more information, see
  [Role session duration](jdbc-v3-driver-jwt-credentials.md#jdbc-v3-driver-jwt-role-session-duration "jdbc-v3-driver-jwt-credentials.md#jdbc-v3-driver-jwt-role-session-duration").

### Fixes

- Thread pool – Created one
  `ThreadPoolExecutor` per connection for asynchronous tasks to
  avoid using the `ForkJoin` pool.
- Credential providers – The proxy
  host is now parsed to get the scheme and host when the HTTP client is
  configured for external IdPs.
- Default credentials provider –
  Ensured the default credentials provider can't be closed by client
  code.
- getColumns – Fixed an
  `ORDINAL_COLUMN` column property issue in the
  `DatabaseMetaData#getColumns` method.
- ResultSet – Added support for
  `Infinity`, `-Infinity`, and `NaN` to
  `ResultSet.` Fixed a discrepancy between the column type
  returned from catalog operations and the result set of a completed
  query.

## 3.2.0

Released 2024-04-26

### Improvements

- Catalog operation performance –
  Performance has been improved for catalog operations that do not use
  wildcard characters.
- Minimum polling interval change –
  The minimum polling interval default has been modified to reduce the number
  of API calls the driver makes to Athena. Query completions are still detected
  as soon as possible.
- BI tool discoverability – The driver
  has been made more easily discoverable for business intelligence
  tools.
- Data type mapping – Data type
  mapping to the Athena `binary`, `array`, and
  `struct` DDL data types has been improved.
- AWS SDK version – The AWS SDK
  version used in the driver has been updated to 2.25.34.

### Fixes

- Federated catalog table listings –
  Fixed an issue that caused federated catalogs to return an empty list of
  tables.
- getSchemas – Fixed an issue that
  caused the JDBC [DatabaseMetaData#getSchemas](https://docs.oracle.com/javase/8/docs/api/java/sql/DatabaseMetaData.html#getSchemas-- "https://docs.oracle.com/javase/8/docs/api/java/sql/DatabaseMetaData.html#getSchemas--") method to fetch databases only from
  the default catalog instead of from all catalogs.
- getColumns – Fixed an issue that
  caused a null catalog to be returned when the JDBC [DatabaseMetaData#getColumns](https://docs.oracle.com/javase/8/docs/api/java/sql/DatabaseMetaData.html#getColumns-java.lang.String-java.lang.String-java.lang.String-java.lang.String- "https://docs.oracle.com/javase/8/docs/api/java/sql/DatabaseMetaData.html#getColumns-java.lang.String-java.lang.String-java.lang.String-java.lang.String-") method was called with a null
  catalog name.

## 3.1.0

Released 2024-02-15

### Improvements

- Support added for Microsoft Active Directory Federation Services (AD FS)
  Windows Integrated Authentication and form-based authentication.
- For backwards compatibility with version 2.x, the `awsathena`
  JDBC sub-protocol is now accepted but produces a deprecation warning. Use
  the `athena` JDBC sub-protocol instead.
- `AwsDataCatalog` is now the default for the catalog parameter,
  and `default` is the default for the database parameter. These
  changes ensure that correct values for the current catalog and database are
  returned instead of null.
- In conformance with the JDBC specification, `IS_AUTOINCREMENT`
  and `IS_GENERATEDCOLUMN` now return an empty string instead of
  `NO`.
- The Athena `int` data type now maps to the same JDBC type as
  Athena `integer` instead of to `other`.
- When the column metadata from Athena does not contain the optional
  `precision` and `scale` fields, the driver now
  returns zero for the corresponding values in a `ResultSet`
  column.
- The AWS SDK version has been updated to 2.21.39.

### Fixes

- Fixed an issue with `GetQueryResultsStream` that caused an
  exception to occur when plain text results from Athena had a column count
  inconsistent with the column count in Athena result metadata.

## 3.0.0

Released 2023-11-16

The Athena JDBC 3.x driver is the new generation driver offering better performance and
compatibility. The JDBC 3.x driver supports reading query results directly from Amazon S3,
which improves the performance of applications that consume large query results. The new
driver also has fewer third-party dependencies, which makes integration with BI tools
and custom applications easier.

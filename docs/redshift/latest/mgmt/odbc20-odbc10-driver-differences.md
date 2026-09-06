

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Differences between the 2.x and 1.x versions of the ODBC driver
<a name="odbc20-odbc10-driver-differences"></a>

This section describes the differences between the [ODBC 1.x driver](configure-odbc-connection.md) and the [ODBC 2.x driver](odbc20-install.md), and provides guidance about how to migrate to the 2.x driver. It describes the changes that might affect your application and how to address them.

## Key differences to address
<a name="odbc20-migrate-key-differences"></a>

The following actions resolve the most common migration issues. Most applications need only a subset of these.

### DSN and connection string
<a name="odbc20-migrate-dsn"></a>
+ **Review your DSN for driver options that might have been removed or renamed.** Some ODBC 1.x driver options are not supported in the ODBC 2.x driver. Others have been renamed. See [Connection string and DSN options](#odbc20-migrate-connection-options) for details.
+ **Set `UseUnicode=true` if your application depends on wide character type codes (`SQL_WVARCHAR`, `SQL_WCHAR`).** In the ODBC 2.x driver, `UseUnicode` defaults to `false`, which reports narrow character types.
+ **Move logging settings to the `[ODBC]` section.** On Linux and macOS, `LogLevel` and `LogPath` must be set in the global `[ODBC]` section of `odbc.ini`, not in an individual DSN section.

### Query and schema
<a name="odbc20-migrate-query-schema"></a>
+ **Include `EXTERNAL TABLE` in `SQLTables` type filters.** In ODBC 2.x, both Amazon Redshift Spectrum tables and datashare tables are reported as `EXTERNAL TABLE`. If you filter `SQLTables` by type, add `EXTERNAL TABLE` to keep seeing these objects. Alternatively, set the `EnableTableTypes` option to 0 to normalize the detailed table type information into the generic TABLE and VIEW table types, as described in the following item.
+ **Detailed table types are enabled by default.** ODBC 2.x enables the `EnableTableTypes` option by default. The 1.x driver disabled this option by default. With the 2.x default, `SQLTables` reports detailed types such as SYSTEM TABLE, SYSTEM VIEW, EXTERNAL TABLE, and LOCAL TEMPORARY. To report every table as the generic type TABLE and every view as VIEW, set `EnableTableTypes` to 0.
+ **Cast `INTERVAL` to `VARCHAR` for applications that do not support the interval data type.** Some clients do not support ODBC interval types. For those clients, cast the column in your query: `SELECT col::VARCHAR FROM ...`

### Application code
<a name="odbc20-migrate-application-code"></a>
+ **Verify query timeout settings.** ODBC 2.x correctly enforces `SQL_ATTR_QUERY_TIMEOUT` per the ODBC specification. ODBC 1.x silently ignored this setting. Long-running queries that previously succeeded might now fail with a timeout error. Review and adjust your timeout values as needed.
+ **Provide the data length for data-at-execution parameters.** 2.x reports `SQL_NEED_LONG_DATA_LEN` as `Y` (1.x reported `N`). Applications that bind `SQL_DATA_AT_EXEC` parameters must now supply the total data length up front in `StrLen_or_IndPtr`.

## Connection string and DSN options
<a name="odbc20-migrate-connection-options"></a>

The following table shows ODBC 1.x driver options that have either been renamed or have direct equivalents in the ODBC 2.x driver.


| 1.x option | 2.x equivalent | Notes | 
| --- | --- | --- | 
| MaxLongVarChar | MaxLongVarcharSize | Default changed from 8190 to 65535. | 
| ConnectionTimeout | LoginTimeout | Same connection timeout, renamed. Defaults to 0 (no timeout). | 
| VpcEndpointUrl | vpc\_endpoint\_url |  | 
| SSLCertPath | TrustStore or CaFile | Path to a CA certificate used to verify the server. On Windows, set this in the Trust Store field of the DSN setup dialog; the dialog has no CaFile field. If both are set, TrustStore takes priority. | 

The following 1.x options are not supported in the current 2.x driver. The 2.x driver ignores them, so they do not affect your connection. Removing them from your DSN is optional but recommended to avoid confusion.
+ `SingleRowMode` – to limit client memory, use `StreamingCursorRows` instead.
+ `UseSystemTrustStore` – not supported. On Windows, the 1.x driver could validate the server certificate against the Windows system certificate store. The 2.x driver validates against a CA certificate file: it uses the bundled Amazon Redshift root certificate by default, or the file you specify in `TrustStore` or `CaFile`.
+ `TextAsLongVarchar`, `CheckCertRevocation`, `EnableAwsSdkLogs`, `UseLogPrefix`, `Locale`, `UseDeclareFetch`, `UseMultipleStatements`, `EnforceSingleStatement` – no equivalent in the current release. The Amazon Redshift team is evaluating equivalents or alternatives for these options in future releases.

For the full list of supported 2.x options, see [ODBC driver options](odbc20-configuration-options.md).

## Data type changes
<a name="odbc20-migrate-data-types"></a>

The following table shows Amazon Redshift data type mappings that changed in ODBC 2.x to comply with the ODBC specification. Most applications are unaffected because they bind columns by index or by name rather than by type code.


| Amazon Redshift data type | ODBC 1.x | ODBC 2.x | 
| --- | --- | --- | 
| DOUBLE PRECISION | SQL\_FLOAT (6) | SQL\_DOUBLE (8) | 
| INTERVAL YEAR TO MONTH | SQL\_VARCHAR (12), text | SQL\_INTERVAL\_YEAR\_TO\_MONTH (107), interval struct | 
| INTERVAL DAY TO SECOND | SQL\_VARCHAR (12), text | SQL\_INTERVAL\_DAY\_TO\_SECOND (110), interval struct | 
| VARCHAR / CHAR / TEXT | Wide types (SQL\_WVARCHAR, SQL\_WCHAR, SQL\_WLONGVARCHAR); default UseUnicode=true | Narrow types (SQL\_VARCHAR, SQL\_CHAR, SQL\_LONGVARCHAR). Set UseUnicode=true to restore wide types. | 
| GEOMETRY / GEOGRAPHY (as SQL\_C\_BINARY) | Hex-encoded ASCII string | Raw binary bytes | 

The `COLUMN_SIZE` values returned by `SQLColumns` also changed for `GEOMETRY`, `GEOGRAPHY`, and `SUPER` data types, which now return NULL to indicate unsized columns per the ODBC specification. Applications that allocate buffers based on `COLUMN_SIZE` must handle NULL by using a default buffer size.

## Post-migration troubleshooting
<a name="odbc20-migrate-troubleshooting"></a>

The following table describes common issues you might encounter after migrating and how to resolve them.


| Symptom | Cause | What to do | 
| --- | --- | --- | 
| External tables not visible in schema browser | Spectrum and datashare tables are reported as EXTERNAL TABLE | Include EXTERNAL TABLE in your SQLTables type filter, or set EnableTableTypes to 0 to normalize the detailed table types into the generic TABLE and VIEW types. | 
| pyodbc errors on interval columns | pyodbc does not support ODBC interval types | Cast intervals to VARCHAR in queries. | 
| Character data displays as unexpected characters (mojibake) | UseUnicode default changed to false. Applications expecting wide-character (UTF-16) data might misinterpret narrow-character bytes as wide pairs, producing garbled output. The data itself is unchanged. | Set UseUnicode=true in your DSN, or update your application to bind columns as SQL\_C\_CHAR instead of SQL\_C\_WCHAR. | 
| Long-running queries return timeout errors | SQL\_ATTR\_QUERY\_TIMEOUT is now enforced. ODBC 1.x silently ignored this setting. | Increase or remove QueryTimeout from your DSN, or set SQL\_ATTR\_QUERY\_TIMEOUT to 0 in your application. | 
| Setting SQL\_ATTR\_CURRENT\_CATALOG returns HY011 | The attribute cannot be set on an open connection. Switching databases on an open connection is not supported. | Set the attribute before connecting, or close and reopen the connection on the target database. | 
| Connection hangs in dual-stack environments | Limitation in versions <= 2.1.16 | Upgrade to 2.1.17 or later. | 
| Error message parsing returns unexpected results | Message format changed; SQLSTATE codes unchanged | Parse SQLSTATE codes instead of message text. | 
| Data-at-execution parameter binding behaves differently | SQL\_NEED\_LONG\_DATA\_LEN changed from FALSE to TRUE; applications using SQL\_DATA\_AT\_EXEC must now provide the total data length up front | Set the length value in StrLen\_or\_IndPtr when binding SQL\_DATA\_AT\_EXEC parameters. | 
| Driver logs are not generated | LogLevel and LogPath must be in the [ODBC] global section of odbc.ini, not in individual DSN sections | Move logging settings from your DSN to the [ODBC] section. | 

## Upgrading from an older ODBC 2.x version
<a name="odbc20-migrate-upgrade-2x"></a>

If you are already running an older ODBC 2.x version, upgrade to the latest release. For a complete list of enhancements and bug fixes across all versions, see the [Amazon Redshift ODBC driver change log](https://github.com/aws/amazon-redshift-odbc-driver/blob/main/CHANGELOG.md) on GitHub.

## More information
<a name="odbc20-migrate-more-info"></a>
+ [Configuring a connection for ODBC driver version 2.x for Amazon Redshift](odbc20-install.md)
+ [ODBC driver options](odbc20-configuration-options.md)
+ [Amazon Redshift ODBC driver change log](https://github.com/aws/amazon-redshift-odbc-driver/blob/main/CHANGELOG.md)
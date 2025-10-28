# Migrate to the ODBC 2.x driver

Because most Athena ODBC 2.x connection parameters are backwardly compatible with the ODBC
1.x driver, you can reuse most of your existing connection string with the Athena ODBC 2.x
driver. However, the following connection parameters require modifications.

## Log level

While the current ODBC driver provides a range of available logging options, starting
from `LOG_OFF (0)` to `LOG_TRACE (6)`, the Amazon Athena ODBC driver
has only two values: 0 (disabled) and 1 (enabled).

For more information about logging the ODBC 2.x driver, see [Logging options](odbc-v2-driver-logging-options.md "odbc-v2-driver-logging-options.md").

|                               | ODBC 1.x driver                         | ODBC 2.x driver            |
| ----------------------------- | --------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connection string name**    | `LogLevel`                              | `LogLevel`                 |
| **Parameter type**            | Optional                                | Optional                   |
| **Default value**             | `0`                                     | `0`                        |
| **Possible values**           | `0-6`                                   | `0,1`                      |
| **Connection string example** | `LogLevel=6;`                           | `LogLevel=1;`              | ## MetadataRetrievalMethod The current ODBC driver provides several options for retrieving the metadata from Athena. The Amazon Athena ODBC driver deprecates the `MetadataRetrievalMethod` and always uses the Amazon Athena API to extract metadata. Athena introduces the flag `QueryExternalCatalogs` for querying external catalogs. To query external catalogs with the current ODBC driver, set `MetadataRetrievalMethod` to `ProxyAPI`. To query external catalogs with the Athena ODBC driver, set `QueryExternalCatalogs` to `1`.                                                                                                                                                                                                                                                                                              |
|                               | ODBC 1.x driver                         | ODBC 2.x driver            |
| ---                           | ---                                     | ---                        |
| **Connection string name**    | `MetadataRetrievalMethod`               | `QueryExternalCatalogs`    |
| **Parameter type**            | Optional                                | Optional                   |
| **Default value**             | `Auto`                                  | `0`                        |
| **Possible values**           | `Auto`, `AWS Glue`, `ProxyAPI`, `Query` | `0`,`1`                    |
| **Connection string example** | `MetadataRetrievalMethod=ProxyAPI;`     | `QueryExternalCatalogs=1;` | ## Connection test When you test an ODBC 1.x driver connection, the driver runs a `SELECT 1` query that generates two files in your Amazon S3 bucket: one for the result set, and one for the metadata. The test connection is charged according to the [Amazon Athena Pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/") policy. When you test an ODBC 2.x driver connection, the driver calls the [GetWorkGroup](../APIReference/API_GetWorkGroup.md "../APIReference/API_GetWorkGroup.md") Athena API action. The call uses the authentication type and corresponding credentials provider that you specified to retrieve the credentials. There is no charge for the connection test when you use the ODBC 2.x driver, and the test does not generate query results in your Amazon S3 bucket. |

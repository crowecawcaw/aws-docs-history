# Advanced options

## Fetch size

The maximum number of results (rows) to return in this request. For parameter
information, see [GetQuery MaxResults](../APIReference/API_GetQueryResults.md#athena-GetQueryResults-request-MaxResults "../APIReference/API_GetQueryResults.md#athena-GetQueryResults-request-MaxResults"). For the streaming API, the maximum value is 10000000.

| **Connection string name** | **Parameter type** | **Default value**                                 | **Connection string example** |
| -------------------------- | ------------------ | ------------------------------------------------- | ----------------------------- |
| RowsToFetchPerBlock        | Optional           | `1000` for non-streaming<br>`20000` for streaming | `RowsToFetchPerBlock=20000;`  |

## Result

fetcher

The default result fetcher downloads query results directly from Amazon S3 without going
through the Athena API operations. When it detects situations where direct S3 download is
not possible, it automatically falls back to using the
`GetQueryResultsStream` API operation. For example, this happens when
query results are encrypted with the `CSE_KMS` option.

Using the `auto` fetcher is recommended in most situations. However, if
your IAM policies, or S3 bucket policies use the `s3:CalledVia` condition to
limit access to S3 objects to requests from Athena, the auto fetcher first attempts to
download the results from S3 and then falls back to using the
`GetQueryResultsStream`. In this situation, you might want to set the
`ResultFetcher` to `GetQueryResultsStream` to avoid an extra
API call.

###### Note

The driver still recognizes the Enable streaming API
(`UseResultsetStreaming=1;`) and Enable S3 fetcher
(`EnableS3Fetcher=1;`) parameters. However, we encourage you to use
`ResultFetcher` parameter for better experience.

| **Connection string name** | **Parameter type** | **Default value** | **Possible values**                                         | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------------------------------------- | ----------------------------- |
| ResultFetcher              | Optional           | `auto`            | `auto`, `S3`, `GetQueryResults`,<br>`GetQueryResultsStream` | `ResultFetcher=auto`          |

## Enable result

reuse

Specifies if previous query results can be reused when the query is run. For parameter
information, see ResultReuseByAgeConfiguration.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| EnableResultReuse          | Optional           | `0`               | `EnableResultReuse=1;`        |

## Result reuse

maximum age

Specifies, in minutes, the maximum age of a previous query result that Athena should
consider for reuse. For parameter information, see [ResultReuseByAgeConfiguration](../APIReference/API_ResultReuseByAgeConfiguration.md "../APIReference/API_ResultReuseByAgeConfiguration.md").

| **Connection string name**  | **Parameter type** | **Default value** | **Connection string example**     |
| --------------------------- | ------------------ | ----------------- | --------------------------------- |
| ReusedResultMaxAgeInMinutes | Optional           | `60`              | `ReusedResultMaxAgeInMinutes=90;` |

## Use multiple

S3 threads

Fetches data from Amazon S3 using multiple threads. When this option is enabled, the result
file stored in the Amazon S3 bucket is fetched in parallel using multiple threads.

Enable this option only if you have good network bandwidth. For example, in our
measurements on an EC2 [c5.2xlarge](https://aws.amazon.com/ec2/instance-types/c5/ "https://aws.amazon.com/ec2/instance-types/c5/") instance, a single-threaded S3 client reached 1 Gbps, while
multiple-threaded S3 clients reached 4 Gbps of network throughput.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| UseMultipleS3Threads       | Optional           | `0`               | `UseMultipleS3Threads=1;`     |

## Use

single catalog and schema

By default, the ODBC driver queries Athena to get the list of available catalogs and
schemas. This option forces the driver to use the catalog and schema specified by the
ODBC Data Source Administrator configuration dialog box or connection parameters.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**  |
| -------------------------- | ------------------ | ----------------- | ------------------------------ |
| UseSingleCatalogAndSchema  | Optional           | `0`               | `UseSingleCatalogAndSchema=1;` |

## Use query to

list tables

For `LAMBDA` catalog types, enables the ODBC driver to submit a [SHOW TABLES](show-tables.md "show-tables.md") query to get a list of available
tables. This setting is the default. If this parameter is set to 0, the ODBC driver uses
the Athena [ListTableMetadata](../APIReference/API_ListTableMetadata.md "../APIReference/API_ListTableMetadata.md") API to get a list of available tables. Note that, for
`LAMBDA` catalog types, using `ListTableMetadata` leads to
performance regression.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| UseQueryToListTables       | Optional           | `1`               | `UseQueryToListTables=1;`     |

## Use WCHAR

for string types

By default, the ODBC driver uses `SQL_CHAR` and `SQL_VARCHAR`
for Athena the string data types `char`, `varchar`,
`string`, `array`, `map<>`,
`struct<>`, and `row`. Setting this parameter to
`1` forces the driver to use `SQL_WCHAR` and
`SQL_WVARCHAR` for string data types. Wide character and wide variable
character types are used to ensure that characters from different languages can be
stored and retrieved correctly.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| UseWCharForStringTypes     | Optional           | `0`               | `UseWCharForStringTypes=1;`   |

## Query external

catalogs

Specifies if the driver needs to query external catalogs from Athena. For more
information, see [Migrate to the ODBC 2.x driver](odbc-v2-driver-migrating.md "odbc-v2-driver-migrating.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| QueryExternalCatalogs      | Optional           | `0`               | `QueryExternalCatalogs=1;`    |

## Verify SSL

Controls whether to verify SSL certificates when you use the AWS SDK. This value is
passed to `ClientConfiguration.verifySSL` parameter. For more information,
see [AWS Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| VerifySSL                  | Optional           | `1`               | `VerifySSL=0;`                |

## S3 result block

size

Specifies, in bytes, the size of the block to download for a single Amazon S3 [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md")
API request. The default value is 67108864 (64 MB). The minimum and maximum values
allowed are 10485760 (10 MB) and 2146435072 (about 2 GB).

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**  |
| -------------------------- | ------------------ | ----------------- | ------------------------------ |
| S3ResultBlockSize          | Optional           | `67108864`        | `S3ResultBlockSize=268435456;` |

## String column

length

Specifies the column length for columns with the `string` data type.
Because Athena uses the [Apache Hive string data type](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-StringsstringStrings "https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Types#LanguageManualTypes-StringsstringStrings"), which does not have defined precision, the
default length reported by Athena is 2147483647 (`INT_MAX`). Because BI tools
usually pre-allocate memory for columns, this can lead to high memory consumption. To
avoid this, the Athena ODBC driver limits the reported precision for columns of the
`string` data type and exposes the `StringColumnLength`
connection parameter so that the default value can be changed.

| Connection string name | Parameter type | Default value | Connection string example   |
| ---------------------- | -------------- | ------------- | --------------------------- |
| StringColumnLength     | Optional       | 255           | `StringColumnLength=65535;` |

## Complex

type column length

Specifies the column length for columns with complex data types like `map`,
`struct`, and `array`. Like [StringColumnLength](#odbc-v2-driver-advanced-options-string-column-length "#odbc-v2-driver-advanced-options-string-column-length"), Athena reports 0 precision for columns with complex data
types. The Athena ODBC driver sets the default precision for columns with complex data
types and exposes the `ComplexTypeColumnLength` connection parameter so that
the default value can be changed.

| Connection string name  | Parameter type | Default value | Connection string example         |
| ----------------------- | -------------- | ------------- | --------------------------------- |
| ComplexTypeColumnLength | Optional       | 65535         | `ComplexTypeColumnLength=123456;` |

## Trusted CA

certificate

Instructs the HTTP client where to find your SSL certificate trust store. This value
is passed to the `ClientConfiguration.caFile` parameter. For more
information, see [AWS Client
configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value**    | **Connection string example**                                                    |
| -------------------------- | ------------------ | -------------------- | -------------------------------------------------------------------------------- |
| TrustedCerts               | Optional           | `%INSTALL_PATH%/bin` | `TrustedCerts=C:\\Program Files\\Amazon Athena ODBC<br>Driver\\bin\\cacert.pem;` |

## Min poll

period

Specifies the minimum value in milliseconds to wait before polling Athena for query
execution status.

| **Connection string name**       | **Parameter type** | **Default value** | **Connection string example**           |
| -------------------------------- | ------------------ | ----------------- | --------------------------------------- |
| MinQueryExecutionPollingInterval | Optional           | `100`             | `MinQueryExecutionPollingInterval=200;` |

## Max poll

period

Specifies the maximum value in milliseconds to wait before polling Athena for the query
execution status.

| **Connection string name**       | **Parameter type** | **Default value** | **Connection string example**            |
| -------------------------------- | ------------------ | ----------------- | ---------------------------------------- |
| MaxQueryExecutionPollingInterval | Optional           | `60000`           | `MaxQueryExecutionPollingInterval=1000;` |

## Poll

multiplier

Specifies the factor for increasing the poll period. By default, polling begins with
the value of min poll period and doubles with each poll until it reaches the value of
max poll period.

| **Connection string name**              | **Parameter type** | **Default value** | **Connection string example**                |
| --------------------------------------- | ------------------ | ----------------- | -------------------------------------------- |
| QueryExecutionPollingIntervalMultiplier | Optional           | `2`               | `QueryExecutionPollingIntervalMultiplier=2;` |

## Max poll

duration

Specifies the maximum value in milliseconds that a driver can poll Athena for query
execution status.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| MaxPollDuration            | Optional           | `1800000`         | `MaxPollDuration=1800000;`    |

## Connection

timeout

The amount of time (in milliseconds) that the HTTP connection waits to establish a
connection. This value is set for `ClientConfiguration.connectTimeoutMs`
Athena client. If not specified, the curl default value is used. For information about
connection parameters, see [Client
Configuration](../../../sdk-for-java/v1/developer-guide/section-client-configuration.md "../../../sdk-for-java/v1/developer-guide/section-client-configuration.md") in the _AWS SDK for Java Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| ConnectionTimeout          | Optional           | `0`               | `ConnectionTimeout=2000;`     |

## Request

timeout

Specifies the socket read timeout for HTTP clients. This value is set for the
`ClientConfiguration.requestTimeoutMs` parameter of the Athena client. For
parameter information, see [Client
Configuration](../../../sdk-for-java/v1/developer-guide/section-client-configuration.md "../../../sdk-for-java/v1/developer-guide/section-client-configuration.md") in the _AWS SDK for Java Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| RequestTimeout             | Optional           | `10000`           | `RequestTimeout=30000;`       |

# Advanced connection

parameters

The following sections describe the advanced connection parameters for the JDBC 3.x
driver.

###### Topics

- [Result encryption
  parameters](#jdbc-v3-driver-result-encryption-parameters "#jdbc-v3-driver-result-encryption-parameters")
- [Result fetching
  parameters](#jdbc-v3-driver-result-fetching-parameters "#jdbc-v3-driver-result-fetching-parameters")
- [Result configuration parameters](#jdbc-v3-driver-result-config "#jdbc-v3-driver-result-config")
- [Query result reuse
  parameters](#jdbc-v3-driver-query-result-reuse-parameters "#jdbc-v3-driver-query-result-reuse-parameters")
- [Query execution
  polling parameters](#jdbc-v3-driver-query-execution-polling-parameters "#jdbc-v3-driver-query-execution-polling-parameters")
- [Endpoint override
  parameters](#jdbc-v3-driver-endpoint-override-parameters "#jdbc-v3-driver-endpoint-override-parameters")
- [Proxy configuration
  parameters](#jdbc-v3-driver-proxy-configuration-parameters "#jdbc-v3-driver-proxy-configuration-parameters")
- [Logging parameters](#jdbc-v3-driver-logging-parameters "#jdbc-v3-driver-logging-parameters")
- [Application name](#jdbc-v3-driver-application-name "#jdbc-v3-driver-application-name")
- [Connection test](#jdbc-v3-driver-connection-test "#jdbc-v3-driver-connection-test")
- [Number of retries](#jdbc-v3-driver-number-of-retries "#jdbc-v3-driver-number-of-retries")
- [Network timeout](#jdbc-v3-driver-networktimeoutmillis "#jdbc-v3-driver-networktimeoutmillis")

## Result encryption

parameters

Note the following points:

- The AWS KMS Key must be specified when `EncryptionOption` is
  `SSE_KMS` or `CSE_KMS`.
- The AWS KMS Key cannot be specified when `EncryptionOption` is not
  specified or when `EncryptionOption` is `SSE_S3`.

### Encryption option

The type of encryption to be used for query results as they are stored in Amazon S3.
For information about query result encryption, see [EncryptionConfiguration](../APIReference/API_EncryptionConfiguration.md "../APIReference/API_EncryptionConfiguration.md") in the
_Amazon Athena API Reference_.

| Parameter name   | Alias                          | Parameter type | Default value | Possible values          |
| ---------------- | ------------------------------ | -------------- | ------------- | ------------------------ |
| EncryptionOption | S3OutputEncOption (deprecated) | Optional       | none          | SSE_S3, SSE_KMS, CSE_KMS |

### KMS Key

The KMS key ARN or ID, if `SSE_KMS` or `CSE_KMS` is chosen
as the encryption option. For more information, see [EncryptionConfiguration](../APIReference/API_EncryptionConfiguration.md "../APIReference/API_EncryptionConfiguration.md") in the
_Amazon Athena API Reference_.

| Parameter name | Alias                          | Parameter type | Default value |
| -------------- | ------------------------------ | -------------- | ------------- |
| KmsKey         | S3OutputEncKMSKey (deprecated) | Optional       | none          |

## Result fetching

parameters

### Result fetcher

The fetcher that will be used to download query results.

The default result fetcher, `auto`, downloads query results directly
from Amazon S3 without using the Athena APIs. When direct S3 download is not possible,
like when query results are encrypted with the `CSE_KMS` option, it
automatically falls back to use the `GetQueryResultsStream` API.

Using the `auto` fetcher is recommended in most situations. If your
IAM policies, or S3 bucket policies use the [s3:CalledVia](security-iam-athena-calledvia.md "security-iam-athena-calledvia.md") condition to limit
access to S3 objects requests from Athena, the `auto` fetcher first
attempts to download the results from S3 and then falls back to use the
`GetQueryResultsStream` API. In this situation, you can set the
ResultFetcher to `GetQueryResultsStream` to avoid an extra API
call.

| Parameter name | Alias | Parameter type | Default value | Possible values                                  |
| -------------- | ----- | -------------- | ------------- | ------------------------------------------------ |
| ResultFetcher  | none  | Optional       | auto          | auto, S3, GetQueryResults, GetQueryResultsStream |

### Fetch size

The value of this parameter is used as the minimum for internal buffers and as the
target page size when fetching results. The value 0 (zero) means that the driver
should use its defaults as described below. The maximum value is 1,000,000.

| Parameter name | Alias                            | Parameter type | Default value |
| -------------- | -------------------------------- | -------------- | ------------- |
| FetchSize      | RowsToFetchPerBlock (deprecated) | Optional       | 0             |

- The `GetQueryResults` fetcher will always use a page size of
  1,000, which is the maximum value supported by the API call. When the fetch
  size is higher than 1,000, multiple successive API calls are made to fill
  the buffer above the minimum.
- The `GetQueryResultsStream` fetcher will use the configured
  fetch size as the page size, or 10,000 by default.
- The `S3` fetcher will use the configured fetch size as the page
  size, or 10,000 by default.

## Result configuration parameters

### Expected bucket owner

The account ID of the expected s3 bucket owner. If the account ID that you provide
does not match the actual owner of the bucket, the request fails. For more
information about verifying s3 bucket owner, see [Verifying bucket ownership](../../../AmazonS3/latest/userguide/bucket-owner-condition.md#bucket-owner-condition-use "../../../AmazonS3/latest/userguide/bucket-owner-condition.md#bucket-owner-condition-use").

| Parameter name      | Alias | Parameter type | Default value |
| ------------------- | ----- | -------------- | ------------- |
| ExpectedBucketOwner | none  | Optional       | none          |

### Acl option

Indicates that an Amazon S3 canned ACL should be set to control ownership of stored
query results. For more information about `AclOption`, see [AclConfiguration](../APIReference/API_AclConfiguration.md "../APIReference/API_AclConfiguration.md").

| Parameter name | Alias | Parameter type | Default value | Possible values           |
| -------------- | ----- | -------------- | ------------- | ------------------------- |
| AclOption      | none  | Optional       | none          | BUCKET_OWNER_FULL_CONTROL |

## Query result reuse

parameters

### Enable result reuse

Specifies whether previous results for the same query can be reused when a query
is run. For information about query result reuse, see [ResultReuseByAgeConfiguration](../APIReference/API_ResultReuseByAgeConfiguration.md "../APIReference/API_ResultReuseByAgeConfiguration.md").

| Parameter name         | Alias | Parameter type | Default value |
| ---------------------- | ----- | -------------- | ------------- |
| EnableResultReuseByAge | none  | Optional       | FALSE         |

### Result reuse max age

The maximum age, in minutes, of a previous query result that Athena should consider
for reuse. For information about result reuse max age, see [ResultReuseByAgeConfiguration](../APIReference/API_ResultReuseByAgeConfiguration.md "../APIReference/API_ResultReuseByAgeConfiguration.md").

| Parameter name             | Alias | Parameter type | Default value |
| -------------------------- | ----- | -------------- | ------------- |
| MaxResultReuseAgeInMinutes | none  | Optional       | 60            |

## Query execution

polling parameters

### Minimum

query execution polling interval

The minimum time, in milliseconds, to wait before polling Athena for the query
execution status.

| Parameter name                         | Alias                                         | Parameter type | Default value |
| -------------------------------------- | --------------------------------------------- | -------------- | ------------- |
| MinQueryExecutionPollingIntervalMillis | MinQueryExecutionPollingInterval (deprecated) | Optional       | 100           |

### Maximum

query execution polling interval

The maximum time, in milliseconds, to wait before polling Athena for the query
execution status.

| Parameter name                         | Alias                                         | Parameter type | Default value |
| -------------------------------------- | --------------------------------------------- | -------------- | ------------- |
| MaxQueryExecutionPollingIntervalMillis | MaxQueryExecutionPollingInterval (deprecated) | Optional       | 5000          |

### Query

execution polling interval multiplier

The factor for increasing the polling period. By default, polling will begin with
the value for `MinQueryExecutionPollingIntervalMillis` and double with
each poll until it reaches the value for
`MaxQueryExecutionPollingIntervalMillis`.

| Parameter name                          | Alias | Parameter type | Default value |
| --------------------------------------- | ----- | -------------- | ------------- |
| QueryExecutionPollingIntervalMultiplier | none  | Optional       | 2             |

## Endpoint override

parameters

### Athena endpoint

override

The endpoint that the driver will use to make API calls to Athena.

Note the following points:

- If the `https://` or `http://` protocols are not
  specified in the provided URL, the driver inserts the `https://`
  prefix.
- If this parameter is not specified, the driver uses a default
  endpoint.

| Parameter name | Alias                         | Parameter type | Default value |
| -------------- | ----------------------------- | -------------- | ------------- |
| AthenaEndpoint | EndpointOverride (deprecated) | Optional       | none          |

### Athena

streaming service endpoint override

The endpoint that the driver will use to download query results when it uses the
Athena streaming service. The Athena streaming service is available on port 444.

Note the following points:

- If the `https://` or `http://` protocols are not
  specified in the provided URL, the driver inserts the `https://`
  prefix.
- If a port is not specified in the provided URL, the driver inserts the
  streaming service port 444.
- If the `AthenaStreamingEndpoint` parameter is not specified,
  the driver uses the `AthenaEndpoint` override. If neither the
  `AthenaStreamingEndpoint` nor the `AthenaEndpoint`
  override is specified, the driver uses a default streaming endpoint.

| Parameter name          | Alias                                  | Parameter type | Default value |
| ----------------------- | -------------------------------------- | -------------- | ------------- |
| AthenaStreamingEndpoint | StreamingEndpointOverride (deprecated) | Optional       | none          |

### LakeFormation endpoint override

The endpoint that the driver will use for the Lake Formation service when using the AWS Lake Formation
[AssumeDecoratedRoleWithSAML](../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md "../../../lake-formation/latest/APIReference/API_AssumeDecoratedRoleWithSAML.md") API to retrieve temporary credentials. If
this parameter is not specified, the driver uses a default Lake Formation endpoint.

Note the following points:

- If the `https://` or `http://` protocols are not
  specified in the provided URL, the driver inserts the `https://`
  prefix.

| Parameter name        | Alias                           | Parameter type | Default value |
| --------------------- | ------------------------------- | -------------- | ------------- |
| LakeFormationEndpoint | LfEndpointOverride (deprecated) | Optional       | none          |

### S3 endpoint

override

The endpoint that the driver will use to download query results when it uses the
Amazon S3 fetcher. If this parameter is not specified, the driver uses a default Amazon S3
endpoint.

Note the following points:

- If the `https://` or `http://` protocols are not
  specified in the provided URL, the driver inserts the `https://`
  prefix.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| S3Endpoint     | None  | Optional       | none          |

### STS endpoint

override

The endpoint that the driver will use for the AWS STS service when using the AWS STS
[AssumeRoleWithSAML](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") API to retrieve temporary credentials. If this
parameter is not specified, the driver uses a default AWS STS endpoint.

Note the following points:

- If the `https://` or `http://` protocols are not
  specified in the provided URL, the driver inserts the `https://`
  prefix.

| Parameter name | Alias                           | Parameter type | Default value |
| -------------- | ------------------------------- | -------------- | ------------- |
| StsEndpoint    | StsEndpointOverride(deprecated) | Optional       | none          |

### SSO OIDC endpoint override

The endpoint that the driver will use when using
`ClientConfiguration.endpointOverride` to override the default HTTP
endpoint for SSO OIDC client. For more information, see [ClientConfiguration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md").

| Parameter name          | Alias | Parameter type | Default value |
| ----------------------- | ----- | -------------- | ------------- |
| SSOOIDCEndpointOverride |       | Optional       | none          |

### SSO Admin endpoint override

The endpoint that the driver will use when using
`ClientConfiguration.endpointOverride` to override the default HTTP
endpoint for SSO Admin client. For more information, see [ClientConfiguration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md").

| Parameter name           | Alias | Parameter type | Default value |
| ------------------------ | ----- | -------------- | ------------- |
| SSOAdminEndpointOverride |       | Optional       | none          |

## Proxy configuration

parameters

### Proxy host

The URL of the proxy host. Use this parameter if you require Athena requests to go
through a proxy.

###### Note

Make sure to include the protocol `https://` or
`http://` at the beginning of the URL for `ProxyHost`.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| ProxyHost      | none  | Optional       | none          |

### Proxy port

The port to be used on the proxy host. Use this parameter if you require Athena
requests to go through a proxy.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| ProxyPort      | none  | Optional       | none          |

### Proxy username

The username to authenticate on the proxy server. Use this parameter if you
require Athena requests to go through a proxy.

| Parameter name | Alias                 | Parameter type | Default value |
| -------------- | --------------------- | -------------- | ------------- |
| ProxyUsername  | ProxyUID (deprecated) | Optional       | none          |

### Proxy password

The password to authenticate on the proxy server. Use this parameter if you
require Athena requests to go through a proxy.

| Parameter name | Alias                 | Parameter type | Default value |
| -------------- | --------------------- | -------------- | ------------- |
| ProxyPassword  | ProxyPWD (deprecated) | Optional       | none          |

### Proxy-exempt hosts

A set of host names that the driver connects to without using a proxy when
proxying is enabled (that is, when the `ProxyHost` and
`ProxyPort` connection parameters are set). The hosts should be
separated by the pipe (`|`) character (for example,
`host1.com|host2.com`).

| Parameter name   | Alias         | Parameter type | Default value |
| ---------------- | ------------- | -------------- | ------------- |
| ProxyExemptHosts | NonProxyHosts | Optional       | none          |

### Proxy enabled

for identity providers

Specifies whether a proxy should be used when the driver connects to an identity
provider.

| Parameter name     | Alias          | Parameter type | Default value |
| ------------------ | -------------- | -------------- | ------------- |
| ProxyEnabledForIdP | UseProxyForIdP | Optional       | FALSE         |

## Logging parameters

This section describes parameters related to logging.

### Log level

Specifies the level for the driver logging. Nothing is logged unless the
`LogPath` parameter is also set.

###### Note

We recommend setting only the `LogPath` parameter unless you have
special requirements. Setting only the `LogPath` parameter enables
logging and uses the default `TRACE` log level. The
`TRACE` log level provides the most detailed logging.

| Parameter name | Alias | Parameter type | Default value | Possible values                        |
| -------------- | ----- | -------------- | ------------- | -------------------------------------- |
| LogLevel       | none  | Optional       | TRACE         | _OFF, ERROR, WARN, INFO, DEBUG, TRACE_ |

### Log path

The path to a directory on the computer that runs the driver where driver logs
will be stored. A log file with a unique name will be created within the specified
directory. If set, enables driver logging.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| LogPath        | none  | Optional       | none          |

## Application name

The name of the application that uses the driver. If a value for this parameter is
specified, the value is included in the user agent string of the API calls that the
driver makes to Athena.

###### Note

You can also set the application name by calling `setApplicationName`
on the `DataSource` object.

| Parameter name  | Alias | Parameter type | Default value |
| --------------- | ----- | -------------- | ------------- |
| ApplicationName | none  | Optional       | none          |

## Connection test

If set to `TRUE`, the driver performs a connection test each time a JDBC
connection is created, even if a query is not executed on the connection.

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| ConnectionTest | none  | Optional       | TRUE          |

###### Note

A connection test submits a `SELECT 1` query to Athena to verify that
the connection has been configured correctly. This means that two files will be
stored in Amazon S3 (the result set and metadata), and additional charges can apply in
accordance with the [Amazon Athena
pricing](https://aws.amazon.com/athena/pricing "https://aws.amazon.com/athena/pricing") policy.

## Number of retries

The maximum number of times the driver should resend a retriable request to
Athena.

| Parameter name | Alias                      | Parameter type | Default value |
| -------------- | -------------------------- | -------------- | ------------- |
| NumRetries     | MaxErrorRetry (deprecated) | Optional       | none          |

## Network timeout

The network timeout controls the amount of time that the driver waits for a network
connection to be established. This includes the time it takes to send API requests. In
rare circumstances, it may be useful to change the network timeout. For example, you
might want to increase the timeout for long garbage collection pauses. Setting this
connection parameter is equivalent to using the `setNetworkTimeout` method on
a `Connection` object.

| Parameter name       | Alias | Parameter type | Default value |
| -------------------- | ----- | -------------- | ------------- |
| NetworkTimeoutMillis | none  | Optional       | none          |

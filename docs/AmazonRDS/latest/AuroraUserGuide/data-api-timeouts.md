# Controlling Data API timeout behavior

All calls to the Data API are synchronous. Suppose that you perform a Data API operation that runs a SQL statement
such as `INSERT` or `CREATE TABLE`. If the Data API call returns successfully,
the SQL processing is finished when the call returns.

By default, the Data API cancels an operation and returns a timeout error if the operation doesn't
finish processing within 45 seconds. In that case, the data isn't inserted, the table isn't created,
and so on.

You can use the Data API to perform long-running operations that can't complete within 45 seconds.
If you expect that an operation such as a bulk `INSERT` or a DDL operation on a large table
takes longer than 45 seconds, you can specify the `continueAfterTimeout` parameter for the
`ExecuteStatement` operation.
Your application still receives the timeout error. However, the operation continues running and
isn't canceled. For an example, see
[Running a SQL transaction](data-api.calling.md#data-api.calling.java.run-transaction "data-api.calling.md#data-api.calling.java.run-transaction").

If the AWS SDK for your programming language has its own timeout period for API calls or HTTP socket connections,
make sure that all such timeout periods are more than 45 seconds.
For some SDKs, the timeout period is less than 45 seconds by default.
We recommend setting any SDK-specific or client-specific timeout periods to at least one minute.
Doing so avoids the possibility that your application receives a timeout error while the
Data API operation still completes successfully. That way, you can be sure whether to retry the operation or not.

For example, suppose that the SDK returns a timeout error to your application, but the Data API operation still
completes within the Data API timeout interval. In that case, retrying the operation might insert duplicate data
or otherwise produce incorrect results. The SDK might retry the operation automatically, causing incorrect data
without any action from your application.

The timeout interval is especially important for the Java 2 SDK. In that SDK, the API call timeout
and the HTTP socket timeout are both 30 seconds by default. Here is an example of setting those
timeouts to a higher value:

```
public RdsDataClient createRdsDataClient() {
    return RdsDataClient.builder()
        .region(Region.US_EAST_1) // Change this to your desired Region
        .overrideConfiguration(createOverrideConfiguration())
        .httpClientBuilder(createHttpClientBuilder())
        .credentialsProvider(defaultCredentialsProvider()) // Change this to your desired credentials provider
        .build();
}

private static ClientOverrideConfiguration createOverrideConfiguration() {
    return ClientOverrideConfiguration.builder()
        .apiCallTimeout(Duration.ofSeconds(60))
        .build();
}

private HttpClientBuilder createHttpClientBuilder() {
    return ApacheHttpClient.builder() // Change this to your desired HttpClient
        .socketTimeout(Duration.ofSeconds(60));
}

```

Here is an equivalent example using the asynchronous data client:

```
public static RdsDataAsyncClient createRdsDataAsyncClient() {
    return RdsDataAsyncClient.builder()
        .region(Region.US_EAST_1) // Change this to your desired Region
        .overrideConfiguration(createOverrideConfiguration())
        .credentialsProvider(defaultCredentialsProvider())  // Change this to your desired credentials provider
        .build();
}

private static ClientOverrideConfiguration createOverrideConfiguration() {
    return ClientOverrideConfiguration.builder()
        .apiCallAttemptTimeout(Duration.ofSeconds(60))
        .build();
}

private HttpClientBuilder createHttpClientBuilder() {
    return NettyNioAsyncHttpClient.builder() // Change this to your desired AsyncHttpClient
        .readTimeout(Duration.ofSeconds(60));
}

```

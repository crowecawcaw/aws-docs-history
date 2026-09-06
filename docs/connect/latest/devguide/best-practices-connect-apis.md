

# Best practices for using Connect Customer APIs
<a name="best-practices-connect-apis"></a>

This topic provides guidance for using Connect Customer Describe and List APIs so you don't get unexpected 4xx errors for the response. It also explains how to configure your client Read APIs.

**Topics**
+ [Types of errors](#failure-types)
+ [Throttling in Connect Customer APIs](#throttling)
+ [How to configure your client Read API(s)](#configure-client-read-apis)
+ [How to make 2 TPS work for List APIs](#configure-client-list-apis)
+ [How to make 2 TPS work for Create/Update APIs](#configure-client-create-apis)
+ [Hitting a resource quota? Delete resources](#delete-unused-resources)
+ [How to request an increase to an API throttling quota](#request-quota-increase)
+ [Supported SDKs](#supported-sdks)

## Types of errors
<a name="failure-types"></a>

The Connect Customer APIs provide an HTTP interface. HTTP defines ranges of HTTP Status Codes for different types of error responses. 
+ Client errors are indicated by HTTP Status Code class of 4xx
+ Service errors are indicated by HTTP Status Code class of 5xx

In this reference guide, the documentation for each API has an **Errors** section that includes a brief discussion about HTTP status codes. We recommend looking there as part of your investigation when you get an error.

For information about the common errors returned by Connect Customer public APIs, see [Common Errors](https://docs.aws.amazon.com/connect/latest/APIReference/CommonErrors.html).

## Throttling in Connect Customer APIs
<a name="throttling"></a>

Throttling errors in Connect Customer public API(s) are defined by HTTP status code 429. This HTTP status code can be retried by the client based on their requirement. 

**Important**  
The throttling limits are defined for each API separately at the AWS account level, not for the individual Connect Customer instance.

To use any API for Connect Customer resources (such as users, queues, and routing profiles), you need the [ID/ARN for the Connect Customer instance](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html). 

 By default, Connect Customer limits the steady-state requests per second (RPS) across all APIs within an AWS account, per Region. It also limits the burst (that is, the maximum bucket size) across all APIs within an AWS account, per Region. 

In Connect Customer the burst limit represents the target maximum number of concurrent request submissions that APIs will fulfill before returning *429 Too Many Requests* error responses. 

For more information about throttling quotas, see [Connect Customer throttling quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#api-throttling-quotas). 

## How to configure your client Read API(s)
<a name="configure-client-read-apis"></a>

Your client configuration will vary based on number of resources that your API tries to describe/list per second.

In the following Java example, the number of retries is set to 3. This means after your Connect Customer client implementation experiences throttling, it retries for maximum of 3 times. Instead of retrying immediately and aggressively, the following snippet waits a specified amount of time (between 0 to max of 5 seconds as defined by maxBackoffTime parameter) between tries and uses [EqualJitterBackoffStrategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/backoff/EqualJitterBackoffStrategy.html). 

```
final class ClientBuilder {

    private static final int NUMBER_OF_RETRIES = 3;

    private static final RetryPolicy RETRY_POLICY =
            RetryPolicy.builder()
                    .numRetries(NUMBER_OF_RETRIES)
                    .retryCondition(RetryCondition.defaultRetryCondition())
                    .backoffStrategy(EqualJitterBackoffStrategy.builder()
                            .baseDelay(Duration.ofSeconds(1))
                            .maxBackoffTime(Duration.ofSeconds(5))
                            .build())
                    .build();

    public static ConnectClient getClient() {
        return ConnectClient.builder()
                .httpClient(LambdaWrapper.HTTP_CLIENT)
                .overrideConfiguration(ClientOverrideConfiguration.builder().retryPolicy(RETRY_POLICY).build())
                .build();
    }
}
```

When failures are caused by overload or contention, backing off often doesn't help as much as it seems like it should. This is because there's a correlation between failures and backing off/contention:
+ If all the failed calls back off to the same time, they cause contention or overload again when they are retried.

To address this, we recommend adding jitter. Jitter adds some amount of randomness to the backoff which spreads the retries around in time. For more information about how much jitter to add and the best ways to add it, see this AWS blog post: [Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/). 

For information about types of backoff strategies, see [Interface BackoffStrategy](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/retry/backoff/BackoffStrategy.html). 

## How to make 2 TPS work for List APIs when you have a large number of resources
<a name="configure-client-list-apis"></a>

There are two options: use List APIs with `maxResults` = 1,000, or use Search APIs as an alternative to List/Describe round trips. Both options are discussed here.

The List API of a particular Connect Customer resource supports a `maxResults` parameter as part of request body. List API(s) support a maximum of 1,000 results in single API call unless specified otherwise in the documentation.

The following example shows the `maxResults` of the [ListUsers](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListUsers.html) API.

```
String nextToken = null;
do {
    ListUsersRequest listUsersRequest = ListUsersRequest.builder()
            .instanceId({{your Connect Customer instanceId}})
            .maxResults(1000)
            .nextToken(nextToken)
            .build();
    ListUsersResponse response = client.listUsers(listUsersRequest);
    nextToken = response.nextToken();
    System.out.println(response.sdkHttpResponse().statusCode());
} while (nextToken != null);
```

If `nextToken` is returned, then more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 `InvalidToken` error.

### When to use Search APIs instead of List APIs
<a name="search-apis"></a>

We recommend you assess the speed of pulling details for 100 records at a time (the Search API limit) instead of pulling 1,000 IDs and doing Describe round trips. It's better to try using Search APIs instead of combination of List and Describe API for a specific resource.

Let's say you have a situation where you're listing specific resources in your Connect Customer instance and then call a Describe API on an individual resource. Instead, we recommend leveraging the Search API for that corresponding resource. Search APIs support several filters that can help to reduce response set as per requirement. 

## How to make 2 TPS work for Create/Update APIs when you have a large number of resources
<a name="configure-client-create-apis"></a>

There is a performance impact behind creating/updating resources at a default 2 TPS. For example, 100 resources can be created/updated with 2 TPS within 50 seconds. A 1,000 resources with this TPS would need nearly 8 minutes. Based on your use case, if the operation is impacting performance, contact Support and provide a business justification for your request to increase your throttling quota. See [How to request an increase to an API throttling quota](#request-quota-increase).

It is your responsibility to always implement the following best practices:
+ Check your logic and implement best practices to make your requests as efficient as possible. Check out [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) (AWS WA Tool) for processes that help measure your architecture using AWS best practices.
+ Test your requests and any custom processes *before adding them to production operations*.

## Hitting a resource quota? Delete unused / stale resources
<a name="delete-unused-resources"></a>

If you keep hitting the quota limit for a specific resource, we recommend deleting any unused or stale resources. You can find the Delete API for a resource on the resource-specific [Action pages](https://docs.aws.amazon.com/connect/latest/APIReference/actions-by-resource.html). These pages list all the APIs for a given resource.

## How to request an increase to an API throttling quota
<a name="request-quota-increase"></a>

**Important**  
We analyze all requests for quota increases and provide guidance for all queries.
We rarely approve requests if they apply to situations other than those listed below. 
For smaller increase requests, we can approve in hours. Larger increase requests take time to review, process, approve, and deploy. Depending on your specific implementation, your resource, and the size of quota that you want, a request can take up to 3 weeks. An extra-large worldwide increase can potentially take months. If you're increasing your quotas as part of a larger project, keep this information in mind and plan accordingly.

For instructions about how to use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home), see [Using the AWS Management Console to request an increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html#quota-console-increase).

In the Services Quotas console, open an Support case and provide the following information:

1. Have you implemented the best practices explained in the [ Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) topic of the *AWS SDKs and Tools Reference Guide*?

1. What is the performance impact without the requested limit increase? Provide some calculations.

1. What is the expected number of resources customer is trying to create/update/describe every second with the APIs? 

1. What is the new quota for the API that you want?

Include in your case if the following situation(s) apply:
+ It is a migration request and you need high TPS for a specific time range to configure your instance(s).
+ There are performance or business impacting usecases, such as handling huge call volume for peak season.
+ You have thousands of resources with multiple concurrent agents working at the same time which might increase the overall traffic from your contact center.

## Supported SDKs for all Connect Customer APIs
<a name="supported-sdks"></a>
+ [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/reference/connect/#cli-aws-connect) 
+ [AWS SDK for .NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Connect/NConnect.html) 
+ [AWS SDK for C\+\+](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-connect/html/namespace_aws_1_1_connect.html) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/api/service/connect/) 
+  [AWS SDK for Java V2](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/connect/ConnectClient.html) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-connect/) 
+ [AWS SDK for PHP V3](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-connect-2017-08-08.html) 
+  [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Connect/Client.html) 


# Request throttling for the Amazon RDS API
<a name="rds-api-throttling"></a>

Amazon RDS throttles API requests for each AWS account in each AWS Region. This helps the performance of the service and ensures fair usage for all Amazon RDS customers. Throttling ensures that requests to the Amazon RDS API don't exceed the maximum allowed API request limits. The request limits apply to API requests from any source, including the following.
+ Your own application code using an AWS SDK
+ A command line tool, such as the AWS CLI
+ The Amazon RDS console
+ A third-party tool that uses your account's credentials, such as an infrastructure-as-code or monitoring tool

If you use any Amazon RDS API operations and exceed the default limit for the number of calls per second, the Amazon RDS API issues an error like the following one.

ClientError: An error occurred (ThrottlingException) when calling the {{API\_name}} operation: Rate exceeded.

This error means that your account exceeded its API request limit. By default, you can make up to 300 requests in a burst and a sustained 12 requests per second. To avoid this error, retry the request with exponential backoff, reduce your request rate, or request a limit increase. For more information, see [Retries and exponential backoff](#rds-api-throttling-backoff), [Reduce the number of API requests](#rds-api-throttling-reduce), and [Request a limit increase](#rds-api-throttling-increase).

**Topics**
+ [How throttling is applied](#rds-api-throttling-how)
+ [Token bucket size and refill rate](#rds-api-throttling-limits)
+ [Retries and exponential backoff](#rds-api-throttling-backoff)
+ [Reduce the number of API requests](#rds-api-throttling-reduce)
+ [Identify the source of throttled requests](#rds-api-throttling-monitor)
+ [View your current API limits](#rds-api-throttling-view-limits)
+ [Request a limit increase](#rds-api-throttling-increase)

## How throttling is applied
<a name="rds-api-throttling-how"></a>

Amazon RDS uses a token bucket to throttle API requests. Understanding how the bucket works helps you predict when throttling occurs and plan your request rate.

Your account has a *bucket* that holds a number of *tokens*. Each request spends one token, and Amazon RDS adds tokens back at a steady rate. The number of tokens in the bucket is the number of requests you can make at that moment.

Your account has one bucket for each AWS Region, shared by all Amazon RDS API actions. Each request that you make removes one token from the bucket. Suppose the bucket size is 300 tokens. You can make up to 300 requests in one second. If you exceed 300 requests in a second, you are throttled and the remaining requests within that second fail.

Buckets automatically refill at a set rate. If the bucket is below its maximum capacity, Amazon RDS adds a set number of tokens back to it every second until it reaches its maximum capacity.

If the bucket is full when refill tokens arrive, the bucket discards them. The bucket can't hold more than its maximum number of tokens.

Suppose the bucket size is 300 tokens and the refill rate is 12 tokens per second. If you make 300 requests in one second, the bucket drops to zero (0) tokens.

The bucket then refills by 12 tokens every second. It reaches its maximum capacity of 300 tokens after 25 seconds if you make no requests during that time.

You don't need to wait for the bucket to be completely full before you can make API requests. You can use refill tokens as they are added to the bucket. If you deplete the bucket by making 300 requests in a second, you can continue to make 12 requests per second by using the refill tokens as they are added to the bucket. The bucket can refill to the maximum capacity only if you make fewer than 12 requests per second.

Amazon RDS separately limits requests that AWS services, such as AWS CloudFormation, make on your behalf. These requests don't consume tokens from your account's bucket.

## Token bucket size and refill rate
<a name="rds-api-throttling-limits"></a>

The following table shows the default API request throttling limits for each AWS account in each AWS Region.


| API actions | Bucket maximum capacity | Bucket refill rate (per second) | 
| --- | --- | --- | 
| All [Amazon RDS API actions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Operations.html) | 300 | 12 | 

These are the default limits. If AWS has increased the limits for your account, your limits are higher.

For more information about quotas on the number of Amazon RDS resources that you can create in your account, see [Quotas in Amazon RDS](CHAP_Limits.md#RDS_Limits.Limits). For more information about Amazon RDS service endpoints and quotas, see [Amazon Relational Database Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/rds-service.html) in the *Amazon Web Services General Reference*.

## Retries and exponential backoff
<a name="rds-api-throttling-backoff"></a>

Your application might need to retry an API request. For example:
+ To check for an update in the status of a resource, such as a DB instance that is being created or modified
+ To enumerate a large number of resources (for example, all your DB snapshots)
+ To retry a request after it fails with a server error (5xx) or a throttling error

However, for a client error (4xx) other than a throttling error, revise the request to correct the problem before trying the request again.

### Resource status changes
<a name="rds-api-throttling-backoff-status"></a>

Before you start polling to check for status updates, give the request time to potentially complete. For example, wait a few minutes before checking whether your DB instance is available. When you begin polling, use an appropriate sleep interval between successive requests to lower the rate of API requests. For best results, use an increasing or variable sleep interval.

Alternatively, you can use Amazon EventBridge to notify you of the status of your resources instead of polling. For example, you can receive an event when a DB instance becomes available or when a snapshot finishes. For more information, see [Creating a rule that triggers on an Amazon RDS event](rds-cloud-watch-events.md).

### Retries
<a name="rds-api-throttling-backoff-retries"></a>

When you need to poll or retry an API request, use an exponential backoff algorithm to calculate the sleep interval between requests. Wait progressively longer between retries. Set a maximum delay and a maximum number of retries. Add jitter (randomized delay) to prevent successive collisions. For implementation guidance, see [Timeouts, retries, and backoff with jitter on the AWS Builders' Library website](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).

Each AWS SDK implements automatic retry logic, and retries `ThrottlingException` errors by default. For more information, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide*.

## Reduce the number of API requests
<a name="rds-api-throttling-reduce"></a>

Because all API actions share one bucket, reducing requests from any caller frees capacity for every other caller in your account. Before requesting a limit increase, consider the following.

Cache responses  
Information returned by `Describe*` actions, such as `DescribeDBInstances` and `DescribeDBClusters`, usually changes infrequently. Cache the results and reuse them instead of calling the API every time you need the information.

Limit your request rate on the client side  
Shape your outbound request rate to stay below the sustained rate before sending requests, rather than relying on retries after throttling.

Replace polling with events  
Use Amazon EventBridge to be notified of resource state changes instead of repeatedly calling `Describe*` actions.

Request only what you need  
Specify an identifier or use the `Filters` parameter so that a `Describe*` action returns only the resources you are interested in, and page through large result sets with `MaxRecords` and `Marker`.

Spread out scheduled requests  
If many workers, scheduled jobs, or monitoring agents call the API at the same moment, add a random delay to each so that requests are spread over time instead of arriving in a burst.

## Identify the source of throttled requests
<a name="rds-api-throttling-monitor"></a>

AWS CloudTrail records every API request in your account. Each record shows you who made the request, which tool made it, and whether it succeeded. Use AWS CloudTrail to find which users, roles, or tools make most of your requests. For more information about AWS CloudTrail logging, see [Monitoring Amazon RDS API calls in AWS CloudTrail](logging-using-cloudtrail.md).

## View your current API limits
<a name="rds-api-throttling-view-limits"></a>

Service Quotas doesn't manage Amazon RDS API throttling limits, and they don't appear in the Service Quotas console. Unless AWS has increased the limits for your account, the default limits apply. If your account has received an increase and you don't know your current limits, open a support case to confirm them.

## Request a limit increase
<a name="rds-api-throttling-increase"></a>

You can request an increase for API throttling limits for your AWS account by opening a support case. Limit increases aren't self-service, and AWS doesn't approve them automatically. AWS reviews your request and your recent traffic before applying a new limit. Allow time for the review and for the new limit to take effect.

### Recommendations
<a name="rds-api-throttling-increase-recommendations"></a>

Consider the following recommendations before you request an increase.
+ Base your request on your measured peak request rate. AWS reviews your traffic pattern before approving an increase.
+ Prioritize increasing the bucket refill rate if you are throttled during sustained traffic. Increase the bucket maximum capacity if you are throttled during short bursts.
+ Spread out scheduled jobs or groups of workers that start at the same time before you request an increase. Spreading requests out usually resolves the throttling without a limit increase.
+ Submit requests for planned events, such as a migration or a large deployment, well before the event.

### Open a support case
<a name="rds-api-throttling-increase-case"></a>

If you still need a higher limit after reviewing the recommendations, [create a case in the AWS Support Center console](https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service). If you haven't created a case before, see [Creating support cases and case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.

To speed up the review, copy the following template into the case description. Replace {{account\_id}}, {{region}}, and the other values with your own information:

```
Please increase the Amazon RDS API throttling limits for my account.
Account ID(s): {{account_id}}
Region(s): {{region}}
Description: {{use_case}}
API actions: {{api_actions}}
Time window: {{time_window}}
Changes already made: {{changes_made}}
Requested limits:
    Bucket maximum capacity: {{current_bucket_capacity}} -> {{requested_bucket_capacity}}
    Bucket refill rate: {{current_refill_rate}} -> {{requested_refill_rate}}
```

The template uses the following values.

{{account\_id}}  
The AWS account ID, or IDs, that need the increase.

{{region}}  
The AWS Region, or Regions, where you are throttled.

{{use\_case}}  
Your use case and the tools that call the Amazon RDS API, such as your application, the AWS CLI, an infrastructure-as-code tool, or a monitoring agent.

{{api\_actions}}  
The Amazon RDS API actions that generate most of your requests.

{{time\_window}}  
A one-hour window, in UTC, when you saw peak throttling or usage. For a planned event, the planned start and end dates.

{{changes\_made}}  
Anything you've already tried to reduce requests, such as retries with exponential backoff, caching, or less frequent polling.

{{current\_bucket\_capacity}}, {{requested\_bucket\_capacity}}  
Your current and requested bucket maximum capacity (burst).

{{current\_refill\_rate}}, {{requested\_refill\_rate}}  
Your current and requested bucket refill rate, in requests per second (sustained).

The more context you provide about your traffic, the faster AWS can find the right limit for you.
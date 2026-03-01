# Using CloudWatch to monitor and log GraphQL API data

You can log and debug your GraphQL API using CloudWatch metrics and CloudWatch logs. These
tools enable developers to monitor performance, troubleshoot issues, and optimize their
GraphQL operations effectively.

CloudWatch metrics is a tool that provides a wide range of metrics to monitor API
performance and usage. These metrics fall into two main categories:

1. **General API Metrics**: These include
   `4XXError` and `5XXError` for tracking client and server
   errors, `Latency` for measuring response times, `Requests` for
   monitoring total API calls, and `TokensConsumed` for tracking resource
   usage.
2. **Real-time Subscription Metrics**: These metrics focus
   on WebSocket connections and subscription activities. They include metrics for
   connection requests, successful connections, subscription registrations, message
   publishing, and active connections and subscriptions.
   The guide also introduces Enhanced Metrics, which offer more granular data on resolver
   performance, data source interactions, and individual GraphQL operations. These metrics
   provide deeper insights but come with additional costs.

CloudWatch Logs is a tool that enables logging capabilities for your GraphQL APIs. Logs can
be set at two levels of the API:

1. **Request-level Logs**: These capture overall request
   information, including HTTP headers, GraphQL queries, operation summaries, and
   subscription registrations.
2. **Field-level Logs**: These provide detailed information
   about individual field resolutions, including request and response mappings, and tracing
   information for each field.
   You can configure logging, interpret log entries, and use log data for troubleshooting and
   optimization. AWS AppSync provides various log types that reveal your query’s execution,
   parsing, validation, and field resolution data.

## Setup and configuration

To turn on automatic logging on a GraphQL API, use the AWS AppSync console.

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
2. On the **APIs** page, choose the name of a GraphQL API.
3. On your API's homepage, in the navigation pane, choose
   **Settings**.
4. Under **Logging**, do the following:
   1. Turn on **Enable Logs**.
   2. For detailed request-level logging, select the check box under
      **Include verbose content**. (optional)
   3. Under **Field resolver log level**, choose your preferred
      field-level logging level (**None**,
      **Error**, **Info**, **Debug**, or **All**).
      (optional)
   4. Under **Create or use an existing role**, choose
      **New role** to create a new AWS Identity and Access Management (IAM) that allows
      AWS AppSync to write logs to CloudWatch. Or, choose **Existing role**
      to select the Amazon Resource Name (ARN) of an existing IAM role in your
      AWS account.

5. Choose **Save**.

### Manual IAM role configuration

If you choose to use an existing IAM role, the role must grant AWS AppSync the
required permissions to write logs to CloudWatch. To configure this manually, you must provide
a service role ARN so that AWS AppSync can assume the role when writing the logs.

In the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam"), create a new policy
with the name `AWSAppSyncPushToCloudWatchLogsPolicy` that has the following
definition:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 }
 ]
}`

```

Next, create a new role with the name **AWSAppSyncPushToCloudWatchLogsRole**, and attach the newly created policy
to the role. Edit the trust relationship for this role to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appsync.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Copy the role ARN and use it when setting up logging for an AWS AppSync GraphQL
API.

## CloudWatch metrics

You can use CloudWatch metrics to monitor and provide alerts about specific events that can
result in HTTP status codes or from latency. The following metrics are emitted:

`4XXError`

Errors resulting from requests that are not valid due to an incorrect
client configuration. Typically, these errors happen anywhere outside of
GraphQL
processing.
For example, these errors can occur when the request includes an incorrect
JSON payload or an incorrect query, when the service is throttled, or when
the authorization settings are misconfigured.

**Unit**: _Count_. Use the
Sum statistic to get the total occurrences of these errors.

`5XXError`

Errors encountered during the
running
of a GraphQL query. For example, this can occur when invoking a query for an
empty or incorrect schema. It can also occur when the Amazon Cognito user pool ID
or AWS Region is not valid. Alternatively, this could also happen if
AWS AppSync encounters an issue during processing of a request.

**Unit**: _Count_. Use the
Sum statistic to get the total occurrences of these errors.

`Latency`

The time between when AWS AppSync receives a request from a client and when
it returns a response to the client. This doesn’t include the network
latency encountered for a response to reach the end devices.

**Unit**: _Millisecond_. Use
the Average statistic to evaluate expected latencies.

`Requests`

The number of requests (queries + mutations) that all APIs in your
account have processed, by Region.

**Unit**: _Count_. The
number of all requests processed in a particular Region.

`TokensConsumed`

Tokens are allocated to `Requests` based on the amount of
resources (processing time and memory used) that a `Request`
consumes. Usually, each `Request` consumes one token. However, a
`Request` that consumes large amounts of resources is
allocated additional tokens as needed.

**Unit**: _Count_. The
number of tokens allocated to requests processed in a particular
Region.

`NetworkBandwidthOutAllowanceExceeded`

###### Note

In the AWS AppSync console, on the cache settings page, the **Cache Health Metrics** option allows you to
enable this cache-related health metric.

The network packets dropped because the throughput exceeded the
aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a
cache configuration. Data is recorded for a particular API by specifying the
`API_Id` in the
`appsyncCacheNetworkBandwidthOutAllowanceExceeded`
metric.

**Unit**: _Count_. The
number of packets dropped after exceeding the bandwidth limit for an API
specified by ID.

`EngineCPUUtilization`

###### Note

In the AWS AppSync console, on the cache settings page, the **Cache Health Metrics** option allows you to
enable this cache-related health metric.

The CPU utilization (percentage) allocated to the Redis OSS process. This
is useful for diagnosing bottlenecks in a cache configuration. Data is
recorded for a particular API by specifying the `API_Id` in the
`appsyncCacheEngineCPUUtilization` metric.

**Unit**: _Percent_. The CPU
percentage currently in use by the Redis OSS process for an API specified by
ID.

### Real-time subscriptions

All metrics are emitted in one dimension: **GraphQLAPIId**. This means that all metrics are coupled with GraphQL API
IDs. The following metrics are related to GraphQL subscriptions over pure
WebSockets:

`ConnectRequests`

The number of WebSocket connection requests made to AWS AppSync, including
both successful and unsuccessful attempts.

**Unit**: _Count_. Use the Sum statistic to get the total number of
connection requests.

`ConnectSuccess`

The number of successful WebSocket connections to AWS AppSync. It is
possible to have connections without subscriptions.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the successful
connections.

`ConnectClientError`

The number of WebSocket connections that were rejected by AWS AppSync
because of client-side errors. This could imply that the service is
throttled or that the authorization settings are misconfigured.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the client-side
connection errors.

`ConnectServerError`

The number of errors that originated from AWS AppSync while processing
connections. This usually happens when an unexpected server-side issue
occurs.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the server-side
connection errors.

`DisconnectSuccess`

The number of successful WebSocket disconnections from
AWS AppSync.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the successful
disconnections.

`DisconnectClientError`

The number of client errors that originated from AWS AppSync while
disconnecting WebSocket connections.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the disconnection
errors.

`DisconnectServerError`

The number of server errors that originated from AWS AppSync while
disconnecting WebSocket connections.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the disconnection
errors.

`SubscribeSuccess`

The number of subscriptions that were successfully registered to
AWS AppSync through WebSocket. It's possible to have connections without
subscriptions, but it's not possible to have subscriptions without
connections.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the successful
subscriptions.

`SubscribeClientError`

The number of subscriptions that were rejected by AWS AppSync because of
client-side errors. This can occur when a JSON payload is incorrect, the
service is throttled, or the authorization settings are
misconfigured.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the client-side
subscription errors.

`SubscribeServerError`

The number of errors that originated from AWS AppSync while processing
subscriptions. This usually happens when an unexpected server-side issue
occurs.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the server-side
subscription errors.

`UnsubscribeSuccess`

The number of unsubscribe requests that were successfully
processed.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the successful
unsubscribe requests.

`UnsubscribeClientError`

The number of unsubscribe requests that were rejected by AWS AppSync
because of client-side errors.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the client-side
unsubscribe request errors.

`UnsubscribeServerError`

The number of errors that originated from AWS AppSync while processing
unsubscribe requests. This usually happens when an unexpected server-side
issue occurs.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the server-side
unsubscribe request errors.

`PublishDataMessageSuccess`

The number of subscription event messages that were successfully
published.

**Unit**: _Count_. Use
the Sum statistic to get the total of the subscription event messages
were successfully published.

`PublishDataMessageClientError`

The number of subscription event messages that failed to publish
because of client-side errors.

`Unit`: _Count_. Use the Sum statistic
to get the total occurrences of the client-side publishing subscription
events errors.

`PublishDataMessageServerError`

The number of errors that originated from AWS AppSync while publishing
subscription event messages. This usually happens when an unexpected
server-side issue occurs.

**Unit**: _Count_. Use
the Sum statistic to get the total occurrences of the server-side
publishing subscription events errors.

`PublishDataMessageSize`

The size of subscription event messages published.

**Unit**:
_Bytes_.

`ActiveConnections`

The number of concurrent WebSocket connections from clients to
AWS AppSync in 1 minute.

**Unit**: _Count_. Use
the Sum statistic to get the total opened connections.

`ActiveSubscriptions`

The number of concurrent subscriptions from clients in 1
minute.

**Unit**: _Count_. Use
the Sum statistic to get the total active subscriptions.

`ConnectionDuration`

The amount of time that the connection stays open.

**Unit**:
_Milliseconds_. Use the Average statistic to
evaluate connection duration.

`OutboundMessages`

The number of metered messages successfully published. One metered
message equals 5 kB of delivered data.

**Unit**: _Count_. Use the Sum statistic to get the total number of
successfully published metered messages.

`InboundMessageSuccess`

The number of inbound messages successfully processed. Each
subscription type invoked by a mutation generates one inbound message.

**Unit**: _Count_. Use the Sum statistic to get the total number of
successfully processed inbound messages.

`InboundMessageError`

The number of inbound messages that failed processing due to invalid
API requests, such as exceeding the 240 kB subscription payload size
limit.

**Unit**: _Count_. Use the Sum statistic to get the total number of
inbound messages with API-related processing failures.

`InboundMessageFailure`

The number of inbound messages that failed processing due to errors
from AWS AppSync.

**Unit**: _Count_. Use the Sum statistic to get the total number of
inbound messages with AWS AppSync-related processing failures.

`InboundMessageDelayed`

The number of delayed inbound messages. Inbound messages can be
delayed when either the inbound message rate quota or outbound message
rate quota is breached.

**Unit**: _Count_. Use the Sum statistic to get the total number of
inbound messages that were delayed.

`InboundMessageDropped`

The number of dropped inbound messages. Inbound messages can be
dropped when either the inbound message rate quota or outbound message
rate quota is breached.

**Unit**: _Count_. Use the Sum statistic to get the total number of
inbound messages that were dropped.

`InvalidationSuccess`

The number of subscriptions successfully invalidated (unsubscribed) by
a mutation with
`$extensions.invalidateSubscriptions()`.

**Unit**: _Count_. Use the Sum statistic to retrieve the total number
of subscriptions that were successfully unsubscribed.

`InvalidationRequestSuccess`

The number of invalidation requests successfully processed.

**Unit**: _Count_. Use the Sum statistic to get the total number of
successfully processed invalidation requests.

`InvalidationRequestError`

The number of invalidation requests that failed processing due to
invalid API requests.

**Unit**: _Count_. Use the Sum statistic to get the total number of
invalidation requests with API-related processing failures.

`InvalidationRequestFailure`

The number of invalidation requests that failed processing due to
errors from AWS AppSync.

**Unit**: _Count_. Use the Sum statistic to get the total number of
invalidation requests with AWS AppSync-related processing failures.

`InvalidationRequestDropped`

The number of invalidation requests dropped when the invalidation
request quota was exceeded.

**Unit**: _Count_. Use the Sum statistic to get the total number of
dropped invalidation requests.

#### Comparing inbound and outbound messages

When a mutation is executed, subscription fields with the _@aws_subscribe_ directive for that mutation are invoked. Each
subscription invocation generates one inbound message. For example, if two
subscription fields specify the same mutation in _@aws_subscribe_, then two inbound messages are generated when that
mutation is called.

One outbound message equals 5 kB of data delivered to WebSocket clients. For
example, sending 15 kB of data to 10 clients results in 30 outbound messages (15 kB \*
10 clients / 5 kB per message = 30 messages).

You can request quota increases for either inbound or outbound messages. For more
information, see [AWS AppSync endpoints and
quotas](../../../general/latest/gr/appsync.md#limits_appsync "../../../general/latest/gr/appsync.md#limits_appsync") in the _AWS General Reference_
guide and the instructions for [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
Guide_.

### Enhanced metrics

Enhanced metrics emit granular data on API usage and performance such as AWS AppSync
request and error counts, latency, and cache hits/misses. All enhanced metric data is
sent to your CloudWatch account, and you can configure the types of data that will be sent.

###### Note

Additional charges are applied when using enhanced metrics. For more information,
see **detailed monitoring** pricing tiers in [Amazon CloudWatch
pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

These metrics can be found on various settings pages in the AWS AppSync console. On the
API settings page, the **Enhanced Metrics** section allows
you to enable or disable the following items:

**Resolver metrics behavior**: These options control how
additional metrics for resolvers are collected. You can choose to enable full request
resolver metrics (metrics enabled for all resolvers in requests) or per-resolver metrics
(metrics only enabled for resolvers where the configuration is set to enabled). The
following options are available:

`GraphQL errors per resolver (GraphQLError)`

The number of GraphQL errors that occured per resolver.

**Metric dimension**:
`API_Id`, `Resolver`

**Unit**: _Count_.

`Requests per resolver (Request)`

The number of invocations that occurred during a request. This is
recorded on a per-resolver basis.

**Metric dimension**:
`API_Id`, `Resolver`

**Unit**: _Count_.

`Latency per resolver (Latency)`

The time to complete a resolver invocation. Latency is measured in
milliseconds and is recorded on a per-resolver basis.

**Metric dimension**:
`API_Id`, `Resolver`

**Unit**: _Millisecond_.

`Cache hits per resolver (CacheHit)`

The number of cache hits during a request. This will only be emitted
if a cache is used. Cache hits are recorded on a per-resolver
basis.

**Metric dimension**:
`API_Id`, `Resolver`

**Unit**: _Count_.

`Cache misses per resolver (CacheMiss)`

The number of cache misses during a request. This will only be emitted
if a cache is used. Cache misses are recorded on a per-resolver
basis.

**Metric dimension**:
`API_Id`, `Resolver`

**Unit**: _Count_.

**Data source metrics behavior**: These options control
how additional metrics for data sources are collected. You can choose to enable full
request data source metrics (metrics enabled for all data sources in requests) or
per-data source metrics (metrics only enabled for data sources where the configuration
is set to enabled). The following options are available:

`Requests per data source (Request)`

The number of invocations that occured during a request. Requests are
recorded on a per-data source basis. If full requests are enabled, each
data source will have its own entry in CloudWatch.

**Metric dimension**:
`API_Id`, `Datasource`

**Unit**: _Count_.

`Latency per data source (Latency)`

The time to complete a data source invocation. Latency is recorded on
a per-data source basis.

**Metric dimension**:
`API_Id`, `Datasource`

**Unit**: _Millisecond_.

`Errors per data source (GraphQLError)`

The number of errors that occurred during a data source
invocation.

**Metric dimension**:
`API_Id`, `Datasource`

**Unit**: _Count_.

**Operation metrics**: Enables GraphQL operation-level
metrics.

`Requests per operation (Request)`

The number of times a specified GraphQL operation was called.

**Metric dimension**:
`API_Id`, `Operation`

**Unit**: _Count_.

`GraphQL errors per operation (GraphQLError)`

The number of GraphQL errors that occurred during a specified GraphQL
operation.

**Metric dimension**:
`API_Id`, `Operation`

**Unit**: _Count_.

## CloudWatch logs

You can configure two types of logging on any new or existing GraphQL API: request-level
and field-level.

### Request-level logs

When request-level logging (**Include verbose content**) is
configured, the following information is logged:

- The number of tokens consumed
- The request and response HTTP headers
- The GraphQL query that is running in the request
- The overall operation summary
- New and existing GraphQL subscriptions that are registered

### Field-level logs

When field-level logging is configured, the following information is logged:

- Generated request mapping with source and arguments for each field
- The transformed response mapping for each field, which includes the data as a
  result of resolving that field
- Tracing information for each field

If you turn on logging, AWS AppSync manages the CloudWatch Logs. The process includes creating
log groups and log streams, and reporting to the log streams with these logs.

When you turn on logging on a GraphQL API and make requests, AWS AppSync creates a log
group and log streams under the log group. The log group is named following the
`/aws/appsync/apis/{graphql_api_id}` format. Within each log group, the
logs are further divided into log streams. These are ordered by **Last Event Time** as logged data is reported.

Every log event is tagged with the **x-amzn-RequestId**
of that request. This helps you filter log events in CloudWatch to get all logged information
about that request. You can get the RequestId from the response headers of every GraphQL
AWS AppSync request.

The field-Level logging is configured with the following log levels:

- **None** - **No field-level
  logs are captured.**
- \***\*Error** - Logs the following information
  **only** for the fields that are in the
  error category:\*\*
  - The error section in the server response
  - Field-level errors
  - The generated request/response functions that got resolved for
    error fields

- \***\*Info** - Logs the following information
  **only** for the fields that are in the info
  and error categories:\*\*
  - Info-level messages
  - The user messages sent through `$util.log.info` and
    `console.log`
  - Field-level tracing and mapping logs are not shown.
  - If field-level logging is set to `INFO` or higher
    with verbose-content included, AWS AppSync adds the transformed mapping
    template logging messages. This will contain any information added
    to the transformed mapping template, or the output of the resolver
    or function executed JavaScript code, and should not be used if you
    are planning to send sensitive information, such as passwords or
    authorization headers, to downstream data sources and do not want
    that information in your logs.

- \***\*Debug** - Logs the following information
  **only** for the fields that are in the
  debug, info, and error categories:\*\*
  - Debug-level messages
  - The user messages sent through `$util.log.info`,
    `$util.log.debug`, `console.log`, and
    `console.debug`
  - Field-level tracing and mapping logs are not shown.

- \***\*All** - Logs the following information for
  **all** fields in the query:\*\*
  - Field-level tracing information
  - The generated request/response functions that were resolved for
    each field

### Benefits of monitoring

You can use logging and metrics to identify, troubleshoot, and optimize your GraphQL
queries. For example, these will help you debug latency issues using the tracing
information that is logged for each field in the query. To demonstrate this, suppose you
are using one or more resolvers nested in a GraphQL query. A sample field operation in
CloudWatch Logs might look similar to the following:

```
{
    "path": [
        "singlePost",
        "authors",
        0,
        "name"
    ],
    "parentType": "Post",
    "returnType": "String!",
    "fieldName": "name",
    "startOffset": 416563350,
    "duration": 11247
}
```

This might correspond to a GraphQL schema, similar to the following:

```
type Post {
  id: ID!
  name: String!
  authors: [Author]
}

type Author {
  id: ID!
  name: String!
}

type Query {
  singlePost(id:ID!): Post
}
```

In the preceding log results, **path** shows a single
item in your data returned from running a query named `singlePost()`. In this
example, it’s representing the **name** field at the first
index (0). The **startOffset** gives an offset from the
start of the GraphQL query operation. The **duration** is
the total time to resolve the field. These values can be useful to troubleshoot why data
from a particular data source might be running slower than expected, or if a specific
field is slowing down the entire query. For example, you might choose to increase
provisioned throughput for an Amazon DynamoDB table, or remove a specific field from a query
that is causing the overall operation to perform poorly.

As of May 8, 2019, AWS AppSync generates log events as fully structured JSON. This can
help you use log analytics services such as CloudWatch Logs Insights and Amazon OpenSearch Service to understand
the performance of your GraphQL requests and usage characteristics of your schema
fields. For example, you can easily identify resolvers with large latencies that may be
the root cause of a performance issue. You can also identify the most and least
frequently used fields in your schema and assess the impact of deprecating GraphQL
fields.

### Conflict detection and sync logging

If an AWS AppSync API has logging to CloudWatch Logs configured with the **Field resolver
log level** set to **All**, then AWS AppSync emits conflict
detection and resolution information to the log group. This provides granular insight
into how the AWS AppSync API responded to a conflict. To help you interpret the response,
the following information is provided in the logs:

`conflictType`

Details whether a conflict occurred due to a version mismatch or the
customer-supplied condition.

`conflictHandlerConfigured`

States the conflict handler configured on the resolver at the time of
the request.

`message`

Provides information on how the conflict was detected and
resolved.

`syncAttempt`

The number of tries the server attempted in order to synchronize the
data before ultimately rejecting the request.

`data`

If the conflict handler configured is `Automerge`, this
field is populated to show what decision `Automerge` took for
each field. Actions provided can be:

- **REJECTED** - When
  `Automerge` rejects the incoming field value in favor
  of the value in the server.
- **ADDED** - When
  `Automerge` adds on the incoming field due to no
  pre-existing value in the server.
- **APPENDED** - When
  `Automerge` appends the incoming values to the values
  for the List that exists in the server.
- **MERGED** - When
  `Automerge` merges the incoming values to the values
  for the Set that exists in the server.

### Using token counts to optimize your requests

Requests that consume less than or equal to 1,500 KB-seconds of memory and vCPU time
are allocated one token. Requests with resource consumption greater than 1,500
KB-seconds receive additional tokens. For example, if a request consumes 3,350
KB-seconds, AWS AppSync allocates three tokens (rounded up to the next integer value) to
the request. By default, AWS AppSync allocates a maximum of 5,000 or 10,000 request tokens
per second to the APIs in your account, depending upon the AWS Region in which it's
deployed. If your APIs each use an average of two tokens per second, you'll be limited
to 2,500 or 5,000 requests per second, respectively. If you need more tokens per second
than the allotted amount, you can submit a request to increase the default quota for the
rate of request tokens. For more information, see [AWS AppSync endpoints and
quotas](../../../general/latest/gr/appsync.md#limits_appsync "../../../general/latest/gr/appsync.md#limits_appsync") in the _AWS General Reference guide_ and [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

A high per-request token count could indicate that there's an opportunity to optimize
your requests and improve the performance of your API. Factors that can increase your
per-request token count include:

- The size and complexity of your GraphQL schema.
- The complexity of request and response mapping templates.
- The number of resolver invocations per request.
- The amount of data returned from resolvers.
- The latency of downstream data sources.
- Schema and query designs that require successive data source calls (as opposed
  to parallel or batched calls).
- Logging configuration, particularly field-level and verbose log
  content.

###### Note

In addition to AWS AppSync metrics and logs, clients can access the number of tokens
consumed in a request via the response header
`x-amzn-appsync-TokensConsumed`.

### Log size limits

By default, if logging has been enabled, AWS AppSync will send up to 1 MB of logs per
request. Logs exceeding this size will be truncated. To reduce log sizes, choose the
`ERROR` logging level for field-level logs and disable
`VERBOSE` logging, or disable field-level logs entirely if not needed. As
an alternative to the `ALL` log level, you can use Enhanced Metrics to obtain
metrics on specific resolvers, data sources, or GraphQL operations, or utilize the
logging utilities provided by AppSync to log only the necessary information.

## Log type reference

### RequestSummary

- **requestId:** Unique identifier for the
  request.
- **graphQLAPIId:** ID of the GraphQL API making the
  request.
- **statusCode:** HTTP status code response.
- **latency:** End-to-end latency of the request, in
  nanoseconds, as an integer.

```
{
     "logType": "RequestSummary",
     "requestId": "dbe87af3-c114-4b32-ae79-8af11f3f96f1",
     "graphQLAPIId": "pmo28inf75eepg63qxq4ekoeg4",
     "statusCode": 200,
     "latency": 242000000
}
```

### ExecutionSummary

- **requestId:** Unique identifier for the
  request.
- **graphQLAPIId:** ID of the GraphQL API making the
  request.
- **startTime:** The start timestamp of GraphQL
  processing for the request, in RFC 3339 format.
- **endTime:** The end timestamp of GraphQL processing
  for the request, in RFC 3339 format.
- **duration:** The total elapsed GraphQL processing
  time, in nanoseconds, as an integer.
- **version:** The schema version of the
  ExecutionSummary.
- \***\*parsing:\*\***
  - **startOffset:** The start offset for
    parsing, in nanoseconds, relative to the invocation, as an
    integer.
  - **duration:** The time spent parsing,
    in nanoseconds, as an integer.

- \***\*validation:\*\***
  - **startOffset:** The start offset for
    validation, in nanoseconds, relative to the invocation, as an
    integer.
  - **duration:** The time spent
    performing validation, in nanoseconds, as an integer.

```
{
    "duration": 217406145,
    "logType": "ExecutionSummary",
    "requestId": "dbe87af3-c114-4b32-ae79-8af11f3f96f1",
    "startTime": "2019-01-01T06:06:18.956Z",
    "endTime": "2019-01-01T06:06:19.174Z",
    "parsing": {
        "startOffset": 49033,
        "duration": 34784
    },
    "version": 1,
    "validation": {
        "startOffset": 129048,
        "duration": 69126
    },
    "graphQLAPIId": "pmo28inf75eepg63qxq4ekoeg4"
}
```

### Tracing

- **requestId:** Unique identifier for the
  request.
- **graphQLAPIId:** ID of the GraphQL API making the
  request.
- **startOffset:** The start offset for field
  resolution, in nanoseconds, relative to the invocation, as an integer.
- **duration:** The time spent resolving the field, in
  nanoseconds, as an integer.
- **fieldName:** The name of the field being
  resolved.
- **parentType:** The parent type of the field being
  resolved.
- **returnType:** The return type of the field being
  resolved.
- **path:** A list of path segments, starting at the
  root of the response and ending with the field being resolved.
- **resolverArn:** The ARN of the resolver used for
  field resolution. Might not be present on nested fields.

```
{
    "duration": 216820346,
    "logType": "Tracing",
    "path": [
        "putItem"
    ],
    "fieldName": "putItem",
    "startOffset": 178156,
    "resolverArn": "arn:aws:appsync:us-east-1:111111111111:apis/pmo28inf75eepg63qxq4ekoeg4/types/Mutation/fields/putItem",
    "requestId": "dbe87af3-c114-4b32-ae79-8af11f3f96f1",
    "parentType": "Mutation",
    "returnType": "Item",
    "graphQLAPIId": "pmo28inf75eepg63qxq4ekoeg4"
}
```

## Analyzing your logs with CloudWatch Logs Insights

The following are examples of queries you can run to get actionable insights into the
performance and health of your GraphQL operations. These examples are available as sample
queries in the CloudWatch Logs Insights console. In the [CloudWatch
console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch"), choose **Logs Insights**, select the AWS AppSync log
group for your GraphQL API, and then choose **AWS AppSync queries** under
**Sample queries**.

The following query returns the top 10 GraphQL requests with maximum tokens
consumed:

```
filter @message like "Tokens Consumed"
| parse @message "* Tokens Consumed: *" as requestId, tokens
| sort tokens desc
| display requestId, tokens
| limit 10
```

The following query returns the top 10 resolvers with maximum latency:

```
  fields resolverArn, duration
| filter logType = "Tracing"
| limit 10
| sort duration desc
```

The following query returns the most frequently invoked resolvers:

```
  fields ispresent(resolverArn) as isRes
| stats count() as invocationCount by resolverArn
| filter isRes and logType = "Tracing"
| limit 10
| sort invocationCount desc
```

The following query returns resolvers with the most errors in mapping templates:

```
  fields ispresent(resolverArn) as isRes
| stats count() as errorCount by resolverArn, logType
| filter isRes and (logType = "RequestMapping" or logType = "ResponseMapping") and fieldInError
| limit 10
| sort errorCount desc
```

The following query returns resolver latency statistics:

```
  fields ispresent(resolverArn) as isRes
| stats min(duration), max(duration), avg(duration) as avg_dur by resolverArn
| filter isRes and logType = "Tracing"
| limit 10
| sort avg_dur desc
```

The following query returns field latency statistics:

```
  stats min(duration), max(duration), avg(duration) as avg_dur
  by concat(parentType, '/', fieldName) as fieldKey
| filter logType = "Tracing"
| limit 10
| sort avg_dur desc
```

The results of CloudWatch Logs Insights queries can be exported to CloudWatch dashboards.

## Analyze your logs with OpenSearch Service

You can search, analyze, and visualize your AWS AppSync logs with Amazon OpenSearch Service to identify
performance bottlenecks and root causes of operational issues. You can identify resolvers
with the maximum latency and errors. In addition, you can use OpenSearch Dashboards to
create dashboards with powerful visualizations. OpenSearch Dashboards is an open source data
visualization and exploration tool available in OpenSearch Service. Using OpenSearch Dashboards, you can
continuously monitor the performance and health of your GraphQL operations. For example,
you can create dashboards to visualize the P90 latency of your GraphQL requests and drill
down into the P90 latencies of each resolver.

When using OpenSearch Service, use **“cwl\*”** as the filter pattern to
search OpenSearch indexes. OpenSearch Service indexes the logs streamed from CloudWatch Logs with a prefix of
**“cwl-”**. To differentiate AWS AppSync API logs from other
CloudWatch logs sent to OpenSearch Service, we recommend adding an additional filter expression of
`graphQLAPIID.keyword=`YourGraphQLAPIID`` to your
search.

## Log format migration

Log events that AWS AppSync generates on or after May 8, 2019 are formatted as fully
structured JSON. To analyze GraphQL requests prior to May 8, 2019, you can migrate older
logs to fully structured JSON using a script available in the [GitHub Sample](https://github.com/aws-samples/aws-appsync-cwl-migrator "https://github.com/aws-samples/aws-appsync-cwl-migrator"). If
you need to use the log format prior to May 8, 2019, create a support ticket with the
following settings: set **Type** to **Account
Management** and then set **Category** to **General
Account Question**.

You can also use [metric filters](../../../AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.md "../../../AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.md") in
CloudWatch to turn log data into numerical CloudWatch metrics, so that you can graph or set an alarm on
them.

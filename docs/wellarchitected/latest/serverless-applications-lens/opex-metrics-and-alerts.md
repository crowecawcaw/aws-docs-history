# Metrics and alerts

It’s important to understand Amazon CloudWatch metrics and dimensions for every AWS service
you intend to use so that you can put a plan in a place to assess its behavior and add
custom metrics where you see fit.

Amazon CloudWatch provides [automated cross service and per service dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.md") to help you understand key
metrics for the AWS services that you use. Use Lambda Powertools for supported languages
to create and capture custom CloudWatch metrics. When Lambda Powertools is not available in your
programming language of choice, use [Amazon CloudWatch Embedded Metric Format](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation.md") (EMF) libraries. EMF logs emitted by Lambda are
processed asynchronously by CloudWatch and do not impact the performance of your Serverless
application.

The following guidelines can be used whether you are creating a dashboard or looking to
formulate a plan for new and existing applications when it comes to metrics:

- **Business metrics**
  - Business KPIs that will measure your application performance against business
    goals and are important to know when something is critically affecting your
    overall business, revenue-wise or not.
  - Examples: Orders placed, debit or credit card operations, flights
    purchased

- **Customer experience metrics**
  - Customer experience data dictates not only the overall effectiveness of its UI
    and UX, but also whether changes or anomalies are affecting customer experience in
    a particular section of your application. Often times, these are measured in
    percentiles to prevent outliers when trying to understand the impact over time and
    how it’s spread across your customer base.
  - Examples: Perceived latency, time it takes to add an item to a basket or to
    check out, page load times

- **System metrics**
  - Vendor and application metrics are important to understand the health of your
    system, uncover root causes from the metrics above, and gain insight into customer
    experience.
  - Examples: Percentage of HTTP errors and successes, memory utilization, function
    duration, error, or throttling, queue length, stream records length, integration
    latency

- **Operational metrics**

      + Operational metrics are equally important to understand sustainability and
       maintenance of a given system. These metrics are also crucial to pinpoint how
       stability progressed or degraded over time.
      + Examples: Number of tickets (successful and unsuccessful resolutions), number
       of times people on-call were paged, availability, CI/CD pipeline stats (successful
       and failed deployments, feedback time, cycle and lead time)

  CloudWatch Alarms should be configured at both individual and aggregated levels. An
  individual-level example is alarming on the _Duration_ metric from
  Lambda or `IntegrationLatency` from API Gateway when invoked through API, since
  different parts of the application likely have different profiles. In this instance, you
  can quickly identify a bad deployment that makes a function execute for much longer than
  usual.

Aggregate-level examples include alarming, but are not limited to the following
metrics:

- **AWS Lambda**: `Duration`,
  `Errors`, `Throttles`, and `ConcurrentExecutions`.
  For stream-based invocations, alert on `IteratorAge`. For asynchronous
  invocations, alert on `DeadLetterErrors`. When provisioned concurrency is
  enabled, use `ProvisionedConcurrencySpilloverInvocations`.
- **Amazon API Gateway**: `IntegrationLatency`,
  `Latency`, `5XXError`. For WebSocket API, use
  `ClientError`, `IntegrationError` and
  `ExecutionError`.
- **Application Load Balancer**: `HTTPCode_ELB_5XX_Count`,
  `RejectedConnectionCount`, `HTTPCode_Target_5XX_Count,
UnHealthyHostCount`, `LambdaInternalError`,
  `LambdaUserError`.
- **AWS AppSync**: `5XX` and `Latency`.
- **Amazon SQS:**
  `ApproximateAgeOfOldestMessage`.
- **Amazon Kinesis Data Streams:**
  `ReadProvisionedThroughputExceeded`,
  `WriteProvisionedThroughputExceeded`,
  `GetRecords.`,`IteratorAgeMilliseconds`,
  `PutRecord.Success`, `PutRecords.Success` (if using Kinesis
  Producer Library) and `GetRecords.Success`.
- **Amazon SNS**: `NumberOfNotificationsFailed`,
  `NumberOfNotificationsFilteredOut-InvalidAttributes`.
- **Amazon SES:**
  `Rejects`, `Bounces`, `Complaints`,
  `RenderingFailures`.
- **AWS Step Functions:**
  `ExecutionThrottled`, `ExecutionsFailed`,
  `ExecutionsTimedOut`, `ActivitiesTimedOut`,
  `LambdaFunctionsTimedOut`.
- **Amazon EventBridge:**
  `FailedInvocations`, `ThrottledRules`.
- **Amazon S3:**
  `5xxErrors`, `TotalRequestLatency`.
- **Amazon DynamoDB:**
  `ReadThrottleEvents`, `WriteThrottleEvents`,
  `SystemErrors`, `ThrottledRequests`, `UserErrors`.

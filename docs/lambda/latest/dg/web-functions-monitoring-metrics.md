

# Using CloudWatch metrics with Lambda Web Functions
<a name="web-functions-monitoring-metrics"></a>

AWS Lambda publishes Web Function metrics to Amazon CloudWatch in two namespaces:
+ `AWS/Lambda/Web` – Request and response metrics for each endpoint, and resource usage metrics for the execution environments that serve each Web Function. Lambda centralizes these metrics into the Web Function's home Region, so the values in the home Region include traffic from every Region that the endpoint serves.
+ `AWS/Lambda/Web/Usage` – Regional usage and throttling metrics that show consumption against Regional quotas and endpoint limits. These metrics are not centralized. They remain in the Region where the request was served.

Lambda publishes request, usage, and throttling metrics only when a request produces a value for them. Execution environment metrics are different: Lambda publishes them every minute for each active execution environment. Some metrics are **sparse**: Lambda does not publish a data point of 0 for a period in which the event did not occur. For example, if no request returns a 5xx response in a period, `HTTPResponseStatusClass5XX` has no data point for that period. The following tables describe when Lambda emits each metric. When you create alarms on sparse metrics, configure how the alarm treats missing data. For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html) in the *Amazon CloudWatch User Guide*.

**Topics**
+ [Request metrics](#web-functions-monitoring-metrics-request)
+ [Execution environment metrics](#web-functions-monitoring-metrics-environment)
+ [Regional usage and throttling metrics](#web-functions-monitoring-metrics-usage)
+ [Using metrics with other CloudWatch features](#web-functions-monitoring-metrics-integrations)
+ [Setting an alarm on 5xx responses](#web-functions-monitoring-alarms)

## Request metrics
<a name="web-functions-monitoring-metrics-request"></a>

Request metrics are published in the `AWS/Lambda/Web` namespace with the `FunctionName` and `EndpointName` dimensions. They use the `Count` unit. Use the `Sum` statistic.


| Metric | Statistic | When Lambda emits it | Description | 
| --- | --- | --- | --- | 
| ExecutedRequests | Sum | Only for periods in which at least one request reached an execution environment. | The number of requests that reached an execution environment. Requests that Lambda throttles or rejects before they reach an execution environment are not counted. | 
| HTTPResponseStatusClass4XX | Sum | Sparse. Only for periods with at least one 4xx response. | The number of responses returned to callers with a status code from 400 through 499. The response can come from your application or from Lambda, including throttled requests that receive HTTP 429. Requests that Lambda rejects before it identifies the endpoint, such as malformed requests, are not counted. | 
| HTTPResponseStatusClass5XX | Sum | Sparse. Only for periods with at least one 5xx response. | The number of responses returned to callers with a status code from 500 through 599. The response can come from your application or from Lambda. During a service disruption, this metric might undercount errors. | 

The status-class metrics count the status code that the caller received. They do not distinguish responses written by your application from responses returned by Lambda. If your application has already sent the response status and headers, a later failure, such as an interrupted stream or a request timeout, is counted under the original status code. To identify the source of an error, use the `lambda-web-error-type` response header and your logs. To count application errors separately, publish your own metrics. For more information, see [Publishing custom metrics with the embedded metric format](web-functions-emf.md).

To estimate a server error rate, divide `HTTPResponseStatusClass5XX` by `ExecutedRequests` over the same period with CloudWatch metric math. For example, use `FILL(m5xx, 0) / m_executed`, where `m5xx` and `m_executed` are the IDs of the two metrics. Because `HTTPResponseStatusClass5XX` is sparse, use `FILL` so that periods without errors evaluate to 0 instead of having no value. `HTTPResponseStatusClass5XX` also counts 5xx responses that Lambda returned before a request reached an execution environment. `ExecutedRequests` does not count these responses, so the ratio can overstate the rate during a service disruption.

Request metrics in the home Region aggregate traffic from every Region that the endpoint serves, so one alarm in the home Region covers the whole endpoint. Build alarms and dashboards on the home Region values. Don't rely on these metrics in other Regions; see [Telemetry in each Region](web-functions-monitoring.md#web-functions-monitoring-replica-telemetry).

Lambda emits request metrics when a request completes. For a long-running request, the data point can appear up to the request timeout after the request started, so errors from long requests can reach your alarms late. For the request timeout, see [Request timeout](web-functions-revisions-timeout.md).

## Execution environment metrics
<a name="web-functions-monitoring-metrics-environment"></a>

Execution environment metrics describe the resources that the execution environments serving your Web Function use. Lambda publishes them in the `AWS/Lambda/Web` namespace with the `FunctionName` dimension, and centralizes them into the Web Function's home Region.

Lambda emits these metrics once per minute for each active execution environment, so they could be sparse if there are no active execution environments. A value can be 0. An execution environment can publish more than one data point in a minute, for example when it initializes and when it shuts down, so don't use the `SampleCount` statistic to count active environments. To count them for an endpoint, use `EndpointActiveEnvironments`.


| Metric | Unit | Statistic | Description | 
| --- | --- | --- | --- | 
| EnvironmentActiveTime | Milliseconds | Sum | The wall-clock time that the function's execution environments were active, including initialization. Each data point is one environment's active time since its previous data point, so the Sum over a period is the total environment time consumed. | 
| EnvironmentCPUTime | Milliseconds | Sum | The vCPU time that the function's execution environments consumed, including initialization. | 
| EnvironmentMaxMemoryUsage | Megabytes | Maximum | The peak memory that an execution environment has used so far in its lifetime. | 
| EnvironmentConcurrentRequests | Count | Maximum | The highest number of requests that one execution environment served at the same time during the period. | 
| ResponseBytes | Bytes | Sum | The number of response bytes that the function's execution environments sent. | 

Execution environment metrics don't include the `EndpointName` dimension. They cover all endpoints of the Web Function.

## Regional usage and throttling metrics
<a name="web-functions-monitoring-metrics-usage"></a>

Usage and throttling metrics show how close your account and endpoints are to their Regional limits, and which limit throttled a request. The account request-rate quota and the account Arm64 vCPU quota apply separately in each AWS Region, so Lambda publishes these metrics in each Region and does not centralize them. To see usage for a Region, view the metrics in that Region. For the quotas, see [Lambda Web Functions](gettingstarted-limits.md#web-functions-quotas).

These metrics are published in the `AWS/Lambda/Web/Usage` namespace with the `FunctionName`, `EndpointName`, and `ExecutionRegion` dimensions. They use the `Count` unit.


| Metric | Statistic | When Lambda emits it | Description | 
| --- | --- | --- | --- | 
| ExecutedRequests | Sum | Only for periods in which at least one request reached an execution environment in the Region. | The number of requests that reached an execution environment in the Region. | 
| EndpointActiveEnvironments | Maximum | With requests to the endpoint. The value can be 0. There are no data points while the endpoint receives no requests. | The number of active execution environments of the endpoint in the Region. Compare this value with maxEnvironments. | 
| AccountRequestThrottles | Sum | Sparse. Only for periods with at least one such throttle. | The number of requests to the endpoint that were throttled because the account reached its request-rate quota in the Region. | 
| EndpointRequestThrottles | Sum | Sparse. Only for periods with at least one such throttle. | The number of requests that were throttled because the endpoint reached its request-rate limit (rateLimit). | 
| AccountActiveVCPUArm64Throttles | Sum | Sparse. Only for periods with at least one such throttle. | The number of requests to the endpoint that were throttled because serving them would have exceeded the account's Arm64 vCPU quota in the Region. Like the other throttle metrics, it counts only this endpoint's throttles. To see the account total, sum it across endpoints. | 
| EndpointActiveEnvironmentThrottles | Sum | Sparse. Only for periods with at least one such throttle. | The number of requests that were throttled because serving them would have exceeded the endpoint's maxEnvironments setting. | 

Lambda attributes each throttled request to one limit, so a throttled request increments at most one throttle metric. Requests that Lambda throttles because too many execution environments are initializing at the same time return HTTP 429 with the `Platform.EndpointConcurrentInitThrottle` error type but do not increment any throttle metric. Throttled requests also count toward `HTTPResponseStatusClass4XX` in the `AWS/Lambda/Web` namespace.

To monitor a `MultiRegion` or `PerRegion` endpoint, view or alarm on usage metrics in each Region, or combine them in a CloudWatch cross-Region dashboard.

## Using metrics with other CloudWatch features
<a name="web-functions-monitoring-metrics-integrations"></a>

Because `AWS/Lambda/Web` metrics are centralized into the home Region, you can use them with the standard CloudWatch features in that Region, including:
+ **Amazon CloudWatch Observability Access Manager** – Share Web Function metrics with a central monitoring account so that one account can observe many application accounts.
+ **Dashboards and alarms** – Build dashboards and alarms on the home Region metrics to cover the entire multi-Region deployment.

## Setting an alarm on 5xx responses
<a name="web-functions-monitoring-alarms"></a>

Create CloudWatch alarms to detect issues such as elevated error rates or throttling.

The following command creates an alarm that triggers when callers receive more than five 5xx responses from the endpoint in a five-minute period.

```
aws cloudwatch put-metric-alarm \
    --alarm-name {{my-web-app-prod-5xx}} \
    --namespace AWS/Lambda/Web \
    --metric-name HTTPResponseStatusClass5XX \
    --statistic Sum \
    --period 300 \
    --threshold 5 \
    --comparison-operator GreaterThanThreshold \
    --evaluation-periods 1 \
    --treat-missing-data notBreaching \
    --dimensions Name=FunctionName,Value={{my-web-app}} Name=EndpointName,Value={{prod}} \
    --alarm-actions {{arn:aws:sns:us-east-1:111122223333:my-alerts}}
```

Replace the following values:
+ {{my-web-app-prod-5xx}} – A name for the alarm.
+ {{my-web-app}} – The name of your Web Function.
+ {{prod}} – The name of the endpoint.
+ {{arn:aws:sns:us-east-1:111122223333:my-alerts}} – The ARN of the Amazon SNS topic that receives alarm notifications.

`--treat-missing-data notBreaching` is important here. `HTTPResponseStatusClass5XX` is a sparse metric, so periods with no 5xx responses produce no data points. Without this setting, the alarm would enter the `INSUFFICIENT_DATA` state during those periods.

**Note**  
Web Function metrics don't include a revision dimension. To attribute errors to a revision during a canary deployment, set an environment variable that identifies the build, such as `APP_VERSION`, in each revision, and include its value in your structured logs or as a dimension in metrics that you publish with the embedded metric format. System log events such as `platform.initStart` also record the `revisionId` that each execution environment runs, and the `lambda-web-logstream` response header identifies the log stream of the execution environment that served a request. For the rollback procedure, see [Rolling back](web-functions-deployment.md#web-functions-deployment-rollback).
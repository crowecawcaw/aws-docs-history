

# PromQL querying
<a name="CloudWatch-PromQL-Querying"></a>

When you ingest OpenTelemetry metrics into CloudWatch through the [Metrics endpoint](CloudWatch-OTLPEndpoint.md#CloudWatch-MetricsEndpoint), the hierarchical OTLP data model is flattened into PromQL-compatible labels. This section describes the label structure, the PromQL syntax for querying these labels, and the UTF-8 support in PromQL.

**Note**  
PromQL in Prometheus 3 supports full UTF-8 characters in metric names and label names. This is particularly important for OTLP metrics, because OpenTelemetry semantic conventions use dots in attribute names such as `service.name`. Previously, these dots were replaced with underscores during translation, causing discrepancies between what was defined in OTel conventions and what was queryable in Prometheus.  
A metric name that contains dots must be quoted, either inside the curly braces, as in `{"http.server.active_requests"}`, or as the value of the `__name__` label, as in `{__name__="http.server.active_requests"}`. A bare, unquoted name such as `http.server.active_requests` isn't valid PromQL.

When using PromQL in CloudWatch, the `@` prefix convention distinguishes OTLP-scoped labels from standard Prometheus labels. Fields within each scope use a double-`@` prefix (for example, `@resource.@schema_url`), while attributes use a single-`@` scope prefix, for example, `@resource.service.name`. Datapoint attributes also support bare (un-prefixed) access for backward compatibility with standard PromQL queries, for example, `{"http.server.active_requests"}` and `{"@datapoint.@name"="http.server.active_requests"}` are equivalent.

A PromQL expression is enclosed in curly braces, specifying the metric name and an optional set of label matchers. The following example selects all time series for the `http.server.active_requests` metric:

```
{"http.server.active_requests"}
```

The following example selects all time series for the metric `http.server.active_requests` where the OpenTelemetry resource attribute `service.name` equals `myservice`:

```
{"http.server.active_requests", "@resource.service.name"="myservice"}
```

You can combine multiple label matchers in a single query. The following example selects all time series for the `http.server.active_requests` metric where the OpenTelemetry resource attribute `service.name` equals `myservice` across all US regions:

```
{"http.server.active_requests",
 "@resource.service.name"="myservice",
 "@aws.region"=~"us-.*"}
```

The following example shows a range query. It calculates the average value of all datapoints within a specified time range for each time series:

```
avg_over_time(
  {"http.server.active_requests",
   "@resource.service.name"="myservice"}[5m]
)
```

The following table summarizes the prefix conventions for each OTLP scope:


| OTLP scope | Fields prefix | Attributes prefix | Example | 
| --- | --- | --- | --- | 
| Resource | `@resource.@` | `@resource.` | `@resource.service.name="myservice"` | 
| Instrumentation Scope | `@instrumentation.@` | `@instrumentation.` | `@instrumentation.@name="otel-go/metrics"` | 
| Datapoint | `@datapoint.@` | `@datapoint.` or bare | `cpu="cpu0"` or `@datapoint.cpu="cpu0"` | 
| AWS-reserved | N/A | `@aws.` | `@aws.account_id="123456789"` | 

## Querying vended AWS metrics with PromQL
<a name="CloudWatch-PromQL-Querying-Vended"></a>

To be able to query vended AWS metrics in PromQL, you first need to enable OTel enrichment of vended metrics. See: [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md).

After you enable OTel enrichment, vended AWS metrics become queryable through PromQL with additional labels. The metric name is the same as the original CloudWatch metric name, and the original CloudWatch dimensions are available as datapoint attributes. The following labels are available (the example below is for an EC2 instance):


| PromQL Label | Description | Example | 
| --- | --- | --- | 
| `InstanceId` | Original CloudWatch dimension, as a datapoint attribute | `i-0123456789abcdef0` | 
| `"@resource.cloud.resource_id"` | Full ARN of the resource | `arn:aws:ec2:us-east-1:123456789012:instance/i-0123456789abcdef0` | 
| `"@resource.cloud.provider"` | Cloud provider | `aws` | 
| `"@resource.cloud.region"` | AWS Region where this metric originated | `us-east-1` | 
| `"@resource.cloud.account.id"` | AWS account ID where this metric originated | `123456789012` | 
| `"@instrumentation.@name"` | Instrumentation scope name identifying the source service | `cloudwatch.aws/ec2` | 
| `"@instrumentation.cloudwatch.source"` | Source service identifier | `aws.ec2` | 
| `"@instrumentation.cloudwatch.solution"` | Enrichment solution identifier | `CloudWatchOTelEnrichment` | 
| `"@aws.tag.Environment"` | AWS resource tag | `production` | 
| `"@aws.account"` | AWS account where this metric was ingested (system label) | `123456789012` | 
| `"@aws.region"` | AWS Region where this metric was ingested (system label) | `us-east-1` | 

The following example selects `Invocations` for a specific Lambda function:

```
{Invocations, FunctionName="my-api-handler"}
```

The following example selects Lambda `Errors` for all functions tagged with a specific team:

```
{Errors, "@instrumentation.@name"="cloudwatch.aws/lambda", "@aws.tag.Team"="backend"}
```

The following example computes the total Lambda `Invocations` grouped by team:

```
sum by ("@aws.tag.Team")(
    {Invocations, "@instrumentation.@name"="cloudwatch.aws/lambda"}
)
```

The following example selects all time series for the EC2 `CPUUtilization` metric. The usage of `"@instrumentation.@name"="cloudwatch.aws/ec2"` is to exclusively match CPUUtilization from EC2 and not from other AWS services such as Amazon Relational Database Service:

```
histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
```

## Querying histogram metrics
<a name="CloudWatch-PromQL-Querying-Histograms"></a>

OpenTelemetry histogram metrics, such as request durations and latencies, are stored as histogram samples rather than float samples. Some AWS vended metrics are also stored as histograms. That's why the previous example uses `histogram_avg`. Histogram samples behave differently from float samples in PromQL, so a query pattern that works for one type can return an empty or incorrect result for the other.

To check whether a metric is a histogram, select its raw time series and inspect the `__type__` label on the results:

```
{"http.server.request.duration"}
```

### Delta and cumulative histograms
<a name="CloudWatch-PromQL-Querying-Histograms-Temporality"></a>

OpenTelemetry histograms use one of two aggregation temporalities:

Cumulative  
Each datapoint is a running total since the start of the series.

Delta  
Each datapoint is a complete total for its own export period.

The temporality determines which query pattern returns a correct result. CloudWatch reports a histogram's temporality in the `__temporality__` label, whose value is either `cumulative` or `delta`. To check the temporality of a metric, select its raw time series and inspect the `__temporality__` label on the results:

```
{"http.server.request.duration"}
```

The `rate`, `increase`, `irate`, and `resets` functions assume cumulative data. They measure growth between datapoints. CloudWatch applies this assumption to every histogram, including delta histograms. On a delta histogram, these functions return an incorrect result without a warning. For example, the common Prometheus pattern `histogram_count(rate({{histogram}}[5m]))` returns the correct observation rate for a cumulative histogram. It doesn't return a correct rate for a delta histogram.

For a cumulative histogram, use `rate`. The following example returns the observation rate, in observations per second:

```
sum(histogram_count(rate({"http.server.request.duration"}[5m])))
```

For a delta histogram, add up the per-period totals with `sum_over_time` and divide by the length of the range. This example also returns the observation rate:

```
sum(histogram_count(sum_over_time({"http.server.request.duration"}[5m]))) / 5m
```

You can adapt the delta pattern as follows:
+ To return the total number of observations in the range instead of a rate, remove `/ 5m`.
+ To return the mean observed value in the range, use `histogram_avg` instead of `histogram_count`.

**Note**  
Don't use a subquery such as `rate(histogram_count({{histogram}})[5m:1m])` to calculate a rate from a delta histogram. It returns the correct result only when the export interval equals the subquery step. If the export interval changes, it returns an incorrect result without a warning.

### Getting statistics from a histogram
<a name="CloudWatch-PromQL-Querying-Histograms-Statistics"></a>

The `min` and `max` aggregation operators operate only on float samples. They skip histogram samples, so applying them to a histogram metric returns an empty result rather than an error. The response includes an informational annotation that contains the text `ignored histogram`.

To read a statistic from a histogram metric, use a histogram function:

`histogram_quantile({{q}}, {{histogram}})`  
Returns the value at the {{q}} quantile — the value below which a fraction {{q}} of observations fall. {{q}} is a value between 0 and 1. For example, use `0.99` for p99, not `99`.

`histogram_avg({{histogram}})`  
Returns the mean of the observed values.

`histogram_count({{histogram}})` and `histogram_sum({{histogram}})`  
Return the number of observations and the sum of the observed values.

PromQL doesn't provide an exact maximum for a histogram. The closest equivalent is a high quantile such as `histogram_quantile(1, {{histogram}})`. Because a quantile is estimated from bucket boundaries, the result can be slightly higher than the largest observed value.

For a delta histogram, apply the function directly to the metric. The following example returns the p99 duration for each export period:

```
histogram_quantile(0.99, {"http.server.request.duration"})
```

The preceding form returns the p99 for a single export period. To calculate the p99 over a longer window, first combine the per-period histograms with `sum_over_time`. You don't divide by the range, because a quantile is unaffected by scaling the bucket counts. The following example returns the p99 duration over the last five minutes:

```
histogram_quantile(0.99, sum_over_time({"http.server.request.duration"}[5m]))
```

For a cumulative histogram, applying the function directly returns a statistic over the whole life of the series. To get a statistic for a recent window, apply the function to `rate`. The following example returns the p99 duration over the last five minutes:

```
histogram_quantile(0.99, rate({"http.server.request.duration"}[5m]))
```

### Keeping labels in the result
<a name="CloudWatch-PromQL-Querying-Histograms-Labels"></a>

An aggregation operator such as `avg` or `sum` combines all matching time series into one. It removes every label that you don't group by. To keep one result per label value, add a `by` clause. The following example returns the observation rate of a delta histogram for each service:

```
sum by ("@resource.service.name")(
    histogram_count(sum_over_time({"http.server.request.duration"}[5m]))
) / 5m
```

Histogram functions such as `histogram_quantile` and `histogram_avg` are functions rather than aggregations, so they keep all labels and return one result for each time series.

## Querying with MCP tools
<a name="CloudWatch-PromQL-Querying-MCP"></a>

The [CloudWatch MCP Server](https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server/) provides Model Context Protocol (MCP) tools that let AI assistants and development tools query CloudWatch PromQL data on your behalf. The MCP tools handle authentication and request formatting automatically, so you can focus on writing PromQL queries rather than managing HTTP requests and SigV4 signing.

The following PromQL tools are available in the CloudWatch MCP Server:


| Tool | Description | 
| --- | --- | 
| `execute_promql_query` | Runs an instant PromQL query, returning metric values at a single point in time. | 
| `execute_promql_range_query` | Runs a PromQL range query over a time window, returning time series data for trend analysis and graphing. | 
| `get_promql_label_values` | Retrieves values for a specific PromQL label, such as `__name__` for metric names or `@resource.service.name` for services. | 
| `get_promql_series` | Finds time series matching PromQL label selectors and returns the full label set of each matching series. | 
| `get_promql_labels` | Lists all available PromQL label names to help discover the label structure of your metrics. | 

For full details on parameters, configuration, and setup instructions, see [Tools for CloudWatch PromQL](https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server#tools-for-cloudwatch-promql) in the CloudWatch MCP Server documentation.

## Querying with the HTTP API
<a name="CloudWatch-PromQL-Querying-API"></a>

You can also query CloudWatch PromQL data programmatically by calling the Prometheus-compatible HTTP endpoints directly. Requests must be signed with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) using `monitoring` as the service name.

The PromQL endpoint follows the pattern `https://monitoring.{{AWS Region}}.amazonaws.com/api/v1/{{operation}}`. For example, for the US East (N. Virginia) (us-east-1) Region, the endpoint for an instant query is `https://monitoring.us-east-1.amazonaws.com/api/v1/query`.

For the full API reference, including supported operations, request parameters, and response formats, see [Prometheus-compatible APIs](CloudWatch-PromQL-APIs.md). For the list of AWS Regions where PromQL querying is available, see [Supported AWS Regions](CloudWatch-PromQL.md#CloudWatch-PromQL-Regions). For the IAM actions required for each operation, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM).
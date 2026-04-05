# PromQL querying

When you ingest OpenTelemetry metrics into CloudWatch via OpenTelemetry Protocol (OTLP), the
hierarchical OTLP data model is flattened into PromQL-compatible labels. This section describes
the label structure, the PromQL syntax for querying these labels, and the UTF-8 support in PromQL.

###### Note

PromQL in Prometheus 3 supports full UTF-8 characters in metric names and label names.
This is particularly important for OTLP metrics, because OpenTelemetry semantic conventions
use dots in attribute names such as `service.name`. Previously, these dots were
replaced with underscores during translation, causing discrepancies between what was defined
in OTel conventions and what was queryable in Prometheus.

When using PromQL in CloudWatch, the `@` prefix convention distinguishes OTLP-scoped
labels from standard Prometheus labels. Fields within each scope use a double-`@`
prefix (for example, `@resource.@schema_url`), while attributes use a single-`@`
scope prefix, for example, `@resource.service.name`. Datapoint attributes also support
bare (un-prefixed) access for backward compatibility with standard PromQL queries, for example,
`{"http.server.active_requests"}` and `{"@datapoint.@name"="http.server.active_requests"}`
are equivalent.

A PromQL expression is enclosed in curly braces, specifying the metric name and an optional set
of label matchers. The following example selects all time series for the
`http.server.active_requests` metric:

```
{"http.server.active_requests"}
```

The following example selects all time series for the metric `http.server.active_requests`
where the OpenTelemetry resource attribute `service.name` equals `myservice`:

```
{"http.server.active_requests", "@resource.service.name"="myservice"}
```

You can combine multiple label matchers in a single query. The following example selects all time
series for the `http.server.active_requests` metric where the OpenTelemetry resource
attribute `service.name` equals `myservice` across all US regions:

```
{"http.server.active_requests",
 "@resource.service.name"="myservice",
 "@aws.region"=~"us-.*"}
```

The following example shows a range query. It calculates the average value of all datapoints
within a specified time range for each time series:

```
avg_over_time(
  {"http.server.active_requests",
   "@resource.service.name"="myservice"}[5m]
)
```

The following table summarizes the prefix conventions for each OTLP scope:

| OTLP scope            | Fields prefix        | Attributes prefix     | Example                                    |
| --------------------- | -------------------- | --------------------- | ------------------------------------------ |
| Resource              | `@resource.@`        | `@resource.`          | `@resource.service.name="myservice"`       |
| Instrumentation Scope | `@instrumentation.@` | `@instrumentation.`   | `@instrumentation.@name="otel-go/metrics"` |
| Datapoint             | `@datapoint.@`       | `@datapoint.` or bare | `cpu="cpu0"` or `@datapoint.cpu="cpu0"`    |
| AWS-reserved          | N/A                  | `@aws.`               | `@aws.account_id="123456789"`              |

## Querying vended AWS metrics with PromQL

To be able to query vended AWS metrics in PromQL, you first need to enable OTel enrichment
of vended metrics. See: [Enabling vended metrics in PromQL](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md").

After you enable OTel enrichment, vended AWS metrics become queryable via PromQL with
additional labels. The metric name is the same as the original CloudWatch metric name, and the
original CloudWatch dimensions are available as datapoint attributes. The following labels are
available (the example below is for an EC2 instance):

| PromQL Label                             | Description                                               | Example                                                           |
| ---------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------- |
| `InstanceId`                             | Original CloudWatch dimension, as a datapoint attribute   | `i-0123456789abcdef0`                                             |
| `"@resource.cloud.resource_id"`          | Full ARN of the resource                                  | `arn:aws:ec2:us-east-1:123456789012:instance/i-0123456789abcdef0` |
| `"@resource.cloud.provider"`             | Cloud provider                                            | `aws`                                                             |
| `"@resource.cloud.region"`               | AWS Region where this metric originated                   | `us-east-1`                                                       |
| `"@resource.cloud.account.id"`           | AWS account ID where this metric originated               | `123456789012`                                                    |
| `"@instrumentation.@name"`               | Instrumentation scope name identifying the source service | `cloudwatch.aws/ec2`                                              |
| `"@instrumentation.cloudwatch.source"`   | Source service identifier                                 | `aws.ec2`                                                         |
| `"@instrumentation.cloudwatch.solution"` | Enrichment solution identifier                            | `CloudWatchOTelEnrichment`                                        |
| `"@aws.tag.Environment"`                 | AWS resource tag                                          | `production`                                                      |
| `"@aws.account"`                         | AWS account where this metric was ingested (system label) | `123456789012`                                                    |
| `"@aws.region"`                          | AWS Region where this metric was ingested (system label)  | `us-east-1`                                                       |

The following example selects `Invocations` for a specific Lambda function:

```
histogram_sum({Invocations, FunctionName="my-api-handler"})
```

The following example selects Lambda `Errors` for all functions tagged with a specific team:

```
histogram_sum(
  {Errors, "@instrumentation.@name"="cloudwatch.aws/lambda", "@aws.tag.Team"="backend"}
)
```

The following example computes the total Lambda `Invocations` grouped by team:

```
sum by ("@aws.tag.Team")(
    {Invocations, "@instrumentation.@name"="cloudwatch.aws/lambda"}
)
```

The following example selects all time series for the EC2 `CPUUtilization` metric.
The usage of `"@instrumentation.@name"="cloudwatch.aws/ec2"` is to exclusively match
CPUUtilization from EC2 and not from other AWS services such as Amazon Relational Database Service:

```
histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
```

# PromQL querying

When you ingest OpenTelemetry metrics into CloudWatch through the [Metrics endpoint](CloudWatch-OTLPEndpoint.md#CloudWatch-MetricsEndpoint "CloudWatch-OTLPEndpoint.md#CloudWatch-MetricsEndpoint"), the
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
of vended metrics. See: [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md").

After you enable OTel enrichment, vended AWS metrics become queryable through PromQL with
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

The following example selects all time series for the EC2 `CPUUtilization` metric.
The usage of `"@instrumentation.@name"="cloudwatch.aws/ec2"` is to exclusively match
CPUUtilization from EC2 and not from other AWS services such as Amazon Relational Database Service:

```
histogram_avg({CPUUtilization, "@instrumentation.@name"="cloudwatch.aws/ec2"})
```

## Querying from Grafana

You can query CloudWatch PromQL data from Grafana by adding the
**Amazon Managed Service for Prometheus** data source
plugin and pointing it at the CloudWatch monitoring endpoint. SigV4 signing is built in to
the plugin and is always enabled, so there is no toggle to turn on. The plugin is
published at [grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/](https://grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/ "https://grafana.com/grafana/plugins/grafana-amazonprometheus-datasource/"); install
it from the Grafana plugins catalog before adding the data source. AMP plugin v3.0.0
requires Grafana `>=11.6.11 <12 || >=12.0.10 <12.1 || >=12.1.7
 <12.2 || >=12.2.5`.

**IAM prerequisites** — the IAM principal whose
credentials Grafana uses must have both `cloudwatch:GetMetricData` (required
for instant and range queries) and `cloudwatch:ListMetrics` (required for
series and label discovery). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM "CloudWatch-PromQL.md#CloudWatch-PromQL-IAM").

To configure Grafana, complete the following steps.

1. Install the **Amazon Managed Service for
   Prometheus** data source plugin from the Grafana plugins
   catalog.
2. In Grafana, go to **Connections**,
   **Data sources**, choose
   **Add data source**, and select
   **Amazon Managed Service for Prometheus**.
3. Set the data source **URL** to
   `https://monitoring.`AWS
   Region`.amazonaws.com`.
4. Set the **Region** to your AWS Region. Choose
   an **Authentication provider** appropriate for
   your environment (default credential chain, access keys, or workspace IAM
   role).
5. Choose **Save & test**.

## Querying from Amazon Managed Grafana

You can query CloudWatch PromQL data from an Amazon Managed Grafana workspace by adding an
**Amazon Managed Service for Prometheus** data source
that points at the CloudWatch monitoring endpoint. This data source plugin signs requests
with SigV4 using the workspace IAM role automatically; SigV4 is always enabled, with
no toggle to configure. The plugin is available in Amazon Managed Grafana version 12
and later. For more information, see [Connect to an
Amazon Managed Service for Prometheus data source](../../../grafana/latest/userguide/amazon-prometheus-data-source.md "../../../grafana/latest/userguide/amazon-prometheus-data-source.md") in the
_Amazon Managed Grafana User Guide_.

**IAM prerequisites** — the Amazon Managed Grafana
workspace IAM role must have both `cloudwatch:GetMetricData` (required for
instant and range queries) and `cloudwatch:ListMetrics` (required for series
and label discovery). For details, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM "CloudWatch-PromQL.md#CloudWatch-PromQL-IAM").

To configure the data source, complete the following steps.

1. In your Amazon Managed Grafana workspace, add an
   **Amazon Managed Service for Prometheus** data
   source.
2. Set the data source **URL** to
   `https://monitoring.`AWS
   Region`.amazonaws.com`.
3. Set the **Region** to your AWS Region.
   Amazon Managed Grafana injects credentials from the workspace IAM role
   automatically; you do not need to configure static keys.
4. Choose **Save & test**.

## Querying with MCP tools

The [CloudWatch MCP Server](https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server/ "https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server/") provides Model Context Protocol (MCP) tools that let
AI assistants and development tools query CloudWatch PromQL data on your behalf. The MCP
tools handle authentication and request formatting automatically, so you can focus on
writing PromQL queries rather than managing HTTP requests and SigV4 signing.

The following PromQL tools are available in the CloudWatch MCP Server:

| Tool                         | Description                                                                                                                       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `execute_promql_query`       | Runs an instant PromQL query, returning metric values at a<br>single point in time.                                               |
| `execute_promql_range_query` | Runs a PromQL range query over a time window, returning time<br>series data for trend analysis and graphing.                      |
| `get_promql_label_values`    | Retrieves values for a specific PromQL label, such as<br>`__name__` for metric names or<br>`@resource.service.name` for services. |
| `get_promql_series`          | Finds time series matching PromQL label selectors and returns<br>the full label set of each matching series.                      |
| `get_promql_labels`          | Lists all available PromQL label names to help discover the<br>label structure of your metrics.                                   |

For full details on parameters, configuration, and setup instructions, see
[Tools for CloudWatch PromQL](https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server#tools-for-cloudwatch-promql "https://awslabs.github.io/mcp/servers/cloudwatch-mcp-server#tools-for-cloudwatch-promql") in the CloudWatch MCP Server documentation.

## Querying with the HTTP API

You can also query CloudWatch PromQL data programmatically by calling the
Prometheus-compatible HTTP endpoints directly. Requests must be signed with
[AWS
Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") using `monitoring` as the service name.

The PromQL endpoint follows the pattern
`https://monitoring.`AWS
Region`.amazonaws.com/api/v1/`operation``.
For example, for the US East (N. Virginia) (us-east-1) Region, the endpoint for an
instant query is
`https://monitoring.us-east-1.amazonaws.com/api/v1/query`.

For the full API reference, including supported operations, request parameters, and
response formats, see [Prometheus-compatible APIs](CloudWatch-PromQL-APIs.md "CloudWatch-PromQL-APIs.md"). For the list of AWS Regions where
PromQL querying is available, see [Supported AWS Regions](CloudWatch-PromQL.md#CloudWatch-PromQL-Regions "CloudWatch-PromQL.md#CloudWatch-PromQL-Regions"). For the IAM actions required for
each operation, see [IAM permissions for PromQL](CloudWatch-PromQL.md#CloudWatch-PromQL-IAM "CloudWatch-PromQL.md#CloudWatch-PromQL-IAM").



# Choose a configuration model for the CloudWatch agent

The Amazon CloudWatch agent (CloudWatch agent) configuration supports three configuration models. Each model collects metrics, logs, and traces. The models differ in configuration format, available sources, metric destination and data model, and how you query metrics.
+ **Classic** – You configure the `metrics`, `logs`, and `traces` sections in the CloudWatch agent JSON file. Metrics publish as CloudWatch metrics in a namespace (`CWAgent` by default), logs go to CloudWatch Logs, and traces go to X-Ray. You query metrics with CloudWatch Metrics Insights and metric math.
+ **Curated OpenTelemetry** – You configure the `opentelemetry` section in the CloudWatch agent JSON file. The agent sends metrics, logs, and traces to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints. You query metrics with PromQL (Prometheus Query Language).
+ **Native OpenTelemetry (YAML)** – You provide a standard OpenTelemetry Collector configuration in YAML, appended to the CloudWatch agent JSON configuration file. This model exposes the full OpenTelemetry Collector receiver, processor, and exporter ecosystem, and sends to the CloudWatch OTLP endpoints.

You can combine models in a single configuration. For example, you can collect host metrics with the `opentelemetry` section and procstat metrics with the `metrics` section in one file. For more information about combining configuration models, see [Use more than one model in one configuration](#CloudWatch-Agent-config-model-both).

We recommend an OpenTelemetry model—either the curated or the native model—for new workloads. For more information about the recommended OpenTelemetry models, see [OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md).

**Note**  
The models differ in how metrics are billed. The Classic model publishes custom metrics, billed for each metric, while the OpenTelemetry models are billed for each GB ingested. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

## Compare the configuration models
<a name="CloudWatch-Agent-config-model-compare"></a>

The following table compares the Classic, Curated OpenTelemetry, and Native OpenTelemetry (YAML) configuration models.


| Attribute | Classic | Curated OpenTelemetry | Native OpenTelemetry (YAML) | 
| --- | --- | --- | --- | 
| Configuration format | CloudWatch agent JSON—metrics, logs, traces sections | CloudWatch agent JSON—opentelemetry section | OpenTelemetry Collector configuration (YAML), appended to the agent configuration | 
| Signals collected | Metrics, logs, and traces | Metrics, logs, and traces | Metrics, logs, and traces | 
| Metric destination | CloudWatch metrics in a namespace (CWAgent by default) | CloudWatch OTLP metrics endpoint | CloudWatch OTLP metrics endpoint | 
| Metric data model and query | Dimensions, up to 30 per metric; query with CloudWatch Metrics Insights and metric math | Labels including resource attributes, up to 150 per data point; query with PromQL | OpenTelemetry metrics, up to 150 labels; query with PromQL | 
| Log destination | CloudWatch Logs | CloudWatch Logs (OTLP logs endpoint) | CloudWatch Logs (OTLP logs endpoint) | 
| Trace destination | X-Ray | X-Ray (OTLP traces endpoint, viewed in Transaction Search) | X-Ray (OTLP traces endpoint, viewed in Transaction Search) | 
| Sources | Host metrics, log files, Windows events, Prometheus, OTLP, StatsD, collectd, procstat, Java Management Extensions (JMX), NVIDIA GPU, and other plugins | host\_metrics, prometheus, otlp, database\_insights (metrics); files, windows\_events, otlp (logs); otlp (traces) | The full OpenTelemetry Collector receiver set, including receivers the curated section does not expose, such as collectd and statsd | 
| Metric pricing | Per custom metric | Per GB ingested. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md). | Per GB ingested. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md). | 
| Configuration wizard | [Supported](create-cloudwatch-agent-configuration-file-wizard.md) | Not supported; author manually | Not supported; author manually | 
| Example configuration | [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md) | [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md) | [Appending OpenTelemetry collector configuration files](CloudWatch-Agent-appending-OpenTelemetry-config-files.md) | 
| Minimum agent version | Depends on the plugin | 1.300070.0 | Not applicable | 

## Which model to use
<a name="CloudWatch-Agent-config-model-choose"></a>

Use the Classic model when any of the following apply:
+ You want to use the configuration wizard.
+ You have dashboards and alarms that use metrics in the `CWAgent` namespace, and you aren't ready to migrate them. For more information, see [Migrate from Classic to OTel metrics](metrics-otel-migrate.md).

Use the Curated OpenTelemetry model when any of the following apply:
+ You're setting up a new workload.
+ You want to query metrics with PromQL, or use existing PromQL dashboards and alarms.
+ You need high-cardinality labels, such as resource attributes, on your metrics.
+ Your sources are covered by the curated set, such as host metrics, Prometheus, OTLP applications, and database insights.

Use the Native OpenTelemetry (YAML) model when any of the following apply:
+ You need a collector receiver that the `opentelemetry` section doesn't expose, such as `collectd` or `statsd`.
+ You already maintain OpenTelemetry Collector YAML.
+ You need custom collector processors or pipelines.

## Use more than one model in one configuration
<a name="CloudWatch-Agent-config-model-both"></a>

You can include the `opentelemetry` section and Classic sections in the same configuration file. For example, you can collect host metrics and OTLP data with the `opentelemetry` section, and collect procstat metrics with the `metrics` section. This is useful while you migrate from Classic metrics. You can also append a Native OpenTelemetry (YAML) collector configuration to run alongside the JSON configuration.

**Important**  
Don't configure an `otlp` source in both the `opentelemetry` section and the `metrics` section on the same endpoints. If both use the default endpoints (`127.0.0.1:4317` and `127.0.0.1:4318`), the agent sends each data point that it receives to both the CloudWatch OTLP endpoint and to the `CWAgent` namespace. You're charged for both. If you need both, set different ports for each `otlp` source.

## Common customizations
<a name="CloudWatch-Agent-OpenTelemetry-config-customize"></a>

The following table shows how to make common changes in the OpenTelemetry configuration, and the Classic setting that each one replaces.


| To do this | In the OpenTelemetry configuration | Classic setting | 
| --- | --- | --- | 
| Add labels, such as an environment or team, to all telemetry | Set `resource_attributes` in the `opentelemetry` section. Each attribute becomes a label, such as `@resource.deployment.environment.name`. | `append_dimensions` | 
| Aggregate metrics across instances | Aggregate at query time with PromQL, for example `avg by ("@resource.cloud.availability_zone") ({"system.cpu.utilization"})`. No agent setting is needed. | `aggregation_dimensions` | 
| Collect metrics more or less often | Set `collection_interval` in `host_metrics`, or `scrape_interval` in the Prometheus scrape configuration. | `metrics_collection_interval` | 
| Keep or drop specific scraped metrics | Add `metric_relabel_configs` to the scrape job in the Prometheus scrape configuration, as shown after this table. | `measurement`, `drop_original_metrics` | 
| Send telemetry to a different account | Set `role_arn` under `credentials` in the `agent` section. | `role_arn` in each section | 

The following scrape job keeps only metrics whose names start with `http_server_`:

```yaml
scrape_configs:
  - job_name: my-app
    static_configs:
      - targets: ['127.0.0.1:9404']
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'http_server_.*'
        action: keep
```

The `host_metrics` source doesn't support selecting individual metrics. It collects the metrics listed in [Host metrics that the agent collects](CloudWatch-Agent-OpenTelemetry-config-collect-host-metrics.md#CloudWatch-Agent-OpenTelemetry-config-host-metrics).

## Create an agent configuration file
<a name="CloudWatch-Agent-config-model-create"></a>

To create a configuration for an OpenTelemetry model, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md). To create a configuration for the Classic model, see [Create the CloudWatch agent configuration file with the wizard](create-cloudwatch-agent-configuration-file-wizard.md) or [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md).
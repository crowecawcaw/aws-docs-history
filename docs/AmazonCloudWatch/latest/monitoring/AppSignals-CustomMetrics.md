# Custom metrics with Application Signals

To monitor application performance and availability, Application Signals collects standard metrics (faults, errors, and latency) and runtime metrics from discovered applications after you enable it.

Custom Metrics add valuable context to your application monitoring and help expedite troubleshooting. You can use them to:

- Customize analysis of telemetry data
- Identify root causes of issues
- Make precise business and operational decisions quickly
  Application Signals lets you view and correlate custom metrics generated from a service with standard and runtime metrics. For example, an application could emit metrics for request size and cache miss count. These custom metrics provide more granular insight into performance issues, helping you diagnose and resolve availability drops and latency spikes faster.

###### Topics

- [Configuring custom metrics to Application Signals](#AppSignals-CustomMetrics-Adding "#AppSignals-CustomMetrics-Adding")
- [Viewing custom metrics in Application Signals](#AppSignals-CustomMetrics-Viewing "#AppSignals-CustomMetrics-Viewing")
- [Frequently asked questions (FAQs)](#AppSignals-CustomMetrics-FAQ "#AppSignals-CustomMetrics-FAQ")

## Configuring custom metrics to Application Signals

You can generate custom metrics from your application using two methods: _OpenTelemetry metrics_ and _Span metrics_.

###### Topics

- [OpenTelemetry metrics](#AppSignals-CustomMetrics-OpenTelemetry "#AppSignals-CustomMetrics-OpenTelemetry")
- [Span metrics](#AppSignals-CustomMetrics-SpanMetrics "#AppSignals-CustomMetrics-SpanMetrics")

### OpenTelemetry metrics

To use custom OpenTelemetry metrics with Application Signals, you must use either the CloudWatch Agent or OpenTelemetry Collector. Custom OpenTelemetry metrics allow you to create and export metrics directly from your application code using the OpenTelemetry Metrics SDK.

1. Onboard service to Application Signals.
2. Configure the agent or collector.
   - When using the CloudWatch agent, you must [configure](CloudWatch-Agent-OpenTelemetry-metrics.md "CloudWatch-Agent-OpenTelemetry-metrics.md") `metrics_collected` with an `otlp`. For example, `cloudwatch-config.json`

   ```
   {
     "traces": {
       "traces_collected": {
         "application_signals": {}
       }
     },
     "logs": {
       "metrics_collected": {
         "application_signals": {},
         "otlp": {
           "grpc_endpoint": "0.0.0.0:4317",
           "http_endpoint": "0.0.0.0:4318"
         }
       }
     }
   }
   ```

   - When using OpenTelemetry Collector, configure a metrics pipeline.
     You must use [CloudWatch EMF Exporter for OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awsemfexporter "https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awsemfexporter") and
     enable [Resource Attributes to Metric Labels](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awsemfexporter#resource-attributes-to-metric-labels "https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awsemfexporter#resource-attributes-to-metric-labels"). It's recommended to configure `dimension_rollup_option: NoDimensionRollup` to
     avoid emitting many metric aggregations. For example, `config.yaml`:

   ```
   receivers:
     otlp:
       protocols:
         grpc:
           endpoint: 0.0.0.0:4317
         http:
           endpoint: 0.0.0.0:4318

   exporters:
     awsemf:
       region: $REGION
       namespace: $NAMESPACE
       log_group_name:$LOG_GROUP_NAME
       resource_to_telemetry_conversion:
         enabled: true
       dimension_rollup_option: "NoDimensionRollup"

     otlphttp/traces:
       compression: gzip
       traces_endpoint: https://xray.$REGION.amazonaws.com/v1/traces
       auth:
         authenticator: sigv4auth/traces

   extensions:
     sigv4auth/logs:
       region: "$REGION"
       service: "logs"
     sigv4auth/traces:
       region: "$REGION"
       service: "xray"

   processors:
     batch:

   service:
     telemetry:
     extensions: [sigv4auth/logs, sigv4auth/traces]
     pipelines:
       metrics:
         receivers: [otlp]
         processors: [batch]
         exporters: [awsemf]
       traces:
         receivers: [otlp]
         processors: [batch]
         exporters: [otlphttp/traces]
   ```

3. Configure the environment. When there are multiple services with the same service name and to accurately correlate Application Signals metrics to the correct service name, it's recommended to configure the resource attribute `deployment.environment.name`.
   Configuring this resource attribute is commonly done through the environment variables.

```
OTEL_RESOURCE_ATTRIBUTES="service.name=$YOUR_SVC_NAME,deployment.environment.name=$YOUR_ENV_NAME"
```

4. Configure metric export to the CloudWatch agent or OpenTelemetry Collector. You can use one of the following approach:
   - (Recommended) Custom export pipeline – In the application code, create a dedicated [MeterProvider](https://opentelemetry.io/docs/specs/otel/metrics/sdk/#meterprovider "https://opentelemetry.io/docs/specs/otel/metrics/sdk/#meterprovider") exporting to the configured agent or collector endpoint. For example:

   ```
   Resource resource = Resource.getDefault().toBuilder()
           .put(AttributeKey.stringKey("service.name"), serviceName)
           .put(AttributeKey.stringKey("deployment.environment.name"), environment)
           .build();

   MetricExporter metricExporter = OtlpHttpMetricExporter.builder()
           .setEndpoint("http://localhost:4318/v1/metrics")
           .build();

   MetricReader metricReader = PeriodicMetricReader.builder(metricExporter)
           .setInterval(Duration.ofSeconds(10))
           .build()

   SdkMeterProvider meterProvider = SdkMeterProvider.builder()
       .setResource(resource)
       .registerMetricReader()
       .build();

   Meter meter = meterProvider.get("myMeter");
   ```

   - Agent-based export – Configure the agent environment variables [OTEL_METRICS_EXPORTER](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#exporter-selection "https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#exporter-selection") and
     [OTEL_EXPORTER_OTLP_METRICS_ENDPOINT](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#otel_exporter_otlp_metrics_endpoint "https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#otel_exporter_otlp_metrics_endpoint"). For example:

   ```
   OTEL_METRICS_EXPORTER=otlp
   OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://localhost:4318/v1/metrics
   ```

   In application code, rely on global MeterProvider created by the agent. For example:

   ```
   Meter meter = GlobalOpenTelemetry.getMeter("myMeter");
   ```

5. Using the [OTEL Metrics SDK](https://opentelemetry.io/docs/specs/otel/metrics/sdk/ "https://opentelemetry.io/docs/specs/otel/metrics/sdk/") in the application code, add the OTEL Metrics. For example, to add the OTEL metrics in Python:

```
counter = meter.counterBuilder("myCounter").build();
counter.add(value);
counter.add(value, Attributes.of(AttributeKey.stringKey("Operation"), "myOperation"));
```

Adding the Operation attribute is not required, but can be useful for correlating Application Signals Service Operations to Custom OpenTelemetry Metrics.

### Span metrics

Custom Span metrics currently only work with Transaction Search. With custom Span metrics, you can:

- Create metrics using Metrics Filters
- Process span attributes added in application code
- Use the OpenTelemetry Traces SDK for implementation

1. Enable Application Signals monitoring with Transaction Search. For more information, see [Transaction Search](CloudWatch-Transaction-Search-getting-started.md "CloudWatch-Transaction-Search-getting-started.md").

To ensure 100% metric sampling, it's recommended to send 100% of spans to the endpoint. 2. Add span attributes using the [OTEL Traces SDK](https://opentelemetry.io/docs/specs/otel/trace/sdk/ "https://opentelemetry.io/docs/specs/otel/trace/sdk/"). There are two ways:

    * [Recommended] Add attributes to automatically generated spans. For example:



    ```
    Span.current().setAttribute("myattribute", value);
    ```
    * Add attributes to manually generated spans. For example:



    ```
    Span span = tracer.spanBuilder("myspan").startSpan();
    try (Scope scope = span.makeCurrent()) {
       span.setAttribute("myattribute",  value);
    }
    ```

3. Create a metric filter with the following values. For information on how to create a metric filter, see [Create a metric filter for a log group](../logs/CreateMetricFilterProcedure.md "../logs/CreateMetricFilterProcedure.md").
   - Log Group – aws/spans
   - Filter pattern – { $.attributes.['myattribute'] = \* }
   - Metric name – myattribute (The values must be an exact match or span correlation will not work
   - Metric value – $.attributes.['myattribute']
   - Dimensions – Field Name: Service, Field Value: $.attributes.['aws.local.service'], Field Name: Environment, Field Value: $.attributes.['aws.local.environment'], and Field Name: Operation, Field Value: $.attributes.['aws.local.operation']

   ###### Note

   When you add attributes to manually generated spans, you cannot set `Operation` because `aws.local.operation` will not be present in span data.

## Viewing custom metrics in Application Signals

You can now view custom metrics for services and operations in the Application Signals console:

- Select a service from the **Services** list to see the new **Related Metrics** tab
- View standard metrics, runtime metrics, and related metrics for your selected service
- Filter and select multiple metrics from the list
- Graph selected metrics to identify correlations and root causes of issues

For more information on Related Metrics, see [View Related metrics](ServiceDetail.md#ServiceDetail-relatedmetrics "ServiceDetail.md#ServiceDetail-relatedmetrics").

## Frequently asked questions (FAQs)

### What is the impact of not adding the configuration for environment for custom metrics?

Application Signals configures the `deployment.environment.name` resource attribute to disambiguate applications. Application Signals cannot correlate custom metrics generated from two different services with the same name to the correct service without disambiguation.

To add environment configuration to your application, see [OpenTelemetry metrics](#AppSignals-CustomMetrics-OpenTelemetry "#AppSignals-CustomMetrics-OpenTelemetry").

### Are there any limits for metrics filters?

You can only create up to 100 metrics filters per CloudWatch Logs log group. Each metric defined can have up to 3 dimensions. You can view limits for metrics filters here [OpenTelemetry metrics](#AppSignals-CustomMetrics-OpenTelemetry "#AppSignals-CustomMetrics-OpenTelemetry").

### Why aren't metric graphs appearing in the metrics table?

The solution depends on your metric type:

- Custom metrics – See [Configuring custom metrics to Application Signals](#AppSignals-CustomMetrics-Adding "#AppSignals-CustomMetrics-Adding") to verify the metric configuration
- Standard or runtime metrics – See [Troubleshooting your Application Signals installation](CloudWatch-Application-Signals-Enable-Troubleshoot.md "CloudWatch-Application-Signals-Enable-Troubleshoot.md")

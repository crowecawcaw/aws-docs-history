# Use metric streams

You can use _metric streams_ to continually stream CloudWatch metrics to a
destination of your choice, with near-real-time delivery and low latency. Supported
destinations include AWS destinations such as Amazon Simple Storage Service and several third-party service
provider destinations.

There are three main usage scenarios for CloudWatch metric streams:

- **Custom setup with Firehose**— Create a metric stream and direct it to an
  Amazon Data Firehose delivery stream that delivers your CloudWatch metrics to where you want them to go.
  You can stream them to a data lake such as
  Amazon S3, or to any destination or endpoint supported by Firehose including third-party providers.
  JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0 formats are supported natively,
  or you can configure transformations in your Firehose delivery stream to convert the data to a different format such as Parquet. With a metric stream,
  you can continually
  update monitoring data, or combine this
  CloudWatch metric data with billing and performance data to create rich datasets. You can
  then use tools such as Amazon Athena to get insight into cost optimization, resource
  performance, and resource utilization.
- **Quick S3 setup**— Stream to Amazon Simple Storage Service with a quick
  setup process. By default, CloudWatch creates the resources needed for the stream. JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0 formats
  are supported.
- **Quick AWS partner setup**— CloudWatch provides a quick setup
  experience for some third-party partners. You can use third-party
  service providers to monitor, troubleshoot, and analyze your applications using the streamed
  CloudWatch data. When you use the quick partner setup workflow, you need to provide only a
  destination URL and API key for your destination, and CloudWatch
  handles the rest of the setup. Quick partner setup is available for the following third-party providers:

      + Datadog
      + Dynatrace
      + Elastic
      + New Relic
      + Splunk Observability Cloud
      + SumoLogic

  You can stream all of your CloudWatch metrics, or use filters to stream only specified metrics. Each metric
  stream can include up to 1000 filters that
  either include or exclude metric namespaces or specific metrics. A single metric stream can have only include or
  exclude filters, but not both.

After a metric stream is created, if new metrics are created that match the filters in place,
the new metrics are automatically included in the stream.

There is no limit on the number of metric streams per account or per Region, and no limit
on the number of metric updates being streamed.

Each stream can use either JSON format, OpenTelemetry 1.0.0, or OpenTelemetry 0.7.0 format. You can edit the output format
of a metric stream at any time, such as for upgrading from OpenTelemetry 0.7.0 to OpenTelemetry 1.0.0. For more information
about output formats, see [CloudWatch metric stream output in JSON format](CloudWatch-metric-streams-formats-json.md "CloudWatch-metric-streams-formats-json.md"), [CloudWatch metric stream output in OpenTelemetry 1.0.0 format](CloudWatch-metric-streams-formats-opentelemetry-100.md "CloudWatch-metric-streams-formats-opentelemetry-100.md"), and [CloudWatch metric stream output in OpenTelemetry 0.7.0 format](CloudWatch-metric-streams-formats-opentelemetry.md "CloudWatch-metric-streams-formats-opentelemetry.md").

For metric streams in monitoring accounts, you can choose whether to include metrics from the source accounts linked to
that monitoring account.
For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

Metric streams always include the `Minimum`, `Maximum`, `SampleCount`,
and `Sum` statistics. You can also choose to include additional statistics at an additional
charge. For more information,
see [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md "CloudWatch-metric-streams-statistics.md").

Metric streams pricing is based on the number of metric updates. You also incur charges from Firehose
for the delivery stream used for the metric stream. For more information, see
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Set up a metric stream](CloudWatch-metric-streams-setup.md "CloudWatch-metric-streams-setup.md")
- [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md "CloudWatch-metric-streams-statistics.md")
- [Metric stream
  operation and maintenance](CloudWatch-metric-streams-operation.md "CloudWatch-metric-streams-operation.md")
- [Monitoring your metric streams with
  CloudWatch metrics](CloudWatch-metric-streams-monitoring.md "CloudWatch-metric-streams-monitoring.md")
- [Trust between CloudWatch and Firehose](CloudWatch-metric-streams-trustpolicy.md "CloudWatch-metric-streams-trustpolicy.md")
- [CloudWatch metric stream output in JSON format](CloudWatch-metric-streams-formats-json.md "CloudWatch-metric-streams-formats-json.md")
- [CloudWatch metric stream output in OpenTelemetry 1.0.0 format](CloudWatch-metric-streams-formats-opentelemetry-100.md "CloudWatch-metric-streams-formats-opentelemetry-100.md")
- [CloudWatch metric stream output in OpenTelemetry 0.7.0 format](CloudWatch-metric-streams-formats-opentelemetry.md "CloudWatch-metric-streams-formats-opentelemetry.md")
- [Troubleshooting metric streams in CloudWatch](CloudWatch-metric-streams-troubleshoot.md "CloudWatch-metric-streams-troubleshoot.md")

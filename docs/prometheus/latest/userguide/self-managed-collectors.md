# Customer managed collectors

This section contains information about ingesting data by setting up your own collectors
that send metrics to Amazon Managed Service for Prometheus using Prometheus remote write.

When you use your own collectors to send metrics to Amazon Managed Service for Prometheus, you are responsible for
securing your metrics and making sure that the ingestion process meets your availability
needs.

Most customer managed collectors use one of the following tools:

- **AWS Distro for OpenTelemetry (ADOT)** –
  ADOT is a fully supported, secure, production-ready open source distribution of
  OpenTelemetry that provides agents to collect metrics. You can use ADOT to collect
  metrics and send them to your Amazon Managed Service for Prometheus workspace. For more information about the
  ADOT Collector, see [AWS Distro for
  OpenTelemetry](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/").
- **Prometheus agent** – You can set up your own
  instance of the open source Prometheus server, running as an agent, to collect
  metrics and forward them to your Amazon Managed Service for Prometheus workspace.
  The following topics describe using both of these tools and include general information
  about setting up your own collectors.

###### Topics

- [Secure the ingestion of your
  metrics](AMP-secure-metric-ingestion.md "AMP-secure-metric-ingestion.md")
- [Using AWS Distro for OpenTelemetry as a
  collector](AMP-ingest-with-adot.md "AMP-ingest-with-adot.md")
- [Using a Prometheus instance as a
  collector](AMP-ingest-with-prometheus.md "AMP-ingest-with-prometheus.md")
- [Set up Amazon Managed Service for Prometheus for high
  availability data](AMP-ingest-high-availability.md "AMP-ingest-high-availability.md")

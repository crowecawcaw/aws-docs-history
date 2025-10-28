# Using a Prometheus instance as a

collector

You can use a Prometheus instance, running in _agent_ mode (known
as a _Prometheus agent_), to scrape metrics and send them to your
Amazon Managed Service for Prometheus workspace.

The following topics describe different ways to set up a Prometheus instance running
in agent mode as a collector for your metrics.

###### Warning

When you create a Prometheus agent, you are responsible for its configuration and
maintenance. Avoid exposing Prometheus scrape endpoints to the public internet by
[enabling security features](https://prometheus.io/docs/prometheus/latest/configuration/https/ "https://prometheus.io/docs/prometheus/latest/configuration/https/").

If you set up multiple Prometheus instances that monitor the same set of metrics and
sent them to a single Amazon Managed Service for Prometheus workspace for high availability, you need to set up
deduplication. If you don't follow the steps to set up deduplication, you will be
charged for all data samples sent to Amazon Managed Service for Prometheus, including duplicate samples. For
instructions about setting up deduplication, see [Deduplicating high availability metrics sent to
Amazon Managed Service for Prometheus](AMP-ingest-dedupe.md "AMP-ingest-dedupe.md").

###### Topics

- [Set up ingestion from a
  new Prometheus server using Helm](AMP-onboard-ingest-metrics-new-Prometheus.md "AMP-onboard-ingest-metrics-new-Prometheus.md")
- [Set up ingestion
  from an existing Prometheus server in Kubernetes on EC2](AMP-onboard-ingest-metrics-existing-Prometheus.md "AMP-onboard-ingest-metrics-existing-Prometheus.md")
- [Set up
  ingestion from an existing Prometheus server in Kubernetes on Fargate](AMP-onboard-ingest-metrics-existing-Prometheus-fargate.md "AMP-onboard-ingest-metrics-existing-Prometheus-fargate.md")

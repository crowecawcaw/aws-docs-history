# Ingest metrics to your Amazon Managed Service for Prometheus

workspace

Metrics must be ingested into your Amazon Managed Service for Prometheus workspace before you can query or alert on
those metrics. This section explains how to set up the ingestion of metrics into your
workspace.

###### Note

Metrics ingested into a workspace are stored for 150 days by default, and are
then automatically deleted. You can adjust the retention period by configuring your workspace up to a maximum of 1095 days (three years). For more information, see [Configure your workspace](AMP-workspace-configuration.md "AMP-workspace-configuration.md").

There are two methods of ingesting metrics into your Amazon Managed Service for Prometheus workspace.

- **Using an AWS managed collector** – Amazon Managed Service for Prometheus
  provides a fully-managed, agentless scraper to automatically
  _scrape_ metrics from your Amazon Elastic Kubernetes Service (Amazon EKS) clusters.
  Scraping automatically pulls the metrics from Prometheus-compatible
  endpoints.
- **Using a customer managed collector** – You have
  many options for managing your own collector. Two of the most common
  collectors to use are installing your own instance of Prometheus, running in agent
  mode, or using AWS Distro for OpenTelemetry. These are both described in detail in
  the following sections.

Collectors send metrics to Amazon Managed Service for Prometheus using Prometheus remote write functionality.
You can directly send metrics to Amazon Managed Service for Prometheus by using Prometheus remote write in your
own application. For more details about directly using remote write, and remote
write configurations, see [remote_write](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write "https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write") in the Prometheus documentation.

###### Topics

- [Ingest metrics with AWS managed collectors](AMP-collector.md "AMP-collector.md")
- [Customer managed collectors](self-managed-collectors.md "self-managed-collectors.md")

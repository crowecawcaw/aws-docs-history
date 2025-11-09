# Send high-availability data to

Amazon Managed Service for Prometheus with AWS Distro for OpenTelemetry

AWS Distro for OpenTelemetry (ADOT) is a secure and production-ready
distribution of the OpenTelemetry project. ADOT provides you with source APIs,
libraries, and agents, so you can collect distributed traces and metrics for
application monitoring. For information about ADOT, see [About AWS Distro for Open
Telemetry](https://aws-otel.github.io/about "https://aws-otel.github.io/about").

To set up ADOT with a high availability configuration, you must configure an ADOT
collector container image and apply the external labels `cluster` and
`__replica__` to the AWS Prometheus remote write exporter. This
exporter sends your scraped metrics to your Amazon Managed Service for Prometheus workspace via the
`remote_write` endpoint. When you set these labels on the remote
write exporter, you prevent duplicate metrics from being kept while redundant
replicas run. For more information about the AWS Prometheus remote write exporter,
see [Getting started with Prometheus remote write exporter for
Amazon Managed Service for Prometheus](https://aws-otel.github.io/docs/getting-started/prometheus-remote-write-exporter "https://aws-otel.github.io/docs/getting-started/prometheus-remote-write-exporter").

###### Note

Certain versions of Kubernetes (1.28 and 1.29) may emit their own metric with
a `cluster` label. This can cause issues with Amazon Managed Service for Prometheus
deduplication. See the [High availability
FAQ](HA_FAQ.md#HA_FAQ_cluster-label "HA_FAQ.md#HA_FAQ_cluster-label") for more information.

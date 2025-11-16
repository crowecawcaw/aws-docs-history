# What are Prometheus-compatible

metrics?

To scrape Prometheus metrics from your applications and infrastructure for use in
Amazon Managed Service for Prometheus, they must instrument and expose _Prometheus-compatible
metrics_ from Prometheus-compatible `/metrics` endpoints. You
can implement your own metrics, but you don't have to. Kubernetes (including Amazon EKS) and
many other libraries and services implement these metrics directly.

When metrics in Amazon EKS are exported to a Prometheus-compatible endpoint, you can have
those metrics automatically scraped by the Amazon Managed Service for Prometheus collector.

For more information, see the following topics:

- For more information about existing libraries and services that export metrics
  as Prometheus metrics, see [Exporters and
  integrations](https://prometheus.io/docs/instrumenting/exporters/ "https://prometheus.io/docs/instrumenting/exporters/") in the Prometheus documentation.
- For more information about exporting Prometheus-compatible metrics from your
  own code, see [Writing
  exporters](https://prometheus.io/docs/instrumenting/writing_exporters/ "https://prometheus.io/docs/instrumenting/writing_exporters/") in the Prometheus documentation.
- For more information about how to set up an Amazon Managed Service for Prometheus collector to scrape
  metrics from your Amazon EKS clusters automatically, see [Set up managed collectors for Amazon EKS](AMP-collector-how-to.md "AMP-collector-how-to.md").

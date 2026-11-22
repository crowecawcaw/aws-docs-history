

# Custom telemetry

Besides the telemetry that Container Insights and Application Signals collect, the Amazon CloudWatch Observability add-on and Helm chart can send your own application telemetry to CloudWatch. The add-on adds the same Kubernetes and cloud attributes to it as Container Insights adds to the pod that sent it, so you can correlate your application data with your infrastructure metrics. For the list of attributes, see [Standard telemetry attributes](eks-standard-telemetry-attributes.md).
+ [OTLP ingestion](eks-observability-addon-otlp-endpoint.md) – Your applications and collectors push metrics, traces, and logs to the CloudWatch agent over OTLP.
+ [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md) – The CloudWatch agent scrapes the Prometheus targets that your ServiceMonitor and PodMonitor objects describe.

To control which of this telemetry the add-on sends, see [Telemetry filters](eks-observability-addon-telemetry-filters.md). That topic lists which filters apply to each source.

**Topics**
+ [OTLP ingestion](eks-observability-addon-otlp-endpoint.md)
+ [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md)
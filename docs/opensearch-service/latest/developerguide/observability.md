

# Observability in Amazon OpenSearch Service
<a name="observability"></a>

Observability is the practice of understanding the internal state and performance of complex systems by examining their outputs. Traditional monitoring tells you a system is down; observability helps you understand why by letting you ask new questions about your telemetry data.

## What Amazon OpenSearch Service provides
<a name="observability-what"></a>

Amazon OpenSearch Service provides a unified observability solution by collecting, correlating, and visualizing three types of telemetry data:
+ **Logs** – Timestamped records of events.
+ **Traces** – End-to-end journey of requests through distributed services.
+ **Metrics** – Time-series data representing system health, through the Amazon Managed Service for Prometheus direct query integration.

By bringing these together in a single interface, Amazon OpenSearch Service helps operations teams, SREs, and developers detect, diagnose, and resolve issues faster.

## The Amazon OpenSearch Service approach to observability
<a name="observability-approach"></a>

Amazon OpenSearch Service differentiates itself in three key ways:
+ **OpenTelemetry-native with OpenSearch Ingestion as the last mile** – Standardize on OTel for instrumentation and collection. Amazon OpenSearch Ingestion serves as the fully managed pipeline that filters, enriches, transforms, and routes your telemetry data before indexing.
+ **Unified logs, traces, and metrics in OpenSearch UI** – Analyze all three signal types from a single observability workspace. Correlate a slow trace to its application logs, or overlay Prometheus metrics on your service dashboards.
+ **Purpose-driven query languages** – Use [Piped Processing Language (PPL)](https://observability.opensearch.org/docs/ppl/) for logs and traces, and PromQL for metrics. Each language is optimized for its signal type, giving you expressive querying without compromise.

![Architecture diagram showing OpenTelemetry data flow from microservices through OTel Collector to OpenSearch Observability Stack components.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/otel-sdk-service.png)


**Note**  
The observability features described in this section are available only in OpenSearch UI. They are not available in OpenSearch Dashboards. For new observability workloads, we recommend setting up an [Using OpenSearch UI in Amazon OpenSearch Service](application.md) with an observability workspace.
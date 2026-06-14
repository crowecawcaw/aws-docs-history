# Metrics in Amazon CloudWatch

Metrics are data about the performance of your systems. Amazon CloudWatch collects metrics
through two paths: AWS vended metrics from services such as Amazon EC2, Amazon EBS, and Amazon RDS,
and custom metrics that you publish using the OpenTelemetry Protocol (OTLP) or the CloudWatch
API.

## Overview

### OpenTelemetry: open-source native metrics in CloudWatch

CloudWatch supports OpenTelemetry as the recommended path for metric ingestion and
querying. You can use vendor-agnostic, open-source instrumentation to send metrics to
CloudWatch – the same OTel SDKs and collectors that work with Prometheus, Grafana,
and other backends work with CloudWatch out of the box.

### Two metric models

CloudWatch supports two metric models. Both are fully supported – choose based on
your needs:

|                         | **[OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md "metrics-otel-recommended.md")** | **[CloudWatch Metrics (Classic)](metrics-classic.md "metrics-classic.md")** |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Ingestion**           | OTLP endpoint (OTel SDKs, collectors)                                                                | PutMetricData API, EMF                                                      |
| **Query language**      | PromQL                                                                                               | CloudWatch Metrics Insights (SQL)                                           |
| **Labels / Dimensions** | Up to 150 labels per data point                                                                      | Up to 30 dimensions per metric                                              |
| **Pricing model**       | Per GB ingested                                                                                      | Per metric per month                                                        |
| **Storage**             | Up to 15 months                                                                                      | Up to 15 months                                                             |
| **Metric names**        | Open-source native                                                                                   | Proprietary (CloudWatch-format)                                             |
| **Best for**            | New workloads, containers, high-cardinality                                                          | Existing integrations, low-cardinality AWS service<br>metrics               |

### Getting started

- **New to CloudWatch metrics?** Start with [OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md "metrics-otel-recommended.md").
- **Already using PutMetricData or EMF?** See [CloudWatch Metrics (Classic)](metrics-classic.md "metrics-classic.md").
- **Want AWS service metrics in PromQL?** Enable
  [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md").

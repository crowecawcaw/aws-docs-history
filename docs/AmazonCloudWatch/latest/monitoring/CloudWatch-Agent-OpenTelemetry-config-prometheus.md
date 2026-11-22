

# Scrape Prometheus metrics

The `prometheus` source scrapes applications that expose metrics in the Prometheus format and sends the metrics to the CloudWatch OTLP metrics endpoint. You query the metrics with PromQL. This source can include the following field:
+ `config_path` – Required. Specifies the path to the Prometheus scrape configuration file.

For the scrape configuration file format, a complete scrape and agent setup example, and service discovery options, see [Scrape Prometheus metrics on Amazon EC2 instances](CloudWatch-Agent-PrometheusEC2.md). To scrape JVM metrics with the Prometheus JMX exporter, see [Example: Scrape JVM metrics with the Prometheus JMX exporter](CloudWatch-Agent-PrometheusEC2.md#CloudWatch-Agent-Prometheus-Java).
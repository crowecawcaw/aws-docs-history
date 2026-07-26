# Amazon CloudWatch solution: Prometheus metric collection on Amazon Amazon EC2

This solution helps you collect Prometheus-compatible metrics from your Amazon EC2
instances without running or scaling your own collection infrastructure. You run one or more
Prometheus exporters on your instances, and a Amazon CloudWatch managed Prometheus collector
discovers the targets in your VPC, scrapes their `/metrics` endpoints, and delivers
the metrics to CloudWatch. For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md "Monitoring-Solutions.md"). For more information
about managed collectors, see [Amazon CloudWatch managed Prometheus collectors](managed-prometheus-collectors.md "managed-prometheus-collectors.md").

###### Topics

- [Requirements](#Solution-Prometheus-On-EC2-Requirements "#Solution-Prometheus-On-EC2-Requirements")
- [Enable Prometheus exporters](#Solution-Prometheus-On-EC2-Exporters "#Solution-Prometheus-On-EC2-Exporters")
- [Step 1: Set up the scrape configuration](#Solution-Prometheus-On-EC2-Scrape-Config "#Solution-Prometheus-On-EC2-Scrape-Config")
- [Step 2: Set up the scraper](#Solution-Prometheus-On-EC2-Create-Scraper "#Solution-Prometheus-On-EC2-Create-Scraper")
- [Validate metrics collection](#Solution-Prometheus-On-EC2-Validate "#Solution-Prometheus-On-EC2-Validate")
- [Build a custom dashboard](#Solution-Prometheus-On-EC2-Dashboards "#Solution-Prometheus-On-EC2-Dashboards")
- [Costs](#Solution-Prometheus-On-EC2-Costs "#Solution-Prometheus-On-EC2-Costs")

## Requirements

This solution is relevant for the following conditions:

- Compute: Amazon EC2 instances that run one or more Prometheus exporters.
- Amazon VPC with DNS enabled, and at least two subnets in different Availability
  Zones for the collector.
- A security group that allows the collector to reach the exporter ports on your
  instances.
- If you deploy the collector in private subnets that have no internet access, an
  interface VPC endpoint for CloudWatch. For more information, see [Configure VPC endpoints for private subnets](managed-prometheus-collectors-vpc-setup.md#managed-prometheus-collectors-vpc-endpoints "managed-prometheus-collectors-vpc-setup.md#managed-prometheus-collectors-vpc-endpoints").

## Enable Prometheus exporters

A Prometheus exporter is a process that exposes metrics in Prometheus
exposition format on an HTTP `/metrics` endpoint. You run an exporter that
matches the workload you want to monitor. The following exporters are commonly used on
Amazon EC2:

- **Node Exporter** — Host-level infrastructure
  metrics such as CPU, memory, disk, and network (default port 9100). For more
  information, see the [Node
  Exporter](https://github.com/prometheus/node_exporter "https://github.com/prometheus/node_exporter") repository on GitHub.
- **JMX Exporter** — JVM and Java application
  metrics for Java workloads. For more information, see the [JMX Exporter](https://github.com/prometheus/jmx_exporter "https://github.com/prometheus/jmx_exporter")
  repository on GitHub.
- **NGINX Prometheus Exporter** — NGINX web
  server and reverse proxy metrics. For more information, see the [NGINX Prometheus
  Exporter](https://github.com/nginx/nginx-prometheus-exporter "https://github.com/nginx/nginx-prometheus-exporter") repository on GitHub.
- **DCGM Exporter** — NVIDIA GPU metrics for GPU
  workloads such as machine learning training and inference (default port 9400). For more
  information, see the [DCGM
  Exporter](https://github.com/NVIDIA/dcgm-exporter "https://github.com/NVIDIA/dcgm-exporter") repository on GitHub.
- **HAProxy Exporter** — HAProxy load balancer
  metrics. For more information, see the [HAProxy Exporter](https://github.com/prometheus/haproxy_exporter "https://github.com/prometheus/haproxy_exporter")
  repository on GitHub.
- **Apache Exporter** — Apache HTTP Server metrics.
  For more information, see the [Apache Exporter](https://github.com/Lusitaniae/apache_exporter "https://github.com/Lusitaniae/apache_exporter")
  repository on GitHub.

Install and run each exporter on your instances by following its official documentation.
Note the port that each exporter listens on, because you reference these ports in your
scrape configuration. For a complete catalog of available exporters, see [Exporters and
integrations](https://prometheus.io/docs/instrumenting/exporters/ "https://prometheus.io/docs/instrumenting/exporters/") in the Prometheus documentation.

After you start an exporter, confirm that it exposes metrics by querying its endpoint
from the instance:

```
curl http://localhost:`port-number`/metrics
```

## Step 1: Set up the scrape configuration

The following example uses `static_configs` with the instance private DNS
names to scrape a sample application (port 8080) and Node Exporter (port 9100) on your Amazon EC2
instances. The `relabel_configs` section adds consistent labels to your metrics so
that you can query and filter across services. For the full set of supported configuration
options, see [Scraper configuration](managed-prometheus-collectors-scraper-configuration.md "managed-prometheus-collectors-scraper-configuration.md").

```
global:
  scrape_interval: 30s
  scrape_timeout: 10s

scrape_configs:
  - job_name: 'ec2-metrics'
    static_configs:
      - targets:
          - ip-`ip-address`.us-west-2.compute.internal:8080
    metrics_path: '/metrics'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        replacement: 'ec2-metrics-instance'
      - target_label: service
        replacement: 'ec2-metrics'
      - target_label: environment
        replacement: 'dev'
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: '.*'
        action: keep

  - job_name: ec2-node-exporter
    static_configs:
      - targets:
          - ip-`ip-address`.us-west-2.compute.internal:9100
```

## Step 2: Set up the scraper

Create a VPC-connected managed collector that scrapes your instances and delivers
metrics to your CloudWatch dataset. Provide the subnets and security group that allow the
collector to reach your exporter ports:

You can use [GetDefaultScraperConfiguration](../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md "../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md") to retrieve a general-purpose
scraper configuration, or provide your own.

AWS API
Use the `CreateScraper` API operation to create a scraper with a CloudWatch
destination. Replace the subnet, security group, and dataset information with your own
values.

```
POST /scrapers HTTP/1.1

{
  "alias": "ec2-payment-service-scraper",
  "source": {
    "vpcConfiguration": {
      "subnetIds": ["`subnet-subnet-id-1`", "`subnet-subnet-id-2`"],
      "securityGroupIds": ["`sg-security-group-id`"]
    }
  },
  "destination": {
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:`us-west-2`:`123456789012`:dataset/default"
    }
  },
  "scrapeConfiguration": {
    "configurationBlob": "`base64-encoded-blob`"
  }
}
```

AWS CLI
Use the `create-scraper` command to create a scraper with a CloudWatch
destination. Replace the subnet, security group, and dataset information with your own
values.

```
aws amp create-scraper \
  --alias "ec2-payment-service-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["`subnet-subnet-id-1`", "`subnet-subnet-id-2`"],
      "securityGroupIds": ["`sg-security-group-id`"]
    }
  }' \
  --scrape-configuration configurationBlob=$(cat `ec2-scraper.yml` | base64 -w 0) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:`us-west-2`:`123456789012`:dataset/default"
    }
  }'
```

When you create a managed collector, Amazon Managed Service for Prometheus automatically creates a service-linked
role that grants the collector permission to access your VPC resources and write to your
CloudWatch dataset.

## Validate metrics collection

Within minutes, metrics begin flowing to your CloudWatch dataset. To confirm that your metrics
arrive, run an ad-hoc query in CloudWatch using [Query
Studio](CloudWatch-PromQL-QueryStudio.md "CloudWatch-PromQL-QueryStudio.md"). For example, the following query returns the metrics for the
`ec2-metrics` job:

```
{job="ec2-metrics"}
```

## Build a custom dashboard

After the collector begins delivering your Amazon EC2 metrics to CloudWatch, you can build a custom
CloudWatch dashboard to visualize them. With custom dashboards, you can combine metrics from your
Prometheus exporters into widgets, add PromQL-based queries, and organize the widgets to
fit your monitoring needs. For more information, see [Using CloudWatch
dashboards](CloudWatch_Dashboards.md "CloudWatch_Dashboards.md").

## Costs

We charge for Prometheus collectors by the hour, and CloudWatch OpenTelemetry metric ingestion pricing applies. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

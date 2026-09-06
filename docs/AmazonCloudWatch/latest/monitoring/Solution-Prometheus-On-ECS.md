

# Amazon CloudWatch solution: Prometheus metric collection on Amazon ECS
<a name="Solution-Prometheus-On-ECS"></a>

This solution helps you collect Prometheus-compatible metrics from your Amazon ECS tasks without running or scaling your own collection infrastructure. Your tasks expose metrics through Prometheus exporters, and a Amazon CloudWatch managed Prometheus collector discovers the tasks in your VPC through DNS-based service discovery, scrapes their `/metrics` endpoints, and delivers the metrics to CloudWatch. Because Amazon ECS tasks are ephemeral and their IP addresses change, this solution uses AWS Cloud Map service discovery so that the collector always scrapes the current set of tasks. For general information about all CloudWatch observability solutions, see [CloudWatch observability solutions](Monitoring-Solutions.md). For more information about managed collectors, see [Amazon CloudWatch managed Prometheus collectors](managed-prometheus-collectors.md).

**Topics**
+ [Requirements](#Solution-Prometheus-On-ECS-Requirements)
+ [Enable Prometheus exporters](#Solution-Prometheus-On-ECS-Exporters)
+ [Step 1: Set up security groups](#Solution-Prometheus-On-ECS-Security-Groups)
+ [Step 2: Set up the scrape configuration](#Solution-Prometheus-On-ECS-Scrape-Config)
+ [Step 3: Set up the scraper](#Solution-Prometheus-On-ECS-Create-Scraper)
+ [Validate metrics collection](#Solution-Prometheus-On-ECS-Validate)
+ [Build a custom dashboard](#Solution-Prometheus-On-ECS-Dashboards)
+ [Costs](#Solution-Prometheus-On-ECS-Costs)

## Requirements
<a name="Solution-Prometheus-On-ECS-Requirements"></a>

This solution is relevant for the following conditions:
+ Compute: Amazon ECS tasks (on Amazon EC2 or AWS Fargate) that expose Prometheus-compatible metrics.
+ Amazon ECS services that you register with AWS Cloud Map for DNS-based service discovery.
+ Amazon VPC with DNS enabled, and at least two subnets in different Availability Zones for the collector.
+ A security group that allows the collector to reach the metrics port on your tasks. If your tasks and the collector share a security group, add a self-referencing ingress rule for the metrics port.

## Enable Prometheus exporters
<a name="Solution-Prometheus-On-ECS-Exporters"></a>

A Prometheus exporter is a process that exposes metrics in Prometheus exposition format on an HTTP `/metrics` endpoint. On Amazon ECS, you typically run an exporter as a sidecar container in the same task definition as your application, or instrument the application to expose metrics directly. The following exporters are commonly used:
+ **Node Exporter** — Host-level infrastructure metrics for tasks on the Amazon EC2 launch type (default port 9100). For more information, see the [Node Exporter](https://github.com/prometheus/node_exporter) repository on GitHub.
+ **JMX Exporter** — JVM and Java application metrics for Java workloads. For more information, see the [JMX Exporter](https://github.com/prometheus/jmx_exporter) repository on GitHub.
+ **NGINX Prometheus Exporter** — NGINX web server and reverse proxy metrics. For more information, see the [NGINX Prometheus Exporter](https://github.com/nginx/nginx-prometheus-exporter) repository on GitHub.
+ **DCGM Exporter** — NVIDIA GPU metrics for GPU workloads (default port 9400). For more information, see the [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) repository on GitHub.
+ **HAProxy Exporter** — HAProxy load balancer metrics. For more information, see the [HAProxy Exporter](https://github.com/prometheus/haproxy_exporter) repository on GitHub.
+ **Apache Exporter** — Apache HTTP Server metrics. For more information, see the [Apache Exporter](https://github.com/Lusitaniae/apache_exporter) repository on GitHub.

Add the exporter to your task definition and expose its metrics port by following the exporter's official documentation. For a complete catalog of available exporters, see [Exporters and integrations](https://prometheus.io/docs/instrumenting/exporters/) in the Prometheus documentation.

## Step 1: Set up security groups
<a name="Solution-Prometheus-On-ECS-Security-Groups"></a>

Confirm that the security group for your Amazon ECS tasks allows inbound traffic from the collector on the metrics port. When your tasks and the collector share a security group, add a self-referencing ingress rule so that resources in the same security group can communicate. The following command allows inbound traffic on port 80 from the same security group:

```
aws ec2 authorize-security-group-ingress \
  --group-id {{sg-security-group-id}} \
  --ip-permissions IpProtocol=tcp,FromPort=80,ToPort=80,UserIdGroupPairs='[{GroupId={{sg-security-group-id}}}]'
```

## Step 2: Set up the scrape configuration
<a name="Solution-Prometheus-On-ECS-Scrape-Config"></a>

For Amazon ECS tasks that you register with AWS Cloud Map, use DNS-based service discovery (`dns_sd_configs`) to automatically find and scrape your tasks as they start and stop. The `dns_sd_configs` section directs the collector to query the AWS Cloud Map DNS name and scrape all returned IP addresses. When Amazon ECS replaces a task, the collector picks up the change on its next DNS query. The `relabel_configs` section adds consistent labels to your metrics so that you can query and filter across services. For the full set of supported configuration options, see [Scraper configuration](managed-prometheus-collectors-scraper-configuration.md).

```
global:
  scrape_interval: 30s
  scrape_timeout: 10s

scrape_configs:
  - job_name: 'ecs-payforadoption'
    dns_sd_configs:
      - names: ['{{payforadoption-go.Workshop-space}}']
        type: A
        port: 80
    metrics_path: '/metrics'
    relabel_configs:
      - target_label: service_name
        replacement: '{{payforadoption-go}}'
      - target_label: cloudmap_namespace
        replacement: '{{Workshop-space}}'
      - target_label: environment
        replacement: 'production'
      - target_label: compute_platform
        replacement: 'ecs-fargate'
```

## Step 3: Set up the scraper
<a name="Solution-Prometheus-On-ECS-Create-Scraper"></a>

Create a VPC-connected managed collector that scrapes your Amazon ECS tasks and delivers metrics to your CloudWatch dataset:

You can use [GetDefaultScraperConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html) to retrieve a general-purpose scraper configuration, or provide your own.

------
#### [ AWS API ]

Use the `CreateScraper` API operation to create a scraper with a CloudWatch destination. Replace the subnet, security group, and dataset information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "ecs-payforadoption-scraper",
  "source": {
    "vpcConfiguration": {
      "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"],
      "securityGroupIds": ["{{sg-security-group-id}}"]
    }
  },
  "destination": {
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default"
    }
  },
  "scrapeConfiguration": {
    "configurationBlob": "{{base64-encoded-blob}}"
  }
}
```

------
#### [ AWS CLI ]

Use the `create-scraper` command to create a scraper with a CloudWatch destination. Replace the subnet, security group, and dataset information with your own values.

```
aws amp create-scraper \
  --alias "ecs-payforadoption-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"],
      "securityGroupIds": ["{{sg-security-group-id}}"]
    }
  }' \
  --scrape-configuration configurationBlob=$(cat {{ecs-scraper.yml}} | base64 -w 0) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default"
    }
  }'
```

------

## Validate metrics collection
<a name="Solution-Prometheus-On-ECS-Validate"></a>

After the collector begins delivering metrics, run an ad-hoc query in CloudWatch using [Query Studio](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.html) to confirm that your metrics arrive. For example, the following query returns the average requests per second to the Amazon ECS task over the last five minutes:

```
rate(payforadoption_requests_total[5m])
```

## Build a custom dashboard
<a name="Solution-Prometheus-On-ECS-Dashboards"></a>

After the collector begins delivering your Amazon ECS metrics to CloudWatch, you can build a custom CloudWatch dashboard to visualize them. With custom dashboards, you can combine metrics from your Prometheus exporters into widgets, add PromQL-based queries, and organize the widgets to fit your monitoring needs. For more information, see [Using CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

## Costs
<a name="Solution-Prometheus-On-ECS-Costs"></a>

We charge for Prometheus collectors by the hour, and CloudWatch OpenTelemetry metric ingestion pricing applies. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).
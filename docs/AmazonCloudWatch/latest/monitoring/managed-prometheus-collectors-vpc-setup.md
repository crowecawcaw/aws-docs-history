# VPC-connected managed collector

The VPC-connected Amazon CloudWatch managed Prometheus collector scrapes Prometheus-compatible
metrics from any resource reachable within your VPC — Amazon EC2 instances and Amazon ECS
tasks. You provide subnets and a security group; the collector creates ENIs and scrapes
Prometheus `/metrics` endpoints according to your configuration.

For detailed, workload-specific walkthroughs, see the CloudWatch observability solutions for
Prometheus metric collection: [Amazon CloudWatch solution: Prometheus metric collection on Amazon Amazon EC2](Solution-Prometheus-On-EC2.md "Solution-Prometheus-On-EC2.md") and [Amazon CloudWatch solution: Prometheus metric collection on Amazon ECS](Solution-Prometheus-On-ECS.md "Solution-Prometheus-On-ECS.md").

## Prerequisites

This procedure assumes familiarity with Amazon VPC subnets, security groups, and
Prometheus exporter endpoints.

- Amazon VPC with DNS enabled
- At least two subnets in different Availability Zones
- Security group allowing the collector to reach your target exporter
  ports
- Targets that expose a Prometheus-compatible `/metrics`
  endpoint
- An interface VPC endpoint for CloudWatch if you deploy the collector in private
  subnets that have no internet access. The collector delivers metrics to CloudWatch
  through this endpoint. For more information, see [Configure VPC endpoints for private subnets](#managed-prometheus-collectors-vpc-endpoints "#managed-prometheus-collectors-vpc-endpoints").

## Configure VPC endpoints for private subnets

A managed collector delivers the metrics it scrapes to your CloudWatch dataset over the
AWS network, without traversing the public internet. When you deploy the collector in
private subnets that have no route to the internet, you must create an interface VPC
endpoint so that the collector can reach the CloudWatch API. Without this endpoint, the
collector can scrape your targets but cannot deliver the metrics to CloudWatch.

Create an interface VPC endpoint for the CloudWatch service
(`com.amazonaws.`region`.monitoring`) in the same
VPC and subnets that you assign to the collector. Associate a security group that allows
inbound HTTPS (port 443) from the collector's security group. For step-by-step
instructions, see [Using
CloudWatch and interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md").

###### Note

If your subnets reach the internet through a NAT gateway, the collector can deliver
metrics to CloudWatch without a VPC endpoint. However, we recommend an interface VPC
endpoint so that traffic to CloudWatch stays within the AWS network.

## Create a scraper

You can use [GetDefaultScraperConfiguration](../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md "../../../prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.md")
to retrieve a general-purpose scraper configuration, or provide your own.

AWS API
Use the `CreateScraper` API operation to create a scraper with
a CloudWatch destination. Replace the subnet, security group, and dataset
information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "vpc-metrics-scraper",
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
destination. Replace the subnet, security group, and dataset information with
your own values.

```
aws amp create-scraper \
  --alias "vpc-metrics-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["`subnet-subnet-id-1`", "`subnet-subnet-id-2`"],
      "securityGroupIds": ["`sg-security-group-id`"]
    }
  }' \
  --scrape-configuration configurationBlob=$(cat `scrape-config.yaml` | base64 -w 0) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:`us-west-2`:`123456789012`:dataset/default"
    }
  }'
```

## Collecting metrics from Amazon EC2

To scrape metrics from Amazon EC2 instances running Prometheus exporters such as DCGM
Exporter or Node Exporter, use `static_configs` with the instance private
IP addresses:

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'ec2-node-exporter'
    static_configs:
      - targets:
          - '`10.0.1.10`:9100'
          - '`10.0.1.11`:9100'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'ec2'

  - job_name: 'ec2-dcgm-exporter'
    static_configs:
      - targets:
          - '`10.0.1.10`:9400'
          - '`10.0.1.11`:9400'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'ec2'
```

## Collecting metrics from Amazon ECS

For Amazon ECS tasks that you register with AWS Cloud Map, use DNS service discovery to
automatically find and scrape your containers:

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'ecs-services'
    dns_sd_configs:
      - names:
          - '`my-service.my-namespace.local`'
        type: A
        port: 9090
    relabel_configs:
      - source_labels: [__meta_dns_name]
        target_label: service_name
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'ecs'
```

## Cross-account observability

For cross-account VPC monitoring, we recommend using Amazon CloudWatch metric centralization. For
more information, see [CloudWatch
metrics centralization](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

For alternative cross-account scraper configurations, see [Cross-account
scrapers](../../../prometheus/latest/userguide/AMP-collector-cross-account.md "../../../prometheus/latest/userguide/AMP-collector-cross-account.md") in the _Amazon Managed Service for Prometheus User Guide_.

## Security best practices

- Deploy scrapers in private subnets without direct internet access.
- Use an interface VPC endpoint for CloudWatch connectivity so that metric delivery
  stays within the AWS network. For private subnets without internet access,
  this endpoint is required. For more information, see [Configure VPC endpoints for private subnets](#managed-prometheus-collectors-vpc-endpoints "#managed-prometheus-collectors-vpc-endpoints").
- Restrict security group ingress to the scraper security group on specific
  exporter ports only.
- Enable TLS encryption in transit for all exporter endpoints where
  possible.

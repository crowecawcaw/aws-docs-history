

# VPC-connected managed collector
<a name="managed-prometheus-collectors-vpc-setup"></a>

The VPC-connected Amazon CloudWatch managed Prometheus collector scrapes Prometheus-compatible metrics from any resource reachable within your VPC — Amazon EC2 instances and Amazon ECS tasks. You provide subnets and a security group; the collector creates elastic network interfaces (ENIs) and scrapes Prometheus `/metrics` endpoints according to your configuration.

For detailed, workload-specific walkthroughs, see the CloudWatch observability solutions for Prometheus metric collection: [Amazon CloudWatch solution: Prometheus metric collection on Amazon Amazon EC2](Solution-Prometheus-On-EC2.md) and [Amazon CloudWatch solution: Prometheus metric collection on Amazon ECS](Solution-Prometheus-On-ECS.md).

## Prerequisites
<a name="managed-prometheus-collectors-vpc-prerequisites"></a>

This procedure assumes familiarity with Amazon VPC subnets, security groups, and Prometheus exporter endpoints.
+ Amazon VPC with DNS enabled
+ At least two subnets in different Availability Zones
+ Security group allowing the collector to reach your target exporter ports
+ Targets that expose a Prometheus-compatible `/metrics` endpoint

The collector delivers scraped metrics to CloudWatch over the AWS network, without traversing the public internet. The subnets and security groups that you specify provide connectivity to your scrape targets; they do not provide the CloudWatch delivery path. You do not need to configure internet access, a NAT gateway, or a CloudWatch interface VPC endpoint in your VPC for metric delivery.

## Create a scraper
<a name="managed-prometheus-collectors-vpc-create-scraper"></a>

You can use [GetDefaultScraperConfiguration](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_GetDefaultScraperConfiguration.html) to retrieve a general-purpose scraper configuration, or provide your own.

------
#### [ AWS API ]

Use the `CreateScraper` API operation to create a scraper with a CloudWatch destination. Replace the subnet, security group, and dataset information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "vpc-metrics-scraper",
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
  --alias "vpc-metrics-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"],
      "securityGroupIds": ["{{sg-security-group-id}}"]
    }
  }' \
  --scrape-configuration configurationBlob=$(cat {{scrape-config.yaml}} | base64 -w 0) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default"
    }
  }'
```

------

## Collecting metrics from Amazon EC2
<a name="managed-prometheus-collectors-vpc-ec2"></a>

To scrape metrics from Amazon EC2 instances running Prometheus exporters such as DCGM Exporter or Node Exporter, use `static_configs` with the instance private IP addresses:

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'ec2-node-exporter'
    static_configs:
      - targets:
          - '{{10.0.1.10}}:9100'
          - '{{10.0.1.11}}:9100'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'ec2'

  - job_name: 'ec2-dcgm-exporter'
    static_configs:
      - targets:
          - '{{10.0.1.10}}:9400'
          - '{{10.0.1.11}}:9400'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'ec2'
```

## Collecting metrics from Amazon ECS
<a name="managed-prometheus-collectors-vpc-ecs"></a>

For Amazon ECS tasks that you register with AWS Cloud Map, use DNS service discovery to automatically find and scrape your containers:

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'ecs-services'
    dns_sd_configs:
      - names:
          - '{{my-service.my-namespace.local}}'
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
<a name="managed-prometheus-collectors-vpc-cross-account"></a>

For cross-account VPC monitoring, we recommend using Amazon CloudWatch metric centralization. For more information, see [CloudWatch metrics centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

For alternative cross-account scraper configurations, see [Cross-account scrapers](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-cross-account.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Security best practices
<a name="managed-prometheus-collectors-vpc-security"></a>
+ Specify private subnets without direct internet access for the collector ENIs.
+ Restrict security group ingress to the scraper security group on specific exporter ports only.
+ Enable TLS encryption in transit for all exporter endpoints where possible.
# Integrate Amazon OpenSearch Service

With an Amazon CloudWatch managed Prometheus collector, you can automatically collect
Prometheus-compatible metrics from your Amazon OpenSearch Service domains. The
managed collector connects to your VPC, collects cluster, node, and index metrics from the
domain, and delivers these metrics directly to CloudWatch. With this integration, you can monitor
the health and performance of your domains in CloudWatch without deploying any agents or
exporters.

###### Note

When a Amazon CloudWatch managed Prometheus collector delivers your Amazon OpenSearch Service
metrics to CloudWatch, it automatically enriches each metric with attributes that identify its
origin. Every metric carries the collector's instrumentation scope, cloud attributes
that record the AWS account and Region, and a unit that the collector infers from the
metric name. You can filter and group on these attributes when you query your metrics
with PromQL.

## Prerequisites

This procedure assumes that you are familiar with Amazon OpenSearch Service domain
administration and Amazon VPC networking concepts.

- An Amazon OpenSearch Service domain with VPC access. Managed collectors
  support only domains that have VPC access. Domains with public access are not
  supported.
- At least two subnets in different Availability Zones
- Security group rules that allow the collector to reach your domain endpoint
  over HTTPS (port 443). Add an inbound rule to the domain's security group that
  allows HTTPS traffic from the security group that you provide for the
  collector.

## Step 1: Configure scrape configuration

The following is an example scrape configuration for Amazon OpenSearch Service. The
managed collector connects to the domain that you specify and collects its metrics
automatically, so you do not specify scrape targets in the configuration. The
configuration must include a `scrape_configs` section with a job whose
`job_name` is exactly `opensearch-exporter`. You reference this
configuration when you create the scraper in the next step. For more information about
configuration options, see [Scraper configuration](managed-prometheus-collectors-scraper-configuration.md "managed-prometheus-collectors-scraper-configuration.md").

```
global:
  external_labels:
    domain_name: `my-opensearch-domain`

scrape_configs:
  - job_name: opensearch-exporter
    scrape_interval: 60s
```

## Step 2: Create the scraper

Create the scraper with a CloudWatch destination. You specify the domain to collect from in
the `exporters` field, and provide the networking (subnets and security
group) in the `source` field.

AWS API
Use the `CreateScraper` API operation to create a scraper with
a CloudWatch destination. Replace the subnet, security group, domain, and dataset
information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "opensearch-metrics-scraper",
  "source": {
    "vpcConfiguration": {
      "subnetIds": ["`subnet-subnet-id-1`", "`subnet-subnet-id-2`"],
      "securityGroupIds": ["`sg-security-group-id`"]
    }
  },
  "exporters": [
    {
      "openSearchConfiguration": {
        "domainArn": "arn:aws:es:`us-west-2`:`123456789012`:domain/`my-opensearch-domain`"
      }
    }
  ],
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
destination. Replace the subnet, security group, domain, and dataset
information with your own values.

```
aws amp create-scraper \
  --alias "opensearch-metrics-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["`subnet-subnet-id-1`", "`subnet-subnet-id-2`"],
      "securityGroupIds": ["`sg-security-group-id`"]
    }
  }' \
  --exporters '[
    {
      "openSearchConfiguration": {
        "domainArn": "arn:aws:es:`us-west-2`:`123456789012`:domain/`my-opensearch-domain`"
      }
    }
  ]' \
  --scrape-configuration configurationBlob=$(base64 -w 0 `opensearch-config.yaml`) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:`us-west-2`:`123456789012`:dataset/default"
    }
  }'
```

## Available metrics

- **Cluster metrics** — Cluster health and
  status, number of nodes and data nodes, active and relocating shards, and
  pending tasks.
- **Node metrics** — CPU usage, JVM heap
  usage and garbage collection, operating system memory, disk usage, and thread
  pool activity for each node.
- **Index metrics** — Indexing and search
  rates and latencies, document counts, merge and refresh activity, and cache
  usage.

For a complete list of available metrics, see [Metrics
collected from Amazon OpenSearch Service](../../../prometheus/latest/userguide/prom-opensearch-integration.md#prom-opensearch-metrics "../../../prometheus/latest/userguide/prom-opensearch-integration.md#prom-opensearch-metrics") in the _Amazon Managed Service for Prometheus User
Guide_.

## Validate metrics collection

To confirm that the collector is delivering metrics from your domain, run the
following query in CloudWatch with [Query
Studio](CloudWatch-PromQL-QueryStudio.md "CloudWatch-PromQL-QueryStudio.md"). The query returns the cluster health status for your domain. If it
returns data points, the collector is collecting metrics from your domain
successfully.

```
opensearch_cluster_health_status
```

## Cross-account observability

For cross-account Amazon OpenSearch Service monitoring, we recommend using Amazon CloudWatch
metric centralization. For more information, see [CloudWatch
metrics centralization](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

For more information about alternative cross-account scraper configurations using role
chaining, see [Integrate
Amazon OpenSearch Service](../../../prometheus/latest/userguide/prom-opensearch-integration.md "../../../prometheus/latest/userguide/prom-opensearch-integration.md") in the _Amazon Managed Service for Prometheus User
Guide_.

## Current limitations

- Managed collectors support only domains with VPC access.
- A scraper collects metrics from a single Amazon OpenSearch Service domain. To
  collect metrics from more than one domain, create a separate scraper for each
  domain.

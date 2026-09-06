

# Integrate Amazon MSK
<a name="managed-prometheus-collectors-msk-setup"></a>

With an Amazon CloudWatch managed Prometheus collector, you can automatically discover and collect Prometheus metrics from your Amazon MSK clusters. When you enable Open Monitoring on your Amazon MSK cluster, it exposes Prometheus metrics through the Java Management Extensions (JMX) Exporter and Node Exporter. The managed collector connects to your VPC and scrapes these metrics from all brokers using DNS-based service discovery and delivers these metrics directly to CloudWatch. With this integration, you can monitor host-level metrics, JVM-level metrics, and Kafka broker metrics in CloudWatch without deploying any agents.

**Note**  
When a Amazon CloudWatch managed Prometheus collector delivers your Amazon MSK metrics to CloudWatch, it automatically enriches each metric with attributes that identify its origin. Every metric carries the collector's instrumentation scope, cloud attributes that record the AWS account and Region, and a unit that the collector infers from the metric name. You can filter and group on these attributes when you query your metrics with PromQL.

## Prerequisites
<a name="managed-prometheus-collectors-msk-prerequisites"></a>

This procedure assumes familiarity with Amazon MSK cluster administration and Amazon VPC networking concepts.
+ Amazon MSK cluster in provisioned mode, with standard or express brokers. Managed collectors do not support Amazon MSK Serverless.
+ Open Monitoring enabled on the cluster. For more information, see [Open Monitoring with Prometheus](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html) in the *Amazon MSK Developer Guide*.
+ At least two subnets in different Availability Zones
+ Security group allowing the collector to reach broker ports 11001 and 11002

## Step 1: Enable Open Monitoring
<a name="managed-prometheus-collectors-msk-enable-monitoring"></a>

Enable Open Monitoring on your Amazon MSK cluster to expose Prometheus metrics. For instructions on enabling Open Monitoring, see [Open Monitoring with Prometheus](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html) in the *Amazon MSK Developer Guide*.

```
aws kafka update-monitoring \
  --cluster-arn "arn:aws:kafka:{{us-west-2}}:{{123456789012}}:cluster/{{my-cluster}}/{{abc123-def456}}" \
  --current-version "{{K1A2B3C4D5}}" \
  --open-monitoring '{
    "Prometheus": {
      "JmxExporter": {"EnabledInBroker": true},
      "NodeExporter": {"EnabledInBroker": true}
    }
  }'
```

**Note**  
The `--open-monitoring` parameter alone exposes the Prometheus endpoints on ports 11001 and 11002. Enhanced monitoring tiers such as `PER_TOPIC_PER_PARTITION` are separate from Open Monitoring and can incur additional charges, so set them only if you need that level of Amazon MSK metrics.

## Step 2: Get your cluster's DNS name
<a name="managed-prometheus-collectors-msk-dns"></a>

Amazon MSK provides a cluster-level DNS name that resolves to all broker IPs. Using this for service discovery makes your monitoring resilient to broker replacements and cluster scaling.

Get your cluster DNS name (remove the broker-specific prefix like `b-1.` or `b-2.`):

```
aws kafka get-bootstrap-brokers --cluster-arn "arn:aws:kafka:{{us-west-2}}:{{123456789012}}:cluster/{{my-cluster}}/{{abc123-def456}}"
```

For example, if the bootstrap broker returns `b-1.my-cluster.abc123.c4.kafka.us-west-2.amazonaws.com`, use `my-cluster.abc123.c4.kafka.us-west-2.amazonaws.com` as your cluster DNS name.

## Step 3: Configure scrape config
<a name="managed-prometheus-collectors-msk-scrape-config"></a>

The following is an example scrape configuration for Amazon MSK. You reference this configuration when you create the scraper in the next step. For more information about configuration options, see [Scraper configuration](managed-prometheus-collectors-scraper-configuration.md).

```
global:
  scrape_interval: 60s
  external_labels:
    cluster_name: {{my-msk-cluster}}

scrape_configs:
  - job_name: 'msk-jmx'
    dns_sd_configs:
      - names:
          - {{my-cluster.abc123.c4.kafka.us-west-2.amazonaws.com}}
        type: A
        port: 11001
    relabel_configs:
      - source_labels: [__meta_dns_name]
        target_label: broker_dns
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'msk'

  - job_name: 'msk-node'
    dns_sd_configs:
      - names:
          - {{my-cluster.abc123.c4.kafka.us-west-2.amazonaws.com}}
        type: A
        port: 11002
    relabel_configs:
      - source_labels: [__meta_dns_name]
        target_label: broker_dns
      - source_labels: [__address__]
        target_label: instance
      - target_label: compute_platform
        replacement: 'msk'
```

## Step 4: Create the scraper
<a name="managed-prometheus-collectors-msk-create-scraper"></a>

Create the scraper with a CloudWatch destination, using the scrape configuration for your Amazon MSK brokers from the previous step.

------
#### [ AWS API ]

Use the `CreateScraper` API operation to create a scraper with a CloudWatch destination. Replace the subnet, security group, and dataset information with your own values.

```
POST /scrapers HTTP/1.1

{
  "alias": "msk-metrics-scraper",
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
  --alias "msk-metrics-scraper" \
  --source '{
    "vpcConfiguration": {
      "subnetIds": ["{{subnet-subnet-id-1}}", "{{subnet-subnet-id-2}}"],
      "securityGroupIds": ["{{sg-security-group-id}}"]
    }
  }' \
  --scrape-configuration configurationBlob=$(cat {{msk-config.yaml}} | base64 -w 0) \
  --destination '{
    "cloudWatchConfiguration": {
      "datasetArn": "arn:aws:cloudwatch:{{us-west-2}}:{{123456789012}}:dataset/default"
    }
  }'
```

------

## Available metrics
<a name="managed-prometheus-collectors-msk-available-metrics"></a>
+ **JMX Exporter (port 11001)** — Kafka broker internals including topic metrics, partition metrics, request rates, consumer lag, and under-replicated partitions.
+ **Node Exporter (port 11002)** — Host-level metrics including CPU, memory, disk I/O, and network throughput.

For a complete list of available metrics, see [MSK metrics collected by managed collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-integration.html#prom-msk-metrics) in the *Amazon Managed Service for Prometheus User Guide*.

## Validate metrics collection
<a name="managed-prometheus-collectors-msk-validate"></a>

To confirm that the collector is delivering both JMX and Node Exporter metrics, run the following queries in CloudWatch with [Query Studio](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.html). If each query returns data points, the collector is scraping the corresponding exporter successfully.

The following query returns a broker-level Kafka metric from the JMX Exporter (port 11001). It reports the mean rate of broker topic activity, such as messages and bytes flowing through the brokers. Data points confirm that the collector is scraping Kafka broker metrics.

```
kafka_server_BrokerTopicMetrics_MeanRate
```

The following query returns host-level CPU utilization from the Node Exporter (port 11002). It subtracts the average idle CPU rate over a five-minute window from 100 to give the percentage of CPU that the brokers are using. Data points confirm that the collector is scraping host-level metrics.

```
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

## View the automatic dashboard
<a name="managed-prometheus-collectors-msk-dashboards"></a>

After the collector begins delivering your Amazon MSK metrics to CloudWatch, the CloudWatch console provides an automatic dashboard named **MSK OTel**. To open it, see [MSK OTel](https://console.aws.amazon.com/cloudwatch/home?#dashboards/templates/msk-otel), or sign in to the AWS Management Console, open the CloudWatch console, choose **Dashboards** in the navigation pane, choose **Automatic dashboards**, and then choose **MSK OTel**. You can start monitoring your clusters without building any widgets or dashboards yourself.

If the automatic dashboard meets your needs, you can use it as is. To build a tailored monitoring experience, you can add any of its widgets to a custom dashboard. For more information about custom dashboards, see [Using CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

## Cross-account observability
<a name="managed-prometheus-collectors-msk-cross-account"></a>

For cross-account Amazon MSK monitoring, we recommend using Amazon CloudWatch metric centralization. For more information, see [CloudWatch metrics centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

For alternative cross-account scraper configurations using role chaining, see [Cross-account Amazon MSK integration](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-cross-account.html) in the *Amazon Managed Service for Prometheus User Guide*.

## Current limitations
<a name="managed-prometheus-collectors-msk-limitations"></a>
+ Managed collectors do not support Amazon MSK Serverless clusters.
+ Managed collectors do not support public access combined with KRaft metadata mode.
+ Each Amazon MSK cluster and CloudWatch dataset combination requires one collector.
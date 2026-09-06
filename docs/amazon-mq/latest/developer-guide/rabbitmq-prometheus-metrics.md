

# Accessing Prometheus metrics
<a name="rabbitmq-prometheus-metrics"></a>

**Note**  
Prometheus metrics are only available for RabbitMQ 4.2 and later. ActiveMQ brokers do not support Prometheus metrics.

Amazon MQ now supports Prometheus metrics for Amazon MQ for RabbitMQ brokers. Prometheus metrics enable you to integrate broker observability into your existing monitoring infrastructure, giving you a unified view of broker performance alongside your other services. With Prometheus metrics, you can set up fine-grained alerting and dashboards to proactively detect and respond to issues in your messaging workloads.

Starting with RabbitMQ 4.2, Amazon MQ for RabbitMQ supports Prometheus metrics, allowing you to scrape broker metrics using the Prometheus monitoring system. The following endpoints are supported:
+ `/metrics`
+ `/metrics/detailed`
+ `/metrics/memory-breakdown`

The `/metrics/per-object` endpoint is not supported.

For more information about the metrics exposed by each endpoint, see [Prometheus metric](https://www.rabbitmq.com/docs/prometheus#metric-aggregation) in the RabbitMQ documentation.

## Prometheus metrics vs CloudWatch metrics
<a name="rabbitmq-prometheus-metrics-vs-cloudwatch"></a>

Amazon MQ for RabbitMQ exposes metrics through both Prometheus endpoints and CloudWatch. While both provide visibility into broker health, they differ in scope and usage.

The Prometheus endpoints expose a richer set of aggregated metrics about RabbitMQ broker health, covering a broader range of broker internals such as connection churn, channel activity, queue and exchange statistics, and Raft consensus metrics. These are suited for integration with existing Prometheus-based monitoring infrastructure and fine-grained alerting.

CloudWatch metrics are a curated subset of broker metrics obtained from the Prometheus endpoints. For a full list of available CloudWatch metrics, see [Available CloudWatch metrics for Amazon MQ for RabbitMQ brokers](rabbitmq-logging-monitoring.md).

In CloudWatch, metrics are always aggregated with an interval of at least 60 seconds before visualization. In contrast, Prometheus exposes raw metric datapoints, and dashboard solutions like Grafana visualize individual datapoints without aggregation by default. As a result, visualizations of the same metric can diverge between CloudWatch and Prometheus depending on the statistic used in CloudWatch

**Note**  
We recommend using Prometheus for unaggregated monitoring of Amazon MQ for RabbitMQ operational metrics.

## Obtaining and accessing the Prometheus endpoints
<a name="rabbitmq-prometheus-metrics-endpoint"></a>

You can obtain the Prometheus endpoint for your Amazon MQ for RabbitMQ broker using the AWS Management Console or the AWS CLI.
+ **AWS Management Console** — Navigate to the Amazon MQ console, open your broker's details page, and locate the Prometheus endpoint under the **Connections** section.
+ **AWS CLI** — Use the `describe-broker` command:

  ```
  aws mq describe-broker --broker-id <broker-id>
  ```

  The Prometheus endpoint is returned in the response under `BrokerInstances.Endpoints`.

Amazon MQ for RabbitMQ Prometheus support uses the same authentication scheme as the broker. For more information about the supported authentication methods, see [Amazon MQ for RabbitMQ Authentication and Authorization](rabbitmq-authentication.md). To learn how to configure authentication in Prometheus, see [http\_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_config) in the Prometheus documentation.

## Prometheus configuration best practices
<a name="rabbitmq-prometheus-metrics-best-practices"></a>
+ Configure a scraping period of 60 seconds or longer. This is recommended for operational safety.

## Sample scraping configuration
<a name="rabbitmq-prometheus-metrics-sample-config"></a>

The following sections provide sample Prometheus scraping configurations for Amazon MQ for RabbitMQ. Replace `<broker-prometheus-endpoint>` with your broker's Prometheus endpoint hostname, and `<username>` and `<password>` with your broker credentials.

### Recommended configuration
<a name="rabbitmq-prometheus-metrics-sample-config-recommended"></a>

The following configuration is recommended for most use cases. Scraping the `/metrics` endpoint provides well-aggregated metrics about overall cluster health, giving you a clear view of broker performance without the overhead of detailed metric collection.

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'rabbitmq-aws-cluster'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics'
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
```

### Detailed metrics configuration
<a name="rabbitmq-prometheus-metrics-sample-config-detailed"></a>

The following configuration scrapes additional detailed metric families for deeper observability into specific broker components.

```
global:
  scrape_interval: 60s

scrape_configs:
  - job_name: 'rabbitmq-connection-churn'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['connection_churn_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-ra'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['ra_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-queue'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['queue_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-exchange'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['exchange_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-connection'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['connection_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-channel'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['channel_metrics']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
  - job_name: 'rabbitmq-exchange-count'
    scheme: https
    basic_auth:
      username: <username>
      password: <password>
    metrics_path: '/metrics/detailed'
    params:
      family: ['exchange_names']
    static_configs:
      - targets:
        - '<broker-prometheus-endpoint>:16001'
        - '<broker-prometheus-endpoint>:16002'
        - '<broker-prometheus-endpoint>:16003'
```
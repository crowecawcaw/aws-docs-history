

# Collecting KEDA metrics with OTel Container Insights
<a name="container-insights-eks-otel-keda"></a>

KEDA (Kubernetes Event-Driven Autoscaling) is an open-source project that allows you to scale Kubernetes workloads based on external metrics from sources like Amazon SQS, Amazon CloudWatch, or custom Prometheus queries. Container Insights collects KEDA metrics through Prometheus scraping. With Container Insights, you gain built-in visibility into ScaledObject status, scaler health, and scale loop performance. You do not need to set up Prometheus or Grafana manually.

KEDA metrics help you answer operational questions such as:
+ Are my ScaledObjects scaling correctly?
+ Which scalers are experiencing errors?
+ What is the current scale loop latency?

## Prerequisites
<a name="container-insights-eks-otel-keda-prereqs"></a>

KEDA metrics collection is enabled by default when the following requirements are met.
+ Amazon EKS cluster running Kubernetes 1.28 or later
+ KEDA installed and running in the cluster (default namespace: `keda`)
+ OTel Container Insights enabled on the cluster (see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md))
+ The `amazon-cloudwatch-observability` add-on in `ACTIVE` status

## Configuring KEDA metrics collection
<a name="container-insights-eks-otel-keda-enable"></a>

KEDA metrics collection is enabled by default. If you already have OTel Container Insights enabled (`otelContainerInsights.enabled: true`) and KEDA is running in your cluster, metrics start flowing automatically with no additional configuration.

If the KEDA scrape target is not present in the cluster, the pipeline finds no pods and does nothing.

To disable KEDA metrics collection, set `otelContainerInsights.solutions.keda.enabled` to `false`. To disable all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`. The global toggle overrides individual solution settings. If `solutions.enabled` is `false`, no solutions collect metrics, even if their individual `enabled` flag is `true`.

The following Helm values show the default configuration.

```
otelContainerInsights:
  solutions:
    enabled: true
    keda:
      enabled: true
```

To disable KEDA metrics using the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"solutions":{"keda":{"enabled":false}}}}' \
  --resolve-conflicts OVERWRITE
```

To disable KEDA metrics using the Helm chart, run the following command.

```
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.keda.enabled=false
```

After you enable KEDA metrics, the CloudWatch agent finds KEDA operator pods by the label `app.kubernetes.io/name=keda-operator`. It scrapes the `/metrics` endpoint on the port named `metrics` every 30 seconds.

## KEDA metrics pipeline architecture
<a name="container-insights-eks-otel-keda-architecture"></a>

The KEDA metrics pipeline uses the following data flow:

1. The Prometheus receiver discovers KEDA operator pods using Kubernetes service discovery.

1. The receiver scrapes the `/metrics` endpoint on each KEDA operator pod.

1. The OpenTelemetry processor chain adds Kubernetes and cloud resource labels to each metric.

1. The exporter sends the enriched metrics to CloudWatch through OTLP.

The KEDA pipeline runs independently from other metric pipelines (API server, Kube State Metrics, cAdvisor). This means a failure in one pipeline does not affect the others. If the KEDA scrape target goes down, other pipelines keep working.

**Note**  
KEDA metrics are cluster-scoped.

## Viewing the KEDA dashboard
<a name="container-insights-eks-otel-keda-dashboard"></a>

After you turn on KEDA metrics, you can view the dashboard in the CloudWatch console.

**To view the KEDA dashboard**

1. Open the CloudWatch console at [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Container Insights**, then choose **Performance monitoring**.

1. For **Service**, choose **EKS OTEL**.

1. In the navigation pane, expand **Solutions** and choose **KEDA**.

The dashboard displays 10 metrics organized into 5 categories: Scaled Objects, Scalers, Triggers, Scaling, and Controller Health.

## Available metrics
<a name="container-insights-eks-otel-keda-metrics"></a>

The following table lists the 10 KEDA metrics that Container Insights collects.


| Metric name | Category | Description | 
| --- | --- | --- | 
| keda\_scaled\_object\_paused | Scaled Objects | 1 if ScaledObject is paused, 0 otherwise | 
| keda\_scaled\_object\_errors\_total | Scaled Objects | Total errors per ScaledObject | 
| keda\_scaler\_active | Scalers | 1 if scaler is active, 0 otherwise | 
| keda\_scaler\_metrics\_value | Scalers | Current value returned by the scaler | 
| keda\_scaler\_metrics\_latency\_seconds | Scalers | Latency of scaler metric retrieval | 
| keda\_scaler\_detail\_errors\_total | Scalers | Total errors per scaler | 
| keda\_trigger\_registered\_total | Triggers | Total registered triggers by type | 
| keda\_internal\_scale\_loop\_latency\_seconds | Scaling | Scale loop latency per ScaledObject | 
| keda\_resource\_registered\_total | Scaling | Total KEDA custom resources registered by type | 
| keda\_build\_info | Controller Health | KEDA build information (version, git commit) | 
# Set up metrics ingestion

using AWS Distro for OpenTelemetry on an Amazon Elastic Kubernetes Service cluster

You can use the AWS Distro for OpenTelemetry (ADOT) collector to scrape
metrics from a Prometheus-instrumented application, and send the metrics to
Amazon Managed Service for Prometheus.

###### Note

For more information about the ADOT collector, see [AWS Distro for
OpenTelemetry](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/").

For more information about Prometheus-instrumented applications, see
[What are Prometheus-compatible
metrics?](prom-compatible-metrics.md "prom-compatible-metrics.md").

Collecting Prometheus metrics with ADOT involves three OpenTelemetry components:
the Prometheus Receiver, the Prometheus Remote Write Exporter, and the Sigv4
Authentication Extension.

You can configure the Prometheus Receiver using your existing Prometheus
configuration to perform service discovery and metric scraping. The Prometheus
Receiver scrapes metrics in the Prometheus exposition format. Any applications or
endpoints that you want to scrape should be configured with the Prometheus client
library. The Prometheus Receiver supports the full set of Prometheus scraping and
re-labeling configurations described in [Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "https://prometheus.io/docs/prometheus/latest/configuration/configuration/") in the Prometheus documentation. You can paste these
configurations directly into your ADOT Collector configurations.

The Prometheus Remote Write Exporter uses the `remote_write` endpoint
to send the scraped metrics to your management portal workspace. The HTTP requests to export
data will be signed with AWS SigV4, the AWS protocol for secure authentication,
with the Sigv4 Authentication Extension. For more information, see [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

The collector automatically discovers Prometheus metrics endpoints on Amazon EKS and
uses the configuration found in [<kubernetes_sd_config>.](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config "https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config")

The following demo is an example of this configuration on a cluster running
Amazon Elastic Kubernetes Service or self-managed Kubernetes. To perform these steps, you must have AWS
credentials from any of the potential options in the default AWS credentials
chain. For more information, see [Configuring the AWS SDK for Go](../../../sdk-for-go/v1/developer-guide/configuring-sdk.md "../../../sdk-for-go/v1/developer-guide/configuring-sdk.md"). This demo uses a sample app that is
used for integration tests of the process. The sample app exposes metrics at the
`/metrics` endpoint, like the Prometheus client library.

## Prerequisites

Before you begin the following ingestion setup steps, you must set up your
IAM role for the service account and trust policy.

###### To set up the IAM role for service account and trust policy

1. Create the IAM role for the service account by following the steps
   in [Set up service roles for the ingestion of metrics
   from Amazon EKS clusters](set-up-irsa.md#set-up-irsa-ingest "set-up-irsa.md#set-up-irsa-ingest").

The ADOT Collector will use this role when it scrapes and exports
metrics. 2. Next, edit the trust policy. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home"). 3. In the left navigation pane, choose **Roles** and
find the **amp-iamproxy-ingest-role** that you created
in step 1. 4. Choose the **Trust relationships** tab and choose
**Edit trust relationship**. 5. In the trust relationship policy JSON, replace `aws-amp`
with `adot-col` and then choose **Update Trust
Policy**. Your resulting trust policy should look like the
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Federated": "arn:aws:iam::`111122223333`:oidc-provider/oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`"
 },
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Condition": {
 "StringEquals": {
 "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:sub": "system:serviceaccount:adot-col:amp-iamproxy-ingest-service-account",
 "oidc.eks.`us-east-1`.amazonaws.com/id/`EXAMPLED539D4633E53DE1B71EXAMPLE`:aud": "sts.amazonaws.com"
 }
 }
 }
 ]
}`

```

6. Choose the **Permissions** tab and make sure that the
   following permissions policy is attached to the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aps:RemoteWrite",
 "aps:GetSeries",
 "aps:GetLabels",
 "aps:GetMetricMetadata"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Enabling

Prometheus metric collection

###### Note

When you create a namespace in Amazon EKS, `alertmanager` and node
exporter are disabled by default.

###### To enable Prometheus collection on an Amazon EKS or Kubernetes cluster

1. Fork and clone the sample app from the repository at [aws-otel-community](https://github.com/aws-observability/aws-otel-community "https://github.com/aws-observability/aws-otel-community").

Then run the following commands.

```
cd ./sample-apps/prometheus-sample-app
docker build . -t prometheus-sample-app:latest
```

2. Push this image to a registry such as Amazon ECR or DockerHub.
3. Deploy the sample app in the cluster by copying this Kubernetes
   configuration and applying it. Change the image to the image that you
   just pushed by replacing `{{PUBLIC_SAMPLE_APP_IMAGE}}` in the
   `prometheus-sample-app.yaml` file.

```
curl https://raw.githubusercontent.com/aws-observability/aws-otel-collector/main/examples/eks/aws-prometheus/prometheus-sample-app.yaml -o prometheus-sample-app.yaml
kubectl apply -f prometheus-sample-app.yaml
```

4. Enter the following command to verify that the sample app has started.
   In the output of the command, you will see
   `prometheus-sample-app` in the `NAME`
   column.

```
kubectl get all -n aoc-prometheus-pipeline-demo
```

5. Start a default instance of the ADOT Collector. To do so, first enter
   the following command to pull the Kubernetes configuration for ADOT
   Collector.

```
curl https://raw.githubusercontent.com/aws-observability/aws-otel-collector/main/examples/eks/aws-prometheus/prometheus-daemonset.yaml -o prometheus-daemonset.yaml
```

Then edit the template file, substituting the
**remote_write** endpoint for your Amazon Managed Service for Prometheus
workspace for `YOUR_ENDPOINT` and your Region for
`YOUR_REGION`. Use the **remote_write**
endpoint that is displayed in the Amazon Managed Service for Prometheus console when you look at
your workspace details.

You'll also need to change `YOUR_ACCOUNT_ID` in the service
account section of the Kubernetes configuration to your AWS account
ID.

In this example, the ADOT Collector configuration uses an annotation
(`scrape=true`) to tell which target endpoints to scrape.
This allows the ADOT Collector to distinguish the sample app endpoint
from kube-system endpoints in your cluster. You can remove this from the
re-label configurations if you want to scrape a different sample
app. 6. Enter the following command to deploy the ADOT collector.

```
kubectl apply -f prometheus-daemonset.yaml
```

7. Enter the following command to verify that the ADOT collector has
   started. Look for `adot-col` in the `NAMESPACE`
   column.

```
kubectl get pods -n adot-col
```

8. Verify that the pipeline works by using the logging exporter. Our
   example template is already integrated with the logging exporter. Enter
   the following commands.

```
kubectl get pods -A
kubectl logs -n adot-col `name_of_your_adot_collector_pod`
```

Some of the scraped metrics from the sample app will look like the
following example.

```
Resource labels:
     -> service.name: STRING(kubernetes-service-endpoints)
     -> host.name: STRING(192.168.16.238)
     -> port: STRING(8080)
     -> scheme: STRING(http)
InstrumentationLibraryMetrics #0
Metric #0
Descriptor:
     -> Name: test_gauge0
     -> Description: This is my gauge
     -> Unit:
     -> DataType: DoubleGauge
DoubleDataPoints #0
StartTime: 0
Timestamp: 1606511460471000000
Value: 0.000000
```

9. To test whether Amazon Managed Service for Prometheus received the metrics, use
   `awscurl`. This tool enables you to send HTTP requests
   through the command line with AWS Sigv4 authentication, so you must
   have AWS credentials set up locally with the correct permissions to
   query from Amazon Managed Service for Prometheus For instructions on installing
   `awscurl`, see [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl").

In the following command, replace `AMP_REGION`, and
`AMP_ENDPOINT` with the information for your Amazon Managed Service for Prometheus
workspace.

```
awscurl --service="aps" --region="`AMP_REGION`" "https://`AMP_ENDPOINT`/api/v1/query?query=adot_test_gauge0"
{"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"adot_test_gauge0"},"value":[1606512592.493,"16.87214000011479"]}]}}
```

If you receive a metric as the response, that means your pipeline
setup has been successful and the metric has successfully propagated
from the sample app into Amazon Managed Service for Prometheus.

**Cleaning up**

To clean up this demo, enter the following commands.

```
kubectl delete namespace aoc-prometheus-pipeline-demo
kubectl delete namespace adot-col
```

## Advanced configuration

The Prometheus Receiver supports the full set of Prometheus scraping and
re-labeling configurations described in [Configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/ "https://prometheus.io/docs/prometheus/latest/configuration/configuration/") in the Prometheus documentation. You can paste these
configurations directly into your ADOT Collector configurations.

The configuration for the Prometheus Receiver includes your service discovery,
scraping configurations, and re-labeling configurations. The receiver
configuration looks like the following.

```
receivers:
  prometheus:
    config:
      [`[Your Prometheus configuration]`]
```

The following is an example configuration.

```
receivers:
  prometheus:
    config:
      global:
        scrape_interval: 1m
        scrape_timeout: 10s

      scrape_configs:
      - job_name: kubernetes-service-endpoints
        sample_limit: 10000
        kubernetes_sd_configs:
        - role: endpoints
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
          insecure_skip_verify: true
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
```

If you have an existing Prometheus configuration, you must replace the
`$` characters with `$$` to avoid having the values
replaced with environment variables. \*This is especially important for the
replacement value of the relabel_configurations. For example, if you start with
the following relabel_configuration:

```
relabel_configs:
- source_labels: [__meta_kubernetes_ingress_scheme,__address__,__meta_kubernetes_ingress_path]
  regex: (.+);(.+);(.+)
  replacement: ${1}://${2}${3}
  target_label: __param_target
```

It would become the following:

```
relabel_configs:
- source_labels: [__meta_kubernetes_ingress_scheme,__address__,__meta_kubernetes_ingress_path]
  regex: (.+);(.+);(.+)
  replacement: $${1}://${2}${3}
  target_label: __param_target
```

**Prometheus remote write exporter and Sigv4
authentication extension**

The configuration for the Prometheus Remote Write Exporter and Sigv4
Authentication Extension are simpler than the Prometheus receiver. At this stage
in the pipeline, metrics have already been ingested, and we’re ready to export
this data to Amazon Managed Service for Prometheus. The minimum requirement for a successful configuration
to communicate with Amazon Managed Service for Prometheus is shown in the following example.

```
extensions:
  sigv4auth:
    service: "aps"
    region: "user-region"
exporters:
  prometheusremotewrite:
    endpoint: "https://aws-managed-prometheus-endpoint/api/v1/remote_write"
    auth:
      authenticator: "sigv4auth"
```

This configuration sends an HTTPS request that is signed by AWS SigV4 using
AWS credentials from the default AWS credentials chain. For more
information, see [Configuring the AWS SDK for Go](../../../sdk-for-go/v1/developer-guide/configuring-sdk.md "../../../sdk-for-go/v1/developer-guide/configuring-sdk.md"). You must specify the service to be
`aps`.

Regardless of the method of deployment, the ADOT collector must have access to
one of the listed options in the default AWS credentials chain. The Sigv4
Authentication Extension depends on the AWS SDK for Go and uses it to fetch
credentials and authenticate. You must ensure that these credentials have remote
write permissions for Amazon Managed Service for Prometheus.

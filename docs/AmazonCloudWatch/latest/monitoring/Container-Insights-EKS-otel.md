# Using AWS Distro for OpenTelemetry

You can set up Container Insights to collect metrics from Amazon EKS clusters by using the
AWS Distro for OpenTelemetry collector. For more information about the AWS Distro for
OpenTelemetry, see [AWS Distro for
OpenTelemetry](https://aws.amazon.com/otel/ "https://aws.amazon.com/otel/").

###### Important

If you install using AWS Distro for OpenTelemetry, you install Container Insights
but do not get Container Insights with enhanced observability for Amazon EKS. You will not
collect the detailed metrics supported in Container Insights with enhanced observability
for Amazon EKS.

How you set up Container Insights depends on whether the cluster is hosted on Amazon EC2
instances or on AWS Fargate.

## Amazon EKS clusters hosted on Amazon EC2

If you have not already done so, make sure that you have fulfilled the prerequisites
including the necessary IAM roles. For more information, see [Verifying prerequisites for Container
Insights in CloudWatch](Container-Insights-prerequisites.md "Container-Insights-prerequisites.md").

Amazon provides a Helm chart that you can use to set up the monitoring of Amazon Elastic Kubernetes Service
on Amazon EC2. This monitoring uses the AWS Distro for OpenTelemetry(ADOT) Collector for
metrics and Fluent Bit for logs. Therefore, the Helm chart is useful for customers who
use Amazon EKS on Amazon EC2 and want to collect metrics and logs to send to CloudWatch Container
Insights. For more information about this Helm chart, see [ADOT Helm chart for EKS on EC2 metrics and logs to Amazon CloudWatch Container
Insights](https://github.com/aws-observability/aws-otel-helm-charts/tree/main/charts/adot-exporter-for-eks-on-ec2 "https://github.com/aws-observability/aws-otel-helm-charts/tree/main/charts/adot-exporter-for-eks-on-ec2").

Alternatively, you can also use the instructions in the rest of this section.

First, deploy the AWS Distro for OpenTelemetry collector as a DaemonSet by
entering the following command.

```
curl https://raw.githubusercontent.com/aws-observability/aws-otel-collector/main/deployment-template/eks/otel-container-insights-infra.yaml |
kubectl apply -f -
```

To confirm that the collector is running, enter the following command.

```
kubectl get pods -l name=aws-otel-eks-ci -n aws-otel-eks
```

If the output of this command includes multiple pods in the `Running`
state, the collector is running and collecting metrics from the cluster. The collector
creates a log group named
`aws/containerinsights/`cluster-name`/performance`
and sends the performance log events to it.

For information about how to see your Container Insights metrics in CloudWatch, see [Viewing Container Insights metrics](Container-Insights-view-metrics.md "Container-Insights-view-metrics.md").

AWS has also provided documentation on GitHub for this scenario. If you want to
customize the metrics and logs published by Container Insights, see [https://aws-otel.github.io/docs/getting-started/container-insights/eks-infra](https://aws-otel.github.io/docs/getting-started/container-insights/eks-infra "https://aws-otel.github.io/docs/getting-started/container-insights/eks-infra").

## Amazon EKS clusters hosted on

Fargate

For instructions for how to configure and deploy an ADOT Collector to collect system
metrics from workloads deployed to an Amazon EKS cluster on Fargate and send them to
CloudWatch Container Insights, see [Container Insights EKS Fargate](https://aws-otel.github.io/docs/getting-started/container-insights/eks-fargate "https://aws-otel.github.io/docs/getting-started/container-insights/eks-fargate") in the AWS Distro for OpenTelemetry
documentation.

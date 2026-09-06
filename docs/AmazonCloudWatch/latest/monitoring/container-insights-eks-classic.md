

# Enhanced Container Insights (Classic)
<a name="container-insights-eks-classic"></a>

Enhanced Container Insights (Classic) is a managed Amazon EKS add-on configuration that deploys the CloudWatch agent and Fluent Bit as a DaemonSet on your cluster. It provides Container Insights with Enhanced Observability, collecting infrastructure metrics, application logs, and performance data from your Amazon EKS workloads.

Both Enhanced Container Insights (Classic) and OTel Container Insights use the same `amazon-cloudwatch-observability` Amazon EKS add-on. The difference is the add-on version and configuration. Enhanced Container Insights (Classic) refers to the legacy configuration of that add-on.

**Maintenance mode**  
Enhanced Container Insights (Classic) is in maintenance mode. It continues to receive security patches and critical bug fixes, but no new features are being developed for this approach.  
For new deployments, we recommend [OTel Container Insights (Recommended)](container-insights-eks-otel.md), which provides broader signal coverage, simpler deployment, and active ongoing development.

This approach is designed for the following use cases:
+ Existing customers who already have the add-on deployed and operational
+ Teams that require a managed add-on model with Amazon EKS add-on lifecycle management

## What Enhanced Container Insights (Classic) provides
<a name="container-insights-eks-classic-features"></a>

Enhanced Container Insights (Classic) includes the following capabilities:
+ **Enhanced Observability** — Detailed Kubernetes metrics at the pod, node, and cluster level
+ **Metrics and logs** — Collects infrastructure metrics and container logs through the CloudWatch agent and Fluent Bit
+ **Managed lifecycle** — Install, update, and remove through the Amazon EKS add-on API or console
+ **Automatic updates** — Security patches delivered through the Amazon EKS add-on update mechanism

## Comparison with OTel Container Insights
<a name="container-insights-eks-classic-comparison"></a>

The following table summarizes the differences between Enhanced Container Insights (Classic) and OTel Container Insights.


| Consideration | Enhanced Container Insights (Classic) | OTel Container Insights (Recommended) | 
| --- | --- | --- | 
| Signals | Metrics, Logs | Metrics, Logs | 
| Enhanced Observability | Yes | Yes | 
| Maintenance status | Maintenance mode | Active development | 
| Deployment model | Amazon EKS managed add-on | Amazon EKS add-on (OTel-based) | 

## Installation methods
<a name="container-insights-eks-classic-installation"></a>

You can install Enhanced Container Insights (Classic) using any of the following methods:
+ **Amazon EKS console** — Enable from the **Observability** tab on your cluster. For more information, see [Enable Enhanced Container Insights (Classic) from the console](container-insights-eks-classic-console.md).
+ **AWS CLI** — Use the `aws eks create-addon` command with the `amazon-cloudwatch-observability` add-on name and a v5.x version. For more information, see [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md).
+ **Helm chart** — Use `helm install` with a Classic-compatible version of the chart.
+ **CloudFormation or AWS CDK** — Use `AWS::EKS::Addon` with the version pinned to a v5.x release. For more information, see [Deploy Enhanced Container Insights (Classic) with CloudFormation or Helm](container-insights-eks-classic-iac.md).

## Metrics reference
<a name="container-insights-eks-classic-metrics-overview"></a>

For the complete list of Enhanced Container Insights (Classic) metric names and dimensions, see [Enhanced Container Insights (Classic) metric reference](container-insights-eks-classic-metrics.md).

## Upgrade to OTel Container Insights
<a name="container-insights-eks-classic-upgrade"></a>

For step-by-step instructions to move from Enhanced Container Insights (Classic) to OTel Container Insights with zero monitoring gaps, see [Migrate from Enhanced Container Insights (Classic) to OTel Container Insights](container-insights-eks-migrate-from-classic.md).

**Topics**
+ [What Enhanced Container Insights (Classic) provides](#container-insights-eks-classic-features)
+ [Comparison with OTel Container Insights](#container-insights-eks-classic-comparison)
+ [Installation methods](#container-insights-eks-classic-installation)
+ [Metrics reference](#container-insights-eks-classic-metrics-overview)
+ [Upgrade to OTel Container Insights](#container-insights-eks-classic-upgrade)
+ [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md)
+ [Enable Enhanced Container Insights (Classic) from the console](container-insights-eks-classic-console.md)
+ [Deploy Enhanced Container Insights (Classic) with CloudFormation or Helm](container-insights-eks-classic-iac.md)
+ [Enhanced Container Insights (Classic) metric reference](container-insights-eks-classic-metrics.md)
+ [Send logs to CloudWatch Logs](Container-Insights-EKS-logs.md)
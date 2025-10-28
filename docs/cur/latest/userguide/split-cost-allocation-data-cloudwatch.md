# Using split cost allocation

data with Amazon CloudWatch Container Insights

Splitting the cost data for Amazon EKS requires that you collect and store metrics from
your clusters, including memory and CPU usage. Amazon CloudWatch Container Insights can be
used for this purpose.

Once you've opted in to split cost allocation data and set up the CloudWatch agent with
EKS observability add-on on your EKS cluster, split cost allocation data starts
receiving the two required metrics `(pod_cpu_usage_total` and
`pod_memory_working_set`) in the `ContainerInsights`
namespace and uses them automatically. To view the full set of container metrics for
EKS, see [Amazon EKS and Kubernetes Container Insights metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md") in
the _Amazon CloudWatch User Guide_.

The following sections describe how to send the correct metrics from your EKS
cluster to split cost allocation data.

## Prerequisites

As prerequisites for using Amazon CloudWatch Container Insights with split cost
allocation data:

- You need to enable split cost allocation data in the AWS Billing and
  Cost Management console. For details, see [Enabling split cost allocation
  data](enabling-split-cost-allocation-data.md "enabling-split-cost-allocation-data.md").
- You need an EKS cluster for which you want to track split cost
  allocation data. This can be an existing cluster, or you can create a
  new one. For more information, see [Create an Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the _Amazon EKS User
  Guide_.

## Setting up Amazon CloudWatch Container

Insights to forward EKS metrics

You need to set up and configure the CloudWatch agent in order to forward EKS
metrics. You can use either the [Amazon CloudWatch Observability EKS add-on or the Amazon CloudWatch
Observability Helm chart](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md") to install the CloudWatch agent and the
Fluent-bit agent on an EKS cluster. For more information on how to install and
set up the CloudWatch agent, see [Install the Amazon CloudWatch Observability EKS
add-on](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md") in the _Amazon CloudWatch User Guide_.

The following are the minimum versions required for the CloudWatch agent and EKS
add-on:

- CloudWatch agent version: v1.300045.0
- CloudWatch Observability EKS add-on version: v2.0.1-eksbuild.1

## Estimating your Amazon CloudWatch

costs

Enabling the feature to use Amazon CloudWatch Container Insights with split cost
allocation data adds two new metrics to Amazon CloudWatch Container Insights:
`pod_cpu_usage_total` and `pod_memory_working_set`.
For details on these metrics, see [Amazon EKS and Kubernetes Container Insights
metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.md") in the _Amazon CloudWatch User Guide_.

###### To understand the costs associated with the feature

1. Open Amazon CloudWatch Pricing at [https://aws.amazon.com/cloudwatch/pricing/](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
2. Navigate to the **Paid tier** section.
3. Choose the **Container Insights** tab.
4. For a detailed calculation of the costs, navigate to the
   **Pricing examples** section, and refer to
   **Example 13 - Container Insights for Amazon EKS and
   Kubernetes**.

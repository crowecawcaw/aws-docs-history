# Enable Enhanced Container Insights (Classic) from the console

You can enable Enhanced Container Insights (Classic) directly from the Amazon EKS console. This
approach installs the Amazon CloudWatch Observability add-on (version prior to v6.2.0) with the Classic
metric pipeline. This is ideal if you prefer a UI-driven experience and want to enable
observability without writing infrastructure code or running CLI commands.

###### Recommendation

For new deployments, we recommend [OTel Container Insights (Recommended)](container-insights-eks-otel.md "container-insights-eks-otel.md"), which uses add-on version 6.2.0 or later
with the OTel-based pipeline.

## Prerequisites

Before you enable Enhanced Container Insights (Classic) from the console, verify that you
meet the following requirements.

- You are signed in to the Amazon EKS console.
- An existing Amazon EKS cluster running Kubernetes version 1.25 or later.
- The `amazon-cloudwatch-observability` add-on version must be prior to
  v6.2.0 (for example, v5.4.0).
- IAM permissions: `eks:DescribeCluster`,
  `eks:UpdateClusterConfig`, `eks:ListAddons`,
  `eks:CreateAddon`, `eks:DescribeAddon`,
  `iam:AttachRolePolicy`, and
  `iam:CreateServiceLinkedRole`.
- The node IAM role must have the `CloudWatchAgentServerPolicy` managed
  policy attached.
- The cluster is in `ACTIVE` state.

## Enable Enhanced Container Insights (Classic)

Use the following procedure to enable Enhanced Container Insights (Classic) from the Amazon EKS
console.

###### To enable Enhanced Container Insights (Classic) by using the console

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/](https://console.aws.amazon.com/eks/ "https://console.aws.amazon.com/eks/").
2. Choose **Clusters**, and then choose your cluster name.
3. Choose the **Observability** tab.
4. Next to **Container Insights** status, choose
   **Manage**.
5. Select **Enhanced Container Insights**, and then choose
   **Enable**.

The console installs the add-on with the Classic configuration. Metrics appear in the
`ContainerInsights` namespace within 3 to 5 minutes.

## Verify that data appears in CloudWatch

After you enable Enhanced Container Insights (Classic), data appears in CloudWatch within 3 to 5
minutes.

###### To verify Container Insights data

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then choose
   **Classic metrics**.
3. Choose the **ContainerInsights** namespace.
4. Verify that metrics such as `pod_cpu_utilization` and
   `node_memory_utilization` appear for your cluster.

## Next steps

After you enable Enhanced Container Insights (Classic), you can explore the following
topics.

- For AWS CLI and advanced setup options, see [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md "container-insights-eks-classic-setup.md").
- For information about the metrics that Enhanced Container Insights (Classic) collects,
  see [Enhanced Container Insights (Classic) metric reference](container-insights-eks-classic-metrics.md "container-insights-eks-classic-metrics.md").
- To migrate to OTel Container Insights, see [Migrate from Enhanced Container Insights (Classic) to OTel Container Insights](container-insights-eks-migrate-from-classic.md "container-insights-eks-migrate-from-classic.md").
- For more information about OTel Container Insights, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md "container-insights-eks-otel.md").

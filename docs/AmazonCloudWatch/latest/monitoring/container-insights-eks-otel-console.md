

# Enable OTel Container Insights from the console
<a name="container-insights-eks-otel-console"></a>

You can enable OTel Container Insights directly from the AWS Management Console with a minimal-click workflow. This approach is ideal if you prefer a UI-driven experience and want to enable full observability on an existing Amazon EKS cluster without writing infrastructure code or running CLI commands.

## Prerequisites
<a name="container-insights-eks-otel-console-prereqs"></a>

Before you enable OTel Container Insights from the console, verify that you meet the following requirements.
+ You are signed in to the Amazon EKS console.
+ An existing Amazon EKS cluster running Kubernetes version 1.28 or later.
+ Version 6.2.0 or later of the `amazon-cloudwatch-observability` add-on.
+ IAM permissions: `eks:DescribeCluster`, `eks:UpdateClusterConfig`, `eks:ListAddons`, `eks:CreateAddon`, `eks:DescribeAddon`, `iam:AttachRolePolicy`, and `iam:CreateServiceLinkedRole`.
+ The node IAM role must have the `CloudWatchAgentServerPolicy` managed policy attached.
+ The cluster is in `ACTIVE` state.

## Enable OTel Container Insights
<a name="container-insights-eks-otel-console-enable"></a>

Use the following procedure to enable OTel Container Insights from the Amazon EKS console.

**To enable OTel Container Insights by using the console**

1. Open the Amazon EKS console at [https://console.aws.amazon.com/eks/](https://console.aws.amazon.com/eks/).

1. Choose **Clusters**, and then choose your cluster name.

1. Choose the **Observability** tab.

1. Next to **Container Insights** status, choose **Manage**.

1. Select the **OTel Container Insights** configuration.

1. Confirm the IAM role for the add-on. The console auto-creates the role if one doesn't already exist.

1. Choose **Enable**.

## What the console configures
<a name="container-insights-eks-otel-console-actions"></a>

When you enable OTel Container Insights from the console, the console performs the following actions on your behalf.
+ Creates and configures the Pod Identity association for the `amazon-cloudwatch` namespace
+ Installs the `amazon-cloudwatch-observability` Amazon EKS add-on with version 6.2.0 or later and `otelContainerInsights.enabled=true`
+ Attaches the `CloudWatchAgentServerPolicy` to the designated IAM role

## Verify that data appears in CloudWatch
<a name="container-insights-eks-otel-console-verify"></a>

After you enable OTel Container Insights, data appears in CloudWatch within 5 minutes.

**To verify Container Insights data**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Insights**, and then choose **Container Insights**.

1. Choose your cluster from the cluster list.

The Container Insights dashboards populate with metrics data from your cluster.

## Troubleshooting
<a name="container-insights-eks-otel-console-troubleshoot"></a>

Use the following guidance to resolve common issues when you enable OTel Container Insights from the console.

### The Enable button is unavailable
<a name="container-insights-eks-otel-console-ts-greyed-out"></a>

**Symptom:** The **Enable** button is greyed out and you can't choose it.

**Cause:** The cluster might be in an updating state, or you don't have sufficient IAM permissions.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that the cluster status is `ACTIVE` on the cluster details page.

1. Verify that your IAM user or role has the required permissions listed in the prerequisites.

1. If the cluster is updating, wait for the update to complete and try again.

### Status shows DEGRADED after you enable
<a name="container-insights-eks-otel-console-ts-degraded"></a>

**Symptom:** After you enable OTel Container Insights, the add-on status shows `DEGRADED`.

**Cause:** The add-on installed but can't function correctly, typically because of IAM role permission issues or node connectivity problems.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that the IAM role has the `CloudWatchAgentServerPolicy` managed policy attached.

1. Verify that the cluster nodes have outbound connectivity to CloudWatch endpoints.

1. Check the add-on health details in the Amazon EKS console by choosing the **Add-ons** tab on the cluster details page.
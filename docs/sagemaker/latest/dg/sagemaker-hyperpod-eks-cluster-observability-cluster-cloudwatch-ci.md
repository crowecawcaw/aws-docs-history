

# Observability with Amazon CloudWatch
<a name="sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci"></a>

Use [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) to collect, aggregate, and summarize metrics and logs from the containerized applications and micro-services on the EKS cluster associated with a HyperPod cluster.

Amazon CloudWatch Insights collects metrics for compute resources, such as CPU, memory, disk, and network. Container Insights also provides diagnostic information, such as container restart failures, to help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on metrics that Container Insights collects.

To find a complete list of metrics, see [Amazon EKS and Kubernetes Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EKS.html) in the *Amazon EKS User Guide*.

## Install CloudWatch Container Insights
<a name="sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci-setup"></a>

Cluster admin users must set up CloudWatch Container Insights following the instructions at [Install the CloudWatch agent by using the Amazon CloudWatch Observability EKS add-on or the Helm chart](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.html) in the *CloudWatch User Guide*. For more information about Amazon EKS add-on, see also [Install the Amazon CloudWatch Observability EKS add-on](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.html) in the *Amazon EKS User Guide*.

After the installation has completed, verify that the CloudWatch Observability add-on is visible in the EKS cluster add-on tab. It might take about a couple of minutes until the dashboard loads.

**Note**  
SageMaker HyperPod requires the CloudWatch Insight v2.0.1-eksbuild.1 or later.

![Amazon CloudWatch Observability add-on showing Creating status with version v2.0.1-eksbuild.1.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/hyperpod-eks-CIaddon.png)


## Access CloudWatch container insights logs
<a name="sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci-access-log"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Logs**, and then choose **Log groups**.

When you have the HyperPod clusters integrated with Amazon CloudWatch Container Insights, you can access the relevant log groups in the following format: `/aws/containerinsights /<eks-cluster-name>/*`. Within this log group, you can find and explore various types of logs such as Performance logs, Host logs, Application logs, and Data plane logs.
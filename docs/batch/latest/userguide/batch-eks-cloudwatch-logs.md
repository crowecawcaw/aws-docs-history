# Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs

You can use Amazon CloudWatch Logs to monitor, store, and view all your log files in one location.
Using CloudWatch Logs, you can search, filter, and analyze log data from multiple sources.

You can download an AWS for Fluent Bit image that includes a plugin to
monitor AWS Batch on Amazon EKS jobs in CloudWatch Logs. Fluent Bit is an open-source log
processor and forwarder that's both Docker and Kubernetes compatible. We recommend that you
use Fluent Bit as your log router because it's less resource intensive than
Fluentd. For more information, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md").

## Prerequisites

- Attach the `CloudWatchAgentServerPolicy` policy to the AWS Identity and Access Management policy of
  your worker nodes. For more information, see [Verify prerequisites](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-prerequisites.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-prerequisites.md").

## Install the

add-on

For instructions on how to install AWS for Fluent Bit and create the
CloudWatch groups, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm
chart](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md").

You must provide the following [additional configuration data](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-configuration") when installing the
add-on:

- If you install the add-on with the AWS Management Console you need to provide the following tolerations in
  **Configuration values**:

```
{
  "tolerations": [
    {
      "key": "batch.amazonaws.com/batch-node",
      "operator": "Exists"
    }
  ]
}
```

- If you install the add-on with the AWS CLI then add the following arguments:

```
--configuration-values '{"tolerations":[{"key":"batch.amazonaws.com/batch-node","operator":"Exists"}]}'
```

###### Tip

Remember that Fluent Bit uses .5 CPU and 100 MB of memory on
AWS Batch nodes. This reduces the total available capacity for AWS Batch jobs. Consider
this when you size your jobs.

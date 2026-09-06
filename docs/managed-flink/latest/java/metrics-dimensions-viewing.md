

# View CloudWatch metrics
<a name="metrics-dimensions-viewing"></a>

You can view CloudWatch metrics for your application using the Amazon CloudWatch console or the AWS CLI.

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. In the **CloudWatch Metrics by Category** pane for Managed Service for Apache Flink, choose a metrics category.

1. In the upper pane, scroll to view the full list of metrics.

**To view metrics using the AWS CLI**
+ At a command prompt, use the following command.

  ```
  1. aws cloudwatch list-metrics --namespace "AWS/KinesisAnalytics" --region {{region}}
  ```
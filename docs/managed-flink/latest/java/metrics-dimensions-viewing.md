Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# View CloudWatch metrics

You can view CloudWatch metrics for your application using the Amazon CloudWatch console or the
AWS CLI.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **CloudWatch Metrics by Category** pane for
   Managed Service for Apache Flink, choose a metrics category.
4. In the upper pane, scroll to view the full list of metrics.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command.

```
`aws cloudwatch list-metrics --namespace "AWS/KinesisAnalytics" --region `region``

```

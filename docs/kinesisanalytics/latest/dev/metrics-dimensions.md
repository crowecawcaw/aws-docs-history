After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Viewing Metrics and Dimensions

When your application processes data streams, sends the following metrics and dimensions to CloudWatch. You can use the following procedures
to view the metrics for .

On the console, metrics are grouped first by service namespace, and then by the
dimension combinations within each namespace.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **CloudWatch Metrics by Category** pane for ,
   choose a metrics category.
4. In the upper pane, scroll to view the full list of metrics.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command.

```
`aws cloudwatch list-metrics --namespace "AWS/KinesisAnalytics" --region `region``

```

metrics are collected at the following levels:

- Application
- Input stream
- Output stream

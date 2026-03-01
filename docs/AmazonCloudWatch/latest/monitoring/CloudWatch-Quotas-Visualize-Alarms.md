# Visualizing your service quotas and setting alarms

For some AWS services, you can use the usage metrics to visualize your current service usage on CloudWatch graphs and
dashboards. You can use a CloudWatch metric math function to display the service quotas for those
resources on your graphs. You can also configure alarms that alert you when your usage
approaches a service quota. For more information about service quotas, see [What Is Service Quotas](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")
in the _Service Quotas User Guide_.

If you are signed in to an account that is set up as a monitoring account in CloudWatch cross-account
observability, you can use that monitoring account to visualize service quotas and set alarms for metrics in the
source accounts that are linked to that monitoring account. For more information, see
[CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

The following services
integrate their usage metrics with Service Quotas:

- AWS CloudHSM
- [Amazon Chime SDK](../../../chime-sdk/latest/dg/usage-metrics.md "../../../chime-sdk/latest/dg/usage-metrics.md")
- [Amazon CloudWatch](CloudWatch-Usage-Metrics.md "CloudWatch-Usage-Metrics.md")
- [Amazon CloudWatch Logs](../logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md#CloudWatchLogs-Usage-Metrics "../logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md#CloudWatchLogs-Usage-Metrics")
- [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/metrics-dimensions.md "../../../amazondynamodb/latest/developerguide/metrics-dimensions.md")
- [Amazon EC2](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#service-quota-metrics "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md#service-quota-metrics")
- [Amazon Elastic Container Registry](../../../AmazonECR/latest/userguide/monitoring-usage.md "../../../AmazonECR/latest/userguide/monitoring-usage.md")
- Elastic Load Balancing
- AWS Fargate
- [AWS Fault Injection Service](../../../fis/latest/userguide/monitoring-cloudwatch.md "../../../fis/latest/userguide/monitoring-cloudwatch.md")
- [AWS Interactive Video Service](../../../ivs/latest/userguide/service-quotas.md#quotas-cloudwatch-integration "../../../ivs/latest/userguide/service-quotas.md#quotas-cloudwatch-integration")
- AWS Key Management Service
- [Amazon Data Firehose](../../../firehose/latest/dev/monitoring-with-cloudwatch-metrics.md#fh-metrics-usage "../../../firehose/latest/dev/monitoring-with-cloudwatch-metrics.md#fh-metrics-usage")
- [Amazon Location Service](../../../location/latest/developerguide/monitoring-using-cloudwatch.md#metrics-exported-to-cloudwatch "../../../location/latest/developerguide/monitoring-using-cloudwatch.md#metrics-exported-to-cloudwatch")
- [Amazon Managed Blockchain (AMB) Query](../../../managed-blockchain/latest/ambq-dg/cw-usage-metrics.md "../../../managed-blockchain/latest/ambq-dg/cw-usage-metrics.md")
- Amazon SageMaker AI
- [Multi-party approval](../../../mpa/latest/userguide/monitoring-cloudwatch.md "../../../mpa/latest/userguide/monitoring-cloudwatch.md")

###### To visualize a service quota and optionally set an alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose **Usage**, and
   then choose **By AWS Resource**.

The list of service quota usage metrics appears. 4. Select the check box next to one of the metrics.

The graph displays your current usage of that AWS resource. 5. To add your service quota to the graph, do the following:

    1. Choose the **Graphed metrics** tab.
    2. Choose **Math expression**, **Start with an empty
     expression**. In the new row, under **Details**, enter
     `SERVICE_QUOTA(m1)`.


    A new line is added to the graph, displaying the service quota for the resource
     represented in the metric.

6. To see your current usage as a percentage of the quota, add a new expression or change the
   current **SERVICE_QUOTA** expression. The new expression to use
   is `m1/SERVICE_QUOTA(m1)*100`.
7. (Optional) To set an alarm that notifies you if you approach the service quota, do the following:
   1. On the row with `m1/SERVICE_QUOTA(m1)*100`,
      under **Actions**, choose the alarm icon. It looks like a bell.

   The alarm creation page appears. 2. Under **Conditions**, ensure that **Threshold
   type** is **Static** and **Whenever Expression1
   is** is set to **Greater**. Under
   **than**, enter `80`. This creates an alarm
   that goes into ALARM state when your usage exceeds 80 percent of the quota. 3. Choose **Next**. 4. On the next page, select an Amazon SNS topic or create a new one, and then choose
   **Next**. The topic you select is notified when the alarm goes to
   ALARM state. 5. On the next page, enter a name and description for the alarm, and then
   choose **Next**. 6. Choose **Create alarm**.

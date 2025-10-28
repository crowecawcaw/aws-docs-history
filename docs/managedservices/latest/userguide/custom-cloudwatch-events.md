# Creating custom CloudWatch metrics and alarms in AMS

You can store your business and application metrics in Amazon CloudWatch. You can view graphs, and set alarms based on
these metrics, just as you can for the metrics that CloudWatch already stores for your AWS Managed Services (AMS) resources. To learn more about CloudWatch, see
[Amazon CloudWatch Concepts](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md").

Amazon SNS allows applications to send time-critical messages to multiple subscribers through a "push" mechanism
against the AMS Managed Monitoring System or MMS, Amazon SNS (SNS) topic that the alarms are published to; in this case, MMS and your SQS queues.
You can use CloudWatch to create custom metrics and, through an SNS topic, have AMS alarm you appropriately. To do this, follow these steps.

###### Note

This process doesn't work for immutable deployments that rely on updated AMIs deployed to Auto Scaling groups,
it is suitable for mutable application (not ASG) deployments.

Setting up a custom metric within the limitations of AMS Advanced, is a complex task. For an example from CloudWatch, see
[Example: Count occurrences of a term](../../../AmazonCloudWatch/latest/logs/CountOccurrencesExample.md "../../../AmazonCloudWatch/latest/logs/CountOccurrencesExample.md").

1. Produce your application monitoring script and custom metric (such as the count occurrences example). For more information and access to example scripts, see
   [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/mon-scripts.md "../../../AWSEC2/latest/UserGuide/mon-scripts.md").
2. Upload your monitoring script. To upload the monitoring script to your Auto Scaling group or Amazon EC2
   instance configuration, you can use **UserData** when configuring your Auto Scaling group or
   Amazon EC2 instance, or, if your application was deployed with CodeDeploy, you can modify the configuration with a
   Deployment | Applications | CodeDeploy application | Deploy CT (ct-2edc3sd1sqmrb).
3. Publish your custom metric to CloudWatch (the first time you publish a data point for a new custom metric, it is created), see
   [Publish Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md").
4. To integrate your customer metric to your application monitoring system, request AMS create an SNS
   topic for the metric by submitting an RFC with the Deployment | Monitoring and notification | SNS | Create change type (ct-3dfnglm4ombbs).
5. Create the CloudWatch alarm, see
   [Creating Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

###### Important

Monitoring data must be sent to this path [infra/`INSTANCE_ID`/`YOUR_CUSTOM_METRIC`].

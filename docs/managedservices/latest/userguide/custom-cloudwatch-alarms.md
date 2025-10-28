# Creating additional CloudWatch alarms in AMS

You can create new CloudWatch alarms using the AWS Managed Services (AMS) Deployment | Monitoring and notification | CloudWatch | Create alarms change type.

###### Important

AMS does not monitor CloudWatch alarms created by you.

Using custom CloudWatch metrics and alarms for Amazon EC2 instances (works only for mutable deployments that do not
rely on updated AMIs deployed to Auto Scaling groups):

1. Produce your application monitoring script and custom metric. For more information and access to example scripts, see
   [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/mon-scripts.md "../../../AWSEC2/latest/UserGuide/mon-scripts.md").
   The Amazon CloudWatch monitoring scripts for Linux Amazon EC2 instances demonstrate how to produce and consume Amazon CloudWatch custom metrics. These sample Perl scripts comprise a fully
   functional example that reports memory, swap, and disk space utilization metrics for a Linux instance.
2. Upload your monitoring script. To upload the monitoring script to your Auto Scaling group or Amazon EC2 instance configuration, you can use UserData when configuring
   your Auto Scaling group or Amazon EC2 instance, or, if your application was deployed with CodeDeploy, you can modify the
   configuration with a Deployment | Applications | CodeDeploy application | Deploy CT (ct-2edc3sd1sqmrb).
3. Publish your custom metric to CloudWatch (the first time you publish a data point for a new custom metric, it is created), see
   [Publishing Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md").
4. Create the CloudWatch alarm, see
   [Create a CloudWatch Alarm for an Instance](../../../AWSEC2/latest/UserGuide/using-cloudwatch-createalarm.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch-createalarm.md").

###### Important

Monitoring data must be sent to this path [`infra/INSTANCE_ID/YOUR_CUSTOM_METRIC`]

To modify or delete a CloudWatch alarm, submit an RFC with the Management | Other | Other | Create change type (ct-1e1xtak34nx76) with the parameters required to complete the action
as described in the Amazon CloudWatch API reference
[PutMetricAlarm](../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md "../../../AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.md").

You can use the CloudWatch event stream. AMS is integrated with CloudWatch and you can request that any AWS API call trigger a CloudWatch event.

To do this, submit a Management | Other | Other | Update CT (ct-0xdawir96cy7k) with the API calls that you are
interested in. An AMS operator will talk to you to gather requirements. To learn more, see the
[Amazon CloudWatch Documentation](../../../cloudwatch/index.md "../../../cloudwatch/index.md").

To get access to the CloudWatch event stream, submit a Management | Other | Other | Update CT (ct-0xdawir96cy7k) to
add a party to the SNS notification topic. An AMS operator will talk to you to gather requirements.

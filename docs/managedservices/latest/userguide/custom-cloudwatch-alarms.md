

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Creating additional CloudWatch alarms in AMS
<a name="custom-cloudwatch-alarms"></a>

You can create new CloudWatch alarms using the AWS Managed Services (AMS) Deployment \| Monitoring and notification \| CloudWatch \| Create alarms change type.

**Important**  
AMS does not monitor CloudWatch alarms created by you.

Using custom CloudWatch metrics and alarms for Amazon EC2 instances (works only for mutable deployments that do not rely on updated AMIs deployed to Auto Scaling groups):

1. Produce your application monitoring script and custom metric. For more information and access to example scripts, see [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html). The Amazon CloudWatch monitoring scripts for Linux Amazon EC2 instances demonstrate how to produce and consume Amazon CloudWatch custom metrics. These sample Perl scripts comprise a fully functional example that reports memory, swap, and disk space utilization metrics for a Linux instance.

1. Upload your monitoring script. To upload the monitoring script to your Auto Scaling group or Amazon EC2 instance configuration, you can use UserData when configuring your Auto Scaling group or Amazon EC2 instance, or, if your application was deployed with CodeDeploy, you can modify the configuration with a Deployment \| Applications \| CodeDeploy application \| Deploy CT (ct-2edc3sd1sqmrb).

1. Publish your custom metric to CloudWatch (the first time you publish a data point for a new custom metric, it is created), see [Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html).

1. Create the CloudWatch alarm, see [Create a CloudWatch Alarm for an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-createalarm.html).

**Important**  
Monitoring data must be sent to this path [`infra/INSTANCE_ID/YOUR_CUSTOM_METRIC`]

To modify or delete a CloudWatch alarm, submit an RFC with the Management \| Other \| Other \| Update change type (ct-0xdawir96cy7k) with the parameters required to complete the action as described in the Amazon CloudWatch API reference [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html).

You can use the CloudWatch event stream. AMS is integrated with CloudWatch and you can request that any AWS API call trigger a CloudWatch event.

To do this, submit a Management \| Other \| Other \| Update CT (ct-0xdawir96cy7k) with the API calls that you are interested in. An AMS operator will talk to you to gather requirements. To learn more, see the [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/index.html).

To get access to the CloudWatch event stream, submit a Management \| Other \| Other \| Update CT (ct-0xdawir96cy7k) to add a party to the SNS notification topic. An AMS operator will talk to you to gather requirements.
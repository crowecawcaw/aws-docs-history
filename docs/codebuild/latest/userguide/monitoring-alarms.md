# Monitor CodeBuild builds with CloudWatch alarms

You can create a CloudWatch alarm for your builds. An alarm watches a single metric over a period of time that you specify and performs one or more actions
based on the value of the metric relative to a specified threshold over a number of time periods. Using native CloudWatch alarm functionality, you can specify any
of the actions supported by CloudWatch when a threshold is exceeded. For example, you can specify that an Amazon SNS notification is sent when more than three builds
in your account fail within fifteen minutes.

###### To create a CloudWatch alarm for a CodeBuild metric

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**.
3. Choose **Create Alarm**.
4. Under **CloudWatch Metrics by Category**, choose **CodeBuild
   Metrics**. If you know you want only project-level metrics, choose **By
   Project**. If you know you want only account-level metrics, choose **Account
   Metrics**.
5. On **Create Alarm**, if it isn't already selected, choose **Select Metric**.
6. Choose a metric for which you want to create an alarm. The options are **By
   Project** or **Account Metrics**.
7. Choose **Next** or **Define Alarm** and then create your
   alarm. For more information, see [Creating
   Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_. For more information
   about setting up Amazon SNS notifications when an alarm is triggered, see [Set up Amazon SNS notifications](../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md "../../../AmazonCloudWatch/latest/monitoring/US_SetupSNS.md") in the _Amazon SNS
   Developer Guide_.
8. Choose **Create Alarm**.

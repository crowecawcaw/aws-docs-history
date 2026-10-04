

# Monitoring
<a name="nx-notify-scale-monitoring"></a>

AWS End User Messaging gives you two complementary views of your Notify messaging, plus a record of your API activity. This section describes how to set up each one.


**Ways to monitor your Notify messaging**  

| What you monitor | How it works | 
| --- | --- | 
| Overall delivery health | Amazon CloudWatch metrics aggregate your Notify sending into near real-time numbers (text and voice messages sent, delivered, and blocked, plus Notify spend) that you watch on dashboards and alarm on. | 
| Granular per-message events | Message events report what happened to each individual message as it is sent and delivered. You route them to a destination with a configuration set, or consume them from Amazon EventBridge. | 
| API activity | AWS CloudTrail logs the AWS End User Messaging API calls made in your account. | 

## Monitoring with CloudWatch
<a name="nx-notify-scale-monitoring-cloudwatch"></a>

You can monitor Notify using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch retains metric data for 15 months, so you can access historical information and gain a better perspective on how your messaging is performing. The namespace for AWS End User Messaging metrics is `AWS/SMSVoice`.

**Note**  
AWS End User Messaging uses an AWS Identity and Access Management (IAM) service-linked role to publish metrics to CloudWatch. The service creates this role for you the first time you perform an action that publishes metrics, so in most cases you do not need to create it yourself.


**Common Notify metrics (AWS/SMSVoice namespace)**  

| Metric | Description | 
| --- | --- | 
| NotifyTextMessagePartsSent | The number of Notify text message parts sent. | 
| NotifyTextMessagePartsDelivered | The number of Notify text message parts confirmed delivered. | 
| NotifyTextMessagesBlocked | The number of Notify text messages that were blocked. | 
| NotifyVoiceMessagesSent | The number of Notify voice messages sent. | 
| NotifyVoiceMessagesDelivered | The number of Notify voice messages confirmed delivered. | 
| NotifyVoiceMessagesBlocked | The number of Notify voice messages that were blocked. | 
| NotifyMessageMonthlySpend | The month-to-date spend on Notify messages, in US Dollars. | 

With CloudWatch, you can also create alarms that trigger based on metric thresholds. For example, you can create an alarm on a Notify delivery or spend metric so that when the metric crosses a threshold you choose, an email notification is sent to an Amazon SNS topic.

------
#### [ Console ]

**To create an alarm that notifies you when a Notify metric exceeds a threshold**

1. Open the CloudWatch console.

1. Choose **Alarms** in the navigation pane, and then choose **Create alarm**.

1. Choose **Select metric**, choose the `AWS/SMSVoice` namespace, and choose the Notify metric that you want to set an alarm for.

1. Set the statistic, period, and condition, and enter the threshold value.

1. For the alarm action, choose an existing Amazon SNS topic to notify or create a new one, enter a name for the alarm, and choose **Create alarm**.

------
#### [ AWS CLI ]

Use the [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command. The following example alarms on Notify spend and notifies an Amazon SNS topic.

```
$ aws cloudwatch put-metric-alarm \
> --alarm-name {{HighNotifySpend}} \
> --namespace AWS/SMSVoice \
> --metric-name NotifyMessageMonthlySpend \
> --statistic Maximum \
> --period 3600 \
> --evaluation-periods 1 \
> --threshold 100 \
> --comparison-operator GreaterThanThreshold \
> --alarm-actions arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{snsTopic}}
```

------

## Send events to a destination with a configuration set
<a name="nx-notify-scale-monitoring-events"></a>

AWS End User Messaging emits an event for each message as it moves through sending and delivery. You route these events to a destination by creating a configuration set, adding one or more event destinations, and selecting the event types to publish. You can send events to Amazon CloudWatch Logs, Amazon Data Firehose, or an Amazon SNS topic, and you can also consume them from Amazon EventBridge. For more information, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

## Logging API calls with CloudTrail
<a name="nx-notify-scale-monitoring-cloudtrail"></a>

AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS End User Messaging, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
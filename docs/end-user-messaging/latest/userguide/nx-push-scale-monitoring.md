

# Monitoring
<a name="nx-push-scale-monitoring"></a>

AWS End User Messaging Push gives you per-message delivery events plus a record of your API activity. This section describes how to set up each one.


**Ways to monitor your push messaging**  

| What you monitor | How it works | 
| --- | --- | 
| Per-message delivery events | Push notification events report what happened to each individual message, such as when a message is delivered or fails at the push notification service. You route these events to a destination by associating a configuration set with your messaging. | 
| Operational metrics | Amazon CloudWatch collects operational metrics for the AWS services that receive your push events, such as the Amazon SNS topic and Lambda function in your event-destination pipeline, so you can alarm on backlogs and errors. | 
| API activity | AWS CloudTrail logs the AWS End User Messaging API calls made in your account. | 

## Send events to a destination with a configuration set
<a name="nx-push-scale-monitoring-events"></a>

AWS End User Messaging Push emits an event for each message as it is sent and delivered, including whether the push notification service accepted or rejected the message. You route these events to a destination by creating a configuration set, adding one or more event destinations, and selecting the event types to publish. The underlying push notification services, such as APNs, FCM, ADM, and Baidu Cloud Push, also return their own delivery feedback, which the events reflect. For more information, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

## Monitoring with CloudWatch
<a name="nx-push-scale-monitoring-cloudwatch"></a>

Push messaging runs through a pipeline of AWS services that each publish their own metrics to CloudWatch, so you build your operational dashboards and alarms on those metrics. For example, you can watch the Amazon SNS delivery metrics for the topic that receives your push events, and the Lambda invocation and error metrics for the function that processes them, and create an alarm when errors or a processing backlog cross a threshold. For the metrics each service publishes, see the monitoring documentation for Amazon SNS and Lambda.

## Logging API calls with CloudTrail
<a name="nx-push-scale-monitoring-cloudtrail"></a>

AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS End User Messaging, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
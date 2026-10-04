

# Monitoring
<a name="nx-whatsapp-scale-monitoring"></a>

AWS End User Messaging gives you two complementary views of your WhatsApp messaging, plus a record of your API activity. This section describes how to set up each one.


**Ways to monitor your WhatsApp messaging**  

| What you monitor | How it works | 
| --- | --- | 
| Per-message events | WhatsApp message and event records report what happened to each individual message as it is sent, delivered, and read. You route these records to an event destination, and you receive inbound messages and status updates through the same destination. | 
| Operational metrics | Amazon CloudWatch collects operational metrics for the AWS services that process your WhatsApp traffic, such as the Amazon SNS topic and Lambda function in your event-destination pipeline, so you can alarm on backlogs and errors. | 
| API activity | AWS CloudTrail logs the AWS End User Messaging API calls made in your account. | 

## Receive message and event records
<a name="nx-whatsapp-scale-monitoring-events"></a>

WhatsApp delivery status, read receipts, and inbound customer messages arrive as event records that AWS End User Messaging publishes to an event destination that you associate with your WhatsApp business account. You set up an Amazon SNS topic as the destination and subscribe your own processing, such as a Lambda function, to that topic. Each record identifies the message, its status, and the phone number it relates to, so you can track delivery outcomes and respond to inbound messages. For more information, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

## Monitoring with CloudWatch
<a name="nx-whatsapp-scale-monitoring-cloudwatch"></a>

WhatsApp messaging runs through a pipeline of AWS services that each publish their own metrics to CloudWatch, so you build your operational dashboards and alarms on those metrics. For example, you can watch the Amazon SNS delivery metrics for the topic that receives your WhatsApp event records, and the Lambda invocation and error metrics for the function that processes them, and create an alarm when errors or a processing backlog cross a threshold. For the metrics each service publishes, see the monitoring documentation for Amazon SNS and Lambda.

## Logging API calls with CloudTrail
<a name="nx-whatsapp-scale-monitoring-cloudtrail"></a>

AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS End User Messaging, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
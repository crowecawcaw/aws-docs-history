

# Centralized Alarms and Notifications
<a name="centralized-alarms-notifications"></a>

Publication date: **January 10, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to deploy a serverless monitoring and alarm system. The system sends workload-specific notifications.

## Centralized Alarms and Notifications
<a name="diagram1"></a>

![Architecture diagram showing a centralized alarm and notification system with Amazon CloudWatch and Amazon Simple Notification Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/centralized-alarms-notifications/images/centralized-alarms-notifications.png)


1. Create cross-account [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms in the central monitoring account. You can tag CloudWatch alarms with resource identifiers.

1. Store workload-specific configuration in the central monitoring account. It contains details on connected workload [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topics.

1. (Optional) Use an intermediary [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) queue to buffer [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) invocations if concurrency issues occur.

1. A central Amazon SNS topic receives alarm events.

1. A serverless function receives the alarm event and queries parameter store for account and workload Amazon SNS delivery topics. The function validates configured topics, cycles through them, and sends the payload.

1. Send messages where no workload configuration exists to a monitoring Amazon SQS dead letter queue (DLQ).

1. Amazon SNS topics configured to receive the message invoke an associated AWS Lambda function to process the message.

1. Each AWS Lambda function performs a unique action (for example, sends email).

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon CloudWatch product page](https://aws.amazon.com/cloudwatch/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 10, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
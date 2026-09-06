

# Resilient AWS IoT Events Alarm for AWS IoT SiteWise
<a name="resilient-iot-events-alarm-sitewise"></a>

Publication date: **April 5, 2021 ([Diagram history](#riea-diagram-history))**

With this architecture, you can efficiently monitor AWS IoT SiteWise metrics by using an [AWS IoT Events](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-events) alarm on an unstable network connection. This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

## Resilient IoT Events alarm architecture diagram
<a name="riea-diagram"></a>

![Reference architecture for a resilient AWS IoT Events alarm for AWS IoT SiteWise.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/resilient-iot-events-alarm-sitewise/images/resilient-aws-iot-events-alarm-for-aws-iot-sitewise-ra.png)


The following steps describe the architecture:

1. AWS IoT Greengrass configures a gateway to send industrial internet of things (IIoT) data to AWS IoT SiteWise.

1. AWS IoT SiteWise collects, stores, organizes, and monitors data from industrial equipment at scale. Operational technology (OT) can quickly compute industrial performance metrics for remote monitoring.

1. AWS IoT Core rules interact with MQTT topics of AWS IoT SiteWise metrics that OT wants to monitor. The rule augments data with an AlarmID so data goes to a specific alarm detector instance.

1. An Lambda function normalizes the JSON payload to extract the AlarmID and metric property values. It then sends them as inputs to AWS IoT Events.

1. (Optional) The Lambda function sends all AlarmID records to [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for future use.

1. CloudWatch Logs collects the AWS IoT SiteWise **Gateway.Heartbeat** metric to monitor health.

1. An CloudWatch alarm tracks CloudWatch Logs events where heartbeat signals are missing due to an internet or AWS service outage. The alarm then transitions to the ON state.

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) triggers an Lambda function when the CloudWatch alarm turns ON.

1. EventBridge triggers an Lambda function to send the switch-off signal with AlarmID records to the AWS IoT Events alarm. You can obtain multiple AlarmIDs from DynamoDB.

1. The AWS IoT Events alarm detects a breach of metric property values. This alarm switches off automatically when the network is intermittent or disconnected.

1. AWS IoT Events sends an [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS) notification if the alarm triggers.

## Further reading
<a name="riea-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="riea-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#riea-diagram-history) | Reference architecture diagram first published. | April 5, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
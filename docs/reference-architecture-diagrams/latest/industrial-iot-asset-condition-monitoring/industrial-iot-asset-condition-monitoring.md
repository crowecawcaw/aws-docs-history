

# AWS Industrial IoT Asset Condition Monitoring
<a name="industrial-iot-asset-condition-monitoring"></a>

Publication date: **August 20, 2020 ([Diagram history](#acm-diagram-history))**

With this architecture, you can monitor the health of factory equipment, detect fault conditions, and respond to events. This solution uses [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), and [AWS IoT Events](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-events).

## Asset condition monitoring architecture diagram
<a name="acm-diagram"></a>

![Reference architecture diagram for monitoring factory equipment health and detecting fault conditions on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-iot-asset-condition-monitoring/images/aws-industrial-asset-condition-monitoring-ra.png)


The following steps describe the architecture:

1. Configure the AWS IoT SiteWise Connector on AWS IoT Greengrass to connect and collect data from factory machines by using OPC Unified Architecture (OPC-UA).

1. Configure the AWS IoT Greengrass Connector for [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions to interface with local Modbus, MQTT, or HTTP traffic.

1. Configure rules in AWS IoT Core to trigger events that send messages to AWS IoT Events and [AWS IoT Analytics](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-analytics).

1. In AWS IoT Analytics, set up a channel, pipeline, and data store to collect and process device telemetry.

1. Derive insights with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) on AWS IoT Analytics.

1. Use AWS IoT SiteWise to model assets that represent on-premises devices, equipment, and processes.

1. Create a web portal with AWS IoT SiteWise Monitor to visualize equipment data and health metrics in near real time.

1. Use AWS IoT Events to detect complex events across multiple data sources and trigger response messages.

1. Publish [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/) messages on events to notify operators of fault conditions.

1. Create a Lambda function to send mitigation commands back to assets through AWS IoT Core.

1. Use AWS IoT Core to forward commands to AWS IoT Greengrass for mitigation actions on the factory floor equipment.

## Further reading
<a name="acm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="acm-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#acm-diagram-history) | Reference architecture diagram first published. | August 20, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
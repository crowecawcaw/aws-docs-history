

# TR-069 and AWS
<a name="tr-069-and-aws"></a>

Publication date: **2021 ([Diagram history](#tr069-history))**

With this architecture, you can connect TR-069 customer premises equipment (CPE) fleets with AWS for bulk data collection and analytics. The solution uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for device connectivity, [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) for ingestion, and Amazon Managed Service for Apache Flink for real-time analytics.

## TR-069 and AWS diagram
<a name="tr069-diagram"></a>

![Reference architecture diagram showing how to connect TR-069 CPE fleets with AWS for data collection, analytics, and AI/ML by using AWS IoT Core, Amazon Kinesis, and Amazon Data Firehose.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/tr-069-and-aws/images/tr-069-and-aws.png)


The following steps describe the data flow and analytics pipeline for this architecture:

1. Configure remote gateways to send key performance indicators to AWS IoT Core through an Auto Configuration Server (ACS) instance. The ACS uses the TR-069 protocol to configure remote gateways. Deploy the ACS on-premises or on AWS.

1. Send TR-181 data model parameters from remote gateways to AWS IoT Core by using HTTPS with custom domains or Message Queuing Telemetry Transport (MQTT).

1. (Optional) Use an AWS IoT Core custom authorizer for authentication if ingestion is done over HTTPS.

1. Route authenticated messages to the rules engine through the Amazon Kinesis Data Streams action.

1. Normalize the TR-181 payload by using Amazon Managed Service for Apache Flink. Output the processed data to another stream in Amazon Kinesis Data Streams. Perform real-time analytics to detect CPE problems. Use findings to start actions on the ACS.

1. Store normalized TR-181 data in a data lake repository by using Amazon Data Firehose.

1. Bring metrics collected by the ACS (outside TR-069) into the data lake through [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/).

1. Visualize data and monitor fleet health by using [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/), and other tools.

1. Use data and insights collected at the data lake to feed external systems. Start actions on the ACS based on findings.

1. Notify operational personnel and end customers based on findings by using [Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) and [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

## Further reading
<a name="tr069-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="tr069-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#tr069-history) | Reference architecture diagram first published. | January 1, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.


# Cold Chain Logistics Powered by Mendix: Mendix Cloud
<a name="cold-chain-logistics-mendix-cloud"></a>

Publication date: **April 29, 2022 ([Diagram history](#ccm-cloud-history))**

With this architecture, you can build low-code cold chain logistics applications on Mendix Cloud, an application platform as a service (aPaaS). Mendix Cloud connects to AWS services through native connectors that use standard AWS SDKs and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) endpoints. The solution uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for device connectivity and [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/) for automated image analysis.

## Cold chain logistics Mendix Cloud diagram
<a name="ccm-cloud-diagram"></a>

![Reference architecture diagram showing cold chain logistics on Mendix Cloud integrated with AWS IoT Core, Amazon Rekognition, and Amazon Timestream.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cold-chain-logistics-mendix/images/cold-chain-logistics-mendix-cloud.png)


The following steps describe the integration components for this architecture:

1. Publish telemetry messages from IoT sensors to AWS IoT Core. Process messages according to custom rules and forward them into the backend service structure.

1. Feed information from external systems into the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake.

1. Use Mendix connectors for IoT to publish and subscribe to IoT devices by using the MQTT protocol. Include condition-based logic to control actuators by updating a device shadow.

1. Incorporate external databases ([Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/)) directly in your Mendix app by using the JDBC driver with the database connector.

1. Upload, modify, and delete unstructured data and files by using the Mendix AWS and Amazon S3 connector. Back up data for long-term storage or reporting.

1. Analyze images by using the Amazon Rekognition connector microflows.

1. Explore topics and publish messages with attributes by using the Mendix [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) connector.

1. Access backend services through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/). Call any AWS service that supports REST API with Signature V4 authentication.

1. Retrieve and analyze data lake content by using standard SQL with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Store time-series data from IoT sensors in [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/). Query records from Mendix by using the database connector (JDBC).

1. Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) as a backend database for systems that require high-performance data processing at scale.

## Further reading
<a name="ccm-cloud-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ccm-cloud-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ccm-cloud-history) | Reference architecture diagram first published. | April 29, 2022 | 
| [Initial publication](cold-chain-logistics-mendix-private.md#ccm-private-history) | Reference architecture diagram first published. | April 29, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
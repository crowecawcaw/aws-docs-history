

# AWS Industrial Anomaly Detection Using AWS IoT
<a name="industrial-anomaly-detection-iot"></a>

Publication date: **October 12, 2021 ([Diagram history](#iad-diagram-history))**

With this architecture, you can detect performance anomalies through hot, warm, and cold analysis paths. You can use AWS IoT, analytics, and ML services to inform operational technology (OT) teams of equipment issues. This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), and [Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/).

## Industrial anomaly detection architecture diagram
<a name="iad-diagram"></a>

![Reference architecture diagram for industrial anomaly detection using AWS IoT with hot, warm, and cold analysis paths.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-anomaly-detection-iot/images/iot-industrial-anomaly-detection-ra.png)


The following steps describe the architecture:

1. Ingest telemetry from industrial assets through AWS IoT Greengrass edge connectors. Run hot anomaly detection at the edge with stream analytics and ML inference.

1. Edge-to-cloud interfaces AWS IoT Core and AWS IoT SiteWise ingest telemetry data.

1. Amazon Managed Service for Apache Flink runs queries for warm-path anomaly detection.

1. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) data lake stores raw and processed telemetry, trained ML models, and inference results.

1. Train ML models for cold-path batch inference with Amazon SageMaker AI or Amazon Lookout for Equipment.

1. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions analyze batch inference results.

1. OT teams consume alerts from [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS) as emails, texts, or ticketing integrations.

1. No-code dashboards through AWS IoT SiteWise Monitor assess real-time and historical performance.

1. [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) evaluates history of anomalies and fleet performance.

## Further reading
<a name="iad-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Data Platform on AWS](../industrial-data-platform/industrial-data-platform.html)

## Diagram history
<a name="iad-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#iad-diagram-history) | Reference architecture diagram first published. | October 12, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
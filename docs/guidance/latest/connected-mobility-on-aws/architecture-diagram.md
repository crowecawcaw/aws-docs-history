# Architecture diagram

The following diagram illustrates the complete architecture for the Guidance for Connected Mobility on AWS, showing the data flow from connected vehicles through ingestion, processing, storage, and visualization layers.

![Connected Mobility Complete Architecture](/images/guidance/latest/connected-mobility-on-aws/images/architecture_final.png)

_Figure 1: Connected Mobility Guidance Architecture on AWS_

The architecture demonstrates a linear data flow optimized for automotive telemetry processing:

- Connected vehicles publish telemetry via MQTT to AWS IoT Core
- IoT Core routes messages to Amazon MSK for durable streaming
- Apache Flink applications process streams in real-time
- Processed data is stored in DynamoDB and S3
- Fleet managers access data through the web dashboard
- CloudWatch provides comprehensive monitoring and observability

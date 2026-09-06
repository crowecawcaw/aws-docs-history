

# Last Mile Delivery
<a name="last-mile-delivery"></a>

Publication date: **October 7, 2020 ([Diagram history](#lmd-history))**

With this architecture, you can optimize your last mile delivery operations. Improve asset utilization and reduce operational costs by eliminating data silos. Analyze data in real time and disseminate alerts across your fleet. The solution uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for vehicle connectivity, [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) for route calculation, and [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) for graph-based routing.

## Last mile delivery diagram
<a name="lmd-diagram"></a>

![Reference architecture diagram showing how to optimize last mile delivery by using AWS IoT Core, AWS Fargate, Amazon Neptune, and Amazon DocumentDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/last-mile-delivery/images/last-mile-delivery.png)


The following steps describe the data flow and delivery components for this architecture:

1. Decouple upstream dependencies with an event-based microservices architecture. Ingest order and location data to increase business agility and lower costs.

1. Ingest vehicle data in real time through the OBD2 interface and AWS IoT Core. Monitor vehicle status continuously for safety by using [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/). Automate outbound calls to drivers and maintenance crews with [Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/).

1. Implement a streaming Internet of Things (IoT) extract, transform, and load (ETL) pipeline without managing infrastructure. Update safe driving scorecards in near real time. Improve safety and reduce claims liability.

1. Create a scalable, real-time mobile fulfillment application for drivers by using AWS AppSync. Protect front-end assets with [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/). Calculate optimal driving routes with AWS Fargate and Amazon Neptune.

1. Use [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/) to track when drivers arrive at the next stop. Increase the accuracy of estimated time of arrival (ETA) communications.

1. Persist IoT data from vehicles at scale by using [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/) and [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) Intelligent-Tiering. Use [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) to set up a data lake as the single source of truth for BI and analytics.

## Further reading
<a name="lmd-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="lmd-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#lmd-history) | Reference architecture diagram first published. | October 7, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.


# Machine Learning Enabled Predictive Maintenance on AWS
<a name="ml-predictive-maintenance"></a>

Publication date: **September 13, 2022 ([Diagram history](#mlpm-diagram-history))**

With this architecture, you can implement condition-based maintenance with near real-time inference results and notifications for sucker rod pumping systems. These systems are the most widely applied artificial lift equipment in oil and gas. This architecture uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/), [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), and [Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/).

## ML predictive maintenance architecture diagram
<a name="mlpm-diagram"></a>

![Reference architecture diagram for machine learning enabled predictive maintenance of sucker rod pumps on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ml-predictive-maintenance/images/machine-learning-enabled-predictive-maintenance-ra.png)


The following steps describe the architecture:

1. Use Message Queuing Telemetry Transport (MQTT) protocol in an IoT device SDK to ingest data to AWS IoT Core from sucker rod pumps.

1. Configure an IoT rule in AWS IoT Core to store data in Amazon Timestream as time series data.

1. Visualize and monitor sensor data with Amazon Managed Grafana from a Timestream database.

1. Configure an IoT rule in AWS IoT Core to capture, transform, and deliver data to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) with Amazon Data Firehose.

1. Amazon Lookout for Equipment analyzes data from Amazon S3 and trains a unique ML model to detect equipment abnormalities in near real time. Store inference results in Amazon S3.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Data Catalog to categorize data. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) integrates with the catalog for on-demand queries.

1. Display inference results from Athena with Amazon Managed Grafana.

## Further reading
<a name="mlpm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Data Platform on AWS](../industrial-data-platform/industrial-data-platform.html)

## Diagram history
<a name="mlpm-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#mlpm-diagram-history) | Reference architecture diagram first published. | September 13, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
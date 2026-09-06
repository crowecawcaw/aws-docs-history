

# Accelerate Industrial Machine Connectivity on AWS
<a name="industrial-machine-connectivity-eot"></a>

Publication date: **April 22, 2021 ([Diagram history](#eot-diagram-history))**

With this architecture, you can provision asset models and ingest real-time sensor data from industrial historians, OPC servers, and Supervisory Control and Data Acquisition (SCADA) platforms into [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/). You use the Embassy of Things (EOT) Twin Talk Express data sharing platform to connect to OSIsoft PI and CygNet SCADA systems. For more information about Twin Talk, see [Twin Talk platform](https://embassyofthings.com/twintalk/) on the Embassy of Things website.

## Industrial machine connectivity architecture diagram
<a name="eot-diagram"></a>

![Reference architecture diagram for ingesting real-time sensor data from industrial historians and SCADA platforms into AWS IoT SiteWise on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-machine-connectivity-eot/images/cygnet-and-pi-data-to-sitewise-ra.png)


The following steps describe the architecture:

1. The OSIsoft PI system, legacy historians, and CygNet SCADA platform collect real-time data from industrial devices and sensors.

1. The EOT Twin Talk data management platform on an AWS Certified industrial PC ingests real-time sensor data and the asset model from supported historians.

1. Enriched data from Twin Talk goes to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), which triggers a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function.

1. The Lambda function normalizes incoming files to an AWS IoT SiteWise compatible format.

1. Store asset model and definitions in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. DynamoDB Streams triggers a Lambda function to create and update assets in AWS IoT SiteWise.

1. AWS IoT SiteWise filters, transforms, and processes incoming data. It publishes an MQTT message to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) on each property update.

1. An AWS IoT Core rule publishes asset property update messages to [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/).

1. Amazon Data Firehose captures data from AWS IoT Core, transforms it, and delivers the data to Amazon S3.

1. Once data is in Amazon S3, ML and third-party applications can consume the data for reporting, analytics, and model training.

## Further reading
<a name="eot-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Machine Connectivity Quick Start](https://aws.amazon.com/quickstart/architecture/industrial-machine-connectivity/) on the AWS website
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="eot-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#eot-diagram-history) | Reference architecture diagram first published. | April 22, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.


# Industrial Data Platform on AWS
<a name="industrial-data-platform"></a>

Publication date: **May 21, 2021 ([Diagram history](#idp-diagram-history))**

With this architecture, you can ingest and store data from industrial equipment and enterprise applications, contextualize data, and build datasets. You can integrate machine learning (ML) predictions with industrial systems of record. This architecture uses [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Industrial data platform architecture diagram
<a name="idp-diagram"></a>

![Reference architecture diagram for building an industrial data platform on AWS that ingests IIoT and enterprise data for analytics and ML predictions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-data-platform/images/industrial-data-platform-ra.png)


The following steps describe the architecture:

1. Ingest and transform asset, machine, and programmable logic controller (PLC) data with AWS IoT Greengrass connectors and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions at the edge. Stream Industrial Internet of Things (IIoT) data into the data lake from AWS IoT SiteWise through AWS IoT Core and Amazon Data Firehose.

1. Synchronize images to the data lake with AWS Storage Gateway. For IP cameras, use AWS Panorama to transfer images.

1. Stream manufacturing application data with [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) Data Streams or transfer with [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/).

1. Export industrial enterprise application data to the data lake. Store historical records in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and reference data in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Use AWS Glue for data engineering and cataloging data sets.

1. Build ML models with Amazon SageMaker AI, or use AWS Industrial AI services like [Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/) to detect anomalies. Initiate ML inference from Lambda and send results to enterprise applications.

1. Access data sets and results through dashboards and applications by using AWS AppSync.

## Further reading
<a name="idp-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="idp-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#idp-diagram-history) | Reference architecture diagram first published. | May 21, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
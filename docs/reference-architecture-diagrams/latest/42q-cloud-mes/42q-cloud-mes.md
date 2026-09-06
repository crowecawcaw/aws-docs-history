

# 42Q Cloud MES on AWS
<a name="42q-cloud-mes"></a>

Publication date: **October 13, 2022 ([Diagram history](#42q-diagram-history))**

With this architecture, you can build end-to-end data flows using AWS services and the 42Q SaaS manufacturing execution system (MES). You can ingest data from industrial equipment and connect it to the 42Q cloud platform for digital factory integration. This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## 42Q Cloud MES architecture diagram
<a name="42q-diagram"></a>

![Reference architecture diagram for 42Q cloud MES data flows on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/42q-cloud-mes/images/42q-cloud-mes-ra.png)


The following steps describe the architecture:

1. Ingest data from multiple sources. AWS IoT Greengrass connectors provide OPC-UA, Modbus-TCP, Modbus-RTU, and IoT Ethernet IP connectivity.

1. AWS Partner solutions connect to additional data sources and provide context.

1. Ingest data into your AWS account. Select the service based on the source. Use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/), [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/), AWS IoT Core, or [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/).

1. Use AI and ML services such as [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) and Amazon SageMaker AI to build, train, and deploy ML models.

1. Use analytics services including [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).

1. Store data optimized for workload. Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), Amazon S3, [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/), and [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/).

1. Lambda writes data from Amazon S3 or any data store to the 42Q MES API.

1. 42Q Xchange SOAP-based APIs connect ERP and CRM systems to 42Q for digital factory integration.

1. 42Q provides cloud-based MES with simplified access.

1. AWS IoT Greengrass supports legacy printers for on-premises label printing.

## Further reading
<a name="42q-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Data Platform on AWS](../industrial-data-platform/industrial-data-platform.html)

## Diagram history
<a name="42q-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#42q-diagram-history) | Reference architecture diagram first published. | October 13, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.


# Tulip Next-Gen MES on AWS
<a name="tulip-next-gen-mes"></a>

Publication date: **October 11, 2022 ([Diagram history](#tulip-diagram-history))**

With this architecture, you can build end-to-end data flows between the Tulip Frontline Operations Platform and your Amazon VPC. You can generate actionable insights for operational excellence using a manufacturing execution system (MES). This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/).

## Tulip Next-Gen MES architecture diagram
<a name="tulip-diagram"></a>

![Reference architecture diagram for Tulip next-generation MES data flows on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/tulip-next-gen-mes/images/tulip-next-gen-mes-ra.png)


The following steps describe the architecture:

1. Tulip Edge IO device provides connectivity to barcode scanners, cameras, printers, and scales. Tulip Connector host connects to local devices on-premises.

1. Ingest data from multiple sources. AWS IoT Greengrass connectors provide OPC-UA, Modbus-TCP, Modbus-RTU, and EtherNet/IP connectivity.

1. AWS Partner solutions connect to additional data sources and provide context.

1. Select ingestion services based on source. Use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/) for file shares. Use [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/), [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/), AWS IoT Core, or [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) for streaming data.

1. Store data optimized for workload. Use [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for key-value, Amazon S3 for objects, [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) for graphs, [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) for warehousing, [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/) for time series, and [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) for industrial equipment data.

1. Use AI and ML services such as [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) and Amazon SageMaker AI to build, train, and deploy ML models.

1. Use analytics services including [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) for data processing.

1. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) provides protection. Amazon API Gateway supports REST methods for Amazon S3, [Amazon Lookout for Vision](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision/), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/), and [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/).

1. The Tulip platform provides a no-code environment to create applications. Ingest data through Tulip Connectors.

## Further reading
<a name="tulip-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Data Platform on AWS](../industrial-data-platform/industrial-data-platform.html)

## Diagram history
<a name="tulip-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#tulip-diagram-history) | Reference architecture diagram first published. | October 11, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
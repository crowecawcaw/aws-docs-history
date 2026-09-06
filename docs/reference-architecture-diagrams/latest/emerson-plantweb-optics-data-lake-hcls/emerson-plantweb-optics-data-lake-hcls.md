

# Emerson Plantweb Optics Data Lake for Health Care and Life Sciences
<a name="emerson-plantweb-optics-data-lake-hcls"></a>

Publication date: **February 21, 2022 ([Diagram history](#emerson-history))**

With this architecture, you can ingest data from multiple disparate sources into a unified data lake by using Emerson Plantweb Optics Data Lake (PWODL). Use cases include end-to-end batch reporting, real-time exception handling, real-time batch review and release, continuous process verification (CPV), manufacturing quality modeling, and digital technology transfer.

## Emerson Plantweb Optics data lake diagram
<a name="emerson-diagram"></a>

![Reference architecture diagram showing how to ingest manufacturing and laboratory data into a unified data lake by using Emerson PWODL, Amazon Kinesis, Lambda, and SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/emerson-plantweb-optics-data-lake-hcls/images/emerson-plantweb-optics-data-lake-hcls.png)


The following steps describe the data flow and ingestion pipeline for this architecture:

1. Ingest data from several disparate sources and data types by using Emerson Plantweb Optics. Sources can be located on the plant or shop floor, or on manufacturing systems. Available data sources include:
   + Laboratory Information Management System (LIMS)
   + Computerized Maintenance Management System (CMMS)
   + Manufacturing Execution System (MES)
   + Batch Processing System
   + Configuration Management System (CMS)
   + Documents Management System (DMS)
   + Programmable Logic Controllers (PLC)

1. Send data to [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/), [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/), and [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) by using PWODL producer connectors. The PWODL Kinesis producer uses the AWS SDK to call the Kinesis PutRecords API. The Kafka producer connects to Amazon MSK, and the MQTT producer publishes to AWS IoT Core topics.

1. Load data reliably into [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) by using Amazon Data Firehose as part of the AWS data lake.

1. Use [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) to extract key phrases, entities, and sentiment from file-based data sources and log files.

1. Use Amazon Managed Grafana (AMG) for visualization through a plug-in for the PWODL API.

1. Use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for serverless compute to provide read and write services to the PWODL REST API. Write the results of artificial intelligence (AI) and ML calculations from [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) back to on-premises deployments of PWODL.

1. Develop, train, and deploy ML models with SageMaker AI.

1. Set up and govern a regulated landing zone by using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/). This supports Good Automated Manufacturing Practice (GAMP) guidance from the International Society for Pharmaceutical Engineering (ISPE).

1. Use [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) and the [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Data Catalog to govern and catalog data in the lake. Query data with [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and visualize insights with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html).

## Further reading
<a name="emerson-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="emerson-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#emerson-history) | Reference architecture diagram first published. | February 21, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
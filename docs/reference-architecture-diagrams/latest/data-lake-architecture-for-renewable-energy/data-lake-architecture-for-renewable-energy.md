

# Data Lake Architecture for Renewable Energy
<a name="data-lake-architecture-for-renewable-energy"></a>

Publication date: **October 26, 2022 ([Diagram history](#diagram-history))**

This architecture enables you to build a renewable energy data lake that includes telemetry data from IoT devices, and business application data for near real-time monitoring. It also enables you to visualize data and make predictions with machine learning (ML) models.

## Data Lake Architecture for Renewable Energy Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to visualize data and make predictions with machine learning.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-lake-architecture-for-renewable-energy/images/data-lake-architecture-for-renewable-energy.png)


1. Renewable energy data is ingested into **AWS IoT Core** with MQ Telemetry Transport (MQTT) protocol. 

1. Using AWS IoT rules engine within **AWS IoT Core**, telemetry data is routed to **Amazon Timestream** and **Amazon Simple Storage Service** (Amazon S3) through **Amazon Kinesis Data Streams**. Use **Amazon Managed Service for Apache Flink** to transform and analyze streaming data in near real-time. 

1. The schemas for the on-premise databases are discovered and converted by the **AWS Schema Conversion Tool** (AWS SCT). The data is moved by **AWS Database Migration Service** (AWS DMS) to **Amazon S3** and **Amazon Redshift**. 

1. Data stored in **Amazon S3** is crawled by **AWS Glue crawler**. The schemas are discovered and the **AWS Glue Data Catalog** is populated with this metadata. 

1. **AWS Glue** extract, transform, load (ETL) jobs process, transform, and enrich the raw data, and output it in an**Amazon S3** processed bucket. 

1. Schemas and tables are then created in **Amazon Redshift**. Using the `COPY` command, data is loaded into **Amazon Redshift** tables. Business logic data transformations can then be performed by stored procedures. 

1. The **AWS Glue Data Catalog**, **AWS Lake Formation**, and **AWS Identity and Access Management** (IAM) are used to provide centralized security and governance. 

1. **Amazon Athena**, **Amazon Quick**, and **Amazon Managed Grafana** visualize data and build dashboards and reporting. 

1. Use raw datasets with **Amazon SageMaker AI** to train and deploy machine learning models. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 26, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
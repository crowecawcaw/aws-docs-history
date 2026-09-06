

# Supply Chain Data Lake Solution
<a name="supply-chain-data-lake"></a>

Publication date: **May 18, 2022 ([Diagram history](#scdl-history))**

With this architecture, you can build a supply chain data lake on AWS. Ingest data from planning, execution, and real-time shipment status providers. Build cross-category scorecards for analysts and planners. The solution uses [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) for the data lake and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for extract, transform, and load (ETL). [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) provides machine learning (ML) capabilities.

## Supply chain data lake diagram
<a name="scdl-diagram"></a>

![Reference architecture diagram showing how to build a supply chain data lake by using AWS Lake Formation, AWS Glue, SageMaker AI, and Amazon Neptune.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/supply-chain-data-lake/images/supply-chain-data-lake.png)


The following steps describe the data ingestion and analytics pipeline for this architecture:

1. Collect supply chain data from multiple enterprise sources. Include ERP/CRM SaaS applications, manufacturing edge devices, logs, streaming media, and social networks.

1. Ingest data by using [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/), [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/), [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), and [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/).

1. Integrate third-party data (such as weather data) into the data lake by using AWS Data Exchange.

1. Build the scalable supply chain data lake with AWS Lake Formation.

1. Use [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for data lake storage.

1. Use AWS Glue to extract, transform, catalog, and ingest data across multiple data stores such as ERP, planning, and shipment visibility systems.

1. Analyze data in Amazon S3 by using standard SQL with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) as a serverless interactive query service.

1. Build dashboards with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) to help planners drill down from planning to execution to real-time shipment status.

1. Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/) as a cloud data warehouse.

1. Process vast amounts of data by using open-source tools with [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) as the cloud big data platform.

1. Build, train, and deploy ML models with SageMaker AI. Add intelligence to your supply chain applications.

1. Optimize network queries for speed and accuracy by using the [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) graph database.

## Further reading
<a name="scdl-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="scdl-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#scdl-history) | Reference architecture diagram first published. | May 18, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
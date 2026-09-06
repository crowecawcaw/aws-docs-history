

# Industrial DataOps on AWS using Cognite Data Fusion
<a name="industrial-dataops-cognite-data-fusion"></a>

Publication date: **November 2024 ([Diagram history](#idcdf-diagram-history))**

With this architecture, you can use AWS Cloud and [Cognite Data Fusion](https://www.cognite.com/en/product/cognite_data_fusion_industrial_dataops_platform) (CDF) to build an industrial DataOps platform. CDF contextualizes diverse industrial data sources and builds knowledge graphs for your operations. You can collect operational technology (OT), information technology (IT), and engineering technology (ET) data. This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Industrial DataOps architecture diagram
<a name="idcdf-diagram"></a>

![Reference architecture for industrial DataOps on AWS using Cognite Data Fusion.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-dataops-cognite-data-fusion/images/industrial-dataops-on-aws-using-cognite-data-fusion.png)


The following steps describe the architecture:

1. Purpose-built extractors ingest industrial data sources such as IT, OT, and engineering data. You can also use AWS IoT Greengrass (an open source IoT edge runtime) to bring data from edge gateways or programmable logic controllers (PLCs) to AWS Cloud.

1. Data from industrial historians and other devices flows through AWS IoT Greengrass into AWS IoT SiteWise. Cognite Native Extractors ingest pre-aggregated industrial data from a customer data lake in Amazon S3, [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Use Lambda and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) together to ingest data from CDF. Transform data by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) and write data back into CDF through the Cognite SDK. [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) and Amazon SageMaker AI provide additional analytics and machine learning (ML) capabilities.

1. End users create custom applications depending on data type by using AWS IoT TwinMaker and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/).

## Further reading
<a name="idcdf-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="idcdf-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#idcdf-diagram-history) | Reference architecture diagram first published. | November 1, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
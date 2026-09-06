

# Manufacturing Data Lake on AWS
<a name="manufacturing-data-lake"></a>

Publication date: **June 29, 2020 ([Diagram history](#mdl-diagram-history))**

With this architecture, you can build a manufacturing data lake that combines operational technology (OT) data from Industrial Internet of Things (IIoT) devices and factory applications with enterprise application data. You can then run manufacturing analytical use cases and predictions with machine learning (ML) models. This architecture uses [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Manufacturing data lake architecture diagram
<a name="mdl-diagram"></a>

![Reference architecture diagram for building a manufacturing data lake on AWS that combines IIoT and enterprise data for analytics and ML predictions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-data-lake/images/manufacturing-data-lake-ra.png)


The following steps describe the architecture:

1. Create the data lake structure with Lake Formation or Amazon S3 and Amazon Redshift. Store raw and processed data in Amazon S3 buckets organized by data source and processing stage.

1. For structured relational data, create an [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS) instance within an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/).

1. For compatible enterprise applications, use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) to create an interface into Amazon RDS.

1. For compatible databases, use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) to create copies or export structured data sets into the data lake.

1. For IIoT and automation equipment, use AWS IoT Core and Amazon Data Firehose to stream data into the data lake. [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) collects and organizes industrial equipment data.

1. For external or batch interfaces, use [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) to put data into the data lake.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) to build the data catalog and create extract, transform, and load (ETL) jobs.

1. Use Amazon SageMaker AI to train and deploy ML models against data in the data lake.

1. Use AWS AppSync to build a GraphQL endpoint with Lambda resolvers. This endpoint provides a flexible API for consuming applications.

1. Build visualizations with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) by using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) and Amazon Redshift.

## Further reading
<a name="mdl-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="mdl-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#mdl-diagram-history) | Reference architecture diagram first published. | June 29, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.


# Flutura Cerebra Asset Performance Management on AWS
<a name="flutura-cerebra-apm"></a>

Publication date: **November 21, 2022 ([Diagram history](#fca-diagram-history))**

With this architecture, you can ingest data from industrial equipment and build physics-based machine learning (ML) models for predictive maintenance, asset performance analysis, and process optimization. Flutura Cerebra APM uses [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) (Amazon EMR), [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

## Flutura Cerebra APM architecture diagram
<a name="fca-diagram"></a>

![Architecture diagram for Flutura Cerebra Asset Performance Management on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/flutura-cerebra-apm/images/flutura-cerebra-APM-ra.png)


The following steps describe the architecture:

1. Cerebra ingests data directly from sensors, historians, and local databases as streams or batch.

1. The extract, transform, and load (ETL) component handles large volumes with Amazon EMR running Spark jobs. Raw data splits into Kafka streams in Amazon MSK for processing.

1. Data streams from the ETL component pass through Spark jobs on Amazon EMR before storage in Amazon S3 or an [OpenTSDB](http://opentsdb.net/) time series database.

1. Lambda synchronizes different data streams with metadata stored in Amazon S3.

1. Cerebra model management facilitates registration of containerized models, version management, and retraining. It consumes Kafka streams from Amazon MSK.

1. Data streams pass through models from Cerebra Engineer's Workbench. Amazon EC2 and [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/) provide additional compute capacity.

1. Cerebra API frameworks run on Amazon EC2 with prebuilt asset-centric and process-centric use case frameworks.

1. Cerebra Digital Assistants run as browser-based applications on Amazon EC2 for operational decision-making.

1. You access data stored in OpenTSDB through secured API frameworks.

1. Cerebra provides browser-based console access through an internet gateway and Application Load Balancer.

For more information about Flutura digital twins, see [Flutura delivers scalable digital twins](https://www.flutura.com/resources/articles/flutura-delivers-scalable-digital-twins-for-industrial-oil-and-gas-use-cases) on the Flutura website.

## Further reading
<a name="fca-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="fca-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#fca-diagram-history) | Reference architecture diagram first published. | November 21, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
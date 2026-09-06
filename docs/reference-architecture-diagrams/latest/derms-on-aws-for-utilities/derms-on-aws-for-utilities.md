

# DERMS on AWS for Utilities
<a name="derms-on-aws-for-utilities"></a>

Publication date: **February 19, 2021 ([Diagram history](#derms-history))**

With this architecture, you can run DERMS on AWS to manage your growing fleet of DERs. On-premises DERMS solutions often face scalability limitations and integration challenges. This architecture scales elastically and integrates with managed ML services to improve grid reliability. The solution uses [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) for machine learning (ML), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) for streaming data, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for data lake storage.

## DERMS on AWS for Utilities diagram
<a name="derms-diagram"></a>

![Reference architecture diagram showing how to run DERMS on AWS by using SageMaker AI, Amazon Forecast, Amazon Kinesis, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/derms-on-aws-for-utilities/images/derms-on-aws-for-utilities.png)


The following steps describe the data flow and analytics pipeline for this architecture:

1. Collect streaming and batch data from various data sources, such as customer and grid data, meter data, DER measurements, market prices, and weather. Integrate with DERMS through one or more of [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html), [AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/) services, streaming, or API services.

1. Deploy vendor DERMS applications by using different compute services, such as [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), or AWS container services. Store associated transactional and operational data sets in purpose-built AWS databases based on their data structure and access patterns.

1. 3A. Control DER assets directly through IoT or APIs from the DERMS.

   3B. Make recommendations to the advanced distribution management system (ADMS) or supervisory control and data acquisition (SCADA) system. Integrate ADMS and other systems with DERMS by using application integration services such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/), [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/), or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

1. Automate extract, transform, and load (ETL) processes such as transformation and deduplication with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Use Amazon S3 as low-cost storage for raw and curated data, with archival copies for retention and compliance. Your data lake serves as the single source of truth for downstream analytics and ML work. Use AWS Glue to automate data schema discovery and metadata tagging to create a searchable metadata catalog.

1. Query petabytes of structured and semi-structured data across your data warehouse and data lake by using standard SQL with [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/). Create and publish interactive dashboards with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html). Access dashboards from any device or embed them into your applications and websites.

1. Use pre-trained AI models, such as Forecast, to detect grid anomalies, forecast energy usage, and predict equipment failures. Build, train, and deploy your own ML model with SageMaker AI.

## Further reading
<a name="derms-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="derms-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#derms-history) | Reference architecture diagram first published. | February 19, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
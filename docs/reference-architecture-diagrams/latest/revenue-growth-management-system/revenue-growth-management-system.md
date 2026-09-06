

# Revenue Growth Management System on AWS
<a name="revenue-growth-management-system"></a>

Publication date: **March 25, 2022 ([Diagram history](#rgm-history))**

With this architecture, you can build a revenue growth management (RGM) system on AWS. A strong RGM system increases revenue by delivering the right brand, pack, or brand-and-pack mix, to the right consumer, at the right price, on the right occasion. You can unlock revenue growth at the intersection of demand shaping, multi-touch attribution, and marketing mix.

## Architecture diagram
<a name="rgm-diagram"></a>

![Data flowing from on-premises and external sources through AWS integration, storage, and analytics services for revenue growth management.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/revenue-growth-management-system/images/revenue-growth-management-system-on-aws-ra.png)


The following steps describe the architecture:

1. Your on-premises systems store data in various internal formats.

1. Use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or AWS Site-to-Site VPN for connectivity. (Optional) Skip this step if your sources are already on AWS.

1. External data sources include publicly available data such as demographics, paid data such as Nielsen or IRI, online media, marketing agency data, and trading partners' point-of-sale (POS) data.

1. Internal and external sources share an integration layer built on [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/), [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/), and Amazon Kinesis Data Firehose for streaming and ingestion. Use [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) for file transfer and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for extract, transform, and load (ETL). You can use REST clients for API calls or scrape websites for data.

1. As a data analyst or engineer, you get different access to the data lakes. You can visualize and analyze data with [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), and Amazon OpenSearch Service. You can also train ML algorithms for demand shaping, sensing, and forecasting by using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/).

1. Raw and curated data from the data lakes on [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) with [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) provides the object storage layer with access control per user group. Amazon RDS stores relational data. Existing relational databases can run on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) for a lift-and-shift option.

1. Services and data on AWS are accessible from existing internal and third-party applications on corporate networks through the connectivity layer.

1. The management and reporting layer provides ad hoc reporting, monitoring, security, data protection, and other native AWS service integration. This layer uses IAM, CloudFormation, Amazon CloudWatch, and Amazon ECS.

## Further reading
<a name="rgm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="rgm-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#rgm-history) | Reference architecture diagram first published. | March 25, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
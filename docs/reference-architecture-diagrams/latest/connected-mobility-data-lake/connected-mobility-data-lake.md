

# Connected Mobility Data Lake
<a name="connected-mobility-data-lake"></a>

Publication date: **January 1, 2023 ([Diagram history](#diagram-history))**

This architecture enables you to create connected mobility data products and democratize data access with a serverless data mesh architecture.

## Connected Mobility Data Lake Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to create connected mobility data products and democratize data access with a serverless data mesh architecture](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-mobility-data-lake/images/connected-mobility-data-lake.png)


1. Ingest vehicle data through a network provider to **AWS IoT Core**. Ingest factory data through **Direct Connect** and **[Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-producers.html)**. Sync a customer relationship management (CRM) database to **Amazon Simple Storage Service** (Amazon S3) with **[AWS DataSync](https://aws.amazon.com/blogs/storage/synchronizing-your-data-to-amazon-s3-using-aws-datasync/)**.

1. Forward messages from **AWS IoT Core** based on rules and use **AWS Lambda** to process messages and ingest into **Amazon DynamoDB** and **Amazon S3**. **DynamoDB** is used for attributes and different vehicle status storage.

1. Store raw data in **Amazon S3** . 

1. An **Amazon S3** event initiates **AWS Lambda** for data processing, which initiates an **AWS Fargate** batch job for data preparation. 

1. Store datasets that you want to present as a product in an **Amazon S3** bucket. Data producers are responsible for data quality and format. 

1. Create **AWS Lake Formation Data Catalog** entities using an **AWS Glue** crawler job in a producer account. The **Data Catalog** is [replicated](https://aws.amazon.com/premiumsupport/knowledge-center/glue-data-catalog-cross-account-access/) in a central data governance account to make data discoverable.

1. Grant roles to a data producer to manage schema changes and permission data transformations (alter, delete, update) on the central **Data Catalog** when it changes at the source. Propagate automatic schema changes from a producer account.

1. Depending on data consumer requests and the need to make data [visible and accessible](https://docs.aws.amazon.com/lake-formation/latest/dg/viewing-shared-resources.html) , the data owner grants **AWS Lake Formation** permissions in the centralized account to a consumer account. These permissions are based on direct entity sharing or tag-based access controls, which can be used to administer access through controls like data classification, cost centers, or environment.

1. [Call center applications ](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/automotive-call-center-ra.pdf) can access data from various sources in different accounts to help customers.

1. Original equipment manufacturer (OEM) departments or their partners see available data and request access to create new use cases. Data queries are done using **Amazon Athena**, **Amazon SageMaker AI Data Wrangler**, or **Amazon Redshift Spectrum**. 

1. OEMs can give end user applications and businesses access to data using **Amazon API Gateway** and [monetize APIs](https://aws.amazon.com/blogs/awsmarketplace/monetize-your-custom-http-apis-via-aws-data-exchange/) . 

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 11, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
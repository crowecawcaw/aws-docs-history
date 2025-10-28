# Payor Strategic Focus Areas

Publication date: **May 22, 2024 ([Diagram history](#diagram-history "#diagram-history"))**

This set of reference architectures illustrates how payors can leverage advanced
analytics and harness structured and unstructured healthcare data to enhance
customer experiences, optimize resource allocation, and make informed decisions
across the healthcare continuum. Additionally, the solution empowers payors to
modernize and standardize healthcare data, enabling seamless integration of
core payor systems, provider data, and healthcare content repositories.

## Modernize Core Payor Functions Diagram

This reference architecture demonstrates how to connect core payor systems, standardize
payor and provider data, and create a ready-to-go repository of healthcare content. The
solution will enable healthcare companies to accelerate the digitization and modernization
of healthcare data and achieve advanced insights into healthcare data at scale.

![Reference architecture diagram showing how to connect core payor systems, standardize payor and provider data, and create a ready-to-go repository of healthcare content. The solution will enable healthcare companies to accelerate the digitization and modernization of healthcare data and achieve advanced insights into healthcare data at scale.](images/1-modernize-core-functions.png)

1. On-premises or cloud data sources are ingested in into the AWS Cloud using
   [**AWS DataSync**](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") or
   [**AWS Database Migration Service**](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
   (AWS DMS), depending on the type of source. Use **DataSync**
   for near real-time ingestion or **AWS DMS** for database migration.
   Ingestion requires secure connectivity with encryption in transit and at rest.
2. The raw data is moved into a data hub landing zone and stored in the source format
   in [**Amazon Simple Storage Service**](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") (Amazon S3).
3. [**AWS Lambda**](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
   functions can be used to run shorter
   processing jobs that use less memory for data curation and referential integrity.
   They can also be used to initiate [**AWS Glue**](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
   (Spark) jobs for data extract, transform, and load (ETL) processing.
4. Data is cleansed and curated into [**Amazon Redshift**](https://aws.amazon.com/redshift "https://aws.amazon.com/redshift") using
   standardization and data quality rules stored in a rules engine. Rules can be common
   across source data elements or plan-specific for extensibility. The atomic layer with
   all datasets should be checked for referential integrity and context applied where
   necessary. The curated and atomic levels use **Amazon Redshift** as
   the data store along with **Amazon S3** for documents storage.
5. Create business terms for data elements in the system. Link technical metadata to the
   business terms and capture and store lineage in the data catalog. An **AWS Glue crawler**
   interacts with data stores to populate **AWS Glue Data Catalog**, which
   contains reference to data that is used as source and targets for ETL jobs in **AWS Glue**.
   [**AWS Lake Formation**](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/") centralizes permissions management of your data and
   provides a single place to manage access controls and data governance across your organization.
6. Data can be stored in a data warehouse for business intelligence (BI), RDS, or key/value store
   for faster access and blob store for bulk data consumption. Purpose-built data stores store
   curated data for downstream consumption. FHIR format data can be directly ingested into
   [**AWS HealthLake**](https://aws.amazon.com/healthlake/ "https://aws.amazon.com/healthlake/");
   for relational and transaction data,
   use [**Amazon Relational Database Service**](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") (Amazon RDS); and for structured and semi-structured
   data at any large scale, use **Amazon Redshift**. For all the other datatypes,
   you can use **Amazon S3**.
7. Query structured claims data and create data products that can be consumed by care management
   to provide more efficient operational analysis and improved clinical insights. Deploy analytical
   models, standard reports, and dashboards to visualize and study performance.
   [**Amazon Athena**](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") can help
   you with direct queries analysis, data preparation for machine learning, and data
   reconciliation. Create visualization dashboards using [**Amazon Quick Suite**](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"),
   then use [**Amazon SageMaker AI**](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to
   build, train, and deploy machine learning models on the available data and integrate with
   custom application. End users include businesses, researchers, data scientists, and technical users.
8. Data security, compliance, and governance is handled at the solution level by a set of purpose
   built-services. [**AWS Identity and Access Management**](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM)
   provides security propagation across services and data is encrypted through
   [**AWS Key Management Service**](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") (AWS KMS).
   [**Amazon CloudWatch**](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") helps
   you monitor your solution's metrics, logs, and alarms.
   [**AWS CloudTrail**](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") helps
   to monitor access to AWS endpoints. For more security and monitoring options, see the
   [AWS Security Decision Guide](https://aws.amazon.com/getting-started/decision-guides/security-on-aws-how-to-choose/ "https://aws.amazon.com/getting-started/decision-guides/security-on-aws-how-to-choose/").

## Advanced Analytics to Drive Business Value Diagram

This reference architecture enables access and delivery of person-centered care, drives improved outcomes
at a lower cost, and accelerates the digitization and utilization of healthcare data. The solution is
designed to help you harness complex structured and un-structured data on multiple determinants of
health to inform clinical and community intervention.

![Reference architecture diagram showing access and delivery of person-centered care, drives improved outcomes at a lower cost, and accelerates the digitization and utilization of healthcare data. The solution is designed to help you harness complex structured and un-structured data on multiple determinants of health to inform clinical and community intervention.](images/2-advanced-analytics.png)

1. On-premises or cloud data sources are ingested in into AWS. Ingested data can be from any of
   the following data sources: clinical, claims, provider, and electronic medical records (EMR).
   Specific connectors will ingest different data types, such as HL7v2, FHIR, CCDA, X12, or
   semi-structured. Clinical large language models (LLMs) can be trained to convert data into
   FHIR for ingestion purposes. Data ingestion requires secure connectivity ensuring encryption
   at rest and in transit. Data ingestion can be streaming, near real time, or batch.
2. Data enrichment pipelines transform and normalize ingested data into a common data
   model. Syntactic parser and semantic harmonization components can be implemented using
   AWS services like [**Amazon Comprehend Medical**](https://aws.amazon.com/comprehend/medical/ "https://aws.amazon.com/comprehend/medical/"),
   [**Amazon Textract**](https://aws.amazon.com/textract/ "https://aws.amazon.com/textract/"),
   and **AWS Lambda**. LLMs from
   [**Amazon Bedrock**](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
   can be leveraged for data enrichment. This step ensures the data that is ingested into **AWS HealthLake**
   is in FHIR R4 format.

Alternatively, AWS Partner solutions are available to implement data ingestion. For more details, refer to [AWS
HealthLake Partners](https://aws.amazon.com/healthlake/partners/ "https://aws.amazon.com/healthlake/partners/"). You can bring your own identity and terminology services to assist
with data harmonization (Employee Master Patient Index or EMPI). 3. Purpose-built data stores will hydrate **AWS HealthLake** using common data
models. You can also store data in graph databases like
[**Amazon Neptune**](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"), NoSQL databases
like [**Amazon DynamoDB**](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"), or data lakes like **Amazon Simple Storage Service** (Amazon S3). 4. Providers have access to patient population data in **AWS HealthLake** and generate
business insights through **Amazon Athena** and **Amazon Redshift**.
**Amazon SageMaker AI** can provide machine learning insights. **Amazon Bedrock**
helps leverage LLMs to translate English queries into SQL FHIR queries.
[**Amazon DataZone**](https://aws.amazon.com/datazone/ "https://aws.amazon.com/datazone/") can be
leveraged to create data products and make them available in a catalog. 5. Create dashboards using **Amazon Quick Suite** (with [**Amazon Q**](https://aws.amazon.com/q/ "https://aws.amazon.com/q/") integration)
and enhanced applications like longitudinal patient view through [**AWS Amplify**](https://aws.amazon.com/amplify/ "https://aws.amazon.com/amplify/").

## Improve the Customer Experience Diagram

This reference architecture enables omni-channel engagement for customers. It provides a responsive,
engaging, and personalized experience by combining data from care, disease, and utilization
management systems and clinician contact centers to help agents make informed customer decisions.

![Reference architecture diagram showing omni-channel engagement for customers. It provides a responsive, engaging, and personalized experience by combining data from care, disease, and utilization management systems and clinician contact centers to help agents make informed customer decisions.](images/3-improved-customer-experience.png)

1. Callers dial through the main line or other channels and interact with the
   call center application. Data ingestion requires secure connectivity ensuring encryption
   at rest and in transit. Data can be streamed, near real-time for calls, or batch for offline communications.
2. [**Amazon Connect**](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/") routes calls while leveraging
   [**Amazon Lex**](https://aws.amazon.com/lex/ "https://aws.amazon.com/lex/")
   for conversation and **AWS Amplify** for agent applications.
   [**Amazon Cognito**](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") provides security while
   [**Amazon API Gateway**](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
   provides API-based access for call log analysis.
3. Call logs are sent to **AWS Lambda**, which leverages
   [**Amazon Data Firehose**](https://aws.amazon.com/firehose/ "https://aws.amazon.com/firehose/")
   to ingest them into **Amazon Simple Storage Service** (Amazon S3). **Amazon SageMaker AI** analyzes the
   stored logs and determines next steps. [**AWS Identity and Access Management**](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) provides security propagation
   across services and data is encrypted through [**AWS Key Management Service**](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") (AWS KMS).
   **Amazon CloudWatch** provides logging capabilities for data pipelines while **AWS CloudTrail**
   helps track API calls.
4. Purpose-built AWS services connect to care management systems to get member information and
   [**Amazon Pinpoint**](https://aws.amazon.com/pinpoint/ "https://aws.amazon.com/pinpoint/")
   connects with customers through scalable, targeted, multi-channel communications.
5. Member and provider profiles are enriched in real time from **AWS HealthLake** and Amazon S3 data lakes and
   passed to a care management system to decide the next best action and react to member calls.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/healthcare-payor-strategic-focus-areas.md "samples/healthcare-payor-strategic-focus-areas.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | May 22, 2024 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |

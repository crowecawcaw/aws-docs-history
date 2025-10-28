# Configuration notes

- To organize data for efficient access and easy management:
  - The storage layer can store data in different states of consumption readiness,
    including raw, trusted, conformed, enriched, and modeled. It’s important to segment
    your data lake into landing, raw, trusted, and curated zones to store data depending
    on its consumption readiness. Typically, data is ingested and stored as is in the data
    lake (without having to first define schema) to accelerate ingestion and reduce time
    needed for preparation before data can be explored.
  - Partition data with keys that align to common query criteria.
  - Convert data to an open columnar file format, and apply compression. This will
    lower storage usage, and increase query performance.

- Choose the proper storage tier based on data temperature. Establish a data lifecycle
  policy to delete old data automatically to meet your data retention requirements.
- Decide on a location for data lake ingestion, for example, an S3 bucket. Select a
  frequency and isolation mechanism that meet your business needs.
- Depending on your ingestion frequency and data mutation rate, schedule file
  compaction to maintain optimal performance.
- Use AWS Glue crawlers to discover new datasets, track lineage, and avoid a data
  swamp.
- Manage access control and security using AWS Lake Formation, IAM role setting, AWS KMS, and
  AWS CloudTrail.
- There is no need to move data between a data lake and the data warehouse for the data
  warehouse to access it. Amazon Redshift Spectrum can directly access the dataset in the data lake.
- For more details, refer to the [Derive Insights from AWS Modern Data](../../../whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.md "../../../whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.md") whitepaper.

 

## User personas

To get the full value from your modern data architecture, there are various personas
who will access the data and perform data analytics. For example, the chief data officer
(CDO) of an organization is responsible for driving digital innovation and transformation
across lines of business. This CDO should set a data-driven vision for the organization and
be a champion of using data, analytics, and AI/ML to inform business decisions.

Table 4: Key personas for a modern data architecture

|                          |                                                                                                                                                     |                                                                                                                                                                                    |                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Personas**             | **Responsibility**                                                                                                                                  | **Areas of interest**                                                                                                                                                              | **Modern data architecture purpose-built AWS services**                                         |
| Chief data officer (CDO) | Build a culture of using data to solve problems and accelerate innovation.                                                                          | Data quality, data governance, data and AI strategy, evangelize the value of data to the business.                                                                                 | AWS Lake Formation, Amazon OpenSearch Service                                                   |
| Data architect           | Driven to architect technical solutions to meet business needs. Focuses on solving complex data challenges to help the CDO deliver on their vision. | Data pipeline, data processing, data integration, data governance, and data catalogs.                                                                                              | AWS Glue, Amazon EMR, Amazon Redshift, Amazon Athena, Amazon OpenSearch Service                 |
| Data engineer            | Deliver usable, accurate dataset to organization in a secure and performant manner.                                                                 | Variety of tools to build data pipeline, ease of use, configuration, and maintenance.                                                                                              | AWS Glue, Amazon EMR, Amazon Kinesis, Amazon Redshift, Amazon Athena, Amazon OpenSearch Service |
| Data security officer    | Data security, privacy, and governance must be strictly defined and adhered to.                                                                     | Keeping information secure. Comply with data privacy regulations and protecting personally identifiable information (PII), applying fine-grained access controls and data masking. | AWS Lake Formation, AWS Identity and Access Management (IAM).                                   |
| Data scientist           | Construct the means for extracting business-focused insight from data quickly for the business to make better decision.                             | Tools that simplify data manipulation, and provide deeper insight than visualization tools. Tools that help build the ML pipeline.                                                 | Amazon SageMaker AI, Amazon Athena, Quick Suite, AWS Glue Studio, AWS Glue DataBrew             |
| Data analyst             | React to market conditions in real time, must have the ability to find data and perform analytics quickly and easily.                               | Querying data and performing analysis to create new business insights, producing reports and visualizations that explain the business insights.                                    | Amazon Athena, Quick Suite, AWS Glue Studio, Amazon Redshift                                    |

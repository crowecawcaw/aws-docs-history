

# Insurance lake
<a name="insurance-lake"></a>

 The insurance data lake provides a method for aggregating end user customer data from a large number of diverse sources, including core systems and third parties, and consolidating it within a single, secure location. The four Cs provide a best practice data lake pattern for creation of your insurance data lake: 

1.  **Collect:** Store all of your data in Amazon S3. 

1.  **Cleanse and curate:** Validate, map, transform, and log the actions performed on your data. 

1.  **Consume:** Derive insights from your data. 

1.  **Comply and secure:** Automate your audit and regulatory compliance requirements and secure your data. 

 **Reference architecture** 

![Insurance lake reference architecture diagram](http://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/images/insurance-lake-reference-architecture.png)


 **Architecture description** 

1. Source data file is dropped into the Collect S3 bucket. Mapping file, transform file, and data quality file are present in the ETL-Scripts S3 bucket .

1. Put Event automatically initiates a Lambda function that reads metadata from the incoming source data, logs all actions, handles any errors, and starts the AWS Step Functions workflow.

1. Step Functions calls PySpark AWS Glue jobs that map the data to your pre-defined data dictionary and perform the transformations and data quality checks for both the Cleanse and Consume layers.

1. Amazon DynamoDB contains lookup values for each source data file as needed by the `lookup` and `multilookup` transforms. ETL metadata, such as job audit logs, data lineage output logs, and data quality results, are written here.

1. Cleansed and curated data is then written to compressed, partitioned Apache Parquet files in the PySpark code. The PySpark code also creates and updates AWS Glue Data Catalog databases and tables defined by your data dictionary.

1. Source data file validation failures are sent to an S3 Quarantine folder and Data Catalog table, which can populate an exception queue dashboard where a human can review and take appropriate action.

1.  SQL queries can be written using the AWS Glue databases and tables. 

1.  Quick dashboards and reports can pull data from the insurance lake on a real-time or scheduled basis. 

1.  Full DevSecOps (everything as code and everything as automated as possible) can be managed using AWS CodePipeline and related services. 
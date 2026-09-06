

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Create a zero-ETL integration
<a name="zero-etl-setting-up.create-integration"></a>

First, you create a zero-ETL integration to replicate your source data to Amazon Redshift.

The source of your data determines which type of zero-ETL integration to create.

**Topics**
+ [Create a zero-ETL integration for Aurora](zero-etl-setting-up.create-integration-aurora.md)
+ [Create a zero-ETL integration for Amazon RDS](zero-etl-setting-up.create-integration-rds.md)
+ [Create a zero-ETL integration for DynamoDB](zero-etl-setting-up.create-integration-ddb.md)
+ [Create a zero-ETL integration with applications](zero-etl-setting-up.create-integration-glue.md)
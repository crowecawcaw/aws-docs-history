

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Create a zero-ETL integration with applications
<a name="zero-etl-setting-up.create-integration-glue"></a>

In this step, you create a zero-ETL integration with applications with Amazon Redshift.

**To create a zero-ETL integration with applications with Amazon Redshift**

1. From the Amazon Redshift console: [Create and configure a target Amazon Redshift data warehouse](zero-etl-setting-up.rs-data-warehouse.md). 
   + From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your data warehouse](zero-etl-setting-up.case-sensitivity.md).
   + From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data warehouse](zero-etl-using.redshift-iam.md).

1. From the AWS Glue console: [Creating an integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-common-integration-tasks.html#zero-etl-creating) as described in the *AWS Glue Developer Guide*.

1. After the destination database has been created and data starts replicating, you can query and create materialized data for your replicated data. For more information, see [Querying replicated data in Amazon Redshift](zero-etl-using.querying-and-creating-materialized-views.md).

For detailed information to create zero-ETL integrations with applications, see [Zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html) in the *AWS Glue Developer Guide*.
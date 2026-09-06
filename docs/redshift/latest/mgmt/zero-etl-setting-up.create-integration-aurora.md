

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Create a zero-ETL integration for Aurora
<a name="zero-etl-setting-up.create-integration-aurora"></a>

In this step, you create an Aurora zero-ETL integration with Amazon Redshift.

**To create an Aurora zero-ETL integration with Amazon Redshift**

1. From the Amazon RDS console, [create a custom DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.html#zero-etl.parameters) as described in the *Amazon Aurora User Guide*.

1. From the Amazon RDS console, [create a source Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.html#zero-etl.create-cluster) as described in the *Amazon Aurora User Guide*.

1. From the Amazon Redshift console: [Create and configure a target Amazon Redshift data warehouse](zero-etl-setting-up.rs-data-warehouse.md). 
   + From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your data warehouse](zero-etl-setting-up.case-sensitivity.md).
   + From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data warehouse](zero-etl-using.redshift-iam.md).

1. From the Amazon RDS console, [create a zero-ETL integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.html#zero-etl.create) as described in the *Amazon Aurora User Guide*.

1. From the Amazon Redshift console or the query editor v2, [create an Amazon Redshift database from your integration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html).

   Then, [query and create materialized views with replicated data](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.querying-and-creating-materialized-views.html).

For detailed information to create Aurora zero-ETL integrations, see [Creating Amazon Aurora zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.html) in the *Amazon Aurora User Guide*.
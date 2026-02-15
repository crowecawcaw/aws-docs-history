Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a zero-ETL integration for

Aurora

In this step, you create an Aurora zero-ETL integration with Amazon Redshift.

###### To create an Aurora zero-ETL integration with Amazon Redshift

1. From the Amazon RDS console, [create a custom DB cluster parameter group](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters") as described in the
   _Amazon Aurora User Guide_.
2. From the Amazon RDS console, [create a source Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.create-cluster "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.create-cluster") as described in the
   _Amazon Aurora User Guide_.
3. From the Amazon Redshift console: [Create and configure a target
   Amazon Redshift data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your
     data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data
     warehouse](zero-etl-using.md "zero-etl-using.md").

4. From the Amazon RDS console, [create
   a zero-ETL integration](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.create "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.create") as described in the
   _Amazon Aurora User Guide_.
5. From the Amazon Redshift console or the query editor v2, [create an Amazon Redshift database
   from your integration](zero-etl-using.md "zero-etl-using.md").

Then, [query and create materialized views with replicated data](zero-etl-using.md "zero-etl-using.md").
For detailed information to create Aurora zero-ETL integrations, see [Creating Amazon Aurora
zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") in the _Amazon Aurora User Guide_.

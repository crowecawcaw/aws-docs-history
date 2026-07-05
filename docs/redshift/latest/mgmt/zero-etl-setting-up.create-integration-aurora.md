Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Create a zero-ETL integration for Aurora

In this step, you create an Aurora zero-ETL integration with Amazon Redshift.

###### To create an Aurora zero-ETL integration with Amazon Redshift

1. From the Amazon RDS console, [create a custom DB cluster parameter group](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.md#zero-etl.parameters "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.md#zero-etl.parameters") as described in the
   _Amazon Aurora User Guide_.
2. From the Amazon RDS console, [create a source Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.md#zero-etl.create-cluster "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.md#zero-etl.create-cluster") as described in the
   _Amazon Aurora User Guide_.
3. From the Amazon Redshift console: [Create and configure a target Amazon Redshift data warehouse](zero-etl-setting-up.rs-data-warehouse.md "zero-etl-setting-up.rs-data-warehouse.md").

   - From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your data warehouse](zero-etl-setting-up.case-sensitivity.md "zero-etl-setting-up.case-sensitivity.md").
   - From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data warehouse](zero-etl-using.redshift-iam.md "zero-etl-using.redshift-iam.md").

4. From the Amazon RDS console, [create
   a zero-ETL integration](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.md#zero-etl.create "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.md#zero-etl.create") as described in the
   _Amazon Aurora User Guide_.
5. From the Amazon Redshift console or the query editor v2, [create an Amazon Redshift database
   from your integration](zero-etl-using.creating-db.md "zero-etl-using.creating-db.md").

Then, [query and create materialized views with replicated data](zero-etl-using.querying-and-creating-materialized-views.md "zero-etl-using.querying-and-creating-materialized-views.md").
For detailed information to create Aurora zero-ETL integrations, see [Creating Amazon Aurora
zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.md") in the _Amazon Aurora User Guide_.

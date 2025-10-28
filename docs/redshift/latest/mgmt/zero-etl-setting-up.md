Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a zero-ETL integration with

applications

In this step, you create a zero-ETL integration with applications with Amazon Redshift.

###### To create a zero-ETL integration with applications with Amazon Redshift

1. From the Amazon Redshift console: [Create and configure a target
   Amazon Redshift data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the AWS CLI or Amazon Redshift console: [Turn on case sensitivity for your
     data warehouse](zero-etl-setting-up.md "zero-etl-setting-up.md").
   - From the Amazon Redshift console: [Configure authorization for your Amazon Redshift data
     warehouse](zero-etl-using.md "zero-etl-using.md").

2. From the AWS Glue console: [Creating an integration](../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-creating "../../../glue/latest/dg/zero-etl-common-integration-tasks.md#zero-etl-creating") as described in the
   _AWS Glue Developer Guide_.
3. After the destination database has been created and data starts replicating, you
   can query and create materialized data for your replicated data.
   For more
   information, see [Querying replicated
   data in Amazon Redshift](zero-etl-using.md "zero-etl-using.md").
   For detailed information to create zero-ETL integrations with applications, see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the
   _AWS Glue Developer Guide_.

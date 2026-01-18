Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Zero-ETL integrations

Zero-ETL integration is a fully managed solution that makes transactional and operational data
available in Amazon Redshift from multiple operational and transactional sources. With this solution,
you can configure an integration from your source to an Amazon Redshift data warehouse. You don't need to
maintain an extract, transform, and load (ETL) pipeline. We take care of the ETL for you by
automating the creation and management of data replication from the data source to the Amazon Redshift
cluster or Redshift Serverless namespace. You can continue to update and query your source data while
simultaneously using Amazon Redshift for analytic workloads, such as reporting and dashboards.

With zero-ETL integration you have fresher data for analytics, AI/ML, and reporting. You get more
accurate and timely insights for use cases like business dashboards, optimized gaming
experience, data quality monitoring, and customer behavior analysis. You can make data-driven
predictions with more confidence, improve customer experiences, and promote data-driven insights
across the business.

The following sources are currently supported for zero-ETL integrations:

- Amazon Aurora MySQL (AMS)
- Amazon Aurora PostgreSQL (APG)
- Amazon DynamoDB
- Amazon RDS for MySQL
- Amazon RDS for Oracle
- Amazon RDS for PostgreSQL
- Oracle Database@AWS
- Applications including Salesforce, Salesforce Marketing Cloud Account Engagement, SAP, ServiceNow, Instagram ads, Meta ads, and Zendesk
- Self-Managed MySQL, PostgreSQL, SQL Server, and Oracle
  To create a zero-ETL integration, you specify an integration source and an Amazon Redshift data warehouse as
  the target. After an initial data load, the integration replicates data from the source to the
  target data warehouse. The data becomes available in Amazon Redshift. You control the encryption of
  your data when you create the integration source, when you create the zero-ETL integration, and when you
  create the Amazon Redshift data warehouse. The integration monitors the health of the data pipeline and
  recovers from issues when possible. You can create integrations from sources of the same type
  into a single Amazon Redshift data warehouse to derive holistic insights across multiple
  applications.

With the data in Amazon Redshift, you can use analytics that Amazon Redshift provides. For example, built-in
machine learning (ML), materialized views, data sharing, and direct access to multiple data
stores and data lakes.
For data engineers,
zero-ETL integration provides access to time-sensitive data that otherwise can get delayed by intermittent
errors in complex data pipelines. You can run analytical queries and ML models on transactional
data to derive timely insights for time-sensitive events and business decisions.

You can create an Amazon Redshift event notification subscription so you can be notified when an event
occurs for a given zero-ETL integration. To view the list of integration-related event notifications, see
[Zero-ETL integration event notifications with
Amazon EventBridge](integration-event-notifications.md "integration-event-notifications.md"). The simplest way to create a subscription
is with the Amazon SNS console. For information on creating an Amazon SNS topic and subscribing to it, see
[Getting started with
Amazon SNS](../../../sns/latest/dg/GettingStarted.md "../../../sns/latest/dg/GettingStarted.md") in the _Amazon Simple Notification Service Developer Guide_.

As you get started with zero-ETL integrations, consider the following concepts:

- A source database is the database from where data is replicated into Amazon Redshift.
- A target data warehouse is the Amazon Redshift provisioned cluster or Redshift Serverless workgroup where data is
  replicated to.
- A destination database is the database that you create from a zero-ETL integration in the target
  data warehouse.
  For information about system tables and views you can use to monitor your zero-ETL integrations, see
  [Monitoring zero-ETL integrations with Amazon Redshift system
  views](zero-etl-monitoring.md#zero-etl-monitoring-sysviews "zero-etl-monitoring.md#zero-etl-monitoring-sysviews").

For a list of AWS Regions that each source for zero-ETL integrations supports, see [Supported Regions for
zero-ETL integrations](zero-etl-using.md "zero-etl-using.md").

For pricing information for zero-ETL integrations, see the appropriate pricing page:

- [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/")
- [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/")
- [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/")
- [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/")
- [AWS Glue pricing](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")
  For more information about zero-ETL integration sources, see the following topics:

- For Aurora zero-ETL integrations, see [Benefits](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.benefits "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.benefits"),
  [Key
  concepts](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.concepts "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.concepts"), [Limitations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.reqs-lims "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.reqs-lims"), [Quotas](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.quotas "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.quotas"), and
  [Supported
  Regions](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.regions "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.regions") of zero-ETL integrations in the _Amazon Aurora User Guide_.
- For RDS zero-ETL integrations, see [Benefits](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.benefits "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.benefits"), [Key
  concepts](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.concepts "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.concepts"), [Limitations](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.reqs-lims "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.reqs-lims"),
  [Quotas](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.quotas "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.quotas"), and [Supported Regions](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.regions "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.regions")
  of zero-ETL integrations in the _Amazon RDS User Guide_.
- For DynamoDB zero-ETL integrations, see [DynamoDB
  zero-ETL integration with Amazon Redshift](../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md "../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md") in the _Amazon DynamoDB Developer Guide_.
- For zero-ETL integrations with applicatons, see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the
  _AWS Glue Developer Guide_.

###### Topics

- [Considerations when using zero-ETL integrations with Amazon Redshift](zero-etl.md "zero-etl.md")
- [Getting started with zero-ETL integrations](zero-etl-using.md "zero-etl-using.md")
- [Creating destination databases in
  Amazon Redshift](zero-etl-using.md "zero-etl-using.md")
- [Querying replicated
  data in Amazon Redshift](zero-etl-using.md "zero-etl-using.md")
- [Viewing zero-ETL integrations](zero-etl-using.md "zero-etl-using.md")
- [History mode](zero-etl-history-mode.md "zero-etl-history-mode.md")
- [Sharing your data in Amazon Redshift](zero-etl-using.md "zero-etl-using.md")
- [Monitoring zero-ETL integrations](zero-etl-monitoring.md "zero-etl-monitoring.md")
- [Metrics for zero-ETL integrations](zero-etl-using.md "zero-etl-using.md")
- [Modify a zero-ETL integration for
  DynamoDB](zero-etl-managing.md "zero-etl-managing.md")
- [Delete a zero-ETL integration for
  DynamoDB](zero-etl-managing.md "zero-etl-managing.md")
- [Supported Regions for
  zero-ETL integrations](zero-etl-using.md "zero-etl-using.md")
- [Troubleshooting zero-ETL integrations](zero-etl-using.md "zero-etl-using.md")

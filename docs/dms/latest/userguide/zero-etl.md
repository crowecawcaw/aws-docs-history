# AWS zero-ETL integration for self-managed database sources

AWS zero-ETL integration is a fully managed solution that makes transactional and operational
data available in Amazon Redshift, Amazon S3, and Amazon S3 Tables from multiple operational and transactional database sources.
Using zero-ETL, you can replicate data from your self-managed source databases such as MySQL, PostgreSQL,
SQL Server, and Oracle to Amazon Redshift through existing AWS Database Migration Service (AWS DMS) source endpoints. The automatic
synchronization avoids the traditional extract, transform, and load (ETL) process. It also enables
real-time analytics and AI workloads. For more information, see
[zero-ETL integrations](../../../redshift/latest/mgmt/zero-etl-using.md "../../../redshift/latest/mgmt/zero-etl-using.md")
in the _Amazon Redshift Management Guide_.

Zero-ETL integration provides the following benefits:

- **Real-time data replication** – Continuous data
  synchronization from Oracle databases to Amazon Redshift with minimal latency.
- **Elimination of complex ETL pipelines** – No need
  to build and maintain custom data integration solutions.
- **Reduced operational overhead** – Automated setup
  and management through AWS APIs.
- **Simplified data integration architecture** – Seamless
  integration between self-managed databases and AWS analytics services.
- **Enhanced security** – Built-in encryption and
  IAM access controls.

## How zero-ETL integration works for self-managed database sources

You can use existing AWS DMS endpoints previously created for self-managed databases or create new ones.

- Use the AWS Glue console or
  [CLI](../../../glue/latest/dg/aws-glue-api-integrations.md "../../../glue/latest/dg/aws-glue-api-integrations.md")
  to create the zero-ETL integration with Amazon Redshift as a target
  in the AWS Glue catalog. You can specify schema and table filter when creating zero-ETL integrations.
- Additional read-only resources related to the integrations are automatically created within
  the AWS DMS service. These resources including the zero-ETL engine are used to initiate full load and
  continuous data change processes, to sync up data with the Amazon Redshift target database.
- You control the encryption of your data when you create the integration source, when you
  create the zero-ETL integration, and when you create the Amazon Redshift data warehouse.
- The integration monitors the health of the data pipeline and recovers from issues
  when possible.
- You can create integrations from sources of the same type into a single Amazon Redshift data warehouse
  to derive holistic insights across multiple applications.

Once the data is replicated you can use the analytics capabilities of Amazon Redshift. For example, built-in
machine learning (ML), materialized views, data sharing, and direct access to multiple data stores and
data lakes. For data engineers, zero-ETL integrations provide access to time-sensitive data that otherwise
can get delayed by intermittent errors in complex data pipelines. You can run analytical queries and ML
models on transactional data to derive timely insights for time-sensitive events and business decisions.

You can create an Amazon Redshift event notification subscriptions to be automatically notified when issues occur
for any zero-ETL integration. To view the list of integration-related event notifications, see
[Zero-ETL integration event notifications with Amazon EventBridge](../../../redshift/latest/mgmt/integration-event-notifications.md "../../../redshift/latest/mgmt/integration-event-notifications.md").
The simplest way to create a subscription is with the Amazon Simple Notification Service console. For information on creating an
Amazon SNS topic and subscribing to it, see
[Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md")
in the _Amazon Simple Notification Service Developer Guide_.

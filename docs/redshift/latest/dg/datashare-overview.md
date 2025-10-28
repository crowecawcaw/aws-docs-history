Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data sharing in Amazon Redshift

With Amazon Redshift, you can securely share data across Amazon Redshift clusters or with other AWS services.
Data sharing lets you share live data, without having to create a copy or move it. Database
administrators and data engineers can use data sharing to provide secure, read-only access to
data for analytics purposes, while maintaining control over the data. Data analysts, business
intelligence professionals, and data scientists can leverage shared data to gain insights
without duplicating or moving data. Common use cases include sharing data with partners,
enabling cross-functional analysis, and facilitating data democratization within an
organization. The following sections cover the details of configuring and managing data
sharing in Amazon Redshift.

With Amazon Redshift _data sharing_, you can securely share
access to live data across Amazon Redshift clusters, workgroups, AWS accounts, and AWS Regions
without manually moving or copying the data. Since the data is live, all users can see the
most up-to-date and consistent information in Amazon Redshift as soon as it’s updated.

You can share data across provisioned clusters, serverless workgroups, Availability Zones,
AWS accounts, and AWS Regions. You can share between cluster types as well as between
provisioned clusters and serverless.

You can share database objects for both reads and writes across different Amazon Redshift clusters or
Amazon Redshift Serverless workgroups within the same AWS account, or from one AWS account to
another. You can read and write data across Regions as well. You can grant permissions such as
SELECT, INSERT, and UPDATE for different tables and USAGE and CREATE for different schemas.
The data is live and available to all warehouses as soon as a write transaction is
committed.

## Data sharing use cases for Amazon Redshift

Amazon Redshift data sharing is especially useful for these use cases:

- **Supporting different kinds of business-critical
  workloads** – Use a central extract, transform, and load (ETL)
  cluster that shares data with multiple business intelligence (BI) or analytic
  clusters. This approach provides read workload isolation and chargeback for
  individual workloads. You can size and scale your individual workload compute
  according to the workload-specific requirements of price and performance.
- **Enabling cross-group collaboration** –
  Enable seamless collaboration across teams and business groups for broader analytics,
  data science, and cross-product impact analysis.
- **Delivering data as a service** – Share data
  as a service across your organization.
- **Sharing data between environments** – Share
  data among development, test, and production environments. You can improve team
  agility by sharing data at different levels of granularity.
- **Licensing access to data in Amazon Redshift** –
  List Amazon Redshift data sets in the AWS Data Exchange catalog that customers can find, subscribe to,
  and query in minutes.

### Data sharing write-access use

cases

Data sharing for writes has several important use cases:

- **Update business source data on the producer**
  – You can share data as a service across your organization, but then
  consumers can also perform actions on the source data. For instance, they can
  communicate back up-to-date values or acknowledge receipt of data. These are just
  a couple possible business use cases.
- **Insert additional records on the producer**
  – Consumers can add records to the original source data. These can be
  marked as from the consumer, if needed.

For information specifically regarding how to perform write operations on a
datashare, see [Sharing
write access to data](getting-started-datashare-writes.md "getting-started-datashare-writes.md").

## Data sharing at different levels in Amazon Redshift

With Amazon Redshift, you can share data at different levels. These levels include databases,
schemas, tables, views (including regular, late-binding, and materialized views), and SQL
user-defined functions (UDFs). You can create multiple datashares for a given database. A
datashare can contain objects from multiple schemas in the database on which sharing is
created.

By having this flexibility in sharing data, you get fine-grained access control. You can
tailor this control for different users and businesses that need access to Amazon Redshift
data.

## Consistency management for data sharing in

Amazon Redshift

Amazon Redshift provides transactional consistency on all producer and consumer clusters and
shares up-to-date and consistent views of the data with all consumers.

You can continuously update data on the producer cluster. All queries on a consumer
cluster within a transaction read the same state of the shared data. Amazon Redshift doesn't
consider the data that was changed by another transaction on the producer cluster that was
committed after the beginning of the transaction on the consumer cluster. After the data
change is committed on the producer cluster, new transactions on the consumer cluster can
immediately query the updated data.

The strong consistency removes the risks of lower-fidelity business reports that might
contain invalid results during sharing of data. This factor is especially important for
financial analysis or where the results might be used to prepare datasets that are used to
train machine learning models.

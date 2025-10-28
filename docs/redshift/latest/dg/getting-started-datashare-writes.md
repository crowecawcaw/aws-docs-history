Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with multi-warehouse

writes using data sharing in Amazon Redshift

You can share database objects for both reads and writes across different Amazon Redshift
clusters or Amazon Redshift Serverless workgroups within the same AWS account, across accounts,
and across regions. The procedures in this topic show how to set up data sharing that
includes write permissions. You can grant permissions such as SELECT, INSERT, and UPDATE
for different tables and USAGE and CREATE for schemas.

Data is live and available to all warehouses as soon as you commit a write
transaction Producer account administrators can determine whether or not specific
namespaces or regions get read-only, read-and-write, or any access to the data. The
procedures assume you're working in a database in a provisioned cluster or
Amazon Redshift Serverless workgroup.

With Amazon Redshift, you can manage data sharing with writes using the console or the SQL
interface to control access and govern data across Amazon Redshift clusters and AWS accounts. The
following sections provide step-by-step instructions on configuring and managing data
sharing with writes using Amazon Redshift.

For a list of Regions where data sharing is available, see [AWS Regions where data sharing is
available](data_sharing_regions.md "data_sharing_regions.md"). For
considerations and limitations for writes, see [Considerations for data sharing in
Amazon Redshift](datashare-considerations.md "datashare-considerations.md").

###### Note

Amazon Redshift multi-warehouse writes using data sharing is only supported on Amazon Redshift
patch 186 for provisioned clusters on current track version 1.0.78881 or greater, and
for Amazon Redshift Serverless workgroups on version 1.0.78890 or greater.

###### Topics

- [Connecting to a database in
  Amazon Redshift](connect-database-console-writes.md "connect-database-console-writes.md")
- [Producer actions for new datashares in
  Amazon Redshift](writes-producer-new.md "writes-producer-new.md")
- [Consumer actions for new datashares in
  Amazon Redshift](writes-consumer-new.md "writes-consumer-new.md")
- [Producer actions for existing datashares
  in Amazon Redshift](writes-producer-existing.md "writes-producer-existing.md")
- [Consumer actions for existing datashares
  in Amazon Redshift](writes-consumer-existing.md "writes-consumer-existing.md")

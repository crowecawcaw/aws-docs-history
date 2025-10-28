# Customizing crawler behavior

When you configure an AWS Glue crawler, you have several options for defining the behavior of your crawler.

- **Incremental crawls** – You can configure a
  crawler to run incremental crawls to add only new partitions to the table schema.
- **Partition indexes** – A crawler creates partition
  indexes for Amazon S3 and Delta Lake targets by default to provide efficient lookup for specific
  partitions.
- **Accelerate crawl time by using Amazon S3 events** –
  You can configure a crawler to use Amazon S3 events to identify the changes between two crawls by
  listing all the files from the subfolder which triggered the event instead of listing the
  full Amazon S3 or Data Catalog target.
- **Handling schema changes** – You can prevent a crawlers
  from making any schema changes to the existing schema. You can use the AWS Management Console or the
  AWS Glue API to configure how your crawler processes certain types of changes.
- **A single schema for multiple Amazon S3 paths** – You
  can configure a crawler to create a single schema for each S3 path if the data is
  compatible.
- **Table location and partitioning levels** – The table
  level crawler option provides you the flexibility to tell the crawler where the tables are
  located, and how you want partitions created.
- **Table threshold** – You can specify the maximum number of
  tables the crawler is allowed to create by specifying a table threshold.
- **AWS Lake Formation credentials** – You can configure a crawler to
  use Lake Formation credentials to access an Amazon S3 data store or a Data Catalog table with an underlying Amazon S3
  location within the same AWS account or another AWS account.
  For more information about using the AWS Glue console
  to add a crawler, see [Configuring a crawler](define-crawler.md "define-crawler.md").

###### Topics

- [Scheduling incremental crawls for adding new partitions](incremental-crawls.md "incremental-crawls.md")
- [Generating partition indexes](crawler-configure-partition-indexes.md "crawler-configure-partition-indexes.md")
- [Preventing a crawler from changing an existing schema](crawler-schema-changes-prevent.md "crawler-schema-changes-prevent.md")
- [Creating a single schema for each Amazon S3 include
  path](crawler-grouping-policy.md "crawler-grouping-policy.md")
- [Specifying the table location and partitioning
  level](crawler-table-level.md "crawler-table-level.md")
- [Specifying the maximum number of tables the crawler is allowed to create](crawler-maximum-number-of-tables.md "crawler-maximum-number-of-tables.md")
- [Configuring a crawler to use Lake Formation credentials](crawler-lf-integ.md "crawler-lf-integ.md")
- [Accelerating crawls using Amazon S3 event notifications](crawler-s3-event-notifications.md "crawler-s3-event-notifications.md")

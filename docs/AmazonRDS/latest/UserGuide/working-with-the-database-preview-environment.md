# Working with the Database Preview environment

The PostgreSQL community continuously releases new PostgreSQL
version and extensions, including beta versions. This gives PostgreSQL users the
opportunity to try out a new PostgreSQL version early. To learn more about the
PostgreSQL community beta release process, see [Beta Information](https://www.postgresql.org/developer/beta/ "https://www.postgresql.org/developer/beta/") in the
PostgreSQL documentation. Similarly, Amazon RDS makes certain PostgreSQL beta versions
available as Preview releases. This allows you to create DB instances using the Preview
version and test out its features in the Database Preview Environment.

RDS for PostgreSQL DB instances in the Database Preview Environment are functionally
similar to other RDS for PostgreSQL instances. However, you can't use a Preview version
for production.

Keep in mind the following important limitations:

- All DB instances are deleted 60 days after you create them, along with any
  backups and snapshots.
- You can only create a DB instance in a virtual private cloud (VPC) based on
  the Amazon VPC service.
- You can only use General Purpose SSD and Provisioned IOPS SSD storage.
- You can't get help from AWS Support with DB instances. Instead, you can
  post your questions to the AWS‐managed Q&A community, [AWS re:Post](https://repost.aws/tags/TAsibBK6ZeQYihN9as4S_psg/amazon-relational-database-service "https://repost.aws/tags/TAsibBK6ZeQYihN9as4S_psg/amazon-relational-database-service").
- You can't copy a snapshot of a DB instance to a production
  environment.
  The following options are supported by the Preview.

- You can create DB instances using M6i, R6i, M6g, M5, T3, R6g, and R5 instance
  types only. For more information about RDS instance classes, see [DB instance classes](Concepts.md "Concepts.md").
- You can use both single-AZ and multi-AZ deployments.
- You can use standard PostgreSQL dump and load functions to export databases
  from or import databases to the Database Preview Environment.

###### Topics

- [Features not supported in the Database Preview environment](#preview-environment-exclusions "#preview-environment-exclusions")
- [PostgreSQL version 17 in the Database Preview environment](#PostgreSQL.Concepts.General.version17 "#PostgreSQL.Concepts.General.version17")
- [Creating a new DB instance in the Database Preview environment](create-db-instance-in-preview-environment.md "create-db-instance-in-preview-environment.md")

## Features not supported in the Database Preview environment

The following features aren't available in the Database Preview
environment:

- Cross-Region snapshot copy
- Cross-Region read replicas

## PostgreSQL version 17 in the Database Preview environment

###### Note

This is preview documentation for Amazon RDS PostgreSQL version 17. It is subject
to change.

PostgreSQL version 17.0 is now available in the Amazon RDS Database Preview
environment. PostgreSQL version 17.0 contains several improvements that are
described in the following PostgreSQL documentation, [PostgreSQL 17
Released!](https://www.postgresql.org/docs/17/release-17.html "https://www.postgresql.org/docs/17/release-17.html")

For information on the Database Preview Environment, see [Working with the Database Preview environment](working-with-the-database-preview-environment.md "working-with-the-database-preview-environment.md"). To access the Preview
Environment from the console, select [https://console.aws.amazon.com/rds-preview/](https://console.aws.amazon.com/rds-preview/ "https://console.aws.amazon.com/rds-preview/").

# Getting started with AWS Database Migration Service

In the following tutorial, you can find out how to perform a database migration with AWS Database Migration Service (AWS DMS).

To perform a database migration, take the following steps:

1. Set up your AWS account by following the steps in [Set up for AWS Database Migration Service](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
2. Create your sample databases and an Amazon EC2 client to populate your source database and test
   replication. Also, create a virtual private cloud (VPC) based on the Amazon Virtual Private Cloud (Amazon VPC) service
   to contain your tutorial resources. To create these resources, follow the steps in
   [Complete prerequisites to set up AWS Database Migration Service](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
3. Populate your source database using a [sample database creation script](https://github.com/aws-samples/aws-database-migration-samples "https://github.com/aws-samples/aws-database-migration-samples").
4. Use DMS Schema Conversion or the AWS Schema Conversion Tool (AWS SCT) to convert the schema from the source database to
   the target database. To use DMS Schema Conversion, follow the steps in [Getting started with DMS Schema Conversion](getting-started.md "getting-started.md"). To convert the schema with AWS SCT, follow the steps in
   [Migrate schema](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
5. Create a replication instance to perform all the processes for the migration. To
   do this and the following tasks, take the steps in [Replication](CHAP_GettingStarted.md "CHAP_GettingStarted.md").
6. Specify source and target database endpoints. For information about creating endpoints, see
   [Creating source and target endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").
7. Create a task to define what tables and replication processes you want to use, and
   start replication. For information about creating database migration tasks, see
   [Creating a task](CHAP_Tasks.md "CHAP_Tasks.md").
8. Verify that replication is working by running queries on the target database.

## Learn more about working with AWS Database Migration Service

Later in this guide, you can learn how to use AWS DMS to migrate your data to and from
the most widely used commercial and open-source databases.

We also recommend that you check the following resources as you prepare and perform a
database migration project:

- [AWS DMS Step-by-Step Migration Guide](../sbs/DMS-SBS-Welcome.md "../sbs/DMS-SBS-Welcome.md") – This guide provides step-by-step
  walkthroughs that go through the process of migrating data to AWS.
- [AWS DMS API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md") – This reference
  describes all the API operations for AWS Database Migration Service in detail.
- [AWS CLI for AWS DMS](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md") – This reference provides
  information about using the AWS Command Line Interface (AWS CLI) with AWS DMS.

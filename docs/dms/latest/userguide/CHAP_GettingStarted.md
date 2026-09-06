

# Getting started with AWS Database Migration Service
<a name="CHAP_GettingStarted"></a>

In the following tutorial, you can find out how to perform a database migration with AWS Database Migration Service (AWS DMS).

To perform a database migration, take the following steps:

1. Set up your AWS account by following the steps in [Set up for AWS Database Migration Service](CHAP_GettingStarted.SettingUp.md).

1. Create your sample databases and an Amazon EC2 client to populate your source database and test replication. Also, create a virtual private cloud (VPC) based on the Amazon Virtual Private Cloud (Amazon VPC) service to contain your tutorial resources. To create these resources, follow the steps in [Complete prerequisites to set up AWS Database Migration Service](CHAP_GettingStarted.Prerequisites.md).

1. Populate your source database using a [sample database creation script](https://github.com/aws-samples/aws-database-migration-samples). 

1. Use DMS Schema Conversion to convert the schema from the source database to the target database. Follow the steps in [Getting started with DMS Schema Conversion](getting-started.md). Alternatively, if you are using the legacy AWS Schema Conversion Tool (AWS SCT), follow the steps in [Migrate schema](CHAP_GettingStarted.SCT.md).

1. Create a replication instance to perform all the processes for the migration. To do this and the following tasks, take the steps in [Replication](CHAP_GettingStarted.Replication.md).

1. Specify source and target database endpoints. For information about creating endpoints, see [Creating source and target endpoints](CHAP_Endpoints.Creating.md).

1. Create a task to define what tables and replication processes you want to use, and start replication. For information about creating database migration tasks, see [Creating a task](CHAP_Tasks.Creating.md).

1. Verify that replication is working by running queries on the target database.

## Learn more about working with AWS Database Migration Service
<a name="CHAP_GettingStarted.References"></a>

Later in this guide, you can learn how to use AWS DMS to migrate your data to and from the most widely used commercial and open-source databases. 

We also recommend that you check the following resources as you prepare and perform a database migration project:
+ [AWS DMS Step-by-Step Migration Guide](https://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html) – This guide provides step-by-step walkthroughs that go through the process of migrating data to AWS.
+ [AWS DMS API Reference](https://docs.aws.amazon.com/dms/latest/APIReference/Welcome.html) – This reference describes all the API operations for AWS Database Migration Service in detail.
+ [AWS CLI for AWS DMS](https://docs.aws.amazon.com/cli/latest/reference/dms/index.html) – This reference provides information about using the AWS Command Line Interface (AWS CLI) with AWS DMS.


# Overview of the homogeneous data migration process in AWS DMS
<a name="dm-getting-started"></a>

You can use homogeneous data migrations in AWS DMS to migrate data between two databases of the same type. Use the following workflow to create and run a data migration.

1. Create the required AWS Identity and Access Management (IAM) policy and role. For more information, see [Creating IAM resources](dm-iam-resources.md).

1. Configure your source and target databases and create database users with the minimum permissions required for homogeneous data migrations in AWS DMS. For more information, see [ Creating source data providers](dm-data-providers-source.md) and [ Create and set a target database](dm-data-providers-target.md). 

1. Store your source and target database credentials in AWS Secrets Manager. For more information, see [Step 1: Create the secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded-db-creds.html#hardcoded-db-creds_step2) in the *AWS Secrets Manager User Guide*.

1. Create a subnet group, an instance profile, and data providers in the AWS DMS console. For more information, see [Creating a subnet group](subnet-group.md), [Creating instance profiles](instance-profiles.md), and [ Creating data providers](data-providers-create.md).

1. Create a migration project by using the resources that you created in the previous step. For more information, see [ Creating migration projects](migration-projects-create.md).

1. Create, configure, and start a data migration. For more information, see [Creating a data migration](dm-migrating-data-create.md).

1. After you complete the full load or ongoing replication, you can cut over to start using your new target database.

1. Clean up your resources. Amazon terminates your data migration in your migration project in three days after you complete the migration. However, you need to manually delete such resources as instance profile, data providers, IAM policy and role, and secrets in AWS Secrets Manager.

For more information about homogeneous data migrations in AWS DMS, read the step-by-step migration walkthough for [PostgreSQL to Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql.html) migrations.

The following video introduces the homogeneous data migrations user interface and helps you get familiar with this feature.

[![AWS Videos](http://img.youtube.com/vi/HOJfrR6lcuU/0.jpg)](http://www.youtube.com/watch?v=HOJfrR6lcuU)

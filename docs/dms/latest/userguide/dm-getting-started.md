# Overview of the homogeneous data migration process in AWS DMS

You can use homogeneous data migrations in AWS DMS to migrate data between two databases of the same type. Use the following workflow
to create and run a data migration.

1. Create the required AWS Identity and Access Management (IAM) policy and role. For more information, see
   [Creating IAM resources](dm-iam-resources.md "dm-iam-resources.md").
2. Configure your source and target databases and create database users with the minimum permissions
   required for homogeneous data migrations in AWS DMS. For more information, see [Creating source data providers](dm-data-providers-source.md "dm-data-providers-source.md") and [Create and set a target database](dm-data-providers-target.md "dm-data-providers-target.md").
3. Store your source and target database credentials in AWS Secrets Manager. For more information, see [Step 1: Create the secret](../../../secretsmanager/latest/userguide/hardcoded-db-creds.md#hardcoded-db-creds_step2 "../../../secretsmanager/latest/userguide/hardcoded-db-creds.md#hardcoded-db-creds_step2") in the _AWS Secrets Manager User Guide_.
4. Create a subnet group, an instance profile, and data providers in the AWS DMS console.
   For more information, see [Creating a subnet group](subnet-group.md "subnet-group.md"),
   [Creating instance profiles](instance-profiles.md "instance-profiles.md"), and
   [Creating data providers](data-providers-create.md "data-providers-create.md").
5. Create a migration project by using the resources that you created in the previous step.
   For more information, see [Creating migration projects](migration-projects-create.md "migration-projects-create.md").
6. Create, configure, and start a data migration. For more information,
   see [Creating a data migration](dm-migrating-data-create.md "dm-migrating-data-create.md").
7. After you complete the full load or ongoing replication, you can cut over to start using your new target database.
8. Clean up your resources. Amazon terminates your data migration in your migration project
   in three days after you complete the migration. However, you need to manually delete such
   resources as instance profile, data providers, IAM policy and role, and secrets in AWS Secrets Manager.
   For more information about homogeneous data migrations in AWS DMS, read the step-by-step migration walkthough for
   [PostgreSQL to
   Amazon RDS for PostgreSQL](../sbs/dm-postgresql.md "../sbs/dm-postgresql.md") migrations.

The following video introduces the homogeneous data migrations
user interface and helps you get familiar with this feature.

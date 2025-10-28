# Migrating PostgreSQL databases to Amazon RDS for PostgreSQL with DMS homogeneous data migrations

This walkthrough gets you started with a homogeneous database migration from PostgreSQL to Amazon RDS for PostgreSQL. To automate the migration, we use homogeneous data migrations in AWS DMS. For homogeneous data migrations, AWS DMS uses native database tools to provide easy and performant like-to-like migrations. This approach helps you effectively set up and run the migration from the source PostgreSQL database to its equivalent target.

With [homogeneous data migrations](../userguide/data-migrations.md "../userguide/data-migrations.md"), you can migrate data, table partitions, data types, and secondary objects such as functions, stored procedures, and so on. Homogeneous data migrations in AWS DMS precisely map your source database to its equivalent Amazon RDS or Amazon Aurora target. You can also use homogeneous data migrations to replicate ongoing changes from your source database to your compatible target.

Note that when using homogeneous data migrations, AWS DMS migrates your source views as tables to the target database. Otherwise, the schema and data of the target matches the schema and data of the source. This typically results in a substantially faster migration from start to finish than using AWS DMS migration tasks.

This introductory exercise shows how you can use homogeneous data migrations in AWS DMS to migrate your self-managed PostgreSQL database to the AWS Cloud.

At a high level, this migration includes the following steps:

- Use the AWS Management Console to create the required resources:
  - Create a VPC in the Amazon VPC console.
  - Create IAM roles in the IAM console.
  - Create your target Amazon RDS for PostgreSQL database in the Amazon RDS console.
  - Store database credentials in AWS Secrets Manager.

- Use the AWS DMS console to configure your migration resources:

      + Create a subnet group and an instance profile for your migration project.
      + Create data providers for your source and target databases.
      + Create a migration project.
      + Create and run a data migration.

  Watch [this video](https://www.youtube.com/embed/HOJfrR6lcuU "https://www.youtube.com/embed/HOJfrR6lcuU") to learn how to use homogeneous data migrations in AWS DMS.

This walkthrough takes approximately three hours to complete. Make sure that you delete resources at the end of this walkthrough to avoid additional charges.

###### Topics

- [Prerequisties for migrating PostgreSQL databases](dm-postgresql-prerequisites.md "dm-postgresql-prerequisites.md")
- [PostgreSQL to Amazon RDS migration overview](dm-postgresql-migration-overview.md "dm-postgresql-migration-overview.md")
- [Step-by-step PostgreSQL database to Amazon RDS migration walkthrough](dm-postgresql-step-by-step-migration.md "dm-postgresql-step-by-step-migration.md")
- [PostgreSQL database to Amazon RDS post-migration clean-up](dm-postgresql-next-steps.md "dm-postgresql-next-steps.md")

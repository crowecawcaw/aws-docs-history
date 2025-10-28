# Step 7: Create a Migration Project

Now you can create a migration project. A migration project describes your instance profile, source and target data providers, and secrets from AWS Secrets Manager.

To create a migration project

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose your AWS Region.
3. Choose **Migration projects**, and then choose **Create migration project**.
4. For **Name**, enter a unique name for your migration project. For example, enter `dm-project`.
5. For **Instance profile**, choose `dm-instance-profile`. You created this instance profile in [Step 5](dm-postgresql-step-5.md "dm-postgresql-step-5.md").
6. For **Source**, choose **Browse**, and then choose `dm-postgresql-source-provider`. You created this data provider in [Step 6](dm-postgresql-step-6.md "dm-postgresql-step-6.md").
7. For **Secret ID**, choose `dm-postgresql-source`. You created this secret in [Step 4](dm-postgresql-step-4.md "dm-postgresql-step-4.md").
8. For **IAM role**, choose `HomogeneousDataMigrationsRole`. You created this role in [Step 1](dm-postgresql-step-1.md "dm-postgresql-step-1.md").
9. For **Target**, choose **Browse**, and then choose `dm-postgresql-target-provider`. You created this data provider in [Step 6](dm-postgresql-step-6.md "dm-postgresql-step-6.md").
10. For **Secret ID**, choose `dm-postgresql-target`. You created this secret in [Step 4](dm-postgresql-step-4.md "dm-postgresql-step-4.md").
11. For **IAM role**, choose `HomogeneousDataMigrationsRole`. You created this role in [Step 1](dm-postgresql-step-1.md "dm-postgresql-step-1.md").
12. Choose **Create migration project**.
    Use this migration project to migrate your source PostgreSQL database to your Amazon RDS for PostgreSQL database.

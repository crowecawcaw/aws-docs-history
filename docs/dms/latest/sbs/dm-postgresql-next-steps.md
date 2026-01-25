# PostgreSQL database to Amazon RDS post-migration clean-up

After you migrate your PostgreSQL database to Amazon RDS for PostgreSQL using homogeneous data migrations in AWS DMS, you can explore several other resources:

- Use DMS Fleet Advisor to inventory your source databases and discover other candidates to move to the cloud. For more information, see the [DMS Fleet Advisor User Guide](../userguide/CHAP_FleetAdvisor.md "../userguide/CHAP_FleetAdvisor.md").
- Learn more about Amazon RDS for PostgreSQL. For more information, see the [Amazon Relational Database Service User Guide](../../../AmazonRDS/latest/UserGuide/Welcome.md "../../../AmazonRDS/latest/UserGuide/Welcome.md").
  After you’ve finished using your migration project, clean up your resources.

**To clean up your AWS DMS resources**

- Sign in to the AWS Management Console and open the AWS DMS console.
- In the navigation pane, choose **Migration projects**, and choose `dm-project`. On the **Data migrations** tab, choose **Stop** for **Actions**.
- After AWS DMS stops your data migration, choose **Delete** for **Actions** and confirm your choice.
- Choose **Migration projects**, and choose `dm-project`. Choose **Delete** for **Actions** and confirm your choice.
- Choose **Instance profiles**, and choose `dm-instance-profile`. Choose **Delete** and confirm your choice.
- Choose **Data providers**, and then select the check boxes for `dm-postgresql-source-provider` and `dm-postgresql-target-provider`. Choose **Delete** and confirm your choice.
- Delete your database users that you created in [Step 2](dm-postgresql-step-2.md "dm-postgresql-step-2.md") and [Step 3](dm-postgresql-step-3.md "dm-postgresql-step-3.md").
- Drop the replication slot and the publisher in the source database by using the following code example.

```
SELECT pg_drop_replication_slot('migration_subscriber_{ARN}');
DROP PUBLICATION publication_{ARN};
```

Also, make sure that you delete your database secrets in AWS Secrets Manager, IAM role, IAM policy, and the virtual private cloud (VPC).

# Limitations and considerations for

Amazon RDS
blue/green deployments

Blue/green deployments in Amazon RDS require careful consideration of factors such as
replication slots, resource management, instance sizing, and potential impacts on database
performance. The following sections provide guidance to help you optimize your deployment
strategy to ensure minimal downtime, seamless transitions, and effective management of your
database environment.

###### Topics

- [Limitations for blue/green deployments](#blue-green-deployments-limitations "#blue-green-deployments-limitations")
- [Considerations for blue/green deployments](#blue-green-deployments-consider "#blue-green-deployments-consider")

## Limitations for blue/green deployments

The following limitations apply to blue/green deployments.

###### Topics

- [General limitations for blue/green
  deployments](#blue-green-deployments-limitations-general "#blue-green-deployments-limitations-general")
- [RDS for MySQL limitations for
  blue/green deployments](#blue-green-deployments-limitations-mysql "#blue-green-deployments-limitations-mysql")
- [RDS for PostgreSQL limitations for
  blue/green deployments with physical replication](#blue-green-deployments-limitations-postgres-physical "#blue-green-deployments-limitations-postgres-physical")
- [RDS for PostgreSQL
  limitations for blue/green deployments with logical
  replication](#blue-green-deployments-limitations-postgres-logical "#blue-green-deployments-limitations-postgres-logical")

### General limitations for blue/green

deployments

The following general limitations apply to blue/green deployments:

- Blue/green deployments don't support managing master user passwords with
  AWS Secrets Manager.
- If dedicated log volume (DLV) is enabled on the blue database, it must be enabled on _all_ DB instances, including read replicas.
- During switchover, the blue and green environments can't have zero-ETL integrations with
  Amazon Redshift. You must delete the integration first and switch over, then recreate the
  integration.
- The Event Scheduler (`event_scheduler` parameter) must be disabled on the
  green environment when you create a blue/green deployment. This prevents events from being
  generated in the green environment and causing inconsistencies.
- You can't change an unencrypted DB instance
  into an encrypted DB instance. In
  addition, you can't change an encrypted DB instance
  into an unencrypted DB instance.
- You can't change a blue DB instance
  to a higher engine version than its
  corresponding green DB instance.
- The resources in the blue environment and green environment must be in the same
  AWS account.
- Blue/green deployments aren't supported for the following features:
  - Amazon RDS Proxy
  - Cascading read replicas
  - Cross-Region read replicas
  - AWS CloudFormation
  - Multi-AZ DB cluster deployments

  Blue/green deployments are supported for Multi-AZ DB instance deployments. For
  more information about Multi-AZ deployments, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

### RDS for MySQL limitations for

blue/green deployments

The following limitations apply to RDS for MySQL blue/green deployments:

- The blue DB instance can't be an external binlog replica.
- If the source database is associated with a custom option group, you can't specify a
  major version upgrade when you create the blue/green deployment.

In this case, you can create a blue/green deployment without specifying a major
version upgrade. Then, you can upgrade the database in the green environment. For more
information, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

- Blue/green deployments don't support the AWS JDBC Driver for MySQL. For more information,
  see [Known Limitations](https://github.com/awslabs/aws-mysql-jdbc?tab=readme-ov-file#known-limitations "https://github.com/awslabs/aws-mysql-jdbc?tab=readme-ov-file#known-limitations") on GitHub.

### RDS for PostgreSQL limitations for

blue/green deployments with physical replication

The following limitations apply to RDS for PostgreSQL blue/green deployments that use
physical replication. For an explanation of when blue/green deployments use physical
replication instead of logical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

- After the green environment is created, you can't perform a manual major version
  upgrade.
- Blue/green deployments that use physical replication don't support schema changes
  on the green environment, as it is strictly read-only.
- The blue DB instance can't be a logical source (publisher) or replica
  (subscriber).
- Blue/Green deployments have the following limitations when configuring delayed
  replication in RDS for PostgreSQL:
  - **Green source instance** — The
    `recovery_min_apply_delay parameter` is disregarded, even
    if configured in the parameter group. Any delay settings on the green
    source instance do not take effect.
  - **Green replica instance** — The
    `recovery_min_apply_delay parameter` is fully supported
    and applied to the PostgreSQL configuration file. Delay settings
    function as expected during the switchover workflow.
  - Delayed replication isn't compatible with RDS Blue/Green deployments for major version upgrades.

### RDS for PostgreSQL

limitations for blue/green deployments with logical
replication

The following limitations apply to RDS for PostgreSQL blue/green
deployments that use logical replication. For an explanation of when blue/green deployments use logical
replication instead of physical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

- [Unlogged](https://www.postgresql.org/docs/16/sql-createtable.html#SQL-CREATETABLE-UNLOGGED "https://www.postgresql.org/docs/16/sql-createtable.html#SQL-CREATETABLE-UNLOGGED") tables aren't replicated to the green environment.
- The blue DB instance can't be a logical source (publisher) or replica
  (subscriber).
- If the blue DB instance is configured as the foreign server of a foreign data wrapper (FDW)
  extension, you must use the instance endpoint name instead of IP addresses. This
  allows the configuration to remain functional after switchover.
- In a blue/green deployment, each database requires a logical replication slot. As
  the number of databases grows, resource overhead increases and can potentially lead to
  replication lag, especially if the DB instance isn't sufficiently scaled. The impact depends
  on factors such as database workload and the number of connections. To mitigate this,
  consider scaling up your DB instance class or reducing the number of databases on the
  source instance.
- The logical replication [apply process](https://www.postgresql.org/docs/current/logical-replication-architecture.html "https://www.postgresql.org/docs/current/logical-replication-architecture.html") in the green environment is single-threaded. If the blue
  environment generates a high volume of write traffic, the green environment might not
  be able to keep up. This can lead to replication lag or failure, especially for
  workloads that produce continuous high write throughput. Make sure to test your
  workloads thoroughly. For scenarios that require major version upgrades and handling
  high-volume write workloads, consider alternative approaches such as using [AWS Database Migration Service
  (AWS DMS)](../../../dms/latest/userguide/data-migrations.md "../../../dms/latest/userguide/data-migrations.md").
- Blue/Green deployments have the following limitations when configuring delayed
  replication in RDS for PostgreSQL:
  - **Green source instance** — The
    `recovery_min_apply_delay parameter` is disregarded, even
    if configured in the parameter group. Any delay settings on the green
    source instance do not take effect.
  - **Green replica instance** — The
    `recovery_min_apply_delay parameter` is fully supported
    and applied to the PostgreSQL configuration file. Delay settings
    function as expected during the switchover workflow.
  - Delayed replication isn't compatible with RDS Blue/Green deployments for major version upgrades.

- Creating new partitions on partitioned tables isn't supported during blue/green
  deployments for RDS for PostgreSQL. Creating new partitions involves data definition language
  (DDL) operations such as `CREATE TABLE`, which aren't replicated from the
  blue environment to the green environment. However, existing partitioned tables and
  their data will be replicated to the green environment.
- The following limitations apply to PostgreSQL extensions:
  - The `pg_partman` extension must be disabled in the blue environment
    when you create a blue/green deployment. The extension performs DDL operations
    such as `CREATE TABLE`, which break logical replication from the blue
    environment to the green environment.
  - The `pg_cron` extension must remain disabled on all green databases
    after the blue/green deployment is created. The extension has background workers
    that run as superuser and bypass the read-only setting of the green environment,
    which might cause replication conflicts.
  - The `pglogical` and `pgactive` extensions must be
    disabled on the blue environment when you create a blue/green deployment. After
    you switch over the green environment to be the new production environment, you
    can enable the extensions again. In addition, the blue database can’t be a logical
    subscriber of an external instance.
  - If you're using the `pgAudit` extension, it must remain in the
    shared libraries (`shared_preload_libraries`) on the custom DB
    parameter groups for both the blue and the green DB instances. For more information, see
    [Setting up the pgAudit extension](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md").

#### Logical replication-specific

limitations for blue/green deployments

PostgreSQL has certain restrictions related to logical replication, which translate to
limitations when creating blue/green deployments for RDS for PostgreSQL
DB instances.

The following table describes logical replication limitations that apply to blue/green
deployments for RDS for PostgreSQL. For more information, see [Restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "https://www.postgresql.org/docs/current/logical-replication-restrictions.html") in the PostgreSQL logical replication documentation.

| Limitation                                                                                                                                                                                                            | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data definition language (DDL) statements, such as `CREATE TABLE` and `CREATE SCHEMA`, aren't replicated from the blue environment to the green environment.                                                          | If Amazon RDS detects a DDL change in the blue environment, your green databases enter a state of **Replication degraded**. You must delete the blue/green deployment and all green databases, then recreate it.                                                                                                                                                                                                                                                      |
| Data control language (DCL) statements, such as `GRANT` and `REVOKE`, aren't replicated from the blue environment to the green environment.                                                                           | If Amazon RDS PostgreSQL detects an attempt to execute a DCL statement in the blue environment, you will see a warning message. There is no configuration or API available to change this behavior, as it is a limitation of the blue/green deployment process.                                                                                                                                                                                                       |
| `NEXTVAL` operations on sequence objects aren't synchronized between the blue environment and the green environment.                                                                                                  | During switchover, Amazon RDS increments sequence values in the green environment to match those in the blue environment. If you have thousands of sequences, this can delay switchover.                                                                                                                                                                                                                                                                              |
| Large objects in the blue environment aren't replicated to the green environment. This includes both existing large objects and any newly created or modified large objects during the blue/green deployment process. | If Amazon RDS detects the creation or modification of large objects in the blue environment that are stored in the `pg_largeobject` system table, your green databases enter a state of **Replication degraded**. You must delete the blue/green deployment and all green databases, then recreate it.                                                                                                                                                                |
| Materialized views aren’t automatically refreshed in the green environment.                                                                                                                                           | Refreshing materialized views in the blue environment doesn't refresh them in the green environment. After switchover, you can manually refresh them using the [REFRESH MATERIALIZED VIEW](https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html "https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html") command, or schedule a refresh.                                                                                       |
| UPDATE and DELETE operations aren't permitted on tables that don't have a primary key.                                                                                                                                | Before you create a blue/green deployment, make sure that all tables have a primary key or use `REPLICA IDENTITY FULL`. However, only use `REPLICA IDENTITY FULL` if no primary or unique key exists, as it affects replication performance. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "https://www.postgresql.org/docs/current/logical-replication-restrictions.html"). | ## Considerations for blue/green deployments Amazon RDS tracks resources in blue/green deployments with the `DbiResourceId` of each resource. This resource ID is an AWS Region-unique, immutable identifier for the resource. The _resource_ ID is separate from the DB _instance_ ID. Each one is listed in the database configuration in the RDS console. The name (instance ID) of a resource changes when you switch over a blue/green deployment, but each resource keeps the same resource ID. For example, a DB instance identifier might be `mydb` in the blue environment. After switchover, the same DB instance might be renamed to `mydb-old1`. However, the resource ID of the DB instance doesn't change during switchover. So, when you switch over the green resources to be the new production resources, their resource IDs don't match the blue resource IDs that were previously in production. After you switch over a blue/green deployment, consider updating the resource IDs to those of the newly transitioned production resources for integrated features and services that you used with the production resources. Specifically, consider the following updates: <br>• If you perform filtering using the RDS API and resource IDs, adjust the resource IDs used in filtering after switchover. <br>• If you use CloudTrail for auditing resources, adjust the consumers of the CloudTrail to track the new resource IDs after switchover. For more information, see [Monitoring Amazon RDS API calls in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md"). <br>• If you use the Performance Insights API, adjust the resource IDs in calls to the API after switchover. For more information, see [Monitoring DB load with Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md"). You can monitor a database with the same name after switchover, but it doesn't contain the data from before the switchover. <br>• If you use resource IDs in IAM policies, make sure you add the resource IDs of the newly transitioned resources when necessary. For more information, see [Identity and access management for Amazon RDS](UsingWithRDS.md "UsingWithRDS.md"). <br>• If you have IAM roles associated with your DB instance, make sure to reassociate them after switchover. Attached roles aren't automatically copied to the green environment. <br>• If you authenticate to your DB instance using [IAM database authentication](UsingWithRDS.md "UsingWithRDS.md"), make sure that the IAM policy used for database access has both the blue and the green databases listed under the `Resource` element of the policy. This is required in order to connect to the green database after switchover. For more information, see [Creating and using an IAM policy for IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md"). <br>• If you use AWS Backup to manage automated backups of resources in a blue/green deployment, adjust the resource IDs used by AWS Backup after switchover. For more information, see [Using AWS Backup to manage automated backups for Amazon RDS](AutomatedBackups.md "AutomatedBackups.md"). <br>• If you want to restore a manual or automated DB snapshot for a DB instance that was part of a blue/green deployment, make sure you restore the correct DB snapshot by examining the time when the snapshot was taken. For more information, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md"). <br>• If you want to describe a previous blue environment DB instance automated backup or restore it to a point in time, use the resource ID for the operation. Because the name of the DB instance changes during switchover, you can't use its previous name for `DescribeDBInstanceAutomatedBackups` or `RestoreDBInstanceToPointInTime` operations. For more information, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md"). <br>• When you add a read replica to a DB instance in the green environment of a blue/green deployment, the new read replica won't replace a read replica in the blue environment when you switch over. However, the new read replica is retained in the new production environment after switchover. <br>• After you switch over, AWS Database Migration Service (AWS DMS) replication tasks can't resume because the checkpoint from the blue environment is invalid in the green environment. You must recreate the DMS task with a new checkpoint to continue replication. <br>• When you delete a DB instance in the green environment of a blue/green deployment, you can't create a new DB instance to replace it in the blue/green deployment. If you create a new DB instance with the same name and Amazon Resource Name (ARN) as the deleted DB instance, it has a different `DbiResourceId`, so it isn't part of the green environment. The following behavior results if you delete a DB instance in the green environment: + If the DB instance in the blue environment with the same name exists, it won't be switched over to the DB instance in the green environment. This DB instance won't be renamed by adding `-old`n`` to the DB instance name. + Any application that points to the DB instance in the blue environment continues to use the same DB instance after switchover. The same behavior applies to DB instances and read replicas. <br>• If you use resource tags for access control or operational management, you need to understand that tag changes aren't synchronized between blue and green environments until switchover. When you create a blue/green deployment, tags from the blue environment are copied to the green environment. After creation, any tag modifications that you make to either environment aren't automatically synchronized. During switchover, blue environment tags replace all tags in the green environment. Apply all necessary tags to the blue environment before you create the blue/green deployment, or reapply required tags to the new production environment after switchover. For more information about tags, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md"). |

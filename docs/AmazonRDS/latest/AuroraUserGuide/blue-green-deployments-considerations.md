# Limitations and considerations for

Amazon Aurora
blue/green deployments

Blue/green deployments in Amazon RDS require careful consideration of factors such as
replication slots, resource management, instance sizing, and potential impacts on database
performance. The following sections provide guidance to help you optimize your deployment
strategy to ensure minimal downtime, seamless transitions, and effective management of your
database environment.

###### Topics

- [Limitations for blue/green deployments](#blue-green-deployments-limitations "#blue-green-deployments-limitations")
- [Aurora Global Database limitations for
  blue/green deployments](#blue-green-deployments-limitations-agd "#blue-green-deployments-limitations-agd")
- [Considerations for blue/green deployments](#blue-green-deployments-consider "#blue-green-deployments-consider")

## Limitations for blue/green deployments

The following limitations apply to blue/green deployments.

###### Topics

- [General limitations for blue/green
  deployments](#blue-green-deployments-limitations-general "#blue-green-deployments-limitations-general")
- [Aurora MySQL limitations for
  blue/green deployments](#blue-green-deployments-limitations-mysql "#blue-green-deployments-limitations-mysql")
- [Aurora PostgreSQL
  limitations for blue/green deployments](#blue-green-deployments-limitations-postgres-logical "#blue-green-deployments-limitations-postgres-logical")

### General limitations for blue/green

deployments

The following general limitations apply to blue/green deployments:

- You can't stop and start a cluster that is part of a blue/green deployment.
- Blue/green deployments don't support managing master user passwords with
  AWS Secrets Manager.
- If you attempt to force a backtrack on the blue DB cluster, the blue/green deployment
  breaks and switchover is blocked.
- During switchover, the blue and green environments can't have zero-ETL integrations with
  Amazon Redshift. You must delete the integration first and switch over, then recreate the
  integration.
- The Event Scheduler (`event_scheduler` parameter) must be disabled on the
  green environment when you create a blue/green deployment. This prevents events from being
  generated in the green environment and causing inconsistencies.
- Auto Scaling policies configured on the blue DB cluster are not copied to the green
  environment. You must reconfigured them after switchover, regardless of whether they
  were initially set up on the blue or green environment.
- You can't change an unencrypted DB
  cluster into an encrypted DB cluster. In
  addition, you can't change an encrypted DB
  cluster into an unencrypted DB cluster.
- You can't change a blue DB
  cluster to a higher engine version than its
  corresponding green DB cluster.
- The resources in the blue environment and green environment must be in the same
  AWS account.
- Blue/green deployments aren't supported for the following features:
  - Amazon RDS Proxy
  - Cross-Region read replicas
  - Aurora Serverless v1 DB clusters
  - CloudFormation

### Aurora MySQL limitations for

blue/green deployments

The following limitations apply to Aurora MySQL blue/green deployments:

- The source DB cluster can't contain any databases named `tmp`. Databases with
  this name will not be copied to the green environment.
- The blue DB cluster can't be an external binlog replica.
- If the source DB cluster that has backtrack enabled, the green DB cluster is created without
  backtracking support. This is because backtracking doesn't work with binary log (binlog)
  replication, which is required for blue/green deployments. For more information, see
  [Backtracking an Aurora DB cluster](AuroraMySQL.Managing.md "AuroraMySQL.Managing.md").
- Blue/green deployments don't support the AWS JDBC Driver for MySQL. For more information,
  see [Known Limitations](https://github.com/awslabs/aws-mysql-jdbc?tab=readme-ov-file#known-limitations "https://github.com/awslabs/aws-mysql-jdbc?tab=readme-ov-file#known-limitations") on GitHub.

### Aurora PostgreSQL

limitations for blue/green deployments

The following limitations apply to Aurora PostgreSQL blue/green
deployments.

- [Unlogged](https://www.postgresql.org/docs/16/sql-createtable.html#SQL-CREATETABLE-UNLOGGED "https://www.postgresql.org/docs/16/sql-createtable.html#SQL-CREATETABLE-UNLOGGED") tables aren't replicated to the green environment unless the `rds.logically_replicate_unlogged_tables`
  parameter is set to `1` on the blue DB cluster. Don't modify this parameter
  value after you create a blue/green deployment to avoid possible replication errors
  on unlogged tables.
- The blue DB cluster can't be a logical source (publisher) or replica
  (subscriber).
- If the blue DB cluster is configured as the foreign server of a foreign data wrapper (FDW)
  extension, you must use the cluster endpoint name instead of IP addresses. This
  allows the configuration to remain functional after switchover.
- In a blue/green deployment, each database requires a logical replication slot. As
  the number of databases grows, resource overhead increases and can potentially lead to
  replication lag, especially if the DB cluster isn't sufficiently scaled. The impact depends
  on factors such as database workload and the number of connections. To mitigate this,
  consider scaling up your DB instance class or reducing the number of databases on the
  source cluster.
- Blue/green deployments are supported for Babelfish for Aurora PostgreSQL only for version 15.7 and
  higher 15 versions, and 16.3 and higher 16 versions.
- If you want to capture execution plans in Aurora Replicas, you must provide the
  blue DB cluster endpoint when calling the
  `apg_plan_mgmt.create_replica_plan_capture` function. This ensures that
  plan captures continue to work after switchover. For more information, see [Capturing Aurora PostgreSQL execution plans in Replicas](AuroraPostgreSQL.QPM.md "AuroraPostgreSQL.QPM.md").
- The logical replication [apply process](https://www.postgresql.org/docs/current/logical-replication-architecture.html "https://www.postgresql.org/docs/current/logical-replication-architecture.html") in the green environment is single-threaded. If the blue
  environment generates a high volume of write traffic, the green environment might not
  be able to keep up. This can lead to replication lag or failure, especially for
  workloads that produce continuous high write throughput. Make sure to test your
  workloads thoroughly. For scenarios that require major version upgrades and handling
  high-volume write workloads, consider alternative approaches such as using [AWS Database Migration Service
  (AWS DMS)](../../../dms/latest/userguide/data-migrations.md "../../../dms/latest/userguide/data-migrations.md") or [self-managed logical replication](AuroraPostgreSQL.md "AuroraPostgreSQL.md").
- Creating new partitions on partitioned tables isn't supported during blue/green
  deployments for Aurora. Creating new partitions involves data definition language
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
  - The `apg_plan_mgmt` extension must have the
    `apg_plan_mgmt.capture_plan_baselines` parameter set to
    `off` on all green databases to avoid primary key conflicts if an
    identical plan is captured in the blue environment. For more information, see
    [Overview of Aurora PostgreSQL query
    plan management](AuroraPostgreSQL.Optimize.md "AuroraPostgreSQL.Optimize.md").
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
limitations when creating blue/green deployments for Aurora PostgreSQL DB clusters.

The following table describes logical replication limitations that apply to blue/green
deployments for Aurora PostgreSQL. For more information, see [Restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "https://www.postgresql.org/docs/current/logical-replication-restrictions.html") in the PostgreSQL logical replication documentation.

| Limitation                                                                                                                                                                                                            | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Data definition language (DDL) statements, such as `CREATE TABLE`<br>and `CREATE SCHEMA`, aren't replicated from the blue environment to the<br>green environment.                                                    | If Aurora detects a DDL change in the blue environment, your green<br>databases enter a state of **Replication<br>degraded**. You must delete the blue/green deployment and all green<br>databases, then recreate it.                                                                                                                                                                                                                                                          |
| Data control language (DCL) statements, such as `GRANT` and `REVOKE`, aren't replicated from the blue environment to the green environment.                                                                           | If Aurora detects an attempt to execute a DCL statement in the blue environment, you will see a warning message. There is no configuration or API available to change this behavior, as it is a limitation of the blue/green deployment process.                                                                                                                                                                                                                               |
| `NEXTVAL` operations on sequence objects aren't synchronized between<br>the blue environment and the green environment.                                                                                               | During switchover, Aurora increments sequence values in the green<br>environment to match those in the blue environment. If you have thousands of<br>sequences, this can delay switchover.                                                                                                                                                                                                                                                                                     |
| Large objects in the blue environment aren't replicated to the green environment. This includes both existing large objects and any newly created or modified large objects during the blue/green deployment process. | If Aurora detects the creation or modification of large objects in the<br>blue environment that are stored in the `pg_largeobject` system<br>table, your green databases enter a state of **Replication<br>degraded**. You must delete the blue/green deployment and all green<br>databases, then recreate it.                                                                                                                                                                 |
| Refreshing materialized views breaks replication.                                                                                                                                                                     | Refreshing materialized views in the blue environment<br>breaks replication to the green environment. Refrain from refreshing<br>materialized views in the blue environment. After a switchover, you can<br>manually refresh them using the [REFRESH MATERIALIZED VIEW](https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html "https://www.postgresql.org/docs/current/sql-refreshmaterializedview.html") command, or schedule a refresh.                   |
| UPDATE and DELETE operations aren't permitted on tables that don't have a<br>primary key.                                                                                                                             | Before you create a blue/green deployment, make sure that all tables have<br>a primary key or use `REPLICA IDENTITY FULL`. However, only use<br>`REPLICA IDENTITY FULL` if no primary or unique key exists, as it<br>affects replication performance. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "https://www.postgresql.org/docs/current/logical-replication-restrictions.html"). |

## Aurora Global Database limitations for

blue/green deployments

In addition to the above stated general and engine specific limitations, the following limitations apply for blue/green deployments for Aurora Global Database:

- All operations must be initiated from the same Region as the writer cluster of the Global Database.
- Performing a global switchover or a global failover will cause active blue/green deployment to become invalid. The blue-green deployment need to be deleted and recreated from the new primary region.
- For Aurora PostgreSQL, if you have global write forwarding enabled in your production environment and create a blue/green deployment, write forwarding is disabled on the green cluster. It is enabled in the green environment only after the blue/green switchover when the green environment becomes the new production environment. After switchover, write forwarding is disabled on the `-old1` cluster.
- Modifying to the topology of the global database after the creation of the blue/green deployment will cause the active blue/green deployment to become invalid. The blue-green deployment would have to be deleted and recreated from the new primary region.
- Automated snapshots are retained per the backup retention days that was originally configured in old blue environment. Automated snapshots from old blue cluster are not copied to green.
- Global failover is supported during a blue/green switchover but a global switchover is not supported during a blue/green switchover.
- Ensure DB cluster and DB parameter groups for the green environment exist in all secondary regions with identical names. If the parameter group in any region is unavailable, the default parameter group in the regions is used.
- Avoid using RDS Proxy on any global database members during blue/green deployment switchover.

## Considerations for blue/green deployments

Amazon RDS tracks resources in blue/green deployments with the `DbiResourceId`
and `DbClusterResourceId` of each resource.
This resource ID is an AWS Region-unique, immutable identifier for the resource.

The _resource_ ID is separate from the DB _cluster_ ID. Each one is listed in the database configuration in
the RDS console.

The name (cluster ID) of a resource changes when you switch over a
blue/green deployment, but each resource keeps the same resource ID. For example, a DB cluster
identifier might have been `mycluster` in the blue environment. After switchover,
the same DB cluster might be renamed to `mycluster-old1`. However, the resource ID of
the DB cluster doesn't change during switchover. So, when you switch over the green resources to
be the new production resources, their resource IDs don't match the blue resource IDs that
were previously in production.

After you switch over a blue/green deployment, consider updating the resource IDs to
those of the newly transitioned production resources for integrated features and services
that you used with the production resources. Specifically, consider the following
updates:

- If you perform filtering using the RDS API and resource IDs, adjust the resource IDs
  used in filtering after switchover.
- If you use CloudTrail for auditing resources, adjust the consumers of the CloudTrail to track
  the new resource IDs after switchover. For more information, see [Monitoring Amazon Aurora API calls in AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- If you use Database Activity Streams for resources in the blue environment, adjust your application to
  monitor database events for the new stream after switchover. For more information, see
  [Supported
  Regions and Aurora DB engines for database activity streams](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").
- If you use the Performance Insights API, adjust the resource IDs in calls to the API
  after switchover. For more information, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

You can monitor a database with the same name after switchover, but it doesn't
contain the data from before the switchover.

- If you use resource IDs in IAM policies, make sure you add the resource IDs of the
  newly transitioned resources when necessary. For more information, see [Identity and access management for Amazon Aurora](UsingWithRDS.md "UsingWithRDS.md").
- If you have IAM roles associated with your DB cluster, make sure to reassociate
  them after switchover. Attached roles aren't automatically copied to the green
  environment.
- If you authenticate to your DB cluster using [IAM database authentication](UsingWithRDS.md "UsingWithRDS.md"), make sure that
  the IAM policy used for database access has both the blue and the green databases
  listed under the `Resource` element of the policy. This is required in order
  to connect to the green database after switchover. For more information, see [Creating and using an IAM policy for
  IAM database access](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").
- If you want to restore a manual DB cluster snapshot for a DB cluster that was part of a
  blue/green deployment, make sure you restore the correct DB cluster snapshot by examining the
  time when the snapshot was taken. For more information, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").
- After you switch over, AWS Database Migration Service (AWS DMS) replication tasks can't resume because the
  checkpoint from the blue environment is invalid in the green environment. You must
  recreate the DMS task with a new checkpoint to continue replication.
- Amazon Aurora creates the green environment by _cloning_ the underlying Aurora storage volume in the blue environment. The
  green cluster volume only stores incremental changes made to the green environment. If
  you delete the DB cluster in the blue environment, the size of the underlying Aurora storage
  volume in the green environment grows to the full size. For more information, see [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md").
- When you add a DB instance to the DB cluster in the green environment of a blue/green
  deployment, the new DB instance won't replace a DB instance in the blue environment when you switch
  over. However, the new DB instance is retained in the DB cluster and becomes a DB instance in the new
  production environment.
- When you delete a DB instance in the DB cluster in the green environment of a blue/green
  deployment, you can't create a new DB instance to replace it in the blue/green
  deployment.

If you create a new DB instance with the same name and ARN as the deleted DB instance, it has a
different `DbiResourceId`, so it isn't part of the green environment.

The following behavior results if you delete a DB instance in the DB cluster in the green
environment:

    + If the DB instance in the blue environment with the same name exists, it won't be
     switched over to the DB instance in the green environment. This DB instance won't be renamed by
     appending `-old`n`` to the DB instance name.
    + Any application that points to the DB instance in the blue environment continues to
     use the same DB instance after switchover.

- If you use resource tags for access control or operational management, you need to
  understand that tag changes aren't synchronized between blue and green environments
  until switchover. When you create a blue/green deployment, tags from the blue
  environment are copied to the green environment. After creation, any tag modifications
  that you make to either environment aren't automatically synchronized. During
  switchover, blue environment tags replace all tags in the green environment. Apply all
  necessary tags to the blue environment before you create the blue/green deployment, or
  reapply required tags to the new production environment after switchover. For more
  information about tags, see [Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").

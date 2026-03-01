# Overview of Amazon Aurora Blue/Green Deployments

By using Amazon Aurora Blue/Green Deployments, you can make and test database changes before
implementing them in a production environment. A _blue/green deployment_
creates a staging environment that copies the production environment. In a blue/green
deployment, the _blue environment_ is the current production environment. The
_green environment_ is the staging environment and stays in sync with the
current production environment.

You can make changes to the Aurora DB cluster in the green environment without affecting production
workloads. For example, you can upgrade the major or minor DB engine version or change
database parameters in the staging environment. You can thoroughly test changes in the green
environment. When ready, you can _switch over_ the environments to transition
the green environment to be the new production environment. The switchover typically takes under
a minute with no data loss and no need for application changes.

Because the green environment is a copy of the topology of the production environment, the DB cluster
and all of its DB instances are copied in the deployment. The green environment also includes the features used by the DB cluster,
such as DB cluster snapshots, Performance Insights, Enhanced Monitoring, and Aurora Serverless v2.

###### Note

Blue/Green Deployments are supported for Aurora MySQL, Aurora PostgreSQL, and Aurora Global Database. For Amazon RDS availability,
see [Overview of Amazon RDS
Blue/Green Deployments](../UserGuide/blue-green-deployments-overview.md "../UserGuide/blue-green-deployments-overview.md") in the _Amazon RDS User Guide_.

###### Topics

- [Region and version availability](#blue-green-deployments-region-version-availability "#blue-green-deployments-region-version-availability")
- [Benefits of using Amazon RDS Blue/Green Deployments](#blue-green-deployments-benefits "#blue-green-deployments-benefits")
- [Workflow of a blue/green deployment](#blue-green-deployments-major-steps "#blue-green-deployments-major-steps")
- [Authorizing access to Amazon Aurora blue/green deployment operations](blue-green-deployments-authorizing-access.md "blue-green-deployments-authorizing-access.md")
- [Limitations and considerations for Amazon Aurora blue/green deployments](blue-green-deployments-considerations.md "blue-green-deployments-considerations.md")
- [Best practices for Amazon Aurora blue/green deployments](blue-green-deployments-best-practices.md "blue-green-deployments-best-practices.md")

## Region and version availability

Feature availability and support varies across specific versions of each database engine,
and across AWS Regions. For more information, see [Supported Regions and Aurora DB engines for Blue/Green Deployments](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

## Benefits of using Amazon RDS Blue/Green Deployments

By using Amazon RDS Blue/Green Deployments, you can stay current on security patches, improve
database performance, and adopt newer database features with short, predictable downtime.
Blue/green deployments reduce the risks and downtime for database updates, such as major or
minor engine version upgrades.

Blue/green deployments provide the following benefits:

- Easily create a production-ready staging environment.
- Automatically replicate database changes from the production environment to the staging environment.
- Test database changes in a safe staging environment without affecting the production environment.
- Stay current with database patches and system updates.
- Implement and test newer database features.
- Switch over your staging environment to be the new production environment without changes to your application.
- Safely switch over through the use of built-in switchover guardrails.
- Eliminate data loss during switchover.
- Switch over quickly, typically under a minute depending on your workload.

## Workflow of a blue/green deployment

Complete the following major steps when you use a blue/green deployment for Aurora DB cluster updates.

1. Identify a production DB cluster that requires updates.

The following image shows an example of a production DB cluster.

![Production (blue) Aurora DB cluster in a blue/green deployment](images/blue-green-deployment-blue-environment-aurora.png) 2. Create the blue/green deployment. For instructions, see [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md "blue-green-deployments-creating.md").

The following image shows an example of a blue/green deployment of the production environment from step 1.
While creating the blue/green deployment, RDS copies the complete topology and configuration of the
Aurora DB cluster to create the green environment. The names of the copied DB cluster and DB instances are appended
with `-green-`random-characters``. The staging environment in 
 the image contains the DB cluster (auroradb-green-`_abc123_`).
 It also contains the three DB instances in the DB cluster 
 (auroradb-instance1-green-`_abc123_`, 
 auroradb-instance2-green-`_abc123_`, and 
 auroradb-instance3-green-`_abc123_`).

![Blue/green deployment for Amazon Aurora](images/blue-green-deployment-aurora.png)

When you create the blue/green deployment, you can specify a higher DB engine version and a different DB cluster parameter
group for the DB cluster in the green environment. You can also specify a different DB parameter group for the DB instances
in the DB cluster.

RDS also configures replication from the primary DB instance in the blue environment to the
primary DB instance in the green environment.

###### Important

For Aurora MySQL version 3, after you create the blue/green deployment, the DB cluster in
the green environment does not allow write operations by default. However, this doesn't
apply for users who have the `CONNECTION_ADMIN` privilege, including the
Aurora master user. Users with this privilege can override the `read_only`
behaviour. For more information, see [Role-based privilege model](AuroraMySQL.md#AuroraMySQL.privilege-model "AuroraMySQL.md#AuroraMySQL.privilege-model"). 3. Make changes to the staging environment.

For example, you might change the DB instance class used by one or more DB instances in the green
environment.

For information about modifying a DB cluster, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). 4. Test your staging environment.

During testing, we recommend that you keep your databases in the green environment
read only. Enable write operations on the green environment with caution because they can
result in replication conflicts. They can also result in unintended data in the production
databases after switchover. To enable write operations for Aurora MySQL, set the
`read_only` parameter to `0`, then reboot the DB instance. For
Aurora PostgreSQL, set the `default_transaction_read_only` parameter to
`off` at the session level. 5. When ready, switch over to transition the staging environment to be the new production
environment. For instructions, see [Switching a blue/green deployment in Amazon Aurora](blue-green-deployments-switching.md "blue-green-deployments-switching.md").

The switchover results in downtime. The downtime is usually under one minute, but it can be longer depending
on your workload.

The following image shows the DB clusters after the switchover.

![DB cluster and DB instances after switching over an Amazon Aurora blue/green deployment](images/blue-green-deployment-switchover-aurora.png)

After the switchover, the Aurora DB cluster in the green environment becomes the new
production DB cluster. The names and endpoints in the current production environment are
assigned to the newly switched over production environment, requiring no changes to your
application. As a result, your production traffic now flows to the new production
environment. The DB cluster and DB instances in the blue environment are renamed by appending
`-old`n`to the current name, where
`n``is a number. For example, assume the name of
 the DB instance in the blue environment is`auroradb-instance-1`. After switchover,
 the DB instance name might be `auroradb-instance-1-old1`.

In the example in the image, the following changes occur during switchover:

    * The green environment DB cluster `auroradb-green-abc123` becomes the production DB
     cluster named `auroradb`.
    * The green environment DB instance named `auroradb-instance1-green-abc123` becomes the
     production DB instance `auroradb-instance1`.
    * The green environment DB instance named
     `auroradb-instance2-green-abc123` becomes the production DB instance
     `auroradb-instance2`.
    * The green environment DB instance named `auroradb-instance3-green-abc123` becomes the
     production DB instance `auroradb-instance3`.
    * The blue environment DB cluster named `auroradb` becomes `auroradb-old1`.
    * The blue environment DB instance named `auroradb-instance1` becomes
     `auroradb-instance1-old1`.
    * The blue environment DB instance named `auroradb-instance2` becomes
     `auroradb-instance2-old1`.
    * The blue environment DB instance named `auroradb-instance3` becomes
     `auroradb-instance3-old1`.

6. If you no longer need a blue/green deployment, you can delete it. For instructions, see
   [Deleting a blue/green deployment in Amazon Aurora](blue-green-deployments-deleting.md "blue-green-deployments-deleting.md").

After switchover, the previous production environment isn't deleted so that you can use it for regression
testing, if necessary.

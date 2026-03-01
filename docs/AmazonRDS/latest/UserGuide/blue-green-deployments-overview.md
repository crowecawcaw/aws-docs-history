# Overview of Amazon RDS Blue/Green Deployments

By using Amazon RDS Blue/Green Deployments, you can make and test database changes before
implementing them in a production environment. A _blue/green deployment_
creates a staging environment that copies the production environment. In a blue/green
deployment, the _blue environment_ is the current production environment. The
_green environment_ is the staging environment and stays in sync with the
current production environment.

You can make changes to the RDS DB instances in the green environment without affecting production
workloads. For example, you can upgrade the major or minor DB engine version, upgrade the underlying file system configuration, or change
database parameters in the staging environment. You can thoroughly test changes in the green
environment. When ready, you can _switch over_ the environments to transition
the green environment to be the new production environment. The switchover typically takes under
a minute with no data loss and no need for application changes.

Because the green environment is a copy of the topology of the
production environment, the green environment includes the features used by the DB instance.
These features include the read replicas, the storage configuration, DB snapshots, automated backups,
Performance Insights, and Enhanced Monitoring. If the blue DB instance is a Multi-AZ DB instance
deployment, then the green DB instance is also a Multi-AZ DB instance deployment.

###### Note

Currently, blue/green deployments are supported only for RDS for MariaDB, RDS for MySQL, and
RDS for PostgreSQL. For Amazon Aurora availability, see [Overview of Amazon Aurora Blue/Green
Deployments](../AuroraUserGuide/blue-green-deployments-overview.md "../AuroraUserGuide/blue-green-deployments-overview.md") in the _Amazon Aurora User Guide_.

Under certain conditions, RDS for PostgreSQL uses logical replication instead of physical
replication to keep the green environment in sync with the blue environment. For more
information, see [PostgreSQL replication methods for blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

###### Topics

- [Region and version availability](#blue-green-deployments-region-version-availability "#blue-green-deployments-region-version-availability")
- [Benefits of using Amazon RDS Blue/Green Deployments](#blue-green-deployments-benefits "#blue-green-deployments-benefits")
- [Workflow of a blue/green deployment](#blue-green-deployments-major-steps "#blue-green-deployments-major-steps")
- [Authorizing access to Amazon RDS blue/green deployment operations](blue-green-deployments-authorizing-access.md "blue-green-deployments-authorizing-access.md")
- [Limitations and considerations for Amazon RDS blue/green deployments](blue-green-deployments-considerations.md "blue-green-deployments-considerations.md")
- [Best practices for Amazon RDS blue/green deployments](blue-green-deployments-best-practices.md "blue-green-deployments-best-practices.md")

## Region and version availability

Feature availability and support varies across specific versions of each database engine,
and across AWS Regions. For more information, see [Supported Regions and DB engines for Amazon RDS Blue/Green Deployments](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

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

Complete the following major steps when you use a blue/green deployment for database updates.

1. Identify a production environment that requires updates.

For example, the production environment in this image has a Multi-AZ DB instance deployment (mydb1) and
a read replica (mydb2).

![Production (blue) environment in a blue/green deployment](images/blue-green-deployment-blue-environment.png) 2. Create the blue/green deployment. For instructions, see [Creating a blue/green deployment in Amazon RDS](blue-green-deployments-creating.md "blue-green-deployments-creating.md").

The following image shows an example of a blue/green deployment of the production environment from step 1.
While creating the blue/green deployment, RDS copies the complete topology and configuration of the
primary DB instance to create the green environment. The copied DB instance names are appended
with `-green-`random-characters``. The staging environment in 
 the image contains a Multi-AZ DB instance deployment (mydb1-green-`_abc123_`) 
 and a read replica (mydb2-green-`_abc123_`).

![Blue/green deployment](images/blue-green-deployment.png)

When you create the blue/green deployment, you can upgrade your DB engine version
and specify a different DB parameter group for the DB instances in the green environment. RDS
also configures replication from the primary DB instance in the blue environment to the primary
DB instance in the green environment.

After you create the blue/green deployment, the DB instance in the green environment is read-only by default. 3. Make additional changes to the staging environment, if required. For example, you
might change the DB instance class used by one or more DB instances in the green environment.

For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). 4. Test your staging environment.

During testing, we recommend that you keep your databases in the green environment
read only. Enable write operations on the green environment with caution because they can
result in replication conflicts. They can also result in unintended data in the production
databases after switchover. To enable write operations for RDS for MySQL, set the
`read_only` parameter to `1`, and wait for the parameter group to synchronize.
Since `read_only` is a dynamic parameter, so a reboot isn't required.
Once synchronized, change `read_only` from `1` to `0`.
For RDS for PostgreSQL deployments that use logical replication, set the
`default_transaction_read_only` parameter to `off` at the session
level. For those that use physical replication, you can't enable write operations on the
green environment. 5. When ready, switch over to transition the staging environment to be the new
production environment. For instructions, see [Switching a blue/green deployment in Amazon RDS](blue-green-deployments-switching.md "blue-green-deployments-switching.md").

The switchover results in downtime. The downtime is usually under one minute, but it can be longer depending
on your workload.

The following image shows the DB instances after the switchover.

![DB instances after switching over a blue/green deployment](images/blue-green-deployment-switchover.png)

After the switchover, the DB instances that were in the green environment become the new
production DB instances. The names and endpoints in the current production environment are
assigned to the newly switched over production environment, requiring no changes to your
application. As a result, your production traffic now flows to the new production
environment. The DB instances in the previous blue environment are renamed by appending
`-old`n`to the current name, where
`n``is a number. For example, assume the name of
 the DB instance in the blue environment is`mydb1`. After switchover, the DB instance name
 will be `mydb1-old1`.

In the example in the image, the following changes occur during switchover:

    * The green environment Multi-AZ DB instance deployment named `mydb1-green-abc123` becomes the production
     Multi-AZ DB instance deployment named `mydb1`.
    * The green environment read replica named `mydb2-green-abc123` becomes the production read replica
     `mydb2`.
    * The blue environment Multi-AZ DB instance deployment named `mydb1` becomes `mydb1-old1`.
    * The blue environment read replica named `mydb2` becomes `mydb2-old1`.

6. If you no longer need a blue/green deployment, you can delete it. For instructions, see
   [Deleting a blue/green deployment in Amazon RDS](blue-green-deployments-deleting.md "blue-green-deployments-deleting.md").

After switchover, the previous production environment isn't deleted so that you can use it for regression
testing, if necessary.

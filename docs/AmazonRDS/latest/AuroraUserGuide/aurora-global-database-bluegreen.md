# Using Blue/Green Deployments for Amazon Aurora Global Database

Amazon RDS Blue/Green Deployments provide a capability for testing database changes safely.
For your global database, blue/green deployments allow you to perform upgrades and maintenance operations with minimal downtime.
You can create a fully managed staging environment (green) that mirrors your entire production environment (blue), including the primary cluster
and all associated secondary regions across multiple AWS Regions. The staging environment reflects your production setup,
enabling you to reliably test changes before switching over to the new environment. Throughout the process, blue/green deployments
keep the staging and production environments in sync. When ready to make your staging environment the new production environment, perform
a blue/green switchover. This operation transitions your primary and all secondary regions to the green environment, with downtime typically
under one minute. The service automatically renames clusters, instances, and endpoints to match the original production environment, enabling
your applications to access the new production environment without requiring any configuration changes and minimizing operational overhead.

###### Topics

- [Benefits of using Blue/Green Deployments with Aurora Global Database](#aurora-blue-green-benefits "#aurora-blue-green-benefits")
- [How Blue/Green Deployments work with Aurora Global Database](#aurora-blue-green-howitworks "#aurora-blue-green-howitworks")

## Benefits of using Blue/Green Deployments with Aurora Global Database

- Perform major version, minor version, and system updates including database patches and OS upgrades on Aurora Global Databases,
  while maintaining minimal downtime.
- Create a production-ready staging (green) environment in both primary and secondary regions of the global database to test and implement newer database features.
- Switchover safely using built-in switchover guardrails with downtime typically under one minute, depending on your workload.
- Maintains disaster recovery capabilities during the Blue/Green switchover process, allowing Global Database failover during the Blue/Green switchover.
- Your traffic will be directed to the new production environment without requiring any application changes.

## How Blue/Green Deployments work with Aurora Global Database

For details on how to create, view, switch, and delete
a Blue/Green Deployment, see [Using Amazon Aurora Blue/Green Deployments for database updates](blue-green-deployments.md "blue-green-deployments.md"). You can use this for major or minor version upgrades, database performance improvements through parameter updates, and adoption of new database features, with minimal downtime.

A representation of how a blue/green deployment for Aurora Global Database with one secondary region looks before and after a blue/green switchover is shown below.

![An example of a Blue/Green deployment for Aurora Global Database.](images/Aurora Global Database_Blue_Green_example.png)

You can create a blue/green deployment from the primary Region of your Global Database. Select the engine configurations such as major or minor Engine version, DB Parameter group, and DB cluster Parameter group for the green environment. Amazon RDS copies the blue environment's topology for the green environment. A visual representation in AWS Management Console is as shown below.

![Summary of a Blue/Green Deployment.](images/auroraglobaldatabase_bluegreen.png)

###### Note

Global failover is supported during a blue/green switchover, but Global switchover is not supported during a blue/green switchover.

When you initiate a global failover during an RDS blue/green switchover, the target region automatically
rolls back to the blue environment or rolls forward to the green environment before the global failover occurs.

For information on creating, viewing, switching, and deleting blue/green deployments, see
[Using Amazon Aurora Blue/Green Deployments for database updates](blue-green-deployments.md "blue-green-deployments.md").
Follow the same workflow for Global Databases, with specific instructions noted in the relevant steps.

# Using Amazon RDS Blue/Green Deployments

for database updates

A blue/green deployment copies a production database environment to a separate,
synchronized staging environment. By using Amazon RDS Blue/Green Deployments, you
can make changes to the database in the staging environment without affecting the production
environment. For example, you can upgrade the major or minor DB engine version or change
database parameters in the staging environment. When you're ready, you can promote the
staging environment to be the new production database environment, with downtime typically
under one minute.

###### Note

Currently, Blue/Green Deployments are supported for RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL only. For Amazon Aurora availability, see
[Using Amazon Aurora
Blue/Green Deployments for database updates](../AuroraUserGuide/blue-green-deployments.md "../AuroraUserGuide/blue-green-deployments.md") in the _Amazon Aurora
User Guide_.

###### Topics

- [Overview of Amazon RDS Blue/Green Deployments](blue-green-deployments-overview.md "blue-green-deployments-overview.md")
- [Creating a blue/green deployment in Amazon RDS](blue-green-deployments-creating.md "blue-green-deployments-creating.md")
- [Viewing a blue/green deployment in Amazon RDS](blue-green-deployments-viewing.md "blue-green-deployments-viewing.md")
- [Switching a blue/green deployment in
  Amazon RDS](blue-green-deployments-switching.md "blue-green-deployments-switching.md")
- [Deleting a blue/green deployment in Amazon RDS](blue-green-deployments-deleting.md "blue-green-deployments-deleting.md")

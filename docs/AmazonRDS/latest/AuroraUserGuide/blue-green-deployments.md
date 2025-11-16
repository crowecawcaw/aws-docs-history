# Using Amazon Aurora Blue/Green Deployments

for database updates

A blue/green deployment copies a production database environment to a separate,
synchronized staging environment. By using Amazon Aurora Blue/Green Deployments, you
can make changes to the database in the staging environment without affecting the production
environment. For example, you can upgrade the major or minor DB engine version or change
database parameters in the staging environment. When you're ready, you can promote the
staging environment to be the new production database environment, with downtime typically
under one minute.

Amazon Aurora creates the staging environment by _cloning_ the underlying Aurora storage volume in the production environment.
The cluster volume in the staging environment only stores incremental changes made to that
environment.

###### Note

Currently, Blue/Green Deployments are supported for
Aurora MySQL, Aurora PostgreSQL, and Aurora Global Database. For Amazon RDS engine availability,
see [Using Amazon RDS Blue/Green
Deployments for database updates](../UserGuide/blue-green-deployments.md "../UserGuide/blue-green-deployments.md") in the _Amazon RDS User
Guide_.

###### Topics

- [Overview of Amazon Aurora Blue/Green Deployments](blue-green-deployments-overview.md "blue-green-deployments-overview.md")
- [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md "blue-green-deployments-creating.md")
- [Viewing a blue/green deployment in Amazon Aurora](blue-green-deployments-viewing.md "blue-green-deployments-viewing.md")
- [Switching a blue/green deployment in
  Amazon Aurora](blue-green-deployments-switching.md "blue-green-deployments-switching.md")
- [Deleting a blue/green deployment in Amazon Aurora](blue-green-deployments-deleting.md "blue-green-deployments-deleting.md")

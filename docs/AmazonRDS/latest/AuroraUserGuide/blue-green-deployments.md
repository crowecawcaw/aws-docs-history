

# Using Amazon Aurora Blue/Green Deployments for database updates
<a name="blue-green-deployments"></a>

A blue/green deployment copies a production database environment to a separate, synchronized staging environment. By using Amazon Aurora Blue/Green Deployments, you can make changes to the database in the staging environment without affecting the production environment. For example, you can upgrade the major or minor DB engine version or change database parameters in the staging environment. When you're ready, you can promote the staging environment to be the new production database environment, with downtime typically under one minute.

Amazon Aurora creates the staging environment by *cloning* the underlying Aurora storage volume in the production environment. The cluster volume in the staging environment only stores incremental changes made to that environment. 

**Note**  
Currently, Blue/Green Deployments are supported for Aurora MySQL, Aurora PostgreSQL, and Aurora Global Database. For Amazon RDS engine availability, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide*. 

**Topics**
+ [Overview of Amazon Aurora Blue/Green Deployments](blue-green-deployments-overview.md)
+ [Creating a blue/green deployment in Amazon Aurora](blue-green-deployments-creating.md)
+ [Viewing a blue/green deployment in Amazon Aurora](blue-green-deployments-viewing.md)
+ [Switching a blue/green deployment in Amazon Aurora](blue-green-deployments-switching.md)
+ [Deleting a blue/green deployment in Amazon Aurora](blue-green-deployments-deleting.md)
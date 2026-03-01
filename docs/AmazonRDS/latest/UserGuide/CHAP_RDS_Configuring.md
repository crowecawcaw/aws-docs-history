# Configuring an Amazon RDS DB instance

This section shows how to set up your Amazon RDS DB instance. Before creating a DB instance, decide on the DB instance class that will run the DB instance.
Also, decide where the DB instance will run by choosing an AWS Region. Next, create the DB instance.

You can configure a DB instance with an option group and a DB parameter group.

- An _option group_ specifies features, called options,
  that are available for a particular Amazon RDS DB instance.
- A _DB parameter group_ acts as a container for engine configuration
  values that are applied to one or more DB instances.
  The options and parameters that are available depend on the DB engine and DB engine
  version. You can specify an option group and a DB parameter group when you create a DB
  instance. You can also modify a DB instance to specify them.

###### Topics

- [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md")
- [Creating Amazon RDS resources with AWS CloudFormation](creating-resources-with-cloudformation.md "creating-resources-with-cloudformation.md")
- [Connecting to an Amazon RDS DB instance](CHAP_CommonTasks.md "CHAP_CommonTasks.md")
- [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md")
- [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")
- [Creating an Amazon ElastiCache cache using Amazon RDS DB instance settings](creating-elasticache-cluster-with-RDS-settings.md "creating-elasticache-cluster-with-RDS-settings.md")
- [Auto migrating EC2 databases to Amazon RDS using AWS Database Migration Service](USER_DMS_migration.md "USER_DMS_migration.md")
- [Tutorial: Creating a MySQL DB instance with a custom parameterand new option group](tutorial-creating-custom-OPG.md "tutorial-creating-custom-OPG.md")

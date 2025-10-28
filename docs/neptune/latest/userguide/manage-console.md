# Managing Your Amazon Neptune Database

This section shows how to manage and maintain your Neptune DB cluster
using the AWS Management Console and the AWS CLI.

Neptune operates on clusters of database servers that are connected in a replication
topology. Thus, managing Neptune often involves deploying changes to multiple servers and
making sure that all Neptune replicas are keeping up with the primary server.

Because Neptune transparently scales the underlying storage as your data grows, managing
Neptune requires relatively little management of disk storage. Likewise, because Neptune
automatically performs continuous backups, a Neptune cluster does not require extensive planning
or downtime for performing backups.

###### Topics

- [Using the Neptune Blue/Green solution to perform blue-green updates](neptune-BG-deployments.md "neptune-BG-deployments.md")
- [Creating an IAM user with permissions for Neptune](manage-console-iam-user.md "manage-console-iam-user.md")
- [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md")
- [Amazon Neptune parameters](parameters.md "parameters.md")
- [Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md "manage-console-launch-console.md")
- [Stopping and starting an Amazon Neptune DB cluster](manage-console-stop-start.md "manage-console-stop-start.md")
- [Empty an Amazon Neptune DB cluster using the fast reset API](manage-console-fast-reset.md "manage-console-fast-reset.md")
- [Adding Neptune reader instances to a DB Cluster](manage-console-add-replicas.md "manage-console-add-replicas.md")
- [Creating a Neptune reader instance using the console](manage-console-create-replica.md "manage-console-create-replica.md")
- [Modifying a Neptune DB Cluster Using the
  Console](manage-console-modify.md "manage-console-modify.md")
- [Performance and Scaling in Amazon Neptune](manage-console-performance-scaling.md "manage-console-performance-scaling.md")
- [Auto-scaling the number of replicas in an Amazon Neptune DB cluster](manage-console-autoscaling.md "manage-console-autoscaling.md")
- [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md "cluster-maintenance.md")
- [Using a AWS CloudFormation template to update the engine
  version of your Neptune DB Cluster](cfn-engine-update.md "cfn-engine-update.md")
- [Database Cloning in Neptune](manage-console-cloning.md "manage-console-cloning.md")
- [Managing Amazon Neptune Instances](manage-console-instances.md "manage-console-instances.md")

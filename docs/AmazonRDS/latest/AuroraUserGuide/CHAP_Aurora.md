# Managing an Amazon Aurora DB cluster

This section shows how to manage and maintain your Aurora DB cluster.
Aurora involves clusters of database servers that are connected in a replication topology. Thus,
managing Aurora often involves deploying changes to multiple servers and making sure that all
Aurora Replicas are keeping up with the source server. Because Aurora transparently scales
the underlying storage as your data grows, managing Aurora requires relatively little management
of disk storage. Likewise, because Aurora automatically performs continuous backups, an Aurora
cluster does not require extensive planning or downtime for performing backups.

###### Topics

- [Stopping and starting an Amazon Aurora DB cluster](aurora-cluster-stop-start.md "aurora-cluster-stop-start.md")
- [Automatically connecting an EC2 instance and an Aurora DB cluster](ec2-rds-connect.md "ec2-rds-connect.md")
- [Automatically connecting a Lambda function and an Aurora DB cluster](lambda-rds-connect.md "lambda-rds-connect.md")
- [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md")
- [Adding Aurora Replicas to a DB cluster](aurora-replicas-adding.md "aurora-replicas-adding.md")
- [Managing performance and scaling for Aurora DB
  clusters](Aurora.Managing.md "Aurora.Managing.md")
- [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md")
- [Integrating Aurora with other AWS services](Aurora.md "Aurora.md")
- [Maintaining an Amazon Aurora DB cluster](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](USER_RebootCluster.md "USER_RebootCluster.md")
- [Failing over an Amazon Aurora DB cluster](aurora-failover.md "aurora-failover.md")
- [Deleting Aurora DB clusters and DB instances](USER_DeleteCluster.md "USER_DeleteCluster.md")
- [Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md")
- [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md")
- [Amazon Aurora updates](Aurora.md "Aurora.md")

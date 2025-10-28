# Viewing retained automated backups for Amazon Aurora

To view your retained automated backups in the RDS console, choose **Automated backups** in the
navigation pane, then choose **Retained**. To view individual snapshots associated with a retained
automated backup, choose **Snapshots** in the navigation pane. Alternatively, you can describe individual
snapshots associated with a retained automated backup. From there, you can restore a DB instance directly from one of those
snapshots.

To describe your retained automated backups using the AWS CLI, use the following command:

```
aws rds describe-db-cluster-automated-backups --db-cluster-resource-id `DB_cluster_resource_ID`
```

To describe your retained automated backups using the RDS API, call the [`DescribeDBClusterAutomatedBackups`](../APIReference/API_DescribeDBClusterAutomatedBackups.md "../APIReference/API_DescribeDBClusterAutomatedBackups.md")
action with the `DbClusterResourceId` parameter.

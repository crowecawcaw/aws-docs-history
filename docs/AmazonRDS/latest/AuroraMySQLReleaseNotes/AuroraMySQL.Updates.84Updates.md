

# Database engine updates for Amazon Aurora MySQL version 8.4
<a name="AuroraMySQL.Updates.84Updates"></a>

The following are database engine updates for Amazon Aurora MySQL version 8.4.

**Topics**<a name="aurora_84_updates"></a>
+ [Aurora MySQL 8.4.10](AuroraMySQL.Updates.8410.md)
+ [Aurora MySQL 8.4.8](AuroraMySQL.Updates.848.md)
+ [Aurora MySQL 8.4.7](AuroraMySQL.Updates.847.md)
+ [About patch releases](#AuroraMySQL.Updates.84Updates.PatchReleases)

## About patch releases
<a name="AuroraMySQL.Updates.84Updates.PatchReleases"></a>

Aurora MySQL version 8.4 delivers critical stability and security fixes for a minor version as patch releases. A patch release doesn't change the engine version that you see in the AWS Management Console or the Amazon RDS API. For example, a cluster on 8.4.7.1 still shows the engine version `8.4.mysql_aurora.8.4.7`. To check the patch level that a DB instance runs, use the following query.

```
SELECT @@aurora_version;
```

Aurora doesn't apply patches to existing clusters automatically. When a patch is available, a `system-update` pending maintenance action appears for your cluster. You can apply it immediately or during your next maintenance window. In the AWS Management Console, choose **Maintenance & backups**, and then find the action under **Pending maintenance**. With the AWS CLI, use the following command.

```
aws rds apply-pending-maintenance-action \
    --resource-identifier {{cluster-arn}} \
    --apply-action system-update \
    --opt-in-type immediate
```

To apply the patch during your next maintenance window instead, use `--opt-in-type next-maintenance`. For more information, see [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

New clusters and restored clusters use the latest available patch for the minor version. Patches are cumulative, and you can't revert a cluster to an earlier patch.
# Upgrading Amazon Aurora DB clusters

With Amazon Aurora, you can control and test upgrades to your DB clusters. Amazon Aurora provides
options for automatic minor version upgrades, manual upgrade control, required upgrades, and
pre-upgrade testing. You can keep your clusters up-to-date with the latest minor version,
deferring non-critical upgrades, forcing upgrades for serious issues, and validating upgrade
behavior in nonproduction environments. The following sections detail how to manage and test
Aurora DB cluster upgrades using these capabilities.

## Automatic minor version upgrades for

Aurora

Automatic minor version upgrades periodically update your
database to recent database engine versions. However, the upgrade might
not always include the latest database engine version. If you need to
keep your databases on specific versions at particular times,
we recommend that you manually upgrade to the database versions that
you need according to your required schedule.
In cases of critical security issues or when a version reaches its end-of-support date,
Amazon Aurora
might apply a minor version upgrade even if you haven't enabled the **Auto minor version upgrade**
option. For more information, see the upgrade documentation for your specific database engine.

See [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md")
and [Performing a minor
version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").

You can stay up to date with Aurora minor versions by turning on **Auto minor
version upgrade** for every DB instance in the Aurora cluster. Aurora performs the
automatic upgrade only if all DB instances in your cluster have this setting turned on.

If **Auto minor version upgrade** is **Yes** for your
DB cluster, Aurora upgrades automatically to the default minor version or to a newer minor
version. For example, if the default minor version is 15.8 for Aurora PostgreSQL 15, and version
15.10 exists, the target for the automatic upgrade could be either 15.8 or 15.10.

Aurora typically schedules automatic upgrades twice a year for DB clusters that have automatic
minor version upgrade enabled. These upgrades occur during the maintenance window that you
specify for your cluster. For more information, see [Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

Automatic minor version upgrades are communicated in advance through an Amazon RDS DB cluster
event with a category of `maintenance` and ID of `RDS-EVENT-0156`. For
more information, see [Amazon RDS event categories and event messages for Aurora](USER_Events.md "USER_Events.md").

## Manually controlling upgrades of your

DB clusters to new versions

If you have the **Auto minor version upgrade** setting enabled, Aurora
automatically upgrades your DB cluster to the default minor version or a newer minor
version. Aurora typically schedules automatic upgrades twice a year for DB clusters that have the
**Auto minor version upgrade** setting enabled. These upgrades are
started during customer-specified maintenance windows.

To turn off automatic minor version upgrades, disable **Auto minor version
upgrade** on any DB instance within an Aurora cluster. Aurora performs an automatic minor
version upgrade only if all DB instances in your cluster have the setting enabled.

###### Note

For mandatory upgrades such as minor-version end of life, Aurora upgrades the DB cluster
even if the **Auto minor version upgrade** setting is
disabled. You get a reminder but no RDS event notification. Aurora upgrades your cluster
occur within a maintenance window after the mandatory upgrade deadline has passed.

Because major version upgrades involve some compatibility risk, they don't occur
automatically. You must initiate these, except if there is a major version deprecation.
We recommend that you thoroughly test your applications with new database versions before
upgrading your cluster to a major version.

For more information about upgrading a DB cluster to a new Aurora major version, see
[Upgrading Amazon Aurora MySQL DB clusters](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md") and [Upgrading Amazon Aurora PostgreSQL DB
clusters](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

## Required Amazon Aurora upgrades

For certain critical fixes, Aurora might perform a managed upgrade to a newer patch level
within the same minor version. In this case, Aurora upgrades your cluster even if
**Auto minor version upgrade** is turned off. Before doing so, Aurora
communicates the detailed upgrade process. Details include the timing of certain milestones,
the impact on your DB clusters, and recommended actions. Such managed upgrades occur
automatically within the cluster maintenance window.

## Testing your DB cluster with a new

Aurora version before upgrading

You can test the upgrade process and how the new version works with your application and
workload. Use one of the following methods:

- Clone your cluster using the Amazon Aurora fast database clone feature. Perform the
  upgrade and any post-upgrade testing on the new cluster.
- Restore from a cluster snapshot to create a new Aurora cluster. You can create a
  cluster snapshot yourself from an existing Aurora cluster. Aurora also automatically
  creates periodic snapshots for you for each of your clusters. You can then initiate a
  version upgrade for the new cluster. You can experiment on the upgraded copy of your
  cluster before deciding whether to upgrade your original cluster.

For more information on these ways to create new clusters for testing, see [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md") and [Creating a DB cluster snapshot](USER_CreateSnapshotCluster.md "USER_CreateSnapshotCluster.md").

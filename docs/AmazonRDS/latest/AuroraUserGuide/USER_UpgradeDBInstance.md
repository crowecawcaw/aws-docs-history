# Upgrading Amazon Aurora PostgreSQL DB

clusters

Amazon Aurora makes new versions of the PostgreSQL database engine available in AWS Regions
only after extensive testing. You can upgrade your Aurora PostgreSQL DB clusters to the new version
when it's available in your Region.

Depending on the version of Aurora PostgreSQL that your DB cluster is currently running, an upgrade
to the new release is either a minor upgrade or a major upgrade. For example, upgrading an
Aurora PostgreSQL 11.15 DB cluster to Aurora PostgreSQL 13.6 is a _major version
upgrade_. Upgrading an Aurora PostgreSQL 13.3 DB cluster to Aurora PostgreSQL 13.7 is
a _minor version upgrade_. In the following topics, you can
find information about how to perform both types of upgrades.

###### Contents

- [Overview of the
  Aurora PostgreSQL upgrade processes](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Overview "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Overview")
- [Getting a list of
  available versions in your AWS Region](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [Performing a major
  version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
  - [Testing an upgrade of your production DB cluster to a new major version](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary")
  - [Post-upgrade recommendations](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.postupgrade "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.postupgrade")
  - [Upgrading the
    Aurora PostgreSQL engine to a new major version](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.Upgrading.Manual "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.Upgrading.Manual")
    - [Major upgrades for
      global databases](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.GlobalDB "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.GlobalDB")

- [Performing a minor
  version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
  - [Before performing a
    minor version upgrade](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.BeforeMinor "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.BeforeMinor")
  - [How to perform minor
    version upgrades and apply patches](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor")
  - [Minor release upgrades
    and zero-downtime patching](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp")
  - [Limitations of zero-downtime patching](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations")
  - [Upgrading the Aurora PostgreSQL
    engine to a new minor version](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.MinorUpgrade "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.MinorUpgrade")

- [Upgrading
  PostgreSQL extensions](USER_UpgradeDBInstance.Upgrading.md "USER_UpgradeDBInstance.Upgrading.md")
- [Alternative blue/green
  upgrade technique](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.BlueGreen "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.BlueGreen")

## Overview of the

Aurora PostgreSQL upgrade processes

The differences between major and minor version upgrades are as follows:

**Minor version upgrades and patches**

Minor version upgrades and patches include only those changes that are
backward-compatible with existing applications. Minor version upgrades and
patches become available to you only after Aurora PostgreSQL tests and approves
them.

Aurora can apply minor version upgrades for you automatically. When you
create a new Aurora PostgreSQL DB cluster, the **Enable minor version
upgrade** option is enabled by default. Unless you manually
turn off this option, Aurora periodically applies automatic minor version
upgrades during your scheduled maintenance window. For more information
about the automatic minor version upgrade (AmVU) option and how to modify
your Aurora DB cluster to use it, see [Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

If automatic minor version upgrade isn't enabled for your
Aurora PostgreSQL DB cluster, your Aurora PostgreSQL isn't automatically upgraded to
a new minor version. Instead, when a new minor version is released in your
AWS Region and your Aurora PostgreSQL DB cluster is running an older minor version,
Aurora prompts you to upgrade. It does so by adding a recommendation to the
maintenance tasks for your cluster.

Patches aren't considered an upgrade, and they aren't applied
automatically. Aurora PostgreSQL prompts you to apply any patches by adding a
recommendation to maintenance tasks for your Aurora PostgreSQL DB cluster. For more
information, see [How to perform minor
version upgrades and apply patches](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor").

###### Note

Patches that resolve security or other critical issues are also added
as maintenance tasks. However, these patches are required. Make sure to
apply security patches to your Aurora PostgreSQL DB cluster when they become
available in your pending maintenance tasks.

Auto minor version upgrades are performed to the default minor version.

The upgrade process involves the possibility of brief outages as each
instance in the cluster is upgraded to the new version. However, after
Aurora PostgreSQL versions 14.3.3, 13.7.3, 12.11.3, 11.16.3, 10.21.3 and other
higher releases of these minor versions and newer major versions, the
upgrade process uses the zero-downtime patching (ZDP) feature. This feature
minimizes outages, and in most cases completely eliminates them. For more
information, see [Minor release upgrades
and zero-downtime patching](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp"). For more
information on the supported features and limitations of ZDP, see [Limitations of zero-downtime patching](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations").

**Major version upgrades**

Unlike for minor version upgrades and patches, Aurora PostgreSQL doesn't
have an automatic major version upgrade option. New major PostgreSQL
versions might contain database changes that aren't backward-compatible
with existing applications. The new functionality can cause your existing
applications to stop working correctly.

To prevent any issues, we strongly recommend that you follow the process
outlined in [Testing an upgrade of your production DB cluster to a new major version](USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary "USER_UpgradeDBInstance.PostgreSQL.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Upgrade.preliminary") before upgrading the DB instances in your Aurora PostgreSQL DB clusters. First
ensure that your applications can run on the new version by following that
procedure. Then you can manually upgrade your Aurora PostgreSQL DB cluster to the new
version.

The upgrade process involves the possibility of brief outage when all the
instances in the cluster are upgraded to the new version. The preliminary
planning process also takes time. We recommend that you always perform
upgrade tasks during your cluster's maintenance window or when
operations are minimal. For more information, see [Performing a major
version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").

###### Note

Both minor version upgrades and major version upgrades might involve brief
outages. For that reason, we recommend strongly that you perform or schedule
upgrades during your maintenance window or during other periods of low
utilization.

Aurora PostgreSQL DB clusters occasionally require operating system updates. These updates
might include a newer version of glibc library. During such updates, we recommend you to
follow the guidelines as described in [Collations supported in
Aurora PostgreSQL](PostgreSQL-Collations.md "PostgreSQL-Collations.md").

## Alternative blue/green

upgrade technique

In some situations, your top priority is to perform an immediate switchover from the
old cluster to an upgraded one. In such situations, you can use a multistep process that
runs the old and new clusters side-by-side. Here, you replicate data from the old
cluster to the new one until you are ready for the new cluster to take over. For
details, see [Using Amazon Aurora Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

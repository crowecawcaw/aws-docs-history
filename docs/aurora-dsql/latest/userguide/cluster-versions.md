

# Cluster versions in Aurora DSQL

Every Aurora DSQL cluster runs a major version of Aurora DSQL, called its cluster version. You choose the version when you create a cluster, and you can later upgrade the cluster to a newer version. During an upgrade, the cluster runs both versions.

**Important**  
Choosing a version when you create a cluster, and upgrading a cluster's version, are currently in Preview. To use them, you must create an ephemeral cluster with the matching early-access feature: **Latest DSQL major version** to choose a newer version, or **Major version upgrades** to upgrade the cluster later. For more information, see [Early-access features and ephemeral clusters in Aurora DSQL](ephemeral-clusters.md).

## Major version releases
<a name="cluster-versions-mvr"></a>

Aurora DSQL names each major version release (MVR) in the format `MVR.{{YYYY}}.{{N}}`, where {{YYYY}} is the release year and {{N}} is the release number within that year. Each MVR is based on a PostgreSQL major version.

The following table lists each MVR, the PostgreSQL major version that it's based on, and its availability.


| Major version release | PostgreSQL major version | Availability | 
| --- | --- | --- | 
| MVR.2025.1 | 16 | Generally available | 
| MVR.2026.1 | 18 | Preview | 

To see your cluster's versions, open the cluster details page in the console. The **Cluster versions** section lists each version with its action and status. To see the PostgreSQL version of a connection, run `SHOW server_version;`.

## Trying a newer version on a new cluster
<a name="cluster-versions-try-new"></a>

To try a newer version without upgrading a cluster, create an ephemeral cluster on the desired version. When you create the cluster, under **Early-access features**, select **Latest DSQL major version** and choose a **Cluster lifetime**. Then choose the version under **Cluster version**. With this feature, the list shows only the versions that are in preview.

For the cluster's lifetime and other limits, see [Early-access features and ephemeral clusters in Aurora DSQL](ephemeral-clusters.md).

## Trying an upgrade to a newer version
<a name="cluster-versions-try-upgrade"></a>

To try upgrading to a newer version, create an ephemeral cluster with the **Major version upgrades** early-access feature. With this feature, Aurora DSQL offers the generally available versions, so the cluster starts on `MVR.2025.1`. You can then upgrade it to `MVR.2026.1` in place. For the upgrade process, see [Upgrading cluster versions in Aurora DSQL](version-upgrade.md).
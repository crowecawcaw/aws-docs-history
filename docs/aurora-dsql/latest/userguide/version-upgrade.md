

# Upgrading cluster versions in Aurora DSQL

You can upgrade a cluster to a newer Amazon Aurora DSQL major version in place, with zero downtime. During the upgrade, the cluster runs both versions over the same data, and clients can connect to either one. Existing connections keep running on the version they're on until you decommission that version. You choose when to move each client to the new version, and you can switch back until you finish the upgrade. For version names and how to see your cluster's version, see [Cluster versions in Aurora DSQL](cluster-versions.md).

**Important**  
Upgrading a cluster is a Preview feature. It requires an ephemeral cluster with the **Major version upgrades** early-access feature, which you select under **Early-access features** when you create the cluster. For more information, see [Early-access features and ephemeral clusters in Aurora DSQL](ephemeral-clusters.md).

## How an upgrade works
<a name="version-upgrade-overview"></a>

An upgrade has four steps. You start each one from the console.

1. **Upgrade** – In the console, choose **Upgrade version**. The new version then shows action **Allow** while Aurora DSQL checks that your schema works on it and prepares it. Aurora DSQL doesn't copy your data, so this step takes longer for larger schemas, not for more data. Your current version stays the default, and clients keep using it.

1. **Test, then switch the default** – When the new version is ready, connect to it by naming it in the connection (see [Connecting to a specific cluster version](#version-upgrade-connect)), and test your clients. Include tools and libraries that read the PostgreSQL system catalogs, because the catalogs differ between major versions. Then switch the default. New connections that don't name a version use the new version. Connections that name the previous version, and connections that are already open, keep working.

1. **Drain the previous version** – The previous version stops accepting new connections. Open connections keep running until they close or reach the maximum connection duration. Draining takes about 75 minutes, so that no connections are still active on the previous version when you decommission it.

1. **Decommission the previous version** – Aurora DSQL removes the previous version. Connections still open on it can no longer commit.

Until you decommission the previous version, you can switch the default back or cancel the upgrade. If you drained the previous version, you can do this after the drain completes.

During an upgrade, plan for the following:
+ You can't make schema changes, including an `ANALYZE` that you run yourself, from the start of the upgrade until decommissioning the previous version completes or a cancellation completes. Reads and writes keep working, and automatic statistics keep updating on both versions.
+ Starting or canceling an upgrade, and decommissioning the previous version, change the set of versions that the cluster runs. A transaction that's open at that moment can receive a `40001` `OC001` response. Retry it, as you would after any other OCC conflict. For more information, see [Concurrency control responses](working-with-concurrency-control.md#dsql-transaction-conflicts).
+ If you cancel an upgrade after the new version is ready, Aurora DSQL drains the new version the same way, so schema changes stay blocked for about 75 minutes after you cancel.

## Requirements
<a name="version-upgrade-requirements"></a>

To start a new upgrade, your cluster must meet the following requirements:
+ The cluster has the **Major version upgrades** early-access feature enabled.
+ The cluster is a single-Region cluster.
+ The cluster is **Active**, **Idle**, or **Inactive**.
+ The cluster has no upgrade in progress.
+ The cluster has a newer version available.

This Preview supports major version upgrades on single-Region ephemeral clusters.

Complete schema changes before starting an upgrade. During the upgrade, including while a version is draining, Aurora DSQL blocks schema changes such as `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, and `ANALYZE`. You can make schema changes again after decommissioning the previous version completes or a cancellation completes. Plan application validation to use existing tables and schemas.

Reads and writes remain available during the upgrade. If a transaction receives a `40001` response during an upgrade, retry it. For more information, see [Concurrency control responses](working-with-concurrency-control.md#dsql-transaction-conflicts).

### Permissions for version upgrades
<a name="version-upgrade-permissions"></a>

To change cluster versions, you must have both `dsql:UpdateCluster` and `dsql:UpdateClusterVersions` permissions on the cluster. Aurora DSQL requires the additional `dsql:UpdateClusterVersions` permission only to change a cluster's versions. Scope both permissions to the cluster's Amazon Resource Name (ARN).

These permissions let you allow a new version, retry activation, switch the default version, drain a version, decommission a version, and cancel an upgrade. You also need both permissions to revert a drain or switch the default back to the previous version.

For more information about policy actions, see [Policy actions for Aurora DSQL](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions).

## Upgrade workflow
<a name="version-upgrade-workflow"></a>

In these steps, V1 is your current version and V2 is the newer version. The following procedure walks through the steps, with testing and switching the default as separate stages, from V1 as **Default** to V2 as **Default**.

For retry and cancellation instructions, including cancellation after switching the default, see [Retrying or canceling an upgrade](#version-upgrade-retry-cancel).

**Important**  
After you decommission a version, you can't roll back to it.

**To upgrade a cluster version in the console**

1. 

**Allow the new version**

   On the cluster details page, choose **Actions**, **Upgrade version**. Review the current and new versions, and then choose **Upgrade**.

   This starts the allow operation. V2 has action **Allow** and status **In progress** while V1 remains the default. When the operation succeeds, V2's action remains **Allow** and its status becomes **Complete**. If it fails, the status becomes **Failed**; the console shows **Allow requested** with an error icon. See [Retrying or canceling an upgrade](#version-upgrade-retry-cancel) for retry and cancellation instructions.

1. 

**Validate the new version**

   When V2 has action **Allow** and status **Complete**, connect to it explicitly to validate queries and application behavior. Connections that don't request a version continue to use the current default. For instructions and a `psql` example, see [Connecting to a specific cluster version](#version-upgrade-connect).

1. 

**Switch the default version**

   In the **Cluster versions** section, choose **Switch default**. In the dialog, review the current and new default versions, and then choose **Switch default**.

   After the switch completes, new connections that don't request a version use the new default. Existing connections to V1 keep running. V1 has action **Allow**, and V2 has action **Default**. Both have status **Complete**.

   To keep an application on V1 until you're ready to move it, have it name V1 when it connects. For instructions, see [Connecting to a specific cluster version](#version-upgrade-connect).

1. 

**Drain the previous version**

   In the **Cluster versions** section, find the previous version's row. In its **Actions** column, choose **Drain version**. In the dialog, type **confirm**, and then choose **Drain**.

   V1 has action **Drain** and status **In progress** as it stops accepting new connections. Existing connections remain open until they close or reach the maximum connection duration. For the connection limit, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md).

   Allow approximately 75 minutes for draining. This waiting period can continue after existing connections have closed. Continue when V1 has action **Drain** and status **Complete**. V2 remains **Default** throughout this stage.

1. 

**Decommission the previous version**

   In the **Cluster versions** section, find the drained version's row. Choose **Actions**, **Decommission version**. In the dialog, type **confirm**, and then choose **Decommission**.

   V1 has action **Decommission** and status **In progress** while Aurora DSQL permanently removes it. V2 remains **Default**.

After decommissioning completes, your cluster runs only the new version as its default. The cluster overview shows the new version.

## Connecting to a specific cluster version
<a name="version-upgrade-connect"></a>

To validate the new version before switching the default, connect to the same cluster endpoint and pass `-c amzn-cluster-version={{version}}` in the PostgreSQL connection's `options` startup parameter. In the **Cluster versions** section, copy the version name from the new version's row after its action is **Allow** and its status is **Complete**. Use that name, such as `MVR.2026.1`.

With `psql`, set `PGOPTIONS` for the connection to supply this startup parameter. The following Bash example connects as `admin` using an IAM authentication token. Before running it, configure the AWS CLI credentials and `psql` as described in [Use the local CLI to access Aurora DSQL with the PostgreSQL interactive terminal (psql)](accessing-psql.md#accessing-sql-clients-psql-local). For the trusted root certificate used by `verify-full`, see [Configuring SSL/TLS certificates for Aurora DSQL connections](configure-root-certificates.md).

Replace the Region, cluster endpoint, version name, and root certificate path with your values. Use the same cluster endpoint for token generation and the connection.

```bash
PGPASSWORD="$(aws dsql generate-db-connect-admin-auth-token \
  --region {{us-east-1}} \
  --hostname {{your_cluster_endpoint}})" \
PGSSLMODE=verify-full \
PGSSLROOTCERT="{{/path/to/AmazonRootCA1.pem}}" \
PGOPTIONS="-c amzn-cluster-version={{MVR.2026.1}}" \
psql --host {{your_cluster_endpoint}} --username admin --dbname postgres
```

The example applies these environment variables only to that `psql` process. Selecting a version for a connection doesn't change the cluster's default version. To use the current default for a new connection, omit `amzn-cluster-version` from its startup options. If you set `PGOPTIONS` separately in your shell or application, remove the version option there too.

You can connect to a version on the cluster after its allow operation completes and while it remains available for connections. Drain and decommission operations stop the version from accepting new connections.

## Retrying or canceling an upgrade
<a name="version-upgrade-retry-cancel"></a>

### Retrying a failed allow operation
<a name="version-upgrade-retry"></a>

If V2 has action **Allow** and status **Failed**, V1 keeps action **Default** and status **Complete**. Choose **Allow requested** with the error icon to see the failure reason. Address the reported issue, then choose **Actions**, **Upgrade version** on the cluster details page. Choose **Upgrade** to retry the same version. V1 stays the default while V2 starts another activation attempt with action **Allow** and status **In progress**. When V2's status becomes **Complete**, continue with validation.

### Canceling before switching the default
<a name="version-upgrade-cancel-before-switch"></a>

You can cancel while V2's action is **Allow** and its status is **In progress**, **Complete**, or **Failed**. In the **Cluster versions** section, choose **Cancel upgrade**. In the dialog, type **confirm**, and then choose **Cancel upgrade**. V2 has action **Cancel** and status **In progress** while Aurora DSQL removes it. If V2's allow operation had completed, cancellation automatically drains and then decommissions it. Its existing connections remain open until they close or reach the maximum connection duration. You don't need to choose separate drain or decommission actions for V2. If V2's allow operation never completed, there are no connections to drain.

Aurora DSQL removes V2 when cancellation completes, and V1 remains **Default**.

### Canceling after switching the default
<a name="version-upgrade-cancel-after-switch"></a>

To cancel after switching the default to V2, first make V1 the default again. Cancellation then automatically drains and decommissions V2. Complete the following steps in the **Cluster versions** section:

1. If the previous version already has action **Allow** and status **Complete**, continue to the next step. If its action is **Drain**, wait until its status is **Complete**. Allow approximately 75 minutes for draining. Then choose **Actions**, **Revert drain** in that row. In the dialog, choose **Revert drain**. Continue when V1 has action **Allow** and status **Complete**.

1. Choose **Switch default** to make the previous version the default. In the dialog, choose **Switch default**. Wait for the switch to complete.

1. Choose **Cancel upgrade** to remove the new version. In the dialog, type **confirm**, and then choose **Cancel upgrade**.

Aurora DSQL removes V2 when cancellation completes, and V1 remains **Default**.

## Version upgrade process chart
<a name="version-upgrade-process"></a>

The chart shows testing and switching the default as separate stages: allowing the new version, validating application behavior, switching the default, draining the previous version, and decommissioning it. V1 remains the default during V2 preparation and validation. Failed V2 activation can be retried. Decommissioning V1 permanently completes the upgrade to V2.

Before the default switches, you can cancel V2 activation while its status is **In progress**, **Complete**, or **Failed**. Cancellation removes V2 and keeps V1 as the default. For a completed activation, cancellation automatically drains and decommissions V2. The retry arrow returns through **Starting state** to show that V1 remains the default. Retrying starts V2 preparation again.

For the chart's decision branches and version states, see [Validation result](#version-upgrade-activation-result) and [Chart states and transitions](#version-upgrade-chart-states). For a text walkthrough of the console steps, see [Upgrade workflow](#version-upgrade-workflow). For the retry and cancellation branches, see [Retrying or canceling an upgrade](#version-upgrade-retry-cancel).

In the chart, V1 represents your current version and V2 represents the newer version. `MVR.2025.1` is an example of the current version. Use the version names shown in your console when connecting to a specific version.

The chart uses short labels such as **Draining** and **Decommissioning**. Each version has an `action` and a separate `status`. The following state descriptions give both values. When a version has action **Allow** and status **Complete**, you can connect to it. During preparation, its status is **In progress**.

The chart labels the decision branches **Failed** and **Successful**. Every card includes written version or state labels. The following descriptions explain each state.

The following chart shows V2 activation branching into failed and successful outcomes, followed by validation, cutover, and V1 removal. The retry arrow returns through **Starting state**. The next activation attempt enters **Preparing**.

![V1 stays the default while V2 is prepared and validated. Failed V2 activation can be retried. After switching the default to V2, drain and permanently remove V1.](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/images/version-upgrade-process.png)


### Validation result
<a name="version-upgrade-activation-result"></a>

The **Validation result** card branches when V2 activation finishes. V1 keeps action **Default** and status **Complete** in both outcomes:
+ **Failed** – V2 has action **Allow** and status **Failed**. Read the failure reason in **Allow requested** and address the issue. Choose **Actions**, **Upgrade version**, then **Upgrade** to retry the same version. The retry arrow leads through **Starting state** to **Preparing**. V1 stays the default while V2 starts another activation attempt with action **Allow** and status **In progress**. You can instead choose **Cancel upgrade** to remove V2.
+ **Successful** – V2 has action **Allow** and status **Complete**. Connect explicitly to V2 and validate queries and application behavior. When you are ready, choose **Switch default** to enter the cutover phase. You can instead choose **Cancel upgrade** to remove V2 and keep V1 as the default.

For the complete retry and cancellation procedures, including cancellation while activation is in progress or after switching the default, see [Retrying or canceling an upgrade](#version-upgrade-retry-cancel).

### Chart states and transitions
<a name="version-upgrade-chart-states"></a>

The following list gives the actions and statuses for each state card. **Starting state** leads to **Preparing** and then to **Validation result**. The retry arrow returns through **Starting state** to **Preparing** for another activation attempt. The **Success** branch continues through **Action**, **Draining**, **Drained**, and **Upgrade complete**.

Starting state: Cluster on MVR.2025.1 (V1)  
V1 has action **Default** and status **Complete**.  
Before the first upgrade attempt, your cluster runs only V1. On retry, V2's failed activation starts again, and V1 stays the default.

Preparing: V2 activation in progress  
V1 has action **Default** and status **Complete**.  
V2 has action **Allow** and status **In progress**.

Failed: V2 upgrade failed  
V1 has action **Default** and status **Complete**.  
V2 has action **Allow** and status **Failed**.

Success: V2 activation complete  
V1 has action **Default** and status **Complete**.  
V2 has action **Allow** and status **Complete**.

Action: Switch default to V2  
V1 has action **Allow** and status **Complete**.  
V2 has action **Default** and status **Complete**.

Draining: V1 drain in progress  
V1 has action **Drain** and status **In progress**.  
V2 has action **Default** and status **Complete**.

Drained: V1 decommission in progress  
V1 has action **Decommission** and status **In progress**.  
V2 has action **Default** and status **Complete**.

Upgrade complete: V1 decommissioned, V2 is default  
After you decommission V1, your cluster runs only V2.  
V2 has action **Default** and status **Complete**.

After switching the default to V2, choose **Drain version** for V1. When V1 has action **Drain** and status **Complete**, choose **Decommission version** to enter the chart's **V1 decommission in progress** state and finalize the upgrade. After you decommission V1, your cluster runs only V2.
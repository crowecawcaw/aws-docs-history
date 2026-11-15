

# Upgrading a domain (console)
<a name="starting-upgrades"></a>

You can start an in-place upgrade or a clone-based upgrade from the console. For information about choosing a method, see [Choose an upgrade method](version-migration.md#upgrade-methods). Before you start either type of upgrade, [take a manual snapshot](managedomains-snapshots.md) of your domain. This snapshot serves as a backup that you can [restore on a new domain](managedomains-snapshot-restore.md) if you want to return to using the prior OpenSearch version.

## Start an upgrade
<a name="console-start"></a>

**To start an upgrade**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the navigation pane, under **Domains**, choose the domain that you want to upgrade.

1. Choose **Actions** and **Upgrade**.

1. For **Select upgrade version**, choose the version to upgrade to. To see older versions, turn on **Include older versions**.

1. (Optional) Choose **Check eligibility** to run the pre-upgrade check and find issues that could block the upgrade. You can stop after the check if you don't want to start an upgrade.

1. If you're upgrading to an OpenSearch version, the **Compatibility mode for legacy Elasticsearch clients** option appears. Some legacy Elasticsearch clients, such as Logstash, check the cluster version before connecting. If you select this option, OpenSearch reports its version as 7.10 to these clients so that they continue to work after the upgrade. You can disable this setting later.

1. For **Action**, choose **Upgrade domain in place** or **Upgrade using a cloned domain**. Then follow the steps in the section for that type of upgrade.

## In-place upgrade
<a name="console-in-place"></a>

If the cluster has dedicated master nodes, OpenSearch upgrades complete without downtime. However, a brief sub-second interruption (approximately 300ms) may occur during master node re-election. Otherwise, the cluster might be unresponsive for several seconds post-upgrade while it elects a master node.

**Important**  
Although an upgrade completes without downtime, it runs as a blue/green deployment. During the deployment, you might experience performance impact, such as increased latency or increased rejections for incoming requests. For more information, see [Performance impact of blue/green deployments](managedomains-configuration-changes.md#performance-impact-bluegreen).

**Warning**  
An in-place upgrade is irreversible and can't be paused or canceled. During the upgrade, you can't make configuration changes to the domain. Before you start, double-check that you want to proceed. To keep the option to roll back, choose **Upgrade using a cloned domain** instead.

**To start an in-place upgrade**

1. With **Upgrade domain in place** selected for **Action**, type `upgrade` in the confirmation field.

1. Choose **Upgrade**.

1. Check the **Status** on the domain dashboard to monitor the status of the upgrade.

## Clone-based upgrade
<a name="console-clone-based"></a>

A clone-based upgrade creates a cloned cluster of your domain on the target version while your domain keeps serving traffic from the primary cluster. You validate the cloned cluster, optionally send some read traffic to it, and then cut over when you're ready. You can cancel any time before cutover. If you keep the primary cluster, you can also roll back after cutover. For more information, see [How a clone-based upgrade works](version-migration.md#how-clone-based-works).

The console uses different names for some of these parts. The following table shows how they map to the terms in this guide.


| In the console | In this guide | 
| --- | --- | 
| Upgrade using a cloned domain | Clone-based upgrade | 
| Cloned domain, clone cluster, replica environment, new environment | Cloned cluster | 
| Primary, original domain, old environment | Primary cluster | 
| Cut over, switching over | Cutover | 
| Retain old environment after cutover, rollback window | Retention period | 

After cutover, the cloned cluster takes the place of the primary cluster and serves traffic through the same domain endpoint. The console describes this as promoting the cloned cluster to primary. In this guide and in the API, the cluster that you retain for rollback is still called the primary cluster.

### Start the upgrade
<a name="console-clone-start"></a>

**To start a clone-based upgrade**

1. With **Upgrade using a cloned domain** selected for **Action**, choose a setting for **Retain old environment after cutover**. The setting keeps the primary cluster for rollback:
   + **Disabled** (default) – OpenSearch Service deletes the primary cluster immediately after cutover, and you can't roll back.
   + **Enabled** – OpenSearch Service keeps the primary cluster for the number of hours that you enter in **Retention period**, so that you can roll back. For information about charges, see [Charges for upgrades](version-migration.md#upgrade-charges).

1. Type `upgrade` in the confirmation field, and then choose **Upgrade**.

1. Check the **Status** on the domain dashboard to monitor the status of the upgrade. When the cloned cluster is ready, a banner reads **Awaiting your action — the replica environment is ready for validation**, and **Configuration change status** shows **Awaiting user input**.

### Validate the cloned cluster
<a name="console-clone-validate"></a>

**To validate the cloned cluster**

1. On the domain page, under **Configuration change status**, choose **Manage upgrade**.

1. For **Action**, choose **Adjust read traffic**. The dialog box shows the current read traffic routing for the primary cluster and the cloned cluster.

1. Use the slider to set the percentage of read traffic to send to the cloned cluster, from 0% to 100%.

1. Choose **Apply read traffic split**.

1. Validate your applications against the cloned cluster, and review its cluster health alongside the primary cluster. For more information about validating, see [Validate the cloned cluster](clone-based-upgrade.md#clone-validate).

You can change the percentage as often as you like. Only read traffic is split. Writes always go to the primary cluster. To send all reads back to the primary cluster, set the slider to 0%.

### Cut over to the cloned cluster
<a name="console-clone-cutover"></a>

**To cut over to the cloned cluster**

1. Choose **Manage upgrade**.

1. For **Action**, choose **Cut over to {{version}}**, where {{version}} is the target version.

1. Under **Retain old environment after cutover**, choose **Disabled** or **Enabled**. If you choose **Enabled**, enter the retention period in hours.

1. Type `cutover` in the confirmation field, and then choose **Cut over to {{version}}**.

OpenSearch Service blocks writes while the cloned cluster catches up, and then moves traffic to the cloned cluster. Your domain endpoint doesn't change.

**Note**  
Writes are blocked until cutover completes.

### Cancel the upgrade before cutover
<a name="console-clone-cancel"></a>

**To cancel the upgrade**

1. Choose **Manage upgrade**.

1. For **Action**, choose **Cancel upgrade**. OpenSearch Service keeps the primary cluster and deletes the cloned cluster.

1. Type `cancel` in the confirmation field, and then choose **Cancel upgrade**.

You can cancel any time before cutover. Your domain stays as it was.

### After cutover
<a name="console-clone-after"></a>

After cutover, the domain runs on the target version. If you enabled **Retain old environment after cutover**, a banner reads **Rollback available** and shows the date and time when the old environment expires. **Configuration change status** also shows **Rollback available**, and the **Rollback window expires** field shows when the retention period ends. OpenSearch Service then deletes the primary cluster automatically, and you can no longer roll back. Before that time, you can roll back or delete the primary cluster. Choose **Manage upgrade** to see when OpenSearch Service deletes the primary cluster and to choose an action.

#### Roll back
<a name="console-clone-rollback"></a>

**To roll back to the primary cluster**

1. In the banner, choose **Rollback to {{version}}**, where {{version}} is the version of the primary cluster. You can also choose **Manage upgrade**, and then for **Action**, choose **Roll back to {{version}}**.

1. Type `rollback` in the confirmation field, and then choose **Confirm rollback**.

**Warning**  
**Data written after cutover will be lost**  
Rollback restores the retained old environment. Any data written to the domain after cutover will not be present unless you replay it manually.

#### Delete the primary cluster early
<a name="console-clone-delete"></a>

**To delete the primary cluster before the retention period ends**

1. Choose **Manage upgrade**.

1. For **Action**, choose **Delete old environment now**.

1. Type `delete` in the confirmation field, and then choose **Delete old environment**.

After you delete the primary cluster, you can no longer roll back.
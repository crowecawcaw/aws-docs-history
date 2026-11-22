

# Upgrading Amazon OpenSearch Service domains

**Note**  
OpenSearch and Elasticsearch version upgrades differ from service software updates. For information on updating the service software for your OpenSearch Service domain, see [Service software updates in Amazon OpenSearch Service](service-software.md).

Amazon OpenSearch Service offers two ways to upgrade a domain: an in-place upgrade and a clone-based upgrade. If you use services like Amazon Data Firehose or Amazon CloudWatch Logs to stream data to OpenSearch Service, check that these services support the newer version of OpenSearch before migrating.

## Upgrade methods and terms
<a name="upgrade-methods-terms"></a>

An **in-place upgrade** upgrades the existing cluster of your domain to the new version. It runs as a blue/green deployment. You can't pause, cancel, or roll back an in-place upgrade. It is available for domains that run OpenSearch 1.0 or later, or Elasticsearch 5.1 or later.

A **clone-based upgrade** creates a cloned cluster of your domain on the target version and keeps it in sync with your data while your domain keeps serving traffic from the primary cluster. It is a blue/green deployment in which the cloned cluster is the green environment, kept isolated so that you can validate it before you cut over. You validate the cloned cluster, and then cut over to it when you're ready. You can cancel before cutover and roll back after it. A clone-based upgrade is available for domains that run Elasticsearch 7.10 or OpenSearch 1.1 or later in all AWS Commercial Regions where Amazon OpenSearch Service is available, except Asia Pacific (New Zealand), Asia Pacific (Taipei), Asia Pacific (Thailand), and Mexico (Central). For a complete list of Regions, see the [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

The following terms describe a clone-based upgrade.

Primary cluster  
The cluster that your domain runs on when the upgrade starts, on the earlier version. It keeps serving traffic until you cut over. After cutover, OpenSearch Service keeps it only for the retention period you set, so that you can roll back.

Cloned cluster  
The new cluster that OpenSearch Service creates on the target version. It receives a copy of your data and stays in sync with the primary cluster.

Validate  
Test the cloned cluster with your own read requests before you cut over. You can validate reads only.

Cutover  
The step that moves your domain's traffic from the primary cluster to the cloned cluster. Writes are blocked during cutover.

Cancel  
Stop the upgrade before cutover. OpenSearch Service deletes the cloned cluster, and your domain stays as it was.

Roll back  
Return to the primary cluster after cutover, during the retention period.

Retention period  
How long OpenSearch Service keeps the primary cluster after cutover so that you can roll back. The period starts when cutover completes. If you don't set a retention period, OpenSearch Service deletes the primary cluster immediately after cutover.

## Choose an upgrade method
<a name="upgrade-methods"></a>

The following table compares the two types of upgrade.


|  | In-place upgrade | Clone-based upgrade | 
| --- | --- | --- | 
| How it works | Upgrades the existing cluster. It runs as a blue/green deployment. | A blue/green deployment in which the cloned cluster is the green environment. It is created on the target version, kept in sync with your data, and kept isolated so that you can validate it. You decide when to cut over. | 
| Available for | OpenSearch 1.0 or later, or Elasticsearch 5.1 or later. | Elasticsearch 7.10 or OpenSearch 1.1 or later. | 
| Try the upgraded version before it takes effect | No. The pre-upgrade checks run, but the upgraded cluster takes over as soon as the upgrade completes. | Yes. Try the cloned cluster with your own requests while your domain keeps serving traffic. | 
| Cancel an upgrade | No. | Yes. You can cancel any time before cutover. | 
| Roll back | No. To return to the earlier version, restore a snapshot on a new domain. | Yes. After cutover, you can roll back during the retention period you set. | 
| Writes during the upgrade | Write performance can degrade during the upgrade. | Writes to the primary cluster aren't affected while the upgrade runs. Writes are blocked until cutover completes. | 

For information about charges, see [Charges for upgrades](#upgrade-charges).

## Before you upgrade
<a name="before-you-upgrade"></a>

Before you start either type of upgrade:

1. [Take a manual snapshot](managedomains-snapshots.md) of your domain. This snapshot serves as a backup that you can [restore on a new domain](managedomains-snapshot-restore.md) if you want to return to using the prior OpenSearch version.

1. Check [Supported upgrade paths](#supported-upgrade-paths) for your current and target versions. A clone-based upgrade is available only for domains that run Elasticsearch 7.10 or OpenSearch 1.1 or later.

1. Run the pre-upgrade check to find issues that could block the upgrade. The same checks run for both types of upgrade. For more information, see [Troubleshooting validation failures](#upgrade-validation).

1. If your domains use managed disaster recovery, upgrade the secondary domain first and the primary domain last. Before a clone-based upgrade, remove the replication relationship. For more information, see [Upgrade domains that use DR](disaster-recovery.md#disaster-recovery-upgrade).

## Supported upgrade paths
<a name="supported-upgrade-paths"></a>

Currently, OpenSearch Service supports the following upgrade paths:

Every path in the following table is available for an in-place upgrade.


| From version | To version | 
| --- | --- | 
| OpenSearch 1.3, 2.x, or 3.x | OpenSearch 3.*x*<br />If you're running OpenSearch 1.3 or 2.x, you must first upgrade to OpenSearch 2.19 *before* upgrading to OpenSearch 3.x.<br />When upgrading from OpenSearch 2.19 to OpenSearch 3.x, you may need to address the following incompatible index settings. These were deprecated earlier in 2.x and will lead to an upgrade check validation failure if not removed.+  index.knn.algo\_param.ef\_construction <br />+  index.knn.algo\_param.m <br />+  index.knn.space\_type <br />+  index.store.hybrid.mmap.extensions <br />For more information about deprecated index settings and steps to remediate them, see [Index settings](https://docs.opensearch.org/2.6/search-plugins/knn/knn-index/#index-settings). For a complete list of breaking changes for OpenSearch 3.x, see [3.0.0](https://docs.opensearch.org/latest/breaking-changes/#300).<br />If your domain contains indexes created in OpenSearch 1.3, Elasticsearch 7.10, or earlier versions, you must reindex them before upgrading to OpenSearch 3.x. OpenSearch 3.x doesn't support these older indexes, regardless of whether they're in hot, UltraWarm, or cold storage. To reindex incompatible UltraWarm or cold indexes:1.  Migrate the indexes to hot storage. <br />2.  Reindex the data. <br />3.  Migrate the indexes back to warm or cold storage. <br />Alternatively, delete the indexes if you no longer need them.<br />Snapshots taken on OpenSearch 1.*x* and on Elasticsearch 7.10 and earlier versions are incompatible with OpenSearch 3.x.<br />For manual snapshot repositories, delete these incompatible snapshots before upgrading to OpenSearch 3.x. | 
| OpenSearch 1.3 or 2.x | OpenSearch 2.*x*<br />OpenSearch 2.17 will enable concurrent segment search by default with auto mode if the domain satisfies the following conditions:+  No previous concurrent search settings are explicitly set. <br />+  All data instances (hot and warm) are of instance type .2xl or more. <br />+  The average p90 cpu utilization on data instances (hot and warm) for more than 1 week is below 45%. <br />For more details about concurrent segment search settings here, see [Concurrent segment search](https://opensearch.org/docs/2.17/search-plugins/concurrent-segment-search/). <br />Version 2.3 has the following breaking changes:+  The `type` parameter was removed from all OpenSearch API endpoints in version 2.0. For more information, see the [breaking changes](https://opensearch.org/docs/latest/breaking-changes/). <br />+  If your domain contains any indexes (hot, UltraWarm, or cold) that were originally created in Elasticsearch 6.8, those indexes are not compatible with OpenSearch 2.3. <br />Before you upgrade to version 2.3, you must reindex the incompatible indexes. For incompatible UltraWarm or cold indexes, migrate them to hot storage, reindex the data, and then migrate them back to warm or cold storage. Alternately, you can delete the indexes if you no longer need them. <br />If you accidentally upgrade your domain to version 2.3 without performing these steps first, you won't be able to migrate the incompatible indexes out of their current storage tier. Your only option is to delete them.  | 
| OpenSearch 1.x | OpenSearch 1.x | 
| Elasticsearch 7.x | Elasticsearch 7.*x* or OpenSearch 1.*x* OpenSearch 1.*x* introduces numerous breaking changes. For details, see [Amazon OpenSearch Service rename - Summary of changes](rename.md).  | 
| Elasticsearch 6.8 | Elasticsearch 7.*x* or OpenSearch 1.*x* Elasticsearch 7.0 and OpenSearch 1.0 include numerous breaking changes. Before initiating an in-place upgrade, we recommend [taking a manual snapshot](managedomains-snapshots.md) of the 6.*x* domain, restoring it on a test 7.*x* or OpenSearch 1.*x* domain, and using that test domain to identify potential upgrade issues. For breaking changes in OpenSearch 1.0, see [Amazon OpenSearch Service rename - Summary of changes](rename.md). <br />Like Elasticsearch 6.*x*, indexes can only contain one mapping type, but that type must now be named `_doc`. As a result, certain APIs no longer require a mapping type in the request body (such as the `_bulk` API). <br />For new indexes, self-hosted Elasticsearch 7.*x* and OpenSearch 1.*x* have a default shard count of one. OpenSearch Service domains on Elasticsearch 7.*x* and later retain the previous default of five.  | 
| Elasticsearch 6.*x* | Elasticsearch 6.*x* | 
| Elasticsearch 5.6 | Elasticsearch 6.*x* Indexes created in version 6.*x* no longer support multiple mapping types. Indexes created in version 5.*x* still support multiple mapping types when restored into a 6.*x* cluster. Check that your client code creates only a single mapping type per index. <br />To minimize downtime during the upgrade from Elasticsearch 5.6 to 6.*x*, OpenSearch Service reindexes the `.kibana` index to `.kibana-6`, deletes `.kibana`, creates an alias named `.kibana`, and maps the new index to the new alias.  | 
| Elasticsearch 5.x | Elasticsearch 5.x | 

A clone-based upgrade is available for the following upgrade paths:
+ Elasticsearch 7.10 to OpenSearch 1.3
+ OpenSearch 1.1 to 1.3
+ OpenSearch 1.3 to 2.19
+ OpenSearch 2.*x* to 2.19
+ OpenSearch 2.19 to 3.*x*

For other upgrade paths, use an in-place upgrade.

## How an in-place upgrade works
<a name="how-in-place-works"></a>

An in-place upgrade consists of three steps:

1. **Pre-upgrade checks** – OpenSearch Service checks for issues that can block an upgrade and doesn't proceed to the next step unless these checks succeed.

1. **Snapshot** – OpenSearch Service takes a snapshot of the OpenSearch or Elasticsearch cluster and doesn't proceed to the next step unless the snapshot succeeds. If the upgrade fails, OpenSearch Service uses this snapshot to restore the cluster to its original state. For more information see [Can't downgrade after upgrade](handling-errors.md#troubleshooting-upgrade-snapshot).

1. **Upgrade** – OpenSearch Service starts the upgrade, which can take from 15 minutes to several hours to complete. OpenSearch Dashboards might be unavailable during some or all of the upgrade.

## How a clone-based upgrade works
<a name="how-clone-based-works"></a>

A clone-based upgrade consists of the following steps:

1. **Pre-upgrade checks** – OpenSearch Service runs the same checks as for an in-place upgrade and doesn't proceed unless they succeed.

1. **Snapshot** – OpenSearch Service takes a snapshot of your domain and doesn't proceed unless the snapshot succeeds.

1. **Cloned cluster creation** – OpenSearch Service creates a cloned cluster of your domain on the target version and copies your data to it. Your domain keeps serving reads and writes from the primary cluster, and the cloned cluster stays in sync with your data.

1. **Validation** – When the cloned cluster is ready, the upgrade waits for you. Validate the cloned cluster, and optionally send a share of read traffic to it.

1. **Cutover** – When you cut over, OpenSearch Service blocks writes until cutover completes. During that time, the cloned cluster catches up, and then OpenSearch Service moves traffic to it. Your domain endpoint doesn't change.

1. **Retention period (optional)** – OpenSearch Service keeps the primary cluster for the retention period you set, so you can roll back. The period starts when cutover completes. If you don't set a retention period, OpenSearch Service deletes the primary cluster immediately after cutover.

You can cancel the upgrade any time before cutover. OpenSearch Service then deletes the cloned cluster, and your domain stays as it was. For information about validating, cutting over, canceling, and rolling back, see [Validating, cutting over, and rolling back during a clone-based upgrade](clone-based-upgrade.md).

## Limitations of a clone-based upgrade
<a name="clone-based-limitations"></a>

A clone-based upgrade has the following limitations:
+ Your domain must run Elasticsearch 7.10 or OpenSearch 1.1 or later. If your domain runs an earlier version, use an in-place upgrade to reach a supported version first.
+ Domains that use OpenSearch Optimized instances (OR1 or OR2) aren't supported.
+ Domains that use UltraWarm instances aren't supported.
+ Domains that use cross-cluster replication aren't supported.
+ If your domain uses managed disaster recovery, remove the replication relationship before you start a clone-based upgrade, and set up disaster recovery again afterward. For more information, see [Upgrade domains that use DR](disaster-recovery.md#disaster-recovery-upgrade).
+ Domains with custom or third-party plugin packages associated aren't supported.
+ Domains that use SAML authentication for OpenSearch Dashboards aren't supported.
+ Domains that use Amazon Cognito authentication for OpenSearch Dashboards aren't supported.
+ You can't change the domain's configuration during the upgrade.

## Charges for upgrades
<a name="upgrade-charges"></a>

An in-place upgrade does not incur additional charges. In case of a clone-based upgrade, standard pricing will apply for the clone's instances and storage, like any other nodes in your domain. You are charged for both the primary cluster and the clone while you validate the clone. If you keep the primary cluster for rollback, you are charged for both until the retention period ends.

## Troubleshooting validation failures
<a name="upgrade-validation"></a>

When you initiate an OpenSearch or Elasticsearch version upgrade, OpenSearch Service first performs a series of validation checks to ensure that your domain is eligible for an upgrade. If any of these checks fail, you receive a notification containing the specific issues that you must fix before upgrading your domain. For a list of potential issues and steps to resolve them, see [Troubleshooting validation errors](managedomains-configuration-changes.md#validation).

## Troubleshooting an upgrade
<a name="upgrade-failures"></a>

Upgrades require healthy domains. Your domain might be ineligible for an upgrade or fail to upgrade for a wide variety of reasons. The following table shows the most common issues.


| Issue | Description | 
| --- | --- | 
| Optional plugin not supported | When you upgrade a domain with optional plugins, OpenSearch Service automatically upgrades the plugins as well. Therefore, the target version for your domain must also support these optional plugins. If the domain has an optional plugin installed that is not available for the target version, the upgrade request fails. | 
| Too many shards per node | OpenSearch, as well as 7.x versions of Elasticsearch, have a default setting of no more than 1,000 shards per node. If a node in your current cluster exceeds this setting, OpenSearch Service doesn't allow you to upgrade. See [Exceeded maximum shard limit](handling-errors.md#troubleshooting-shard-limit) for troubleshooting options. | 
| Domain in processing | The domain is in the middle of a configuration change. Check upgrade eligibility after the operation completes. | 
| Red cluster status | One or more indexes in the cluster is red. For troubleshooting steps, see [Red cluster status](handling-errors.md#handling-errors-red-cluster-status). | 
| High error rate | The cluster is returning a large number of 5xx errors when attempting to process requests. This problem is usually the result of too many simultaneous read or write requests. Consider reducing traffic to the cluster or scaling your domain. | 
| Split brain | Split brain means that your cluster has more than one master node and has split into two clusters that never will rejoin on their own. You can avoid split brain by using the recommended number of [dedicated master nodes](managedomains-dedicatedmasternodes.md). For help recovering from split brain, contact [Support](https://console.aws.amazon.com/support/home). | 
| Master node not found | OpenSearch Service can't find the cluster's master node. If your domain uses [multi-AZ](managedomains-multiaz.md), an Availability Zone failure might have caused the cluster to lose quorum and be unable to elect a new [master node](managedomains-dedicatedmasternodes.md). If the issue does not self-resolve, contact [Support](https://console.aws.amazon.com/support/home). | 
| Too many pending tasks | The master node is under heavy load and has many pending tasks. Consider reducing traffic to the cluster or scaling your domain. | 
| Impaired storage volume | The disk volume of one or more nodes isn't functioning properly. This issue often occurs alongside other issues, like a high error rate or too many pending tasks. If it occurs in isolation and doesn't self-resolve, contact [Support](https://console.aws.amazon.com/support/home). | 
| KMS key issue | The KMS key that is used to encrypt the domain is either inaccessible or missing. For more information, see [Monitoring domains that encrypt data at rest](encryption-at-rest.md#monitoring-ear). | 
| Snapshot in progress | The domain is currently taking a snapshot. Check upgrade eligibility after the snapshot finishes. Also check that you can list manual snapshot repositories, list snapshots within those repositories, and take manual snapshots. If OpenSearch Service is unable to check whether a snapshot is in progress, upgrades can fail. | 
| Snapshot timeout or failure | The pre-upgrade snapshot took too long to complete or failed. Check cluster health, and try again. If the problem persists, contact [Support](https://console.aws.amazon.com/support/home). | 
| Incompatible indexes | One or more indexes is incompatible with the target version. This problem can occur if you migrated the indexes from an older version of OpenSearch or Elasticsearch. Reindex the indexes and try again. | 
| High disk usage | Disk usage for the cluster is above 90%. Delete data or scale the domain, and try again. | 
| High JVM usage | JVM memory pressure is above 75%. Reduce traffic to the cluster or scale the domain, and try again. | 
| OpenSearch Dashboards alias problem | .dashboards is already configured as an alias and maps to an incompatible index, likely one from an earlier version of OpenSearch Dashboards. Reindex and try again. | 
| Red Dashboards status | OpenSearch Dashboards status is red. Try using Dashboards when the upgrade completes. If the red status persists, resolve it manually, and try again. | 
| Cross-cluster compatibility | You can only upgrade if cross-cluster compatibility is maintained between the source and destination domains after the upgrade. During the upgrade process, any incompatible connections are identified. To proceed, either upgrade the remote domain or delete the incompatible connections. Note that if replication is active on the domain, you can't resume it once you delete the connection.  | 
| Other OpenSearch Service service issue | Issues with OpenSearch Service itself might cause your domain to display as ineligible for an upgrade. If none of the preceding conditions apply to your domain and the problem persists for more than a day, contact [Support](https://console.aws.amazon.com/support/home). | 
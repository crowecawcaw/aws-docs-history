

# Validating, cutting over, and rolling back during a clone-based upgrade

After you start a clone-based upgrade, OpenSearch Service creates a cloned cluster of your domain and copies your data to it. When the cloned cluster is ready, the upgrade waits for you. This page explains how to validate the cloned cluster, cut over to it, cancel the upgrade, and roll back. For information about the requests that perform each action, see [Upgrading a domain (CLI)](starting-upgrades-cli.md) and [Upgrading a domain (SDK)](starting-upgrades-sdk.md).

## Monitor progress
<a name="clone-monitor"></a>

To track a clone-based upgrade, call `DescribeDomainChangeProgress`. The response lists the following stages. The stages refer to the cloned cluster as the *new environment* and to the primary cluster as the *old environment*.


| Stage | What it means | 
| --- | --- | 
| Initializing | OpenSearch Service initializes the upgrade. | 
| Validation | OpenSearch Service checks that your domain is eligible for the upgrade. | 
| Creating a new environment | OpenSearch Service creates the cloned cluster. | 
| Provisioning new nodes | OpenSearch Service creates the cloned cluster's nodes. | 
| Replicating data | OpenSearch Service replicates your data to the cloned cluster. | 
| Customer application validation | The cloned cluster is ready. After preparation, test your application on the new version before deciding whether to cut over. The upgrade waits for you. | 
| Traffic shift | OpenSearch Service sends the share of read traffic that you chose to the cloned cluster. | 
| Cut-over to new environment | OpenSearch Service cuts over to the cloned cluster. | 
| Complete upgrade | OpenSearch Service finishes the upgrade. | 
| Deleting older resources | OpenSearch Service deletes the resources associated with the old environment. | 

While the cloned cluster waits for you, the `ConfigChangeStatus` is `PendingUserInput`. The response also includes `TrafficSplit`, which shows the share of read traffic that goes to the primary cluster and to the cloned cluster.

## Validate the cloned cluster
<a name="clone-validate"></a>

While the upgrade waits, your domain keeps serving traffic from the primary cluster. Writes always go to the primary cluster, so you can validate reads only. Use any of the following methods.

### Send a share of read traffic to the cloned cluster
<a name="clone-validate-traffic"></a>

Use `UpdateClone` with `TrafficSplitOptions` to send a percentage of read requests, from 0 to 100, to the cloned cluster. The percentage applies to search requests, such as `_search`, `_msearch`, `_count`, and `_mget`. Other requests, including all writes, go to the primary cluster. You can change the percentage as often as you like. Set it to 0 to send all reads back to the primary cluster.

### Use OpenSearch Dashboards on the cloned cluster
<a name="clone-validate-dashboards"></a>

If your domain runs OpenSearch, open the cloned cluster's OpenSearch Dashboards at `https://{{my-domain-endpoint}}/_dashboards/clone`. To run the same queries on the primary cluster, use the standard Dashboards URL, `https://{{my-domain-endpoint}}/_dashboards`.

The `clone` URL is available only until you cut over. After cutover, the cloned cluster takes the place of the primary cluster, and you use the standard Dashboards URL.

### Compare CloudWatch metrics
<a name="clone-validate-metrics"></a>

The cloned cluster publishes metrics to the same CloudWatch namespace as your domain. Each metric name starts with `Clone.`, for example `Clone.CPUUtilization`. Monitor these metrics in CloudWatch to compare how your workload performs on the primary cluster (the earlier version) and the cloned cluster (the target version) before you decide to cut over. For a complete list of metrics, see [Clone-based upgrade metrics](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-clone-upgrade).

## Cut over to the cloned cluster
<a name="clone-cutover"></a>

When you're satisfied with the cloned cluster, cut over to it with `UpdateClone` and `CutoverOptions` set to `ClonedCluster`. OpenSearch Service then does the following:

1. Checks the health of both clusters. If either cluster has a red status, OpenSearch Service rejects the cutover.

1. Blocks writes to the primary cluster so that the cloned cluster can catch up. Reads stay available.

1. Waits for the cloned cluster to catch up. If the cloned cluster doesn't catch up within 5 minutes, OpenSearch Service unblocks writes and the cutover fails.

1. Moves traffic to the cloned cluster. Your domain endpoint doesn't change.

1. Deletes the primary cluster immediately, or keeps it for the retention period you set.

**Important**  
Writes are blocked until cutover completes. Cut over during a period of low write traffic.

## Cancel the upgrade before cutover
<a name="clone-cancel"></a>

You can cancel at any time before you cut over. Call `UpdateClone` with `CutoverOptions` set to `PrimaryCluster`. OpenSearch Service deletes the cloned cluster, and your domain stays as it was. A cluster with a red status doesn't block a cancel.

## Retention period
<a name="clone-retention"></a>

The retention period is how long OpenSearch Service keeps the primary cluster after cutover so that you can roll back. If you don't set a retention period, OpenSearch Service deletes the primary cluster immediately after cutover, and the only way to return to the earlier version is to restore a snapshot on a new domain.
+ The maximum retention period is 336 hours (14 days). To request a longer period, contact [AWS Support](https://aws.amazon.com/premiumsupport/).
+ You can set it when you start the upgrade, or in a separate call before cutover. The period counts from when the cutover completes.
+ After cutover, you can shorten or extend the period with `RetentionInHours`.
+ To end the period early, call `UpdateClone` with `RetentionAction`. Use `RollbackToPrimaryCluster` to return to the primary cluster and delete the cloned cluster. Use `DeletePrimaryCluster` to delete the primary cluster now.

## Roll back
<a name="clone-rollback"></a>

During the retention period, you can return to the primary cluster. Call `UpdateClone` with `RetentionAction` set to `RollbackToPrimaryCluster`. OpenSearch Service returns to the primary cluster and deletes the cloned cluster.

**Warning**  
**Data written after cutover will be lost**  
Rollback restores the retained old environment. Any data written to the domain after cutover will not be present unless you replay it manually.

## Charges
<a name="clone-charges"></a>

For information about charges, see [Charges for upgrades](version-migration.md#upgrade-charges).

## Troubleshooting
<a name="clone-troubleshooting"></a>


| Issue | Description | 
| --- | --- | 
| Cloned cluster creation fails | The stage that failed shows in the DescribeDomainChangeProgress response. The primary cluster isn't affected. | 
| Data copy fails | If the copy to the cloned cluster pauses or fails, the Replicating data stage fails. The primary cluster isn't affected. | 
| Cutover is rejected | One of the clusters has a red status. Fix the red indexes, and try again. | 
| Cutover fails after blocking writes | The cloned cluster didn't catch up within 5 minutes. OpenSearch Service unblocks writes automatically. Try again when write traffic is lower. | 
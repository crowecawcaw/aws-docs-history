

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Troubleshooting FSx for ONTAP issues
<a name="fsx-ontap-troubleshooting"></a>

This section covers common issues when using FSx for ONTAP as the target storage type with MGN.

**Topics**
+ [Troubleshooting FSx for ONTAP iSCSI connectivity](#fsx-iscsi-troubleshooting)
+ [FSx for ONTAP replication errors](#fsx-storage-timeout-troubleshooting)
+ [Failed to start data transfer](#fsx-failed-to-start-data-transfer)
+ [Not converging](#fsx-not-converging)
+ [Replication volume not deleted after Finalize cutover/Disconnect from service (FlexClone split blocked by backup)](#fsx-flexclone-split-blocked)
+ [Orphaned FSx for ONTAP target volumes (FlexClone) after launch cleanup](#fsx-orphaned-flexclone)
+ [Troubleshooting FSx for ONTAP launch errors](#fsx-ontap-launch-troubleshooting)

## Troubleshooting FSx for ONTAP iSCSI connectivity
<a name="fsx-iscsi-troubleshooting"></a>

When MGN migrates a server using FSx for ONTAP, the target instance must establish iSCSI sessions to the ONTAP SVM. A postboot script (`mgn_iscsi_postboot`) runs automatically to configure iSCSI connectivity with multipath redundancy when available. If no iSCSI sessions are established within the validation window (15 minutes for Linux, 25 minutes for Windows), the job fails.

**Postboot log location:**
+ Linux: `/var/log/mgn_iscsi_postboot.log`
+ Windows: `C:\Windows\Temp\mgn_iscsi_postboot.log`

[Connect to the target instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) via [SSM Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or SSH to read the log. The target instance ID is shown in the MGN console Launch status section. Look for `ERROR` or `WARNING` entries.

**Common failures:**


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Package installation errors or No supported package manager found | Target instance cannot reach OS package repositories | Ensure outbound internet access (NAT gateway or internet gateway) for package downloads. See [Step 6](fsx-ontap.md#fsx-ontap-step6-launch-settings). | 
| Package installation fails due to missing or inaccessible repositories (SLES, RHEL, CentOS) | Instance-bound or subscription-based repository credentials are not valid on the migrated target instance | Pre-install the required iSCSI and multipath packages on the source server before migration. See the packages table in [Step 6](fsx-ontap.md#fsx-ontap-step6-launch-settings). | 
| Connection refused or timeout on port 3260 | Security groups or NACLs not configured for iSCSI traffic | Allow TCP 3260 between the target instance and FSx for ONTAP security groups. See [Step 1](fsx-ontap.md#fsx-ontap-step1-security-groups). | 
| No route to host or network unreachable | No network path between target instance and FSx for ONTAP subnets | Verify routing between the target subnet and FSx for ONTAP subnets ([VPC route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html), VPC peering, or transit gateway). | 
| Multipath-IO could not be installed | MPIO packages unavailable or Windows Desktop SKU without the feature | The migration will succeed with single-path connectivity. For full HA redundancy, ensure the instance can install MPIO (Linux: multipath-tools or device-mapper-multipath packages; Windows: Server SKU with MultiPath-IO feature available). | 
| Phase 1 completed but Phase 2 never starts (Windows only) | Instance failed to reboot after MPIO installation or postboot service did not re-trigger | Verify the instance is running in the EC2 console. Check Windows Event Viewer for boot errors. Retry the launch. | 
| Log file does not exist | Postboot script did not run (conversion failure before postboot stage) | Check the MGN console for earlier errors in the launch status. | 

**Note**  
If the validation reports "iSCSI connectivity established with 1 of 2 expected sessions - operating without multipath", the migration succeeds but without full HA redundancy. Verify that both FSx for ONTAP subnet endpoints are routable from the target instance.

For manual iSCSI verification, see [Mounting iSCSI LUNs on FSx for ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-luns.html).

After fixing the issue, launch a new test or cutover from the MGN console. The postboot script will run again automatically.

## FSx for ONTAP replication errors
<a name="fsx-storage-timeout-troubleshooting"></a>

When MGN encounters storage issues while replicating data to FSx for ONTAP, replication stalls and an error is displayed in the MGN console. This section covers the common replication stall errors and how to resolve them.

### Failed to start data transfer
<a name="fsx-failed-to-start-data-transfer"></a>

If replication stalls with a "Failed to Start Data Transfer" error, MGN could not begin writing data to the FSx for ONTAP file system. This may be caused by a storage capacity issue.

**Possible causes and resolutions:**


| Cause | How to verify | Resolution | 
| --- | --- | --- | 
| File system is out of storage capacity | In the [FSx console](https://console.aws.amazon.com/fsx/), check the file system's Storage capacity and Used storage metrics. | Increase the file system's storage capacity. For more information, see [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html). | 
| Replication volume is out of storage capacity | In the [FSx console](https://console.aws.amazon.com/fsx/), check for volume-level errors on the replication volume. | Increase the volume size to accommodate the replicated data. | 

After resolving the issue, replication recovers automatically. It may take up to a few hours for the stall indicator to clear in the MGN console.

### Not converging
<a name="fsx-not-converging"></a>

If replication enters a "Not Converging" state, MGN is unable to keep up with changes on the source server. The rate of incoming data exceeds the rate at which MGN can write to the FSx for ONTAP file system. In addition to the general causes listed in [Common replication errors](common-replication-errors.md), the following FSx for ONTAP-specific causes may apply:

**Possible causes and resolutions:**


| Cause | How to verify | Resolution | 
| --- | --- | --- | 
| File system is out of storage capacity | In the [FSx console](https://console.aws.amazon.com/fsx/), check the file system's Storage capacity and Used storage metrics. | Increase the file system's storage capacity. For more information, see [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html). | 
| Throughput capacity is insufficient for the workload | In the FSx console, check the Throughput CloudWatch metrics for the file system. Look for sustained throughput near the provisioned limit. | Increase the file system's throughput capacity. You can modify throughput at any time. For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html). | 

After resolving the issue, replication recovers automatically. It may take up to a few hours for the stall indicator to clear in the MGN console.

### Storage operation timed out
<a name="fsx-storage-operation-timed-out"></a>

If a migration operation fails with a storage operation timeout, this indicates that MGN could not complete a storage request to the FSx for ONTAP file system within the expected time. This can be caused by insufficient capacity or degraded performance.

**Possible causes and resolutions:**


| Cause | How to verify | Resolution | 
| --- | --- | --- | 
| File system is out of storage capacity | In the [FSx console](https://console.aws.amazon.com/fsx/), check the file system's Storage capacity and Used storage metrics. | Increase the file system's storage capacity. For more information, see [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html). | 
| Throughput capacity is insufficient for the workload | In the FSx console, check the Throughput CloudWatch metrics for the file system. Look for sustained throughput near the provisioned limit. | Increase the file system's throughput capacity. You can modify throughput at any time. For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html). | 

After resolving the issue, replication recovers automatically. It may take up to a few hours for the stall indicator to clear in the MGN console.

## Replication volume not deleted after Finalize cutover/Disconnect from service (FlexClone split blocked by backup)
<a name="fsx-flexclone-split-blocked"></a>

**Symptoms:**
+ After finalize cutover, the replication volume remains in the FSx for ONTAP file system and is not cleaned up by MGN.
+ The MGN console may show the source server in "Cutover" state but the old replication volume persists.

**Cause:**

After finalize cutover, MGN creates a FlexClone from the replication volume and initiates a split to make it independent. If FSx for ONTAP automatic backups (or a manual backup) were taken on the target volume (FlexClone) after finalize cutover, the backup creates a locked snapshot that blocks the FlexClone split operation. MGN cannot complete the split until the locked snapshot is removed.

**Resolution:**

1. **Check if automatic backups are enabled** – In the FSx for ONTAP console, navigate to your file system and check the backup settings. If automatic backups are enabled, disable them to prevent new backups from being created on the volumes.

1. **Delete backups from target volumes** – In the FSx for ONTAP console, navigate to **Backups** and delete all backups associated with volumes matching the `target_{{source_server_id}}_{{timestamp}}` pattern. There may be more than one target volume per source server. Select each backup and choose **Actions** → **Delete backup**. This releases the locked snapshots that block the split.
**Note**  
Deleting the backup does not affect the target volume data. If you need to retain backup data, you can restore it to a separate volume before deleting.

1. **Wait 24 hours for cleanup** – MGN will automatically complete the FlexClone split and delete the replication volume within 24 hours. No further manual action is needed.

1. **Re-enable automatic backups** – After the replication volume has been cleaned up, re-enable automatic backups on the FSx for ONTAP file system to resume regular backup protection.

For more information, see [Managing FSx for ONTAP volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html) and [FSx for ONTAP backups](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html).

## Orphaned FSx for ONTAP target volumes (FlexClone) after launch cleanup
<a name="fsx-orphaned-flexclone"></a>

**Symptom:**

After a "Revert to Ready for testing", "Revert to Ready for cutover", or "Terminate launched instances" action, one or more FSx for ONTAP volumes prefixed with `atx_cleanup_required_` remain on the file system.

**Cause:**

MGN cannot delete FlexClone volumes that have active FSx for ONTAP backup relationships (SnapMirror) on them. When this occurs, MGN renames the volume with the `atx_cleanup_required_` prefix to indicate that it requires manual cleanup.

**How to confirm:**

1. Navigate to the MGN console → **Launch history**.

1. Find the job corresponding to the termination action.

1. Check the job event logs for the following message:

   `"{{N}} FSx for ONTAP volume(s) (prefixed 'atx_cleanup_required_') could not be deleted due to active backup relationships. Delete these volumes from the FSx console manually."`

**Finding volumes that require cleanup:**

1. Open the FSx for ONTAP console → **Volumes**.

1. Filter or search for volumes with names starting with `atx_cleanup_required_`.

**Resolution:**

Delete the orphaned volume manually via the FSx for ONTAP console:

1. Open the FSx for ONTAP console → **Volumes**.

1. Locate the volume matching the `atx_cleanup_required_` prefix.

1. Delete the volume.

**Verifying cleanup is complete:**

Confirm that no volumes with the `atx_cleanup_required_` prefix remain in your FSx for ONTAP file system.

## Troubleshooting FSx for ONTAP launch errors
<a name="fsx-ontap-launch-troubleshooting"></a>

Use the information in this section to troubleshoot launch errors specific to FSx for ONTAP migrations.

### Insufficient file system capacity
<a name="fsx-ontap-insufficient-capacity"></a>

Before launching a test or cutover, MGN validates that the FSx for ONTAP file system has sufficient capacity. The launch fails if predicted usage would exceed 90% of the aggregate capacity, with an error similar to:

```
Launch check failed: insufficient capacity on file system fs-0123456789abcdef0
(85% used). This job needs ~50 GB of free space. Expand storage and retry.
```

**Cause**  
The FSx for ONTAP file system does not have enough free SSD storage capacity to create FlexClone volumes for all source servers in the launch job.

**Resolution**  
Increase the SSD storage capacity of your FSx for ONTAP file system.

1. Open the FSx for ONTAP console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/), and choose **File systems**.

1. Select the file system shown in the error message.

1. On the **Summary** panel, choose **Update** next to **SSD storage capacity**.

1. Enter the new desired capacity. The minimum increase is 10% of the current capacity or 1 TiB, whichever is greater.

1. Choose **Update**.

1. Wait for the storage update to complete, then retry the launch from the MGN console.

**Note**  
Storage capacity increases are non-disruptive. The file system remains available during the scaling operation.

**Tip**  
During migration, the file system holds both the replica volumes (used for ongoing replication) and the cloned volumes (created at launch). Both coexist until you finalize the cutover and delete the replica volumes. Plan your SSD capacity to accommodate both sets simultaneously, or reduce the number of source servers in a single launch job.

For more information, see [Managing SSD storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html).
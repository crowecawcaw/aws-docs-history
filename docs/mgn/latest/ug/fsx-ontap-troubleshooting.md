NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Troubleshooting FSx for ONTAP issues

This section covers common issues when using FSx for ONTAP as the target storage type
with MGN.

**Topics**

- [Troubleshooting FSx for ONTAP iSCSI connectivity](#fsx-iscsi-troubleshooting "#fsx-iscsi-troubleshooting")
- [FSx for ONTAP storage operation timed out](#fsx-storage-timeout-troubleshooting "#fsx-storage-timeout-troubleshooting")
- [Replication volume not deleted after Finalize cutover/Disconnect from service (FlexClone split blocked by backup)](#fsx-flexclone-split-blocked "#fsx-flexclone-split-blocked")
- [Orphaned FSx for ONTAP target volumes (FlexClone) after launch cleanup](#fsx-orphaned-flexclone "#fsx-orphaned-flexclone")

## Troubleshooting FSx for ONTAP iSCSI connectivity

When MGN migrates a server using FSx for ONTAP, the target instance must establish iSCSI
sessions to the ONTAP SVM. A postboot script (`mgn_iscsi_postboot`) runs automatically
to configure iSCSI connectivity with multipath redundancy when available. If no iSCSI sessions
are established within the validation window (15 minutes for Linux, 25 minutes for Windows),
the job fails.

**Postboot log location:**

- Linux: `/var/log/mgn_iscsi_postboot.log`
- Windows: `C:\Windows\Temp\mgn_iscsi_postboot.log`

[Connect
to the target instance](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md") via
[SSM
Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") or SSH to read the log. The target
instance ID is shown in the MGN console Launch status section. Look for `ERROR` or
`WARNING` entries.

**Common failures:**

| Symptom                                                                                     | Cause                                                                                                        | Resolution                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Package installation errors or `No supported package manager found`                         | Target instance cannot reach OS package repositories                                                         | Ensure outbound internet access (NAT gateway or internet gateway) for package<br>downloads. See [Step 6](fsx-ontap.md#fsx-ontap-step6-launch-settings "fsx-ontap.md#fsx-ontap-step6-launch-settings").                                                       |
| Package installation fails due to missing or inaccessible repositories (SLES, RHEL, CentOS) | Instance-bound or subscription-based repository credentials are not valid on the<br>migrated target instance | Pre-install the required iSCSI and multipath packages on the source server before<br>migration. See the packages table in<br>[Step 6](fsx-ontap.md#fsx-ontap-step6-launch-settings "fsx-ontap.md#fsx-ontap-step6-launch-settings").                          |
| Connection refused or timeout on port 3260                                                  | Security groups or NACLs not configured for iSCSI traffic                                                    | Allow TCP 3260 between the target instance and FSx for ONTAP security groups. See<br>[Step 1](fsx-ontap.md#fsx-ontap-step1-security-groups "fsx-ontap.md#fsx-ontap-step1-security-groups").                                                                  |
| No route to host or network unreachable                                                     | No network path between target instance and FSx for ONTAP subnets                                            | Verify routing between the target subnet and FSx for ONTAP subnets<br>([VPC<br>route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md"), VPC peering, or transit gateway).                       |
| Multipath-IO could not be installed                                                         | MPIO packages unavailable or Windows Desktop SKU without the feature                                         | The migration will succeed with single-path connectivity. For full HA redundancy,<br>ensure the instance can install MPIO (Linux: `multipath-tools` or<br>`device-mapper-multipath` packages; Windows: Server SKU with<br>`MultiPath-IO` feature available). |
| Phase 1 completed but Phase 2 never starts (Windows only)                                   | Instance failed to reboot after MPIO installation or postboot service did not<br>re-trigger                  | Verify the instance is running in the EC2 console. Check Windows Event Viewer for<br>boot errors. Retry the launch.                                                                                                                                          |
| Log file does not exist                                                                     | Postboot script did not run (conversion failure before postboot stage)                                       | Check the MGN console for earlier errors in the launch status.                                                                                                                                                                                               |

###### Note

If the validation reports "iSCSI connectivity established with 1 of 2 expected sessions -
operating without multipath", the migration succeeds but without full HA redundancy. Verify that
both FSx for ONTAP subnet endpoints are routable from the target instance.

For manual iSCSI verification, see
[Mounting
iSCSI LUNs on FSx for ONTAP](../../../fsx/latest/ONTAPGuide/mount-iscsi-luns.md "../../../fsx/latest/ONTAPGuide/mount-iscsi-luns.md").

After fixing the issue, launch a new test or cutover from the MGN console. The postboot
script will run again automatically.

## FSx for ONTAP storage operation timed out

If a migration operation fails with a storage operation timeout, this indicates that
MGN could not complete a storage request to the FSx for ONTAP file system within the expected
time. This can be caused by insufficient capacity, degraded performance, or a network
connectivity issue between MGN and the file system.

**Possible causes and resolutions:**

| Cause                                                                 | How to verify                                                                                                                                                                                                                                                                                                                                     | Resolution                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File system is out of storage capacity                                | In the [FSx console](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/"),<br>check the file system's *_Storage capacity_<br>• and<br>*_Used storage_<br>• metrics.                                                                                                                                                         | Increase the file system's storage capacity. For more information, see<br>[Managing<br>storage capacity and provisioned IOPS](../../../fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.md "../../../fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.md").                                                               |
| Throughput capacity is insufficient for the workload                  | In the FSx console, check the **Throughput**<br>CloudWatch metrics for the file system. Look for sustained throughput near the<br>provisioned limit.                                                                                                                                                                                              | Increase the file system's throughput capacity. You can modify throughput at any<br>time. For more information, see<br>[Managing<br>throughput capacity](../../../fsx/latest/ONTAPGuide/managing-throughput-capacity.md "../../../fsx/latest/ONTAPGuide/managing-throughput-capacity.md").                              |
| Network connectivity issue between MGN and the FSx for ONTAP REST API | Verify that the security group attached to the FSx for ONTAP file system allows<br>inbound HTTPS (TCP 443) from the FSx for ONTAP preferred and standby subnet CIDRs. These<br>rules are required for MGN to access the ONTAP REST API. See<br>[1.2 FSx for ONTAP security group](fsx-ontap.md#fsx-ontap-fsx-sg "fsx-ontap.md#fsx-ontap-fsx-sg"). | Add inbound HTTPS (TCP 443) rules to the FSx for ONTAP security group with the<br>preferred and standby subnet CIDRs as the source. For details on identifying these<br>CIDRs, see [Step 1: Configure security<br>groups](fsx-ontap.md#fsx-ontap-step1-security-groups "fsx-ontap.md#fsx-ontap-step1-security-groups"). |

After resolving the issue, retry the migration operation from the MGN console.

## Replication volume not deleted after Finalize cutover/Disconnect from service (FlexClone split blocked by backup)

**Symptoms:**

- After finalize cutover, the replication volume remains in the FSx for ONTAP file system and is not
  cleaned up by MGN.
- The MGN console may show the source server in "Cutover" state but the old replication
  volume persists.

**Cause:**

After finalize cutover, MGN creates a FlexClone from the replication volume and initiates a split
to make it independent. If FSx for ONTAP automatic backups (or a manual backup) were taken on the
target volume (FlexClone) after finalize cutover, the backup creates a locked snapshot that blocks the
FlexClone split operation. MGN cannot complete the split until the locked snapshot is
removed.

**Resolution:**

1. **Check if automatic backups are enabled** – In the
   FSx for ONTAP console, navigate to your file system and check the backup settings. If automatic
   backups are enabled, disable them to prevent new backups from being created on the
   volumes.
2. **Delete backups from target volumes** – In the
   FSx for ONTAP console, navigate to **Backups** and delete all
   backups associated with volumes matching the
   `target_`source_server_id`_`timestamp``
   pattern. There may be more than one target volume per source server. Select each backup and
   choose **Actions** →
   **Delete backup**. This releases the locked snapshots that
   block the split.

###### Note

Deleting the backup does not affect the target volume data. If you need to retain backup
data, you can restore it to a separate volume before deleting. 3. **Wait 24 hours for cleanup** – MGN will
automatically complete the FlexClone split and delete the replication volume within 24 hours.
No further manual action is needed. 4. **Re-enable automatic backups** – After the
replication volume has been cleaned up, re-enable automatic backups on the FSx for ONTAP
file system to resume regular backup protection.

For more information, see
[Managing
FSx for ONTAP volumes](../../../fsx/latest/ONTAPGuide/managing-volumes.md "../../../fsx/latest/ONTAPGuide/managing-volumes.md") and
[FSx for ONTAP
backups](../../../fsx/latest/ONTAPGuide/using-backups.md "../../../fsx/latest/ONTAPGuide/using-backups.md").

## Orphaned FSx for ONTAP target volumes (FlexClone) after launch cleanup

**Symptom:**

After a "Revert to Ready for testing", "Revert to Ready for cutover",
or "Terminate launched instances" action, one or more FSx for ONTAP volumes prefixed with
`atx_cleanup_required_` remain on the file system.

**Cause:**

MGN cannot delete FlexClone volumes that have active FSx for ONTAP backup relationships
(SnapMirror) on them. When this occurs, MGN renames the volume with the
`atx_cleanup_required_` prefix to indicate that it requires manual cleanup.

**How to confirm:**

1. Navigate to the MGN console → **Launch history**.
2. Find the job corresponding to the termination action.
3. Check the job event logs for the following message:

`"`N` FSx for ONTAP volume(s) (prefixed 'atx_cleanup_required_')
 could not be deleted due to active backup relationships.
 Delete these volumes from the FSx console manually."`

**Finding volumes that require cleanup:**

1. Open the FSx for ONTAP console → **Volumes**.
2. Filter or search for volumes with names starting with
   `atx_cleanup_required_`.

**Resolution:**

Delete the orphaned volume manually via the FSx for ONTAP console:

1. Open the FSx for ONTAP console → **Volumes**.
2. Locate the volume matching the
   `atx_cleanup_required_` prefix.
3. Delete the volume.

**Verifying cleanup is complete:**

Confirm that no volumes with the `atx_cleanup_required_` prefix remain in your
FSx for ONTAP file system.

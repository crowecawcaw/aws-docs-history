# Restoring SAP HANA from EBS snapshots

A successful restore strategy is dependent on many factors, including:

- The failure scenario or event that led to the restore
- The recovery point to which you need to restore
- The date and time of your last successful backup
  All of these factors can impact the restore and recovery approach. It is recommended that a comprehensive disaster recovery (DR) strategy is developed, tested, and well documented to ensure that the recovery process and recovery times are well understood.

The following steps do not cover detailed instructions on log recovery, which is likely to involve a secondary backup mechanism, such as AWS Backint for SAP HANA. Ensure that when you select the volumes to recover, you consider the potential impact on your recovery point.

###### Topics

- [Step 1: Prepare for a restore](#step1 "#step1")
- [Step 2: Attach or replace the restored EBS volumes](#step2 "#step2")
- [Step 3: Recover SAP HANA database](#step3 "#step3")
- [Step 4: Resume standard operations](#step4 "#step4")

## Step 1: Prepare for a restore

1. Get information about the EBS volume to restore. This information can help you identify which volumes need to be restored. For example, it can help you to identify the data volumes and the log volumes for your workload. Use this information to tag your volumes or save the information in a location that will not be impacted by the loss of the instance.

Run the following commands and note the volume’s ID, serial number, UUID, mount point information, fstab configuration, and attachment information.

```
$ lsblk -o +LABEL,UUID,SERIAL | sed 's/vol/vol-/g'
```

```
$ cat /etc/fstab | column -t
```

```
$ aws ec2 describe-volumes \
  --filters Name=attachment.instance-id,Values=<instance_id> \
  --query 'Volumes[*].[VolumeId,Size,Attachments[0].Device,Attachments[0].InstanceId,Attachments[0].State]' \
  --output table
```

1. Review the fast snapshot restore state for the EBS snapshots. EBS volumes that are created from snapshots with fast snapshot restore instantly deliver all of their provisioned performance. This eliminates the latency of I/O operations on a block when it is accessed for the first time. This is important for SAP HANA restores as tables are read from disk on startup so that they can be loaded into memory. Before you create the EBS volume, ensure that fast snapshot restore is in the `enabled` state for the snapshot in the Availability Zone in which you want to create the volume. You will also need sufficient volume creation credits. For more information, see [Considerations](dlm-sap-considerations.md "dlm-sap-considerations.md").
2. Identify the backup and backup catalog. If possible, identify the time stamp and backup ID of the backup you plan to restore to. Ensure that the backup catalog is available in a location that will be available after the EBS volume is restored.
3. Stop SAP HANA and any backup schedules. If you are restoring in place, ensure a clean SAP HANA and operating system state for the recovery.

Run the following command to stop SAP HANA and any connected SAP applications using sapcontrol or other SAP tools, and to remove remaining processes and clean shared memory segments.

```
$ cleanipc <hana_sys_no> remove
```

(Optional) Do the following to prevent SAP HANA from trying to start up before the restore is complete. This can be helpful if you need to restart the operating system before the restore is complete.

```
$ cd /usr/sap/<hana_sid>/SYS/profile
$ vi <hana_start_profile>
```

Then, check and change the value of `autostart` to `0`.

```
#autostart=1 # Previous value changed for restore.
autostart=0
```

4. (Optional) Temporarily disable or modify Amazon Data Lifecycle Manager policies or schedules to exclude the EC2 instance where you are performing the restore. This prevents interference with the restore and ensures that the required snapshots are retained for the duration of the restore process.

## Step 2: Attach or replace the restored EBS volumes

The following steps are dependent on whether you are restoring to the EC2 instance where the backups were created or to a new EC2 instance. If you are replacing EBS volumes on the same instance, then you must detach all previous volumes.

1. Identify the mount points to be restored from the EBS snapshot and, if applicable, unmount the filesystems associated with the old volumes from the EC2 Instance. For example, run the following command as the root user.

```
$ umount </hana/data>
```

If you are concerned that the state of the volumes might impact the ability to reboot the instance, you can comment out the entries in `/etc/fstab`. 2. Follow the prescriptive guidance on [Restoring an EBS volume from an EBS snapshot](../../../prescriptive-guidance/latest/backup-recovery/restore.md#restore-snapshot "../../../prescriptive-guidance/latest/backup-recovery/restore.md#restore-snapshot") to create volumes from the snapshots that match the backup time and the volumes that need to be restored, and then attach the volumes to the instance using the mapping information that you noted in Step 1.

If you are using striped Logical Volume Manager (LVM) volumes, take additional care to ensure that all required volumes in the volume group are recovered from the same point. 3. Scan or refresh connected volumes. Run the following command as the root user.

```
$ pvscan --cache -aay
```

If you are using LVM, run the following command.

```
$ vgchange --refresh
```

4. Remount the volumes and ensure that `/etc/fstab` reflects the required filesystems. For example, run the following command.````

```
$ mount </hana/data>
```

Review the operating system logs for any errors.

## Step 3: Recover SAP HANA database

After the EBS volumes have been restored, follow the instructions in the SAP documentation to recover the SAP HANA system database and all tenants. Ensure that the backup catalog and any required logs for roll forward are available. This can include access to AWS Backing for SAP HANA and/or local filesystems.

As both the system and tenant databases generally share the same filesystems, all databases need to be recovered.

1. Recover the SAP HANA system database. For more information, see [Recover SAP HANA From a Data Snapshot](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/9fd053d58cb94ac69655b4ebc41d7b05.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/9fd053d58cb94ac69655b4ebc41d7b05.html") in the SAP documentation.
2. Recover all SAP HANA tenant databases. For more information, see [Recover all Tenant Databases From a Data Snapshot](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/b2c283094b9041e7bdc0830c06b77bf8.html "https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/b2c283094b9041e7bdc0830c06b77bf8.html") in the SAP documentation.

## Step 4: Resume standard operations

If you previously disabled the Amazon Data Lifecycle Manager policy when you started the restore process, then you should now re-enable the policy so that it will continue to automate the creation of application-consistent EBS snapshots for all targeted EC2 instances.

You might also consider changing the `autostart` back to `1` so that SAP HANA restarts automatically after a system reboot.

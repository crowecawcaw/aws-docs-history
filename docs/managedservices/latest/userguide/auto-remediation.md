

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS automatic remediation of alerts
<a name="auto-remediation"></a>

After verification, AWS Managed Services (AMS) automatically remediates certain alerts according to specific conditions and processes described in this section.


| Alert name | Description | Thresholds | Action | 
| --- | --- | --- | --- | 
| Broken secure channel | The Broken Secure Channel Alarm is triggered on Windows EC2 Instances when the instance loses connection with the AD Domain Controller. | The threshold is above the defined value 10 times in the last 15 minutes. | AMS automatic remediation validates that the instance is online in SSM, the hostname is not duplicated, and that the AD Computer Object is aligned with the CloudFormation stack . The remediation repairs the secure channel connection to restore access to the instance. | 
| Status Check Failed | Possible hardware failures or a fault state of the instance. | The system has detected a failed status at least once within the last 15 minutes. | AMS automatic remediation first validates if the instance is accessible. If the instance is inaccessible, then the instance is stopped and restarted. The stop and start allows the instance to migrate to new underlying hardware. For more information, see the following section "EC2 Status Check Failure Remediation Automation." | 
| AMSLinuxDiskUsage | Trigger when the disk usage of 1 mount point (designated space on a volume) on your EC2 instance is filling up. | The threshold is above the defined value 6 times on the last 30 minutes. | AMS automatic remediation first deletes temporary files. If that does not free up enough disk space, it extends the volume to prevent downtime if the volume becomes full. | 
| AMSWindowsDiskUsage | When the disk usage of 1 mount point (designated space on a volume) on your EC2 instance is filling up. | The threshold is above the defined value 6 times during the last 30 minutes. | AMS automatic remediation first deletes temporary files. If that does not free up enough disk space, it extends the volume to prevent downtime if the volume becomes full. | 
| RDS-EVENT-0089 | The DB instance has consumed more than 90% of its allocated storage. | The storage is more than 90% allocated. | AMS automatic remediation first validates that the DB is in a modifiable and available or storage-full state. It then attempts to increase the allocated storage, IOPS, and storage throughput through a CloudFormation changeset. If stack drift is already detected, it falls back to the RDS API to prevent downtime.<br />This feature can be opted out of by adding the following tag to the RDS DB Instance: `"Key: ams:rt:ams-rds-max-allocated-storage-policy, Value: ams-opt-out".` | 
| RDS-EVENT-0007 | Allocated storage for the DB instance has been exhausted. To resolve, allocate additional storage. | Storage is 100% allocated. | AMS automatic remediation first validates that the DB is in a modifiable and available or storage-full state. It then attempts to increase the allocated storage, IOPS, and storage throughput through a CloudFormation changeset. If stack drift is already detected, it falls back to the RDS API to prevent downtime.<br />This feature can be opted out of by adding the following tag to the RDS DB Instance: `"Key: ams:rt:ams-rds-max-allocated-storage-policy, Value: ams-opt-out".` | 
| RDS-EVENT-0224 | The requested allocated storage reaches or exceeds the configured maximum storage threshold. | The maximum storage threshold for the DB instance has been exhausted or is greater than or equal to the requested allocated storage. | AMS automatic remediation first validates that the requested amount of RDS storage will breach the max storage threshold. If confirmed, AMS attempts to increase the max storage threshold by 30% with a CloudFormation changeset, or direct RDS API if resources are not provisioned through CloudFormation.<br />This feature can be opted out of by adding the following tag to the RDS DB Instance: `"Key: ams:rt:ams-rds-max-allocated-storage-policy, Value: ams-opt-out".` | 
| RDS-Storage-Capacity | Less than 1GB is left at the allocated storage for the DB instance. | Storage is 99% allocated. | AMS automatic remediation first validates that the DB is in a modifiable and available or storage-full state. It then attempts to increase the allocated storage, IOPS, and storage throughput through a CloudFormation changeset. If stack drift is already detected, it falls back to the RDS API to prevent downtime.<br />This feature can be opted out of by adding the following tag to the RDS DB Instance: `"Key: ams:rt:ams-rds-max-allocated-storage-policy, Value: ams-opt-out".` | 
| AMSFSXONTAPVolumeCapacityUtilization | The Amazon FSx for NetApp ONTAP volume has consumed more than the default allocated storage (80%). | FSx for ONTAP Volume Capacity Utilization is greater than 80% for two hours (default value). | AMS automatic remediation first validates that the volume lifecycle state is in a modifiable state, then extends volume size by 10% while verifying against the file system maximum capacity. If the file system lacks sufficient storage capacity for the volume expansion, both the volume and file system are expanded together. This expansion is limited to a maximum of three times within any seven-day period. The maximum storage limit that AMS Automation expands to is 5120 GiB.If iSCSI LUN is configured on top of the volume, expand the iSCSI LUN at the operating system level. For more information, see [Why is my FSx for ONTAP LUN in read-only mode?](https://repost.aws/knowledge-center/fsx-ontap-lun-in-read-only-mode) | 

## Amazon EC2 Broken Secure Channel: Remediation automation note
<a name="ar-broken-channel-note"></a>

Before AWS Managed Services (AMS) auto-remediation performs remediation on Amazon EC2 Windows Broken Secure Channel issues, the automation carries out the following pre-checks and creates an incident report for further investigation:
+ Validates that the Amazon EC2 instance SSM status is "Online."
+ Validates whether the Amazon EC2 instance is part of an Auto Scaling group and whether all instances in the Auto Scaling group have the same hostname.
+ Checks if the Amazon EC2 instance is part of the CloudFormation stack that was used to provision it. If the instance has been removed from the CloudFormation stack, the automation verifies whether the associated Active Directory Organizational Unit (OU) is still referencing the stack.

After the above validations have passed, automation proceeds to remediate the Broken Secure channel.

Remediation Steps:
+ Auto-remediation attempts to repair the secure channel between the EC2 instance and the AD Domain, restoring access to the instance.
+ Post remediation the automation checks that the secure channel is established. If unsuccessful, AMS creates an incident and engages AMS operations to investigate.

## EC2 status check failure: Remediation automation notes
<a name="auto-remediation-ec2-fail"></a>

How AMS auto-remediation works with EC2 status check failure issues:
+ If your Amazon EC2 instance has become unreachable, the instance must be stopped and started again so it can be migrated to new hardware and recovered.
+ If the root of the problem is within the OS (missing devices in fstab, kernel corruption, and so on), the automation is not able to recover your instance.
+ If your instance belongs to an Auto Scaling group, the automation takes no action—the AutoScalingGroup scaling action replaces the instance.
+ If your instance has EC2 Auto Recovery enabled, the remediation doesn't take action.

## EC2 volume usage remediation automation
<a name="auto-remediation-ec2-vol-use"></a>

How AWS Managed Services (AMS) auto-remediation works with EC2 volume usage issues:
+ The automation first validates if the volume expansion is required and if it can be performed. If the expansion is deemed appropriate, the automation can increase the volume capacity. This automated process balances the need for growth with controlled, limited expansion.
+ Before extending a volume, the automation performs cleanup tasks (Windows: Disk Cleaner, Linux: Logrotate \+ Simple Service Manager Agent Log removal) on the instance to try to free up space.
**Note**  
The cleanup tasks are not run on EC2 "T" family instances due to their reliance on CPU credits for continued functionality.
+ On Linux, the automation only supports extending file systems of type EXT2, EXT3, EXT4 and XFS.
+ On Windows, the automation only supports New Technology File System (NTFS) and Resilient File System (ReFS).
+ The automation doesn't extend volumes that are part of Logical Volume Manager (LVM) or a RAID array.
+ The automation doesn't extend *instance store* volumes.
+ The automation doesn't take action if the affected volume is already bigger than 2 TiB.
+ The expansion through automation is limited to a maximum of three times per week and five times total over the system's lifetime.
+ The automation doesn't expand the volume if the previous expansion happened within the last six hours.

When these rules prevent the automation from taking action, AMS reaches out to you through an outbound service request to determine the next actions to take.

## Amazon RDS low storage event remediation automation
<a name="auto-remediation-rds"></a>

How AWS Managed Services (AMS) auto-remediation works with Amazon RDS low storage event issues:
+ Before trying to extend the Amazon RDS instance storage, the automation performs several checks to ensure the Amazon RDS instance is in a modifiable and available, or storage-full, state.
+ Where CloudFormation stack drift is detected, remediation occurs through the Amazon RDS API.
+ Depending on the triggering event, the remediation modifies the properties `MaxAllocatedStorage`, `AllocatedStorage`, `Iops`, or `StorageThroughput`. Other Amazon RDS instance properties are not modified. For more information, see [Settings for DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Settings.html).
+ The remediation action does not run in the following scenarios:
  + The Amazon RDS instance status is not "available" or "storage-full".
  + The Amazon RDS instance storage is not currently modifiable (such as when the storage has been modified in the last six hours).
  + The Amazon RDS instance has auto-scaling storage enabled.
+ Remediation is limited to one expansion per six hours and no more than three expansions within a rolling fourteen day period.
+ When these scenarios occur, AMS reaches out to you with an outbound incident to determine next actions.

## ONTAP volume capacity remediation automation
<a name="auto-remediation-fsx-ontap"></a>

How AWS Managed Services (AMS) auto-remediation works with ONTAP volume capacity issues:
+ Before extending the volume, the automation validates that the volume lifecycle state is in a modifiable state.
+ The automation extends the volume size by 10% while verifying against the file system maximum capacity.
+ If the file system doesn't have sufficient storage capacity to accommodate the volume expansion, both the volume and file system capacity are expanded.
+ Remediation is limited to no more than three updates within a seven-day period.
+ The maximum storage limit that AMS Automation expands to is 5120 GiB.
+ If iSCSI LUN is configured on top of the volume, you must manually expand the iSCSI LUN at the OS level after the automatic remediation completes. For more information, see [Why is my FSx for ONTAP LUN in read-only mode?](https://repost.aws/knowledge-center/fsx-ontap-lun-in-read-only-mode)
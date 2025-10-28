NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Other troubleshooting topics

Use the information in this section to help you with other troubleshooting.

###### Topics

- [Re-initialize the AWS Application Migration Service](#Re-initialize-the-service "#Re-initialize-the-service")
- [Windows license activation – AWS](#Windows-License-Activation "#Windows-License-Activation")
- [Migration leaving behind replication
  volumes after cutover](#Migration-Leaving-Replication-Volumes "#Migration-Leaving-Replication-Volumes")
- [Replication lag issues](#Replication-Lag-Issues "#Replication-Lag-Issues")
- [Windows Driver changes](#Windows-Drive-Changes "#Windows-Drive-Changes")
- [Windows Dynamic Disk troubleshooting](#Windows-Dynamic-Disk "#Windows-Dynamic-Disk")
- [Deleting AWS MGN resources](#Deleting-Resources "#Deleting-Resources")
- [Set UEFI boot mode](#set-uefi-boot-mode "#set-uefi-boot-mode")

## Re-initialize the AWS Application Migration Service

AWS Application Migration Service can be re-initialized in case of any issues with IAM service roles

To re-initialize the AWS MGN service, please follow these steps:

- Open the AWS Application Migration Service Console and navigate to the correct region you are migrating to.
- In the left navigation pane, select "Settings". Under "Replication template," click "Reinitialize service permissions" and then click "Confirm."

## Windows license activation – AWS

AWS Application Migration Service converts the Windows OS licenses to AWS Windows licenses and activates them
against the AWS KMS.

If license activation failed, follow [this AWS
guide](https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/ "https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/") to resolve.

## Migration leaving behind replication

volumes after cutover

If you are seeing left behind replication volumes in AWS after running the cutover process,
then ensure that the names of the replication volumes match those given to them by AWS Application Migration Service (AWS MGN).

Most likely, you have a script running in your AWS account that renames Amazon EBS volumes to
match the name of the EC2 instance they are attached to.

However, by renaming an EBS volume used by AWS MGN for replication
you are severing its association with AWS MGN, and AWS MGN will not automatically clean up such volumes.

This can also occur if MGN service tags associated with EBS volumes are modified.

Key: AWSApplicationMigrationManaged; Value: mgn.amazonaws.com

Key: Name;Value: AWS Application Migration Service Replication Volume

## Replication lag issues

Potential solutions:

- Make sure that the Source server is up and running.
- Make sure that AWS MGN services are up and running.
- Make sure that TCP Port 1500 is not blocked outbound from the source server to the
  replication server.
- If the MAC address of the Source had changed, that would require a reinstallation of the
  AWS Replication Agent.
- If the source server was rebooted recently or the AWS Application Migration Service
  were restarted, the disks are re-read after this and until its finished, the Lag will
  grow.
- If the source server had a spike of write operations, the lag will grow until
  AWS Application Migration Service manages to flush all the written data to the test or cutover
  instance replication server.
- Make sure you have selected the right replication instance and EBS type by using the following runbook: [AWSSupport-CalculateEBSPerformanceMetrics automation runbook](../../../systems-manager-automation-runbooks/latest/userguide/automation-calculate-ebs-performance-metrics.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-calculate-ebs-performance-metrics.md") .
  The replication instance ID, which is used as an input parameter for the runbook, is available under the source server replication dashboard.

To learn more about replication lag troubleshooting, please refer [AWS Support knowlege center article](https://repost.aws/knowledge-center/mgn-windows-fix-replication-lag "https://repost.aws/knowledge-center/mgn-windows-fix-replication-lag").

## Windows Driver changes

Users may see changes in Windows drive letter assignments (for example, Drive D changed to
E) on target machines launched by AWS Application Migration Service.

This happens because Windows sometimes re-configures the drive letters when a machine comes
up on a new infrastructure, for example, if the Source server had a drive letter mapped to a
disk that was not replicated (such as a network drive). You can solve this issue by remapping
the drive letters on the test or cutover instance correctly after it has been launched.

## Windows Dynamic Disk troubleshooting

Moving a Windows Dynamic Disk from a local computer to another computer may change the disk
status to "Foreign", resulting in a disruption in replication. The solution is to import the
foreign disk, as discussed in [this Microsoft troubleshooting article](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/troubleshooting-disk-management#a-dynamic-disks-status-is-foreign "https://docs.microsoft.com/en-us/windows-server/storage/disk-management/troubleshooting-disk-management#a-dynamic-disks-status-is-foreign").

## Deleting AWS MGN resources

You can delete various AWS MGN resources, including source servers, jobs, and the
replication settings template, through the MGN API. Use the following API commands to delete
resources:

**DeleteSourceServer**

Use the _DeleteSourceServer_ API command to delete source
servers.

This command:

- Deletes a single source server by ID.
- Successful deletion should result in a 204 HTTP response code.
- To delete source server the server should be in a _DISCONNECTED_ or _CUTOVER_ state. If the source
  server has not been cut over, you must first call the _DisconnectFromService_ API and then call the _DeleteSourceServer_ API.

**DeleteJob**

Use the _DeleteJob_ API command to delete a Job.

This command:

- Deletes a single Job by ID.
- Successful deletion should result in a 204 HTTP response code.
- Job must be in a _COMPLETED_ state to be deleted.

**DeleteReplicationConfigurationTemplate**

Use the _DeleteReplicationConfigurationTemplate_ API
command to delete the replication template.

This command:

- Deletes a single replication template by ID.
- Successful deletion should result in a 204 HTTP response code.
- All source servers and jobs must first be deleted before calling the _DeleteReplicationConfigurationTemplate_ API.

## Set UEFI boot mode

UEFI boot mode can only be used with Nitro based EC2 Instance types. Nitro requires ENA
driver, which is only supported from kernel 3.10.

UEFI to UEFI boot mode is not supported with agentless replication.

If you get the error `Source server boot mode is UEFI which is inconsistent with
 target instance.` It might be because

- The OS uses an old UEFI format from kernel 3.8 or earlier. If so, set the source server boot
  mode to 'Legacy BIOS'.
- You are performing UEFI to UEFI boot mode with agentless replication.

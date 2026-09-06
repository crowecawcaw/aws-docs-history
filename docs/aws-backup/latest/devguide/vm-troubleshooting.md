

# Troubleshoot VM issues
<a name="vm-troubleshooting"></a>

## Incremental Backups / CBT issues and messages
<a name="w2aac17c19c43c27b3"></a>

**Failure message:** `"The VMware Change Block Tracking (CBT) data was invalid during this backup, but the incremental backup was successfully completed with our proprietary change detection mechanism."`

If this message continues, [reset CBT](https://knowledge.broadcom.com/external/article?legacyId=1020128) as directed by VMware.

**Message notes CBT was not turned on or was unavailable:** *"VMware Change Block Tracking (CBT) was not available for this virtual machine, but the incremental backup was successfully completed with our proprietary change mechanism."*

Check to make sure CBT is turned on. To verify if a virtual disk has CBT enabled:

1. Open the vSphere Client and select a powered-off virtual machine.

1. Right-click the virtual machine and navigate to **Edit Settings** > **Options** > **Advanced/General** > **Configuration Parameters**.

1. The option `ctkEnabled` needs to equal `True`.

If it is turned on, ensure you are using up-to-date VMware features. The host must be ESXi 4.0 or later and the virtual machine owning the disks to be tracked must be hardware version 7 or later.

**Note**  
The ESXi and hardware version requirements above are VMware's minimum requirements for the CBT feature to function. They do not represent the vSphere versions supported by AWS Backup. For the list of vSphere versions supported by AWS Backup, see [Supported VMs](vm-backups.md#supported-vms).

If CBT is turned on (enabled) and the software and hardware are up to date, turn off the virtual machine and then turn it back on again. Ensure that CBT is turned on. Then, perform the backup again.

## VMware backup failure
<a name="w2aac17c19c43c27b5"></a>

When a VMware backup fails, it may be related to one of the following:

**Failure message:** `"Failed to process backup data. Aborted backup job."` or `"Error opening disk on the virtual machine"`.

**Possible causes:** This error may occur because of a configuration issue; or, the VMware version or disk isn't supported.

**Remedy 1:** Ensure your infrastructure is configured to use a gateway and ensure all required ports are open.

1. Access the [backup gateway console](https://docs.aws.amazon.com/storagegateway/latest/tgw/accessing-local-console.html#MaintenanceConsoleWindowVMware-common). Note this is different from the AWS Backup console.

1. On the **Backup gateway configuration** page enter option **3** to test the network connectivity.

1. If the network test is successful, enter **X**.

1. Return to the Backup gateway configuration page.

1. Enter **7** to access the command prompt.

1. Run the following commands to verify network connectivity:

   `ncport -d {{ESXi Host}}-p 902`

   `ncport -d {{ESXi Host}}-p 443`

**Remedy 2:** Use [Supported VMs](vm-backups.md#supported-vms) versions.

**Remedy 3:** If a gateway appliance is configured with incorrect DNS servers, then the backup fails. To verify the DNS configuration, complete the following steps:

1. Access the [backup gateway console](https://docs.aws.amazon.com/storagegateway/latest/tgw/accessing-local-console.html#MaintenanceConsoleWindowVMware-common).

1. On the **Backup gateway configuration** page enter option **2** to navigate to the network configuration.

1. In **Network configuration**, enter **7** to view the DNS configuration.

1. Review the DNS server IP addresses. If the DNS server IP address are incorrect then exist the prompt to return to **Network Configuration**.

1. In **Network Configuration**, enter **6** to edit the DNS configuration.

1. Enter the correct DNS server IP addresses. Then, enter **X** to complete your network configuration.

To obtain more information about your hypervisor, such as errors and network configuration and connection, see [Editing a hypervisor configuration](working-with-hypervisors.md#edit-hypervisor) to configure the hypervisor to integrate with Amazon CloudWatch Logs.

## Backup failures from network connection issues
<a name="w2aac17c19c43c27b7"></a>

**Failure message: **`"Failed to upload backup during data ingestion. Aborted backup job."` or `"Cloud network request timed out during data ingestion"`.

**Possible causes:** This error can occur if the network connection is insufficient to handle data uploads. If network bandwidth is low, the link between the VM and AWS Backup can become congested and cause backups to fail.

Required network bandwidth depends on several factors, including the size of the VM, the incremental data generated for each VM backup, the backup window, and restore requirements.

**Remedy:** Best practices and recommendations include having a minimum bandwidth of 100 Mbps upload bandwidth for on-premises VMs connected to AWS Backup. This is the minimum required for the gateway to function. Bandwidth below 100 Mbps prevents the gateway from completing any backup or restore job. With a large number of VMs, backup jobs might still fail due to timeout even with bandwidth above 100 Mbps. Consider increasing bandwidth based on the number of VMs and the size of data being backed up. Once the bandwidth is confirmed, retry the backup job.

## Aborted backup job
<a name="w2aac17c19c43c27b9"></a>

**Failure message:** `"Failed to create backup during snapshot creation. Aborted backup job."`

**Possible cause:** The VMware host where the gateway appliance resides may have an issue.

**Remedy:** Check the configuration of your VMware host and review the it for issues. For additional information, see [Editing a hypervisor configuration](working-with-hypervisors.md#edit-hypervisor).

## No available gateways
<a name="w2aac17c19c43c27c11"></a>

**Failure message:** `"No gateways available to work on job."`

**Possible cause:** all connected gateways are busy with other jobs. Each gateway has a limit of four concurrent jobs (backup or restore).

For **remedies**, see the next section for steps on increasing number of gateways and steps to increase backup plan window time.

## VMware backup job failure
<a name="w2aac17c19c43c27c13"></a>

**Failure message: **`"Abort signal detected"`

**Possible causes:**
+ **Low Network Bandwidth**: Insufficient network bandwidth can impede the completion of backups within the completion window. When the backup job requires more bandwidth than available, it can result in failure and trigger the "Abort Signal Detected" error.
+ **Inadequate Number of Backup Gateways**: If the number of backup gateways is not sufficient to handle the backup rotation for all the configured VMs, the backup job may fail. This can occur when the backup plan's window for completing backups is too short or the number of backup gateways are not enough.
+ Backup Plan completion window is too small.

**Remedies:**

**Increase bandwidth:** Consider increasing the network bandwidth between AWS and the on-premises environment. This step will provide more bandwidth for the backup process, allowing data to transfer smoothly without triggering the error. You must have at least 100 Mbps bandwidth to AWS to back up on-premises VMware VMs using AWS Backup. This is the minimum required for the gateway to complete any backup or restore job. If you have a large number of VMs, consider increasing bandwidth beyond 100 Mbps, as jobs might still time out with insufficient bandwidth.

If a bandwidth rate limit is configured for the backup gateway, it can restrict the flow of data and lead to backup failures. Increasing the bandwidth rate limit to ensure sufficient data transfer capacity may help reduce failures. This adjustment can mitigate the occurrence of the "Abort Signal Detected" error. For more information, see [Backup gateway Bandwidth Throttling](working-with-gateways.md#backup-gateway-bandwidth-throttling).

**Increase the number of Backup gateways:** A single backup gateway can process up to 4 backup and restore jobs at a time. Additional jobs will queue and wait for the gateway to free up until the backup start window passed. If the backup window passes and the queued jobs have not started, those backup jobs will fail with "abort signal detected". You can increase the number of backup gateways to alleviate the number of failed jobs. See [Working with gateways](working-with-gateways.md) for more detail.

**Increase backup plan window time:** You can increase the **complete within duration** of the backup window in your backup plan. See [Backup plan options and configuration](plan-options-and-configuration.md) for more detail.

## Restore to EC2 fails due to missing ENA drivers
<a name="w2aac17c19c43c27c15"></a>

**Failure message:** `"Restore failed because the instance type selected for restore requires that the VirtualMachine image have Elastic Network Adapter (ENA) drivers installed, but no ENA drivers were present in the backed up VM."`

**Possible cause:** Your restore job failed because you are attempting to restore a VMware backup that does not have ENA drivers installed to an Amazon EC2 instance type that requires Elastic Network Adapters (ENA).

**Remedies:**

**Restore to an instance type that does not require ENA:** Restore this recovery point to an instance type that does not require ENA. For a list of instance types and their requirements, see [Amazon EC2 instance types](https://docs.aws.amazon.com/ec2/latest/instancetypes/pg.html).

**Install ENA drivers and take a new backup:** To restore to instance types that require ENA, install ENA drivers on the virtual machine first, take a new backup, and then restore from that backup. For more information about driver requirements, see [VM Import/Export requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/limitations-image-importing.html#limitations-image-importing-linux).

For help resolving these issues, see [AWS Knowledge Center](https://repost.aws/knowledge-center/backup-troubleshoot-vmware-backups).
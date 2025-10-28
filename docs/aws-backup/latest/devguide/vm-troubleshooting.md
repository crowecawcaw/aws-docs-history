# Troubleshoot VM issues

## Incremental Backups / CBT issues and messages

**Failure message:** `"The VMware Change Block Tracking (CBT) 
 data was invalid during this backup, but the incremental backup was successfully completed 
 with our proprietary change detection mechanism."`

If this message continues,
[reset CBT](https://knowledge.broadcom.com/external/article?legacyId=1020128 "https://knowledge.broadcom.com/external/article?legacyId=1020128") as directed by VMware.

**Message notes CBT was not turned on or was unavailable:**
_"VMware Change Block Tracking (CBT) was not available for this virtual machine, but
the incremental backup was successfully completed with our proprietary change mechanism."_

Check to make sure CBT is turned on. To verify if a virtual disk has CBT enabled:

1. Open the vSphere Client and select a powered-off virtual machine.
2. Right-click the virtual machine and navigate to
   **Edit Settings** > **Options** > **Advanced/General**
   > **Configuration Parameters**.
3. The option `ctkEnabled` needs to equal `True`.

If it is turned on, ensure you are using up-to-date VMware features. The host must be ESXi
4.0 or later and the virtual machine owning the disks to be tracked must be hardware version
7 or later.

If CBT is turned on (enabled) and the software and hardware are up to date, turn off the virtual
machine and then turn it back on again. Ensure that CBT is turned on. Then, perform the backup again.

## VMware backup failure

When a VMware backup fails, it may be related to one of the following:

**Failure message:** `"Failed to process backup data. Aborted
 backup job."` or `"Error opening disk on the virtual
 machine"`.

**Possible causes:** This error may occur because of a
configuration issue; or, the VMware version or disk isn't supported.

**Remedy 1:** Ensure your infrastructure is configured to use a
gateway and ensure all required ports are open.

1. Access the [backup gateway console](../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common "../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common"). Note this is different from the AWS Backup
   console.
2. On the **Backup gateway configuration** page enter option
   **3** to test the network connectivity.
3. If the network test is successful, enter **X**.
4. Return to the Backup gateway configuration page.
5. Enter **7** to access the command prompt.
6. Run the following commands to verify network connectivity:

`ncport -d `ESXi Host`-p 902`

`ncport -d `ESXi Host`-p 443`

**Remedy 2:** Use [Supported VMs](vm-backups.md#supported-vms "vm-backups.md#supported-vms") versions.

**Remedy 3:** If a gateway appliance is configured with incorrect
DNS servers, then the backup fails. To verify the DNS configuration, complete the
following steps:

1. Access the [backup gateway console](../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common "../../../storagegateway/latest/tgw/accessing-local-console.md#MaintenanceConsoleWindowVMware-common").
2. On the **Backup gateway configuration** page enter option
   **2** to navigate to the network configuration.
3. In **Network configuration**, enter **7** to
   view the DNS configuration.
4. Review the DNS server IP addresses. If the DNS server IP address are incorrect
   then exist the prompt to return to **Network
   Configuration**.
5. In **Network Configuration**, enter **6** to
   edit the DNS configuration.
6. Enter the correct DNS server IP addresses. Then, enter **X** to
   complete your network configuration.

To obtain more information about your hypervisor, such as errors and network
configuration and connection, see [Editing a hypervisor configuration](working-with-hypervisors.md#edit-hypervisor "working-with-hypervisors.md#edit-hypervisor") to configure the hypervisor to integrate with
Amazon CloudWatch Logs.

## Backup failures from network connection issues

**Failure message:** `"Failed to upload backup during data
 ingestion. Aborted backup job."` or `"Cloud network request timed out
 during data ingestion"`.

**Possible causes:** This error can occur if the network connection is insufficient to
handle data uploads. If network bandwidth is low, the link between the VM and AWS Backup can
become congested and cause backups to fail.

Required network bandwidth depends on several factors, including the size of the VM,
the incremental data generated for each VM backup, the backup window, and restore
requirements.

**Remedy:** Best practices and recommendations include having a minimum bandwidth of
1000 Mbps upload bandwidth for on-premises VMs connected to AWS Backup. Once the bandwidth is
confirmed, retry the backup job.

## Aborted backup job

**Failure message:**
`"Failed to create backup during snapshot creation. Aborted backup
 job."`

**Possible cause:** The VMware host where the gateway appliance resides may have an
issue.

**Remedy:** Check the configuration of your VMware host and review the it for issues.
For additional information, see [Editing a hypervisor configuration](working-with-hypervisors.md#edit-hypervisor "working-with-hypervisors.md#edit-hypervisor").

## No available gateways

**Failure message:** `"No gateways available to work on job."`

**Possible cause:** all connected gateways are busy with other jobs. Each gateway
has a limit of four concurrent jobs (backup or restore).

For **remedies**, see the next section for steps on increasing number
of gateways and steps to increase backup plan window time.

## VMware backup job failure

**Failure message:** `"Abort signal detected"`

**Possible causes:**

- **Low Network Bandwidth**: Insufficient network bandwidth can
  impede the completion of backups within the completion window. When the backup job
  requires more bandwidth than available, it can result in failure and trigger the
  "Abort Signal Detected" error.
- **Inadequate Number of Backup Gateways**: If the number of backup gateways is not
  sufficient to handle the backup rotation for all the configured VMs, the backup job
  may fail. This can occur when the backup plan's window for completing backups is too
  short or the number of backup gateways are not enough.
- Backup Plan completion window is too small.

**Remedies:**

**Increase bandwidth:** Consider increasing the network capacity
between AWS and the on-premises environment. This step will provide more bandwidth for
the backup process, allowing data to transfer smoothly without triggering the error. It
is recommended you have at least 100-Mbps bandwidth to AWS to backup on-premises
VMware VMs using AWS Backup.

If a bandwidth rate limit is configured for the backup gateway, it can restrict the
flow of data and lead to backup failures. Increasing the bandwidth rate limit to ensure
sufficient data transfer capacity may help reduce failures. This adjustment can mitigate
the occurrence of the "Abort Signal Detected" error. For more information, see [Backup gateway Bandwidth Throttling](working-with-gateways.md#backup-gateway-bandwidth-throttling "working-with-gateways.md#backup-gateway-bandwidth-throttling").

**Increase the number of Backup gateways:** A single backup gateway
can process up to 4 backup and restore jobs at a time. Additional jobs will queue and
wait for the gateway to free up until the backup start window passed. If the backup
window passes and the queued jobs have not started, those backup jobs will fail with
"abort signal detected". You can increase the number of backup gateways to alleviate the
number of failed jobs. See [Working with gateways](working-with-gateways.md "working-with-gateways.md") for more detail.

**Increase backup plan window time:** You can increase the
**complete within duration** of the backup window in your backup
plan. See [Backup plan options and
configuration](plan-options-and-configuration.md "plan-options-and-configuration.md") for more detail.

For help resolving these issues, see [AWS
Knowledge Center](https://repost.aws/knowledge-center/backup-troubleshoot-vmware-backups "https://repost.aws/knowledge-center/backup-troubleshoot-vmware-backups").



# Troubleshooting
<a name="troubleshooting"></a>

This chapter details some common issues encountered while creating or managing Amazon EVS environments.

## Broadcom and AWS Support guidance
<a name="broadcom-aws-support-guidance"></a>

 AWS provides support for Amazon EVS and its associated infrastructure services, including VMware Cloud Foundation (VCF). For VCF-specific configuration guidance, or issues related to other VMware products such as Aria Suite, HCX, or NSX, you can also contact Broadcom directly using your Broadcom support entitlement. For more information, see [Broadcom Support Portal](https://support.broadcom.com/).

## Troubleshoot failed environment status checks
<a name="troubleshoot-env-status"></a>

Amazon EVS performs automated checks on your environment to identify issues. You can view the status of your environment to identify specific and detectable problems.

### Review environment status check information
<a name="view-env-status"></a>

 **To investigate impaired environments using the Amazon EVS console** 

1. Open the Amazon EVS console.

1. In the navigation pane, choose **Environments**, and then select your environment.

1. Select the **Details** tab to see an overview of the environment.

1. Check the **Environment status**. Hover on this field to expand a popover with individual results for each environment status check.

### Reachability check failed
<a name="troubleshoot-reachability"></a>

The reachability check verifies that Amazon EVS has a persistent connection to SDDC Manager. If Amazon EVS cannot reach the environment, this check fails.

If this check fails, Amazon EVS can no longer reach SDDC Manager to validate the environment status, and hosts can no longer be added to the environment. Reachability failure will also cause the license key re-use and key coverage checks to fail, and the host count check to return an **Unknown** response.

To ensure reachability, check the following:
+ Ensure that your certificates are valid and unexpired. You can use the SDDC Manager UI or vSphere client to manage certificates in a VCF environment. After deployment, it is recommended that you replace all certificates of the VMware Cloud Foundation management domain. For more information, see [Managing Certificates in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/certificate-management-admin.html) in the VMware Cloud Foundation documentation.
+ Ensure that your DNS servers are reachable from the service access subnet, DNS records are valid, and no duplicate hostnames or IP addresses exist.
+ If you wish to create your own firewall rules, follow these guidelines:
  + Allow TCP/UDP access to the DNS servers.
  + Allow HTTPS/SSH access to the host management VLAN subnet.
  + Allow HTTPS/SSH access to the Management VM VLAN subnet.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

### Host count check failed
<a name="troubleshoot-host-count"></a>

This check verifies that your environment meets the minimum host count required by your VCF deployment topology.

If this check fails, add hosts so that your environment meets the minimum requirement. For minimum host counts by VCF version and deployment topology, see the [VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf.html).

### Key re-use check failed
<a name="troubleshoot-key-reuse"></a>

This check verifies that the VCF license key is not in use by another Amazon EVS environment. VCF licenses can be used for only one Amazon EVS environment. This check fails if you supply VCF license keys in an environment creation request that are already in use by another environment.

If this check fails, you receive an error response that the Amazon EVS environment could not be created. To address the issue, review your license settings in SDDC Manager and replace any previously used licenses with unused licenses.

**Important**  
Use the SDDC Manager user interface to manage VCF solution and vSAN license keys. Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly. While keys must be assigned to your hosts and vSAN cluster using the vSphere Client, you must make sure that those keys also appear in the licensing screen of the SDDC Manager user interface.

### Key coverage check failed
<a name="troubleshoot-key-coverage"></a>

This check verifies that your VCF license key assigned to vCenter Server allocates sufficient vCPU cores and vSAN storage capacity (TiB) for all deployed hosts.

If this check fails, you receive an error response that the Amazon EVS environment could not be created. Key coverage failure may indicate one of the following issues:
+ VCF licenses are not properly assigned to vCenter Server. You must assign a license to vCenter Server before its evaluation period expires or the currently assigned license expires. If this is the issue, review license assignments in SDDC Manager.
+ Current VCF licenses don’t cover vCPU core and vSAN storage capacity needs. The requirements for the VCF solution key (including minimum core count) and vSAN license key (including minimum vSAN capacity) vary depending on the instance type. For specific thresholds for your configuration, see [VCF subscriptions](vcf-license-mgmt.md). If this is the issue, add vSAN licenses in SDDC Manager until your usage needs are met.

If the above actions don’t resolve the issue, reach out to AWS Support for further assistance.

**Important**  
Use the SDDC Manager user interface to manage VCF solution and vSAN license keys. Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly. While keys must be assigned to your hosts and vSAN cluster using the vSphere Client, you must make sure that those keys also appear in the licensing screen of the SDDC Manager user interface.

## vSphere HA agent on this host could not reach isolation address
<a name="troubleshoot-vsphere-ha-agent-ipv6"></a>

In the vCenter user interface, with the ESX host selected, you see the message "vSphere HA agent on this host could not reach isolation address <IPv6 address>".

This error message indicates that the vSphere HA agent on a host is unable to reach the default IPv6 isolation address that vSphere HA uses for heartbeat checks. The error message is not indicative of a problem, and only occurs because Amazon EVS does not support IPv6 at this time. The absence of IPV6 support for Amazon EVS does not affect the core functionality of vSphere HA.

## vSAN upgrade prechecks fail for ESX host cluster
<a name="troubleshoot-vsan-precheck-fail"></a>

When attempting to upgrade the ESX host cluster using SDDC Manager, vSAN disk-related prechecks may fail. This is because Amazon EVS uses vSAN Express Storage Architecture (ESA), and the upgrade prechecks do not apply to vSAN ESA. For more information, see [the Broadcom knowledge base article on this topic](https://knowledge.broadcom.com/external/article/369423/upgrade-prechecks-fails-with-esxi-cluste.html).

## Add host failure due to incompatible cluster image
<a name="troubleshoot-cluster-image"></a>

 **Problem** 

When you add a host to your environment, the host has the latest available version of the EVS custom vendor add-on. If your environment uses hosts with an older add-on version, adding new hosts fails with an error that the new host is not compatible with your cluster image. To fix this issue, you must use vSphere Lifecyle Manager to extract the latest available add-on version from the newly added host.

 **Solution** 

Follow these steps.

1. Go to the Hosts and Clusters inventory in VMware vCenter Server.

1. Extract the add-on from the newly added host by creating a temporary empty cluster.

1. Under **Basics**, select **Import image from an existing host in the vCenter Inventory** and create the cluster. Leave all other settings as the default.

1. Once this temporary cluster is created with the extracted image, you can delete the temporary cluster. The add-on will now be available in your vSphere Lifecycle Manager depot.

1. Go to your environment cluster and select the **Updates** tab.

1. Edit your cluster image and change the add-on version to the newly extracted version.

1. Choose **Save**.

1. In SDDC Manager, retry the failed add host task. This will remediate your cluster hosts, updating all hosts to the latest add-on version. Cluster image remediation will require host reboots.

## SDDC Manager fails VCF host validation during host commissioning
<a name="troubleshoot-sddc-failure-host-commission"></a>

 **Problem** 

If you have updated your ESX version after the Amazon EVS environment deployment, SDDC manager may fail during VCF host validation in the commission hosts step. To fix this issue, you will have to use vSphere Lifecyle Manager to upgrade ESX on the newly added host.

 **Solution** 

Follow these steps.

**Important**  
These steps require temporarily adding the host to vCenter outside of SDDC Manager. Using vSphere Lifecyle Manager for any operations other than ESX upgrades may render your host unusable, and require you to delete and create a new Amazon EVS host.

1. Go to the Hosts and Clusters inventory in VMware vCenter Server.

1. Add the host temporarily to your virtual data center, ensuring to select **manage host with an image**. The host will be removed in a later step after the ESX upgrade is complete. For more information, see [How to Add a Host to Your vSphere Data Center or Folder](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/organizing-your-inventory-host-management/add-a-host-to-a-folder-or-a-data-center-host-management.html) in the vSphere documentation.

1. Once the host is added to vSphere, upgrade the ESX version on the host. This can be done in the **Updates** tab of your host. Edit the host image to match the ESX version of your cluster.

1. After the upgrade has completed, remove the host from your vCenter inventory. For more information, see [How to Remove an ESX Host from Your vCenter Server Instance](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/managing-hosts-in-vcenter-server-host-management/remove-a-host-from-vcenter-server-host-management.html) in the vSphere documentation.

1. Commission your host in SDDC manager. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the VMware Cloud Foundation documentation.

1. After the host is commissioned, add the host to your cluster using SDDC Manager.

## Windows Server entitlement status is At Risk due to appliance reachability failure
<a name="troubleshoot-entitlement-at-risk"></a>

An entitlement enters the at risk state when the associated Amazon EVS connector fails its reachability check for the VCF management appliance. For Windows Server entitlements, you have 8 hours from the point the entitlement reaches the at risk status to restore the connection. If the connection is not restored within this period, entitlements are automatically dropped and Windows Server usage tracking is stopped.

To resolve this issue, check the following:
+ Verify the connector state is Active and its reachability check status is Failed.
+ Verify that the appliance credentials stored in AWS Secrets Manager are current and correct. If the credentials have been rotated in the appliance, update the values in the existing Secrets Manager secret. If you need to point to a different secret, use UpdateEnvironmentConnector to update the secret identifier.
+ Ensure that your DNS servers are reachable from the service access subnet, DNS records for the appliance FQDN are valid, and no duplicate hostnames or IP addresses exist.
+ Verify that firewall rules allow HTTPS/SSH access to the management VM VLAN subnet and TCP/UDP access to DNS servers.
+ Ensure that the appliance is running and accessible.

Once the connection is restored, entitlements will automatically return to the healthy Created state. If entitlements have already been dropped and have the Entitlement Removed state, you must create new entitlements after the connector returns to an Active state with a passed reachability check.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

## Entitlement failed due to unsupported guest OS
<a name="troubleshoot-entitlement-unsupported-os"></a>

An entitlement creation fails or an existing entitlement is removed when Amazon EVS detects that the VM is running a guest operating system that is not supported for Amazon EVS Windows Server Licensing.

This can occur when:
+ A VM with an existing Windows Server entitlement is reconfigured to use an unsupported OS version or a non-Windows operating system.
+ An entitlement creation failed because of a VM that is already running an unsupported guest OS.

To resolve this issue:
+ Verify the connector state is Active and its reachability check status is Passed.
+ Verify the guest OS configured on the VM. Amazon EVS Windows Server Licensing supports Windows Server 2016 or later.
+ Reconfigure the VM to use a supported Windows Server version.
+ After updating the guest OS, create a new entitlement for the VM.
+ (**Optional**) Delete the entitlement in the Entitlement Removed state.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

## Entitlement status is entitlement removed
<a name="troubleshoot-entitlement-removed"></a>

An entitlement with the Entitlement Removed status indicates that Amazon EVS has removed the entitlement for the VM. When an entitlement is removed, Windows Server usage tracking stops for the affected VM.

This status can result from several causes:
+ Appliance reachability failure that exceeded the 8-hour grace period. See [Windows Server entitlement status is At Risk due to appliance reachability failure](#troubleshoot-entitlement-at-risk).
+ VM no longer present in the appliance inventory. See [Entitlement removed due to VM disconnect, isolated, or missing from inventory](#troubleshoot-entitlement-vm-disconnect).
+ VM became disconnected or isolated from its host. See [Entitlement removed due to VM disconnect, isolated, or missing from inventory](#troubleshoot-entitlement-vm-disconnect).
+ VM guest OS was changed to an unsupported version. See [Entitlement failed due to unsupported guest OS](#troubleshoot-entitlement-unsupported-os).

To restore entitlement:
+ Check the entitlement’s error details to identify the specific cause of the removal.
+ Resolve the underlying issue.
+ Create a new entitlement for the VM once the connector is in an Active state with a reachability check in a Passed state.
+ (**Optional**) Delete the entitlement in the Entitlement Removed state.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

## Entitlement removed due to VM disconnect, isolated, or missing from inventory
<a name="troubleshoot-entitlement-vm-disconnect"></a>

An entitlement is removed when Amazon EVS detects that a VM has become disconnected, isolated, or is no longer present in the appliance inventory. The entitlement is removed immediately and usage tracking is stopped.

To resolve this issue:
+ Verify the connector state is Active and its reachability check status is Passed.
+ Check the VM’s connection state in your appliance. A disconnected or isolated VM may indicate a host or network issue.
+ Resolve the underlying host or network issue causing the VM to be disconnected or isolated.
+ After the VM is reconnected and running normally, create a new entitlement to resume Windows Server usage.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.
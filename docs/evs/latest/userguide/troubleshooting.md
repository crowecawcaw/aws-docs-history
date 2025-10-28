# Troubleshooting

This chapter details some common issues encountered while creating or managing Amazon EVS environments.

## Troubleshoot failed environment status checks

Amazon EVS performs automated checks on your environment to identify issues.
You can view the status of your environment to identify specific and detectable problems.

### Review environment status check information

**To investigate impaired environments using the Amazon EVS console**

1. Open the Amazon EVS console.
2. In the navigation pane, choose **Environments**, and then select your environment.
3. Select the **Details** tab to see an overview of the environment.
4. Check the **Environment status**.
   Hover on this field to expand a popover with individual results for each environment status check.

### Reachability check failed

The reachability check verifies that Amazon EVS has a persistent connection to SDDC Manager.
If Amazon EVS cannot reach the environment, this check fails.

If this check fails, Amazon EVS can no longer reach SDDC Manager to validate the environment status, and hosts can no longer be added to the environment.
Reachability failure will also cause the license key re-use and key coverage checks to fail, and the host count check to return an **Unknown** response.

To ensure reachability, check the following:

- Ensure that your certificates are valid and unexpired.
  You can use the SDDC Manager UI or vSphere client to manage certificates in a VCF environment.
  After deployment, it is recommended that you replace all certificates of the VMware Cloud Foundation management domain.
  For more information, see [Managing Certificates in VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/certificate-management-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/certificate-management-admin.html") in the VMware Cloud Foundation documentation.
- Ensure that your DNS servers are reachable from the service access subnet, DNS records are valid, and no duplicate hostnames or IP addresses exist.
- If you wish to create your own firewall rules, follow these guidelines:
  - Allow TCP/UDP access to the DNS servers.
  - Allow HTTPS/SSH access to the host management VLAN subnet.
  - Allow HTTPS/SSH access to the Management VM VLAN subnet.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

### Host count check failed

This check verifies that your environment has a minimum of four hosts, which is a requirement for VCF 5.2.1.

If this check fails, you will need to add hosts so that your environment meets this minimum requirement.
Amazon EVS only supports environments with 4 to 16 hosts.

### Key re-use check failed

This check verifies that the VCF license key is not in use by another Amazon EVS environment.
VCF licenses can be used for only one Amazon EVS environment.
This check fails if you supply VCF license keys in an environment creation request that are already in use by another environment.

If this check fails, you receive an error response that the Amazon EVS environment could not be created.
To address the issue, review your license settings in SDDC Manager and replace any previously used licenses with unused licenses.

###### Important

Use the SDDC Manager user interface to manage VCF solution and vSAN license keys.
Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly.
While keys must be assigned to your hosts and vSAN cluster using the vSphere Client, you must make sure that those keys also appear in the licensing screen of the SDDC Manager user interface.

### Key coverage check failed

This check verifies that your VCF license key assigned to vCenter Server allocates sufficient vCPU cores and vSAN storage capacity (TiB) for all deployed hosts.

If this check fails, you receive an error response that the Amazon EVS environment could not be created.
Key coverage failure may indicate one of the following issues:

- VCF licenses are not properly assigned to vCenter Server.
  You must assign a license to vCenter Server before its evaluation period expires or the currently assigned license expires.
  If this is the issue, review license assignments in SDDC Manager.
- Current VCF licenses don’t cover vCPU core and vSAN storage capacity needs.
  The VCF solution key must have at least 256 cores.
  The vSAN license key must have at least 110 TiB of vSAN capacity.
  If this is the issue, add vSAN licenses in SDDC Manager until your usage needs are met.

If the above actions don’t resolve the issue, reach out to AWS Support for further assistance.

###### Important

Use the SDDC Manager user interface to manage VCF solution and vSAN license keys.
Amazon EVS requires that you maintain valid VCF solution and vSAN license keys in SDDC Manager for the service to function properly.
While keys must be assigned to your hosts and vSAN cluster using the vSphere Client, you must make sure that those keys also appear in the licensing screen of the SDDC Manager user interface.

## vSphere HA agent on this host could not reach isolation address

In the vCenter user interface, with the ESXi host selected, you see the message "vSphere HA agent on this host could not reach isolation address <IPv6 address>".

This error message indicates that the vSphere HA agent on a host is unable to reach the default IPv6 isolation address that vSphere HA uses for heartbeat checks.
The error message is not indicative of a problem, and only occurs because Amazon EVS does not support IPv6 at this time.
The absence of IPV6 support for Amazon EVS does not affect the core functionality of vSphere HA.

## vSAN upgrade prechecks fail for ESXi host cluster

When attempting to upgrade the ESXi host cluster using SDDC Manager, vSAN disk-related prechecks may fail.
This is because Amazon EVS uses vSAN Express Storage Architecture (ESA), and the upgrade prechecks do not apply to vSAN ESA.
For more information, see [the Broadcom knowledge base article on this topic](https://knowledge.broadcom.com/external/article/369423/upgrade-prechecks-fails-with-esxi-cluste.html "https://knowledge.broadcom.com/external/article/369423/upgrade-prechecks-fails-with-esxi-cluste.html").

## Add host failure due to incompatible cluster image

**Problem**

When you add a host to your environment, the host has the latest available version of the EVS custom vendor add-on.
If your environment uses hosts with an older add-on version, adding new hosts fails with an error that the new host is not compatible with your cluster image.
To fix this issue, you must use vSphere Lifecyle Manager to extract the latest available add-on version from the newly added host.

**Solution**

Follow these steps.

1. Go to the Hosts and Clusters inventory in VMware vCenter Server.
2. Extract the add-on from the newly added host by creating a temporary empty cluster.
3. Under **Basics**, select **Import image from an existing host in the vCenter Inventory** and create the cluster.
   Leave all other settings as the default.
4. Once this temporary cluster is created with the extracted image, you can delete the temporary cluster.
   The add-on will now be available in your vSphere Lifecycle Manager depot.
5. Go to your environment cluster and select the **Updates** tab.
6. Edit your cluster image and change the add-on version to the newly extracted version.
7. Choose **Save**.
8. In SDDC Manager, retry the failed add host task.
   This will remediate your cluster hosts, updating all hosts to the latest add-on version.
   Cluster image remediation will require host reboots.

## SDDC Manager fails VCF host validation during host commissioning

**Problem**

If you have updated your ESXi version after the Amazon EVS environment deployment, SDDC manager may fail
during VCF host validation in the commission hosts step.
To fix this issue, you will have to use vSphere Lifecyle Manager to upgrade ESXi on the newly added host.

**Solution**

Follow these steps.

###### Important

These steps require temporarily adding the host to vCenter outside of SDDC Manager.
Using vSphere Lifecyle Manager for any operations other than ESXi upgrades may render your host unusable, and require you to delete and create a new Amazon EVS host.

1. Go to the Hosts and Clusters inventory in VMware vCenter Server.
2. Add the host temporarily to your virtual data center, ensuring to select **manage host with an image**.
   The host will be removed in a later step after the ESXi upgrade is complete.
   For more information, see [How to Add a Host to Your vSphere Data Center or Folder](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/organizing-your-inventory-host-management/add-a-host-to-a-folder-or-a-data-center-host-management.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/organizing-your-inventory-host-management/add-a-host-to-a-folder-or-a-data-center-host-management.html") in the vSphere documentation.
3. Once the host is added to vSphere, upgrade the ESX version on the host.
   This can be done in the **Updates** tab of your host.
   Edit the host image to match the ESX version of your cluster.
4. After the upgrade has completed, remove the host from your vCenter inventory.
   For more information, see [How to Remove an ESXi Host from Your vCenter Server Instance](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/managing-hosts-in-vcenter-server-host-management/remove-a-host-from-vcenter-server-host-management.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/managing-hosts-in-vcenter-server-host-management/remove-a-host-from-vcenter-server-host-management.html") in the vSphere documentation.
5. Commission your host in SDDC manager.
   For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html") in the VMware Cloud Foundation documentation.
6. After the host is commissioned, add the host to your cluster using SDDC Manager.
